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

- 실행시간(UTC): **2026-08-06 15:01:39**
- 데이터 기준일(일봉): **2026-08-06**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-08-05** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 718.43
- Weekly RSI14: **60.18**
- 52W MA: 634.28 / gap: **13.27%**
- 104W MA gap: **26.36%**
- 52W MA 13W slope: **7.31%**
- VXN: **24.15** / 5D change: -6.69

## Daily trigger: 실제 매수 타이밍

- QQQ close: 718.50
- Daily RSI14: **55.82**
- 20D gap: **2.55%**
- 50D gap: **0.56%**
- 200D gap: **11.20%**
- MACD hist: 3.9582 / change: 0.7557
- ATR14%: **2.14%**
- 20D high drawdown: **-0.97%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-06 15:00:53**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.4 / 4주 변화 10.0 bp
- VIX (VIXCLS): 15.81
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.815097
- MA60: 9.493085
- gap: -7.14%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.374575
- MA60: 0.388586
- gap: -3.61%
- MA60_slope_proxy: 0.013607
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-06 15:00:57**

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
- TERM_SPREAD_10Y_POLICY: 115.31 bp / 4주 변화 9.39 bp
- CURVE_10s5s: 48.14 bp / 4주 변화 -0.7 bp

## NWG Price
- close: 719.4
- MA50: 653.08 / gap50: 10.15%
- MA200: 617.092 / gap200: 16.58%

## Relative Strength
- RS vs FTSE gap: 8.61% / slope_proxy: 0.002447
- RS vs Peers gap: 5.63% / slope_proxy: 0.002532

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-06 15:01:11**

## Commodity Regime

- WTI ref (CL=F): 76.71 / 5D -8.23%
- Brent ref (BZ=F): 81.35 / 5D -8.63%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.64
- Gas ref (NG=F): 2.62 / 5D -4.97%

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

- close: 56.40
- MA20 / MA60 / MA200: 55.37 / 55.05 / 50.19
- gap20 / gap60: 1.86% / 2.45%
- 5D return: 0.80%
- 20D high/low: 57.60 / 52.89

### Relative Strength

- ratio: 0.976030
- ratio_MA60: 0.968324
- ratio_gap: 0.80%
- ratio_slope_proxy(20d): -0.014821

### Volume (if available)

- volume: 7068001.00
- volume_MA20: 8322380.05
- volume_ratio: 0.85

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.58
- MA20 / MA60 / MA200: 18.39 / 18.12 / 16.24
- gap20 / gap60: 1.03% / 2.54%
- 5D return: -2.85%
- 20D high/low: 19.40 / 17.32

### Relative Strength

- ratio: 0.513263
- ratio_MA60: 0.513011
- ratio_gap: 0.05%
- ratio_slope_proxy(20d): -0.005478

### Volume (if available)

- volume: 3782101.00
- volume_MA20: 13745160.05
- volume_ratio: 0.28

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.28
- MA20 / MA60 / MA200: 5.20 / 5.70 / 5.36
- gap20 / gap60: 1.47% / -7.38%
- 5D return: 3.84%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013335
- ratio_MA60: 0.014149
- ratio_gap: -5.76%
- ratio_slope_proxy(20d): -0.000451

### Volume (if available)

- volume: 12943209.00
- volume_MA20: 40962160.45
- volume_ratio: 0.32

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

- close: 12.77
- MA20 / MA60 / MA200: 13.33 / 12.66 / 10.77
- gap20 / gap60: -4.21% / 0.91%
- 5D return: -3.55%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.048714
- ratio_MA60: 0.051315
- ratio_gap: -5.07%
- ratio_slope_proxy(20d): 0.001147

### Volume (if available)

- volume: 3641674.00
- volume_MA20: 15072808.70
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-06 15:01:22**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.4
- VIX: 15.81
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 8.43% / slope_proxy: 0.010603
- GDXJ/GLD gap: 4.34% / slope_proxy: -0.007546

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 60.629215 | ATR14%: 5.24%
- MA20 gap: 10.56% | MA50 gap: 6.21% | MA200 gap: -12.32%
- vol_ratio(Volume/Vol20): 0.183826 | gap_open: 1.39%
- RS vs SILJ gap: 2.66% / slope_proxy: 0.006082
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
- close: 7.98 | RSI14: 66.543058 | ATR14%: 6.04%
- MA20 gap: 21.15% | MA50 gap: 16.86% | MA200 gap: -5.47%
- vol_ratio(Volume/Vol20): 0.297265 | gap_open: 3.39%
- SilverMarginGate: SI=61.799999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.29% / slope_proxy: -0.004964
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
- close: 24.370001 | RSI14: 58.699297 | ATR14%: 7.22%
- MA20 gap: 17.43% | MA50 gap: 1.82% | MA200 gap: -13.16%
- vol_ratio(Volume/Vol20): 0.256067 | gap_open: 3.92%
- RS vs SILJ gap: -7.42% / slope_proxy: -0.145956
- RS vs GDXJ gap: -9.78% / slope_proxy: -0.03554
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

