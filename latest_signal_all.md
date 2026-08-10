# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-10 15:01:54**
- 데이터 기준일(일봉): **2026-08-10**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-07** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 722.28
- Weekly RSI14: **60.74**
- 52W MA: 637.21 / gap: **13.35%**
- 104W MA gap: **26.49%**
- 52W MA 13W slope: **7.14%**
- VXN: **22.82** / 5D change: -3.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 722.28
- Daily RSI14: **56.84**
- 20D gap: **3.05%**
- 50D gap: **1.15%**
- 200D gap: **11.59%**
- MACD hist: 4.6241 / change: 0.2030
- ATR14%: **1.96%**
- 20D high drawdown: **-0.22%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 15:01:04**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.43 / 4주 변화 12.0 bp
- VIX (VIXCLS): 14.9
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.564162
- MA60: 9.397279
- gap: -8.87%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.37318
- MA60: 0.390896
- gap: -4.53%
- MA60_slope_proxy: 0.013178
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 15:01:08**

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
- TERM_SPREAD_10Y_POLICY: 116.29 bp / 4주 변화 2.09 bp
- CURVE_10s5s: 48.25 bp / 4주 변화 -0.2 bp

## NWG Price
- close: 711.2
- MA50: 657.596 / gap50: 8.15%
- MA200: 618.7222 / gap200: 14.95%

## Relative Strength
- RS vs FTSE gap: 7.14% / slope_proxy: 0.002646
- RS vs Peers gap: 4.75% / slope_proxy: 0.006436

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-10 15:01:18**

## Commodity Regime

- WTI ref (CL=F): 80.76 / 5D 0.52%
- Brent ref (BZ=F): 86.14 / 5D 2.83%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.38
- Gas ref (NG=F): 2.80 / 5D 0.83%

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

- close: 57.74
- MA20 / MA60 / MA200: 55.65 / 55.07 / 50.35
- gap20 / gap60: 3.76% / 4.85%
- 5D return: 4.09%
- 20D high/low: 57.74 / 53.65

### Relative Strength

- ratio: 0.974104
- ratio_MA60: 0.967935
- ratio_gap: 0.64%
- ratio_slope_proxy(20d): -0.014044

### Volume (if available)

- volume: 2426136.00
- volume_MA20: 8313196.80
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.20
- MA20 / MA60 / MA200: 18.43 / 18.05 / 16.31
- gap20 / gap60: -1.25% / 0.81%
- 5D return: -4.51%
- 20D high/low: 19.40 / 17.47

### Relative Strength

- ratio: 0.516679
- ratio_MA60: 0.512313
- ratio_gap: 0.85%
- ratio_slope_proxy(20d): -0.006049

### Volume (if available)

- volume: 2980510.00
- volume_MA20: 14065355.50
- volume_ratio: 0.21

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.62
- MA20 / MA60 / MA200: 5.21 / 5.66 / 5.38
- gap20 / gap60: 7.81% / -0.71%
- 5D return: 9.03%
- 20D high/low: 5.62 / 4.95

### Relative Strength

- ratio: 0.013880
- ratio_MA60: 0.014102
- ratio_gap: -1.57%
- ratio_slope_proxy(20d): -0.000451

### Volume (if available)

- volume: 10650611.00
- volume_MA20: 39890425.55
- volume_ratio: 0.27

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 14.01
- MA20 / MA60 / MA200: 13.46 / 12.69 / 10.82
- gap20 / gap60: 4.12% / 10.44%
- 5D return: 7.11%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.053367
- ratio_MA60: 0.051299
- ratio_gap: 4.03%
- ratio_slope_proxy(20d): 0.001092

### Volume (if available)

- volume: 3185553.00
- volume_MA20: 14555707.65
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 15:01:30**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.43
- VIX: 14.9
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 9.09% / slope_proxy: 0.012103
- GDXJ/GLD gap: 9.30% / slope_proxy: -0.006555

## VZLA (Vizsla Silver)
- close: 3.8699 | RSI14: 66.595666 | ATR14%: 5.09%
- MA20 gap: 16.67% | MA50 gap: 14.39% | MA200 gap: -5.34%
- vol_ratio(Volume/Vol20): 0.370671 | gap_open: 0.27%
- RS vs SILJ gap: 3.64% / slope_proxy: 0.006105
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
- close: 8.75 | RSI14: 72.691361 | ATR14%: 5.77%
- MA20 gap: 28.66% | MA50 gap: 27.67% | MA200 gap: 3.35%
- vol_ratio(Volume/Vol20): 0.618351 | gap_open: 1.19%
- SilverMarginGate: SI=64.894997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.75% / slope_proxy: -0.004335
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
- close: 26.75 | RSI14: 64.247215 | ATR14%: 6.89%
- MA20 gap: 25.59% | MA50 gap: 12.94% | MA200 gap: -5.30%
- vol_ratio(Volume/Vol20): 0.401348 | gap_open: 0.94%
- RS vs SILJ gap: -3.06% / slope_proxy: -0.144557
- RS vs GDXJ gap: -5.49% / slope_proxy: -0.036218
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

