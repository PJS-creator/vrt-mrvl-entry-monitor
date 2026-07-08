# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-08 15:01:34**
- 데이터 기준일(일봉): **2026-07-08**
- 데이터 기준일(주봉): **2026-07-06**
- VXN 기준일: **2026-07-07** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 704.93
- Weekly RSI14: **59.89**
- 52W MA: 623.49 / gap: **13.06%**
- 104W MA gap: **26.09%**
- 52W MA 13W slope: **8.35%**
- VXN: **27.92** / 5D change: -1.45

## Daily trigger: 실제 매수 타이밍

- QQQ close: 704.93
- Daily RSI14: **45.81**
- 20D gap: **-2.03%**
- 50D gap: **-0.98%**
- 200D gap: **10.95%**
- MACD hist: -3.0131 / change: -0.5857
- ATR14%: **2.23%**
- 20D high drawdown: **-5.15%**

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

- 데이터 기준일(주가): **2026-07-08**
- 실행시간(UTC): **2026-07-08 15:01:05**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.67 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.24 / 4주 변화 3.0 bp
- VIX (VIXCLS): 16.13
- NFCI: -0.515

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.032707
- MA60: 9.472712
- gap: 5.91%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.395814
- MA60: 0.373421
- gap: 6.00%
- MA60_slope_proxy: 0.063854
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-08**
- 실행시간(UTC): **2026-07-08 15:01:08**

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
- TERM_SPREAD_10Y_POLICY: 101.94 bp / 4주 변화 -14.41 bp
- CURVE_10s5s: 48.95 bp / 4주 변화 4.31 bp

## NWG Price
- close: 658.2
- MA50: 609.2771 / gap50: 8.03%
- MA200: 601.7768 / gap200: 9.38%

## Relative Strength
- RS vs FTSE gap: 7.21% / slope_proxy: 0.002325
- RS vs Peers gap: 2.62% / slope_proxy: -0.007969

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-08 15:01:18**

## Commodity Regime

- WTI ref (CL=F): 75.30 / 5D 8.35%
- Brent ref (BZ=F): 79.50 / 5D 9.02%
- Brent Tier: **70-80**
- Brent-WTI spread: 4.20
- Gas ref (NG=F): 3.27 / 5D -0.03%

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

- close: 54.36
- MA20 / MA60 / MA200: 52.21 / 55.57 / 49.03
- gap20 / gap60: 4.11% / -2.17%
- 5D return: 11.92%
- 20D high/low: 57.10 / 47.94

### Relative Strength

- ratio: 0.975417
- ratio_MA60: 0.984426
- ratio_gap: -0.92%
- ratio_slope_proxy(20d): -0.025716

### Volume (if available)

- volume: 7047251.00
- volume_MA20: 9732372.55
- volume_ratio: 0.72

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.11
- MA20 / MA60 / MA200: 16.92 / 19.13 / 15.71
- gap20 / gap60: 1.14% / -10.58%
- 5D return: 5.88%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.500146
- ratio_MA60: 0.521598
- ratio_gap: -4.11%
- ratio_slope_proxy(20d): -0.014364

### Volume (if available)

- volume: 5471657.00
- volume_MA20: 14379487.85
- volume_ratio: 0.38

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.23
- MA20 / MA60 / MA200: 5.37 / 6.11 / 5.16
- gap20 / gap60: -2.57% / -14.36%
- 5D return: 6.95%
- 20D high/low: 6.04 / 4.87

### Relative Strength

- ratio: 0.013924
- ratio_MA60: 0.014641
- ratio_gap: -4.90%
- ratio_slope_proxy(20d): -0.000880

### Volume (if available)

- volume: 12109193.00
- volume_MA20: 33868414.65
- volume_ratio: 0.36

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

- close: 12.56
- MA20 / MA60 / MA200: 11.53 / 12.32 / 10.69
- gap20 / gap60: 8.98% / 1.97%
- 5D return: 12.89%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.048850
- ratio_MA60: 0.050205
- ratio_gap: -2.70%
- ratio_slope_proxy(20d): -0.002018

### Volume (if available)

- volume: 7175545.00
- volume_MA20: 13067927.25
- volume_ratio: 0.55

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-08**
- 실행시간(UTC): **2026-07-08 15:01:22**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.24
- VIX: 16.13
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 2.88% / slope_proxy: 0.008008
- GDXJ/GLD gap: -7.88% / slope_proxy: -0.002152

## VZLA (Vizsla Silver)
- close: 2.95 | RSI14: 35.255983 | ATR14%: 7.07%
- MA20 gap: -11.85% | MA50 gap: -15.40% | MA200 gap: -30.08%
- vol_ratio(Volume/Vol20): 0.321796 | gap_open: 1.29%
- RS vs SILJ gap: 2.19% / slope_proxy: 0.005097
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
- close: 6.11 | RSI14: 37.17032 | ATR14%: 8.12%
- MA20 gap: -9.21% | MA50 gap: -20.16% | MA200 gap: -28.24%
- vol_ratio(Volume/Vol20): 0.336451 | gap_open: 2.20%
- SilverMarginGate: SI=58.195 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.60% / slope_proxy: -0.005965
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
- close: 20.395 | RSI14: 31.275258 | ATR14%: 10.38%
- MA20 gap: -14.91% | MA50 gap: -33.79% | MA200 gap: -23.35%
- vol_ratio(Volume/Vol20): 0.185545 | gap_open: 3.22%
- RS vs SILJ gap: -23.24% / slope_proxy: -0.094991
- RS vs GDXJ gap: -23.73% / slope_proxy: -0.020804
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

