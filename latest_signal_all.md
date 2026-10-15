# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-15 15:01:16**
- 데이터 기준일(일봉): **2026-10-15**
- 데이터 기준일(주봉): **2026-10-12**
- VXN 기준일: **2026-10-14** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 723.20
- Weekly RSI14: **55.66**
- 52W MA: 661.35 / gap: **9.35%**
- 104W MA gap: **22.09%**
- 52W MA 13W slope: **5.67%**
- VXN: **22.70** / 5D change: 1.70

## Daily trigger: 실제 매수 타이밍

- QQQ close: 723.15
- Daily RSI14: **41.57**
- 20D gap: **-2.65%**
- 50D gap: **-0.44%**
- 200D gap: **7.42%**
- MACD hist: -3.3242 / change: -1.2346
- ATR14%: **1.35%**
- 20D high drawdown: **-4.81%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
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

- 데이터 기준일(주가): **2026-10-15**
- 실행시간(UTC): **2026-10-15 15:00:51**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.25 / 4주 변화 55.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.88 / 4주 변화 26.0 bp
- VIX (VIXCLS): 16.87
- NFCI: -0.499

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.543093
- MA60: 8.585538
- gap: -12.14%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.427128
- MA60: 0.403741
- gap: 5.79%
- MA60_slope_proxy: 0.014542
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-15**
- 실행시간(UTC): **2026-10-15 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 164.28 bp / 4주 변화 3.12 bp
- CURVE_10s5s: 40.97 bp / 4주 변화 -2.31 bp

## NWG Price
- close: 676.0
- MA50: 686.7721 / gap50: -1.57%
- MA200: 635.5674 / gap200: 6.36%

## Relative Strength
- RS vs FTSE gap: -2.54% / slope_proxy: 7.2e-05
- RS vs Peers gap: 5.52% / slope_proxy: 0.014934

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-15 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 95.29 / 5D 4.15%
- Brent ref (BZ=F): 105.44 / 5D 1.11%
- Brent Tier: **>=90**
- Brent-WTI spread: 10.15
- Gas ref (NG=F): 3.27 / 5D 3.28%

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

- close: 60.82
- MA20 / MA60 / MA200: 58.36 / 58.47 / 54.52
- gap20 / gap60: 4.22% / 4.03%
- 5D return: 0.90%
- 20D high/low: 61.65 / 54.94

### Relative Strength

- ratio: 0.911776
- ratio_MA60: 0.938659
- ratio_gap: -2.86%
- ratio_slope_proxy(20d): -0.009899

### Volume (if available)

- volume: 2265592.00
- volume_MA20: 8932299.60
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 25.79
- MA20 / MA60 / MA200: 22.70 / 20.16 / 17.95
- gap20 / gap60: 13.61% / 27.91%
- 5D return: 4.44%
- 20D high/low: 25.94 / 20.37

### Relative Strength

- ratio: 0.607565
- ratio_MA60: 0.538576
- ratio_gap: 12.81%
- ratio_slope_proxy(20d): 0.031365

### Volume (if available)

- volume: 4619335.00
- volume_MA20: 23523651.75
- volume_ratio: 0.20

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

- close: 5.53
- MA20 / MA60 / MA200: 5.44 / 5.55 / 5.75
- gap20 / gap60: 1.74% / -0.38%
- 5D return: -0.18%
- 20D high/low: 5.65 / 5.17

### Relative Strength

- ratio: 0.014778
- ratio_MA60: 0.013850
- ratio_gap: 6.70%
- ratio_slope_proxy(20d): 0.000117

### Volume (if available)

- volume: 11955445.00
- volume_MA20: 37439407.25
- volume_ratio: 0.32

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

- close: 12.26
- MA20 / MA60 / MA200: 13.13 / 13.76 / 12.31
- gap20 / gap60: -6.68% / -10.91%
- 5D return: -7.79%
- 20D high/low: 14.02 / 12.26

### Relative Strength

- ratio: 0.044029
- ratio_MA60: 0.050405
- ratio_gap: -12.65%
- ratio_slope_proxy(20d): -0.000165

### Volume (if available)

- volume: 15236187.00
- volume_MA20: 12622649.35
- volume_ratio: 1.21

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

- 데이터 기준일(주가): **2026-10-15**
- 실행시간(UTC): **2026-10-15 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 55.0 bp / latest 3.25
- IG OAS 4주 변화: 6.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.88
- VIX: 16.87
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -2.79% / slope_proxy: 0.007042
- GDXJ/GLD gap: -5.00% / slope_proxy: 0.012265

## VZLA (Vizsla Silver)
- close: 3.25 | RSI14: 34.648856 | ATR14%: 5.56%
- MA20 gap: -12.10% | MA50 gap: -14.89% | MA200 gap: -16.33%
- vol_ratio(Volume/Vol20): 0.27388 | gap_open: 1.89%
- RS vs SILJ gap: -0.80% / slope_proxy: 0.002462
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
- close: 8.12 | RSI14: 41.729053 | ATR14%: 6.63%
- MA20 gap: -8.30% | MA50 gap: -11.01% | MA200 gap: -9.34%
- vol_ratio(Volume/Vol20): 0.27186 | gap_open: 0.63%
- SilverMarginGate: SI=57.244999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.37% / slope_proxy: 0.021895
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
- close: 16.67 | RSI14: 34.290223 | ATR14%: 7.49%
- MA20 gap: -13.63% | MA50 gap: -25.34% | MA200 gap: -45.69%
- vol_ratio(Volume/Vol20): 0.389167 | gap_open: 1.56%
- RS vs SILJ gap: -13.86% / slope_proxy: -0.052199
- RS vs GDXJ gap: -17.89% / slope_proxy: -0.017859
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

