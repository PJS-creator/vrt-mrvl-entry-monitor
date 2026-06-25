# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-25 03:01:20**
- 데이터 기준일(일봉): **2026-06-24**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-23** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 710.62
- Weekly RSI14: **62.08**
- 52W MA: 617.51 / gap: **15.08%**
- 104W MA gap: **28.07%**
- 52W MA 13W slope: **8.49%**
- VXN: **32.37** / 5D change: 6.45

## Daily trigger: 실제 매수 타이밍

- QQQ close: 710.62
- Daily RSI14: **48.05**
- 20D gap: **-2.14%**
- 50D gap: **1.67%**
- 200D gap: **12.92%**
- MACD hist: -3.2167 / change: -0.9474
- ATR14%: **2.27%**
- 20D high drawdown: **-4.66%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-25 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -1.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.29 / 4주 변화 19.0 bp
- VIX (VIXCLS): 19.49
- NFCI: -0.516

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.612236
- MA60: 9.240795
- gap: 4.02%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.447069
- MA60: 0.350239
- gap: 27.65%
- MA60_slope_proxy: 0.071024
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-25 03:00:48**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **True**
- MacroGreen: **True**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 103.3 bp / 4주 변화 -8.36 bp
- CURVE_10s5s: 45.6 bp / 4주 변화 0.94 bp

## NWG Price
- close: 647.0
- MA50: 595.8251 / gap50: 8.59%
- MA200: 594.4374 / gap200: 8.84%

## Relative Strength
- RS vs FTSE gap: 8.37% / slope_proxy: 0.001274
- RS vs Peers gap: 0.92% / slope_proxy: -0.016582

## Why not today?
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-25 03:00:55**

## Commodity Regime

- WTI ref (CL=F): 69.42 / 5D -8.72%
- Brent ref (BZ=F): 72.61 / 5D -8.04%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.19
- Gas ref (NG=F): 3.29 / 5D 1.54%

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

- close: 51.09
- MA20 / MA60 / MA200: 55.64 / 57.33 / 48.83
- gap20 / gap60: -8.18% / -10.88%
- 5D return: -4.81%
- 20D high/low: 59.37 / 51.09

### Relative Strength

- ratio: 0.953705
- ratio_MA60: 1.002253
- ratio_gap: -4.84%
- ratio_slope_proxy(20d): -0.002241

### Volume (if available)

- volume: 7783774.00
- volume_MA20: 10243508.70
- volume_ratio: 0.76

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.45
- MA20 / MA60 / MA200: 17.81 / 19.64 / 15.43
- gap20 / gap60: -7.62% / -16.25%
- 5D return: -3.52%
- 20D high/low: 18.82 / 16.45

### Relative Strength

- ratio: 0.485968
- ratio_MA60: 0.527255
- ratio_gap: -7.83%
- ratio_slope_proxy(20d): 0.002717

### Volume (if available)

- volume: 12681802.00
- volume_MA20: 15106685.10
- volume_ratio: 0.84

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.04
- MA20 / MA60 / MA200: 5.88 / 6.34 / 5.08
- gap20 / gap60: -14.31% / -20.52%
- 5D return: -9.84%
- 20D high/low: 6.25 / 5.04

### Relative Strength

- ratio: 0.013575
- ratio_MA60: 0.015042
- ratio_gap: -9.75%
- ratio_slope_proxy(20d): -0.000734

### Volume (if available)

- volume: 42277721.00
- volume_MA20: 30459481.05
- volume_ratio: 1.39

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 10.51
- MA20 / MA60 / MA200: 12.13 / 12.87 / 10.80
- gap20 / gap60: -13.33% / -18.34%
- 5D return: -5.23%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045525
- ratio_MA60: 0.051353
- ratio_gap: -11.35%
- ratio_slope_proxy(20d): 0.000085

### Volume (if available)

- volume: 14605371.00
- volume_MA20: 14165408.55
- volume_ratio: 1.03

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-25 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.29
- VIX: 19.49
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 8.13% / slope_proxy: 0.001626
- GDXJ/GLD gap: -6.22% / slope_proxy: -0.002557

## VZLA (Vizsla Silver)
- close: 3.11 | RSI14: 37.668912 | ATR14%: 7.48%
- MA20 gap: -13.61% | MA50 gap: -11.76% | MA200 gap: -26.75%
- vol_ratio(Volume/Vol20): 0.970146 | gap_open: 2.99%
- RS vs SILJ gap: 6.67% / slope_proxy: 0.004512
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
- close: 6.33 | RSI14: 37.722515 | ATR14%: 9.34%
- MA20 gap: -12.25% | MA50 gap: -21.62% | MA200 gap: -25.63%
- vol_ratio(Volume/Vol20): 0.921008 | gap_open: 5.29%
- SilverMarginGate: SI=56.73 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.83% / slope_proxy: -0.009894
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
- close: 21.700001 | RSI14: 30.997116 | ATR14%: 11.56%
- MA20 gap: -21.77% | MA50 gap: -36.26% | MA200 gap: -16.06%
- vol_ratio(Volume/Vol20): 1.375053 | gap_open: 5.10%
- RS vs SILJ gap: -23.93% / slope_proxy: -0.079286
- RS vs GDXJ gap: -22.64% / slope_proxy: -0.017255
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

