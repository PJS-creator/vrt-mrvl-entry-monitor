# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-09 23:03:30**
- 데이터 기준일(일봉): **2026-08-07**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-08-06** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 723.03
- Weekly RSI14: **60.94**
- 52W MA: 634.37 / gap: **13.98%**
- 104W MA gap: **27.16%**
- 52W MA 13W slope: **7.32%**
- VXN: **23.95** / 5D change: -3.60

## Daily trigger: 실제 매수 타이밍

- QQQ close: 723.03
- Daily RSI14: **57.18**
- 20D gap: **3.24%**
- 50D gap: **1.22%**
- 200D gap: **11.80%**
- MACD hist: 4.4211 / change: 0.7086
- ATR14%: **2.07%**
- 20D high drawdown: **-0.11%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-07**
- 실행시간(UTC): **2026-08-09 23:03:06**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.43 / 4주 변화 12.0 bp
- VIX (VIXCLS): 15.15
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.568732
- MA60: 9.432505
- gap: -9.16%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.375356
- MA60: 0.389855
- gap: -3.72%
- MA60_slope_proxy: 0.013378
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-07**
- 실행시간(UTC): **2026-08-09 23:03:08**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 113.02 bp / 4주 변화 -7.43 bp
- CURVE_10s5s: 49.31 bp / 4주 변화 1.39 bp

## NWG Price
- close: 712.4
- MA50: 655.188 / gap50: 8.73%
- MA200: 617.8931 / gap200: 15.29%

## Relative Strength
- RS vs FTSE gap: 7.14% / slope_proxy: 0.002541
- RS vs Peers gap: 4.82% / slope_proxy: 0.004499

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-09 23:03:14**

## Commodity Regime

- WTI ref (CL=F): 78.81 / 5D -1.90%
- Brent ref (BZ=F): 84.39 / 5D 0.74%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.58
- Gas ref (NG=F): 2.72 / 5D -2.30%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 55.91
- MA20 / MA60 / MA200: 55.50 / 55.04 / 50.26
- gap20 / gap60: 0.74% / 1.58%
- 5D return: -2.03%
- 20D high/low: 57.60 / 53.65

### Relative Strength

- ratio: 0.972348
- ratio_MA60: 0.967990
- ratio_gap: 0.45%
- ratio_slope_proxy(20d): -0.014621

### Volume (if available)

- volume: 7680900.00
- volume_MA20: 8835100.00
- volume_ratio: 0.87

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.96
- MA20 / MA60 / MA200: 18.41 / 18.07 / 16.28
- gap20 / gap60: -2.47% / -0.64%
- 5D return: -7.42%
- 20D high/low: 19.40 / 17.47

### Relative Strength

- ratio: 0.508206
- ratio_MA60: 0.512595
- ratio_gap: -0.86%
- ratio_slope_proxy(20d): -0.005571

### Volume (if available)

- volume: 28527600.00
- volume_MA20: 14944430.00
- volume_ratio: 1.91

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.26
- MA20 / MA60 / MA200: 5.20 / 5.67 / 5.36
- gap20 / gap60: 1.23% / -7.26%
- 5D return: -1.13%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013547
- ratio_MA60: 0.014123
- ratio_gap: -4.08%
- ratio_slope_proxy(20d): -0.000451

### Volume (if available)

- volume: 29941800.00
- volume_MA20: 41904465.00
- volume_ratio: 0.71

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.26
- MA20 / MA60 / MA200: 13.42 / 12.67 / 10.79
- gap20 / gap60: -1.21% / 4.67%
- 5D return: -0.90%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.051769
- ratio_MA60: 0.051314
- ratio_gap: 0.89%
- ratio_slope_proxy(20d): 0.001160

### Volume (if available)

- volume: 8861600.00
- volume_MA20: 15465360.00
- volume_ratio: 0.57

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-09**
- 실행시간(UTC): **2026-08-09 23:03:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.43
- VIX: 15.15
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 10.05% / slope_proxy: 0.011398
- GDXJ/GLD gap: 9.75% / slope_proxy: -0.007025

