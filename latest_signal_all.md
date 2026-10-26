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

- 실행시간(UTC): **2026-10-26 15:01:34**
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

- QQQ close: 714.75
- Weekly RSI14: **53.25**
- 52W MA: 664.53 / gap: **7.56%**
- 104W MA gap: **19.82%**
- 52W MA 13W slope: **5.35%**
- VXN: **28.30** / 5D change: 1.17

## Daily trigger: 실제 매수 타이밍

- QQQ close: 714.75
- Daily RSI14: **43.32**
- 20D gap: **-2.64%**
- 50D gap: **-1.43%**
- 200D gap: **5.64%**
- MACD hist: -4.3565 / change: 0.8118
- ATR14%: **1.60%**
- 20D high drawdown: **-5.91%**

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
- 실행시간(UTC): **2026-10-26 15:00:57**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.38 / 4주 변화 45.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.64 / 4주 변화 -21.0 bp
- VIX (VIXCLS): 19.45
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.200072
- MA60: 8.428192
- gap: -14.57%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.429636
- MA60: 0.414355
- gap: 3.69%
- MA60_slope_proxy: 0.026218
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-26**
- 실행시간(UTC): **2026-10-26 15:01:01**

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
- close: 640.2
- MA50: 677.384 / gap50: -5.49%
- MA200: 635.3713 / gap200: 0.76%

## Relative Strength
- RS vs FTSE gap: -6.64% / slope_proxy: -0.000439
- RS vs Peers gap: 3.08% / slope_proxy: 0.021466

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-26 15:01:11**

## Commodity Regime

- WTI ref (CL=F): 101.04 / 5D -2.53%
- Brent ref (BZ=F): 110.13 / 5D 0.53%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.09
- Gas ref (NG=F): 3.02 / 5D -1.34%

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

- close: 63.88
- MA20 / MA60 / MA200: 60.38 / 59.30 / 55.29
- gap20 / gap60: 5.80% / 7.72%
- 5D return: 1.85%
- 20D high/low: 64.17 / 54.94

### Relative Strength

- ratio: 0.921191
- ratio_MA60: 0.934918
- ratio_gap: -1.47%
- ratio_slope_proxy(20d): -0.012308

### Volume (if available)

- volume: 2165768.00
- volume_MA20: 8532413.40
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.46
- MA20 / MA60 / MA200: 24.22 / 20.97 / 18.43
- gap20 / gap60: -11.41% / 2.33%
- 5D return: -16.06%
- 20D high/low: 26.16 / 20.65

### Relative Strength

- ratio: 0.650776
- ratio_MA60: 0.551648
- ratio_gap: 17.97%
- ratio_slope_proxy(20d): 0.033225

### Volume (if available)

- volume: 44843785.00
- volume_MA20: 25441084.25
- volume_ratio: 1.76

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

- close: 6.56
- MA20 / MA60 / MA200: 5.65 / 5.65 / 5.81
- gap20 / gap60: 16.14% / 16.04%
- 5D return: 11.38%
- 20D high/low: 6.56 / 5.17

### Relative Strength

- ratio: 0.016375
- ratio_MA60: 0.014074
- ratio_gap: 16.35%
- ratio_slope_proxy(20d): 0.000317

### Volume (if available)

- volume: 14782267.00
- volume_MA20: 38731728.35
- volume_ratio: 0.38

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.84
- MA20 / MA60 / MA200: 13.10 / 13.72 / 12.53
- gap20 / gap60: 5.64% / 0.82%
- 5D return: 8.00%
- 20D high/low: 14.00 / 12.50

### Relative Strength

- ratio: 0.046245
- ratio_MA60: 0.049694
- ratio_gap: -6.94%
- ratio_slope_proxy(20d): -0.001224

### Volume (if available)

- volume: 4576605.00
- volume_MA20: 13479735.25
- volume_ratio: 0.34

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
- 실행시간(UTC): **2026-10-26 15:01:19**

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
- 10Y Real Yield 4주 변화: -21.0 bp / latest 2.64
- VIX: 19.45
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.25% / slope_proxy: 0.007151
- GDXJ/GLD gap: -9.00% / slope_proxy: 0.009683

## VZLA (Vizsla Silver)
- close: 3.095 | RSI14: 34.763388 | ATR14%: 5.85%
- MA20 gap: -9.32% | MA50 gap: -17.32% | MA200 gap: -18.53%
- vol_ratio(Volume/Vol20): 0.301131 | gap_open: 0.32%
- RS vs SILJ gap: 1.73% / slope_proxy: 0.001032
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
- close: 7.0 | RSI14: 32.268903 | ATR14%: 7.33%
- MA20 gap: -16.23% | MA50 gap: -22.19% | MA200 gap: -21.17%
- vol_ratio(Volume/Vol20): 0.438303 | gap_open: 0.58%
- SilverMarginGate: SI=54.09 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.31% / slope_proxy: 0.021058
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
- close: 15.52 | RSI14: 32.553875 | ATR14%: 7.50%
- MA20 gap: -12.25% | MA50 gap: -25.79% | MA200 gap: -48.86%
- vol_ratio(Volume/Vol20): 0.239287 | gap_open: 0.06%
- RS vs SILJ gap: -11.74% / slope_proxy: -0.049293
- RS vs GDXJ gap: -15.61% / slope_proxy: -0.01675
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

