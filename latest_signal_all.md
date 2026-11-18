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

- 실행시간(UTC): **2026-11-18 15:01:28**
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

- QQQ close: 656.95
- Weekly RSI14: **41.38**
- 52W MA: 667.77 / gap: **-1.62%**
- 104W MA gap: **9.31%**
- 52W MA 13W slope: **4.42%**
- VXN: **34.44** / 5D change: 5.87

## Daily trigger: 실제 매수 타이밍

- QQQ close: 660.84
- Daily RSI14: **38.30**
- 20D gap: **-3.72%**
- 50D gap: **-7.48%**
- 200D gap: **-3.08%**
- MACD hist: -1.4068 / change: 0.0615
- ATR14%: **2.43%**
- 20D high drawdown: **-8.93%**

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
- 실행시간(UTC): **2026-11-18 15:00:54**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.34 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.9 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.92 / 4주 변화 12.0 bp
- VIX (VIXCLS): 25.46
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.175932
- MA60: 8.042899
- gap: -10.78%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.318946
- MA60: 0.400737
- gap: -20.41%
- MA60_slope_proxy: -0.008965
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-18**
- 실행시간(UTC): **2026-11-18 15:00:58**

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
- close: 594.0
- MA50: 647.44 / gap50: -8.25%
- MA200: 630.7358 / gap200: -5.82%

## Relative Strength
- RS vs FTSE gap: -8.49% / slope_proxy: -0.002744
- RS vs Peers gap: -0.92% / slope_proxy: 0.004706

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-18 15:01:05**

## Commodity Regime

- WTI ref (CL=F): 83.04 / 5D -4.03%
- Brent ref (BZ=F): 89.03 / 5D -4.02%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.99
- Gas ref (NG=F): 3.24 / 5D 0.78%

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

- close: 54.67
- MA20 / MA60 / MA200: 59.51 / 59.55 / 56.61
- gap20 / gap60: -8.13% / -8.20%
- 5D return: -4.49%
- 20D high/low: 64.17 / 54.67

### Relative Strength

- ratio: 0.876380
- ratio_MA60: 0.921359
- ratio_gap: -4.88%
- ratio_slope_proxy(20d): -0.015138

### Volume (if available)

- volume: 1456199.00
- volume_MA20: 10389279.95
- volume_ratio: 0.14

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.08
- MA20 / MA60 / MA200: 20.22 / 21.43 / 18.97
- gap20 / gap60: -15.53% / -20.29%
- 5D return: -4.15%
- 20D high/low: 26.16 / 17.08

### Relative Strength

- ratio: 0.553109
- ratio_MA60: 0.577258
- ratio_gap: -4.18%
- ratio_slope_proxy(20d): 0.031365

### Volume (if available)

- volume: 2878912.00
- volume_MA20: 26926170.60
- volume_ratio: 0.11

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

- close: 5.20
- MA20 / MA60 / MA200: 5.79 / 5.67 / 5.90
- gap20 / gap60: -10.13% / -8.30%
- 5D return: -2.07%
- 20D high/low: 6.94 / 5.04

### Relative Strength

- ratio: 0.014557
- ratio_MA60: 0.014437
- ratio_gap: 0.83%
- ratio_slope_proxy(20d): 0.000493

### Volume (if available)

- volume: 5620609.00
- volume_MA20: 40201280.45
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

- close: 12.33
- MA20 / MA60 / MA200: 12.97 / 13.50 / 12.87
- gap20 / gap60: -4.92% / -8.67%
- 5D return: -2.61%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041231
- ratio_MA60: 0.047442
- ratio_gap: -13.09%
- ratio_slope_proxy(20d): -0.002609

### Volume (if available)

- volume: 1130417.00
- volume_MA20: 15210475.85
- volume_ratio: 0.07

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
- 실행시간(UTC): **2026-11-18 15:01:12**

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
- VIX: 25.46
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 1.90% / slope_proxy: 0.003411
- GDXJ/GLD gap: -10.47% / slope_proxy: -0.004231

## VZLA (Vizsla Silver)
- close: 2.98 | RSI14: 40.006438 | ATR14%: 6.43%
- MA20 gap: -5.71% | MA50 gap: -14.13% | MA200 gap: -16.21%
- vol_ratio(Volume/Vol20): 0.251175 | gap_open: 2.69%
- RS vs SILJ gap: 6.51% / slope_proxy: 0.002541
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
- close: 7.11 | RSI14: 45.662822 | ATR14%: 8.16%
- MA20 gap: -1.40% | MA50 gap: -13.05% | MA200 gap: -15.36%
- vol_ratio(Volume/Vol20): 0.399714 | gap_open: 4.86%
- SilverMarginGate: SI=45.150002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.36% / slope_proxy: 0.00562
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
- close: 15.69 | RSI14: 42.020793 | ATR14%: 9.44%
- MA20 gap: -7.36% | MA50 gap: -14.63% | MA200 gap: -44.64%
- vol_ratio(Volume/Vol20): 0.283727 | gap_open: 5.86%
- RS vs SILJ gap: 4.33% / slope_proxy: -0.04674
- RS vs GDXJ gap: 1.58% / slope_proxy: -0.015682
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

