# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-17 15:01:22**
- 데이터 기준일(일봉): **2026-09-17**
- 데이터 기준일(주봉): **2026-09-14**
- VXN 기준일: **2026-09-16** / source: `FRED: VXNCLS`

## Verdict

**✅ QLD/TIGER 레버리지 매수 허용**
- Regime: **A: QLD 본격 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,200,000원** (60%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **800,000원** (40%)
- 대기자금: **0원** (0%)

## Weekly gate: 큰 환경

- QQQ close: 715.03
- Weekly RSI14: **57.46**
- 52W MA: 650.61 / gap: **9.90%**
- 104W MA gap: **22.64%**
- 52W MA 13W slope: **5.90%**
- VXN: **22.44** / 5D change: 0.12

## Daily trigger: 실제 매수 타이밍

- QQQ close: 715.03
- Daily RSI14: **51.86**
- 20D gap: **0.34%**
- 50D gap: **0.72%**
- 200D gap: **8.14%**
- MACD hist: -0.8283 / change: 0.5990
- ATR14%: **1.31%**
- 20D high drawdown: **-0.84%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
