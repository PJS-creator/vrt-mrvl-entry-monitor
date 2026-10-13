# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-13 03:01:13**
- 데이터 기준일(일봉): **2026-10-12**
- 데이터 기준일(주봉): **2026-10-12**
- VXN 기준일: **2026-10-09** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 746.04
- Weekly RSI14: **63.18**
- 52W MA: 661.79 / gap: **12.73%**
- 104W MA gap: **25.90%**
- 52W MA 13W slope: **5.74%**
- VXN: **20.55** / 5D change: -0.65

## Daily trigger: 실제 매수 타이밍

- QQQ close: 746.04
- Daily RSI14: **56.71**
- 20D gap: **0.92%**
- 50D gap: **2.88%**
- 200D gap: **11.10%**
- MACD hist: 0.0712 / change: -0.7721
- ATR14%: **1.20%**
- 20D high drawdown: **-1.79%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-10-12**
- 실행시간(UTC): **2026-10-13 03:00:50**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.15 / 4주 변화 45.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.87 / 4주 변화 32.0 bp
- VIX (VIXCLS): 14.84
- NFCI: -0.494

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.25664
- MA60: 8.687767
- gap: -4.96%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.449855
- MA60: 0.399504
- gap: 12.60%
- MA60_slope_proxy: 0.008311
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-12**
- 실행시간(UTC): **2026-10-13 03:00:52**

## Verdict
🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **True**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **True**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 167.92 bp / 4주 변화 11.02 bp
- CURVE_10s5s: 43.54 bp / 4주 변화 1.13 bp

## NWG Price
- close: 642.6
- MA50: 690.6145 / gap50: -6.95%
- MA200: 635.2201 / gap200: 1.16%

## Relative Strength
- RS vs FTSE gap: -5.01% / slope_proxy: 0.000336
- RS vs Peers gap: 2.73% / slope_proxy: 0.012989

## Why not today?
- DemandGreen=FALSE (monthly)

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-13 03:00:58**

## Commodity Regime

- WTI ref (CL=F): 92.61 / 5D 3.56%
- Brent ref (BZ=F): 105.47 / 5D 5.13%
- Brent Tier: **>=90**
- Brent-WTI spread: 12.86
- Gas ref (NG=F): 3.16 / 5D 3.00%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 61.13
- MA20 / MA60 / MA200: 58.27 / 58.21 / 54.20
- gap20 / gap60: 4.90% / 5.02%
- 5D return: 4.84%
- 20D high/low: 63.52 / 54.94

### Relative Strength

- ratio: 0.926072
- ratio_MA60: 0.941265
- ratio_gap: -1.61%
- ratio_slope_proxy(20d): -0.008440

### Volume (if available)

- volume: 6404700.00
- volume_MA20: 9460585.00
- volume_ratio: 0.68

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 25.42
- MA20 / MA60 / MA200: 22.02 / 19.77 / 17.73
- gap20 / gap60: 15.47% / 28.56%
- 5D return: 5.30%
- 20D high/low: 25.42 / 20.37

### Relative Strength

- ratio: 0.583831
- ratio_MA60: 0.533469
- ratio_gap: 9.44%
- ratio_slope_proxy(20d): 0.030255

### Volume (if available)

- volume: 13275700.00
- volume_MA20: 24490475.00
- volume_ratio: 0.54

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.60
- MA20 / MA60 / MA200: 5.45 / 5.53 / 5.72
- gap20 / gap60: 2.67% / 1.24%
- 5D return: 1.63%
- 20D high/low: 5.94 / 5.17

### Relative Strength

- ratio: 0.014407
- ratio_MA60: 0.013797
- ratio_gap: 4.42%
- ratio_slope_proxy(20d): 0.000081

### Volume (if available)

- volume: 36130500.00
- volume_MA20: 40469810.00
- volume_ratio: 0.89

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.13
- MA20 / MA60 / MA200: 13.38 / 13.82 / 12.22
- gap20 / gap60: -1.88% / -4.97%
- 5D return: -2.38%
- 20D high/low: 15.29 / 12.54

### Relative Strength

- ratio: 0.046480
- ratio_MA60: 0.050790
- ratio_gap: -8.49%
- ratio_slope_proxy(20d): 0.000545

### Volume (if available)

- volume: 7271800.00
- volume_MA20: 12569135.00
- volume_ratio: 0.58

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-12**
- 실행시간(UTC): **2026-10-13 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.15
- IG OAS 4주 변화: 2.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 32.0 bp / latest 2.87
- VIX: 14.84
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -0.92% / slope_proxy: 0.007994
- GDXJ/GLD gap: -0.18% / slope_proxy: 0.012601

## VZLA (Vizsla Silver)
- close: 3.5 | RSI14: 39.698081 | ATR14%: 5.17%
- MA20 gap: -7.44% | MA50 gap: -8.57% | MA200 gap: -10.73%
- vol_ratio(Volume/Vol20): 0.223539 | gap_open: 0.85%
- RS vs SILJ gap: -0.51% / slope_proxy: 0.002787
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

## SCZM (Santacruz Silver)
- close: 8.89 | RSI14: 49.110452 | ATR14%: 6.18%
- MA20 gap: -0.34% | MA50 gap: -2.00% | MA200 gap: -1.11%
- vol_ratio(Volume/Vol20): 0.349653 | gap_open: 0.99%
- SilverMarginGate: SI=60.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.76% / slope_proxy: 0.020693
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