- 실행시간(UTC): **2026-11-18 15:01:27**
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

- HY OAS: 3.34 / 4주 변화 0.05 bp-ish / 2026-11-16
- IG OAS: 0.90 / 4주 변화 0.03 bp-ish / 2026-11-16
- 10Y Real Yield: 2.92 / 4주 변화 0.18 bp-ish / 2026-11-16
- VIX: 25.46 / 4주 변화 8.15 / 2026-11-17
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -6.04% / slope_proxy -1.36%
- GDXJ/GLD: gap -10.46% / slope_proxy -3.79%
- SILJ/SLV: gap 1.90% / slope_proxy 7.97%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.89 | RSI14: 36.75 | ATR14%: 6.58%
- MA20/50/200 gap: -10.53% / -21.56% / -15.09%
- 5D return: -12.12% | 20D drawdown: -17.98% | vol_ratio: 0.26
- RS vs GDXJ: gap -5.07% / slope_proxy -4.53%
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
- close: 3.79 | RSI14: 26.55 | ATR14%: 11.12%
- MA20/50/200 gap: -27.21% / -40.80% / -43.63%
- 5D return: -30.07% | 20D drawdown: -35.65% | vol_ratio: 0.37
- RS vs GDXJ: gap -28.42% / slope_proxy -25.72%
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
- close: 0.59 | RSI14: 25.00 | ATR14%: 12.23%
- MA20/50/200 gap: -25.83% / -42.16% / -56.10%
- 5D return: -25.32% | 20D drawdown: -34.44% | vol_ratio: 0.35
- RS vs GDXJ: gap -32.62% / slope_proxy -21.95%
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
- close: 1.34 | RSI14: 35.51 | ATR14%: 9.54%
- MA20/50/200 gap: -17.82% / -34.81% / -31.15%
- 5D return: -19.28% | 20D drawdown: -25.56% | vol_ratio: 0.44
- RS vs GDXJ: gap -21.99% / slope_proxy -16.35%
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
- close: 7.12 | RSI14: 48.97 | ATR14%: 8.60%
- MA20/50/200 gap: -1.27% / -12.93% / -15.24%
- 5D return: -3.26% | 20D drawdown: -11.99% | vol_ratio: 0.40
- RS vs SILJ: gap 7.53% / slope_proxy 11.61%
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
- close: 2.98 | RSI14: 40.00 | ATR14%: 6.93%
- MA20/50/200 gap: -5.71% / -14.13% / -16.21%
- 5D return: -8.02% | 20D drawdown: -14.86% | vol_ratio: 0.25
- RS vs SILJ: gap 6.54% / slope_proxy 4.41%
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
- close: 20.37 | RSI14: 36.87 | ATR14%: 8.38%
- MA20/50/200 gap: -14.54% / -21.26% / -3.90%
- 5D return: -16.82% | 20D drawdown: -23.91% | vol_ratio: 0.50
- RS vs SILJ: gap -1.58% / slope_proxy -4.58%
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
- close: 6.76 | RSI14: 38.16 | ATR14%: 7.81%
- MA20/50/200 gap: -11.09% / -20.06% / -28.38%
- 5D return: -16.81% | 20D drawdown: -19.00% | vol_ratio: 0.41
- RS vs SILJ: gap -2.49% / slope_proxy -1.31%
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
- close: 12.00 | RSI14: 35.47 | ATR14%: 7.63%
- MA20/50/200 gap: -13.46% / -24.62% / -32.53%
- 5D return: -15.01% | 20D drawdown: -22.13% | vol_ratio: 0.11
- RS vs SILJ: gap -7.76% / slope_proxy -4.95%
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
- close: 2.17 | RSI14: 30.84 | ATR14%: 12.00%
- MA20/50/200 gap: -24.46% / -43.09% / -59.43%
- 5D return: -26.52% | 20D drawdown: -33.89% | vol_ratio: 0.26
- RS vs SILJ: gap -30.95% / slope_proxy -23.79%
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
- close: 15.73 | RSI14: 44.34 | ATR14%: 10.78%
- MA20/50/200 gap: -7.16% / -14.45% / -44.52%
- 5D return: -15.91% | 20D drawdown: -26.07% | vol_ratio: 0.28
- RS vs SILJ: gap 4.58% / slope_proxy 11.52%
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
- close: 3.90 | RSI14: 35.93 | ATR14%: 7.72%
- MA20/50/200 gap: -13.27% / -25.52% / -40.69%
- 5D return: -14.92% | 20D drawdown: -20.47% | vol_ratio: 0.29
- RS vs SILJ: gap -10.34% / slope_proxy -8.50%
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
