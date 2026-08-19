# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-19 15:01:28**
- 데이터 기준일(일봉): **2026-08-19**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-18** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 718.52
- Weekly RSI14: **58.85**
- 52W MA: 640.25 / gap: **12.22%**
- 104W MA gap: **25.30%**
- 52W MA 13W slope: **6.93%**
- VXN: **22.56** / 5D change: 0.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 718.52
- Daily RSI14: **52.67**
- 20D gap: **1.64%**
- 50D gap: **0.79%**
- 200D gap: **10.39%**
- MACD hist: 1.8179 / change: -0.8948
- ATR14%: **1.67%**
- 20D high drawdown: **-1.85%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
