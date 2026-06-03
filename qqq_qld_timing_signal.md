# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-03 03:07:43**
- 데이터 기준일(일봉): **2026-06-02**
- 데이터 기준일(주봉): **2026-06-01**
- VXN 기준일: **2026-06-02** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 746.16
- Weekly RSI14: **78.27**
- 52W MA: 607.85 / gap: **22.75%**
- 104W MA gap: **36.00%**
- 52W MA 13W slope: **7.83%**
- VXN: **23.27** / 5D change: -0.63

## Daily trigger: 실제 매수 타이밍

- QQQ close: 746.16
- Daily RSI14: **79.37**
- 20D gap: **4.19%**
- 50D gap: **13.19%**
- 200D gap: **20.64%**
- MACD hist: 0.3783 / change: 0.1428
- ATR14%: **1.35%**
- 20D high drawdown: **0.00%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
