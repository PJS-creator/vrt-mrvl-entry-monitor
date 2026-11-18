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

- 실행시간(UTC): **2026-11-18 22:35:55**
- 데이터 기준일(일봉): **2026-11-18**
- 데이터 기준일(주봉): **2026-11-16**
- VXN 기준일: **2026-11-17** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 659.51
- Weekly RSI14: **41.84**
- 52W MA: 667.82 / gap: **-1.24%**
- 104W MA gap: **9.73%**
- 52W MA 13W slope: **4.43%**
- VXN: **34.44** / 5D change: 5.87

## Daily trigger: 실제 매수 타이밍

- QQQ close: 659.51
- Daily RSI14: **37.71**
- 20D gap: **-3.90%**
- 50D gap: **-7.66%**
- 200D gap: **-3.27%**
- MACD hist: -1.4917 / change: -0.0234
- ATR14%: **2.44%**
- 20D high drawdown: **-9.11%**

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

- 데이터 기준일(주가): **2026-11-18**
- 실행시간(UTC): **2026-11-18 22:35:32**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.43 / 4주 변화 10.0 bp
- IG OAS (BAMLC0A0CM): 0.92 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.89 / 4주 변화 12.0 bp
- VIX (VIXCLS): 25.46
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.139186
- MA60: 8.042287
- gap: -11.23%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.316708
- MA60: 0.4007
- gap: -20.96%
- MA60_slope_proxy: -0.009003
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-18**
- 실행시간(UTC): **2026-11-18 22:35:35**

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
- TERM_SPREAD_10Y_POLICY: 131.51 bp / 4주 변화 -30.89 bp
- CURVE_10s5s: 34.17 bp / 4주 변화 -6.45 bp

## NWG Price
- close: 588.8
- MA50: 647.336 / gap50: -9.04%
- MA200: 630.7098 / gap200: -6.64%

## Relative Strength
- RS vs FTSE gap: -8.69% / slope_proxy: -0.002746
- RS vs Peers gap: -0.77% / slope_proxy: 0.004732

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-18 22:35:40**

## Commodity Regime

- WTI ref (CL=F): 81.89 / 5D -5.36%
- Brent ref (BZ=F): 88.68 / 5D -4.40%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.79
- Gas ref (NG=F): 3.38 / 5D 5.04%

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

- close: 53.76
- MA20 / MA60 / MA200: 59.46 / 59.54 / 56.61
- gap20 / gap60: -9.59% / -9.71%
- 5D return: -6.08%
- 20D high/low: 64.17 / 53.76

### Relative Strength

- ratio: 0.877141
- ratio_MA60: 0.921372
- ratio_gap: -4.80%
- ratio_slope_proxy(20d): -0.015126

### Volume (if available)

- volume: 13047537.00
- volume_MA20: 10968846.85
- volume_ratio: 1.19

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.73
- MA20 / MA60 / MA200: 20.20 / 21.42 / 18.96
- gap20 / gap60: -17.19% / -21.90%
- 5D return: -6.12%
- 20D high/low: 26.16 / 16.73

### Relative Strength

- ratio: 0.556368
- ratio_MA60: 0.577313
- ratio_gap: -3.63%
- ratio_slope_proxy(20d): 0.031420

### Volume (if available)

- volume: 24591089.00
- volume_MA20: 28011779.45
- volume_ratio: 0.88

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

- close: 5.03
- MA20 / MA60 / MA200: 5.78 / 5.67 / 5.90
- gap20 / gap60: -12.94% / -11.25%
- 5D return: -5.27%
- 20D high/low: 6.94 / 5.03

### Relative Strength

- ratio: 0.014329
- ratio_MA60: 0.014433
- ratio_gap: -0.72%
- ratio_slope_proxy(20d): 0.000490

### Volume (if available)

- volume: 42319184.00
- volume_MA20: 42036209.20
- volume_ratio: 1.01

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

- close: 12.04
- MA20 / MA60 / MA200: 12.95 / 13.50 / 12.87
- gap20 / gap60: -7.06% / -10.79%
- 5D return: -4.90%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.040608
- ratio_MA60: 0.047432
- ratio_gap: -14.39%
- ratio_slope_proxy(20d): -0.002620

### Volume (if available)

- volume: 9500566.00
- volume_MA20: 15629493.30
- volume_ratio: 0.61

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

- 데이터 기준일(주가): **2026-11-18**
- 실행시간(UTC): **2026-11-18 22:35:44**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 10.0 bp / latest 3.43
- IG OAS 4주 변화: 5.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.89
- VIX: 25.46
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 0.93% / slope_proxy: 0.003328
- GDXJ/GLD gap: -10.42% / slope_proxy: -0.004229

## VZLA (Vizsla Silver)
- close: 2.98 | RSI14: 40.006438 | ATR14%: 6.45%
- MA20 gap: -5.71% | MA50 gap: -14.13% | MA200 gap: -16.21%
- vol_ratio(Volume/Vol20): 2.20364 | gap_open: 2.69%
- RS vs SILJ gap: 8.04% / slope_proxy: 0.002575
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
- close: 6.8 | RSI14: 43.134274 | ATR14%: 8.58%
- MA20 gap: -5.50% | MA50 gap: -16.78% | MA200 gap: -19.03%
- vol_ratio(Volume/Vol20): 1.933086 | gap_open: 4.86%
- SilverMarginGate: SI=44.974998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.23% / slope_proxy: 0.005454
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
- close: 15.25 | RSI14: 40.490826 | ATR14%: 9.74%
- MA20 gap: -9.84% | MA50 gap: -16.99% | MA200 gap: -46.19%
- vol_ratio(Volume/Vol20): 1.322956 | gap_open: 5.86%
- RS vs SILJ gap: 2.91% / slope_proxy: -0.046911
- RS vs GDXJ gap: -0.14% / slope_proxy: -0.015732
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

