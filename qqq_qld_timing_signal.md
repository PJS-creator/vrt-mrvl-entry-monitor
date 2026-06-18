# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-18 03:01:04**
- 데이터 기준일(일봉): **2026-06-17**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-16** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 722.51
- Weekly RSI14: **68.29**
- 52W MA: 614.65 / gap: **17.55%**
- 104W MA gap: **30.65%**
- 52W MA 13W slope: **8.22%**
- VXN: **26.95** / 5D change: -2.83

## Daily trigger: 실제 매수 타이밍

- QQQ close: 722.51
- Daily RSI14: **53.38**
- 20D gap: **-0.41%**
- 50D gap: **4.64%**
- 200D gap: **15.26%**
- MACD hist: -2.7071 / change: -0.1212
- ATR14%: **2.15%**
- 20D high drawdown: **-3.17%**

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
