# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-30 02:07:52**
- 데이터 기준일(일봉): **2026-10-29**
- 데이터 기준일(주봉): **2026-10-26**
- VXN 기준일: **2026-10-28** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **B: QLD 부분 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **500,000원** (25%)
- 대기자금: **0원** (0%)

## Weekly gate: 큰 환경

- QQQ close: 715.34
- Weekly RSI14: **53.39**
- 52W MA: 664.54 / gap: **7.64%**
- 104W MA gap: **19.92%**
- 52W MA 13W slope: **5.35%**
- VXN: **23.78** / 5D change: -0.64

## Daily trigger: 실제 매수 타이밍

- QQQ close: 715.34
- Daily RSI14: **44.45**
- 20D gap: **-2.16%**
- 50D gap: **-1.35%**
- 200D gap: **5.51%**
- MACD hist: -1.8046 / change: 0.2480
- ATR14%: **1.57%**
- 20D high drawdown: **-5.83%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **True**
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

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-30 02:07:29**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.14 / 4주 변화 2.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.67 / 4주 변화 -26.0 bp
- VIX (VIXCLS): 16.91
- NFCI: -0.487

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.622721
- MA60: 8.402691
- gap: 2.62%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.388734
- MA60: 0.417112
- gap: -6.80%
- MA60_slope_proxy: 0.027278
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-30 02:07:32**

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
- TERM_SPREAD_10Y_POLICY: 155.46 bp / 4주 변화 -5.94 bp
- CURVE_10s5s: 36.02 bp / 4주 변화 -6.81 bp

## NWG Price
- close: 646.8
- MA50: 675.04 / gap50: -4.18%
- MA200: 635.5058 / gap200: 1.78%

## Relative Strength
- RS vs FTSE gap: -4.71% / slope_proxy: -0.000668
- RS vs Peers gap: 7.04% / slope_proxy: 0.023668

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-30 02:07:39**

## Commodity Regime

- WTI ref (CL=F): 104.38 / 5D 4.94%
- Brent ref (BZ=F): 113.42 / 5D 0.22%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.04
- Gas ref (NG=F): 2.90 / 5D 3.72%

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

- close: 63.01
- MA20 / MA60 / MA200: 61.41 / 59.72 / 55.60
- gap20 / gap60: 2.60% / 5.51%
- 5D return: 0.82%
- 20D high/low: 64.17 / 58.08

### Relative Strength

- ratio: 0.917043
- ratio_MA60: 0.933688
- ratio_gap: -1.78%
- ratio_slope_proxy(20d): -0.011581

### Volume (if available)

- volume: 7041600.00
- volume_MA20: 8396025.00
- volume_ratio: 0.84

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.90
- MA20 / MA60 / MA200: 24.46 / 21.18 / 18.60
- gap20 / gap60: -10.46% / 3.40%
- 5D return: -14.52%
- 20D high/low: 26.16 / 21.65

### Relative Strength

- ratio: 0.660833
- ratio_MA60: 0.559448
- ratio_gap: 18.12%
- ratio_slope_proxy(20d): 0.036275

### Volume (if available)

- volume: 28407900.00
- volume_MA20: 30045800.00
- volume_ratio: 0.95

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

- close: 6.69
- MA20 / MA60 / MA200: 5.86 / 5.73 / 5.85
- gap20 / gap60: 14.25% / 16.85%
- 5D return: 10.03%
- 20D high/low: 6.71 / 5.17

### Relative Strength

- ratio: 0.016401
- ratio_MA60: 0.014213
- ratio_gap: 15.39%
- ratio_slope_proxy(20d): 0.000455

### Volume (if available)

- volume: 44735500.00
- volume_MA20: 41601115.00
- volume_ratio: 1.08

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.77
- MA20 / MA60 / MA200: 13.34 / 13.80 / 12.63
- gap20 / gap60: 10.71% / 7.04%
- 5D return: 15.30%
- 20D high/low: 14.77 / 12.50

### Relative Strength

- ratio: 0.046310
- ratio_MA60: 0.049541
- ratio_gap: -6.52%
- ratio_slope_proxy(20d): -0.001442

### Volume (if available)

- volume: 16719400.00
- volume_MA20: 14218785.00
- volume_ratio: 1.18

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

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-30 02:07:43**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.14
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: -26.0 bp / latest 2.67
- VIX: 16.91
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -0.24% / slope_proxy: 0.006436
- GDXJ/GLD gap: -8.65% / slope_proxy: 0.008105

## VZLA (Vizsla Silver)
- close: 3.29 | RSI14: 44.176804 | ATR14%: 5.47%
- MA20 gap: -1.30% | MA50 gap: -11.49% | MA200 gap: -12.53%
- vol_ratio(Volume/Vol20): 0.850602 | gap_open: 3.07%
- RS vs SILJ gap: 6.01% / slope_proxy: 0.000422
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
- close: 7.24 | RSI14: 37.513334 | ATR14%: 6.82%
- MA20 gap: -11.11% | MA50 gap: -18.73% | MA200 gap: -17.97%
- vol_ratio(Volume/Vol20): 0.59911 | gap_open: 3.47%
- SilverMarginGate: SI=51.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.26% / slope_proxy: 0.019071
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
- close: 17.27 | RSI14: 44.969222 | ATR14%: 6.90%
- MA20 gap: -0.71% | MA50 gap: -15.24% | MA200 gap: -42.70%
- vol_ratio(Volume/Vol20): 0.869455 | gap_open: 4.01%
- RS vs SILJ gap: -2.60% / slope_proxy: -0.048432
- RS vs GDXJ gap: -5.15% / slope_proxy: -0.016594
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

