# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: EXK**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-14 02:40:56**
- 데이터 기준일(일봉): **2026-11-13**
- 데이터 기준일(주봉): **2026-11-09**
- VXN 기준일: **2026-11-12** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 679.89
- Weekly RSI14: **45.93**
- 52W MA: 666.43 / gap: **2.02%**
- 104W MA gap: **13.41%**
- 52W MA 13W slope: **4.67%**
- VXN: **28.55** / 5D change: -9.71

## Daily trigger: 실제 매수 타이밍

- QQQ close: 679.89
- Daily RSI14: **42.82**
- 20D gap: **-2.24%**
- 50D gap: **-5.27%**
- 200D gap: **-0.19%**
- MACD hist: -0.1002 / change: 0.4512
- ATR14%: **2.40%**
- 20D high drawdown: **-6.30%**

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

- 데이터 기준일(주가): **2026-11-13**
- 실행시간(UTC): **2026-11-14 02:40:26**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.2 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.89 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.86 / 4주 변화 8.0 bp
- VIX (VIXCLS): 18.7
- NFCI: -0.462

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.107633
- MA60: 8.108503
- gap: -12.34%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.322054
- MA60: 0.40603
- gap: -20.68%
- MA60_slope_proxy: 0.001191
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-13**
- 실행시간(UTC): **2026-11-14 02:40:29**

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
- TERM_SPREAD_10Y_POLICY: 120.44 bp / 4주 변화 -42.86 bp
- CURVE_10s5s: 31.92 bp / 4주 변화 -9.46 bp

## NWG Price
- close: 597.2
- MA50: 655.564 / gap50: -8.90%
- MA200: 632.513 / gap200: -5.58%

## Relative Strength
- RS vs FTSE gap: -10.84% / slope_proxy: -0.002351
- RS vs Peers gap: -3.91% / slope_proxy: 0.010865

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-14 02:40:40**

## Commodity Regime

- WTI ref (CL=F): 88.92 / 5D -2.10%
- Brent ref (BZ=F): 96.08 / 5D -2.28%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.16
- Gas ref (NG=F): 3.24 / 5D 8.14%

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

- close: 58.75
- MA20 / MA60 / MA200: 60.50 / 59.73 / 56.43
- gap20 / gap60: -2.89% / -1.64%
- 5D return: 4.20%
- 20D high/low: 64.17 / 55.76

### Relative Strength

- ratio: 0.904403
- ratio_MA60: 0.924554
- ratio_gap: -2.18%
- ratio_slope_proxy(20d): -0.013147

### Volume (if available)

- volume: 10712100.00
- volume_MA20: 10648840.00
- volume_ratio: 1.01

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.34
- MA20 / MA60 / MA200: 21.48 / 21.47 / 18.93
- gap20 / gap60: -14.61% / -14.59%
- 5D return: -1.03%
- 20D high/low: 26.16 / 17.82

### Relative Strength

- ratio: 0.569212
- ratio_MA60: 0.575059
- ratio_gap: -1.02%
- ratio_slope_proxy(20d): 0.034614

### Volume (if available)

- volume: 17736100.00
- volume_MA20: 27625075.00
- volume_ratio: 0.64

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.54
- MA20 / MA60 / MA200: 5.90 / 5.70 / 5.90
- gap20 / gap60: -6.11% / -2.87%
- 5D return: 5.73%
- 20D high/low: 6.94 / 5.10

### Relative Strength

- ratio: 0.014752
- ratio_MA60: 0.014426
- ratio_gap: 2.26%
- ratio_slope_proxy(20d): 0.000565

### Volume (if available)

- volume: 30160500.00
- volume_MA20: 43837885.00
- volume_ratio: 0.69

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.14
- MA20 / MA60 / MA200: 13.02 / 13.59 / 12.83
- gap20 / gap60: 0.94% / -3.30%
- 5D return: 13.96%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.042559
- ratio_MA60: 0.047932
- ratio_gap: -11.21%
- ratio_slope_proxy(20d): -0.002403

### Volume (if available)

- volume: 7852100.00
- volume_MA20: 16576580.00
- volume_ratio: 0.47

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-13**
- 실행시간(UTC): **2026-11-14 02:40:46**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 3.2
- IG OAS 4주 변화: 5.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.86
- VIX: 18.7
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 2.16% / slope_proxy: 0.004409
- GDXJ/GLD gap: -6.20% / slope_proxy: -0.0008

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 41.672801 | ATR14%: 6.39%
- MA20 gap: -4.29% | MA50 gap: -13.18% | MA200 gap: -14.46%
- vol_ratio(Volume/Vol20): 0.94131 | gap_open: 0.32%
- RS vs SILJ gap: 1.94% / slope_proxy: 0.00167
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
- close: 6.83 | RSI14: 40.250346 | ATR14%: 7.63%
- MA20 gap: -7.76% | MA50 gap: -18.35% | MA200 gap: -19.43%
- vol_ratio(Volume/Vol20): 0.926797 | gap_open: 0.57%
- SilverMarginGate: SI=48.650002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.34% / slope_proxy: 0.007862
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
- close: 15.9 | RSI14: 42.089773 | ATR14%: 9.87%
- MA20 gap: -7.28% | MA50 gap: -15.49% | MA200 gap: -44.56%
- vol_ratio(Volume/Vol20): 0.911347 | gap_open: 0.06%
- RS vs SILJ gap: -2.95% / slope_proxy: -0.049633
- RS vs GDXJ gap: -6.17% / slope_proxy: -0.01665
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

