# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-19 22:57:38**
- 데이터 기준일(일봉): **2026-08-19**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-18** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 716.08
- Weekly RSI14: **58.22**
- 52W MA: 640.20 / gap: **11.85%**
- 104W MA gap: **24.88%**
- 52W MA 13W slope: **6.92%**
- VXN: **22.56** / 5D change: 0.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 716.08
- Daily RSI14: **51.47**
- 20D gap: **1.32%**
- 50D gap: **0.45%**
- 200D gap: **10.01%**
- MACD hist: 1.6625 / change: -1.0502
- ATR14%: **1.68%**
- 20D high drawdown: **-2.18%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
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

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 22:56:55**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.41 / 4주 변화 4.0 bp
- VIX (VIXCLS): 15.84
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.228273
- MA60: 9.272494
- gap: -11.26%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.423002
- MA60: 0.397771
- gap: 6.34%
- MA60_slope_proxy: 0.016417
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 22:57:00**

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
- TERM_SPREAD_10Y_POLICY: 129.27 bp / 4주 변화 2.32 bp
- CURVE_10s5s: 48.77 bp / 4주 변화 1.39 bp

## NWG Price
- close: 682.0
- MA50: 672.6628 / gap50: 1.39%
- MA200: 622.8266 / gap200: 9.50%

## Relative Strength
- RS vs FTSE gap: 2.60% / slope_proxy: 0.003003
- RS vs Peers gap: 2.13% / slope_proxy: 0.015007

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-19 22:57:07**

## Commodity Regime

- WTI ref (CL=F): 84.31 / 5D 1.25%
- Brent ref (BZ=F): 91.39 / 5D 2.71%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.08
- Gas ref (NG=F): 2.78 / 5D -0.93%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.09
- MA20 / MA60 / MA200: 57.02 / 55.10 / 50.98
- gap20 / gap60: 5.39% / 9.05%
- 5D return: 2.63%
- 20D high/low: 60.09 / 53.81

### Relative Strength

- ratio: 0.945108
- ratio_MA60: 0.962950
- ratio_gap: -1.85%
- ratio_slope_proxy(20d): -0.013443

### Volume (if available)

- volume: 6942893.00
- volume_MA20: 8400969.65
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.54
- MA20 / MA60 / MA200: 18.42 / 17.84 / 16.54
- gap20 / gap60: 0.67% / 3.93%
- 5D return: 4.39%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.541156
- ratio_MA60: 0.510793
- ratio_gap: 5.94%
- ratio_slope_proxy(20d): -0.006767

### Volume (if available)

- volume: 16371142.00
- volume_MA20: 15191182.10
- volume_ratio: 1.08

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.84
- MA20 / MA60 / MA200: 5.42 / 5.50 / 5.45
- gap20 / gap60: 7.69% / 6.19%
- 5D return: 2.46%
- 20D high/low: 5.87 / 4.95

### Relative Strength

- ratio: 0.013948
- ratio_MA60: 0.013951
- ratio_gap: -0.02%
- ratio_slope_proxy(20d): -0.000511

### Volume (if available)

- volume: 40039359.00
- volume_MA20: 46780587.95
- volume_ratio: 0.86

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

- close: 13.79
- MA20 / MA60 / MA200: 13.49 / 12.67 / 10.98
- gap20 / gap60: 2.23% / 8.85%
- 5D return: 0.51%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.050273
- ratio_MA60: 0.050669
- ratio_gap: -0.78%
- ratio_slope_proxy(20d): -0.000210

### Volume (if available)

- volume: 11267028.00
- volume_MA20: 14604091.40
- volume_ratio: 0.77

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 22:57:20**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.75
- IG OAS 4주 변화: 4.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.41
- VIX: 15.84
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 11.08% / slope_proxy: 0.01883
- GDXJ/GLD gap: 12.74% / slope_proxy: -0.000338

## VZLA (Vizsla Silver)
- close: 3.89 | RSI14: 62.57292 | ATR14%: 4.92%
- MA20 gap: 10.84% | MA50 gap: 15.20% | MA200 gap: -4.56%
- vol_ratio(Volume/Vol20): 1.003722 | gap_open: 4.48%
- RS vs SILJ gap: -3.02% / slope_proxy: 0.004672
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
- close: 9.54 | RSI14: 71.071735 | ATR14%: 5.67%
- MA20 gap: 23.65% | MA50 gap: 35.48% | MA200 gap: 11.34%
- vol_ratio(Volume/Vol20): 1.852241 | gap_open: 4.78%
- SilverMarginGate: SI=67.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.64% / slope_proxy: -0.000206
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
- close: 27.9 | RSI14: 61.296272 | ATR14%: 7.00%
- MA20 gap: 18.19% | MA50 gap: 20.58% | MA200 gap: -3.54%
- vol_ratio(Volume/Vol20): 1.836372 | gap_open: 8.06%
- RS vs SILJ gap: -1.71% / slope_proxy: -0.121913
- RS vs GDXJ gap: -5.23% / slope_proxy: -0.032521
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