- 실행시간(UTC): **2026-06-25 03:01:17**
- 데이터 기준일(주가): **2026-06-24**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA**

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

- HY OAS: 2.71 / 4주 변화 0.00 bp-ish / 2026-06-23
- IG OAS: 0.74 / 4주 변화 0.00 bp-ish / 2026-06-23
- 10Y Real Yield: 2.29 / 4주 변화 0.13 bp-ish / 2026-06-23
- VIX: 19.49 / 4주 변화 2.48 / 2026-06-23
- NFCI: -0.52 / 4주 변화 0.05 / 2026-06-19

### Leadership ratios

- GDX/GLD: gap -4.46% / slope_proxy -2.54%
- GDXJ/GLD: gap -6.22% / slope_proxy -4.71%
- SILJ/SLV: gap 8.13% / slope_proxy 10.90%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.28 | RSI14: 38.90 | ATR14%: 7.06%
- MA20/50/200 gap: -8.14% / -8.30% / 10.23%
- 5D return: -13.23% | 20D drawdown: -16.32% | vol_ratio: 2.22
- RS vs GDXJ: gap 14.33% / slope_proxy 2.14%
- FundamentalScore: 88 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **64.8**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.16 | RSI14: 40.66 | ATR14%: 8.47%
- MA20/50/200 gap: -10.63% / -14.39% / -22.68%
- 5D return: -17.14% | 20D drawdown: -21.09% | vol_ratio: 1.41
- RS vs GDXJ: gap 2.22% / slope_proxy 2.95%
- FundamentalScore: 70 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **56.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 4.96 | RSI14: 29.83 | ATR14%: 7.81%
- MA20/50/200 gap: -16.02% / -22.99% / -28.53%
- 5D return: -15.93% | 20D drawdown: -29.65% | vol_ratio: 1.80
- RS vs GDXJ: gap -8.16% / slope_proxy -6.88%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **53.4**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.48 | RSI14: 27.47 | ATR14%: 7.34%
- MA20/50/200 gap: -13.37% / -19.63% / -11.58%
- 5D return: -10.30% | 20D drawdown: -24.87% | vol_ratio: 1.09
- RS vs GDXJ: gap -1.25% / slope_proxy -7.28%
- FundamentalScore: 55 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **41.2**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 17.12 | RSI14: 40.42 | ATR14%: 8.60%
- MA20/50/200 gap: -10.11% / -7.66% / 12.11%
- 5D return: -18.67% | 20D drawdown: -20.34% | vol_ratio: 0.89
- RS vs SILJ: gap 12.93% / slope_proxy 7.50%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **63.7**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.71 | RSI14: 36.68 | ATR14%: 8.00%
- MA20/50/200 gap: -11.99% / -17.51% / -18.52%
- 5D return: -17.10% | 20D drawdown: -22.67% | vol_ratio: 1.07
- RS vs SILJ: gap -1.26% / slope_proxy -2.76%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **58.4**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.11 | RSI14: 30.16 | ATR14%: 7.66%
- MA20/50/200 gap: -13.61% / -11.76% / -26.75%
- 5D return: -15.72% | 20D drawdown: -24.70% | vol_ratio: 0.97
- RS vs SILJ: gap 6.67% / slope_proxy 0.99%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.52 | RSI14: 36.68 | ATR14%: 6.93%
- MA20/50/200 gap: -9.43% / -16.86% / -18.61%
- 5D return: -13.16% | 20D drawdown: -18.43% | vol_ratio: 1.27
- RS vs SILJ: gap -1.69% / slope_proxy 0.76%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **56.6**
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
- close: 4.56 | RSI14: 33.58 | ATR14%: 9.92%
- MA20/50/200 gap: -16.67% / -22.51% / -18.88%
- 5D return: -22.45% | 20D drawdown: -29.08% | vol_ratio: 1.04
- RS vs SILJ: gap -5.81% / slope_proxy -8.53%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **52.1**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.33 | RSI14: 39.39 | ATR14%: 9.46%
- MA20/50/200 gap: -12.25% / -21.62% / -25.63%
- 5D return: -20.58% | 20D drawdown: -24.01% | vol_ratio: 0.92
- RS vs SILJ: gap -5.83% / slope_proxy -4.48%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **49.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.64 | RSI14: 36.59 | ATR14%: 8.82%
- MA20/50/200 gap: -13.24% / -16.85% / -13.49%
- 5D return: -18.85% | 20D drawdown: -23.99% | vol_ratio: 0.90
- RS vs SILJ: gap -0.04% / slope_proxy -0.75%
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
- close: 21.70 | RSI14: 25.18 | ATR14%: 11.36%
- MA20/50/200 gap: -21.77% / -36.26% / -16.06%
- 5D return: -18.33% | 20D drawdown: -35.84% | vol_ratio: 1.38
- RS vs SILJ: gap -23.93% / slope_proxy -20.24%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **40.4**
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