- 실행시간(UTC): **2026-11-14 02:40:55**
- 데이터 기준일(주가): **2026-11-13**

## Verdict
**🟡 Precious miners watch/add-on candidates: EXK**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.20 / 4주 변화 -0.05 bp-ish / 2026-11-12
- IG OAS: 0.89 / 4주 변화 0.05 bp-ish / 2026-11-12
- 10Y Real Yield: 2.86 / 4주 변화 0.02 bp-ish / 2026-11-12
- VIX: 18.70 / 4주 변화 2.24 / 2026-11-12
- NFCI: -0.46 / 4주 변화 0.05 / 2026-11-06

### Leadership ratios

- GDX/GLD: gap -1.63% / slope_proxy 0.85%
- GDXJ/GLD: gap -6.20% / slope_proxy -2.39%
- SILJ/SLV: gap 2.16% / slope_proxy 5.13%
- Gold breadth proxy: above50 0.00%, above200 23.08%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.40 | RSI14: 42.53 | ATR14%: 5.83%
- MA20/50/200 gap: -7.29% / -17.59% / -8.86%
- 5D return: -7.96% | 20D drawdown: -17.32% | vol_ratio: 1.22
- RS vs GDXJ: gap -6.65% / slope_proxy -9.52%
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
- close: 4.57 | RSI14: 35.38 | ATR14%: 8.23%
- MA20/50/200 gap: -18.04% / -31.27% / -32.62%
- 5D return: -17.95% | 20D drawdown: -30.55% | vol_ratio: 4.06
- RS vs GDXJ: gap -21.76% / slope_proxy -24.00%
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
- close: 0.76 | RSI14: 42.55 | ATR14%: 8.98%
- MA20/50/200 gap: -9.69% / -29.35% / -44.29%
- 5D return: -6.17% | 20D drawdown: -20.00% | vol_ratio: 0.69
- RS vs GDXJ: gap -22.46% / slope_proxy -12.45%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **42.8**
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
- close: 1.54 | RSI14: 45.05 | ATR14%: 8.44%
- MA20/50/200 gap: -10.26% / -27.79% / -21.21%
- 5D return: -7.23% | 20D drawdown: -24.14% | vol_ratio: 0.43
- RS vs GDXJ: gap -18.43% / slope_proxy -16.98%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **36.0**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.66 | RSI14: 52.11 | ATR14%: 6.50%
- MA20/50/200 gap: -1.59% / -11.93% / -19.31%
- 5D return: -2.30% | 20D drawdown: -8.15% | vol_ratio: 0.98
- RS vs SILJ: gap 1.99% / slope_proxy 3.02%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **61.9**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 22.88 | RSI14: 46.78 | ATR14%: 7.12%
- MA20/50/200 gap: -7.16% / -13.22% / 8.30%
- 5D return: -9.81% | 20D drawdown: -14.53% | vol_ratio: 1.09
- RS vs SILJ: gap 2.86% / slope_proxy -4.23%
- FundamentalScore: 86 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **60.2**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.07 | RSI14: 50.00 | ATR14%: 6.74%
- MA20/50/200 gap: -4.29% / -13.18% / -14.46%
- 5D return: -6.97% | 20D drawdown: -12.29% | vol_ratio: 0.94
- RS vs SILJ: gap 1.94% / slope_proxy 6.58%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **57.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.50 | RSI14: 39.06 | ATR14%: 10.37%
- MA20/50/200 gap: -19.16% / -37.58% / -54.02%
- 5D return: -19.09% | 20D drawdown: -33.69% | vol_ratio: 1.31
- RS vs SILJ: gap -28.26% / slope_proxy -26.33%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **52.1**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 13.10 | RSI14: 44.62 | ATR14%: 6.67%
- MA20/50/200 gap: -8.34% / -20.24% / -26.97%
- 5D return: -11.13% | 20D drawdown: -14.99% | vol_ratio: 0.76
- RS vs SILJ: gap -7.53% / slope_proxy -3.30%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **51.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.83 | RSI14: 47.86 | ATR14%: 7.68%
- MA20/50/200 gap: -7.76% / -18.35% / -19.43%
- 5D return: -9.18% | 20D drawdown: -18.59% | vol_ratio: 0.93
- RS vs SILJ: gap -4.34% / slope_proxy -9.56%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **49.6**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.29 | RSI14: 43.62 | ATR14%: 6.78%
- MA20/50/200 gap: -8.36% / -21.18% / -35.68%
- 5D return: -7.74% | 20D drawdown: -17.66% | vol_ratio: 0.77
- RS vs SILJ: gap -9.97% / slope_proxy -8.53%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **43.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.90 | RSI14: 51.72 | ATR14%: 10.86%
- MA20/50/200 gap: -7.28% / -15.49% / -44.56%
- 5D return: -15.29% | 20D drawdown: -25.25% | vol_ratio: 0.91
- RS vs SILJ: gap -2.95% / slope_proxy 4.77%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **35.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
