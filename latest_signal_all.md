# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: JAG.TO, AYA, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-04 03:01:03**
- 데이터 기준일(일봉): **2026-08-03**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-07-31** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 700.07
- Weekly RSI14: **56.80**
- 52W MA: 633.93 / gap: **10.43%**
- 104W MA gap: **23.17%**
- 52W MA 13W slope: **7.25%**
- VXN: **26.00** / 5D change: -2.39

## Daily trigger: 실제 매수 타이밍

- QQQ close: 700.07
- Daily RSI14: **50.06**
- 20D gap: **0.03%**
- 50D gap: **-2.02%**
- 200D gap: **8.65%**
- MACD hist: -0.7932 / change: 1.7676
- ATR14%: **2.19%**
- 20D high drawdown: **-3.51%**

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

- 데이터 기준일(주가): **2026-08-03**
- 실행시간(UTC): **2026-08-04 03:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 9.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.47 / 4주 변화 21.0 bp
- VIX (VIXCLS): 15.99
- NFCI: -0.554

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.431089
- MA60: 9.529579
- gap: -11.53%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.355251
- MA60: 0.384721
- gap: -7.66%
- MA60_slope_proxy: 0.015056
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-31**
- 실행시간(UTC): **2026-08-04 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 124.67 bp / 4주 변화 24.77 bp
- CURVE_10s5s: 47.32 bp / 4주 변화 -1.4 bp

## NWG Price
- close: 705.8
- MA50: 643.048 / gap50: 9.76%
- MA200: 613.4957 / gap200: 15.05%

## Relative Strength
- RS vs FTSE gap: 7.98% / slope_proxy: 0.002114
- RS vs Peers gap: 2.53% / slope_proxy: -0.002187

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-04 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 81.11 / 5D -1.82%
- Brent ref (BZ=F): 84.70 / 5D -4.14%
- Brent Tier: **80-90**
- Brent-WTI spread: 3.59
- Gas ref (NG=F): 2.77 / 5D 0.07%

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

- close: 55.47
- MA20 / MA60 / MA200: 54.98 / 54.98 / 49.97
- gap20 / gap60: 0.89% / 0.89%
- 5D return: 0.98%
- 20D high/low: 57.60 / 51.68

### Relative Strength

- ratio: 0.943528
- ratio_MA60: 0.968853
- ratio_gap: -2.61%
- ratio_slope_proxy(20d): -0.017623

### Volume (if available)

- volume: 7027304.00
- volume_MA20: 9042965.20
- volume_ratio: 0.78

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.06
- MA20 / MA60 / MA200: 18.15 / 18.20 / 16.14
- gap20 / gap60: 5.02% / 4.70%
- 5D return: 5.89%
- 20D high/low: 19.40 / 16.66

### Relative Strength

- ratio: 0.523339
- ratio_MA60: 0.513742
- ratio_gap: 1.87%
- ratio_slope_proxy(20d): -0.006157

### Volume (if available)

- volume: 11118307.00
- volume_MA20: 15416200.35
- volume_ratio: 0.72

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

- close: 5.15
- MA20 / MA60 / MA200: 5.19 / 5.75 / 5.33
- gap20 / gap60: -0.70% / -10.48%
- 5D return: -2.46%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013477
- ratio_MA60: 0.014235
- ratio_gap: -5.33%
- ratio_slope_proxy(20d): -0.000476

### Volume (if available)

- volume: 25351491.00
- volume_MA20: 42448054.55
- volume_ratio: 0.60

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

- close: 13.08
- MA20 / MA60 / MA200: 13.25 / 12.60 / 10.72
- gap20 / gap60: -1.32% / 3.81%
- 5D return: 2.03%
- 20D high/low: 15.16 / 11.59

### Relative Strength

- ratio: 0.050682
- ratio_MA60: 0.051248
- ratio_gap: -1.10%
- ratio_slope_proxy(20d): 0.000984

### Volume (if available)

- volume: 10436283.00
- volume_MA20: 16515179.15
- volume_ratio: 0.63

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

- 데이터 기준일(주가): **2026-08-03**
- 실행시간(UTC): **2026-08-04 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.47
- VIX: 15.99
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 3.70% / slope_proxy: 0.008016
- GDXJ/GLD gap: -1.57% / slope_proxy: -0.008654

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 50.39216 | ATR14%: 5.82%
- MA20 gap: 2.56% | MA50 gap: -3.49% | MA200 gap: -20.74%
- vol_ratio(Volume/Vol20): 0.527109 | gap_open: 0.96%
- RS vs SILJ gap: 4.96% / slope_proxy: 0.006064
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
- close: 6.73 | RSI14: 52.44718 | ATR14%: 6.72%
- MA20 gap: 5.25% | MA50 gap: -1.77% | MA200 gap: -20.17%
- vol_ratio(Volume/Vol20): 0.660192 | gap_open: 1.08%
- SilverMarginGate: SI=58.98 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 3.02% / slope_proxy: -0.005278
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
- close: 20.620001 | RSI14: 45.551575 | ATR14%: 8.31%
- MA20 gap: 1.04% | MA50 gap: -15.79% | MA200 gap: -25.92%
- vol_ratio(Volume/Vol20): 0.823955 | gap_open: 1.64%
- RS vs SILJ gap: -14.18% / slope_proxy: -0.145612
- RS vs GDXJ gap: -16.59% / slope_proxy: -0.034693
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

