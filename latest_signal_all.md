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

- 실행시간(UTC): **2026-11-25 03:01:08**
- 데이터 기준일(일봉): **2026-11-24**
- 데이터 기준일(주봉): **2026-11-23**
- VXN 기준일: **2026-11-23** / source: `FRED: VXNCLS`

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
- VXN: **36.31** / 5D change: 3.41

## Daily trigger: 실제 매수 타이밍

- QQQ close: 638.10
- Daily RSI14: **39.46**
- 20D gap: **-4.95%**
- 50D gap: **-9.93%**
- 200D gap: **-6.49%**
- MACD hist: -2.8216 / change: 0.4419
- ATR14%: **3.27%**
- 20D high drawdown: **-12.06%**

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

- 데이터 기준일(주가): **2026-11-24**
- 실행시간(UTC): **2026-11-25 03:00:41**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.63 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.97 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 2.79 / 4주 변화 13.0 bp
- VIX (VIXCLS): 26.62
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.657985
- MA60: 7.924688
- gap: -15.98%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.308307
- MA60: 0.3941
- gap: -21.77%
- MA60_slope_proxy: -0.021644
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-24**
- 실행시간(UTC): **2026-11-25 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 120.72 bp / 4주 변화 -35.8 bp
- CURVE_10s5s: 33.75 bp / 4주 변화 -3.74 bp

## NWG Price
- close: 591.0
- MA50: 641.204 / gap50: -7.83%
- MA200: 629.8502 / gap200: -6.17%

## Relative Strength
- RS vs FTSE gap: -7.21% / slope_proxy: -0.002906
- RS vs Peers gap: 0.44% / slope_proxy: 0.002409

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-25 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 80.78 / 5D -6.08%
- Brent ref (BZ=F): 87.56 / 5D -5.99%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.78
- Gas ref (NG=F): 3.66 / 5D 14.12%

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

- close: 53.38
- MA20 / MA60 / MA200: 57.48 / 59.17 / 56.76
- gap20 / gap60: -7.13% / -9.78%
- 5D return: -5.56%
- 20D high/low: 64.00 / 52.70

### Relative Strength

- ratio: 0.883044
- ratio_MA60: 0.917372
- ratio_gap: -3.74%
- ratio_slope_proxy(20d): -0.017107

### Volume (if available)

- volume: 9774300.00
- volume_MA20: 11322605.00
- volume_ratio: 0.86

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 15.67
- MA20 / MA60 / MA200: 18.56 / 21.25 / 18.99
- gap20 / gap60: -15.59% / -26.27%
- 5D return: -9.99%
- 20D high/low: 22.05 / 15.67

### Relative Strength

- ratio: 0.534812
- ratio_MA60: 0.579357
- ratio_gap: -7.69%
- ratio_slope_proxy(20d): 0.025212

### Volume (if available)

- volume: 28246900.00
- volume_MA20: 23788085.00
- volume_ratio: 1.19

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

- close: 4.83
- MA20 / MA60 / MA200: 5.45 / 5.60 / 5.89
- gap20 / gap60: -11.38% / -13.76%
- 5D return: -4.17%
- 20D high/low: 6.94 / 4.64

### Relative Strength

- ratio: 0.014302
- ratio_MA60: 0.014451
- ratio_gap: -1.03%
- ratio_slope_proxy(20d): 0.000340

### Volume (if available)

- volume: 64275300.00
- volume_MA20: 41205500.00
- volume_ratio: 1.56

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

- close: 11.87
- MA20 / MA60 / MA200: 12.63 / 13.34 / 12.92
- gap20 / gap60: -5.99% / -10.99%
- 5D return: -5.04%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.040100
- ratio_MA60: 0.046760
- ratio_gap: -14.24%
- ratio_slope_proxy(20d): -0.002962

### Volume (if available)

- volume: 5865500.00
- volume_MA20: 14439500.00
- volume_ratio: 0.41

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

- 데이터 기준일(주가): **2026-11-24**
- 실행시간(UTC): **2026-11-25 03:00:57**

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
- VIX: 26.62
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 2.27% / slope_proxy: 0.000779
- GDXJ/GLD gap: -11.05% / slope_proxy: -0.009049

## VZLA (Vizsla Silver)
- close: 2.69 | RSI14: 38.188168 | ATR14%: 8.15%
- MA20 gap: -12.21% | MA50 gap: -20.26% | MA200 gap: -23.59%
- vol_ratio(Volume/Vol20): 1.045471 | gap_open: 2.92%
- RS vs SILJ gap: 5.96% / slope_proxy: 0.003221
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
- close: 6.85 | RSI14: 45.602089 | ATR14%: 8.78%
- MA20 gap: -3.36% | MA50 gap: -13.96% | MA200 gap: -17.49%
- vol_ratio(Volume/Vol20): 0.990734 | gap_open: 1.17%
- SilverMarginGate: SI=40.634998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.72% / slope_proxy: 0.00616
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
- close: 12.87 | RSI14: 34.545957 | ATR14%: 11.88%
- MA20 gap: -21.32% | MA50 gap: -27.46% | MA200 gap: -53.82%
- vol_ratio(Volume/Vol20): 0.841116 | gap_open: 2.94%
- RS vs SILJ gap: -4.27% / slope_proxy: -0.043269
- RS vs GDXJ gap: -8.62% / slope_proxy: -0.014787
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

