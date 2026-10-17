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

- 실행시간(UTC): **2026-10-17 03:01:15**
- 데이터 기준일(일봉): **2026-10-16**
- 데이터 기준일(주봉): **2026-10-12**
- VXN 기준일: **2026-10-15** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 709.80
- Weekly RSI14: **52.02**
- 52W MA: 661.09 / gap: **7.37%**
- 104W MA gap: **19.85%**
- 52W MA 13W slope: **5.63%**
- VXN: **22.89** / 5D change: 0.91

## Daily trigger: 실제 매수 타이밍

- QQQ close: 709.80
- Daily RSI14: **35.14**
- 20D gap: **-4.41%**
- 50D gap: **-2.28%**
- 200D gap: **5.36%**
- MACD hist: -4.6662 / change: -1.6516
- ATR14%: **1.49%**
- 20D high drawdown: **-6.56%**

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

- 데이터 기준일(주가): **2026-10-16**
- 실행시간(UTC): **2026-10-17 03:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.23 / 4주 변화 53.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.78 / 4주 변화 17.0 bp
- VIX (VIXCLS): 16.46
- NFCI: -0.499

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.33286
- MA60: 8.541231
- gap: -14.15%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.422072
- MA60: 0.404839
- gap: 4.26%
- MA60_slope_proxy: 0.015986
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-16**
- 실행시간(UTC): **2026-10-17 03:00:46**

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
- TERM_SPREAD_10Y_POLICY: 163.3 bp / 4주 변화 14.09 bp
- CURVE_10s5s: 41.38 bp / 4주 변화 -2.16 bp

## NWG Price
- close: 674.0
- MA50: 686.7321 / gap50: -1.85%
- MA200: 635.5574 / gap200: 6.05%

## Relative Strength
- RS vs FTSE gap: -2.87% / slope_proxy: 6.9e-05
- RS vs Peers gap: 5.46% / slope_proxy: 0.014924

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-17 03:00:53**

## Commodity Regime

- WTI ref (CL=F): 99.04 / 5D 7.83%
- Brent ref (BZ=F): 109.69 / 5D 4.75%
- Brent Tier: **>=90**
- Brent-WTI spread: 10.65
- Gas ref (NG=F): 3.12 / 5D -3.20%

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

- close: 62.38
- MA20 / MA60 / MA200: 58.53 / 58.55 / 54.63
- gap20 / gap60: 6.58% / 6.55%
- 5D return: 3.78%
- 20D high/low: 62.38 / 54.94

### Relative Strength

- ratio: 0.914127
- ratio_MA60: 0.937701
- ratio_gap: -2.51%
- ratio_slope_proxy(20d): -0.010280

### Volume (if available)

- volume: 11598300.00
- volume_MA20: 9120965.00
- volume_ratio: 1.27

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 26.00
- MA20 / MA60 / MA200: 22.93 / 20.28 / 18.02
- gap20 / gap60: 13.38% / 28.23%
- 5D return: 2.77%
- 20D high/low: 26.00 / 20.37

### Relative Strength

- ratio: 0.621563
- ratio_MA60: 0.540445
- ratio_gap: 15.01%
- ratio_slope_proxy(20d): 0.031863

### Volume (if available)

- volume: 24018900.00
- volume_MA20: 24649405.00
- volume_ratio: 0.97

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

- close: 5.62
- MA20 / MA60 / MA200: 5.43 / 5.56 / 5.75
- gap20 / gap60: 3.43% / 1.15%
- 5D return: 2.00%
- 20D high/low: 5.65 / 5.17

### Relative Strength

- ratio: 0.014705
- ratio_MA60: 0.013861
- ratio_gap: 6.09%
- ratio_slope_proxy(20d): 0.000119

### Volume (if available)

- volume: 51086000.00
- volume_MA20: 39556540.00
- volume_ratio: 1.29

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.72
- MA20 / MA60 / MA200: 13.08 / 13.72 / 12.34
- gap20 / gap60: -2.74% / -7.28%
- 5D return: -3.34%
- 20D high/low: 13.84 / 12.50

### Relative Strength

- ratio: 0.043948
- ratio_MA60: 0.050221
- ratio_gap: -12.49%
- ratio_slope_proxy(20d): -0.000461

### Volume (if available)

- volume: 22590200.00
- volume_MA20: 13847350.00
- volume_ratio: 1.63

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

- 데이터 기준일(주가): **2026-10-16**
- 실행시간(UTC): **2026-10-17 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 53.0 bp / latest 3.23
- IG OAS 4주 변화: 6.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.78
- VIX: 16.46
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -1.07% / slope_proxy: 0.007097
- GDXJ/GLD gap: -3.38% / slope_proxy: 0.011954

## VZLA (Vizsla Silver)
- close: 3.25 | RSI14: 35.93482 | ATR14%: 5.68%
- MA20 gap: -11.19% | MA50 gap: -14.80% | MA200 gap: -16.08%
- vol_ratio(Volume/Vol20): 0.640984 | gap_open: 0.60%
- RS vs SILJ gap: -2.46% / slope_proxy: 0.002236
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
- close: 8.34 | RSI14: 44.488218 | ATR14%: 6.51%
- MA20 gap: -5.28% | MA50 gap: -8.71% | MA200 gap: -6.79%
- vol_ratio(Volume/Vol20): 0.923886 | gap_open: 0.36%
- SilverMarginGate: SI=57.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.94% / slope_proxy: 0.022099
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
- close: 17.17 | RSI14: 37.850823 | ATR14%: 7.55%
- MA20 gap: -10.23% | MA50 gap: -22.69% | MA200 gap: -44.01%
- vol_ratio(Volume/Vol20): 1.081835 | gap_open: 1.03%
- RS vs SILJ gap: -12.54% / slope_proxy: -0.051781
- RS vs GDXJ gap: -16.81% / slope_proxy: -0.017787
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

