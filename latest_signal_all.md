# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-24 03:01:08**
- 데이터 기준일(일봉): **2026-06-23**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 713.65
- Weekly RSI14: **62.89**
- 52W MA: 617.57 / gap: **15.56%**
- 104W MA gap: **28.61%**
- 52W MA 13W slope: **8.50%**
- VXN: **27.67** / 5D change: 0.40

## Daily trigger: 실제 매수 타이밍

- QQQ close: 713.65
- Daily RSI14: **49.07**
- 20D gap: **-1.85%**
- 50D gap: **2.38%**
- 200D gap: **13.52%**
- MACD hist: -2.2693 / change: -1.2432
- ATR14%: **2.27%**
- 20D high drawdown: **-4.25%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-24 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.65 / 4주 변화 -9.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.28 / 4주 변화 12.0 bp
- VIX (VIXCLS): 17.28
- NFCI: -0.505

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.510606
- MA60: 9.21807
- gap: 3.17%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.448581
- MA60: 0.347011
- gap: 29.27%
- MA60_slope_proxy: 0.070211
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-24 03:00:42**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **True**
- MacroGreen: **True**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 97.13 bp / 4주 변화 -14.53 bp
- CURVE_10s5s: 44.9 bp / 4주 변화 0.24 bp

## NWG Price
- close: 657.2
- MA50: 595.1371 / gap50: 10.43%
- MA200: 593.7614 / gap200: 10.68%

## Relative Strength
- RS vs FTSE gap: 10.69% / slope_proxy: 0.001125
- RS vs Peers gap: 1.40% / slope_proxy: -0.01674

## Why not today?
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-24 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 72.32 / 5D -10.44%
- Brent ref (BZ=F): 76.18 / 5D -8.40%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.86
- Gas ref (NG=F): 3.19 / 5D 1.21%

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

- close: 52.23
- MA20 / MA60 / MA200: 55.95 / 57.56 / 48.80
- gap20 / gap60: -6.65% / -9.26%
- 5D return: -4.09%
- 20D high/low: 59.37 / 51.82

### Relative Strength

- ratio: 0.959053
- ratio_MA60: 1.003804
- ratio_gap: -4.46%
- ratio_slope_proxy(20d): 0.000019

### Volume (if available)

- volume: 9508414.00
- volume_MA20: 10363855.70
- volume_ratio: 0.92

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.03
- MA20 / MA60 / MA200: 17.95 / 19.71 / 15.41
- gap20 / gap60: -5.11% / -13.59%
- 5D return: -1.79%
- 20D high/low: 19.25 / 16.75

### Relative Strength

- ratio: 0.498682
- ratio_MA60: 0.528568
- ratio_gap: -5.65%
- ratio_slope_proxy(20d): 0.005780

### Volume (if available)

- volume: 9359600.00
- volume_MA20: 15288870.00
- volume_ratio: 0.61

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

- close: 5.29
- MA20 / MA60 / MA200: 5.95 / 6.37 / 5.07
- gap20 / gap60: -11.15% / -16.99%
- 5D return: -9.26%
- 20D high/low: 6.48 / 5.29

### Relative Strength

- ratio: 0.013757
- ratio_MA60: 0.015093
- ratio_gap: -8.85%
- ratio_slope_proxy(20d): -0.000711

### Volume (if available)

- volume: 20875992.00
- volume_MA20: 29971009.60
- volume_ratio: 0.70

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

- close: 11.21
- MA20 / MA60 / MA200: 12.24 / 12.99 / 10.81
- gap20 / gap60: -8.45% / -13.68%
- 5D return: -4.19%
- 20D high/low: 13.27 / 11.02

### Relative Strength

- ratio: 0.047861
- ratio_MA60: 0.051579
- ratio_gap: -7.21%
- ratio_slope_proxy(20d): 0.000543

### Volume (if available)

- volume: 7107601.00
- volume_MA20: 13989620.05
- volume_ratio: 0.51

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

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-24 03:00:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.65
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.28
- VIX: 17.28
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.20% / slope_proxy: 0.000204
- GDXJ/GLD gap: -4.84% / slope_proxy: -0.003174

## VZLA (Vizsla Silver)
- close: 3.35 | RSI14: 43.412914 | ATR14%: 6.79%
- MA20 gap: -7.73% | MA50 gap: -5.06% | MA200 gap: -21.15%
- vol_ratio(Volume/Vol20): 0.790676 | gap_open: 5.40%
- RS vs SILJ gap: 10.10% / slope_proxy: 0.004569
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
- close: 6.62 | RSI14: 40.137107 | ATR14%: 9.16%
- MA20 gap: -9.32% | MA50 gap: -18.49% | MA200 gap: -22.19%
- vol_ratio(Volume/Vol20): 0.815946 | gap_open: 4.67%
- SilverMarginGate: SI=61.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.93% / slope_proxy: -0.010228
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
- close: 23.139999 | RSI14: 33.366442 | ATR14%: 10.93%
- MA20 gap: -18.27% | MA50 gap: -32.73% | MA200 gap: -10.21%
- vol_ratio(Volume/Vol20): 1.01384 | gap_open: 5.51%
- RS vs SILJ gap: -22.75% / slope_proxy: -0.076426
- RS vs GDXJ gap: -21.51% / slope_proxy: -0.016667
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

