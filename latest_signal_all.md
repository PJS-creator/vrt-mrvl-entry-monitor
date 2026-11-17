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

- 실행시간(UTC): **2026-11-17 15:01:22**
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

- QQQ close: 661.51
- Weekly RSI14: **42.21**
- 52W MA: 667.86 / gap: **-0.95%**
- 104W MA gap: **10.06%**
- 52W MA 13W slope: **4.44%**
- VXN: **32.90** / 5D change: 3.93

## Daily trigger: 실제 매수 타이밍

- QQQ close: 661.50
- Daily RSI14: **37.71**
- 20D gap: **-4.10%**
- 50D gap: **-7.54%**
- 200D gap: **-2.95%**
- MACD hist: -1.1780 / change: -0.3248
- ATR14%: **2.36%**
- 20D high drawdown: **-8.84%**

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
- 실행시간(UTC): **2026-11-17 15:00:52**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.23 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.89 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.91 / 4주 변화 17.0 bp
- VIX (VIXCLS): 22.91
- NFCI: -0.462

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.987954
- MA60: 8.059169
- gap: -13.29%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.31923
- MA60: 0.402561
- gap: -20.70%
- MA60_slope_proxy: -0.005304
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-17**
- 실행시간(UTC): **2026-11-17 15:00:54**

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
- close: 592.6
- MA50: 649.4 / gap50: -8.75%
- MA200: 631.2418 / gap200: -6.12%

## Relative Strength
- RS vs FTSE gap: -10.14% / slope_proxy: -0.002634
- RS vs Peers gap: -2.98% / slope_proxy: 0.006092

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-17 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 87.15 / 5D 1.29%
- Brent ref (BZ=F): 93.86 / 5D 2.59%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.71
- Gas ref (NG=F): 3.08 / 5D -6.58%

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

- close: 57.84
- MA20 / MA60 / MA200: 59.98 / 59.63 / 56.57
- gap20 / gap60: -3.56% / -3.01%
- 5D return: 1.65%
- 20D high/low: 64.17 / 55.76

### Relative Strength

- ratio: 0.898904
- ratio_MA60: 0.922575
- ratio_gap: -2.57%
- ratio_slope_proxy(20d): -0.014225

### Volume (if available)

- volume: 764035.00
- volume_MA20: 10288136.75
- volume_ratio: 0.07

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.48
- MA20 / MA60 / MA200: 20.65 / 21.44 / 18.95
- gap20 / gap60: -15.37% / -18.47%
- 5D return: -4.38%
- 20D high/low: 26.16 / 17.30

### Relative Strength

- ratio: 0.559539
- ratio_MA60: 0.576303
- ratio_gap: -2.91%
- ratio_slope_proxy(20d): 0.032354

### Volume (if available)

- volume: 2326756.00
- volume_MA20: 26974592.80
- volume_ratio: 0.09

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

- close: 5.17
- MA20 / MA60 / MA200: 5.83 / 5.68 / 5.90
- gap20 / gap60: -11.31% / -8.92%
- 5D return: -0.10%
- 20D high/low: 6.94 / 5.10

### Relative Strength

- ratio: 0.014245
- ratio_MA60: 0.014431
- ratio_gap: -1.29%
- ratio_slope_proxy(20d): 0.000519

### Volume (if available)

- volume: 2668023.00
- volume_MA20: 40186051.15
- volume_ratio: 0.07

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

- close: 12.73
- MA20 / MA60 / MA200: 13.01 / 13.53 / 12.86
- gap20 / gap60: -2.09% / -5.90%
- 5D return: 6.12%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041604
- ratio_MA60: 0.047600
- ratio_gap: -12.60%
- ratio_slope_proxy(20d): -0.002503

### Volume (if available)

- volume: 798485.00
- volume_MA20: 15610244.25
- volume_ratio: 0.05

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
- 실행시간(UTC): **2026-11-17 15:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 3.23
- IG OAS 4주 변화: 4.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 17.0 bp / latest 2.91
- VIX: 22.91
- NFCI: -0.462

### Leadership ratios
- SILJ/SLV gap: 2.33% / slope_proxy: 0.003961
- GDXJ/GLD gap: -6.86% / slope_proxy: -0.002874

## VZLA (Vizsla Silver)
- close: 3.065 | RSI14: 43.249395 | ATR14%: 6.28%
- MA20 gap: -3.74% | MA50 gap: -12.29% | MA200 gap: -14.10%
- vol_ratio(Volume/Vol20): 0.296453 | gap_open: 1.19%
- RS vs SILJ gap: 3.74% / slope_proxy: 0.002275
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
- close: 7.47 | RSI14: 48.978895 | ATR14%: 7.64%
- MA20 gap: 2.79% | MA50 gap: -9.40% | MA200 gap: -11.37%
- vol_ratio(Volume/Vol20): 0.679591 | gap_open: 7.17%
- SilverMarginGate: SI=47.759998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.84% / slope_proxy: 0.00582
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
- close: 16.059999 | RSI14: 43.682422 | ATR14%: 9.37%
- MA20 gap: -5.68% | MA50 gap: -13.33% | MA200 gap: -43.60%
- vol_ratio(Volume/Vol20): 0.194285 | gap_open: 0.72%
- RS vs SILJ gap: 0.79% / slope_proxy: -0.048453
- RS vs GDXJ gap: -2.93% / slope_proxy: -0.016169
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