- 실행시간(UTC): **2026-08-04 03:01:02**
- 데이터 기준일(주가): **2026-08-03**

## Verdict
**🟡 Precious miners watch/add-on candidates: JAG.TO, AYA, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.84 / 4주 변화 0.09 bp-ish / 2026-07-30
- IG OAS: 0.80 / 4주 변화 0.05 bp-ish / 2026-07-30
- 10Y Real Yield: 2.47 / 4주 변화 0.21 bp-ish / 2026-07-31
- VIX: 15.99 / 4주 변화 0.18 / 2026-07-31
- NFCI: -0.55 / 4주 변화 -0.07 / 2026-07-24

### Leadership ratios

- GDX/GLD: gap -0.77% / slope_proxy 1.94%
- GDXJ/GLD: gap -1.57% / slope_proxy 1.29%
- SILJ/SLV: gap 3.70% / slope_proxy 1.76%
- Gold breadth proxy: above50 7.69%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.39 | RSI14: 65.00 | ATR14%: 5.30%
- MA20/50/200 gap: 3.19% / -3.43% / -21.23%
- 5D return: 1.13% | 20D drawdown: -4.09% | vol_ratio: 1.19
- RS vs GDXJ: gap 3.44% / slope_proxy 4.47%
- FundamentalScore: 82 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **62.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.88 | RSI14: 42.86 | ATR14%: 6.76%
- MA20/50/200 gap: 0.83% / 5.74% / 4.07%
- 5D return: -1.05% | 20D drawdown: -8.74% | vol_ratio: 0.15
- RS vs GDXJ: gap 14.06% / slope_proxy 20.47%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **60.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, StaticRiskPolicy=WATCH_ONLY

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.22 | RSI14: 46.70 | ATR14%: 5.16%
- MA20/50/200 gap: -0.54% / -5.39% / 5.12%
- 5D return: 0.28% | 20D drawdown: -6.96% | vol_ratio: 0.94
- RS vs GDXJ: gap -0.11% / slope_proxy -6.35%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **50.9**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.13 | RSI14: 54.05 | ATR14%: 5.63%
- MA20/50/200 gap: 0.49% / -7.42% / -23.56%
- 5D return: 3.67% | 20D drawdown: -9.60% | vol_ratio: 0.35
- RS vs GDXJ: gap 0.19% / slope_proxy -1.53%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **42.8**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 20.34 | RSI14: 51.45 | ATR14%: 6.39%
- MA20/50/200 gap: 3.66% / 5.82% / 24.33%
- 5D return: -1.21% | 20D drawdown: -2.68% | vol_ratio: 0.74
- RS vs SILJ: gap 15.56% / slope_proxy 10.49%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.73 | RSI14: 53.56 | ATR14%: 6.46%
- MA20/50/200 gap: 5.25% / -1.77% / -20.17%
- 5D return: 6.66% | 20D drawdown: -0.74% | vol_ratio: 0.66
- RS vs SILJ: gap 3.02% / slope_proxy 7.78%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **58.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.26 | RSI14: 52.34 | ATR14%: 5.59%
- MA20/50/200 gap: 2.56% / -3.49% / -20.74%
- 5D return: -1.81% | 20D drawdown: -4.68% | vol_ratio: 0.53
- RS vs SILJ: gap 4.96% / slope_proxy 7.63%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **57.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.73 | RSI14: 44.68 | ATR14%: 6.14%
- MA20/50/200 gap: -1.45% / -7.66% / -19.15%
- 5D return: -2.64% | 20D drawdown: -7.31% | vol_ratio: 0.63
- RS vs SILJ: gap -1.84% / slope_proxy -1.68%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **53.1**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.43 | RSI14: 41.30 | ATR14%: 5.60%
- MA20/50/200 gap: -3.93% / -7.83% / -21.20%
- 5D return: -5.00% | 20D drawdown: -8.79% | vol_ratio: 0.47
- RS vs SILJ: gap -1.70% / slope_proxy -5.39%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **51.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.09 | RSI14: 47.64 | ATR14%: 7.12%
- MA20/50/200 gap: 1.36% / -15.16% / -28.57%
- 5D return: 0.49% | 20D drawdown: -8.30% | vol_ratio: 0.88
- RS vs SILJ: gap -10.92% / slope_proxy -4.74%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.53 | RSI14: 42.52 | ATR14%: 6.80%
- MA20/50/200 gap: -3.58% / -10.50% / -16.94%
- 5D return: -2.81% | 20D drawdown: -11.66% | vol_ratio: 0.75
- RS vs SILJ: gap -4.05% / slope_proxy -7.06%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **43.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 20.62 | RSI14: 45.14 | ATR14%: 7.79%
- MA20/50/200 gap: 1.04% / -15.79% / -25.92%
- 5D return: 0.93% | 20D drawdown: -5.67% | vol_ratio: 0.82
- RS vs SILJ: gap -14.18% / slope_proxy -3.11%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **35.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