## HYMC (Hycroft Mining)
- close: 18.27 | RSI14: 38.987824 | ATR14%: 6.97%
- MA20 gap: -8.12% | MA50 gap: -19.39% | MA200 gap: -40.70%
- vol_ratio(Volume/Vol20): 0.542023 | gap_open: 0.99%
- RS vs SILJ gap: -12.83% / slope_proxy: -0.05444
- RS vs GDXJ gap: -15.44% / slope_proxy: -0.018337
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

- 실행시간(UTC): **2026-10-13 03:01:12**
- 데이터 기준일(주가): **2026-10-12**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.15 / 4주 변화 0.45 bp-ish / 2026-10-08
- IG OAS: 0.82 / 4주 변화 0.02 bp-ish / 2026-10-08
- 10Y Real Yield: 2.87 / 4주 변화 0.32 bp-ish / 2026-10-08
- VIX: 14.84 / 4주 변화 -1.00 / 2026-10-09
- NFCI: -0.49 / 4주 변화 0.01 / 2026-10-02

### Leadership ratios

- GDX/GLD: gap 1.52% / slope_proxy -3.00%
- GDXJ/GLD: gap -0.18% / slope_proxy -3.20%
- SILJ/SLV: gap -0.92% / slope_proxy -1.91%
- Gold breadth proxy: above50 7.69%, above200 30.77%, count 13
- Silver breadth proxy: above50 0.00%, above200 15.38%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.19 | RSI14: 26.09 | ATR14%: 3.73%
- MA20/50/200 gap: -4.93% / -6.09% / 15.89%
- 5D return: 1.21% | 20D drawdown: -12.81% | vol_ratio: 0.28
- RS vs GDXJ: gap 1.82% / slope_proxy -3.82%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **50.9**
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
- close: 6.98 | RSI14: 35.56 | ATR14%: 4.94%
- MA20/50/200 gap: -4.73% / -4.19% / -1.25%
- 5D return: 1.31% | 20D drawdown: -14.77% | vol_ratio: 0.21
- RS vs GDXJ: gap 2.50% / slope_proxy -6.18%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.02 | RSI14: 19.18 | ATR14%: 8.96%
- MA20/50/200 gap: -14.89% / -25.76% / -30.77%
- 5D return: -0.97% | 20D drawdown: -32.89% | vol_ratio: 1.37
- RS vs GDXJ: gap -21.84% / slope_proxy -24.11%
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
- close: 2.20 | RSI14: 19.54 | ATR14%: 6.07%
- MA20/50/200 gap: -8.35% / -8.13% / 10.19%
- 5D return: 1.38% | 20D drawdown: -20.86% | vol_ratio: 0.52
- RS vs GDXJ: gap -2.85% / slope_proxy -5.90%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.45 | RSI14: 30.68 | ATR14%: 4.81%
- MA20/50/200 gap: -3.79% / -2.95% / 31.37%
- 5D return: -2.15% | 20D drawdown: -12.94% | vol_ratio: 0.30
- RS vs SILJ: gap 8.17% / slope_proxy 6.90%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **58.7**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.89 | RSI14: 41.03 | ATR14%: 5.89%
- MA20/50/200 gap: -0.34% / -2.00% / -1.11%
- 5D return: -0.45% | 20D drawdown: -6.91% | vol_ratio: 0.35
- RS vs SILJ: gap 9.76% / slope_proxy 11.04%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **53.3**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.54 | RSI14: 20.24 | ATR14%: 5.05%
- MA20/50/200 gap: -6.56% / -13.41% / -13.86%
- 5D return: -0.70% | 20D drawdown: -18.74% | vol_ratio: 0.49
- RS vs SILJ: gap -4.51% / slope_proxy -4.40%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.84 | RSI14: 27.70 | ATR14%: 4.02%
- MA20/50/200 gap: -4.55% / -9.04% / -11.83%
- 5D return: -1.00% | 20D drawdown: -11.51% | vol_ratio: 0.50
- RS vs SILJ: gap 0.06% / slope_proxy -2.72%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **46.4**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.50 | RSI14: 15.52 | ATR14%: 4.91%
- MA20/50/200 gap: -7.44% / -8.57% / -10.73%
- 5D return: -0.28% | 20D drawdown: -18.60% | vol_ratio: 0.22
- RS vs SILJ: gap -0.51% / slope_proxy 0.45%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **43.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.20 | RSI14: 22.96 | ATR14%: 5.70%
- MA20/50/200 gap: -8.89% / -15.00% / -28.17%
- 5D return: -5.19% | 20D drawdown: -20.15% | vol_ratio: 0.42
- RS vs SILJ: gap -6.43% / slope_proxy -3.36%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **41.9**
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
- close: 5.40 | RSI14: 19.55 | ATR14%: 4.58%
- MA20/50/200 gap: -6.95% / -17.83% / -22.65%
- 5D return: -3.23% | 20D drawdown: -16.80% | vol_ratio: 0.45
- RS vs SILJ: gap -10.54% / slope_proxy -5.09%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **38.2**
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
- close: 18.27 | RSI14: 24.94 | ATR14%: 6.13%
- MA20/50/200 gap: -8.12% / -19.39% / -40.70%
- 5D return: -2.82% | 20D drawdown: -19.48% | vol_ratio: 0.54
- RS vs SILJ: gap -12.83% / slope_proxy -4.75%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **30.2**
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