- 실행시간(UTC): **2026-11-17 15:01:21**
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

- HY OAS: 3.23 / 4주 변화 -0.08 bp-ish / 2026-11-13
- IG OAS: 0.89 / 4주 변화 0.04 bp-ish / 2026-11-13
- 10Y Real Yield: 2.91 / 4주 변화 0.13 bp-ish / 2026-11-13
- VIX: 22.91 / 4주 변화 4.47 / 2026-11-16
- NFCI: -0.46 / 4주 변화 0.05 / 2026-11-06

### Leadership ratios

- GDX/GLD: gap -2.24% / slope_proxy -0.51%
- GDXJ/GLD: gap -6.86% / slope_proxy -3.85%
- SILJ/SLV: gap 2.33% / slope_proxy 6.81%
- Gold breadth proxy: above50 0.00%, above200 23.08%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.07 | RSI14: 36.41 | ATR14%: 6.44%
- MA20/50/200 gap: -9.34% / -20.14% / -12.90%
- 5D return: -11.62% | 20D drawdown: -19.29% | vol_ratio: 0.10
- RS vs GDXJ: gap -8.98% / slope_proxy -10.04%
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
- close: 4.18 | RSI14: 28.78 | ATR14%: 10.03%
- MA20/50/200 gap: -21.69% / -35.56% / -38.01%
- 5D return: -25.22% | 20D drawdown: -33.55% | vol_ratio: 0.51
- RS vs GDXJ: gap -26.53% / slope_proxy -25.92%
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
- close: 0.68 | RSI14: 27.66 | ATR14%: 9.56%
- MA20/50/200 gap: -16.62% / -34.62% / -49.66%
- 5D return: -18.07% | 20D drawdown: -27.66% | vol_ratio: 0.88
- RS vs GDXJ: gap -28.13% / slope_proxy -19.36%
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
- close: 1.44 | RSI14: 34.86 | ATR14%: 8.53%
- MA20/50/200 gap: -13.23% / -30.86% / -26.10%
- 5D return: -16.28% | 20D drawdown: -25.39% | vol_ratio: 0.01
- RS vs GDXJ: gap -21.90% / slope_proxy -16.83%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.47 | RSI14: 49.74 | ATR14%: 7.94%
- MA20/50/200 gap: 2.79% / -9.40% / -11.37%
- 5D return: -1.32% | 20D drawdown: -8.57% | vol_ratio: 0.68
- RS vs SILJ: gap 6.84% / slope_proxy 3.86%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **58.3**
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
- close: 3.07 | RSI14: 44.14 | ATR14%: 6.81%
- MA20/50/200 gap: -3.74% / -12.29% / -14.10%
- 5D return: -7.68% | 20D drawdown: -12.43% | vol_ratio: 0.30
- RS vs SILJ: gap 3.74% / slope_proxy 3.62%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 21.99 | RSI14: 39.44 | ATR14%: 7.63%
- MA20/50/200 gap: -9.01% / -15.65% / 3.81%
- 5D return: -12.63% | 20D drawdown: -17.86% | vol_ratio: 0.16
- RS vs SILJ: gap 0.58% / slope_proxy -6.06%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.30 | RSI14: 42.11 | ATR14%: 6.94%
- MA20/50/200 gap: -4.93% / -14.48% / -22.75%
- 5D return: -9.48% | 20D drawdown: -12.41% | vol_ratio: 0.11
- RS vs SILJ: gap -0.47% / slope_proxy -0.14%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 12.80 | RSI14: 37.78 | ATR14%: 7.06%
- MA20/50/200 gap: -8.86% / -20.54% / -28.29%
- 5D return: -10.46% | 20D drawdown: -16.97% | vol_ratio: 0.09
- RS vs SILJ: gap -7.26% / slope_proxy -4.00%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.32 | RSI14: 31.52 | ATR14%: 11.20%
- MA20/50/200 gap: -21.61% / -40.42% / -57.04%
- 5D return: -23.34% | 20D drawdown: -35.69% | vol_ratio: 0.13
- RS vs SILJ: gap -31.10% / slope_proxy -26.95%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 16.06 | RSI14: 45.13 | ATR14%: 10.56%
- MA20/50/200 gap: -5.68% / -13.33% / -43.60%
- 5D return: -14.89% | 20D drawdown: -24.49% | vol_ratio: 0.19
- RS vs SILJ: gap 0.79% / slope_proxy 6.50%
- FundamentalScore: 42 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **43.9**
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
- close: 4.17 | RSI14: 37.99 | ATR14%: 7.12%
- MA20/50/200 gap: -8.78% / -21.53% / -36.99%
- 5D return: -10.13% | 20D drawdown: -19.96% | vol_ratio: 0.16
- RS vs SILJ: gap -9.86% / slope_proxy -9.08%
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

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
