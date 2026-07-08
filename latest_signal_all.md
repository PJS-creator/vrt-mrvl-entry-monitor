# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-08 03:01:40**
- 데이터 기준일(일봉): **2026-07-07**
- 데이터 기준일(주봉): **2026-07-06**
- VXN 기준일: **2026-07-06** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 709.43
- Weekly RSI14: **61.15**
- 52W MA: 623.57 / gap: **13.77%**
- 104W MA gap: **26.89%**
- 52W MA 13W slope: **8.36%**
- VXN: **26.81** / 5D change: -4.01

## Daily trigger: 실제 매수 타이밍

- QQQ close: 709.43
- Daily RSI14: **47.25**
- 20D gap: **-1.48%**
- 50D gap: **-0.23%**
- 200D gap: **11.76%**
- MACD hist: -2.4274 / change: -0.6140
- ATR14%: **2.32%**
- 20D high drawdown: **-4.54%**

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

- 데이터 기준일(주가): **2026-07-07**
- 실행시간(UTC): **2026-07-08 03:00:55**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.24 / 4주 변화 3.0 bp
- VIX (VIXCLS): 15.57
- NFCI: -0.504

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.892522
- MA60: 9.452392
- gap: 4.66%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.396767
- MA60: 0.371726
- gap: 6.74%
- MA60_slope_proxy: 0.066444
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-07**
- 실행시간(UTC): **2026-07-08 03:00:59**

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
- TERM_SPREAD_10Y_POLICY: 101.52 bp / 4주 변화 -11.21 bp
- CURVE_10s5s: 48.71 bp / 4주 변화 4.07 bp

## NWG Price
- close: 686.4
- MA50: 605.6171 / gap50: 13.34%
- MA200: 600.2207 / gap200: 14.36%

## Relative Strength
- RS vs FTSE gap: 10.81% / slope_proxy: 0.002201
- RS vs Peers gap: 3.67% / slope_proxy: -0.008817

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-08 03:01:07**

## Commodity Regime

- WTI ref (CL=F): 72.29 / 5D 2.18%
- Brent ref (BZ=F): 76.06 / 5D 3.98%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.77
- Gas ref (NG=F): 3.28 / 5D 3.14%

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

- close: 51.68
- MA20 / MA60 / MA200: 52.36 / 55.62 / 49.00
- gap20 / gap60: -1.29% / -7.09%
- 5D return: 5.28%
- 20D high/low: 57.22 / 47.94

### Relative Strength

- ratio: 0.945827
- ratio_MA60: 0.985181
- ratio_gap: -3.99%
- ratio_slope_proxy(20d): -0.025577

### Volume (if available)

- volume: 11594521.00
- volume_MA20: 9812901.05
- volume_ratio: 1.18

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.66
- MA20 / MA60 / MA200: 16.95 / 19.20 / 15.68
- gap20 / gap60: -1.71% / -13.25%
- 5D return: 2.33%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.480947
- ratio_MA60: 0.521967
- ratio_gap: -7.86%
- ratio_slope_proxy(20d): -0.013915

### Volume (if available)

- volume: 20794827.00
- volume_MA20: 14731491.35
- volume_ratio: 1.41

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.02
- MA20 / MA60 / MA200: 5.42 / 6.13 / 5.15
- gap20 / gap60: -7.29% / -18.09%
- 5D return: -0.40%
- 20D high/low: 6.17 / 4.87

### Relative Strength

- ratio: 0.013705
- ratio_MA60: 0.014674
- ratio_gap: -6.61%
- ratio_slope_proxy(20d): -0.000889

### Volume (if available)

- volume: 34088293.00
- volume_MA20: 34231439.65
- volume_ratio: 1.00

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

- close: 11.59
- MA20 / MA60 / MA200: 11.54 / 12.33 / 10.69
- gap20 / gap60: 0.42% / -5.99%
- 5D return: 3.95%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045451
- ratio_MA60: 0.050206
- ratio_gap: -9.47%
- ratio_slope_proxy(20d): -0.001952

### Volume (if available)

- volume: 11954448.00
- volume_MA20: 13166272.40
- volume_ratio: 0.91

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-07**
- 실행시간(UTC): **2026-07-08 03:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.72
- IG OAS 4주 변화: 0.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.24
- VIX: 15.57
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 3.70% / slope_proxy: 0.00775
- GDXJ/GLD gap: -5.67% / slope_proxy: -0.00193

## VZLA (Vizsla Silver)
- close: 3.09 | RSI14: 38.833284 | ATR14%: 6.90%
- MA20 gap: -8.34% | MA50 gap: -11.58% | MA200 gap: -26.83%
- vol_ratio(Volume/Vol20): 1.313095 | gap_open: 0.61%
- RS vs SILJ gap: 2.23% / slope_proxy: 0.005022
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
- close: 6.37 | RSI14: 40.029081 | ATR14%: 8.02%
- MA20 gap: -5.50% | MA50 gap: -17.27% | MA200 gap: -25.19%
- vol_ratio(Volume/Vol20): 1.044071 | gap_open: 2.35%
- SilverMarginGate: SI=60.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.25% / slope_proxy: -0.006859
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
- close: 21.709999 | RSI14: 34.149273 | ATR14%: 10.00%
- MA20 gap: -10.53% | MA50 gap: -30.32% | MA200 gap: -18.18%
- vol_ratio(Volume/Vol20): 0.627393 | gap_open: 2.08%
- RS vs SILJ gap: -22.57% / slope_proxy: -0.092558
- RS vs GDXJ gap: -22.68% / slope_proxy: -0.020307
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

