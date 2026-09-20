# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-20 15:01:08**
- 데이터 기준일(일봉): **2026-09-18**
- 데이터 기준일(주봉): **2026-09-14**
- VXN 기준일: **2026-09-17** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 721.45
- Weekly RSI14: **58.92**
- 52W MA: 650.74 / gap: **10.87%**
- 104W MA gap: **23.73%**
- 52W MA 13W slope: **5.92%**
- VXN: **19.96** / 5D change: -3.37

## Daily trigger: 실제 매수 타이밍

- QQQ close: 721.45
- Daily RSI14: **55.87**
- 20D gap: **1.15%**
- 50D gap: **1.62%**
- 200D gap: **9.02%**
- MACD hist: 0.0683 / change: 0.7760
- ATR14%: **1.29%**
- 20D high drawdown: **0.00%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
