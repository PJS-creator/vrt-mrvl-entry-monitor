# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-04 03:01:18**
- 데이터 기준일(일봉): **2026-11-03**
- 데이터 기준일(주봉): **2026-11-02**
- VXN 기준일: **2026-11-02** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 685.28
- Weekly RSI14: **45.69**
- 52W MA: 665.57 / gap: **2.96%**
- 104W MA gap: **14.60%**
- 52W MA 13W slope: **5.03%**
- VXN: **30.89** / 5D change: 4.49

## Daily trigger: 실제 매수 타이밍

- QQQ close: 685.28
- Daily RSI14: **34.65**
- 20D gap: **-4.92%**
- 50D gap: **-5.30%**
- 200D gap: **0.92%**
- MACD hist: -4.5751 / change: -0.2323
- ATR14%: **1.86%**
- 20D high drawdown: **-9.56%**

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

- 데이터 기준일(주가): **2026-11-03**
- 실행시간(UTC): **2026-11-04 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.43 / 4주 변화 31.0 bp
- IG OAS (BAMLC0A0CM): 0.94 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.62 / 4주 변화 -33.0 bp
- VIX (VIXCLS): 21.15
- NFCI: -0.487

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.415478
- MA60: 8.374726
- gap: 0.49%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.331655
- MA60: 0.416028
- gap: -20.28%
- MA60_slope_proxy: 0.023596
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-03**
- 실행시간(UTC): **2026-11-04 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 149.97 bp / 4주 변화 -8.44 bp
- CURVE_10s5s: 35.58 bp / 4주 변화 -8.66 bp

## NWG Price
- close: 592.2
- MA50: 670.312 / gap50: -11.65%
- MA200: 634.8573 / gap200: -6.72%

## Relative Strength
- RS vs FTSE gap: -12.65% / slope_proxy: -0.001145
- RS vs Peers gap: -0.60% / slope_proxy: 0.022021

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-04 03:00:57**

## Commodity Regime

- WTI ref (CL=F): 95.03 / 5D -4.87%
- Brent ref (BZ=F): 102.71 / 5D -9.81%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.68
- Gas ref (NG=F): 2.85 / 5D 5.60%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.43
- MA20 / MA60 / MA200: 61.93 / 59.98 / 55.88
- gap20 / gap60: -2.43% / 0.76%
- 5D return: -3.67%
- 20D high/low: 64.17 / 58.21

### Relative Strength

- ratio: 0.906269
- ratio_MA60: 0.930501
- ratio_gap: -2.60%
- ratio_slope_proxy(20d): -0.012674

### Volume (if available)

- volume: 7433500.00
- volume_MA20: 8625740.00
- volume_ratio: 0.86

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.08
- MA20 / MA60 / MA200: 24.19 / 21.36 / 18.74
- gap20 / gap60: -12.87% / -1.32%
- 5D return: -5.47%
- 20D high/low: 26.16 / 21.08

### Relative Strength

- ratio: 0.664356
- ratio_MA60: 0.567772
- ratio_gap: 17.01%
- ratio_slope_proxy(20d): 0.040438

### Volume (if available)

- volume: 20930900.00
- volume_MA20: 27080365.00
- volume_ratio: 0.77

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.90
- MA20 / MA60 / MA200: 6.00 / 5.77 / 5.88
- gap20 / gap60: -1.75% / 2.18%
- 5D return: -8.67%
- 20D high/low: 6.94 / 5.39

### Relative Strength

- ratio: 0.015320
- ratio_MA60: 0.014339
- ratio_gap: 6.84%
- ratio_slope_proxy(20d): 0.000584

### Volume (if available)

- volume: 38048300.00
- volume_MA20: 42942130.00
- volume_ratio: 0.89

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.00
- MA20 / MA60 / MA200: 13.37 / 13.79 / 12.71
- gap20 / gap60: -2.76% / -5.75%
- 5D return: -5.87%
- 20D high/low: 14.79 / 12.50

### Relative Strength

- ratio: 0.041778
- ratio_MA60: 0.049066
- ratio_gap: -14.85%
- ratio_slope_proxy(20d): -0.001928

### Volume (if available)

- volume: 10587000.00
- volume_MA20: 16136330.00
- volume_ratio: 0.66

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-03**
- 실행시간(UTC): **2026-11-04 03:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 31.0 bp / latest 3.43
- IG OAS 4주 변화: 10.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: -33.0 bp / latest 2.62
- VIX: 21.15
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -1.29% / slope_proxy: 0.005387
- GDXJ/GLD gap: -11.37% / slope_proxy: 0.005104