- 실행시간(UTC): **2026-10-26 15:01:32**
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
- 10Y Real Yield: 2.64 / 4주 변화 -0.12 bp-ish / 2026-10-22
- VIX: 19.45 / 4주 변화 4.58 / 2026-10-23
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-16

### Leadership ratios

- GDX/GLD: gap -5.30% / slope_proxy -5.40%
- GDXJ/GLD: gap -9.00% / slope_proxy -9.85%
- SILJ/SLV: gap -5.25% / slope_proxy -3.97%
- Gold breadth proxy: above50 0.00%, above200 7.69%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.91 | RSI14: 31.84 | ATR14%: 4.88%
- MA20/50/200 gap: -10.98% / -18.33% / -1.80%
- 5D return: -11.56% | 20D drawdown: -17.03% | vol_ratio: 0.31
- RS vs GDXJ: gap -2.94% / slope_proxy -4.46%
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
- close: 5.55 | RSI14: 26.80 | ATR14%: 6.50%
- MA20/50/200 gap: -15.60% / -23.46% / -20.81%
- 5D return: -15.65% | 20D drawdown: -22.92% | vol_ratio: 0.30
- RS vs GDXJ: gap -8.30% / slope_proxy -11.80%
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
- close: 0.84 | RSI14: 32.50 | ATR14%: 7.53%
- MA20/50/200 gap: -13.45% / -34.76% / -41.84%
- 5D return: -11.58% | 20D drawdown: -26.32% | vol_ratio: 0.16
- RS vs GDXJ: gap -23.63% / slope_proxy -16.39%
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
- close: 1.72 | RSI14: 21.43 | ATR14%: 7.39%
- MA20/50/200 gap: -17.55% / -27.85% / -13.50%
- 5D return: -15.27% | 20D drawdown: -27.12% | vol_ratio: 0.68
- RS vs GDXJ: gap -12.92% / slope_proxy -17.31%
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
- close: 24.07 | RSI14: 32.34 | ATR14%: 5.40%
- MA20/50/200 gap: -8.19% / -11.56% / 16.41%
- 5D return: -9.31% | 20D drawdown: -12.50% | vol_ratio: 0.16
- RS vs SILJ: gap 9.06% / slope_proxy 4.66%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.57 | RSI14: 32.38 | ATR14%: 5.19%
- MA20/50/200 gap: -8.79% / -20.77% / -23.00%
- 5D return: -8.41% | 20D drawdown: -13.44% | vol_ratio: 0.35
- RS vs SILJ: gap -2.60% / slope_proxy 2.14%
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
- close: 13.98 | RSI14: 25.24 | ATR14%: 5.27%
- MA20/50/200 gap: -12.24% / -22.86% / -25.79%
- 5D return: -7.11% | 20D drawdown: -18.72% | vol_ratio: 0.18
- RS vs SILJ: gap -4.05% / slope_proxy -3.81%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.00 | RSI14: 26.89 | ATR14%: 6.94%
- MA20/50/200 gap: -16.23% / -22.19% / -21.17%
- 5D return: -16.57% | 20D drawdown: -23.16% | vol_ratio: 0.44
- RS vs SILJ: gap -3.31% / slope_proxy -7.96%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **44.6**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.10 | RSI14: 33.83 | ATR14%: 5.50%
- MA20/50/200 gap: -9.18% / -17.19% / -18.40%
- 5D return: -3.13% | 20D drawdown: -19.27% | vol_ratio: 0.30
- RS vs SILJ: gap 1.89% / slope_proxy -4.74%
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
- close: 3.08 | RSI14: 16.86 | ATR14%: 7.44%
- MA20/50/200 gap: -22.37% / -34.30% / -46.55%
- 5D return: -18.44% | 20D drawdown: -31.67% | vol_ratio: 0.36
- RS vs SILJ: gap -19.58% / slope_proxy -19.36%
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
- close: 4.64 | RSI14: 30.05 | ATR14%: 5.97%
- MA20/50/200 gap: -11.94% / -25.62% / -32.89%
- 5D return: -10.94% | 20D drawdown: -17.58% | vol_ratio: 0.49
- RS vs SILJ: gap -9.45% / slope_proxy -2.74%
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
- close: 15.54 | RSI14: 30.06 | ATR14%: 6.91%
- MA20/50/200 gap: -12.15% / -25.70% / -48.80%
- 5D return: -7.83% | 20D drawdown: -19.81% | vol_ratio: 0.24
- RS vs SILJ: gap -11.63% / slope_proxy -5.38%
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
