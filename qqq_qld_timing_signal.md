# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-03 15:01:23**
- 데이터 기준일(일봉): **2026-11-03**
- 데이터 기준일(주봉): **2026-11-02**
- VXN 기준일: **2026-11-02** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 685.04
- Weekly RSI14: **45.63**
- 52W MA: 665.57 / gap: **2.93%**
- 104W MA gap: **14.56%**
- 52W MA 13W slope: **5.03%**
- VXN: **30.89** / 5D change: 4.49

## Daily trigger: 실제 매수 타이밍

- QQQ close: 685.03
- Daily RSI14: **34.50**
- 20D gap: **-4.95%**
- 50D gap: **-5.34%**
- 200D gap: **0.89%**
- MACD hist: -4.5910 / change: -0.2483
- ATR14%: **1.85%**
- 20D high drawdown: **-9.59%**

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
