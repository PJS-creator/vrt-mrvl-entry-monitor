# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-11 03:06:20**
- 데이터 기준일(일봉): **2026-06-10**
- 데이터 기준일(주봉): **2026-06-08**
- VXN 기준일: **2026-06-10** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 693.69
- Weekly RSI14: **62.04**
- 52W MA: 610.31 / gap: **13.66%**
- 104W MA gap: **26.04%**
- 52W MA 13W slope: **7.83%**
- VXN: **32.68** / 5D change: 8.84

## Daily trigger: 실제 매수 타이밍

- QQQ close: 693.69
- Daily RSI14: **43.42**
- 20D gap: **-3.83%**
- 50D gap: **2.58%**
- 200D gap: **11.35%**
- MACD hist: -7.0065 / change: -1.5019
- ATR14%: **2.10%**
- 20D high drawdown: **-7.03%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
