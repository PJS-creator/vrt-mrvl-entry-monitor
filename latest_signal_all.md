# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-07 15:01:18**
- 데이터 기준일(일봉): **2026-10-07**
- 데이터 기준일(주봉): **2026-10-05**
- VXN 기준일: **2026-10-06** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 754.07
- Weekly RSI14: **65.74**
- 52W MA: 659.06 / gap: **14.42%**
- 104W MA gap: **27.78%**
- 52W MA 13W slope: **5.75%**
- VXN: **21.15** / 5D change: -0.92

## Daily trigger: 실제 매수 타이밍

- QQQ close: 754.08
- Daily RSI14: **64.79**
- 20D gap: **2.83%**
- 50D gap: **4.61%**
- 200D gap: **12.63%**
- MACD hist: 2.0425 / change: -0.3762
- ATR14%: **1.20%**
- 20D high drawdown: **-0.73%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-07 15:00:46**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.12 / 4주 변화 44.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.95 / 4주 변화 52.0 bp
- VIX (VIXCLS): 15.01
- NFCI: -0.494

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.458421
- MA60: 8.761008
- gap: -3.45%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.45164
- MA60: 0.393869
- gap: 14.67%
- MA60_slope_proxy: -0.000224
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-07 15:00:49**

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
- TERM_SPREAD_10Y_POLICY: 161.34 bp / 4주 변화 25.55 bp
- CURVE_10s5s: 43.23 bp / 4주 변화 -3.66 bp

## NWG Price
- close: 650.2
- MA50: 691.9459 / gap50: -6.03%
- MA200: 635.2795 / gap200: 2.35%

## Relative Strength
- RS vs FTSE gap: -3.06% / slope_proxy: 0.000525
- RS vs Peers gap: 3.04% / slope_proxy: 0.011775

## Why not today?
- DemandGreen=FALSE (monthly)

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-07 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 89.78 / 5D -0.71%
- Brent ref (BZ=F): 101.91 / 5D -1.56%
- Brent Tier: **>=90**
- Brent-WTI spread: 12.13
- Gas ref (NG=F): 3.23 / 5D 6.84%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.90
- MA20 / MA60 / MA200: 58.40 / 57.87 / 53.88
- gap20 / gap60: -0.86% / 0.05%
- 5D return: 4.66%
- 20D high/low: 63.52 / 54.94

### Relative Strength

- ratio: 0.916212
- ratio_MA60: 0.942454
- ratio_gap: -2.78%
- ratio_slope_proxy(20d): -0.008673

### Volume (if available)

- volume: 1870832.00
- volume_MA20: 9251626.60
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 23.73
- MA20 / MA60 / MA200: 21.42 / 19.37 / 17.52
- gap20 / gap60: 10.79% / 22.48%
- 5D return: 13.70%
- 20D high/low: 24.14 / 20.37

### Relative Strength

- ratio: 0.556716
- ratio_MA60: 0.528559
- ratio_gap: 5.33%
- ratio_slope_proxy(20d): 0.029085

### Volume (if available)

- volume: 6187773.00
- volume_MA20: 23111678.65
- volume_ratio: 0.27

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.34
- MA20 / MA60 / MA200: 5.46 / 5.51 / 5.70
- gap20 / gap60: -2.27% / -3.10%
- 5D return: 1.91%
- 20D high/low: 5.94 / 5.17

### Relative Strength

- ratio: 0.014021
- ratio_MA60: 0.013759
- ratio_gap: 1.90%
- ratio_slope_proxy(20d): 0.000025

### Volume (if available)

- volume: 5064574.00
- volume_MA20: 41820913.70
- volume_ratio: 0.12

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

- close: 12.81
- MA20 / MA60 / MA200: 13.71 / 13.81 / 12.12
- gap20 / gap60: -6.55% / -7.19%
- 5D return: 1.38%
- 20D high/low: 15.76 / 12.54

### Relative Strength

- ratio: 0.047150
- ratio_MA60: 0.050948
- ratio_gap: -7.45%
- ratio_slope_proxy(20d): 0.001075

### Volume (if available)

- volume: 4893109.00
- volume_MA20: 13969105.45
- volume_ratio: 0.35

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

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-07 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 44.0 bp / latest 3.12
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 52.0 bp / latest 2.95
- VIX: 15.01
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.67% / slope_proxy: 0.00966
- GDXJ/GLD gap: -0.84% / slope_proxy: 0.01196

## VZLA (Vizsla Silver)
- close: 3.385 | RSI14: 34.127077 | ATR14%: 5.81%
- MA20 gap: -11.89% | MA50 gap: -11.09% | MA200 gap: -14.36%
- vol_ratio(Volume/Vol20): 0.25441 | gap_open: 3.40%
- RS vs SILJ gap: -1.04% / slope_proxy: 0.002949
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.46 | RSI14: 43.40232 | ATR14%: 6.86%
- MA20 gap: -6.13% | MA50 gap: -5.29% | MA200 gap: -5.92%
- vol_ratio(Volume/Vol20): 0.373711 | gap_open: 3.91%
- SilverMarginGate: SI=60.049999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.71% / slope_proxy: 0.019409
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 17.950001 | RSI14: 34.928309 | ATR14%: 7.60%
- MA20 gap: -11.39% | MA50 gap: -21.02% | MA200 gap: -41.85%
- vol_ratio(Volume/Vol20): 0.325744 | gap_open: 4.92%
- RS vs SILJ gap: -12.64% / slope_proxy: -0.059543
- RS vs GDXJ gap: -15.35% / slope_proxy: -0.01959
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-10-07 15:01:16**
- 데이터 기준일(주가): **2026-10-07**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA**

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

