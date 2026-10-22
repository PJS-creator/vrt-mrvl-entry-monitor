# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-22 00:52:39**
- 데이터 기준일(일봉): **2026-10-20**
- 데이터 기준일(주봉): **2026-10-19**
- VXN 기준일: **2026-10-21** / source: `Yahoo Finance ^VXN fallback; FRED error=Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 725.20
- Weekly RSI14: **55.61**
- 52W MA: 663.23 / gap: **9.34%**
- 104W MA gap: **21.99%**
- 52W MA 13W slope: **5.58%**
- VXN: **24.42** / 5D change: 1.72

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.63
- Daily RSI14: **40.90**
- 20D gap: **-3.01%**
- 50D gap: **-1.18%**
- 200D gap: **6.36%**
- MACD hist: -4.9900 / change: -0.0218
- ATR14%: **1.53%**
- 20D high drawdown: **-5.53%**

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