- 실행시간(UTC): **2026-08-06 15:01:37**
- 데이터 기준일(주가): **2026-08-06**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.75 / 4주 변화 0.05 bp-ish / 2026-08-05
- IG OAS: 0.78 / 4주 변화 0.02 bp-ish / 2026-08-05
- 10Y Real Yield: 2.40 / 4주 변화 0.10 bp-ish / 2026-08-04
- VIX: 15.81 / 4주 변화 -1.09 / 2026-08-05
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 4.41% / slope_proxy 7.30%
- GDXJ/GLD: gap 4.32% / slope_proxy 7.01%
- SILJ/SLV: gap 8.47% / slope_proxy 5.72%
- Gold breadth proxy: above50 92.31%, above200 30.77%, count 13
- Silver breadth proxy: above50 84.62%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.20 | RSI14: 72.34 | ATR14%: 4.80%
- MA20/50/200 gap: 12.59% / 7.76% / 19.05%
- 5D return: 15.01% | 20D drawdown: 0.00% | vol_ratio: 1.69
- RS vs GDXJ: gap 1.78% / slope_proxy -4.45%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **68.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.94 | RSI14: 56.67 | ATR14%: 6.08%
- MA20/50/200 gap: 2.78% / 9.69% / 6.94%
- 5D return: 8.99% | 20D drawdown: -5.83% | vol_ratio: 0.22
- RS vs GDXJ: gap 1.11% / slope_proxy -3.50%
- FundamentalScore: 55 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **60.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.26 | RSI14: 83.57 | ATR14%: 5.36%
- MA20/50/200 gap: 17.32% / 12.25% / -8.38%
- 5D return: 17.01% | 20D drawdown: 0.00% | vol_ratio: 0.23
- RS vs GDXJ: gap 4.16% / slope_proxy 6.54%
- FundamentalScore: 82 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **60.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.36 | RSI14: 78.18 | ATR14%: 5.41%
- MA20/50/200 gap: 18.88% / 11.73% / -7.79%
- 5D return: 20.35% | 20D drawdown: 0.00% | vol_ratio: 1.47
- RS vs GDXJ: gap 4.28% / slope_proxy 3.77%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **60.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 25.09 | RSI14: 73.00 | ATR14%: 5.86%
- MA20/50/200 gap: 23.08% / 27.90% / 51.78%
- 5D return: 22.45% | 20D drawdown: 0.00% | vol_ratio: 0.32
- RS vs SILJ: gap 24.95% / slope_proxy 13.21%
- FundamentalScore: 86 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **71.2**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.59 | RSI14: 67.57 | ATR14%: 5.09%
- MA20/50/200 gap: 10.56% / 6.21% / -12.32%
- 5D return: 10.80% | 20D drawdown: 0.00% | vol_ratio: 0.18
- RS vs SILJ: gap 2.66% / slope_proxy 5.11%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **61.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.98 | RSI14: 70.32 | ATR14%: 5.58%
- MA20/50/200 gap: 12.89% / 7.82% / -5.90%
- 5D return: 15.64% | 20D drawdown: 0.00% | vol_ratio: 0.25
- RS vs SILJ: gap 2.17% / slope_proxy 1.90%
- FundamentalScore: 82 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **60.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.98 | RSI14: 76.02 | ATR14%: 5.92%
- MA20/50/200 gap: 21.15% / 16.86% / -5.47%
- 5D return: 17.70% | 20D drawdown: 0.00% | vol_ratio: 0.30
- RS vs SILJ: gap 9.29% / slope_proxy 12.33%
- FundamentalScore: 74 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **57.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.31 | RSI14: 63.48 | ATR14%: 5.43%
- MA20/50/200 gap: 7.90% / 4.63% / -11.08%
- 5D return: 9.21% | 20D drawdown: -1.42% | vol_ratio: 0.17
- RS vs SILJ: gap -0.59% / slope_proxy -5.55%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **55.4**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.75 | RSI14: 68.56 | ATR14%: 6.32%
- MA20/50/200 gap: 16.40% / -0.07% / -17.04%
- 5D return: 20.53% | 20D drawdown: -1.27% | vol_ratio: 0.48
- RS vs SILJ: gap -6.49% / slope_proxy 1.21%
- FundamentalScore: 68 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **45.6**
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.49 | RSI14: 64.23 | ATR14%: 5.98%
- MA20/50/200 gap: 12.33% / 5.53% / -2.44%
- 5D return: 17.45% | 20D drawdown: 0.00% | vol_ratio: 0.32
- RS vs SILJ: gap 0.60% / slope_proxy -1.62%
- FundamentalScore: 60 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **42.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 24.37 | RSI14: 70.94 | ATR14%: 6.51%
- MA20/50/200 gap: 17.43% / 1.82% / -13.17%
- 5D return: 21.43% | 20D drawdown: -0.45% | vol_ratio: 0.26
- RS vs SILJ: gap -7.42% / slope_proxy 4.46%
- FundamentalScore: 42 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **33.9**
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