## VZLA (Vizsla Silver)
- close: 3.03 | RSI14: 36.025578 | ATR14%: 5.96%
- MA20 gap: -7.00% | MA50 gap: -17.32% | MA200 gap: -18.47%
- vol_ratio(Volume/Vol20): 0.997311 | gap_open: 0.16%
- RS vs SILJ gap: 3.79% / slope_proxy: 0.00036
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.77 | RSI14: 34.597343 | ATR14%: 7.15%
- MA20 gap: -13.59% | MA50 gap: -22.53% | MA200 gap: -22.70%
- vol_ratio(Volume/Vol20): 1.276869 | gap_open: 2.01%
- SilverMarginGate: SI=49.325001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.76% / slope_proxy: 0.016122
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 16.09 | RSI14: 39.161974 | ATR14%: 7.43%
- MA20 gap: -5.38% | MA50 gap: -18.63% | MA200 gap: -46.12%
- vol_ratio(Volume/Vol20): 0.99694 | gap_open: 1.35%
- RS vs SILJ gap: -2.15% / slope_proxy: -0.049825
- RS vs GDXJ gap: -4.76% / slope_proxy: -0.016787
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-11-04 03:01:17**
- 데이터 기준일(주가): **2026-11-03**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.43 / 4주 변화 0.31 bp-ish / 2026-11-02
- IG OAS: 0.94 / 4주 변화 0.10 bp-ish / 2026-11-02
- 10Y Real Yield: 2.62 / 4주 변화 -0.30 bp-ish / 2026-11-02
- VIX: 21.15 / 4주 변화 5.63 / 2026-11-02
- NFCI: -0.49 / 4주 변화 0.02 / 2026-10-23

### Leadership ratios

- GDX/GLD: gap -7.23% / slope_proxy -5.00%
- GDXJ/GLD: gap -11.37% / slope_proxy -8.84%
- SILJ/SLV: gap -1.29% / slope_proxy 2.34%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.25 | RSI14: 26.79 | ATR14%: 5.01%
- MA20/50/200 gap: -13.95% / -22.70% / -10.50%
- 5D return: -11.37% | 20D drawdown: -22.54% | vol_ratio: 0.78
- RS vs GDXJ: gap -6.05% / slope_proxy -5.66%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.02 | RSI14: 25.00 | ATR14%: 6.55%
- MA20/50/200 gap: -17.82% / -28.65% / -27.48%
- 5D return: -13.00% | 20D drawdown: -28.69% | vol_ratio: 0.37
- RS vs GDXJ: gap -12.04% / slope_proxy -14.85%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **48.1**
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.78 | RSI14: 27.78 | ATR14%: 7.88%
- MA20/50/200 gap: -13.57% / -34.75% / -44.77%
- 5D return: -13.33% | 20D drawdown: -23.53% | vol_ratio: 0.69
- RS vs GDXJ: gap -22.28% / slope_proxy -6.86%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.59 | RSI14: 27.00 | ATR14%: 8.04%
- MA20/50/200 gap: -16.38% / -30.68% / -19.63%
- 5D return: -8.09% | 20D drawdown: -28.05% | vol_ratio: 0.56
- RS vs GDXJ: gap -14.05% / slope_proxy -14.09%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **36.0**
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
- close: 23.03 | RSI14: 37.74 | ATR14%: 5.80%
- MA20/50/200 gap: -8.93% / -14.44% / 10.20%
- 5D return: -7.58% | 20D drawdown: -16.01% | vol_ratio: 0.56
- RS vs SILJ: gap 7.71% / slope_proxy 3.32%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **58.7**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.03 | RSI14: 44.17 | ATR14%: 5.78%
- MA20/50/200 gap: -7.00% / -17.32% / -18.47%
- 5D return: -7.06% | 20D drawdown: -14.65% | vol_ratio: 1.00
- RS vs SILJ: gap 3.79% / slope_proxy 3.90%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **52.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.77 | RSI14: 33.14 | ATR14%: 6.69%
- MA20/50/200 gap: -13.59% / -22.53% / -22.70%
- 5D return: -9.85% | 20D drawdown: -25.69% | vol_ratio: 1.28
- RS vs SILJ: gap -2.76% / slope_proxy -6.04%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **49.8**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.03 | RSI14: 36.75 | ATR14%: 5.72%
- MA20/50/200 gap: -11.62% / -23.45% / -27.62%
- 5D return: -10.10% | 20D drawdown: -18.73% | vol_ratio: 0.88
- RS vs SILJ: gap -5.18% / slope_proxy -0.91%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **48.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.71 | RSI14: 21.05 | ATR14%: 7.91%
- MA20/50/200 gap: -23.12% / -38.50% / -52.12%
- 5D return: -15.05% | 20D drawdown: -37.84% | vol_ratio: 1.06
- RS vs SILJ: gap -23.84% / slope_proxy -23.78%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **47.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 13.21 | RSI14: 34.38 | ATR14%: 5.21%
- MA20/50/200 gap: -12.05% / -24.19% / -28.70%
- 5D return: -9.64% | 20D drawdown: -22.61% | vol_ratio: 0.97
- RS vs SILJ: gap -5.37% / slope_proxy -5.48%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **46.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.27 | RSI14: 35.27 | ATR14%: 6.16%
- MA20/50/200 gap: -13.88% / -27.65% / -37.67%
- 5D return: -11.41% | 20D drawdown: -23.06% | vol_ratio: 0.84
- RS vs SILJ: gap -11.23% / slope_proxy -5.87%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **38.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 16.09 | RSI14: 48.19 | ATR14%: 7.11%
- MA20/50/200 gap: -5.38% / -18.63% / -46.12%
- 5D return: -4.79% | 20D drawdown: -16.15% | vol_ratio: 1.00
- RS vs SILJ: gap -2.15% / slope_proxy 5.07%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **30.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
