# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-16 15:01:09**
- 데이터 기준일(일봉): **2026-08-14**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-13** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 731.07
- Weekly RSI14: **62.31**
- 52W MA: 637.38 / gap: **14.70%**
- 104W MA gap: **28.01%**
- 52W MA 13W slope: **7.17%**
- VXN: **21.23** / 5D change: -2.72

## Daily trigger: 실제 매수 타이밍

- QQQ close: 731.07
- Daily RSI14: **59.60**
- 20D gap: **3.83%**
- 50D gap: **2.57%**
- 200D gap: **12.55%**
- MACD hist: 4.3638 / change: -0.1172
- ATR14%: **1.73%**
- 20D high drawdown: **-0.14%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
