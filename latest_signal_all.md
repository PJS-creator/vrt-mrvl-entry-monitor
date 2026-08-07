# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: EXK**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-07 01:38:13**
- 데이터 기준일(일봉): **2026-08-06**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-08-05** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 714.65
- Weekly RSI14: **59.53**
- 52W MA: 634.21 / gap: **12.68%**
- 104W MA gap: **25.70%**
- 52W MA 13W slope: **7.30%**
- VXN: **24.15** / 5D change: -6.69

## Daily trigger: 실제 매수 타이밍

- QQQ close: 714.65
- Daily RSI14: **54.35**
- 20D gap: **2.03%**
- 50D gap: **0.03%**
- 200D gap: **10.60%**
- MACD hist: 3.7125 / change: 0.5099
- ATR14%: **2.15%**
- 20D high drawdown: **-1.50%**

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

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-07 01:37:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.41 / 4주 변화 10.0 bp
- VIX (VIXCLS): 15.81
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.738663
- MA60: 9.464967
- gap: -7.67%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.368412
- MA60: 0.388483
- gap: -5.17%
- MA60_slope_proxy: 0.013504
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-07 01:37:46**

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
- close: 713.8
- MA50: 650.496 / gap50: 9.73%
- MA200: 616.1819 / gap200: 15.84%

## Relative Strength
- RS vs FTSE gap: 8.10% / slope_proxy: 0.002325
- RS vs Peers gap: 5.57% / slope_proxy: 0.000502

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-07 01:37:53**

## Commodity Regime

- WTI ref (CL=F): 77.83 / 5D -6.89%
- Brent ref (BZ=F): 83.17 / 5D N/A
- Brent Tier: **80-90**
- Brent-WTI spread: 5.34
- Gas ref (NG=F): 2.62 / 5D -4.93%

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

- close: 56.04
- MA20 / MA60 / MA200: 55.35 / 55.04 / 50.18
- gap20 / gap60: 1.25% / 1.81%
- 5D return: 0.16%
- 20D high/low: 57.60 / 52.89

### Relative Strength

- ratio: 0.963549
- ratio_MA60: 0.968116
- ratio_gap: -0.47%
- ratio_slope_proxy(20d): -0.015029

### Volume (if available)

- volume: 16207079.00
- volume_MA20: 8779838.95
- volume_ratio: 1.85

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.52
- MA20 / MA60 / MA200: 18.38 / 18.11 / 16.24
- gap20 / gap60: 0.75% / 2.24%
- 5D return: -3.14%
- 20D high/low: 19.40 / 17.32

### Relative Strength

- ratio: 0.517174
- ratio_MA60: 0.513076
- ratio_gap: 0.80%
- ratio_slope_proxy(20d): -0.005413

### Volume (if available)

- volume: 11949034.00
- volume_MA20: 14153551.70
- volume_ratio: 0.84

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

- close: 5.16
- MA20 / MA60 / MA200: 5.19 / 5.69 / 5.35
- gap20 / gap60: -0.64% / -9.37%
- 5D return: 1.57%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013161
- ratio_MA60: 0.014146
- ratio_gap: -6.97%
- ratio_slope_proxy(20d): -0.000454

### Volume (if available)

- volume: 43699053.00
- volume_MA20: 42500287.65
- volume_ratio: 1.03

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.58
- MA20 / MA60 / MA200: 13.37 / 12.67 / 10.77
- gap20 / gap60: 1.56% / 7.19%
- 5D return: 2.57%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.051097
- ratio_MA60: 0.051355
- ratio_gap: -0.50%
- ratio_slope_proxy(20d): 0.001187

### Volume (if available)

- volume: 12165478.00
- volume_MA20: 15499183.90
- volume_ratio: 0.78

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

- 데이터 기준일(주가): **2026-08-06**
- 실행시간(UTC): **2026-08-07 01:38:03**

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
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.41
- VIX: 15.81
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 7.12% / slope_proxy: 0.010501
- GDXJ/GLD gap: 4.35% / slope_proxy: -0.007546

## VZLA (Vizsla Silver)
- close: 3.53 | RSI14: 58.20393 | ATR14%: 5.36%
- MA20 gap: 8.82% | MA50 gap: 4.47% | MA200 gap: -13.78%
- vol_ratio(Volume/Vol20): 0.662925 | gap_open: 1.39%
- RS vs SILJ gap: 1.95% / slope_proxy: 0.006066
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
- close: 7.97 | RSI14: 66.455135 | ATR14%: 6.11%
- MA20 gap: 21.01% | MA50 gap: 16.71% | MA200 gap: -5.58%
- vol_ratio(Volume/Vol20): 1.067003 | gap_open: 3.39%
- SilverMarginGate: SI=62.064999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.21% / slope_proxy: -0.004923
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
- close: 23.799999 | RSI14: 56.400441 | ATR14%: 7.40%
- MA20 gap: 14.84% | MA50 gap: -0.51% | MA200 gap: -15.19%
- vol_ratio(Volume/Vol20): 0.857629 | gap_open: 3.92%
- RS vs SILJ gap: -8.67% / slope_proxy: -0.146158
- RS vs GDXJ gap: -11.40% / slope_proxy: -0.035607
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

