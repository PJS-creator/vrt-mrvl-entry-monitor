# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-23 03:01:01**
- 데이터 기준일(일봉): **2026-06-22**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-18** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 737.14
- Weekly RSI14: **69.97**
- 52W MA: 618.02 / gap: **19.27%**
- 104W MA gap: **32.79%**
- 52W MA 13W slope: **8.58%**
- VXN: **26.31** / 5D change: -4.13

## Daily trigger: 실제 매수 타이밍

- QQQ close: 737.95
- Daily RSI14: **58.30**
- 20D gap: **1.47%**
- 50D gap: **6.18%**
- 200D gap: **17.52%**
- MACD hist: -1.0260 / change: 0.5627
- ATR14%: **2.10%**
- 20D high drawdown: **-0.99%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-22**
- 실행시간(UTC): **2026-06-23 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.66 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.21 / 4주 변화 3.0 bp
- VIX (VIXCLS): 16.78
- NFCI: -0.505

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.587399
- MA60: 9.197263
- gap: 15.11%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.460241
- MA60: 0.343808
- gap: 33.87%
- MA60_slope_proxy: 0.06948
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-22**
- 실행시간(UTC): **2026-06-23 03:00:42**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **True**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 97.13 bp / 4주 변화 -20.8 bp
- CURVE_10s5s: 44.9 bp / 4주 변화 -0.88 bp

## NWG Price
- close: 663.0
- MA50: 594.2811 / gap50: 11.56%
- MA200: 593.0044 / gap200: 11.80%

## Relative Strength
- RS vs FTSE gap: 11.87% / slope_proxy: 0.000969
- RS vs Peers gap: 1.77% / slope_proxy: -0.017485

## Why not today?
- CurveGreen=FALSE
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-23 03:00:48**

## Commodity Regime

- WTI ref (CL=F): 74.12 / 5D -12.68%
- Brent ref (BZ=F): 78.08 / 5D -10.59%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.96
- Gas ref (NG=F): 3.27 / 5D 4.71%

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

- close: 52.00
- MA20 / MA60 / MA200: 56.26 / 57.75 / 48.77
- gap20 / gap60: -7.58% / -9.96%
- 5D return: -8.03%
- 20D high/low: 59.37 / 51.82

### Relative Strength

- ratio: 0.961894
- ratio_MA60: 1.005301
- ratio_gap: -4.32%
- ratio_slope_proxy(20d): 0.002396

### Volume (if available)

- volume: 7616743.00
- volume_MA20: 10204812.15
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.01
- MA20 / MA60 / MA200: 18.08 / 19.76 / 15.38
- gap20 / gap60: -5.93% / -13.91%
- 5D return: -7.45%
- 20D high/low: 19.75 / 16.75

### Relative Strength

- ratio: 0.496352
- ratio_MA60: 0.529427
- ratio_gap: -6.25%
- ratio_slope_proxy(20d): 0.008723

### Volume (if available)

- volume: 12033340.00
- volume_MA20: 15302387.00
- volume_ratio: 0.79

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

- close: 5.41
- MA20 / MA60 / MA200: 6.03 / 6.40 / 5.06
- gap20 / gap60: -10.28% / -15.46%
- 5D return: -10.43%
- 20D high/low: 6.81 / 5.31

### Relative Strength

- ratio: 0.013911
- ratio_MA60: 0.015142
- ratio_gap: -8.13%
- ratio_slope_proxy(20d): -0.000675

### Volume (if available)

- volume: 30855413.00
- volume_MA20: 30520045.65
- volume_ratio: 1.01

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

- close: 11.26
- MA20 / MA60 / MA200: 12.37 / 13.08 / 10.82
- gap20 / gap60: -9.01% / -13.92%
- 5D return: -13.80%
- 20D high/low: 13.81 / 11.02

### Relative Strength

- ratio: 0.048776
- ratio_MA60: 0.051744
- ratio_gap: -5.74%
- ratio_slope_proxy(20d): 0.000986

### Volume (if available)

- volume: 15252544.00
- volume_MA20: 14191877.20
- volume_ratio: 1.07

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

- 데이터 기준일(주가): **2026-06-22**
- 실행시간(UTC): **2026-06-23 03:00:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.66
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.21
- VIX: 16.78
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.71% / slope_proxy: -0.001398
- GDXJ/GLD gap: -1.46% / slope_proxy: -0.004064

## VZLA (Vizsla Silver)
- close: 3.52 | RSI14: 48.252454 | ATR14%: 6.51%
- MA20 gap: -3.07% | MA50 gap: -0.19% | MA200 gap: -17.18%
- vol_ratio(Volume/Vol20): 0.708655 | gap_open: 0.85%
- RS vs SILJ gap: 9.25% / slope_proxy: 0.004507
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
- close: 7.06 | RSI14: 44.115466 | ATR14%: 8.64%
- MA20 gap: -4.21% | MA50 gap: -13.36% | MA200 gap: -16.98%
- vol_ratio(Volume/Vol20): 0.804215 | gap_open: 2.10%
- SilverMarginGate: SI=63.610001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.56% / slope_proxy: -0.010449
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
- close: 25.049999 | RSI14: 36.834134 | ATR14%: 10.26%
- MA20 gap: -12.94% | MA50 gap: -27.78% | MA200 gap: -2.46%
- vol_ratio(Volume/Vol20): 0.598318 | gap_open: 3.52%
- RS vs SILJ gap: -21.51% / slope_proxy: -0.074173
- RS vs GDXJ gap: -19.77% / slope_proxy: -0.016192
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