- 실행시간(UTC): **2026-07-08 03:01:37**
- 데이터 기준일(주가): **2026-07-07**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

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

- HY OAS: 2.72 / 4주 변화 -0.03 bp-ish / 2026-07-06
- IG OAS: 0.75 / 4주 변화 0.00 bp-ish / 2026-07-06
- 10Y Real Yield: 2.24 / 4주 변화 0.13 bp-ish / 2026-07-06
- VIX: 15.57 / 4주 변화 -3.35 / 2026-07-06
- NFCI: -0.50 / 4주 변화 0.05 / 2026-06-26

### Leadership ratios

- GDX/GLD: gap -5.11% / slope_proxy 1.35%
- GDXJ/GLD: gap -5.67% / slope_proxy 2.46%
- SILJ/SLV: gap 3.70% / slope_proxy 8.74%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.73 | RSI14: 46.13 | ATR14%: 5.30%
- MA20/50/200 gap: 1.52% / -1.90% / 15.14%
- 5D return: 5.03% | 20D drawdown: -7.87% | vol_ratio: 0.76
- RS vs GDXJ: gap 12.75% / slope_proxy 7.29%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **75.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.74 | RSI14: 49.23 | ATR14%: 5.30%
- MA20/50/200 gap: 8.18% / -3.42% / 1.42%
- 5D return: 15.23% | 20D drawdown: -0.57% | vol_ratio: 1.45
- RS vs GDXJ: gap 11.01% / slope_proxy 3.46%
- FundamentalScore: 55 | TechnicalScore: 80 | RegimeScore: 30 | OverallScore: **58.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.29 | RSI14: 32.80 | ATR14%: 5.87%
- MA20/50/200 gap: -3.22% / -13.53% / -23.69%
- 5D return: 1.73% | 20D drawdown: -13.98% | vol_ratio: 0.29
- RS vs GDXJ: gap -3.71% / slope_proxy -5.64%
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
- close: 1.18 | RSI14: 29.58 | ATR14%: 8.20%
- MA20/50/200 gap: -5.41% / -10.78% / -21.83%
- 5D return: 2.61% | 20D drawdown: -19.73% | vol_ratio: 0.87
- RS vs GDXJ: gap 1.47% / slope_proxy -0.02%
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
- close: 18.78 | RSI14: 41.02 | ATR14%: 7.52%
- MA20/50/200 gap: -0.25% / 0.14% / 20.51%
- 5D return: 0.05% | 20D drawdown: -10.78% | vol_ratio: 0.58
- RS vs SILJ: gap 16.32% / slope_proxy 11.53%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 55 | OverallScore: **79.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.02 | RSI14: 33.83 | ATR14%: 6.46%
- MA20/50/200 gap: -3.63% / -11.92% / -16.00%
- 5D return: -2.55% | 20D drawdown: -13.76% | vol_ratio: 0.74
- RS vs SILJ: gap 0.68% / slope_proxy 3.73%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.56 | RSI14: 39.85 | ATR14%: 5.56%
- MA20/50/200 gap: 0.34% / -8.08% / -13.70%
- 5D return: 1.04% | 20D drawdown: -6.94% | vol_ratio: 0.91
- RS vs SILJ: gap 4.08% / slope_proxy 8.67%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.37 | RSI14: 31.68 | ATR14%: 7.27%
- MA20/50/200 gap: -5.50% / -17.27% / -25.19%
- 5D return: -2.15% | 20D drawdown: -20.08% | vol_ratio: 1.04
- RS vs SILJ: gap -6.25% / slope_proxy 4.48%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **54.8**
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
- close: 3.09 | RSI14: 26.67 | ATR14%: 6.23%
- MA20/50/200 gap: -8.34% / -11.58% / -26.83%
- 5D return: -5.50% | 20D drawdown: -16.26% | vol_ratio: 1.31
- RS vs SILJ: gap 2.23% / slope_proxy -6.59%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **53.9**
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
- close: 4.38 | RSI14: 22.62 | ATR14%: 8.72%
- MA20/50/200 gap: -12.37% / -22.44% / -23.13%
- 5D return: -6.61% | 20D drawdown: -25.51% | vol_ratio: 1.11
- RS vs SILJ: gap -11.31% / slope_proxy -8.17%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.07 | RSI14: 36.81 | ATR14%: 6.98%
- MA20/50/200 gap: -2.79% / -8.34% / -7.99%
- 5D return: -3.19% | 20D drawdown: -12.66% | vol_ratio: 0.72
- RS vs SILJ: gap 4.30% / slope_proxy 5.55%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.71 | RSI14: 24.94 | ATR14%: 8.37%
- MA20/50/200 gap: -10.53% / -30.32% / -18.18%
- 5D return: -7.14% | 20D drawdown: -22.02% | vol_ratio: 0.63
- RS vs SILJ: gap -22.57% / slope_proxy -14.26%
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
