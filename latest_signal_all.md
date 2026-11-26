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

- 실행시간(UTC): **2026-11-26 03:01:17**
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

- QQQ close: 633.93
- Weekly RSI14: **40.09**
- 52W MA: 667.18 / gap: **-4.98%**
- 104W MA gap: **5.34%**
- 52W MA 13W slope: **3.87%**
- VXN: **36.42** / 5D change: 1.98

## Daily trigger: 실제 매수 타이밍

- QQQ close: 633.93
- Daily RSI14: **38.59**
- 20D gap: **-4.92%**
- 50D gap: **-10.34%**
- 200D gap: **-7.12%**
- MACD hist: -2.5078 / change: 0.3138
- ATR14%: **3.40%**
- 20D high drawdown: **-11.38%**

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
- 실행시간(UTC): **2026-11-26 03:00:52**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.72 / 4주 변화 54.0 bp
- IG OAS (BAMLC0A0CM): 0.98 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.79 / 4주 변화 15.0 bp
- VIX (VIXCLS): 26.36
- NFCI: -0.444

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.62223
- MA60: 7.892922
- gap: -16.10%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.309923
- MA60: 0.392835
- gap: -21.11%
- MA60_slope_proxy: -0.02397
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-26 03:00:54**

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
- close: 582.6
- MA50: 639.072 / gap50: -8.84%
- MA200: 629.7399 / gap200: -7.49%

## Relative Strength
- RS vs FTSE gap: -8.22% / slope_proxy: -0.002913
- RS vs Peers gap: 1.60% / slope_proxy: 0.001907

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-26 03:01:03**

## Commodity Regime

- WTI ref (CL=F): 83.81 / 5D 0.66%
- Brent ref (BZ=F): 90.52 / 5D -1.56%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.71
- Gas ref (NG=F): 3.68 / 5D 9.07%

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

- close: 53.95
- MA20 / MA60 / MA200: 57.03 / 59.06 / 56.81
- gap20 / gap60: -5.41% / -8.65%
- 5D return: 0.35%
- 20D high/low: 64.00 / 52.70

### Relative Strength

- ratio: 0.885878
- ratio_MA60: 0.916432
- ratio_gap: -3.33%
- ratio_slope_proxy(20d): -0.017642

### Volume (if available)

- volume: 8484900.00
- volume_MA20: 11383440.00
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.05
- MA20 / MA60 / MA200: 18.26 / 21.18 / 19.00
- gap20 / gap60: -12.12% / -24.22%
- 5D return: -4.06%
- 20D high/low: 22.05 / 15.67

### Relative Strength

- ratio: 0.532162
- ratio_MA60: 0.578961
- ratio_gap: -8.08%
- ratio_slope_proxy(20d): 0.022294

### Volume (if available)

- volume: 29053900.00
- volume_MA20: 23689495.00
- volume_ratio: 1.23

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
- MA20 / MA60 / MA200: 5.37 / 5.59 / 5.89
- gap20 / gap60: -6.26% / -9.95%
- 5D return: 0.00%
- 20D high/low: 6.94 / 4.64

### Relative Strength

- ratio: 0.014503
- ratio_MA60: 0.014461
- ratio_gap: 0.29%
- ratio_slope_proxy(20d): 0.000299

### Volume (if available)

- volume: 89406000.00
- volume_MA20: 43642635.00
- volume_ratio: 2.05

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

- close: 11.74
- MA20 / MA60 / MA200: 12.50 / 13.28 / 12.93
- gap20 / gap60: -6.05% / -11.59%
- 5D return: -2.49%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.038875
- ratio_MA60: 0.046552
- ratio_gap: -16.49%
- ratio_slope_proxy(20d): -0.003142

### Volume (if available)

- volume: 8343700.00
- volume_MA20: 14292990.00
- volume_ratio: 0.58

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

- 데이터 기준일(주가): **2026-11-25**
- 실행시간(UTC): **2026-11-26 03:01:07**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.72
- IG OAS 4주 변화: 10.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.79
- VIX: 26.36
- NFCI: -0.444

### Leadership ratios
- SILJ/SLV gap: 5.90% / slope_proxy: 0.000831
- GDXJ/GLD gap: -7.72% / slope_proxy: -0.009844

## VZLA (Vizsla Silver)
- close: 2.86 | RSI14: 43.838092 | ATR14%: 8.10%
- MA20 gap: -6.04% | MA50 gap: -14.80% | MA200 gap: -18.62%
- vol_ratio(Volume/Vol20): 1.202741 | gap_open: 3.72%
- RS vs SILJ gap: 7.76% / slope_proxy: 0.003428
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
- close: 7.51 | RSI14: 51.968668 | ATR14%: 8.57%
- MA20 gap: 5.94% | MA50 gap: -5.48% | MA200 gap: -9.32%
- vol_ratio(Volume/Vol20): 1.220345 | gap_open: 6.42%
- SilverMarginGate: SI=42.119999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 19.03% / slope_proxy: 0.00684
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
- close: 13.72 | RSI14: 39.230528 | ATR14%: 11.49%
- MA20 gap: -15.16% | MA50 gap: -22.11% | MA200 gap: -50.57%
- vol_ratio(Volume/Vol20): 1.367501 | gap_open: 4.97%
- RS vs SILJ gap: -2.13% / slope_proxy: -0.041365
- RS vs GDXJ gap: -6.28% / slope_proxy: -0.014254
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

