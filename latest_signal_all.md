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

- 실행시간(UTC): **2026-08-06 03:01:17**
- 데이터 기준일(일봉): **2026-08-05**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-08-04** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 717.30
- Weekly RSI14: **59.99**
- 52W MA: 634.26 / gap: **13.09%**
- 104W MA gap: **26.16%**
- 52W MA 13W slope: **7.31%**
- VXN: **25.48** / 5D change: -3.13

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.30
- Daily RSI14: **55.42**
- 20D gap: **2.34%**
- 50D gap: **0.36%**
- 200D gap: **11.11%**
- MACD hist: 3.2026 / change: 1.2597
- ATR14%: **2.20%**
- 20D high drawdown: **-1.13%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-06 03:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.73 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.4 / 4주 변화 10.0 bp
- VIX (VIXCLS): 16.5
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.815097
- MA60: 9.493085
- gap: -7.14%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.370405
- MA60: 0.387282
- gap: -4.36%
- MA60_slope_proxy: 0.014038
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-06 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 118.82 bp / 4주 변화 16.88 bp
- CURVE_10s5s: 47.26 bp / 4주 변화 -1.69 bp

## NWG Price
- close: 716.0
- MA50: 648.212 / gap50: 10.46%
- MA200: 615.2889 / gap200: 16.37%

## Relative Strength
- RS vs FTSE gap: 8.85% / slope_proxy: 0.002216
- RS vs Peers gap: 2.75% / slope_proxy: -0.001301

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-06 03:00:55**

## Commodity Regime

- WTI ref (CL=F): 75.56 / 5D -10.54%
- Brent ref (BZ=F): 79.86 / 5D -11.99%
- Brent Tier: **70-80**
- Brent-WTI spread: 4.30
- Gas ref (NG=F): 2.67 / 5D -1.83%

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

- close: 53.81
- MA20 / MA60 / MA200: 55.16 / 55.02 / 50.10
- gap20 / gap60: -2.45% / -2.20%
- 5D return: -3.96%
- 20D high/low: 57.60 / 52.30

### Relative Strength

- ratio: 0.938929
- ratio_MA60: 0.968173
- ratio_gap: -3.02%
- ratio_slope_proxy(20d): -0.016059

### Volume (if available)

- volume: 6715428.00
- volume_MA20: 8289356.40
- volume_ratio: 0.81

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.36
- MA20 / MA60 / MA200: 18.31 / 18.15 / 16.21
- gap20 / gap60: 0.28% / 1.16%
- 5D return: -1.24%
- 20D high/low: 19.40 / 17.03

### Relative Strength

- ratio: 0.508446
- ratio_MA60: 0.513418
- ratio_gap: -0.97%
- ratio_slope_proxy(20d): -0.005736

### Volume (if available)

- volume: 13827811.00
- volume_MA20: 14502990.55
- volume_ratio: 0.95

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

- close: 5.14
- MA20 / MA60 / MA200: 5.19 / 5.72 / 5.35
- gap20 / gap60: -1.00% / -10.08%
- 5D return: 3.84%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013349
- ratio_MA60: 0.014180
- ratio_gap: -5.86%
- ratio_slope_proxy(20d): -0.000460

### Volume (if available)

- volume: 28614301.00
- volume_MA20: 42070950.05
- volume_ratio: 0.68

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

- close: 12.43
- MA20 / MA60 / MA200: 13.32 / 12.64 / 10.75
- gap20 / gap60: -6.68% / -1.63%
- 5D return: -4.75%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.048791
- ratio_MA60: 0.051307
- ratio_gap: -4.90%
- ratio_slope_proxy(20d): 0.001125

### Volume (if available)

- volume: 9449906.00
- volume_MA20: 15668580.30
- volume_ratio: 0.60

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-06 03:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.73
- IG OAS 4주 변화: 2.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.4
- VIX: 16.5
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 7.98% / slope_proxy: 0.00967
- GDXJ/GLD gap: 4.32% / slope_proxy: -0.007837

## VZLA (Vizsla Silver)
- close: 3.59 | RSI14: 60.629215 | ATR14%: 5.42%
- MA20 gap: 11.30% | MA50 gap: 6.13% | MA200 gap: -12.42%
- vol_ratio(Volume/Vol20): 1.545125 | gap_open: 5.00%
- RS vs SILJ gap: 2.92% / slope_proxy: 0.006081
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
- close: 7.96 | RSI14: 66.366754 | ATR14%: 6.09%
- MA20 gap: 22.06% | MA50 gap: 16.54% | MA200 gap: -5.61%
- vol_ratio(Volume/Vol20): 1.327783 | gap_open: 7.29%
- SilverMarginGate: SI=62.57 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.08% / slope_proxy: -0.005294
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
- close: 24.48 | RSI14: 59.164672 | ATR14%: 7.38%
- MA20 gap: 18.69% | MA50 gap: 1.53% | MA200 gap: -12.51%
- vol_ratio(Volume/Vol20): 1.766018 | gap_open: 7.71%
- RS vs SILJ gap: -7.67% / slope_proxy: -0.145661
- RS vs GDXJ gap: -9.67% / slope_proxy: -0.035046
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

