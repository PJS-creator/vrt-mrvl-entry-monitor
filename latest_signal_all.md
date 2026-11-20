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

- 실행시간(UTC): **2026-11-20 15:01:23**
- 데이터 기준일(일봉): **2026-11-20**
- 데이터 기준일(주봉): **2026-11-16**
- VXN 기준일: **2026-11-19** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 640.49
- Weekly RSI14: **38.64**
- 52W MA: 667.46 / gap: **-4.04%**
- 104W MA gap: **6.60%**
- 52W MA 13W slope: **4.37%**
- VXN: **36.48** / 5D change: 7.93

## Daily trigger: 실제 매수 타이밍

- QQQ close: 640.49
- Daily RSI14: **32.81**
- 20D gap: **-5.83%**
- 50D gap: **-9.98%**
- 200D gap: **-6.12%**
- MACD hist: -2.7302 / change: -0.5038
- ATR14%: **2.62%**
- 20D high drawdown: **-11.73%**

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

- 데이터 기준일(주가): **2026-11-20**
- 실행시간(UTC): **2026-11-20 15:01:01**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.52 / 4주 변화 12.0 bp
- IG OAS (BAMLC0A0CM): 0.94 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.88 / 4주 변화 12.0 bp
- VIX (VIXCLS): 28.44
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.728989
- MA60: 7.98566
- gap: -15.74%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.305431
- MA60: 0.396578
- gap: -22.98%
- MA60_slope_proxy: -0.016398
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-20**
- 실행시간(UTC): **2026-11-20 15:01:03**

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
- TERM_SPREAD_10Y_POLICY: 126.8 bp / 4주 변화 -31.57 bp
- CURVE_10s5s: 34.36 bp / 4주 변화 -3.96 bp

## NWG Price
- close: 582.4
- MA50: 643.184 / gap50: -9.45%
- MA200: 630.0295 / gap200: -7.56%

## Relative Strength
- RS vs FTSE gap: -7.98% / slope_proxy: -0.002878
- RS vs Peers gap: 1.09% / slope_proxy: 0.002778

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-20 15:01:11**

## Commodity Regime

- WTI ref (CL=F): 81.42 / 5D -8.06%
- Brent ref (BZ=F): 88.17 / 5D -8.00%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.75
- Gas ref (NG=F): 3.65 / 5D 12.85%

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

- close: 54.18
- MA20 / MA60 / MA200: 58.53 / 59.39 / 56.69
- gap20 / gap60: -7.43% / -8.77%
- 5D return: -7.78%
- 20D high/low: 64.07 / 53.76

### Relative Strength

- ratio: 0.884427
- ratio_MA60: 0.919317
- ratio_gap: -3.80%
- ratio_slope_proxy(20d): -0.016242

### Volume (if available)

- volume: 870076.00
- volume_MA20: 10493333.80
- volume_ratio: 0.08

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.21
- MA20 / MA60 / MA200: 19.24 / 21.36 / 18.98
- gap20 / gap60: -15.72% / -24.09%
- 5D return: -11.59%
- 20D high/low: 22.50 / 16.21

### Relative Strength

- ratio: 0.549289
- ratio_MA60: 0.578875
- ratio_gap: -5.11%
- ratio_slope_proxy(20d): 0.029503

### Volume (if available)

- volume: 1946287.00
- volume_MA20: 27300364.35
- volume_ratio: 0.07

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

- close: 4.80
- MA20 / MA60 / MA200: 5.63 / 5.64 / 5.90
- gap20 / gap60: -14.75% / -14.85%
- 5D return: -13.34%
- 20D high/low: 6.94 / 4.77

### Relative Strength

- ratio: 0.014016
- ratio_MA60: 0.014436
- ratio_gap: -2.91%
- ratio_slope_proxy(20d): 0.000404

### Volume (if available)

- volume: 5667377.00
- volume_MA20: 39403153.85
- volume_ratio: 0.14

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

- close: 12.07
- MA20 / MA60 / MA200: 12.82 / 13.42 / 12.90
- gap20 / gap60: -5.88% / -10.06%
- 5D return: -8.14%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.040611
- ratio_MA60: 0.047096
- ratio_gap: -13.77%
- ratio_slope_proxy(20d): -0.002786

### Volume (if available)

- volume: 1156796.00
- volume_MA20: 14168454.80
- volume_ratio: 0.08

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

- 데이터 기준일(주가): **2026-11-20**
- 실행시간(UTC): **2026-11-20 15:01:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 12.0 bp / latest 3.52
- IG OAS 4주 변화: 5.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.88
- VIX: 28.44
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 0.87% / slope_proxy: 0.002075
- GDXJ/GLD gap: -10.87% / slope_proxy: -0.006629

## VZLA (Vizsla Silver)
- close: 2.815 | RSI14: 35.399979 | ATR14%: 7.02%
- MA20 gap: -10.01% | MA50 gap: -17.78% | MA200 gap: -20.45%
- vol_ratio(Volume/Vol20): 0.428436 | gap_open: 5.67%
- RS vs SILJ gap: 8.06% / slope_proxy: 0.003076
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
- close: 6.54 | RSI14: 41.039167 | ATR14%: 8.38%
- MA20 gap: -8.52% | MA50 gap: -18.73% | MA200 gap: -21.68%
- vol_ratio(Volume/Vol20): 0.276357 | gap_open: 2.12%
- SilverMarginGate: SI=42.095001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.24% / slope_proxy: 0.005543
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
- close: 14.3594 | RSI14: 38.809347 | ATR14%: 10.35%
- MA20 gap: -14.33% | MA50 gap: -20.59% | MA200 gap: -48.93%
- vol_ratio(Volume/Vol20): 0.256907 | gap_open: 2.25%
- RS vs SILJ gap: 3.41% / slope_proxy: -0.044565
- RS vs GDXJ gap: -0.51% / slope_proxy: -0.01511
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

