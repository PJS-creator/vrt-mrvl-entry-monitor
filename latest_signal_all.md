# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-31 01:46:51**
- 데이터 기준일(일봉): **2026-10-30**
- 데이터 기준일(주봉): **2026-10-26**
- VXN 기준일: **2026-10-29** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 690.49
- Weekly RSI14: **47.00**
- 52W MA: 664.07 / gap: **3.98%**
- 104W MA gap: **15.80%**
- 52W MA 13W slope: **5.27%**
- VXN: **25.18** / 5D change: -3.54

## Daily trigger: 실제 매수 타이밍

- QQQ close: 690.49
- Daily RSI14: **34.93**
- 20D gap: **-5.18%**
- 50D gap: **-4.72%**
- 200D gap: **1.79%**
- MACD hist: -3.1159 / change: -1.3113
- ATR14%: **1.84%**
- 20D high drawdown: **-9.11%**

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

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-10-30**
- 실행시간(UTC): **2026-10-31 01:46:26**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.26 / 4주 변화 2.0 bp
- IG OAS (BAMLC0A0CM): 0.89 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.63 / 4주 변화 -25.0 bp
- VIX (VIXCLS): 17.2
- NFCI: -0.487

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.271078
- MA60: 8.391833
- gap: -1.44%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.375892
- MA60: 0.417238
- gap: -9.91%
- MA60_slope_proxy: 0.026877
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-30**
- 실행시간(UTC): **2026-10-31 01:46:28**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 155.87 bp / 4주 변화 -6.27 bp
- CURVE_10s5s: 34.73 bp / 4주 변화 -10.17 bp

## NWG Price
- close: 635.2
- MA50: 674.104 / gap50: -5.77%
- MA200: 635.4886 / gap200: -0.05%

## Relative Strength
- RS vs FTSE gap: -6.50% / slope_proxy: -0.000779
- RS vs Peers gap: 5.38% / slope_proxy: 0.023742

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-31 01:46:34**

## Commodity Regime

- WTI ref (CL=F): 102.95 / 5D -0.31%
- Brent ref (BZ=F): 112.33 / 5D -3.76%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.38
- Gas ref (NG=F): 2.88 / 5D 9.20%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 64.00
- MA20 / MA60 / MA200: 61.71 / 59.86 / 55.70
- gap20 / gap60: 3.71% / 6.92%
- 5D return: -0.26%
- 20D high/low: 64.17 / 58.21

### Relative Strength

- ratio: 0.914025
- ratio_MA60: 0.932841
- ratio_gap: -2.02%
- ratio_slope_proxy(20d): -0.011915

### Volume (if available)

- volume: 9112500.00
- volume_MA20: 8406065.00
- volume_ratio: 1.08

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 22.05
- MA20 / MA60 / MA200: 24.48 / 21.25 / 18.65
- gap20 / gap60: -9.92% / 3.78%
- 5D return: -15.71%
- 20D high/low: 26.16 / 21.90

### Relative Strength

- ratio: 0.679298
- ratio_MA60: 0.562396
- ratio_gap: 20.79%
- ratio_slope_proxy(20d): 0.037662

### Volume (if available)

- volume: 24223600.00
- volume_MA20: 30203620.00
- volume_ratio: 0.80

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.94
- MA20 / MA60 / MA200: 5.94 / 5.75 / 5.86
- gap20 / gap60: 16.76% / 20.59%
- 5D return: 8.27%
- 20D high/low: 6.94 / 5.39

### Relative Strength

- ratio: 0.016862
- ratio_MA60: 0.014275
- ratio_gap: 18.13%
- ratio_slope_proxy(20d): 0.000520

### Volume (if available)

- volume: 47678200.00
- volume_MA20: 42551470.00
- volume_ratio: 1.12

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.79
- MA20 / MA60 / MA200: 13.42 / 13.82 / 12.66
- gap20 / gap60: 10.18% / 7.02%
- 5D return: 5.64%
- 20D high/low: 14.79 / 12.50

### Relative Strength

- ratio: 0.044775
- ratio_MA60: 0.049436
- ratio_gap: -9.43%
- ratio_slope_proxy(20d): -0.001558

### Volume (if available)

- volume: 23467100.00
- volume_MA20: 14851465.00
- volume_ratio: 1.58

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-30**
- 실행시간(UTC): **2026-10-31 01:46:38**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.26
- IG OAS 4주 변화: 3.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.63
- VIX: 17.2
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -0.40% / slope_proxy: 0.006224
- GDXJ/GLD gap: -10.90% / slope_proxy: 0.007255

