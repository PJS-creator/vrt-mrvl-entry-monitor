from __future__ import annotations

import json
import math
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

START = pd.Timestamp('2010-02-11')
END = pd.Timestamp('2026-07-17')
TICKERS = ['QQQ', 'QLD', 'TQQQ', 'XLV', 'GLD']
PHASES = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
ROOT = Path(__file__).resolve().parents[1]
PHASE_FILE = ROOT / 'data' / 'k6_phase_intervals_min.csv'
OUT_DIR = ROOT / 'reports' / 'kostolany_k6_5ticker'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def get_adjusted_closes() -> pd.DataFrame:
    raw = yf.download(
        TICKERS,
        start=(START - pd.Timedelta(days=10)).strftime('%Y-%m-%d'),
        end=(END + pd.Timedelta(days=3)).strftime('%Y-%m-%d'),
        auto_adjust=False,
        actions=False,
        progress=False,
        group_by='column',
        threads=False,
    )
    if raw.empty:
        raise RuntimeError('yfinance returned an empty price panel')
    if isinstance(raw.columns, pd.MultiIndex):
        field = 'Adj Close' if 'Adj Close' in raw.columns.get_level_values(0) else 'Close'
        close = raw[field].copy()
    else:
        close = raw.copy()
    close.index = pd.to_datetime(close.index).tz_localize(None).normalize()
    close = close.reindex(columns=TICKERS).sort_index()
    close = close.loc[(close.index >= START) & (close.index <= END)]
    if close.empty:
        raise RuntimeError('No prices in requested analysis period')
    missing = close.isna().sum()
    if int(missing.sum()) > 0:
        raise RuntimeError(f'Missing adjusted closes: {missing.to_dict()}')
    return close


def load_effective_phase(price_index: pd.DatetimeIndex) -> pd.Series:
    intervals = pd.read_csv(PHASE_FILE)
    required = {'Episode_ID', 'Phase', 'Start', 'End'}
    if not required.issubset(intervals.columns):
        raise RuntimeError(f'Interval file missing columns: {sorted(required - set(intervals.columns))}')
    intervals['Start'] = pd.to_datetime(intervals['Start'])
    intervals['End'] = pd.to_datetime(intervals['End'])
    phase_at_close = pd.Series(index=price_index, dtype='object')
    for row in intervals.itertuples(index=False):
        mask = (price_index >= row.Start) & (price_index <= row.End)
        phase_at_close.loc[mask] = str(row.Phase).upper()
    invalid = sorted(set(phase_at_close.dropna()) - set(PHASES))
    if invalid:
        raise RuntimeError(f'Invalid K6 phases: {invalid}')
    # Phase confirmed at t close applies to the next completed trading session.
    return phase_at_close.shift(1)


def episode_ids(labels: pd.Series) -> pd.Series:
    return labels.ne(labels.shift()).cumsum()


def calculate(close: pd.DataFrame):
    returns = close.pct_change(fill_method=None)
    effective_phase = load_effective_phase(close.index)
    common = pd.DataFrame({'phase': effective_phase}).join(returns, how='inner')
    common = common.loc[(common.index >= START) & (common.index <= END)]
    common = common.dropna(subset=['phase'] + TICKERS)
    eids = episode_ids(common['phase'])

    summary_rows = []
    episode_rows = []
    for phase in PHASES:
        mask = common['phase'].eq(phase)
        phase_groups = common.loc[mask].groupby(eids[mask])
        for ticker in TICKERS:
            r = common.loc[mask, ticker].dropna()
            active_days = len(r)
            if active_days == 0:
                continue
            cumulative = float((1.0 + r).prod() - 1.0)
            ep_rets = []
            for eid, block in phase_groups:
                er = float((1.0 + block[ticker].dropna()).prod() - 1.0)
                ep_rets.append(er)
                episode_rows.append({
                    'phase': phase,
                    'episode_id': int(eid),
                    'ticker': ticker,
                    'start_date': block.index.min().date().isoformat(),
                    'end_date': block.index.max().date().isoformat(),
                    'trading_days': int(len(block)),
                    'episode_return': er,
                })
            ep = np.asarray(ep_rets, dtype=float)
            summary_rows.append({
                'phase': phase,
                'ticker': ticker,
                'active_days': int(active_days),
                'episodes': int(len(ep)),
                'cumulative_return': cumulative,
                'mean_episode_return': float(ep.mean()),
                'median_episode_return': float(np.median(ep)),
                'positive_episode_rate': float((ep > 0).mean()),
                'mean_daily_return': float(r.mean()),
                'median_daily_return': float(r.median()),
                'positive_day_rate': float((r > 0).mean()),
                'active_day_annualized_geometric_return': float((1.0 + cumulative) ** (252.0 / active_days) - 1.0),
                'annualized_volatility': float(r.std(ddof=1) * math.sqrt(252.0)),
            })

    summary = pd.DataFrame(summary_rows)
    episodes = pd.DataFrame(episode_rows)
    return common, summary, episodes