- 실행시간(UTC): **2026-08-07 01:38:10**
- 데이터 기준일(주가): **2026-08-06**

## Verdict
**🟡 Precious miners watch/add-on candidates: EXK**

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
- 10Y Real Yield: 2.41 / 4주 변화 0.10 bp-ish / 2026-08-05
- VIX: 15.81 / 4주 변화 -1.09 / 2026-08-05
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 4.59% / slope_proxy 7.50%
- GDXJ/GLD: gap 4.35% / slope_proxy 7.04%
- SILJ/SLV: gap 7.12% / slope_proxy 4.39%
- Gold breadth proxy: above50 92.31%, above200 30.77%, count 13
- Silver breadth proxy: above50 69.23%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.66 | RSI14: 78.37 | ATR14%: 4.84%
- MA20/50/200 gap: 18.18% / 13.79% / 25.46%
- 5D return: 16.40% | 20D drawdown: 0.00% | vol_ratio: 1.99
- RS vs GDXJ: gap 7.20% / slope_proxy 1.52%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **77.3**
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.93 | RSI14: 56.04 | ATR14%: 6.22%
- MA20/50/200 gap: 2.28% / 9.14% / 6.39%
- 5D return: 8.43% | 20D drawdown: -6.31% | vol_ratio: 1.63
- RS vs GDXJ: gap 1.10% / slope_proxy -3.51%
- FundamentalScore: 55 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **66.0**
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
- close: 6.27 | RSI14: 83.64 | ATR14%: 5.39%
- MA20/50/200 gap: 17.49% / 12.43% / -8.23%
- 5D return: 17.20% | 20D drawdown: 0.00% | vol_ratio: 1.09
- RS vs GDXJ: gap 4.85% / slope_proxy 7.26%
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
- close: 1.36 | RSI14: 78.18 | ATR14%: 5.41%
- MA20/50/200 gap: 18.88% / 11.73% / -7.79%
- 5D return: 20.35% | 20D drawdown: 0.00% | vol_ratio: 1.84
- RS vs GDXJ: gap 4.80% / slope_proxy 4.30%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.83 | RSI14: 67.84 | ATR14%: 5.68%
- MA20/50/200 gap: 11.06% / 6.00% / -7.52%
- 5D return: 13.64% | 20D drawdown: -1.45% | vol_ratio: 0.94
- RS vs SILJ: gap 1.40% / slope_proxy 1.13%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **65.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 25.20 | RSI14: 73.22 | ATR14%: 5.83%
- MA20/50/200 gap: 23.58% / 28.45% / 52.44%
- 5D return: 22.99% | 20D drawdown: 0.00% | vol_ratio: 1.11
- RS vs SILJ: gap 26.70% / slope_proxy 14.82%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.97 | RSI14: 75.96 | ATR14%: 5.99%
- MA20/50/200 gap: 21.01% / 16.71% / -5.58%
- 5D return: 17.55% | 20D drawdown: 0.00% | vol_ratio: 1.07
- RS vs SILJ: gap 10.21% / slope_proxy 13.29%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.53 | RSI14: 64.94 | ATR14%: 5.21%
- MA20/50/200 gap: 8.82% / 4.47% / -13.78%
- 5D return: 8.95% | 20D drawdown: -1.67% | vol_ratio: 0.66
- RS vs SILJ: gap 1.95% / slope_proxy 4.37%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.86 | RSI14: 59.85 | ATR14%: 5.58%
- MA20/50/200 gap: 5.11% / 1.83% / -13.50%
- 5D return: 6.23% | 20D drawdown: -4.11% | vol_ratio: 0.86
- RS vs SILJ: gap -2.32% / slope_proxy -7.23%
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
- close: 4.67 | RSI14: 66.54 | ATR14%: 6.52%
- MA20/50/200 gap: 14.57% / -1.70% / -18.41%
- 5D return: 18.53% | 20D drawdown: -2.91% | vol_ratio: 1.16
- RS vs SILJ: gap -7.13% / slope_proxy 0.50%
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
- close: 6.38 | RSI14: 62.29 | ATR14%: 6.09%
- MA20/50/200 gap: 10.45% / 3.70% / -4.16%
- 5D return: 15.37% | 20D drawdown: -1.54% | vol_ratio: 0.93
- RS vs SILJ: gap -0.19% / slope_proxy -2.41%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **47.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 23.80 | RSI14: 67.90 | ATR14%: 6.67%
- MA20/50/200 gap: 14.84% / -0.51% / -15.19%
- 5D return: 18.58% | 20D drawdown: -2.78% | vol_ratio: 0.86
- RS vs SILJ: gap -8.67% / slope_proxy 3.01%
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
