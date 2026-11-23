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

- 실행시간(UTC): **2026-11-23 15:01:19**
- 데이터 기준일(일봉): **2026-11-23**
- 데이터 기준일(주봉): **2026-11-23**
- VXN 기준일: **2026-11-20** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 650.28
- Weekly RSI14: **43.33**
- 52W MA: 667.49 / gap: **-2.58%**
- 104W MA gap: **8.03%**
- 52W MA 13W slope: **3.92%**
- VXN: **45.25** / 5D change: 15.87

## Daily trigger: 실제 매수 타이밍

- QQQ close: 650.28
- Daily RSI14: **41.97**
- 20D gap: **-3.72%**
- 50D gap: **-8.38%**
- 200D gap: **-4.69%**
- MACD hist: -3.3117 / change: 1.4633
- ATR14%: **3.21%**
- 20D high drawdown: **-10.38%**

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

- 데이터 기준일(주가): **2026-11-23**
- 실행시간(UTC): **2026-11-23 15:00:53**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.52 / 4주 변화 12.0 bp
- IG OAS (BAMLC0A0CM): 0.98 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 2.88 / 4주 변화 24.0 bp
- VIX (VIXCLS): 35.89
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.069925
- MA60: 7.958727
- gap: -11.17%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.315135
- MA60: 0.395308
- gap: -20.28%
- MA60_slope_proxy: -0.01908
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-23**
- 실행시간(UTC): **2026-11-23 15:00:55**

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
- TERM_SPREAD_10Y_POLICY: 128.85 bp / 4주 변화 -23.99 bp
- CURVE_10s5s: 34.78 bp / 4주 변화 -2.26 bp

## NWG Price
- close: 588.8
- MA50: 641.16 / gap50: -8.17%
- MA200: 629.8392 / gap200: -6.52%

## Relative Strength
- RS vs FTSE gap: -7.27% / slope_proxy: -0.002907
- RS vs Peers gap: 0.70% / slope_proxy: 0.002452

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-23 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 81.85 / 5D -4.51%
- Brent ref (BZ=F): 88.00 / 5D -4.80%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.15
- Gas ref (NG=F): 3.50 / 5D 12.17%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **False**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.07
- MA20 / MA60 / MA200: 58.01 / 59.30 / 56.73
- gap20 / gap60: -6.80% / -8.82%
- 5D return: -5.74%
- 20D high/low: 64.00 / 53.76

### Relative Strength

- ratio: 0.890554
- ratio_MA60: 0.918529
- ratio_gap: -3.05%
- ratio_slope_proxy(20d): -0.016369

### Volume (if available)

- volume: 1342241.00
- volume_MA20: 10629212.05
- volume_ratio: 0.13

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.15
- MA20 / MA60 / MA200: 18.91 / 21.32 / 18.99
- gap20 / gap60: -14.59% / -24.23%
- 5D return: -6.63%
- 20D high/low: 22.30 / 16.01

### Relative Strength

- ratio: 0.549896
- ratio_MA60: 0.579548
- ratio_gap: -5.12%
- ratio_slope_proxy(20d): 0.027765

### Volume (if available)

- volume: 2079368.00
- volume_MA20: 23322873.40
- volume_ratio: 0.09

### Checks

- RISK_OK_SOFT: **False**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 4.67
- MA20 / MA60 / MA200: 5.53 / 5.62 / 5.89
- gap20 / gap60: -15.65% / -16.94%
- 5D return: -10.63%
- 20D high/low: 6.94 / 4.64

### Relative Strength

- ratio: 0.013700
- ratio_MA60: 0.014434
- ratio_gap: -5.09%
- ratio_slope_proxy(20d): 0.000362

### Volume (if available)

- volume: 4303484.00
- volume_MA20: 38364019.20
- volume_ratio: 0.11

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

- close: 12.09
- MA20 / MA60 / MA200: 12.73 / 13.38 / 12.91
- gap20 / gap60: -5.06% / -9.67%
- 5D return: -3.05%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.040497
- ratio_MA60: 0.046932
- ratio_gap: -13.71%
- ratio_slope_proxy(20d): -0.002866

### Volume (if available)

- volume: 1430890.00
- volume_MA20: 14047949.50
- volume_ratio: 0.10

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

- 데이터 기준일(주가): **2026-11-23**
- 실행시간(UTC): **2026-11-23 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **False**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 12.0 bp / latest 3.52
- IG OAS 4주 변화: 7.0 bp / latest 0.98
- 10Y Real Yield 4주 변화: 24.0 bp / latest 2.88
- VIX: 35.89
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -1.26% / slope_proxy: 0.001109
- GDXJ/GLD gap: -11.47% / slope_proxy: -0.007979

