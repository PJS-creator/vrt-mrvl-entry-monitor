# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-17 22:35:59**
- 데이터 기준일(일봉): **2026-11-17**
- 데이터 기준일(주봉): **2026-11-16**
- VXN 기준일: **2026-11-16** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 656.95
- Weekly RSI14: **41.38**
- 52W MA: 667.77 / gap: **-1.62%**
- 104W MA gap: **9.31%**
- 52W MA 13W slope: **4.42%**
- VXN: **32.90** / 5D change: 3.93

## Daily trigger: 실제 매수 타이밍

- QQQ close: 656.95
- Daily RSI14: **36.55**
- 20D gap: **-4.73%**
- 50D gap: **-8.17%**
- 200D gap: **-3.61%**
- MACD hist: -1.4684 / change: -0.6151
- ATR14%: **2.52%**
- 20D high drawdown: **-9.46%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-11-17**
- 실행시간(UTC): **2026-11-17 22:35:27**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.34 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.9 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.92 / 4주 변화 12.0 bp
- VIX (VIXCLS): 22.91
- NFCI: -0.462

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.986055
- MA60: 8.059138
- gap: -13.32%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.323278
- MA60: 0.402628
- gap: -19.71%
- MA60_slope_proxy: -0.005237
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-17**
- 실행시간(UTC): **2026-11-17 22:35:31**

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
- TERM_SPREAD_10Y_POLICY: 130.11 bp / 4주 변화 -24.76 bp
- CURVE_10s5s: 34.85 bp / 4주 변화 -4.88 bp

## NWG Price
- close: 588.6
- MA50: 649.32 / gap50: -9.35%
- MA200: 631.2218 / gap200: -6.75%

## Relative Strength
- RS vs FTSE gap: -10.09% / slope_proxy: -0.002634
- RS vs Peers gap: -2.59% / slope_proxy: 0.006158

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-17 22:35:38**

## Commodity Regime

- WTI ref (CL=F): 85.61 / 5D -0.50%
- Brent ref (BZ=F): 93.07 / 5D 1.73%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.46
- Gas ref (NG=F): 3.20 / 5D -2.97%

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

- close: 56.52
- MA20 / MA60 / MA200: 59.91 / 59.61 / 56.56
- gap20 / gap60: -5.66% / -5.19%
- 5D return: -0.67%
- 20D high/low: 64.17 / 55.76

### Relative Strength

- ratio: 0.892045
- ratio_MA60: 0.922460
- ratio_gap: -3.30%
- ratio_slope_proxy(20d): -0.014339

### Volume (if available)

- volume: 8711601.00
- volume_MA20: 10685515.05
- volume_ratio: 0.82

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.41
- MA20 / MA60 / MA200: 20.65 / 21.44 / 18.95
- gap20 / gap60: -15.69% / -18.79%
- 5D return: -4.76%
- 20D high/low: 26.16 / 17.30

### Relative Strength

- ratio: 0.561251
- ratio_MA60: 0.576331
- ratio_gap: -2.62%
- ratio_slope_proxy(20d): 0.032383

### Volume (if available)

- volume: 14640864.00
- volume_MA20: 27590298.20
- volume_ratio: 0.53

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.04
- MA20 / MA60 / MA200: 5.83 / 5.68 / 5.90
- gap20 / gap60: -13.52% / -11.27%
- 5D return: -2.70%
- 20D high/low: 6.94 / 5.04

### Relative Strength

- ratio: 0.014222
- ratio_MA60: 0.014431
- ratio_gap: -1.45%
- ratio_slope_proxy(20d): 0.000519

### Volume (if available)

- volume: 29207609.00
- volume_MA20: 41513030.45
- volume_ratio: 0.70

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

- close: 12.50
- MA20 / MA60 / MA200: 12.99 / 13.53 / 12.86
- gap20 / gap60: -3.81% / -7.60%
- 5D return: 4.17%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041395
- ratio_MA60: 0.047596
- ratio_gap: -13.03%
- ratio_slope_proxy(20d): -0.002506

### Volume (if available)

- volume: 8751520.00
- volume_MA20: 16007896.00
- volume_ratio: 0.55

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

- 데이터 기준일(주가): **2026-11-17**
- 실행시간(UTC): **2026-11-17 22:35:45**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 3.34
- IG OAS 4주 변화: 3.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.92
- VIX: 22.91
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 1.46% / slope_proxy: 0.003886
- GDXJ/GLD gap: -8.01% / slope_proxy: -0.002932

## VZLA (Vizsla Silver)
- close: 2.97 | RSI14: 39.564894 | ATR14%: 6.53%
- MA20 gap: -6.59% | MA50 gap: -14.96% | MA200 gap: -16.76%
- vol_ratio(Volume/Vol20): 2.04884 | gap_open: 1.19%
- RS vs SILJ gap: 2.45% / slope_proxy: 0.002246
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
- close: 7.41 | RSI14: 48.409037 | ATR14%: 7.76%
- MA20 gap: 2.01% | MA50 gap: -10.11% | MA200 gap: -12.08%
- vol_ratio(Volume/Vol20): 2.40688 | gap_open: 7.17%
- SilverMarginGate: SI=47.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.96% / slope_proxy: 0.005879
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## HYMC (Hycroft Mining)
- close: 15.69 | RSI14: 42.020793 | ATR14%: 9.59%
- MA20 gap: -7.75% | MA50 gap: -15.29% | MA200 gap: -44.90%
- vol_ratio(Volume/Vol20): 1.204404 | gap_open: 0.72%
- RS vs SILJ gap: 0.33% / slope_proxy: -0.048508
- RS vs GDXJ gap: -3.66% / slope_proxy: -0.016189
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