- 실행시간(UTC): **2026-08-06 03:01:16**
- 데이터 기준일(주가): **2026-08-05**

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

- HY OAS: 2.73 / 4주 변화 0.06 bp-ish / 2026-08-04
- IG OAS: 0.78 / 4주 변화 0.02 bp-ish / 2026-08-04
- 10Y Real Yield: 2.40 / 4주 변화 0.10 bp-ish / 2026-08-04
- VIX: 16.50 / 4주 변화 0.37 / 2026-08-04
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 4.23% / slope_proxy 7.18%
- GDXJ/GLD: gap 4.32% / slope_proxy 7.33%
- SILJ/SLV: gap 7.98% / slope_proxy 4.75%
- Gold breadth proxy: above50 92.31%, above200 15.38%, count 13
- Silver breadth proxy: above50 92.31%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.20 | RSI14: 72.34 | ATR14%: 4.80%
- MA20/50/200 gap: 12.59% / 7.76% / 19.05%
- 5D return: 15.01% | 20D drawdown: 0.00% | vol_ratio: 1.59
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.24 | RSI14: 78.57 | ATR14%: 5.48%
- MA20/50/200 gap: 18.16% / 11.84% / -8.70%
- 5D return: 15.56% | 20D drawdown: 0.00% | vol_ratio: 3.12
- RS vs GDXJ: gap 4.33% / slope_proxy 5.60%
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
- close: 1.34 | RSI14: 70.69 | ATR14%: 5.41%
- MA20/50/200 gap: 18.32% / 10.05% / -9.18%
- 5D return: 19.64% | 20D drawdown: 0.00% | vol_ratio: 1.22
- RS vs GDXJ: gap 3.34% / slope_proxy 3.55%
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
- close: 1.94 | RSI14: 52.04 | ATR14%: 6.30%
- MA20/50/200 gap: 3.25% / 9.82% / 7.09%
- 5D return: 5.43% | 20D drawdown: -5.83% | vol_ratio: 1.55
- RS vs GDXJ: gap 1.92% / slope_proxy -4.29%
- FundamentalScore: 55 | TechnicalScore: 55 | RegimeScore: 75 | OverallScore: **59.0**
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
- close: 25.07 | RSI14: 72.97 | ATR14%: 5.82%
- MA20/50/200 gap: 24.57% / 28.63% / 52.25%
- 5D return: 30.44% | 20D drawdown: 0.00% | vol_ratio: 1.71
- RS vs SILJ: gap 25.77% / slope_proxy 16.30%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.59 | RSI14: 67.57 | ATR14%: 5.23%
- MA20/50/200 gap: 11.30% / 6.13% / -12.42%
- 5D return: 15.06% | 20D drawdown: 0.00% | vol_ratio: 1.55
- RS vs SILJ: gap 2.92% / slope_proxy 4.72%
- FundamentalScore: 72 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **73.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.96 | RSI14: 68.70 | ATR14%: 5.58%
- MA20/50/200 gap: 13.11% / 7.36% / -6.16%
- 5D return: 18.52% | 20D drawdown: 0.00% | vol_ratio: 1.13
- RS vs SILJ: gap 1.82% / slope_proxy 0.23%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.96 | RSI14: 75.13 | ATR14%: 5.94%
- MA20/50/200 gap: 22.06% / 16.54% / -5.61%
- 5D return: 26.15% | 20D drawdown: 0.00% | vol_ratio: 1.33
- RS vs SILJ: gap 9.08% / slope_proxy 10.01%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **62.3**
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
- close: 16.54 | RSI14: 63.87 | ATR14%: 5.26%
- MA20/50/200 gap: 9.65% / 5.96% / -9.74%
- 5D return: 16.89% | 20D drawdown: 0.00% | vol_ratio: 1.09
- RS vs SILJ: gap 0.78% / slope_proxy -3.44%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **60.6**
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
- close: 4.81 | RSI14: 70.66 | ATR14%: 6.34%
- MA20/50/200 gap: 18.31% / 0.74% / -15.95%
- 5D return: 31.42% | 20D drawdown: 0.00% | vol_ratio: 1.61
- RS vs SILJ: gap -5.64% / slope_proxy -0.59%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.48 | RSI14: 63.90 | ATR14%: 6.09%
- MA20/50/200 gap: 12.40% / 5.14% / -2.62%
- 5D return: 22.96% | 20D drawdown: 0.00% | vol_ratio: 1.79
- RS vs SILJ: gap 0.45% / slope_proxy -2.87%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **47.2**
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
- close: 24.48 | RSI14: 72.89 | ATR14%: 6.55%
- MA20/50/200 gap: 18.69% / 1.53% / -12.51%
- 5D return: 27.77% | 20D drawdown: 0.00% | vol_ratio: 1.77
- RS vs SILJ: gap -7.67% / slope_proxy 3.51%
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