- 실행시간(UTC): **2026-06-23 03:01:00**
- 데이터 기준일(주가): **2026-06-22**

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

- HY OAS: 2.66 / 4주 변화 -0.08 bp-ish / 2026-06-19
- IG OAS: 0.74 / 4주 변화 0.00 bp-ish / 2026-06-19
- 10Y Real Yield: 2.21 / 4주 변화 0.08 bp-ish / 2026-06-18
- VIX: 16.78 / 4주 변화 0.08 / 2026-06-19
- NFCI: -0.51 / 4주 변화 0.06 / 2026-06-12

### Leadership ratios

- GDX/GLD: gap -0.78% / slope_proxy 3.07%
- GDXJ/GLD: gap -1.46% / slope_proxy 2.30%
- SILJ/SLV: gap 5.71% / slope_proxy 11.17%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.12 | RSI14: 44.92 | ATR14%: 6.14%
- MA20/50/200 gap: 1.34% / 2.54% / 23.47%
- 5D return: 6.98% | 20D drawdown: -6.67% | vol_ratio: 0.64
- RS vs GDXJ: gap 16.64% / slope_proxy 5.31%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **75.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.31 | RSI14: 45.68 | ATR14%: 7.28%
- MA20/50/200 gap: -0.27% / -4.13% / -12.48%
- 5D return: -4.38% | 20D drawdown: -10.88% | vol_ratio: 0.42
- RS vs GDXJ: gap 4.48% / slope_proxy 3.60%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **51.5**
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
- close: 5.56 | RSI14: 32.80 | ATR14%: 7.31%
- MA20/50/200 gap: -7.75% / -14.90% / -19.91%
- 5D return: -6.24% | 20D drawdown: -21.13% | vol_ratio: 0.34
- RS vs GDXJ: gap -7.31% / slope_proxy -1.38%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.57 | RSI14: 27.78 | ATR14%: 6.82%
- MA20/50/200 gap: -9.85% / -15.65% / -5.67%
- 5D return: -7.10% | 20D drawdown: -20.30% | vol_ratio: 0.66
- RS vs GDXJ: gap -4.77% / slope_proxy -19.45%
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
- close: 19.74 | RSI14: 46.61 | ATR14%: 7.40%
- MA20/50/200 gap: 3.40% / 6.72% / 29.87%
- 5D return: 5.51% | 20D drawdown: -8.14% | vol_ratio: 0.80
- RS vs SILJ: gap 18.83% / slope_proxy 17.74%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.52 | RSI14: 35.52 | ATR14%: 6.66%
- MA20/50/200 gap: -3.07% / -0.19% / -17.18%
- 5D return: -1.95% | 20D drawdown: -14.77% | vol_ratio: 0.71
- RS vs SILJ: gap 9.25% / slope_proxy 9.03%
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
- close: 15.98 | RSI14: 40.25 | ATR14%: 6.19%
- MA20/50/200 gap: -1.84% / -9.45% / -10.14%
- 5D return: 4.51% | 20D drawdown: -10.22% | vol_ratio: 1.22
- RS vs SILJ: gap -2.81% / slope_proxy -1.77%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.55 | RSI14: 38.70 | ATR14%: 7.25%
- MA20/50/200 gap: -4.10% / -9.17% / -9.47%
- 5D return: -0.47% | 20D drawdown: -14.24% | vol_ratio: 0.56
- RS vs SILJ: gap -1.40% / slope_proxy -3.31%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.42 | RSI14: 40.00 | ATR14%: 7.88%
- MA20/50/200 gap: -2.68% / -6.02% / -1.30%
- 5D return: 0.47% | 20D drawdown: -13.48% | vol_ratio: 0.66
- RS vs SILJ: gap 2.78% / slope_proxy 2.62%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **52.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.06 | RSI14: 40.39 | ATR14%: 8.88%
- MA20/50/200 gap: -4.21% / -13.36% / -16.98%
- 5D return: 1.15% | 20D drawdown: -15.25% | vol_ratio: 0.80
- RS vs SILJ: gap -5.56% / slope_proxy -8.23%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.33 | RSI14: 38.44 | ATR14%: 8.48%
- MA20/50/200 gap: -4.52% / -9.99% / -4.84%
- 5D return: 0.95% | 20D drawdown: -17.11% | vol_ratio: 0.68
- RS vs SILJ: gap -0.96% / slope_proxy -4.08%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 25.05 | RSI14: 30.86 | ATR14%: 9.88%
- MA20/50/200 gap: -12.94% / -27.78% / -2.46%
- 5D return: -2.76% | 20D drawdown: -25.93% | vol_ratio: 0.60
- RS vs SILJ: gap -21.51% / slope_proxy -19.10%
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
