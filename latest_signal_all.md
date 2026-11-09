# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-09 03:01:17**
- 데이터 기준일(일봉): **2026-11-06**
- 데이터 기준일(주봉): **2026-11-02**
- VXN 기준일: **2026-11-05** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 656.10
- Weekly RSI14: **39.53**
- 52W MA: 665.01 / gap: **-1.34%**
- 104W MA gap: **9.77%**
- 52W MA 13W slope: **4.94%**
- VXN: **38.26** / 5D change: 13.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 656.10
- Daily RSI14: **31.40**
- 20D gap: **-7.28%**
- 50D gap: **-8.97%**
- 200D gap: **-3.49%**
- MACD hist: -6.6609 / change: -0.4216
- ATR14%: **2.36%**
- 20D high drawdown: **-12.06%**

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

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-09 03:00:51**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.48 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 2.6 / 4주 변화 -27.0 bp
- VIX (VIXCLS): 28.18
- NFCI: -0.459

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.549427
- MA60: 8.254273
- gap: -20.65%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.304337
- MA60: 0.412709
- gap: -26.26%
- MA60_slope_proxy: 0.015054
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-09 03:00:53**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 138.64 bp / 4주 변화 -24.88 bp
- CURVE_10s5s: 35.69 bp / 4주 변화 -8.55 bp

## NWG Price
- close: 587.4
- MA50: 662.756 / gap50: -11.37%
- MA200: 633.7156 / gap200: -7.31%

## Relative Strength
- RS vs FTSE gap: -11.69% / slope_proxy: -0.001793
- RS vs Peers gap: -2.34% / slope_proxy: 0.017197

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-09 03:01:02**

## Commodity Regime

- WTI ref (CL=F): 91.11 / 5D -5.55%
- Brent ref (BZ=F): 98.18 / 5D -6.29%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.07
- Gas ref (NG=F): 3.02 / 5D 5.88%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 56.38
- MA20 / MA60 / MA200: 61.51 / 59.90 / 56.09
- gap20 / gap60: -8.34% / -5.88%
- 5D return: -11.91%
- 20D high/low: 64.17 / 56.36

### Relative Strength

- ratio: 0.914963
- ratio_MA60: 0.928076
- ratio_gap: -1.41%
- ratio_slope_proxy(20d): -0.013627

### Volume (if available)

- volume: 9022200.00
- volume_MA20: 9112790.00
- volume_ratio: 0.99

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.53
- MA20 / MA60 / MA200: 23.34 / 21.44 / 18.83
- gap20 / gap60: -20.61% / -13.59%
- 5D return: -15.96%
- 20D high/low: 26.16 / 18.53

### Relative Strength

- ratio: 0.579425
- ratio_MA60: 0.571814
- ratio_gap: 1.33%
- ratio_slope_proxy(20d): 0.039817

### Volume (if available)

- volume: 17153700.00
- volume_MA20: 26771850.00
- volume_ratio: 0.64

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.24
- MA20 / MA60 / MA200: 5.97 / 5.75 / 5.89
- gap20 / gap60: -12.26% / -8.87%
- 5D return: -24.50%
- 20D high/low: 6.94 / 5.10

### Relative Strength

- ratio: 0.014713
- ratio_MA60: 0.014382
- ratio_gap: 2.30%
- ratio_slope_proxy(20d): 0.000599

### Volume (if available)

- volume: 37007400.00
- volume_MA20: 47544740.00
- volume_ratio: 0.78

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.53
- MA20 / MA60 / MA200: 13.15 / 13.70 / 12.75
- gap20 / gap60: -12.30% / -15.87%
- 5D return: -22.04%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041482
- ratio_MA60: 0.048605
- ratio_gap: -14.66%
- ratio_slope_proxy(20d): -0.002286

### Volume (if available)

- volume: 12346300.00
- volume_MA20: 17231560.00
- volume_ratio: 0.72

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-08**
- 실행시간(UTC): **2026-11-09 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.48
- IG OAS 4주 변화: 11.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.6
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 4.41% / slope_proxy: 0.004901
- GDXJ/GLD gap: -2.97% / slope_proxy: 0.002828

## VZLA (Vizsla Silver)
- close: 3.3 | RSI14: 48.773418 | ATR14%: 6.07%
- MA20 gap: 2.33% | MA50 gap: -8.73% | MA200 gap: -10.10%
- vol_ratio(Volume/Vol20): 0.827751 | gap_open: 0.63%
- RS vs SILJ gap: 1.88% / slope_proxy: 0.000578
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 7.52 | RSI14: 46.410472 | ATR14%: 7.10%
- MA20 gap: -1.81% | MA50 gap: -12.56% | MA200 gap: -13.31%
- vol_ratio(Volume/Vol20): 0.677489 | gap_open: 1.44%
- SilverMarginGate: SI=53.139999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.57% / slope_proxy: 0.013117
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
- close: 18.77 | RSI14: 55.562341 | ATR14%: 7.47%
- MA20 gap: 11.06% | MA50 gap: -2.69% | MA200 gap: -36.34%
- vol_ratio(Volume/Vol20): 1.286552 | gap_open: 1.82%
- RS vs SILJ gap: 4.44% / slope_proxy: -0.052245
- RS vs GDXJ gap: -0.19% / slope_proxy: -0.01755
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

