# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **✅ Precious miners entry confirmed: EXK**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-05-29 15:01:15**
- 데이터 기준일(일봉): **2026-05-29**
- 데이터 기준일(주봉): **2026-05-25**
- VXN 기준일: **2026-05-27** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 737.26
- Weekly RSI14: **77.23**
- 52W MA: 603.62 / gap: **22.14%**
- 104W MA gap: **35.07%**
- 52W MA 13W slope: **7.48%**
- VXN: **23.39** / 5D change: -0.70

## Daily trigger: 실제 매수 타이밍

- QQQ close: 737.26
- Daily RSI14: **76.90**
- 20D gap: **3.99%**
- 50D gap: **12.92%**
- 200D gap: **19.53%**
- MACD hist: -0.0438 / change: 0.1349
- ATR14%: **1.40%**
- 20D high drawdown: **0.00%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-29 15:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.09 / 4주 변화 13.0 bp
- VIX (VIXCLS): 16.29
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.985987
- MA60: 8.919577
- gap: 0.74%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.338639
- MA60: 0.286236
- gap: 18.31%
- MA60_slope_proxy: 0.04197
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-29 15:00:46**

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
- TERM_SPREAD_10Y_POLICY: 107.59 bp / 4주 변화 -17.94 bp
- CURVE_10s5s: 45.99 bp / 4주 변화 1.7 bp

## NWG Price
- close: 596.2
- MA50: 577.3718 / gap50: 3.26%
- MA200: 587.1563 / gap200: 1.54%

## Relative Strength
- RS vs FTSE gap: 2.28% / slope_proxy: -0.001139
- RS vs Peers gap: -4.13% / slope_proxy: -0.027108

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-29 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 88.84 / 5D -7.79%
- Brent ref (BZ=F): 92.00 / 5D -10.31%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.16
- Gas ref (NG=F): 3.33 / 5D 10.50%

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

- close: 56.53
- MA20 / MA60 / MA200: 57.48 / 58.36 / 48.15
- gap20 / gap60: -1.66% / -3.14%
- 5D return: -3.92%
- 20D high/low: 60.70 / 53.03

### Relative Strength

- ratio: 1.002039
- ratio_MA60: 1.004366
- ratio_gap: -0.23%
- ratio_slope_proxy(20d): 0.027521

### Volume (if available)

- volume: 2854589.00
- volume_MA20: 11867119.45
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.61
- MA20 / MA60 / MA200: 20.23 / 20.12 / 15.05
- gap20 / gap60: -7.96% / -7.48%
- 5D return: -7.06%
- 20D high/low: 22.01 / 18.61

### Relative Strength

- ratio: 0.520772
- ratio_MA60: 0.527241
- ratio_gap: -1.23%
- ratio_slope_proxy(20d): 0.042476

### Volume (if available)

- volume: 4966984.00
- volume_MA20: 16943089.20
- volume_ratio: 0.29

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

- close: 6.26
- MA20 / MA60 / MA200: 6.68 / 6.50 / 4.84
- gap20 / gap60: -6.34% / -3.82%
- 5D return: -8.28%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014907
- ratio_MA60: 0.015707
- ratio_gap: -5.09%
- ratio_slope_proxy(20d): -0.000201

### Volume (if available)

- volume: 4604863.00
- volume_MA20: 34328243.15
- volume_ratio: 0.13

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

- close: 12.23
- MA20 / MA60 / MA200: 13.01 / 13.45 / 10.87
- gap20 / gap60: -5.96% / -9.05%
- 5D return: -9.77%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.054182
- ratio_MA60: 0.051757
- ratio_gap: 4.69%
- ratio_slope_proxy(20d): 0.003139

### Volume (if available)

- volume: 3058219.00
- volume_MA20: 19131455.95
- volume_ratio: 0.16

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

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-29 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.71
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.09
- VIX: 16.29
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 1.68% / slope_proxy: -0.013143
- GDXJ/GLD gap: -0.11% / slope_proxy: -0.006273

## VZLA (Vizsla Silver)
- close: 3.87 | RSI14: 60.68752 | ATR14%: 5.67%
- MA20 gap: 9.01% | MA50 gap: 13.77% | MA200 gap: -8.75%
- vol_ratio(Volume/Vol20): 0.273075 | gap_open: 0.26%
- RS vs SILJ gap: 11.35% / slope_proxy: 0.000214
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
- close: 8.165 | RSI14: 45.480856 | ATR14%: 7.17%
- MA20 gap: -5.02% | MA50 gap: -2.26% | MA200 gap: -1.69%
- vol_ratio(Volume/Vol20): 0.230336 | gap_open: 0.00%
- SilverMarginGate: SI=75.379997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.43% / slope_proxy: -0.011723
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
- close: 33.131599 | RSI14: 42.698043 | ATR14%: 8.88%
- MA20 gap: -9.78% | MA50 gap: -9.67% | MA200 gap: 38.42%
- vol_ratio(Volume/Vol20): 0.23609 | gap_open: 0.69%
- RS vs SILJ gap: -10.95% / slope_proxy: 0.008754
- RS vs GDXJ gap: -8.07% / slope_proxy: 0.004034
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-05-29 15:01:13**
- 데이터 기준일(주가): **2026-05-29**

