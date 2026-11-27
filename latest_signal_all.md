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

- 실행시간(UTC): **2026-11-27 15:01:18**
- 데이터 기준일(일봉): **2026-11-27**
- 데이터 기준일(주봉): **2026-11-23**
- VXN 기준일: **2026-11-25** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 637.95
- Weekly RSI14: **40.92**
- 52W MA: 667.25 / gap: **-4.39%**
- 104W MA gap: **6.00%**
- 52W MA 13W slope: **3.88%**
- VXN: **38.53** / 5D change: 5.41

## Daily trigger: 실제 매수 타이밍

- QQQ close: 637.95
- Daily RSI14: **39.96**
- 20D gap: **-3.76%**
- 50D gap: **-9.57%**
- 200D gap: **-6.55%**
- MACD hist: -1.7623 / change: 0.7455
- ATR14%: **3.27%**
- 20D high drawdown: **-7.80%**

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

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 15:00:50**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.72 / 4주 변화 54.0 bp
- IG OAS (BAMLC0A0CM): 0.98 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.79 / 4주 변화 15.0 bp
- VIX (VIXCLS): 26.8
- NFCI: -0.444

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.638524
- MA60: 7.860603
- gap: -15.55%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.316369
- MA60: 0.391858
- gap: -19.26%
- MA60_slope_proxy: -0.025254
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 15:00:53**

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
- TERM_SPREAD_10Y_POLICY: 109.86 bp / 4주 변화 -46.01 bp
- CURVE_10s5s: 34.37 bp / 4주 변화 -0.36 bp

## NWG Price
- close: 599.11
- MA50: 632.0742 / gap50: -5.22%
- MA200: 629.6385 / gap200: -4.85%

## Relative Strength
- RS vs FTSE gap: -6.89% / slope_proxy: -0.002961
- RS vs Peers gap: 2.01% / slope_proxy: 0.00236

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-27 15:00:59**

## Commodity Regime

- WTI ref (CL=F): 84.04 / 5D 1.00%
- Brent ref (BZ=F): 91.21 / 5D -0.84%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.17
- Gas ref (NG=F): 3.52 / 5D 7.74%

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

- close: 54.42
- MA20 / MA60 / MA200: 56.60 / 58.95 / 56.84
- gap20 / gap60: -3.86% / -7.69%
- 5D return: 1.13%
- 20D high/low: 64.00 / 52.70

### Relative Strength

- ratio: 0.880440
- ratio_MA60: 0.915491
- ratio_gap: -3.83%
- ratio_slope_proxy(20d): -0.018197

### Volume (if available)

- volume: 759652.00
- volume_MA20: 11069342.60
- volume_ratio: 0.07

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.86
- MA20 / MA60 / MA200: 18.01 / 21.11 / 19.01
- gap20 / gap60: -6.40% / -20.15%
- 5D return: 3.50%
- 20D high/low: 22.05 / 15.67

### Relative Strength

- ratio: 0.505699
- ratio_MA60: 0.578262
- ratio_gap: -12.55%
- ratio_slope_proxy(20d): 0.018814

### Volume (if available)

- volume: 10645545.00
- volume_MA20: 22801377.25
- volume_ratio: 0.47

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

- close: 5.02
- MA20 / MA60 / MA200: 5.28 / 5.57 / 5.88
- gap20 / gap60: -4.97% / -9.81%
- 5D return: 5.24%
- 20D high/low: 6.94 / 4.64

### Relative Strength

- ratio: 0.014180
- ratio_MA60: 0.014460
- ratio_gap: -1.94%
- ratio_slope_proxy(20d): 0.000247

### Volume (if available)

- volume: 10817060.00
- volume_MA20: 41946843.00
- volume_ratio: 0.26

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

- close: 12.23
- MA20 / MA60 / MA200: 12.37 / 13.24 / 12.94
- gap20 / gap60: -1.09% / -7.58%
- 5D return: 0.87%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.039988
- ratio_MA60: 0.046389
- ratio_gap: -13.80%
- ratio_slope_proxy(20d): -0.003263

### Volume (if available)

- volume: 1168260.00
- volume_MA20: 13515583.00
- volume_ratio: 0.09

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.72
- IG OAS 4주 변화: 10.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.79
- VIX: 26.8
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 4.47% / slope_proxy: 0.000559
- GDXJ/GLD gap: -5.04% / slope_proxy: -0.010444

## VZLA (Vizsla Silver)
- close: 3.005 | RSI14: 48.188241 | ATR14%: 7.58%
- MA20 gap: -0.82% | MA50 gap: -9.95% | MA200 gap: -14.38%
- vol_ratio(Volume/Vol20): 0.115081 | gap_open: 4.55%
- RS vs SILJ gap: 8.19% / slope_proxy: 0.003509
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
- close: 8.0 | RSI14: 56.078616 | ATR14%: 8.13%
- MA20 gap: 12.25% | MA50 gap: 0.92% | MA200 gap: -3.20%
- vol_ratio(Volume/Vol20): 0.206104 | gap_open: 6.79%
- SilverMarginGate: SI=44.055 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 20.97% / slope_proxy: 0.007614
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