- 실행시간(UTC): **2026-11-26 03:01:16**
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

- HY OAS: 3.72 / 4주 변화 0.54 bp-ish / 2026-11-24
- IG OAS: 0.98 / 4주 변화 0.10 bp-ish / 2026-11-24
- 10Y Real Yield: 2.79 / 4주 변화 0.13 bp-ish / 2026-11-24
- VIX: 26.36 / 4주 변화 8.84 / 2026-11-24
- NFCI: -0.44 / 4주 변화 0.07 / 2026-11-20

### Leadership ratios

- GDX/GLD: gap -2.06% / slope_proxy 2.26%
- GDXJ/GLD: gap -7.72% / slope_proxy -2.25%
- SILJ/SLV: gap 5.90% / slope_proxy 6.30%
- Gold breadth proxy: above50 7.69%, above200 7.69%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.59 | RSI14: 33.51 | ATR14%: 6.72%
- MA20/50/200 gap: -9.55% / -21.72% / -18.55%
- 5D return: -2.23% | 20D drawdown: -21.55% | vol_ratio: 1.39
- RS vs GDXJ: gap -5.20% / slope_proxy -2.96%
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
- close: 3.48 | RSI14: 26.37 | ATR14%: 11.56%
- MA20/50/200 gap: -24.84% / -41.49% / -47.36%
- 5D return: -6.20% | 20D drawdown: -40.92% | vol_ratio: 1.04
- RS vs GDXJ: gap -29.72% / slope_proxy -28.57%
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
- close: 0.59 | RSI14: 29.63 | ATR14%: 11.26%
- MA20/50/200 gap: -18.51% / -36.70% / -55.02%
- 5D return: 1.72% | 20D drawdown: -34.44% | vol_ratio: 1.24
- RS vs GDXJ: gap -26.74% / slope_proxy -20.07%
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
- close: 1.33 | RSI14: 37.07 | ATR14%: 10.90%
- MA20/50/200 gap: -11.66% / -30.87% / -31.16%
- 5D return: -0.75% | 20D drawdown: -26.11% | vol_ratio: 1.28
- RS vs GDXJ: gap -17.53% / slope_proxy -7.18%
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
- close: 7.51 | RSI14: 51.61 | ATR14%: 8.69%
- MA20/50/200 gap: 5.94% / -5.48% / -9.32%
- 5D return: 10.44% | 20D drawdown: -7.17% | vol_ratio: 1.22
- RS vs SILJ: gap 19.03% / slope_proxy 24.36%
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
- close: 2.86 | RSI14: 41.79 | ATR14%: 8.21%
- MA20/50/200 gap: -6.04% / -14.80% / -18.62%
- 5D return: -4.03% | 20D drawdown: -18.29% | vol_ratio: 1.20
- RS vs SILJ: gap 7.76% / slope_proxy 4.22%
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
- close: 19.86 | RSI14: 34.06 | ATR14%: 8.05%
- MA20/50/200 gap: -11.46% / -20.58% / -6.51%
- 5D return: -2.07% | 20D drawdown: -25.81% | vol_ratio: 1.32
- RS vs SILJ: gap 1.20% / slope_proxy -2.62%
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
- close: 6.14 | RSI14: 34.41 | ATR14%: 8.29%
- MA20/50/200 gap: -14.23% / -23.74% / -33.90%
- 5D return: -6.40% | 20D drawdown: -26.38% | vol_ratio: 1.02
- RS vs SILJ: gap -5.01% / slope_proxy -5.14%
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
- close: 11.28 | RSI14: 29.60 | ATR14%: 7.19%
- MA20/50/200 gap: -13.42% / -25.34% / -35.50%
- 5D return: -3.34% | 20D drawdown: -26.80% | vol_ratio: 1.14
- RS vs SILJ: gap -6.93% / slope_proxy -6.41%
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
- close: 1.91 | RSI14: 23.47 | ATR14%: 11.52%
- MA20/50/200 gap: -26.16% / -45.94% / -63.43%
- 5D return: -11.98% | 20D drawdown: -41.95% | vol_ratio: 2.18
- RS vs SILJ: gap -32.94% / slope_proxy -25.41%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.69 | RSI14: 32.68 | ATR14%: 7.90%
- MA20/50/200 gap: -12.46% / -25.63% / -42.53%
- 5D return: -4.40% | 20D drawdown: -24.85% | vol_ratio: 1.53
- RS vs SILJ: gap -8.15% / slope_proxy -4.04%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 13.72 | RSI14: 39.20 | ATR14%: 12.82%
- MA20/50/200 gap: -15.16% / -22.11% / -50.57%
- 5D return: -10.03% | 20D drawdown: -35.50% | vol_ratio: 1.37
- RS vs SILJ: gap -2.13% / slope_proxy -4.75%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 25 | OverallScore: **34.4**
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