- 실행시간(UTC): **2026-10-17 03:01:13**
- 데이터 기준일(주가): **2026-10-16**

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

- HY OAS: 3.23 / 4주 변화 0.53 bp-ish / 2026-10-15
- IG OAS: 0.84 / 4주 변화 0.06 bp-ish / 2026-10-15
- 10Y Real Yield: 2.78 / 4주 변화 0.10 bp-ish / 2026-10-15
- VIX: 16.46 / 4주 변화 1.02 / 2026-10-15
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-09

### Leadership ratios

- GDX/GLD: gap -0.20% / slope_proxy -3.14%
- GDXJ/GLD: gap -3.38% / slope_proxy -6.57%
- SILJ/SLV: gap -1.07% / slope_proxy -0.29%
- Gold breadth proxy: above50 0.00%, above200 30.77%, count 13
- Silver breadth proxy: above50 0.00%, above200 15.38%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.63 | RSI14: 31.33 | ATR14%: 5.40%
- MA20/50/200 gap: -6.69% / -9.78% / -5.95%
- 5D return: -1.34% | 20D drawdown: -19.05% | vol_ratio: 1.22
- RS vs GDXJ: gap 0.64% / slope_proxy -2.26%
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

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.98 | RSI14: 41.44 | ATR14%: 3.83%
- MA20/50/200 gap: -4.25% / -8.96% / 12.41%
- 5D return: -4.06% | 20D drawdown: -13.65% | vol_ratio: 0.57
- RS vs GDXJ: gap 1.53% / slope_proxy -1.25%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.97 | RSI14: 27.78 | ATR14%: 8.10%
- MA20/50/200 gap: -12.65% / -28.28% / -33.70%
- 5D return: 3.19% | 20D drawdown: -36.18% | vol_ratio: 0.73
- RS vs GDXJ: gap -21.40% / slope_proxy -27.75%
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
- close: 2.14 | RSI14: 25.61 | ATR14%: 6.01%
- MA20/50/200 gap: -7.64% / -11.28% / 7.29%
- 5D return: 0.94% | 20D drawdown: -23.02% | vol_ratio: 1.70
- RS vs GDXJ: gap -1.58% / slope_proxy -7.17%
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
- close: 26.67 | RSI14: 50.93 | ATR14%: 4.37%
- MA20/50/200 gap: -1.84% / -2.91% / 30.98%
- 5D return: -2.74% | 20D drawdown: -12.21% | vol_ratio: 0.84
- RS vs SILJ: gap 13.02% / slope_proxy 7.96%
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
- close: 8.34 | RSI14: 39.57 | ATR14%: 5.73%
- MA20/50/200 gap: -5.28% / -8.71% / -6.79%
- 5D return: -8.45% | 20D drawdown: -12.67% | vol_ratio: 0.92
- RS vs SILJ: gap 6.94% / slope_proxy 7.22%
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
- close: 8.24 | RSI14: 35.71 | ATR14%: 4.44%
- MA20/50/200 gap: -6.28% / -16.24% / -16.60%
- 5D return: -4.74% | 20D drawdown: -21.60% | vol_ratio: 0.87
- RS vs SILJ: gap -2.86% / slope_proxy -5.57%
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
- close: 15.30 | RSI14: 33.71 | ATR14%: 4.56%
- MA20/50/200 gap: -10.07% / -17.33% / -19.54%
- 5D return: -10.37% | 20D drawdown: -19.60% | vol_ratio: 0.64
- RS vs SILJ: gap -4.16% / slope_proxy -3.20%
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
- close: 3.25 | RSI14: 26.45 | ATR14%: 5.14%
- MA20/50/200 gap: -11.19% / -14.80% / -16.08%
- 5D return: -8.45% | 20D drawdown: -24.42% | vol_ratio: 0.64
- RS vs SILJ: gap -2.46% / slope_proxy -7.30%
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
- close: 5.33 | RSI14: 42.31 | ATR14%: 4.69%
- MA20/50/200 gap: -4.73% / -17.97% / -23.32%
- 5D return: -3.96% | 20D drawdown: -17.87% | vol_ratio: 1.78
- RS vs SILJ: gap -5.95% / slope_proxy 0.13%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.78 | RSI14: 28.05 | ATR14%: 5.82%
- MA20/50/200 gap: -14.14% / -22.68% / -34.94%
- 5D return: -13.30% | 20D drawdown: -28.14% | vol_ratio: 0.99
- RS vs SILJ: gap -10.82% / slope_proxy -12.58%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 17.17 | RSI14: 34.42 | ATR14%: 6.20%
- MA20/50/200 gap: -10.23% / -22.69% / -44.01%
- 5D return: -10.53% | 20D drawdown: -24.33% | vol_ratio: 1.08
- RS vs SILJ: gap -12.54% / slope_proxy -2.91%
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