- 실행시간(UTC): **2026-11-09 03:01:16**
- 데이터 기준일(주가): **2026-11-06**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **False**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.48 / 4주 변화 0.33 bp-ish / 2026-11-05
- IG OAS: 0.93 / 4주 변화 0.11 bp-ish / 2026-11-05
- 10Y Real Yield: 2.60 / 4주 변화 -0.32 bp-ish / 2026-11-05
- VIX: 28.18 / 4주 변화 12.77 / 2026-11-05
- NFCI: -0.46 / 4주 변화 0.04 / 2026-10-30

### Leadership ratios

- GDX/GLD: gap 0.86% / slope_proxy 1.51%
- GDXJ/GLD: gap -2.97% / slope_proxy -2.12%
- SILJ/SLV: gap 4.41% / slope_proxy 6.31%
- Gold breadth proxy: above50 38.46%, above200 38.46%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.57 | RSI14: 33.00 | ATR14%: 6.19%
- MA20/50/200 gap: -5.64% / -19.16% / -18.99%
- 5D return: 6.50% | 20D drawdown: -20.20% | vol_ratio: 1.21
- RS vs GDXJ: gap -13.38% / slope_proxy -15.25%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **52.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.04 | RSI14: 36.09 | ATR14%: 5.05%
- MA20/50/200 gap: -2.59% / -12.57% / -0.90%
- 5D return: 7.34% | 20D drawdown: -12.51% | vol_ratio: 0.79
- RS vs GDXJ: gap -7.55% / slope_proxy -8.31%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **49.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.81 | RSI14: 30.56 | ATR14%: 7.67%
- MA20/50/200 gap: -7.95% / -29.42% / -42.02%
- 5D return: 3.85% | 20D drawdown: -20.59% | vol_ratio: 0.63
- RS vs GDXJ: gap -27.22% / slope_proxy -15.66%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **41.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.66 | RSI14: 33.03 | ATR14%: 8.39%
- MA20/50/200 gap: -9.29% / -25.74% / -15.80%
- 5D return: 8.50% | 20D drawdown: -24.55% | vol_ratio: 0.28
- RS vs GDXJ: gap -20.35% / slope_proxy -19.86%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **35.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 25.37 | RSI14: 45.46 | ATR14%: 6.33%
- MA20/50/200 gap: 1.18% / -5.09% / 20.76%
- 5D return: 10.21% | 20D drawdown: -4.87% | vol_ratio: 0.90
- RS vs SILJ: gap 6.61% / slope_proxy 4.62%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **57.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.30 | RSI14: 53.57 | ATR14%: 6.24%
- MA20/50/200 gap: 2.33% / -8.73% / -10.10%
- 5D return: 7.84% | 20D drawdown: -5.71% | vol_ratio: 0.83
- RS vs SILJ: gap 1.88% / slope_proxy 2.84%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **51.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 18.77 | RSI14: 60.62 | ATR14%: 7.38%
- MA20/50/200 gap: 11.06% / -2.69% / -36.34%
- 5D return: 14.31% | 20D drawdown: 0.00% | vol_ratio: 1.29
- RS vs SILJ: gap 4.44% / slope_proxy 12.06%
- FundamentalScore: 42 | TechnicalScore: 75 | RegimeScore: 25 | OverallScore: **50.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.84 | RSI14: 44.44 | ATR14%: 6.20%
- MA20/50/200 gap: 0.00% / -12.73% / -18.65%
- 5D return: 8.74% | 20D drawdown: -8.20% | vol_ratio: 0.90
- RS vs SILJ: gap -3.96% / slope_proxy 0.14%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **47.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.09 | RSI14: 33.81 | ATR14%: 8.02%
- MA20/50/200 gap: -7.55% / -27.30% / -44.75%
- 5D return: 7.67% | 20D drawdown: -26.43% | vol_ratio: 1.02
- RS vs SILJ: gap -20.35% / slope_proxy -19.75%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **46.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.74 | RSI14: 47.71 | ATR14%: 5.78%
- MA20/50/200 gap: 0.16% / -13.53% / -19.48%
- 5D return: 8.94% | 20D drawdown: -12.47% | vol_ratio: 0.93
- RS vs SILJ: gap -4.63% / slope_proxy -4.53%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **45.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.52 | RSI14: 40.54 | ATR14%: 7.01%
- MA20/50/200 gap: -1.81% / -12.56% / -13.31%
- 5D return: 11.08% | 20D drawdown: -15.41% | vol_ratio: 0.68
- RS vs SILJ: gap -2.57% / slope_proxy -7.73%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **43.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.65 | RSI14: 37.27 | ATR14%: 6.33%
- MA20/50/200 gap: -3.93% / -18.78% / -31.74%
- 5D return: 7.14% | 20D drawdown: -13.89% | vol_ratio: 0.99
- RS vs SILJ: gap -11.65% / slope_proxy -6.07%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **37.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
