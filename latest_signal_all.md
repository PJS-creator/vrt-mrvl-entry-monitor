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

- 실행시간(UTC): **2026-08-23 03:01:18**
- 데이터 기준일(일봉): **2026-08-21**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-20** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 713.44
- Weekly RSI14: **57.56**
- 52W MA: 640.15 / gap: **11.45%**
- 104W MA gap: **24.42%**
- 52W MA 13W slope: **6.91%**
- VXN: **23.26** / 5D change: 2.03

## Daily trigger: 실제 매수 타이밍

- QQQ close: 713.44
- Daily RSI14: **50.17**
- 20D gap: **0.60%**
- 50D gap: **0.01%**
- 200D gap: **9.47%**
- MACD hist: -0.0339 / change: -0.5923
- ATR14%: **1.59%**
- 20D high drawdown: **-2.54%**

## Checks

- weekly_good: **False**
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

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-23 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.35 / 4주 변화 -8.0 bp
- VIX (VIXCLS): 16.01
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.268624
- MA60: 9.227424
- gap: -10.39%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.422968
- MA60: 0.400933
- gap: 5.50%
- MA60_slope_proxy: 0.018202
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-23 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 129.01 bp / 4주 변화 -0.23 bp
- CURVE_10s5s: 48.56 bp / 4주 변화 1.84 bp

## NWG Price
- close: 683.8
- MA50: 675.8588 / gap50: 1.18%
- MA200: 623.7639 / gap200: 9.62%

## Relative Strength
- RS vs FTSE gap: 1.22% / slope_proxy: 0.002953
- RS vs Peers gap: 1.33% / slope_proxy: 0.016548

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-23 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 87.06 / 5D 5.66%
- Brent ref (BZ=F): 94.39 / 5D 6.63%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.33
- Gas ref (NG=F): 2.77 / 5D 1.46%

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

- close: 61.30
- MA20 / MA60 / MA200: 57.41 / 55.25 / 51.19
- gap20 / gap60: 6.77% / 10.94%
- 5D return: 5.04%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.963231
- ratio_MA60: 0.961810
- ratio_gap: 0.15%
- ratio_slope_proxy(20d): -0.012941

### Volume (if available)

- volume: 6451000.00
- volume_MA20: 8360550.00
- volume_ratio: 0.77

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.15
- MA20 / MA60 / MA200: 18.44 / 17.84 / 16.61
- gap20 / gap60: 3.87% / 7.34%
- 5D return: 7.10%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.546206
- ratio_MA60: 0.511072
- ratio_gap: 6.87%
- ratio_slope_proxy(20d): -0.006244

### Volume (if available)

- volume: 17485800.00
- volume_MA20: 16123775.00
- volume_ratio: 1.08

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

- close: 5.92
- MA20 / MA60 / MA200: 5.49 / 5.49 / 5.47
- gap20 / gap60: 7.91% / 7.88%
- 5D return: 2.78%
- 20D high/low: 6.01 / 4.95

### Relative Strength

- ratio: 0.014254
- ratio_MA60: 0.013847
- ratio_gap: 2.94%
- ratio_slope_proxy(20d): -0.000536

### Volume (if available)

- volume: 29506200.00
- volume_MA20: 45424040.00
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.21
- MA20 / MA60 / MA200: 13.44 / 12.72 / 11.04
- gap20 / gap60: 5.72% / 11.68%
- 5D return: 1.57%
- 20D high/low: 14.29 / 12.17

### Relative Strength

- ratio: 0.051205
- ratio_MA60: 0.050564
- ratio_gap: 1.27%
- ratio_slope_proxy(20d): -0.000580

### Volume (if available)

- volume: 11475300.00
- volume_MA20: 13883820.00
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-23 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.75
- IG OAS 4주 변화: 3.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -8.0 bp / latest 2.35
- VIX: 16.01
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 7.41% / slope_proxy: 0.020483
- GDXJ/GLD gap: 15.00% / slope_proxy: 0.001335

## VZLA (Vizsla Silver)
- close: 3.96 | RSI14: 64.080169 | ATR14%: 4.71%
- MA20 gap: 10.80% | MA50 gap: 16.37% | MA200 gap: -2.80%
- vol_ratio(Volume/Vol20): 2.171241 | gap_open: 3.36%
- RS vs SILJ gap: -2.84% / slope_proxy: 0.004125
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

## SCZM (Santacruz Silver)
- close: 9.675 | RSI14: 70.575673 | ATR14%: 5.74%
- MA20 gap: 20.07% | MA50 gap: 34.39% | MA200 gap: 12.26%
- vol_ratio(Volume/Vol20): 1.422385 | gap_open: 5.12%
- SilverMarginGate: SI=69.466003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.10% / slope_proxy: 0.001645
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

## HYMC (Hycroft Mining)
- close: 27.07 | RSI14: 57.575152 | ATR14%: 7.18%
- MA20 gap: 11.71% | MA50 gap: 16.45% | MA200 gap: -7.01%
- vol_ratio(Volume/Vol20): 1.520446 | gap_open: 4.82%
- RS vs SILJ gap: -5.24% / slope_proxy: -0.116911
- RS vs GDXJ gap: -11.20% / slope_proxy: -0.031847
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