## HYMC (Hycroft Mining)
- close: 14.71 | RSI14: 44.236453 | ATR14%: 10.61%
- MA20 gap: -8.31% | MA50 gap: -15.84% | MA200 gap: -46.80%
- vol_ratio(Volume/Vol20): 0.167745 | gap_open: 8.09%
- RS vs SILJ gap: 0.50% / slope_proxy: -0.03916
- RS vs GDXJ gap: -3.46% / slope_proxy: -0.013718
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

- 실행시간(UTC): **2026-11-27 15:01:16**
- 데이터 기준일(주가): **2026-11-27**

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

- HY OAS: 3.72 / 4주 변화 0.54 bp-ish / 2026-11-24
- IG OAS: 0.98 / 4주 변화 0.10 bp-ish / 2026-11-24
- 10Y Real Yield: 2.79 / 4주 변화 0.13 bp-ish / 2026-11-24
- VIX: 26.80 / 4주 변화 9.60 / 2026-11-26
- NFCI: -0.44 / 4주 변화 0.07 / 2026-11-20

### Leadership ratios

- GDX/GLD: gap 0.12% / slope_proxy 6.37%
- GDXJ/GLD: gap -5.04% / slope_proxy 2.94%
- SILJ/SLV: gap 4.43% / slope_proxy 4.92%
- Gold breadth proxy: above50 7.69%, above200 7.69%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.91 | RSI14: 35.33 | ATR14%: 6.37%
- MA20/50/200 gap: -4.50% / -17.16% / -14.51%
- 5D return: 10.46% | 20D drawdown: -17.68% | vol_ratio: 0.15
- RS vs GDXJ: gap -4.59% / slope_proxy -4.10%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 3.81 | RSI14: 22.92 | ATR14%: 9.97%
- MA20/50/200 gap: -14.58% / -34.24% / -41.98%
- 5D return: 16.16% | 20D drawdown: -35.31% | vol_ratio: 0.14
- RS vs GDXJ: gap -25.82% / slope_proxy -24.33%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.62 | RSI14: 22.00 | ATR14%: 10.48%
- MA20/50/200 gap: -12.06% / -31.22% / -52.23%
- 5D return: 8.77% | 20D drawdown: -31.11% | vol_ratio: 0.36
- RS vs GDXJ: gap -25.48% / slope_proxy -17.44%
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
- close: 1.27 | RSI14: 26.55 | ATR14%: 11.08%
- MA20/50/200 gap: -13.69% / -32.16% / -34.06%
- 5D return: 11.40% | 20D drawdown: -29.44% | vol_ratio: 0.14
- RS vs GDXJ: gap -23.94% / slope_proxy -13.78%
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
- close: 21.52 | RSI14: 37.64 | ATR14%: 7.61%
- MA20/50/200 gap: -3.41% / -13.42% / 1.24%
- 5D return: 13.89% | 20D drawdown: -19.59% | vol_ratio: 0.38
- RS vs SILJ: gap 4.79% / slope_proxy 1.15%
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
- close: 3.01 | RSI14: 42.79 | ATR14%: 7.78%
- MA20/50/200 gap: -0.82% / -9.95% / -14.38%
- 5D return: 6.56% | 20D drawdown: -14.14% | vol_ratio: 0.12
- RS vs SILJ: gap 8.25% / slope_proxy 6.23%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.49 | RSI14: 35.79 | ATR14%: 7.85%
- MA20/50/200 gap: -8.53% / -18.65% / -29.92%
- 5D return: 6.74% | 20D drawdown: -22.18% | vol_ratio: 0.16
- RS vs SILJ: gap -3.65% / slope_proxy -2.63%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.01 | RSI14: 53.82 | ATR14%: 8.49%
- MA20/50/200 gap: 12.32% / 0.98% / -3.14%
- 5D return: 21.10% | 20D drawdown: -1.05% | vol_ratio: 0.21
- RS vs SILJ: gap 21.10% / slope_proxy 27.91%
- FundamentalScore: 74 | TechnicalScore: 25 | RegimeScore: 25 | OverallScore: **47.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 11.77 | RSI14: 31.36 | ATR14%: 6.98%
- MA20/50/200 gap: -8.73% / -21.35% / -32.47%
- 5D return: 5.55% | 20D drawdown: -23.63% | vol_ratio: 0.13
- RS vs SILJ: gap -6.78% / slope_proxy -5.90%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.07 | RSI14: 24.05 | ATR14%: 10.51%
- MA20/50/200 gap: -18.58% / -40.55% / -60.24%
- 5D return: 0.73% | 20D drawdown: -37.23% | vol_ratio: 0.30
- RS vs SILJ: gap -29.98% / slope_proxy -22.17%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **40.9**
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.93 | RSI14: 36.98 | ATR14%: 7.55%
- MA20/50/200 gap: -5.89% / -19.93% / -38.41%
- 5D return: 7.81% | 20D drawdown: -19.86% | vol_ratio: 0.19
- RS vs SILJ: gap -5.82% / slope_proxy -1.92%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 14.71 | RSI14: 36.02 | ATR14%: 11.50%
- MA20/50/200 gap: -8.31% / -15.84% / -46.80%
- 5D return: 6.75% | 20D drawdown: -30.84% | vol_ratio: 0.17
- RS vs SILJ: gap 0.55% / slope_proxy -3.09%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **29.2**
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
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