def pct(x: float, digits: int = 2) -> str:
    return f'{x * 100:,.{digits}f}%'


def markdown_matrix(summary: pd.DataFrame, field: str, digits: int = 2) -> str:
    m = summary.pivot(index='phase', columns='ticker', values=field).reindex(index=PHASES, columns=TICKERS)
    m = m.map(lambda x: pct(x, digits))
    return m.to_markdown()


def write_outputs(common: pd.DataFrame, summary: pd.DataFrame, episodes: pd.DataFrame):
    summary_csv = OUT_DIR / 'kostolany_k6_5ticker_phase_return_summary.csv'
    episodes_csv = OUT_DIR / 'kostolany_k6_5ticker_phase_episode_returns.csv'
    json_path = OUT_DIR / 'kostolany_k6_5ticker_phase_return_summary.json'
    report_path = OUT_DIR / 'KOSTOLANY_K6_5TICKER_RETURN_REPORT_KO.md'
    zip_path = OUT_DIR / 'KOSTOLANY_K6_5TICKER_RETURNS_BUNDLE.zip'

    summary.to_csv(summary_csv, index=False, encoding='utf-8-sig')
    episodes.to_csv(episodes_csv, index=False, encoding='utf-8-sig')
    payload = {
        'generated_at_utc': pd.Timestamp.utcnow().isoformat(),
        'analysis_period': {'start': str(START.date()), 'end': str(END.date())},
        'price_source': 'Yahoo Finance via yfinance; adjusted close',
        'alignment': 'K6 phase confirmed at t close, assigned to t+1 close-to-close return',
        'costs': 'none',
        'summary': summary.to_dict(orient='records'),
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')

    best_rows = []
    for phase in PHASES:
        sub = summary[summary['phase'].eq(phase)]
        bc = sub.loc[sub['cumulative_return'].idxmax()]
        ba = sub.loc[sub['mean_episode_return'].idxmax()]
        best_rows.append({
            '단계': phase,
            '누적수익률 1위': bc['ticker'],
            '누적수익률': pct(float(bc['cumulative_return'])),
            '평균 에피소드 1위': ba['ticker'],
            '평균 에피소드 수익률': pct(float(ba['mean_episode_return'])),
        })
    best = pd.DataFrame(best_rows)

    lines = [
        '# K6-PVLM 단계별 QQQ·QLD·TQQQ·XLV·GLD 수익률',
        '',
        f'- 분석기간: **{START.date()} ~ {END.date()}**',
        f'- 공통 계산 거래일: **{len(common):,}일**',
        '- 가격: Yahoo Finance 조정종가',
        '- 기본 정렬: t일 종가에 확정된 K6 단계를 t+1 종가-종가 수익률에 적용',
        '- 누적수익률: 해당 단계의 거래일만 보유하고 다른 단계는 수익률 0% 현금으로 가정하여 복리 연결',
        '- 평균수익률: 각 연속 단계 에피소드 누적수익률의 산술평균',
        '- 거래비용·슬리피지·세금 미반영',
        '',
        '## 누적수익률', '', markdown_matrix(summary, 'cumulative_return'), '',
        '## 평균 에피소드 수익률', '', markdown_matrix(summary, 'mean_episode_return'), '',
        '## 평균 일수익률', '', markdown_matrix(summary, 'mean_daily_return', 4), '',
        '## 단계별 1위', '', best.to_markdown(index=False), '',
        '## 주의', '',
        '- A2처럼 보유일 수가 긴 단계는 누적수익률이 구조적으로 커질 수 있으므로 평균 에피소드 수익률과 함께 봐야 한다.',
        '- B3는 에피소드 수가 적어 평균값의 불확실성이 크다.',
        '- 실제 다음 시가 체결 백테스트가 아니라 조정종가 기준의 단계별 조건부 성과분해다.',
    ]
    report_path.write_text('\n'.join(lines), encoding='utf-8')

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for p in [summary_csv, episodes_csv, json_path, report_path]:
            zf.write(p, arcname=p.name)

    print(report_path.read_text(encoding='utf-8'))
    for p in [summary_csv, episodes_csv, json_path, report_path, zip_path]:
        print(f'WROTE {p}')


def main():
    close = get_adjusted_closes()
    common, summary, episodes = calculate(close)
    if len(summary) != len(PHASES) * len(TICKERS):
        raise RuntimeError(f'Unexpected summary row count: {len(summary)}')
    write_outputs(common, summary, episodes)


if __name__ == '__main__':
    main()
