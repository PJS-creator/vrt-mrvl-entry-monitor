# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-23 15:01:24**
- 데이터 기준일(일봉): **2026-06-23**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 719.55
- Weekly RSI14: **64.53**
- 52W MA: 617.69 / gap: **16.49%**
- 104W MA gap: **29.67%**
- 52W MA 13W slope: **8.52%**
- VXN: **27.67** / 5D change: 0.40

## Daily trigger: 실제 매수 타이밍

- QQQ close: 719.59
- Daily RSI14: **51.04**
- 20D gap: **-1.08%**
- 50D gap: **3.22%**
- 200D gap: **14.46%**
- MACD hist: -1.8902 / change: -0.8642
- ATR14%: **2.24%**
- 20D high drawdown: **-3.45%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