- 실행시간(UTC): **2026-08-23 03:01:15**
- 데이터 기준일(주가): **2026-08-21**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **True**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.75 / 4주 변화 -0.02 bp-ish / 2026-08-20
- IG OAS: 0.82 / 4주 변화 0.03 bp-ish / 2026-08-20
- 10Y Real Yield: 2.35 / 4주 변화 -0.08 bp-ish / 2026-08-20
- VIX: 16.01 / 4주 변화 -2.69 / 2026-08-20
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 16.24% / slope_proxy 20.16%
- GDXJ/GLD: gap 15.00% / slope_proxy 18.51%
- SILJ/SLV: gap 7.41% / slope_proxy 8.13%
- Gold breadth proxy: above50 100.00%, above200 92.31%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.88 | RSI14: 90.03 | ATR14%: 4.61%
- MA20/50/200 gap: 22.41% / 36.49% / 14.19%
- 5D return: 12.41% | 20D drawdown: 0.00% | vol_ratio: 1.34
- RS vs GDXJ: gap 7.70% / slope_proxy 9.05%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **79.7**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.54 | RSI14: 86.09 | ATR14%: 5.75%
- MA20/50/200 gap: 18.67% / 30.91% / 47.33%
- 5D return: 4.15% | 20D drawdown: 0.00% | vol_ratio: 0.93
- RS vs GDXJ: gap 4.55% / slope_proxy 9.30%
- FundamentalScore: 88 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **77.1**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.63 | RSI14: 84.72 | ATR14%: 5.50%
- MA20/50/200 gap: 18.33% / 28.45% / 10.07%
- 5D return: 6.54% | 20D drawdown: -1.21% | vol_ratio: 1.13
- RS vs GDXJ: gap 2.46% / slope_proxy 10.30%
- FundamentalScore: 70 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **74.2**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.49 | RSI14: 74.40 | ATR14%: 5.57%
- MA20/50/200 gap: 19.14% / 33.10% / 33.44%
- 5D return: 6.87% | 20D drawdown: 0.00% | vol_ratio: 0.82
- RS vs GDXJ: gap 6.61% / slope_proxy -3.33%
- FundamentalScore: 55 | TechnicalScore: 25 | RegimeScore: 100 | OverallScore: **53.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.65 | RSI14: 70.66 | ATR14%: 6.43%
- MA20/50/200 gap: 8.96% / 24.60% / 53.00%
- 5D return: 2.82% | 20D drawdown: -4.96% | vol_ratio: 1.10
- RS vs SILJ: gap 7.76% / slope_proxy 1.02%
- FundamentalScore: 86 | TechnicalScore: 80 | RegimeScore: 75 | OverallScore: **81.7**
- Checks:
  - sector_ok: **False**
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
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.62 | RSI14: 72.27 | ATR14%: 6.48%
- MA20/50/200 gap: 13.75% / 22.79% / 9.85%
- 5D return: -0.38% | 20D drawdown: -3.37% | vol_ratio: 1.50
- RS vs SILJ: gap 3.70% / slope_proxy 4.39%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.68 | RSI14: 80.97 | ATR14%: 6.24%
- MA20/50/200 gap: 20.07% / 34.39% / 12.26%
- 5D return: 9.32% | 20D drawdown: -0.87% | vol_ratio: 1.42
- RS vs SILJ: gap 14.10% / slope_proxy 19.67%
- FundamentalScore: 74 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **71.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.72 | RSI14: 80.45 | ATR14%: 5.23%
- MA20/50/200 gap: 21.75% / 28.76% / 11.11%
- 5D return: 12.79% | 20D drawdown: -0.48% | vol_ratio: 0.79
- RS vs SILJ: gap 8.89% / slope_proxy 6.46%
- FundamentalScore: 78 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **67.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.96 | RSI14: 73.03 | ATR14%: 4.70%
- MA20/50/200 gap: 10.80% / 16.37% / -2.80%
- 5D return: 5.32% | 20D drawdown: 0.00% | vol_ratio: 2.17
- RS vs SILJ: gap -2.84% / slope_proxy -6.91%
- FundamentalScore: 72 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **64.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.40 | RSI14: 72.53 | ATR14%: 6.12%
- MA20/50/200 gap: 13.10% / 17.72% / 9.15%
- 5D return: 5.41% | 20D drawdown: -2.63% | vol_ratio: 1.25
- RS vs SILJ: gap -0.98% / slope_proxy 1.50%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **56.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.39 | RSI14: 73.90 | ATR14%: 5.71%
- MA20/50/200 gap: 14.40% / 15.76% / -6.80%
- 5D return: 2.86% | 20D drawdown: 0.00% | vol_ratio: 1.44
- RS vs SILJ: gap -4.75% / slope_proxy 3.36%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 27.07 | RSI14: 66.96 | ATR14%: 7.60%
- MA20/50/200 gap: 11.71% / 16.45% / -7.01%
- 5D return: 0.00% | 20D drawdown: -2.97% | vol_ratio: 1.52
- RS vs SILJ: gap -5.24% / slope_proxy 3.41%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **44.4**
- Checks:
  - sector_ok: **False**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
