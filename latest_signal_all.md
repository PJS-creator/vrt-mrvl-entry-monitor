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

- 실행시간(UTC): **2026-10-27 01:36:59**
- 데이터 기준일(일봉): **2026-10-26**
- 데이터 기준일(주봉): **2026-10-26**
- VXN 기준일: **2026-10-23** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 712.20
- Weekly RSI14: **52.62**
- 52W MA: 664.48 / gap: **7.18%**
- 104W MA gap: **19.40%**
- 52W MA 13W slope: **5.34%**
- VXN: **28.30** / 5D change: 1.17

## Daily trigger: 실제 매수 타이밍

- QQQ close: 712.20
- Daily RSI14: **41.80**
- 20D gap: **-2.97%**
- 50D gap: **-1.78%**
- 200D gap: **5.27%**
- MACD hist: -4.5192 / change: 0.6490
- ATR14%: **1.61%**
- 20D high drawdown: **-6.25%**

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

- 데이터 기준일(주가): **2026-10-26**
- 실행시간(UTC): **2026-10-27 01:36:33**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.38 / 4주 변화 45.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.66 / 4주 변화 -17.0 bp
- VIX (VIXCLS): 19.45
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.230547
- MA60: 8.4287
- gap: -14.22%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.431631
- MA60: 0.414388
- gap: 4.16%
- MA60_slope_proxy: 0.026251
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-26**
- 실행시간(UTC): **2026-10-27 01:36:36**

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
- TERM_SPREAD_10Y_POLICY: 152.84 bp / 4주 변화 -6.54 bp
- CURVE_10s5s: 37.04 bp / 4주 변화 -4.9 bp

## NWG Price
- close: 627.4
- MA50: 678.736 / gap50: -7.56%
- MA200: 635.3695 / gap200: -1.25%

## Relative Strength
- RS vs FTSE gap: -7.96% / slope_proxy: -0.000336
- RS vs Peers gap: 2.54% / slope_proxy: 0.020721

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-27 01:36:43**

## Commodity Regime

- WTI ref (CL=F): 101.13 / 5D -2.44%
- Brent ref (BZ=F): 110.01 / 5D 0.42%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.88
- Gas ref (NG=F): 3.04 / 5D -0.72%

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

- close: 64.07
- MA20 / MA60 / MA200: 60.39 / 59.30 / 55.29
- gap20 / gap60: 6.10% / 8.04%
- 5D return: 2.15%
- 20D high/low: 64.17 / 54.94

### Relative Strength

- ratio: 0.920017
- ratio_MA60: 0.934898
- ratio_gap: -1.59%
- ratio_slope_proxy(20d): -0.012328

### Volume (if available)

- volume: 7303700.00
- volume_MA20: 8790260.00
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 22.50
- MA20 / MA60 / MA200: 24.27 / 20.98 / 18.44
- gap20 / gap60: -7.30% / 7.22%
- 5D return: -11.97%
- 20D high/low: 26.16 / 20.65

### Relative Strength

- ratio: 0.658858
- ratio_MA60: 0.551783
- ratio_gap: 19.41%
- ratio_slope_proxy(20d): 0.033360

### Volume (if available)

- volume: 102563900.00
- volume_MA20: 28327645.00
- volume_ratio: 3.62

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

- close: 6.53
- MA20 / MA60 / MA200: 5.65 / 5.65 / 5.81
- gap20 / gap60: 15.64% / 15.52%
- 5D return: 10.87%
- 20D high/low: 6.53 / 5.17

### Relative Strength

- ratio: 0.016228
- ratio_MA60: 0.014072
- ratio_gap: 15.32%
- ratio_slope_proxy(20d): 0.000315

### Volume (if available)

- volume: 63866400.00
- volume_MA20: 41187855.00
- volume_ratio: 1.55

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.76
- MA20 / MA60 / MA200: 13.09 / 13.72 / 12.52
- gap20 / gap60: 5.10% / 0.29%
- 5D return: 7.42%
- 20D high/low: 14.00 / 12.50

### Relative Strength

- ratio: 0.045777
- ratio_MA60: 0.049686
- ratio_gap: -7.87%
- ratio_slope_proxy(20d): -0.001232

### Volume (if available)

- volume: 13231200.00
- volume_MA20: 13914155.00
- volume_ratio: 0.95

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

- 데이터 기준일(주가): **2026-10-26**
- 실행시간(UTC): **2026-10-27 01:36:47**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 45.0 bp / latest 3.38
- IG OAS 4주 변화: 10.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -17.0 bp / latest 2.66
- VIX: 19.45
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.16% / slope_proxy: 0.007159
- GDXJ/GLD gap: -9.31% / slope_proxy: 0.009667

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 33.993693 | ATR14%: 5.90%
- MA20 gap: -10.02% | MA50 gap: -17.98% | MA200 gap: -19.19%
- vol_ratio(Volume/Vol20): 0.972617 | gap_open: 0.32%
- RS vs SILJ gap: 1.43% / slope_proxy: 0.001025
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
- close: 7.04 | RSI14: 32.92306 | ATR14%: 7.34%
- MA20 gap: -15.77% | MA50 gap: -21.75% | MA200 gap: -20.72%
- vol_ratio(Volume/Vol20): 1.168057 | gap_open: 0.58%
- SilverMarginGate: SI=53.935001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.28% / slope_proxy: 0.021112
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
- close: 15.39 | RSI14: 31.741832 | ATR14%: 7.62%
- MA20 gap: -12.96% | MA50 gap: -26.40% | MA200 gap: -49.29%
- vol_ratio(Volume/Vol20): 0.75975 | gap_open: 0.06%
- RS vs SILJ gap: -12.03% / slope_proxy: -0.04933
- RS vs GDXJ gap: -15.80% / slope_proxy: -0.016756
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

