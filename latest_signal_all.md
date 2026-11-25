# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-25 15:01:24**
- 데이터 기준일(일봉): **2026-11-25**
- 데이터 기준일(주봉): **2026-11-23**
- VXN 기준일: **2026-11-24** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 638.10
- Weekly RSI14: **40.95**
- 52W MA: 667.26 / gap: **-4.37%**
- 104W MA gap: **6.03%**
- 52W MA 13W slope: **3.88%**
- VXN: **36.42** / 5D change: 1.98

## Daily trigger: 실제 매수 타이밍

- QQQ close: 617.57
- Daily RSI14: **35.52**
- 20D gap: **-7.26%**
- 50D gap: **-12.61%**
- 200D gap: **-9.51%**
- MACD hist: -3.5518 / change: -0.7302
- ATR14%: **3.49%**
- 20D high drawdown: **-13.67%**

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

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-25 15:01:03**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.63 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.97 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 2.79 / 4주 변화 13.0 bp
- VIX (VIXCLS): 26.36
- NFCI: -0.444

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.458805
- MA60: 7.890199
- gap: -18.14%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.304935
- MA60: 0.392752
- gap: -22.36%
- MA60_slope_proxy: -0.024053
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-25 15:01:05**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 117.93 bp / 4주 변화 -37.55 bp
- CURVE_10s5s: 31.63 bp / 4주 변화 -4.78 bp

## NWG Price
- close: 574.2
- MA50: 636.512 / gap50: -9.79%
- MA200: 629.5596 / gap200: -8.79%

## Relative Strength
- RS vs FTSE gap: -8.99% / slope_proxy: -0.002971
- RS vs Peers gap: 1.71% / slope_proxy: 0.001091

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-25 15:01:12**

## Commodity Regime

- WTI ref (CL=F): 83.12 / 5D -0.17%
- Brent ref (BZ=F): 89.75 / 5D -2.39%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.63
- Gas ref (NG=F): 3.65 / 5D 8.10%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.24
- MA20 / MA60 / MA200: 57.05 / 59.06 / 56.81
- gap20 / gap60: -4.92% / -8.16%
- 5D return: 0.89%
- 20D high/low: 64.00 / 52.70

### Relative Strength

- ratio: 0.895050
- ratio_MA60: 0.916585
- ratio_gap: -2.35%
- ratio_slope_proxy(20d): -0.017489

### Volume (if available)

- volume: 1035116.00
- volume_MA20: 11010950.80
- volume_ratio: 0.09

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 15.79
- MA20 / MA60 / MA200: 18.25 / 21.18 / 19.00
- gap20 / gap60: -13.51% / -25.46%
- 5D return: -5.65%
- 20D high/low: 22.05 / 15.67

### Relative Strength

- ratio: 0.537819
- ratio_MA60: 0.579055
- ratio_gap: -7.12%
- ratio_slope_proxy(20d): 0.022388

### Volume (if available)

- volume: 4643150.00
- volume_MA20: 22468957.50
- volume_ratio: 0.21

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

- close: 4.92
- MA20 / MA60 / MA200: 5.36 / 5.58 / 5.89
- gap20 / gap60: -8.13% / -11.81%
- 5D return: -2.09%
- 20D high/low: 6.94 / 4.64

### Relative Strength

- ratio: 0.014614
- ratio_MA60: 0.014463
- ratio_gap: 1.04%
- ratio_slope_proxy(20d): 0.000301

### Volume (if available)

- volume: 3687058.00
- volume_MA20: 39356687.90
- volume_ratio: 0.09

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.72
- MA20 / MA60 / MA200: 12.49 / 13.28 / 12.93
- gap20 / gap60: -6.20% / -11.74%
- 5D return: -2.66%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.039414
- ratio_MA60: 0.046561
- ratio_gap: -15.35%
- ratio_slope_proxy(20d): -0.003133

### Volume (if available)

- volume: 1252801.00
- volume_MA20: 13938445.05
- volume_ratio: 0.09

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-25 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.63
- IG OAS 4주 변화: 7.0 bp / latest 0.97
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.79
- VIX: 26.36
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 2.94% / slope_proxy: 0.000577
- GDXJ/GLD gap: -12.01% / slope_proxy: -0.010054

## VZLA (Vizsla Silver)
- close: 2.61 | RSI14: 36.461998 | ATR14%: 8.27%
- MA20 gap: -13.90% | MA50 gap: -22.14% | MA200 gap: -25.70%
- vol_ratio(Volume/Vol20): 0.155432 | gap_open: 3.72%
- RS vs SILJ gap: 6.77% / slope_proxy: 0.003406
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
- close: 6.525 | RSI14: 42.807968 | ATR14%: 9.09%
- MA20 gap: -7.31% | MA50 gap: -17.67% | MA200 gap: -21.17%
- vol_ratio(Volume/Vol20): 0.095883 | gap_open: 6.42%
- SilverMarginGate: SI=38.924999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.40% / slope_proxy: 0.006483
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
- close: 12.21 | RSI14: 32.594948 | ATR14%: 12.27%
- MA20 gap: -24.14% | MA50 gap: -30.57% | MA200 gap: -56.00%
- vol_ratio(Volume/Vol20): 0.141314 | gap_open: 4.97%
- RS vs SILJ gap: -5.40% / slope_proxy: -0.041754
- RS vs GDXJ gap: -9.68% / slope_proxy: -0.01435
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