## VZLA (Vizsla Silver)
- close: 2.695 | RSI14: 37.798452 | ATR14%: 8.28%
- MA20 gap: -12.79% | MA50 gap: -20.60% | MA200 gap: -23.59%
- vol_ratio(Volume/Vol20): 0.184397 | gap_open: 11.93%
- RS vs SILJ gap: 2.95% / slope_proxy: 0.003025
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.01 | RSI14: 47.064864 | ATR14%: 8.72%
- MA20 gap: -1.67% | MA50 gap: -12.38% | MA200 gap: -15.82%
- vol_ratio(Volume/Vol20): 0.438727 | gap_open: 13.72%
- SilverMarginGate: SI=43.605 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.97% / slope_proxy: 0.00589
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **False**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 13.905 | RSI14: 39.121317 | ATR14%: 11.34%
- MA20 gap: -16.23% | MA50 gap: -22.38% | MA200 gap: -50.35%
- vol_ratio(Volume/Vol20): 0.268283 | gap_open: 16.93%
- RS vs SILJ gap: -0.14% / slope_proxy: -0.043673
- RS vs GDXJ gap: -4.60% / slope_proxy: -0.014886
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **False**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- RiskGreen=FALSE
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- RiskFilter(ATR/Gap/Shock)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-11-23 15:01:16**
- 데이터 기준일(주가): **2026-11-23**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **False**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.52 / 4주 변화 0.12 bp-ish / 2026-11-19
- IG OAS: 0.98 / 4주 변화 0.07 bp-ish / 2026-11-20
- 10Y Real Yield: 2.88 / 4주 변화 0.12 bp-ish / 2026-11-19
- VIX: 35.89 / 4주 변화 16.44 / 2026-11-20
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -6.51% / slope_proxy -3.38%
- GDXJ/GLD: gap -11.48% / slope_proxy -7.09%
- SILJ/SLV: gap -1.26% / slope_proxy 1.16%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.39 | RSI14: 39.33 | ATR14%: 7.27%
- MA20/50/200 gap: -14.11% / -25.38% / -21.17%
- 5D return: -7.60% | 20D drawdown: -23.99% | vol_ratio: 0.14
- RS vs GDXJ: gap -7.23% / slope_proxy -6.95%
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
- close: 3.45 | RSI14: 30.11 | ATR14%: 11.97%
- MA20/50/200 gap: -29.15% / -43.56% / -48.09%
- 5D return: -11.64% | 20D drawdown: -41.34% | vol_ratio: 0.20
- RS vs GDXJ: gap -30.36% / slope_proxy -28.62%
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
- close: 0.60 | RSI14: 32.00 | ATR14%: 10.95%
- MA20/50/200 gap: -20.69% / -37.84% / -54.72%
- 5D return: -13.04% | 20D drawdown: -33.33% | vol_ratio: 0.10
- RS vs GDXJ: gap -26.13% / slope_proxy -20.52%
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
- close: 1.27 | RSI14: 36.89 | ATR14%: 12.26%
- MA20/50/200 gap: -18.17% / -35.58% / -34.45%
- 5D return: -13.61% | 20D drawdown: -29.44% | vol_ratio: 0.46
- RS vs GDXJ: gap -21.23% / slope_proxy -12.48%
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
- close: 7.01 | RSI14: 51.76 | ATR14%: 9.55%
- MA20/50/200 gap: -1.67% / -12.38% / -15.82%
- 5D return: 9.19% | 20D drawdown: -13.35% | vol_ratio: 0.44
- RS vs SILJ: gap 12.98% / slope_proxy 15.08%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 0 | OverallScore: **47.3**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 2.69 | RSI14: 42.04 | ATR14%: 8.95%
- MA20/50/200 gap: -12.79% / -20.60% / -23.59%
- 5D return: -8.02% | 20D drawdown: -23.00% | vol_ratio: 0.18
- RS vs SILJ: gap 2.95% / slope_proxy 1.92%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 0 | OverallScore: **46.4**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.98 | RSI14: 38.45 | ATR14%: 9.36%
- MA20/50/200 gap: -17.55% / -25.01% / -10.60%
- 5D return: -10.77% | 20D drawdown: -29.10% | vol_ratio: 0.23
- RS vs SILJ: gap -1.97% / slope_proxy -6.10%
- FundamentalScore: 86 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **44.0**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.14 | RSI14: 41.02 | ATR14%: 8.95%
- MA20/50/200 gap: -16.56% / -25.15% / -34.40%
- 5D return: -14.20% | 20D drawdown: -26.44% | vol_ratio: 0.25
- RS vs SILJ: gap -4.47% / slope_proxy -3.28%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 11.15 | RSI14: 38.87 | ATR14%: 8.55%
- MA20/50/200 gap: -16.79% / -27.61% / -36.72%
- 5D return: -8.80% | 20D drawdown: -27.68% | vol_ratio: 0.13
- RS vs SILJ: gap -7.44% / slope_proxy -6.02%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **40.4**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.09 | RSI14: 36.97 | ATR14%: 11.90%
- MA20/50/200 gap: -23.12% / -42.64% / -60.46%
- 5D return: -8.33% | 20D drawdown: -36.47% | vol_ratio: 0.27
- RS vs SILJ: gap -27.12% / slope_proxy -19.23%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **35.9**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.69 | RSI14: 39.64 | ATR14%: 8.52%
- MA20/50/200 gap: -14.95% / -27.09% / -43.15%
- 5D return: -8.44% | 20D drawdown: -24.85% | vol_ratio: 0.23
- RS vs SILJ: gap -7.97% / slope_proxy -5.62%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **32.2**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 13.88 | RSI14: 43.42 | ATR14%: 13.33%
- MA20/50/200 gap: -16.38% / -22.52% / -50.43%
- 5D return: -9.28% | 20D drawdown: -34.74% | vol_ratio: 0.27
- RS vs SILJ: gap -0.32% / slope_proxy 1.26%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **24.2**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