- 실행시간(UTC): **2026-07-08 15:01:32**
- 데이터 기준일(주가): **2026-07-08**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

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

- HY OAS: 2.67 / 4주 변화 -0.11 bp-ish / 2026-07-07
- IG OAS: 0.76 / 4주 변화 0.01 bp-ish / 2026-07-07
- 10Y Real Yield: 2.24 / 4주 변화 0.13 bp-ish / 2026-07-06
- VIX: 16.13 / 4주 변화 -3.74 / 2026-07-07
- NFCI: -0.52 / 4주 변화 0.03 / 2026-07-03

### Leadership ratios

- GDX/GLD: gap -6.94% / slope_proxy -1.11%
- GDXJ/GLD: gap -7.88% / slope_proxy 0.24%
- SILJ/SLV: gap 2.88% / slope_proxy 6.06%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.32 | RSI14: 29.96 | ATR14%: 5.54%
- MA20/50/200 gap: -3.81% / -7.01% / 8.84%
- 5D return: 0.14% | 20D drawdown: -12.75% | vol_ratio: 0.21
- RS vs GDXJ: gap 10.98% / slope_proxy 6.78%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **68.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.13 | RSI14: 34.02 | ATR14%: 5.74%
- MA20/50/200 gap: -5.87% / -15.67% / -25.96%
- 5D return: -0.77% | 20D drawdown: -16.59% | vol_ratio: 0.38
- RS vs GDXJ: gap -2.36% / slope_proxy -3.88%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **48.1**
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.69 | RSI14: 53.33 | ATR14%: 5.33%
- MA20/50/200 gap: 4.84% / -6.09% / -1.82%
- 5D return: 4.97% | 20D drawdown: -3.43% | vol_ratio: 0.35
- RS vs GDXJ: gap 12.21% / slope_proxy 8.65%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **44.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.12 | RSI14: 30.00 | ATR14%: 8.26%
- MA20/50/200 gap: -10.04% / -15.04% / -25.79%
- 5D return: -2.61% | 20D drawdown: -23.81% | vol_ratio: 0.09
- RS vs GDXJ: gap 0.67% / slope_proxy -1.44%
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.47 | RSI14: 37.50 | ATR14%: 7.82%
- MA20/50/200 gap: -2.15% / -1.65% / 18.24%
- 5D return: -2.48% | 20D drawdown: -12.26% | vol_ratio: 0.33
- RS vs SILJ: gap 19.30% / slope_proxy 17.84%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.91 | RSI14: 34.97 | ATR14%: 5.84%
- MA20/50/200 gap: -3.83% / -11.48% / -17.37%
- 5D return: -3.34% | 20D drawdown: -10.80% | vol_ratio: 0.13
- RS vs SILJ: gap 4.73% / slope_proxy 9.39%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **60.1**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.57 | RSI14: 26.21 | ATR14%: 6.98%
- MA20/50/200 gap: -8.72% / -16.43% / -20.72%
- 5D return: -8.51% | 20D drawdown: -18.55% | vol_ratio: 0.30
- RS vs SILJ: gap -0.25% / slope_proxy 2.96%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **53.1**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.65 | RSI14: 29.56 | ATR14%: 7.56%
- MA20/50/200 gap: -9.28% / -14.36% / -14.44%
- 5D return: -10.88% | 20D drawdown: -18.71% | vol_ratio: 0.29
- RS vs SILJ: gap 1.84% / slope_proxy 4.21%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **52.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.11 | RSI14: 19.61 | ATR14%: 7.23%
- MA20/50/200 gap: -9.21% / -20.16% / -28.24%
- 5D return: -5.86% | 20D drawdown: -23.34% | vol_ratio: 0.34
- RS vs SILJ: gap -5.60% / slope_proxy 6.60%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 2.95 | RSI14: 21.54 | ATR14%: 6.51%
- MA20/50/200 gap: -11.85% / -15.40% / -30.08%
- 5D return: -10.61% | 20D drawdown: -20.05% | vol_ratio: 0.32
- RS vs SILJ: gap 2.19% / slope_proxy -5.72%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **48.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.17 | RSI14: 17.24 | ATR14%: 9.09%
- MA20/50/200 gap: -15.91% / -25.72% / -26.90%
- 5D return: -11.65% | 20D drawdown: -29.08% | vol_ratio: 0.28
- RS vs SILJ: gap -11.32% / slope_proxy -5.98%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 20.40 | RSI14: 24.85 | ATR14%: 8.51%
- MA20/50/200 gap: -14.91% / -33.79% / -23.35%
- 5D return: -12.84% | 20D drawdown: -26.74% | vol_ratio: 0.19
- RS vs SILJ: gap -23.24% / slope_proxy -12.66%
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
