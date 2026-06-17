# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-17 03:01:09**
- 데이터 기준일(일봉): **2026-06-16**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-15** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 729.86
- Weekly RSI14: **69.39**
- 52W MA: 614.79 / gap: **18.72%**
- 104W MA gap: **31.97%**
- 52W MA 13W slope: **8.25%**
- VXN: **25.92** / 5D change: -1.20

## Daily trigger: 실제 매수 타이밍

- QQQ close: 729.86
- Daily RSI14: **56.35**
- 20D gap: **0.75%**
- 50D gap: **6.11%**
- 200D gap: **16.57%**
- MACD hist: -2.5860 / change: 0.5162
- ATR14%: **2.14%**
- 20D high drawdown: **-2.18%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
