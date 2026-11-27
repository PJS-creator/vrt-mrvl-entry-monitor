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

- 실행시간(UTC): **2026-11-27 22:35:55**
- 데이터 기준일(일봉): **2026-11-27**
- 데이터 기준일(주봉): **2026-11-23**
- VXN 기준일: **2026-11-25** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 650.99
- Weekly RSI14: **43.46**
- 52W MA: 667.51 / gap: **-2.47%**
- 104W MA gap: **8.14%**
- 52W MA 13W slope: **3.92%**
- VXN: **38.53** / 5D change: 5.41

## Daily trigger: 실제 매수 타이밍

- QQQ close: 650.99
- Daily RSI14: **44.02**
- 20D gap: **-1.89%**
- 50D gap: **-7.75%**
- 200D gap: **-4.65%**
- MACD hist: -0.9301 / change: 1.5777
- ATR14%: **3.26%**
- 20D high drawdown: **-5.92%**

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

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 22:35:27**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.77 / 4주 변화 51.0 bp
- IG OAS (BAMLC0A0CM): 0.99 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.73 / 4주 변화 6.0 bp
- VIX (VIXCLS): 26.8
- NFCI: -0.444

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.748867
- MA60: 7.862442
- gap: -14.16%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.319366
- MA60: 0.391908
- gap: -18.51%
- MA60_slope_proxy: -0.025204
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 22:35:30**

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
- TERM_SPREAD_10Y_POLICY: 109.86 bp / 4주 변화 -46.01 bp
- CURVE_10s5s: 34.37 bp / 4주 변화 -0.36 bp

## NWG Price
- close: 600.0
- MA50: 632.092 / gap50: -5.08%
- MA200: 629.643 / gap200: -4.71%

## Relative Strength
- RS vs FTSE gap: -6.86% / slope_proxy: -0.002961
- RS vs Peers gap: 1.92% / slope_proxy: 0.002344

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-27 22:35:38**

## Commodity Regime

- WTI ref (CL=F): 83.08 / 5D -0.16%
- Brent ref (BZ=F): 90.84 / 5D -1.24%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.76
- Gas ref (NG=F): 3.49 / 5D 6.82%

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

- close: 54.17
- MA20 / MA60 / MA200: 56.59 / 58.95 / 56.84
- gap20 / gap60: -4.28% / -8.11%
- 5D return: 0.67%
- 20D high/low: 64.00 / 52.70

### Relative Strength

- ratio: 0.878385
- ratio_MA60: 0.915457
- ratio_gap: -4.05%
- ratio_slope_proxy(20d): -0.018232

### Volume (if available)

- volume: 4154768.00
- volume_MA20: 11239098.40
- volume_ratio: 0.37

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.84
- MA20 / MA60 / MA200: 18.01 / 21.11 / 19.01
- gap20 / gap60: -6.50% / -20.24%
- 5D return: 3.38%
- 20D high/low: 22.05 / 15.67

### Relative Strength

- ratio: 0.508454
- ratio_MA60: 0.578308
- ratio_gap: -12.08%
- ratio_slope_proxy(20d): 0.018860

### Volume (if available)

- volume: 23728725.00
- volume_MA20: 23455536.25
- volume_ratio: 1.01

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

- close: 5.18
- MA20 / MA60 / MA200: 5.29 / 5.57 / 5.88
- gap20 / gap60: -2.09% / -6.98%
- 5D return: 8.60%
- 20D high/low: 6.94 / 4.64

### Relative Strength

- ratio: 0.014540
- ratio_MA60: 0.014466
- ratio_gap: 0.51%
- ratio_slope_proxy(20d): 0.000253

### Volume (if available)

- volume: 68496881.00
- volume_MA20: 44830834.05
- volume_ratio: 1.53

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.07
- MA20 / MA60 / MA200: 12.36 / 13.24 / 12.94
- gap20 / gap60: -2.35% / -8.81%
- 5D return: -0.49%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.039569
- ratio_MA60: 0.046382
- ratio_gap: -14.69%
- ratio_slope_proxy(20d): -0.003270

### Volume (if available)

- volume: 4596241.00
- volume_MA20: 13686982.05
- volume_ratio: 0.34

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-27**
- 실행시간(UTC): **2026-11-27 22:35:44**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 51.0 bp / latest 3.77
- IG OAS 4주 변화: 10.0 bp / latest 0.99
- 10Y Real Yield 4주 변화: 6.0 bp / latest 2.73
- VIX: 26.8
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 8.44% / slope_proxy: 0.0009
- GDXJ/GLD gap: -2.06% / slope_proxy: -0.010298

## VZLA (Vizsla Silver)
- close: 3.1 | RSI14: 50.690581 | ATR14%: 7.51%
- MA20 gap: 2.16% | MA50 gap: -7.15% | MA200 gap: -11.69%
- vol_ratio(Volume/Vol20): 0.452867 | gap_open: 4.55%
- RS vs SILJ gap: 7.20% / slope_proxy: 0.003486
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

## SCZM (Santacruz Silver)
- close: 8.38 | RSI14: 58.811821 | ATR14%: 7.88%
- MA20 gap: 17.27% | MA50 gap: 5.61% | MA200 gap: 1.38%
- vol_ratio(Volume/Vol20): 0.710549 | gap_open: 6.79%
- SilverMarginGate: SI=43.702 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 21.67% / slope_proxy: 0.007652
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
- close: 15.77 | RSI14: 48.756172 | ATR14%: 10.23%
- MA20 gap: -2.03% | MA50 gap: -9.89% | MA200 gap: -42.98%
- vol_ratio(Volume/Vol20): 0.633369 | gap_open: 8.09%
- RS vs SILJ gap: 3.41% / slope_proxy: -0.038812
- RS vs GDXJ gap: -0.26% / slope_proxy: -0.013628
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