- HY OAS: 3.12 / 4주 변화 0.44 bp-ish / 2026-10-05
- IG OAS: 0.84 / 4주 변화 0.03 bp-ish / 2026-10-05
- 10Y Real Yield: 2.95 / 4주 변화 0.52 bp-ish / 2026-10-05
- VIX: 15.01 / 4주 변화 -0.71 / 2026-10-06
- NFCI: -0.49 / 4주 변화 0.01 / 2026-10-02

### Leadership ratios

- GDX/GLD: gap 0.54% / slope_proxy -6.03%
- GDXJ/GLD: gap -0.84% / slope_proxy -6.89%
- SILJ/SLV: gap -2.74% / slope_proxy -8.61%
- Gold breadth proxy: above50 0.00%, above200 23.08%, count 13
- Silver breadth proxy: above50 0.00%, above200 15.38%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.75 | RSI14: 15.95 | ATR14%: 4.16%
- MA20/50/200 gap: -10.57% / -9.48% / 11.02%
- 5D return: -6.82% | 20D drawdown: -16.98% | vol_ratio: 0.40
- RS vs GDXJ: gap 0.32% / slope_proxy 0.89%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **59.6**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.70 | RSI14: 29.63 | ATR14%: 5.10%
- MA20/50/200 gap: -9.89% / -7.30% / -5.31%
- 5D return: -5.10% | 20D drawdown: -18.19% | vol_ratio: 0.24
- RS vs GDXJ: gap 3.29% / slope_proxy -4.45%
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
- close: 0.97 | RSI14: 18.67 | ATR14%: 9.65%
- MA20/50/200 gap: -22.24% / -29.72% / -34.34%
- 5D return: -8.49% | 20D drawdown: -36.18% | vol_ratio: 0.74
- RS vs GDXJ: gap -23.00% / slope_proxy -25.28%
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
- close: 2.12 | RSI14: 22.83 | ATR14%: 6.47%
- MA20/50/200 gap: -13.08% / -10.94% / 6.19%
- 5D return: -6.61% | 20D drawdown: -23.74% | vol_ratio: 0.57
- RS vs GDXJ: gap -2.36% / slope_proxy -6.60%
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
- close: 26.41 | RSI14: 37.87 | ATR14%: 5.09%
- MA20/50/200 gap: -4.53% / -1.61% / 32.37%
- 5D return: -1.82% | 20D drawdown: -13.07% | vol_ratio: 0.23
- RS vs SILJ: gap 12.34% / slope_proxy 8.36%
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
- close: 8.46 | RSI14: 44.80 | ATR14%: 6.75%
- MA20/50/200 gap: -6.13% / -5.29% / -5.92%
- 5D return: -4.19% | 20D drawdown: -12.69% | vol_ratio: 0.37
- RS vs SILJ: gap 8.81% / slope_proxy 1.80%
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
- close: 8.39 | RSI14: 23.02 | ATR14%: 5.56%
- MA20/50/200 gap: -10.53% / -14.45% / -15.54%
- 5D return: -2.23% | 20D drawdown: -20.26% | vol_ratio: 0.34
- RS vs SILJ: gap -3.48% / slope_proxy -7.02%
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
- close: 16.46 | RSI14: 26.03 | ATR14%: 4.69%
- MA20/50/200 gap: -8.81% / -10.40% / -14.07%
- 5D return: -3.37% | 20D drawdown: -17.80% | vol_ratio: 0.11
- RS vs SILJ: gap 0.70% / slope_proxy -4.15%
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
- close: 3.38 | RSI14: 26.42 | ATR14%: 5.53%
- MA20/50/200 gap: -11.89% / -11.09% / -14.36%
- 5D return: -10.69% | 20D drawdown: -21.28% | vol_ratio: 0.25
- RS vs SILJ: gap -0.95% / slope_proxy -1.32%
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
- close: 4.21 | RSI14: 29.70 | ATR14%: 6.09%
- MA20/50/200 gap: -10.74% / -14.27% / -28.23%
- 5D return: -3.38% | 20D drawdown: -19.91% | vol_ratio: 0.38
- RS vs SILJ: gap -3.49% / slope_proxy -3.49%
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
- close: 5.32 | RSI14: 25.94 | ATR14%: 5.03%
- MA20/50/200 gap: -10.88% / -18.90% / -23.92%
- 5D return: -4.05% | 20D drawdown: -25.21% | vol_ratio: 0.38
- RS vs SILJ: gap -9.87% / slope_proxy -12.79%
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
- close: 17.95 | RSI14: 31.87 | ATR14%: 7.01%
- MA20/50/200 gap: -11.39% / -21.02% / -41.85%
- 5D return: -5.72% | 20D drawdown: -20.89% | vol_ratio: 0.33
- RS vs SILJ: gap -12.55% / slope_proxy -2.15%
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