## Verdict
**✅ Precious miners entry confirmed: EXK**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **True**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 -0.11 bp-ish / 2026-05-27
- IG OAS: 0.74 / 4주 변화 -0.07 bp-ish / 2026-05-27
- 10Y Real Yield: 2.09 / 4주 변화 0.17 bp-ish / 2026-05-27
- VIX: 16.29 / 4주 변화 -2.52 / 2026-05-27
- NFCI: -0.51 / 4주 변화 0.04 / 2026-05-22

### Leadership ratios

- GDX/GLD: gap -0.76% / slope_proxy 2.78%
- GDXJ/GLD: gap -0.13% / slope_proxy 2.98%
- SILJ/SLV: gap 1.69% / slope_proxy 4.00%
- Gold breadth proxy: above50 15.38%, above200 69.23%, count 13
- Silver breadth proxy: above50 69.23%, above200 84.62%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.71 | RSI14: 57.04 | ATR14%: 6.06%
- MA20/50/200 gap: 6.93% / 17.25% / 37.91%
- 5D return: 0.73% | 20D drawdown: 0.00% | vol_ratio: 0.28
- RS vs GDXJ: gap 21.47% / slope_proxy 14.04%
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
- close: 6.89 | RSI14: 47.10 | ATR14%: 5.68%
- MA20/50/200 gap: 4.14% / 0.67% / 0.75%
- 5D return: 16.19% | 20D drawdown: -6.39% | vol_ratio: 0.41
- RS vs GDXJ: gap 0.51% / slope_proxy 6.08%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **65.7**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.93 | RSI14: 51.70 | ATR14%: 9.59%
- MA20/50/200 gap: -3.45% / 5.30% / 22.77%
- 5D return: -5.85% | 20D drawdown: -22.49% | vol_ratio: 0.30
- RS vs GDXJ: gap 9.12% / slope_proxy 12.22%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **60.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.36 | RSI14: 41.38 | ATR14%: 5.51%
- MA20/50/200 gap: -2.61% / -2.94% / -6.11%
- 5D return: 2.26% | 20D drawdown: -11.69% | vol_ratio: 0.18
- RS vs GDXJ: gap -1.99% / slope_proxy 0.32%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.78 | RSI14: 47.71 | ATR14%: 6.76%
- MA20/50/200 gap: -0.15% / 2.54% / 6.01%
- 5D return: 4.82% | 20D drawdown: -14.66% | vol_ratio: 0.16
- RS vs SILJ: gap 0.49% / slope_proxy 1.94%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 100 | OverallScore: **86.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **True**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 20.69 | RSI14: 56.08 | ATR14%: 6.86%
- MA20/50/200 gap: 9.78% / 20.81% / 43.10%
- 5D return: 21.14% | 20D drawdown: -3.41% | vol_ratio: 0.31
- RS vs SILJ: gap 21.38% / slope_proxy 7.42%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **81.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 6.16 | RSI14: 42.68 | ATR14%: 7.80%
- MA20/50/200 gap: -1.00% / 3.70% / 14.57%
- 5D return: 7.88% | 20D drawdown: -16.87% | vol_ratio: 0.21
- RS vs SILJ: gap -1.34% / slope_proxy 0.63%
- FundamentalScore: 68 | TechnicalScore: 60 | RegimeScore: 100 | OverallScore: **71.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: RelativeStrength(vs SILJ)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.28 | RSI14: 54.42 | ATR14%: 6.93%
- MA20/50/200 gap: 4.58% / 7.89% / 15.07%
- 5D return: 9.47% | 20D drawdown: -8.66% | vol_ratio: 0.23
- RS vs SILJ: gap 6.29% / slope_proxy 6.10%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **69.8**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.86 | RSI14: 58.60 | ATR14%: 5.95%
- MA20/50/200 gap: 8.61% / 13.34% / -9.10%
- 5D return: 14.05% | 20D drawdown: 0.00% | vol_ratio: 0.27
- RS vs SILJ: gap 10.92% / slope_proxy 6.84%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **66.4**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.51 | RSI14: 44.81 | ATR14%: 6.75%
- MA20/50/200 gap: -3.13% / -4.70% / 1.91%
- 5D return: 1.24% | 20D drawdown: -16.79% | vol_ratio: 0.25
- RS vs SILJ: gap -6.45% / slope_proxy -7.00%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **60.4**
- Checks:
  - sector_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.16 | RSI14: 39.69 | ATR14%: 7.31%
- MA20/50/200 gap: -5.02% / -2.26% / -1.69%
- 5D return: -0.18% | 20D drawdown: -19.56% | vol_ratio: 0.23
- RS vs SILJ: gap -4.43% / slope_proxy -4.05%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **58.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 33.13 | RSI14: 39.25 | ATR14%: 9.17%
- MA20/50/200 gap: -9.79% / -9.67% / 38.41%
- 5D return: -0.48% | 20D drawdown: -26.64% | vol_ratio: 0.24
- RS vs SILJ: gap -10.95% / slope_proxy -17.97%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **44.2**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