- 실행시간(UTC): **2026-10-30 02:07:51**
- 데이터 기준일(주가): **2026-10-29**

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

- HY OAS: 3.14 / 4주 변화 0.02 bp-ish / 2026-10-28
- IG OAS: 0.86 / 4주 변화 0.02 bp-ish / 2026-10-28
- 10Y Real Yield: 2.67 / 4주 변화 -0.24 bp-ish / 2026-10-28
- VIX: 16.91 / 4주 변화 0.57 / 2026-10-28
- NFCI: -0.49 / 4주 변화 0.02 / 2026-10-23

### Leadership ratios

- GDX/GLD: gap -5.32% / slope_proxy -4.44%
- GDXJ/GLD: gap -8.66% / slope_proxy -8.40%
- SILJ/SLV: gap -0.24% / slope_proxy 1.49%
- Gold breadth proxy: above50 0.00%, above200 7.69%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.82 | RSI14: 24.67 | ATR14%: 4.66%
- MA20/50/200 gap: -9.96% / -18.33% / -3.29%
- 5D return: -2.49% | 20D drawdown: -16.45% | vol_ratio: 1.67
- RS vs GDXJ: gap -4.72% / slope_proxy -4.92%
- FundamentalScore: 88 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **56.1**
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
- close: 5.61 | RSI14: 31.19 | ATR14%: 6.16%
- MA20/50/200 gap: -11.93% / -21.89% / -19.53%
- 5D return: -1.06% | 20D drawdown: -20.31% | vol_ratio: 0.42
- RS vs GDXJ: gap -7.64% / slope_proxy -9.94%
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
- close: 0.85 | RSI14: 40.00 | ATR14%: 7.48%
- MA20/50/200 gap: -9.24% / -31.84% / -40.52%
- 5D return: 1.19% | 20D drawdown: -17.48% | vol_ratio: 0.49
- RS vs GDXJ: gap -21.76% / slope_proxy -6.24%
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
- close: 1.65 | RSI14: 27.62 | ATR14%: 8.01%
- MA20/50/200 gap: -17.25% / -29.73% / -16.87%
- 5D return: -7.30% | 20D drawdown: -25.34% | vol_ratio: 0.75
- RS vs GDXJ: gap -16.29% / slope_proxy -15.67%
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
- close: 24.45 | RSI14: 33.77 | ATR14%: 5.12%
- MA20/50/200 gap: -5.56% / -9.86% / 17.55%
- 5D return: 2.47% | 20D drawdown: -11.12% | vol_ratio: 0.49
- RS vs SILJ: gap 7.88% / slope_proxy 2.85%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.29 | RSI14: 40.15 | ATR14%: 5.26%
- MA20/50/200 gap: -1.30% / -11.49% / -12.53%
- 5D return: 3.13% | 20D drawdown: -8.86% | vol_ratio: 0.85
- RS vs SILJ: gap 6.01% / slope_proxy 3.96%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **52.4**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.45 | RSI14: 29.27 | ATR14%: 4.96%
- MA20/50/200 gap: -7.20% / -19.08% / -22.74%
- 5D return: 2.41% | 20D drawdown: -15.99% | vol_ratio: 1.28
- RS vs SILJ: gap -2.75% / slope_proxy -4.16%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **51.6**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.76 | RSI14: 35.50 | ATR14%: 4.95%
- MA20/50/200 gap: -5.06% / -17.46% / -20.63%
- 5D return: 1.44% | 20D drawdown: -10.50% | vol_ratio: 0.86
- RS vs SILJ: gap -1.97% / slope_proxy 2.93%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.24 | RSI14: 25.71 | ATR14%: 6.34%
- MA20/50/200 gap: -11.11% / -18.73% / -17.97%
- 5D return: 1.54% | 20D drawdown: -20.53% | vol_ratio: 0.60
- RS vs SILJ: gap -2.26% / slope_proxy -6.15%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.07 | RSI14: 17.59 | ATR14%: 7.07%
- MA20/50/200 gap: -18.52% / -32.65% / -46.25%
- 5D return: -3.76% | 20D drawdown: -31.32% | vol_ratio: 0.92
- RS vs SILJ: gap -20.19% / slope_proxy -20.77%
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
- close: 4.61 | RSI14: 29.74 | ATR14%: 5.81%
- MA20/50/200 gap: -10.37% / -24.30% / -33.08%
- 5D return: -3.35% | 20D drawdown: -17.38% | vol_ratio: 0.95
- RS vs SILJ: gap -11.01% / slope_proxy -5.24%
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
- close: 17.27 | RSI14: 38.98 | ATR14%: 6.62%
- MA20/50/200 gap: -0.71% / -15.24% / -42.70%
- 5D return: 9.58% | 20D drawdown: -10.01% | vol_ratio: 0.87
- RS vs SILJ: gap -2.60% / slope_proxy 5.30%
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