- 실행시간(UTC): **2026-10-27 01:36:57**
- 데이터 기준일(주가): **2026-10-26**

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

- HY OAS: 3.38 / 4주 변화 0.45 bp-ish / 2026-10-23
- IG OAS: 0.91 / 4주 변화 0.10 bp-ish / 2026-10-23
- 10Y Real Yield: 2.66 / 4주 변화 -0.19 bp-ish / 2026-10-23
- VIX: 19.45 / 4주 변화 4.58 / 2026-10-23
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-16

### Leadership ratios

- GDX/GLD: gap -5.21% / slope_proxy -5.31%
- GDXJ/GLD: gap -9.31% / slope_proxy -10.16%
- SILJ/SLV: gap -5.16% / slope_proxy -3.87%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.92 | RSI14: 31.89 | ATR14%: 4.88%
- MA20/50/200 gap: -10.93% / -18.28% / -1.74%
- 5D return: -11.51% | 20D drawdown: -16.98% | vol_ratio: 0.90
- RS vs GDXJ: gap -2.28% / slope_proxy -3.81%
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
- close: 5.57 | RSI14: 27.30 | ATR14%: 6.54%
- MA20/50/200 gap: -15.30% / -23.19% / -20.52%
- 5D return: -15.35% | 20D drawdown: -22.64% | vol_ratio: 0.77
- RS vs GDXJ: gap -7.42% / slope_proxy -10.94%
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
- close: 0.83 | RSI14: 31.71 | ATR14%: 7.70%
- MA20/50/200 gap: -14.43% / -35.53% / -42.53%
- 5D return: -12.63% | 20D drawdown: -27.19% | vol_ratio: 0.42
- RS vs GDXJ: gap -24.06% / slope_proxy -16.88%
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
- close: 1.65 | RSI14: 19.78 | ATR14%: 7.71%
- MA20/50/200 gap: -20.77% / -30.74% / -17.01%
- 5D return: -18.72% | 20D drawdown: -30.08% | vol_ratio: 1.00
- RS vs GDXJ: gap -15.90% / slope_proxy -20.18%
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
- close: 23.83 | RSI14: 30.63 | ATR14%: 5.49%
- MA20/50/200 gap: -9.06% / -12.42% / 15.26%
- 5D return: -10.21% | 20D drawdown: -13.38% | vol_ratio: 0.73
- RS vs SILJ: gap 8.54% / slope_proxy 4.14%
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
- close: 7.04 | RSI14: 27.57 | ATR14%: 6.94%
- MA20/50/200 gap: -15.77% / -21.75% / -20.72%
- 5D return: -16.09% | 20D drawdown: -22.72% | vol_ratio: 1.17
- RS vs SILJ: gap -2.28% / slope_proxy -6.96%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.49 | RSI14: 30.72 | ATR14%: 5.25%
- MA20/50/200 gap: -9.66% / -21.54% / -23.76%
- 5D return: -9.32% | 20D drawdown: -14.30% | vol_ratio: 0.82
- RS vs SILJ: gap -3.06% / slope_proxy 1.65%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.01 | RSI14: 16.20 | ATR14%: 7.59%
- MA20/50/200 gap: -23.95% / -35.67% / -47.68%
- 5D return: -20.16% | 20D drawdown: -33.11% | vol_ratio: 1.34
- RS vs SILJ: gap -20.86% / slope_proxy -20.66%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 13.98 | RSI14: 25.24 | ATR14%: 5.31%
- MA20/50/200 gap: -12.24% / -22.86% / -25.79%
- 5D return: -7.11% | 20D drawdown: -18.72% | vol_ratio: 0.89
- RS vs SILJ: gap -3.57% / slope_proxy -3.31%
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
- close: 3.07 | RSI14: 32.84 | ATR14%: 5.56%
- MA20/50/200 gap: -10.02% / -17.98% / -19.19%
- 5D return: -4.06% | 20D drawdown: -20.05% | vol_ratio: 0.97
- RS vs SILJ: gap 1.43% / slope_proxy -5.17%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.60 | RSI14: 29.54 | ATR14%: 6.02%
- MA20/50/200 gap: -12.66% / -26.25% / -33.47%
- 5D return: -11.71% | 20D drawdown: -18.29% | vol_ratio: 1.16
- RS vs SILJ: gap -9.77% / slope_proxy -3.09%
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
- close: 15.39 | RSI14: 29.10 | ATR14%: 7.03%
- MA20/50/200 gap: -12.96% / -26.40% / -49.29%
- 5D return: -8.72% | 20D drawdown: -20.59% | vol_ratio: 0.76
- RS vs SILJ: gap -12.03% / slope_proxy -5.81%
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