## VZLA (Vizsla Silver)
- close: 3.06 | RSI14: 36.901679 | ATR14%: 6.16%
- MA20 gap: -7.44% | MA50 gap: -17.32% | MA200 gap: -18.33%
- vol_ratio(Volume/Vol20): 1.195479 | gap_open: 4.26%
- RS vs SILJ gap: 4.54% / slope_proxy: 0.000398
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.77 | RSI14: 33.290763 | ATR14%: 7.45%
- MA20 gap: -15.83% | MA50 gap: -23.49% | MA200 gap: -23.11%
- vol_ratio(Volume/Vol20): 1.170471 | gap_open: 5.80%
- SilverMarginGate: SI=49.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.06% / slope_proxy: 0.018214
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 16.42 | RSI14: 40.774677 | ATR14%: 7.38%
- MA20 gap: -4.97% | MA50 gap: -18.64% | MA200 gap: -45.36%
- vol_ratio(Volume/Vol20): 1.169454 | gap_open: 7.01%
- RS vs SILJ gap: -1.42% / slope_proxy: -0.047946
- RS vs GDXJ gap: -3.75% / slope_proxy: -0.016412
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-10-31 01:46:49**
- 데이터 기준일(주가): **2026-10-30**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.26 / 4주 변화 0.02 bp-ish / 2026-10-29
- IG OAS: 0.89 / 4주 변화 0.03 bp-ish / 2026-10-29
- 10Y Real Yield: 2.63 / 4주 변화 -0.30 bp-ish / 2026-10-29
- VIX: 17.20 / 4주 변화 0.81 / 2026-10-29
- NFCI: -0.49 / 4주 변화 0.02 / 2026-10-23

### Leadership ratios

- GDX/GLD: gap -7.04% / slope_proxy -5.92%
- GDXJ/GLD: gap -10.90% / slope_proxy -10.19%
- SILJ/SLV: gap -0.40% / slope_proxy 2.54%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.49 | RSI14: 23.44 | ATR14%: 5.05%
- MA20/50/200 gap: -12.87% / -21.28% / -7.43%
- 5D return: -6.02% | 20D drawdown: -19.98% | vol_ratio: 2.42
- RS vs GDXJ: gap -3.00% / slope_proxy -2.02%
- FundamentalScore: 88 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **56.1**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.23 | RSI14: 21.50 | ATR14%: 6.88%
- MA20/50/200 gap: -16.78% / -26.72% / -24.81%
- 5D return: -4.91% | 20D drawdown: -25.71% | vol_ratio: 1.11
- RS vs GDXJ: gap -8.44% / slope_proxy -9.16%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **53.4**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.78 | RSI14: 22.73 | ATR14%: 8.15%
- MA20/50/200 gap: -15.68% / -36.58% / -45.20%
- 5D return: -7.14% | 20D drawdown: -24.27% | vol_ratio: 1.41
- RS vs GDXJ: gap -23.22% / slope_proxy -9.38%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.0**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.53 | RSI14: 19.27 | ATR14%: 8.64%
- MA20/50/200 gap: -22.00% / -34.32% / -22.84%
- 5D return: -12.57% | 20D drawdown: -30.77% | vol_ratio: 1.37
- RS vs GDXJ: gap -17.38% / slope_proxy -15.62%
- FundamentalScore: 55 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **41.2**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 23.02 | RSI14: 32.15 | ATR14%: 5.80%
- MA20/50/200 gap: -10.37% / -14.89% / 10.52%
- 5D return: -3.16% | 20D drawdown: -16.32% | vol_ratio: 1.11
- RS vs SILJ: gap 7.60% / slope_proxy 2.66%
- FundamentalScore: 86 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **64.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.06 | RSI14: 35.33 | ATR14%: 6.17%
- MA20/50/200 gap: -7.44% / -17.32% / -18.33%
- 5D return: -0.97% | 20D drawdown: -13.80% | vol_ratio: 1.20
- RS vs SILJ: gap 4.54% / slope_proxy 5.09%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **57.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.21 | RSI14: 31.05 | ATR14%: 5.88%
- MA20/50/200 gap: -11.04% / -22.69% / -26.11%
- 5D return: -3.48% | 20D drawdown: -16.84% | vol_ratio: 1.05
- RS vs SILJ: gap -3.33% / slope_proxy 1.06%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **53.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 13.53 | RSI14: 26.39 | ATR14%: 5.76%
- MA20/50/200 gap: -12.07% / -23.61% / -27.46%
- 5D return: -2.31% | 20D drawdown: -20.88% | vol_ratio: 1.00
- RS vs SILJ: gap -3.41% / slope_proxy -4.12%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **51.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.77 | RSI14: 24.15 | ATR14%: 7.17%
- MA20/50/200 gap: -15.83% / -23.49% / -23.11%
- 5D return: -2.59% | 20D drawdown: -25.69% | vol_ratio: 1.17
- RS vs SILJ: gap -3.06% / slope_proxy -8.61%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **49.8**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.87 | RSI14: 17.24 | ATR14%: 7.89%
- MA20/50/200 gap: -22.23% / -36.37% / -49.61%
- 5D return: -6.51% | 20D drawdown: -35.79% | vol_ratio: 1.29
- RS vs SILJ: gap -20.47% / slope_proxy -21.91%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **47.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.34 | RSI14: 28.28 | ATR14%: 6.55%
- MA20/50/200 gap: -14.62% / -27.96% / -36.89%
- 5D return: -6.47% | 20D drawdown: -22.22% | vol_ratio: 1.26
- RS vs SILJ: gap -10.81% / slope_proxy -6.24%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **43.5**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 16.42 | RSI14: 39.29 | ATR14%: 7.14%
- MA20/50/200 gap: -4.97% / -18.64% / -45.36%
- 5D return: 6.35% | 20D drawdown: -14.43% | vol_ratio: 1.17
- RS vs SILJ: gap -1.42% / slope_proxy 5.28%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **35.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