- 실행시간(UTC): **2026-08-10 15:01:52**
- 데이터 기준일(주가): **2026-08-10**

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

- HY OAS: 2.71 / 4주 변화 0.01 bp-ish / 2026-08-06
- IG OAS: 0.78 / 4주 변화 0.02 bp-ish / 2026-08-06
- 10Y Real Yield: 2.43 / 4주 변화 0.12 bp-ish / 2026-08-06
- VIX: 14.90 / 4주 변화 -0.13 / 2026-08-07
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 8.49% / slope_proxy 11.03%
- GDXJ/GLD: gap 9.32% / slope_proxy 11.20%
- SILJ/SLV: gap 9.13% / slope_proxy 5.64%
- Gold breadth proxy: above50 100.00%, above200 61.54%, count 13
- Silver breadth proxy: above50 100.00%, above200 53.85%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.42 | RSI14: 79.60 | ATR14%: 5.11%
- MA20/50/200 gap: 25.12% / 23.12% / 35.71%
- 5D return: 30.47% | 20D drawdown: -1.26% | vol_ratio: 0.65
- RS vs GDXJ: gap 8.09% / slope_proxy 7.35%
- FundamentalScore: 88 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **72.1**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.76 | RSI14: 86.06 | ATR14%: 5.35%
- MA20/50/200 gap: 23.21% / 20.90% / -1.15%
- 5D return: 25.42% | 20D drawdown: 0.00% | vol_ratio: 1.45
- RS vs GDXJ: gap 5.48% / slope_proxy 10.79%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **65.9**
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
- close: 1.44 | RSI14: 80.95 | ATR14%: 5.36%
- MA20/50/200 gap: 22.87% / 17.88% / -2.41%
- 5D return: 27.43% | 20D drawdown: -0.69% | vol_ratio: 1.66
- RS vs GDXJ: gap 3.43% / slope_proxy 6.63%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.13 | RSI14: 66.67 | ATR14%: 5.70%
- MA20/50/200 gap: 11.75% / 19.78% / 16.87%
- 5D return: 13.30% | 20D drawdown: 0.00% | vol_ratio: 0.39
- RS vs GDXJ: gap 3.55% / slope_proxy -13.25%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **53.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.38 | RSI14: 77.18 | ATR14%: 5.75%
- MA20/50/200 gap: 29.47% / 37.27% / 64.09%
- 5D return: 34.61% | 20D drawdown: 0.00% | vol_ratio: 0.41
- RS vs SILJ: gap 26.44% / slope_proxy 17.45%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.06 | RSI14: 71.05 | ATR14%: 5.34%
- MA20/50/200 gap: 23.68% / 20.63% / 5.26%
- 5D return: 30.16% | 20D drawdown: 0.00% | vol_ratio: 0.45
- RS vs SILJ: gap 7.61% / slope_proxy 7.04%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **69.4**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.75 | RSI14: 76.90 | ATR14%: 5.84%
- MA20/50/200 gap: 28.66% / 27.67% / 3.35%
- 5D return: 30.01% | 20D drawdown: 0.00% | vol_ratio: 0.62
- RS vs SILJ: gap 12.75% / slope_proxy 15.72%
- FundamentalScore: 74 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **65.8**
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
- close: 7.18 | RSI14: 64.71 | ATR14%: 5.76%
- MA20/50/200 gap: 21.82% / 16.54% / 7.56%
- 5D return: 29.75% | 20D drawdown: 0.00% | vol_ratio: 0.80
- RS vs SILJ: gap 4.42% / slope_proxy 3.14%
- FundamentalScore: 60 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **59.5**
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
- close: 3.87 | RSI14: 67.47 | ATR14%: 5.08%
- MA20/50/200 gap: 16.67% / 14.39% / -5.34%
- 5D return: 18.71% | 20D drawdown: 0.00% | vol_ratio: 0.37
- RS vs SILJ: gap 3.64% / slope_proxy 3.96%
- FundamentalScore: 72 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **56.1**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.20 | RSI14: 61.83 | ATR14%: 5.26%
- MA20/50/200 gap: 12.88% / 10.50% / -6.36%
- 5D return: 19.20% | 20D drawdown: 0.00% | vol_ratio: 0.15
- RS vs SILJ: gap -1.17% / slope_proxy -4.61%
- FundamentalScore: 78 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **50.1**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.09 | RSI14: 67.71 | ATR14%: 6.12%
- MA20/50/200 gap: 22.35% / 8.07% / -11.10%
- 5D return: 24.57% | 20D drawdown: 0.00% | vol_ratio: 0.37
- RS vs SILJ: gap -4.90% / slope_proxy 4.29%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 26.75 | RSI14: 71.58 | ATR14%: 6.47%
- MA20/50/200 gap: 25.59% / 12.94% / -5.30%
- 5D return: 29.73% | 20D drawdown: 0.00% | vol_ratio: 0.40
- RS vs SILJ: gap -3.06% / slope_proxy 5.20%
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