- 실행시간(UTC): **2026-11-17 22:35:58**
- 데이터 기준일(주가): **2026-11-17**

## Verdict
**🟡 Precious miners watch/add-on candidates: SCZM**

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

- HY OAS: 3.34 / 4주 변화 0.05 bp-ish / 2026-11-16
- IG OAS: 0.90 / 4주 변화 0.03 bp-ish / 2026-11-16
- 10Y Real Yield: 2.92 / 4주 변화 0.18 bp-ish / 2026-11-16
- VIX: 22.91 / 4주 변화 4.47 / 2026-11-16
- NFCI: -0.46 / 4주 변화 0.05 / 2026-11-06

### Leadership ratios

- GDX/GLD: gap -3.06% / slope_proxy -1.35%
- GDXJ/GLD: gap -8.01% / slope_proxy -5.05%
- SILJ/SLV: gap 1.46% / slope_proxy 5.89%
- Gold breadth proxy: above50 7.69%, above200 7.69%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 4.05 | RSI14: 26.41 | ATR14%: 10.42%
- MA20/50/200 gap: -24.04% / -37.54% / -39.93%
- 5D return: -27.55% | 20D drawdown: -35.61% | vol_ratio: 1.49
- RS vs GDXJ: gap -27.67% / slope_proxy -27.09%
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
- close: 6.98 | RSI14: 34.86 | ATR14%: 6.52%
- MA20/50/200 gap: -10.44% / -21.14% / -14.01%
- 5D return: -12.75% | 20D drawdown: -20.32% | vol_ratio: 0.88
- RS vs GDXJ: gap -8.73% / slope_proxy -9.78%
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
- close: 0.63 | RSI14: 25.00 | ATR14%: 11.17%
- MA20/50/200 gap: -22.51% / -39.36% / -53.35%
- 5D return: -24.10% | 20D drawdown: -32.98% | vol_ratio: 4.43
- RS vs GDXJ: gap -32.31% / slope_proxy -24.11%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.0**
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
- close: 1.45 | RSI14: 35.19 | ATR14%: 8.77%
- MA20/50/200 gap: -12.65% / -30.39% / -25.59%
- 5D return: -15.70% | 20D drawdown: -24.87% | vol_ratio: 1.03
- RS vs GDXJ: gap -20.14% / slope_proxy -14.93%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.41 | RSI14: 49.23 | ATR14%: 8.06%
- MA20/50/200 gap: 2.01% / -10.11% / -12.08%
- 5D return: -2.11% | 20D drawdown: -9.30% | vol_ratio: 2.41
- RS vs SILJ: gap 7.96% / slope_proxy 4.97%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **63.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 2.97 | RSI14: 40.76 | ATR14%: 7.08%
- MA20/50/200 gap: -6.59% / -14.96% / -16.76%
- 5D return: -10.54% | 20D drawdown: -15.14% | vol_ratio: 2.05
- RS vs SILJ: gap 2.45% / slope_proxy 2.31%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **62.6**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.13 | RSI14: 39.71 | ATR14%: 7.21%
- MA20/50/200 gap: -7.10% / -16.49% / -24.60%
- 5D return: -11.65% | 20D drawdown: -14.51% | vol_ratio: 1.31
- RS vs SILJ: gap -1.01% / slope_proxy -0.69%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **58.4**
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 21.56 | RSI14: 37.72 | ATR14%: 7.78%
- MA20/50/200 gap: -10.71% / -17.27% / 1.79%
- 5D return: -14.34% | 20D drawdown: -19.46% | vol_ratio: 1.00
- RS vs SILJ: gap 0.48% / slope_proxy -6.15%
- FundamentalScore: 86 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **55.0**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.26 | RSI14: 30.25 | ATR14%: 11.69%
- MA20/50/200 gap: -23.40% / -41.82% / -58.06%
- 5D return: -25.17% | 20D drawdown: -37.22% | vol_ratio: 1.20
- RS vs SILJ: gap -31.46% / slope_proxy -27.34%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 12.50 | RSI14: 35.60 | ATR14%: 7.22%
- MA20/50/200 gap: -10.87% / -22.34% / -29.94%
- 5D return: -12.53% | 20D drawdown: -18.88% | vol_ratio: 0.75
- RS vs SILJ: gap -7.68% / slope_proxy -4.44%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **51.4**
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.69 | RSI14: 43.65 | ATR14%: 10.81%
- MA20/50/200 gap: -7.75% / -15.29% / -44.90%
- 5D return: -16.85% | 20D drawdown: -26.23% | vol_ratio: 1.20
- RS vs SILJ: gap 0.33% / slope_proxy 6.01%
- FundamentalScore: 42 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **49.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.09 | RSI14: 36.00 | ATR14%: 7.26%
- MA20/50/200 gap: -10.45% / -23.01% / -38.20%
- 5D return: -11.85% | 20D drawdown: -21.50% | vol_ratio: 1.18
- RS vs SILJ: gap -9.92% / slope_proxy -9.14%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **48.5**
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

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