- 실행시간(UTC): **2026-11-18 22:35:53**
- 데이터 기준일(주가): **2026-11-18**

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

- HY OAS: 3.43 / 4주 변화 0.10 bp-ish / 2026-11-17
- IG OAS: 0.92 / 4주 변화 0.05 bp-ish / 2026-11-17
- 10Y Real Yield: 2.89 / 4주 변화 0.09 bp-ish / 2026-11-17
- VIX: 25.46 / 4주 변화 8.15 / 2026-11-17
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -5.65% / slope_proxy -0.94%
- GDXJ/GLD: gap -10.42% / slope_proxy -3.74%
- SILJ/SLV: gap 0.93% / slope_proxy 6.93%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.74 | RSI14: 35.25 | ATR14%: 6.73%
- MA20/50/200 gap: -12.39% / -23.24% / -16.93%
- 5D return: -14.03% | 20D drawdown: -19.76% | vol_ratio: 2.01
- RS vs GDXJ: gap -6.09% / slope_proxy -5.58%
- FundamentalScore: 88 | TechnicalScore: 30 | RegimeScore: 0 | OverallScore: **50.1**
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
- close: 3.71 | RSI14: 26.01 | ATR14%: 11.51%
- MA20/50/200 gap: -28.69% / -42.03% / -44.81%
- 5D return: -31.55% | 20D drawdown: -37.01% | vol_ratio: 2.65
- RS vs GDXJ: gap -29.14% / slope_proxy -26.48%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 0 | OverallScore: **47.4**
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
- close: 0.58 | RSI14: 24.53 | ATR14%: 12.44%
- MA20/50/200 gap: -27.04% / -43.13% / -56.85%
- 5D return: -26.58% | 20D drawdown: -35.56% | vol_ratio: 1.24
- RS vs GDXJ: gap -33.02% / slope_proxy -22.42%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 0 | OverallScore: **42.0**
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
- close: 1.34 | RSI14: 35.51 | ATR14%: 9.65%
- MA20/50/200 gap: -17.82% / -34.81% / -31.15%
- 5D return: -19.28% | 20D drawdown: -25.56% | vol_ratio: 1.25
- RS vs GDXJ: gap -21.13% / slope_proxy -15.42%
- FundamentalScore: 55 | TechnicalScore: 30 | RegimeScore: 0 | OverallScore: **35.2**
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
- close: 6.80 | RSI14: 46.43 | ATR14%: 9.06%
- MA20/50/200 gap: -5.50% / -16.78% / -19.03%
- 5D return: -7.61% | 20D drawdown: -15.95% | vol_ratio: 1.93
- RS vs SILJ: gap 4.23% / slope_proxy 8.13%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 25 | OverallScore: **57.6**
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
- close: 2.98 | RSI14: 40.00 | ATR14%: 6.95%
- MA20/50/200 gap: -5.71% / -14.13% / -16.21%
- 5D return: -8.02% | 20D drawdown: -14.86% | vol_ratio: 2.20
- RS vs SILJ: gap 8.04% / slope_proxy 5.91%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 25 | OverallScore: **56.6**
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
- close: 20.28 | RSI14: 36.66 | ATR14%: 8.41%
- MA20/50/200 gap: -14.90% / -21.61% / -4.33%
- 5D return: -17.19% | 20D drawdown: -24.24% | vol_ratio: 1.60
- RS vs SILJ: gap -0.62% / slope_proxy -3.64%
- FundamentalScore: 86 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **54.2**
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
- close: 6.56 | RSI14: 36.49 | ATR14%: 8.23%
- MA20/50/200 gap: -13.54% / -22.34% / -30.44%
- 5D return: -19.21% | 20D drawdown: -21.34% | vol_ratio: 1.68
- RS vs SILJ: gap -3.92% / slope_proxy -2.78%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **52.4**
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
- close: 11.67 | RSI14: 34.13 | ATR14%: 8.05%
- MA20/50/200 gap: -15.74% / -26.66% / -34.38%
- 5D return: -17.35% | 20D drawdown: -24.27% | vol_ratio: 1.18
- RS vs SILJ: gap -8.99% / slope_proxy -6.23%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **50.6**
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
- close: 2.17 | RSI14: 30.77 | ATR14%: 12.03%
- MA20/50/200 gap: -24.63% / -43.21% / -59.52%
- 5D return: -26.69% | 20D drawdown: -34.04% | vol_ratio: 1.48
- RS vs SILJ: gap -30.13% / slope_proxy -22.88%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **46.1**
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.25 | RSI14: 42.82 | ATR14%: 11.14%
- MA20/50/200 gap: -9.84% / -16.99% / -46.19%
- 5D return: -18.45% | 20D drawdown: -28.30% | vol_ratio: 1.32
- RS vs SILJ: gap 2.91% / slope_proxy 9.71%
- FundamentalScore: 42 | TechnicalScore: 55 | RegimeScore: 25 | OverallScore: **43.2**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.86 | RSI14: 35.29 | ATR14%: 7.86%
- MA20/50/200 gap: -14.22% / -26.37% / -41.37%
- 5D return: -15.90% | 20D drawdown: -21.38% | vol_ratio: 1.49
- RS vs SILJ: gap -10.10% / slope_proxy -8.25%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **42.5**
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

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