- 실행시간(UTC): **2026-11-27 22:35:54**
- 데이터 기준일(주가): **2026-11-27**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **False**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.77 / 4주 변화 0.51 bp-ish / 2026-11-26
- IG OAS: 0.99 / 4주 변화 0.10 bp-ish / 2026-11-26
- 10Y Real Yield: 2.73 / 4주 변화 0.09 bp-ish / 2026-11-25
- VIX: 26.80 / 4주 변화 9.60 / 2026-11-26
- NFCI: -0.44 / 4주 변화 0.07 / 2026-11-20

### Leadership ratios

- GDX/GLD: gap 2.81% / slope_proxy 9.28%
- GDXJ/GLD: gap -2.06% / slope_proxy 6.23%
- SILJ/SLV: gap 8.44% / slope_proxy 9.02%
- Gold breadth proxy: above50 7.69%, above200 15.38%, count 13
- Silver breadth proxy: above50 7.69%, above200 15.38%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.08 | RSI14: 38.00 | ATR14%: 6.34%
- MA20/50/200 gap: -2.33% / -15.21% / -12.48%
- 5D return: 13.10% | 20D drawdown: -15.71% | vol_ratio: 0.64
- RS vs GDXJ: gap -5.79% / slope_proxy -5.32%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **49.9**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 3.95 | RSI14: 25.63 | ATR14%: 9.87%
- MA20/50/200 gap: -11.58% / -31.86% / -39.85%
- 5D return: 20.43% | 20D drawdown: -32.94% | vol_ratio: 0.71
- RS vs GDXJ: gap -25.84% / slope_proxy -24.35%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.64 | RSI14: 24.00 | ATR14%: 10.38%
- MA20/50/200 gap: -9.35% / -29.03% / -50.70%
- 5D return: 12.28% | 20D drawdown: -28.89% | vol_ratio: 0.83
- RS vs GDXJ: gap -25.82% / slope_proxy -17.82%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **41.8**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.24 | RSI14: 24.55 | ATR14%: 11.41%
- MA20/50/200 gap: -15.65% / -33.74% / -35.61%
- 5D return: 8.77% | 20D drawdown: -31.11% | vol_ratio: 0.97
- RS vs GDXJ: gap -28.34% / slope_proxy -18.83%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **35.0**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 22.84 | RSI14: 42.50 | ATR14%: 7.50%
- MA20/50/200 gap: 2.19% / -8.23% / 7.40%
- 5D return: 20.85% | 20D drawdown: -14.68% | vol_ratio: 1.35
- RS vs SILJ: gap 6.69% / slope_proxy 3.02%
- FundamentalScore: 86 | TechnicalScore: 55 | RegimeScore: 25 | OverallScore: **63.0**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.38 | RSI14: 56.40 | ATR14%: 8.23%
- MA20/50/200 gap: 17.27% / 5.61% / 1.38%
- 5D return: 26.78% | 20D drawdown: 0.00% | vol_ratio: 0.71
- RS vs SILJ: gap 21.67% / slope_proxy 28.52%
- FundamentalScore: 74 | TechnicalScore: 50 | RegimeScore: 25 | OverallScore: **55.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.10 | RSI14: 45.33 | ATR14%: 7.70%
- MA20/50/200 gap: 2.16% / -7.15% / -11.69%
- 5D return: 9.93% | 20D drawdown: -11.43% | vol_ratio: 0.45
- RS vs SILJ: gap 7.20% / slope_proxy 5.19%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.87 | RSI14: 40.55 | ATR14%: 7.74%
- MA20/50/200 gap: -3.43% / -13.97% / -25.83%
- 5D return: 12.99% | 20D drawdown: -17.63% | vol_ratio: 0.91
- RS vs SILJ: gap -2.13% / slope_proxy -1.06%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.23 | RSI14: 29.91 | ATR14%: 10.22%
- MA20/50/200 gap: -12.36% / -35.86% / -57.07%
- 5D return: 8.78% | 20D drawdown: -32.22% | vol_ratio: 1.07
- RS vs SILJ: gap -27.45% / slope_proxy -19.32%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 12.12 | RSI14: 34.25 | ATR14%: 6.84%
- MA20/50/200 gap: -6.14% / -19.04% / -30.47%
- 5D return: 8.70% | 20D drawdown: -21.35% | vol_ratio: 0.70
- RS vs SILJ: gap -7.84% / slope_proxy -6.99%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.11 | RSI14: 40.75 | ATR14%: 7.41%
- MA20/50/200 gap: -1.91% / -16.43% / -35.67%
- 5D return: 12.60% | 20D drawdown: -16.29% | vol_ratio: 0.74
- RS vs SILJ: gap -5.59% / slope_proxy -1.67%
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
- close: 15.77 | RSI14: 40.37 | ATR14%: 11.06%
- MA20/50/200 gap: -2.03% / -9.89% / -42.98%
- 5D return: 14.44% | 20D drawdown: -25.86% | vol_ratio: 0.63
- RS vs SILJ: gap 3.41% / slope_proxy -0.28%
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