## VZLA (Vizsla Silver)
- close: 3.74 | RSI14: 63.680119 | ATR14%: 5.23%
- MA20 gap: 14.22% | MA50 gap: 10.61% | MA200 gap: -8.55%
- vol_ratio(Volume/Vol20): 1.901828 | gap_open: 5.38%
- RS vs SILJ gap: 1.65% / slope_proxy: 0.006042
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.4 | RSI14: 70.094375 | ATR14%: 5.95%
- MA20 gap: 25.73% | MA50 gap: 22.79% | MA200 gap: -0.61%
- vol_ratio(Volume/Vol20): 1.225569 | gap_open: 6.21%
- SilverMarginGate: SI=63.880001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.60% / slope_proxy: -0.004728
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 26.540001 | RSI14: 63.74979 | ATR14%: 7.08%
- MA20 gap: 26.48% | MA50 gap: 11.45% | MA200 gap: -5.72%
- vol_ratio(Volume/Vol20): 1.391651 | gap_open: 11.05%
- RS vs SILJ gap: -3.26% / slope_proxy: -0.145738
- RS vs GDXJ gap: -7.34% / slope_proxy: -0.036011
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-08-09 23:03:28**
- 데이터 기준일(주가): **2026-08-07**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 0.01 bp-ish / 2026-08-06
- IG OAS: 0.78 / 4주 변화 0.02 bp-ish / 2026-08-06
- 10Y Real Yield: 2.43 / 4주 변화 0.12 bp-ish / 2026-08-06
- VIX: 15.15 / 4주 변화 -0.69 / 2026-08-06
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 9.55% / slope_proxy 12.88%
- GDXJ/GLD: gap 9.75% / slope_proxy 13.59%
- SILJ/SLV: gap 10.05% / slope_proxy 7.06%
- Gold breadth proxy: above50 100.00%, above200 61.54%, count 13
- Silver breadth proxy: above50 100.00%, above200 38.46%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.54 | RSI14: 82.71 | ATR14%: 4.94%
- MA20/50/200 gap: 28.58% / 24.96% / 37.84%
- 5D return: 34.37% | 20D drawdown: 0.00% | vol_ratio: 3.12
- RS vs GDXJ: gap 9.40% / slope_proxy 6.88%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **77.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.12 | RSI14: 66.67 | ATR14%: 6.03%
- MA20/50/200 gap: 11.43% / 19.54% / 16.59%
- 5D return: 12.17% | 20D drawdown: 0.00% | vol_ratio: 2.23
- RS vs GDXJ: gap 2.95% / slope_proxy -13.48%
- FundamentalScore: 55 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **66.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.71 | RSI14: 85.77 | ATR14%: 5.31%
- MA20/50/200 gap: 24.09% / 20.12% / -1.84%
- 5D return: 22.00% | 20D drawdown: 0.00% | vol_ratio: 0.95
- RS vs GDXJ: gap 4.30% / slope_proxy 8.90%
- FundamentalScore: 82 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **60.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.45 | RSI14: 80.95 | ATR14%: 5.37%
- MA20/50/200 gap: 25.27% / 18.87% / -1.72%
- 5D return: 22.88% | 20D drawdown: 0.00% | vol_ratio: 1.58
- RS vs GDXJ: gap 3.81% / slope_proxy 6.00%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **60.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.19 | RSI14: 78.10 | ATR14%: 5.70%
- MA20/50/200 gap: 31.13% / 37.40% / 63.76%
- 5D return: 38.37% | 20D drawdown: 0.00% | vol_ratio: 1.30
- RS vs SILJ: gap 27.99% / slope_proxy 20.49%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.54 | RSI14: 72.17 | ATR14%: 5.65%
- MA20/50/200 gap: 18.89% / 14.47% / -0.09%
- 5D return: 26.86% | 20D drawdown: 0.00% | vol_ratio: 1.10
- RS vs SILJ: gap 3.36% / slope_proxy 3.10%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **65.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.88 | RSI14: 66.33 | ATR14%: 6.12%
- MA20/50/200 gap: 18.25% / 11.75% / 3.30%
- 5D return: 29.08% | 20D drawdown: 0.00% | vol_ratio: 1.66
- RS vs SILJ: gap 1.47% / slope_proxy 1.56%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **64.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.40 | RSI14: 77.99 | ATR14%: 6.08%
- MA20/50/200 gap: 25.73% / 22.79% / -0.61%
- 5D return: 30.03% | 20D drawdown: 0.00% | vol_ratio: 1.23
- RS vs SILJ: gap 9.60% / slope_proxy 12.08%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **62.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.74 | RSI14: 67.66 | ATR14%: 5.19%
- MA20/50/200 gap: 14.22% / 10.61% / -8.55%
- 5D return: 19.11% | 20D drawdown: 0.00% | vol_ratio: 1.90
- RS vs SILJ: gap 1.65% / slope_proxy 4.93%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **61.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.85 | RSI14: 64.68 | ATR14%: 5.57%
- MA20/50/200 gap: 11.29% / 8.20% / -8.16%
- 5D return: 19.33% | 20D drawdown: 0.00% | vol_ratio: 0.93
- RS vs SILJ: gap -2.07% / slope_proxy -6.38%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **55.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.01 | RSI14: 70.76 | ATR14%: 6.50%
- MA20/50/200 gap: 21.85% / 5.83% / -12.50%
- 5D return: 31.15% | 20D drawdown: 0.00% | vol_ratio: 1.27
- RS vs SILJ: gap -5.66% / slope_proxy 5.07%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 26.54 | RSI14: 74.75 | ATR14%: 6.68%
- MA20/50/200 gap: 26.48% / 11.45% / -5.72%
- 5D return: 35.89% | 20D drawdown: 0.00% | vol_ratio: 1.39
- RS vs SILJ: gap -3.26% / slope_proxy 10.07%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
