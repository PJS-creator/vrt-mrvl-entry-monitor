# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-09 15:01:14**
- 데이터 기준일(일봉): **2026-09-09**
- 데이터 기준일(주봉): **2026-09-07**
- VXN 기준일: **2026-09-08** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 718.45
- Weekly RSI14: **58.50**
- 52W MA: 648.40 / gap: **10.80%**
- 104W MA gap: **23.70%**
- 52W MA 13W slope: **6.26%**
- VXN: **21.71** / 5D change: 1.53

## Daily trigger: 실제 매수 타이밍

- QQQ close: 718.45
- Daily RSI14: **53.26**
- 20D gap: **0.15%**
- 50D gap: **1.02%**
- 200D gap: **9.19%**
- MACD hist: 0.0485 / change: 0.1269
- ATR14%: **1.23%**
- 20D high drawdown: **-1.86%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.
