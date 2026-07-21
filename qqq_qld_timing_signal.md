# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-21 03:01:10**
- 데이터 기준일(일봉): **2026-07-20**
- 데이터 기준일(주봉): **2026-07-20**
- VXN 기준일: **2026-07-17** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 696.06
- Weekly RSI14: **56.27**
- 52W MA: 629.06 / gap: **10.65%**
- 104W MA gap: **23.48%**
- 52W MA 13W slope: **7.88%**
- VXN: **29.03** / 5D change: 4.14

## Daily trigger: 실제 매수 타이밍

- QQQ close: 696.06
- Daily RSI14: **42.40**
- 20D gap: **-2.80%**
- 50D gap: **-3.13%**
- 200D gap: **8.76%**
- MACD hist: -3.2542 / change: -0.4399
- ATR14%: **2.15%**
- 20D high drawdown: **-5.68%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
