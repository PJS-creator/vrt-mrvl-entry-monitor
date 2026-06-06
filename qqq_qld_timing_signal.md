# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-06 15:08:01**
- 데이터 기준일(일봉): **2026-06-05**
- 데이터 기준일(주봉): **2026-06-01**
- VXN 기준일: **2026-06-05** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 705.06
- Weekly RSI14: **65.53**
- 52W MA: 607.05 / gap: **16.14%**
- 104W MA gap: **28.60%**
- 52W MA 13W slope: **7.69%**
- VXN: **30.47** / 5D change: 7.89

## Daily trigger: 실제 매수 타이밍

- QQQ close: 705.06
- Daily RSI14: **48.34**
- 20D gap: **-2.35%**
- 50D gap: **5.58%**
- 200D gap: **13.56%**
- MACD hist: -3.2766 / change: -2.8115
- ATR14%: **1.69%**
- 20D high drawdown: **-5.51%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
