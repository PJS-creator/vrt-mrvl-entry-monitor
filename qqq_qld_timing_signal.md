# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-05-26 06:04:16**
- 데이터 기준일(일봉): **2026-05-22**
- 데이터 기준일(주봉): **2026-05-18**
- VXN 기준일: **2026-05-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 717.54
- Weekly RSI14: **74.70**
- 52W MA: 599.37 / gap: **19.71%**
- 104W MA gap: **32.13%**
- 52W MA 13W slope: **7.10%**
- VXN: **22.74** / 5D change: -1.34

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.54
- Daily RSI14: **71.38**
- 20D gap: **3.26%**
- 50D gap: **11.76%**
- 200D gap: **16.94%**
- MACD hist: -1.3572 / change: -0.0658
- ATR14%: **1.49%**
- 20D high drawdown: **-0.31%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