- 실행시간(UTC): **2026-08-19 22:57:33**
- 데이터 기준일(주가): **2026-08-19**

## Verdict
**⏸ No confirmed entry; watchlist only**

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

- HY OAS: 2.75 / 4주 변화 0.06 bp-ish / 2026-08-18
- IG OAS: 0.82 / 4주 변화 0.04 bp-ish / 2026-08-18
- 10Y Real Yield: 2.41 / 4주 변화 0.04 bp-ish / 2026-08-18
- VIX: 15.84 / 4주 변화 -1.21 / 2026-08-18
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 13.10% / slope_proxy 16.47%
- GDXJ/GLD: gap 12.74% / slope_proxy 16.40%
- SILJ/SLV: gap 11.08% / slope_proxy 9.82%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.40 | RSI14: 82.77 | ATR14%: 5.79%
- MA20/50/200 gap: 21.89% / 30.96% / 46.99%
- 5D return: 4.10% | 20D drawdown: 0.00% | vol_ratio: 1.83
- RS vs GDXJ: gap 8.34% / slope_proxy 8.70%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **82.3**
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.49 | RSI14: 88.00 | ATR14%: 4.63%
- MA20/50/200 gap: 21.65% / 31.11% / 8.78%
- 5D return: 8.08% | 20D drawdown: 0.00% | vol_ratio: 1.03
- RS vs GDXJ: gap 7.47% / slope_proxy 10.24%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.64 | RSI14: 87.14 | ATR14%: 5.40%
- MA20/50/200 gap: 24.43% / 30.43% / 10.54%
- 5D return: 13.10% | 20D drawdown: 0.00% | vol_ratio: 1.97
- RS vs GDXJ: gap 7.97% / slope_proxy 12.72%
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
- close: 2.46 | RSI14: 72.14 | ATR14%: 6.16%
- MA20/50/200 gap: 21.63% / 34.84% / 33.28%
- 5D return: 13.36% | 20D drawdown: 0.00% | vol_ratio: 1.98
- RS vs GDXJ: gap 10.37% / slope_proxy 1.26%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **67.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.25 | RSI14: 74.95 | ATR14%: 6.37%
- MA20/50/200 gap: 14.37% / 30.46% / 58.69%
- 5D return: -2.82% | 20D drawdown: -2.82% | vol_ratio: 1.49
- RS vs SILJ: gap 13.97% / slope_proxy 7.06%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.99 | RSI14: 74.47 | ATR14%: 5.87%
- MA20/50/200 gap: 21.53% / 28.95% / 13.98%
- 5D return: 3.58% | 20D drawdown: 0.00% | vol_ratio: 1.16
- RS vs SILJ: gap 9.28% / slope_proxy 9.75%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.54 | RSI14: 75.34 | ATR14%: 5.22%
- MA20/50/200 gap: 24.75% / 29.74% / 10.61%
- 5D return: 13.48% | 20D drawdown: 0.00% | vol_ratio: 1.64
- RS vs SILJ: gap 10.14% / slope_proxy 5.91%
- FundamentalScore: 78 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **72.8**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.54 | RSI14: 77.38 | ATR14%: 6.11%
- MA20/50/200 gap: 23.65% / 35.26% / 11.23%
- 5D return: 7.55% | 20D drawdown: 0.00% | vol_ratio: 1.86
- RS vs SILJ: gap 14.89% / slope_proxy 19.62%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.57 | RSI14: 73.61 | ATR14%: 5.75%
- MA20/50/200 gap: 19.04% / 21.88% / 12.12%
- 5D return: 6.02% | 20D drawdown: 0.00% | vol_ratio: 1.18
- RS vs SILJ: gap 3.04% / slope_proxy 5.09%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **64.8**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.89 | RSI14: 74.84 | ATR14%: 4.85%
- MA20/50/200 gap: 10.61% / 15.03% / -4.77%
- 5D return: 2.37% | 20D drawdown: 0.00% | vol_ratio: 0.99
- RS vs SILJ: gap -2.64% / slope_proxy -5.70%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **52.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.39 | RSI14: 75.62 | ATR14%: 5.86%
- MA20/50/200 gap: 17.66% / 16.43% / -6.58%
- 5D return: 3.85% | 20D drawdown: 0.00% | vol_ratio: 1.28
- RS vs SILJ: gap -3.75% / slope_proxy 4.87%
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
- close: 27.90 | RSI14: 71.81 | ATR14%: 7.19%
- MA20/50/200 gap: 18.19% / 20.58% / -3.54%
- 5D return: 1.64% | 20D drawdown: 0.00% | vol_ratio: 1.84
- RS vs SILJ: gap -1.71% / slope_proxy 7.61%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