- 실행시간(UTC): **2026-10-15 15:01:15**
- 데이터 기준일(주가): **2026-10-15**

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

- HY OAS: 3.25 / 4주 변화 0.55 bp-ish / 2026-10-14
- IG OAS: 0.84 / 4주 변화 0.06 bp-ish / 2026-10-14
- 10Y Real Yield: 2.88 / 4주 변화 0.28 bp-ish / 2026-10-13
- VIX: 16.87 / 4주 변화 -0.84 / 2026-10-14
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-09

### Leadership ratios

- GDX/GLD: gap -2.03% / slope_proxy -5.50%
- GDXJ/GLD: gap -5.00% / slope_proxy -8.94%
- SILJ/SLV: gap -2.77% / slope_proxy -2.89%
- Gold breadth proxy: above50 0.00%, above200 15.38%, count 13
- Silver breadth proxy: above50 0.00%, above200 15.38%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.77 | RSI14: 29.63 | ATR14%: 3.96%
- MA20/50/200 gap: -7.18% / -11.00% / 10.01%
- 5D return: -2.56% | 20D drawdown: -16.79% | vol_ratio: 0.15
- RS vs GDXJ: gap 1.43% / slope_proxy -3.81%
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
- close: 6.24 | RSI14: 22.27 | ATR14%: 5.64%
- MA20/50/200 gap: -12.72% / -14.96% / -11.52%
- 5D return: -6.31% | 20D drawdown: -23.81% | vol_ratio: 0.45
- RS vs GDXJ: gap -3.12% / slope_proxy -6.80%
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
- close: 0.94 | RSI14: 20.00 | ATR14%: 8.51%
- MA20/50/200 gap: -17.11% / -30.87% / -35.85%
- 5D return: -1.05% | 20D drawdown: -38.16% | vol_ratio: 0.27
- RS vs GDXJ: gap -22.55% / slope_proxy -25.03%
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
- close: 2.06 | RSI14: 17.11 | ATR14%: 5.89%
- MA20/50/200 gap: -11.97% / -14.44% / 3.29%
- 5D return: -3.29% | 20D drawdown: -25.90% | vol_ratio: 0.10
- RS vs GDXJ: gap -3.25% / slope_proxy -9.69%
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
- close: 25.92 | RSI14: 35.40 | ATR14%: 4.60%
- MA20/50/200 gap: -4.90% / -5.54% / 27.67%
- 5D return: -1.52% | 20D drawdown: -14.68% | vol_ratio: 0.18
- RS vs SILJ: gap 12.19% / slope_proxy 9.00%
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
- close: 8.12 | RSI14: 30.57 | ATR14%: 6.11%
- MA20/50/200 gap: -8.30% / -11.01% / -9.34%
- 5D return: -4.25% | 20D drawdown: -14.97% | vol_ratio: 0.27
- RS vs SILJ: gap 6.35% / slope_proxy 1.98%
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
- close: 8.10 | RSI14: 26.34 | ATR14%: 4.58%
- MA20/50/200 gap: -8.74% / -17.68% / -18.03%
- 5D return: -5.43% | 20D drawdown: -22.88% | vol_ratio: 0.35
- RS vs SILJ: gap -2.78% / slope_proxy -4.99%
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
- close: 15.16 | RSI14: 23.74 | ATR14%: 4.68%
- MA20/50/200 gap: -11.72% / -18.10% / -20.36%
- 5D return: -9.38% | 20D drawdown: -20.34% | vol_ratio: 0.14
- RS vs SILJ: gap -3.44% / slope_proxy -4.10%
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
- close: 3.25 | RSI14: 20.83 | ATR14%: 5.15%
- MA20/50/200 gap: -12.10% / -14.89% / -16.33%
- 5D return: -6.34% | 20D drawdown: -24.42% | vol_ratio: 0.27
- RS vs SILJ: gap -0.81% / slope_proxy -4.66%
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
- close: 3.77 | RSI14: 20.33 | ATR14%: 6.03%
- MA20/50/200 gap: -15.73% / -23.24% / -35.28%
- 5D return: -11.20% | 20D drawdown: -28.42% | vol_ratio: 0.41
- RS vs SILJ: gap -9.78% / slope_proxy -13.01%
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
- close: 5.05 | RSI14: 26.20 | ATR14%: 4.76%
- MA20/50/200 gap: -10.46% / -22.50% / -27.40%
- 5D return: -7.51% | 20D drawdown: -22.19% | vol_ratio: 0.42
- RS vs SILJ: gap -9.48% / slope_proxy -5.27%
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
- close: 16.67 | RSI14: 22.29 | ATR14%: 6.38%
- MA20/50/200 gap: -13.63% / -25.34% / -45.69%
- 5D return: -8.46% | 20D drawdown: -26.53% | vol_ratio: 0.39
- RS vs SILJ: gap -13.88% / slope_proxy -6.77%
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