- 실행시간(UTC): **2026-11-25 15:01:23**
- 데이터 기준일(주가): **2026-11-25**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **False**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.63 / 4주 변화 0.33 bp-ish / 2026-11-23
- IG OAS: 0.97 / 4주 변화 0.07 bp-ish / 2026-11-23
- 10Y Real Yield: 2.79 / 4주 변화 0.13 bp-ish / 2026-11-23
- VIX: 26.36 / 4주 변화 8.84 / 2026-11-24
- NFCI: -0.44 / 4주 변화 0.07 / 2026-11-20

### Leadership ratios

- GDX/GLD: gap -5.84% / slope_proxy -1.75%
- GDXJ/GLD: gap -12.01% / slope_proxy -6.87%
- SILJ/SLV: gap 2.97% / slope_proxy 3.30%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.34 | RSI14: 31.41 | ATR14%: 6.92%
- MA20/50/200 gap: -12.83% / -24.64% / -21.63%
- 5D return: -5.93% | 20D drawdown: -24.52% | vol_ratio: 0.16
- RS vs GDXJ: gap -1.36% / slope_proxy 1.04%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **44.9**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 3.13 | RSI14: 21.23 | ATR14%: 12.23%
- MA20/50/200 gap: -32.14% / -47.31% / -52.64%
- 5D return: -15.63% | 20D drawdown: -46.86% | vol_ratio: 0.17
- RS vs GDXJ: gap -31.57% / slope_proxy -30.47%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **42.1**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.52 | RSI14: 22.86 | ATR14%: 11.70%
- MA20/50/200 gap: -27.16% / -43.59% / -59.97%
- 5D return: -9.48% | 20D drawdown: -41.67% | vol_ratio: 0.21
- RS vs GDXJ: gap -29.42% / slope_proxy -23.03%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **36.8**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.17 | RSI14: 29.09 | ATR14%: 11.66%
- MA20/50/200 gap: -21.87% / -39.09% / -39.41%
- 5D return: -12.69% | 20D drawdown: -35.00% | vol_ratio: 0.16
- RS vs GDXJ: gap -21.43% / slope_proxy -11.64%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **30.0**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.53 | RSI14: 43.09 | ATR14%: 9.23%
- MA20/50/200 gap: -7.31% / -17.67% / -21.17%
- 5D return: -4.04% | 20D drawdown: -19.34% | vol_ratio: 0.10
- RS vs SILJ: gap 12.37% / slope_proxy 17.27%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **52.3**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 2.61 | RSI14: 34.81 | ATR14%: 8.41%
- MA20/50/200 gap: -14.06% / -22.28% / -25.85%
- 5D return: -12.58% | 20D drawdown: -25.57% | vol_ratio: 0.16
- RS vs SILJ: gap 6.54% / slope_proxy 3.03%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **51.4**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.23 | RSI14: 27.74 | ATR14%: 8.29%
- MA20/50/200 gap: -18.46% / -27.03% / -14.18%
- 5D return: -10.13% | 20D drawdown: -31.92% | vol_ratio: 0.11
- RS vs SILJ: gap 0.79% / slope_proxy -3.01%
- FundamentalScore: 86 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **49.0**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.49 | RSI14: 27.10 | ATR14%: 8.72%
- MA20/50/200 gap: -22.89% / -31.64% / -40.83%
- 5D return: -16.23% | 20D drawdown: -34.11% | vol_ratio: 0.18
- RS vs SILJ: gap -7.69% / slope_proxy -7.86%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **47.1**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 10.50 | RSI14: 24.65 | ATR14%: 7.39%
- MA20/50/200 gap: -19.17% / -30.43% / -39.95%
- 5D return: -10.03% | 20D drawdown: -31.86% | vol_ratio: 0.09
- RS vs SILJ: gap -5.99% / slope_proxy -5.45%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **45.4**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 1.77 | RSI14: 21.69 | ATR14%: 12.23%
- MA20/50/200 gap: -31.19% / -49.72% / -66.01%
- 5D return: -18.20% | 20D drawdown: -46.05% | vol_ratio: 0.19
- RS vs SILJ: gap -32.37% / slope_proxy -24.77%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **40.9**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.29 | RSI14: 24.51 | ATR14%: 8.30%
- MA20/50/200 gap: -21.57% / -33.59% / -48.74%
- 5D return: -14.77% | 20D drawdown: -32.99% | vol_ratio: 0.14
- RS vs SILJ: gap -11.07% / slope_proxy -7.14%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **37.2**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 12.21 | RSI14: 34.06 | ATR14%: 13.77%
- MA20/50/200 gap: -24.15% / -30.57% / -56.00%
- 5D return: -19.93% | 20D drawdown: -42.60% | vol_ratio: 0.14
- RS vs SILJ: gap -5.42% / slope_proxy -8.01%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **29.2**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