- 실행시간(UTC): **2026-11-20 15:01:22**
- 데이터 기준일(주가): **2026-11-20**

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

- HY OAS: 3.52 / 4주 변화 0.12 bp-ish / 2026-11-19
- IG OAS: 0.94 / 4주 변화 0.05 bp-ish / 2026-11-19
- 10Y Real Yield: 2.88 / 4주 변화 0.11 bp-ish / 2026-11-18
- VIX: 28.44 / 4주 변화 9.41 / 2026-11-19
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -5.79% / slope_proxy -0.99%
- GDXJ/GLD: gap -10.87% / slope_proxy -3.97%
- SILJ/SLV: gap 0.83% / slope_proxy 6.68%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.31 | RSI14: 34.72 | ATR14%: 7.17%
- MA20/50/200 gap: -16.11% / -26.92% / -22.15%
- 5D return: -14.73% | 20D drawdown: -24.88% | vol_ratio: 0.33
- RS vs GDXJ: gap -7.17% / slope_proxy -6.98%
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
- close: 3.47 | RSI14: 26.58 | ATR14%: 11.47%
- MA20/50/200 gap: -30.48% / -44.16% / -48.02%
- 5D return: -24.07% | 20D drawdown: -41.09% | vol_ratio: 0.24
- RS vs GDXJ: gap -29.54% / slope_proxy -27.27%
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
- close: 0.57 | RSI14: 27.66 | ATR14%: 11.15%
- MA20/50/200 gap: -25.78% / -41.97% / -57.16%
- 5D return: -25.00% | 20D drawdown: -36.67% | vol_ratio: 0.24
- RS vs GDXJ: gap -29.46% / slope_proxy -19.82%
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
- close: 1.23 | RSI14: 33.64 | ATR14%: 10.92%
- MA20/50/200 gap: -21.93% / -38.45% / -36.60%
- 5D return: -20.13% | 20D drawdown: -31.67% | vol_ratio: 0.22
- RS vs GDXJ: gap -23.07% / slope_proxy -12.97%
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
- close: 6.54 | RSI14: 46.45 | ATR14%: 8.88%
- MA20/50/200 gap: -8.52% / -18.73% / -21.68%
- 5D return: -4.25% | 20D drawdown: -19.16% | vol_ratio: 0.28
- RS vs SILJ: gap 6.24% / slope_proxy 10.47%
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
- close: 2.82 | RSI14: 42.03 | ATR14%: 7.37%
- MA20/50/200 gap: -10.01% / -17.78% / -20.45%
- 5D return: -8.31% | 20D drawdown: -19.57% | vol_ratio: 0.43
- RS vs SILJ: gap 8.06% / slope_proxy 9.04%
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
- close: 18.35 | RSI14: 33.09 | ATR14%: 8.83%
- MA20/50/200 gap: -21.26% / -27.98% / -13.51%
- 5D return: -19.78% | 20D drawdown: -31.43% | vol_ratio: 0.28
- RS vs SILJ: gap -4.58% / slope_proxy -8.40%
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
- close: 6.06 | RSI14: 36.61 | ATR14%: 8.39%
- MA20/50/200 gap: -18.53% / -26.77% / -35.39%
- 5D return: -20.89% | 20D drawdown: -27.34% | vol_ratio: 0.27
- RS vs SILJ: gap -5.30% / slope_proxy -3.79%
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
- close: 11.19 | RSI14: 35.99 | ATR14%: 7.78%
- MA20/50/200 gap: -17.54% / -28.10% / -36.68%
- 5D return: -14.58% | 20D drawdown: -27.39% | vol_ratio: 0.10
- RS vs SILJ: gap -6.79% / slope_proxy -4.81%
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
- close: 2.00 | RSI14: 30.87 | ATR14%: 12.00%
- MA20/50/200 gap: -27.76% / -45.94% / -62.35%
- 5D return: -20.00% | 20D drawdown: -39.21% | vol_ratio: 0.27
- RS vs SILJ: gap -30.42% / slope_proxy -20.98%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 14.43 | RSI14: 43.78 | ATR14%: 11.86%
- MA20/50/200 gap: -13.90% / -20.18% / -48.66%
- 5D return: -9.22% | 20D drawdown: -32.14% | vol_ratio: 0.26
- RS vs SILJ: gap 3.94% / slope_proxy 11.54%
- FundamentalScore: 42 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **37.9**
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
- close: 3.62 | RSI14: 34.61 | ATR14%: 7.92%
- MA20/50/200 gap: -17.71% / -29.33% / -44.58%
- 5D return: -15.73% | 20D drawdown: -26.37% | vol_ratio: 0.27
- RS vs SILJ: gap -9.73% / slope_proxy -6.55%
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

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