- 실행시간(UTC): **2026-11-25 03:01:07**
- 데이터 기준일(주가): **2026-11-24**

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
- VIX: 26.62 / 4주 변화 8.23 / 2026-11-23
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -4.91% / slope_proxy -2.43%
- GDXJ/GLD: gap -11.05% / slope_proxy -7.49%
- SILJ/SLV: gap 2.27% / slope_proxy 3.58%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.68 | RSI14: 33.69 | ATR14%: 6.73%
- MA20/50/200 gap: -9.26% / -21.30% / -17.49%
- 5D return: -4.30% | 20D drawdown: -20.48% | vol_ratio: 1.47
- RS vs GDXJ: gap 0.01% / slope_proxy 2.31%
- FundamentalScore: 88 | TechnicalScore: 55 | RegimeScore: 0 | OverallScore: **58.9**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 3.25 | RSI14: 22.31 | ATR14%: 12.33%
- MA20/50/200 gap: -31.59% / -46.09% / -51.01%
- 5D return: -19.75% | 20D drawdown: -44.82% | vol_ratio: 0.89
- RS vs GDXJ: gap -32.05% / slope_proxy -31.55%
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
- close: 0.55 | RSI14: 23.53 | ATR14%: 12.08%
- MA20/50/200 gap: -25.58% / -41.97% / -58.29%
- 5D return: -12.70% | 20D drawdown: -38.89% | vol_ratio: 0.24
- RS vs GDXJ: gap -29.52% / slope_proxy -23.33%
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
- close: 1.22 | RSI14: 27.59 | ATR14%: 11.71%
- MA20/50/200 gap: -20.13% / -37.33% / -36.93%
- 5D return: -15.86% | 20D drawdown: -32.22% | vol_ratio: 1.09
- RS vs GDXJ: gap -21.58% / slope_proxy -14.49%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 2.69 | RSI14: 34.54 | ATR14%: 8.62%
- MA20/50/200 gap: -12.21% / -20.26% / -23.59%
- 5D return: -9.43% | 20D drawdown: -23.14% | vol_ratio: 1.05
- RS vs SILJ: gap 5.96% / slope_proxy 6.08%
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
- close: 18.79 | RSI14: 26.75 | ATR14%: 8.68%
- MA20/50/200 gap: -17.24% / -25.28% / -11.51%
- 5D return: -12.85% | 20D drawdown: -29.81% | vol_ratio: 1.31
- RS vs SILJ: gap 0.11% / slope_proxy -4.48%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.85 | RSI14: 42.72 | ATR14%: 9.27%
- MA20/50/200 gap: -3.36% / -13.96% / -17.49%
- 5D return: -7.56% | 20D drawdown: -15.33% | vol_ratio: 0.99
- RS vs SILJ: gap 13.72% / slope_proxy 17.42%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 10.90 | RSI14: 24.33 | ATR14%: 7.84%
- MA20/50/200 gap: -17.49% / -28.49% / -37.88%
- 5D return: -12.80% | 20D drawdown: -29.27% | vol_ratio: 1.66
- RS vs SILJ: gap -6.34% / slope_proxy -6.08%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.78 | RSI14: 27.37 | ATR14%: 8.85%
- MA20/50/200 gap: -20.28% / -28.81% / -37.98%
- 5D return: -18.93% | 20D drawdown: -30.70% | vol_ratio: 0.90
- RS vs SILJ: gap -6.84% / slope_proxy -6.76%
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
- close: 1.90 | RSI14: 21.63 | ATR14%: 12.33%
- MA20/50/200 gap: -28.33% / -47.03% / -63.84%
- 5D return: -15.93% | 20D drawdown: -42.25% | vol_ratio: 1.05
- RS vs SILJ: gap -30.97% / slope_proxy -23.67%
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
- close: 3.47 | RSI14: 24.70 | ATR14%: 8.54%
- MA20/50/200 gap: -18.74% / -30.70% / -46.23%
- 5D return: -15.16% | 20D drawdown: -29.33% | vol_ratio: 0.94
- RS vs SILJ: gap -10.22% / slope_proxy -6.86%
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
- close: 12.87 | RSI14: 34.54 | ATR14%: 13.86%
- MA20/50/200 gap: -21.32% / -27.46% / -53.82%
- 5D return: -17.97% | 20D drawdown: -39.49% | vol_ratio: 0.84
- RS vs SILJ: gap -4.27% / slope_proxy -5.13%
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