- 실행시간(UTC): **2026-06-24 03:01:06**
- 데이터 기준일(주가): **2026-06-23**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA**

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

- HY OAS: 2.65 / 4주 변화 -0.07 bp-ish / 2026-06-22
- IG OAS: 0.74 / 4주 변화 0.00 bp-ish / 2026-06-22
- 10Y Real Yield: 2.28 / 4주 변화 0.10 bp-ish / 2026-06-22
- VIX: 17.28 / 4주 변화 0.69 / 2026-06-22
- NFCI: -0.51 / 4주 변화 0.06 / 2026-06-12

### Leadership ratios

- GDX/GLD: gap -3.56% / slope_proxy -3.72%
- GDXJ/GLD: gap -4.84% / slope_proxy -5.42%
- SILJ/SLV: gap 5.20% / slope_proxy 8.44%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.71 | RSI14: 39.76 | ATR14%: 6.60%
- MA20/50/200 gap: -3.53% / -2.84% / 16.97%
- 5D return: -2.90% | 20D drawdown: -11.38% | vol_ratio: 0.68
- RS vs GDXJ: gap 16.27% / slope_proxy 3.76%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.23 | RSI14: 43.53 | ATR14%: 7.75%
- MA20/50/200 gap: -5.82% / -9.65% / -17.93%
- 5D return: -16.33% | 20D drawdown: -16.33% | vol_ratio: 1.06
- RS vs GDXJ: gap 3.54% / slope_proxy 3.40%
- FundamentalScore: 70 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **56.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.27 | RSI14: 36.09 | ATR14%: 7.29%
- MA20/50/200 gap: -11.73% / -18.83% / -24.09%
- 5D return: -14.31% | 20D drawdown: -25.25% | vol_ratio: 1.34
- RS vs GDXJ: gap -7.03% / slope_proxy -4.62%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.57 | RSI14: 30.49 | ATR14%: 6.69%
- MA20/50/200 gap: -9.14% / -15.26% / -5.95%
- 5D return: -10.29% | 20D drawdown: -20.30% | vol_ratio: 0.63
- RS vs GDXJ: gap 0.27% / slope_proxy -1.01%
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
- close: 18.21 | RSI14: 38.25 | ATR14%: 8.28%
- MA20/50/200 gap: -4.79% / -1.77% / 19.50%
- 5D return: -11.82% | 20D drawdown: -15.26% | vol_ratio: 0.87
- RS vs SILJ: gap 15.59% / slope_proxy 12.16%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **63.7**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.35 | RSI14: 29.69 | ATR14%: 7.10%
- MA20/50/200 gap: -7.73% / -5.06% / -21.15%
- 5D return: -8.22% | 20D drawdown: -18.89% | vol_ratio: 0.79
- RS vs SILJ: gap 10.10% / slope_proxy 3.89%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **57.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.07 | RSI14: 34.22 | ATR14%: 6.83%
- MA20/50/200 gap: -6.88% / -14.18% / -15.40%
- 5D return: -9.54% | 20D drawdown: -15.34% | vol_ratio: 1.61
- RS vs SILJ: gap -2.56% / slope_proxy -1.10%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **56.6**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.01 | RSI14: 34.30 | ATR14%: 7.94%
- MA20/50/200 gap: -9.54% / -14.65% / -15.27%
- 5D return: -12.07% | 20D drawdown: -19.66% | vol_ratio: 0.75
- RS vs SILJ: gap -1.92% / slope_proxy -3.74%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **53.1**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.62 | RSI14: 35.43 | ATR14%: 9.58%
- MA20/50/200 gap: -9.32% / -18.49% / -22.19%
- 5D return: -12.32% | 20D drawdown: -20.53% | vol_ratio: 0.82
- RS vs SILJ: gap -5.93% / slope_proxy -5.13%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **49.6**
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.90 | RSI14: 31.91 | ATR14%: 9.43%
- MA20/50/200 gap: -11.51% / -17.06% / -12.69%
- 5D return: -14.93% | 20D drawdown: -23.79% | vol_ratio: 0.88
- RS vs SILJ: gap -3.30% / slope_proxy -3.53%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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
- close: 5.88 | RSI14: 33.82 | ATR14%: 8.81%
- MA20/50/200 gap: -10.42% / -13.63% / -9.71%
- 5D return: -13.91% | 20D drawdown: -20.75% | vol_ratio: 0.98
- RS vs SILJ: gap -0.21% / slope_proxy -1.69%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **43.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 23.14 | RSI14: 24.91 | ATR14%: 10.64%
- MA20/50/200 gap: -18.27% / -32.73% / -10.21%
- 5D return: -16.88% | 20D drawdown: -31.58% | vol_ratio: 1.01
- RS vs SILJ: gap -22.75% / slope_proxy -19.64%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **40.4**
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
