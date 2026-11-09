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

- 실행시간(UTC): **2026-11-09 15:01:20**
- 데이터 기준일(일봉): **2026-11-09**
- 데이터 기준일(주봉): **2026-11-09**
- VXN 기준일: **2026-11-05** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 672.32
- Weekly RSI14: **44.05**
- 52W MA: 666.29 / gap: **0.91%**
- 104W MA gap: **12.16%**
- 52W MA 13W slope: **4.64%**
- VXN: **38.26** / 5D change: 13.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 672.32
- Daily RSI14: **38.69**
- 20D gap: **-4.49%**
- 50D gap: **-6.61%**
- 200D gap: **-1.14%**
- MACD hist: -5.4503 / change: 1.2105
- ATR14%: **2.32%**
- 20D high drawdown: **-9.58%**

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

- 데이터 기준일(주가): **2026-11-09**
- 실행시간(UTC): **2026-11-09 15:00:55**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.42 / 4주 변화 31.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.6 / 4주 변화 -27.0 bp
- VIX (VIXCLS): 28.18
- NFCI: -0.459

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.944366
- MA60: 8.216484
- gap: -15.48%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.3162
- MA60: 0.411686
- gap: -23.19%
- MA60_slope_proxy: 0.012182
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-09**
- 실행시간(UTC): **2026-11-09 15:00:59**

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
- TERM_SPREAD_10Y_POLICY: 113.92 bp / 4주 변화 -54.0 bp
- CURVE_10s5s: 36.78 bp / 4주 변화 -6.76 bp

## NWG Price
- close: 595.2
- MA50: 661.072 / gap50: -9.96%
- MA200: 633.4415 / gap200: -6.04%

## Relative Strength
- RS vs FTSE gap: -10.79% / slope_proxy: -0.001937
- RS vs Peers gap: -2.63% / slope_proxy: 0.016112

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-09 15:01:06**

## Commodity Regime

- WTI ref (CL=F): 87.52 / 5D -9.27%
- Brent ref (BZ=F): 94.01 / 5D -10.27%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.49
- Gas ref (NG=F): 3.14 / 5D 9.84%

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

- close: 55.84
- MA20 / MA60 / MA200: 61.24 / 59.86 / 56.16
- gap20 / gap60: -8.82% / -6.72%
- 5D return: -8.04%
- 20D high/low: 64.17 / 55.84

### Relative Strength

- ratio: 0.906494
- ratio_MA60: 0.927452
- ratio_gap: -2.26%
- ratio_slope_proxy(20d): -0.013813

### Volume (if available)

- volume: 1377254.00
- volume_MA20: 8861417.70
- volume_ratio: 0.16

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.44
- MA20 / MA60 / MA200: 22.99 / 21.46 / 18.85
- gap20 / gap60: -19.80% / -14.08%
- 5D return: -12.85%
- 20D high/low: 26.16 / 18.44

### Relative Strength

- ratio: 0.570280
- ratio_MA60: 0.572787
- ratio_gap: -0.44%
- ratio_slope_proxy(20d): 0.039317

### Volume (if available)

- volume: 4562364.00
- volume_MA20: 26336183.20
- volume_ratio: 0.17

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

- close: 5.24
- MA20 / MA60 / MA200: 5.95 / 5.74 / 5.89
- gap20 / gap60: -12.00% / -8.73%
- 5D return: -15.89%
- 20D high/low: 6.94 / 5.10

### Relative Strength

- ratio: 0.014571
- ratio_MA60: 0.014397
- ratio_gap: 1.21%
- ratio_slope_proxy(20d): 0.000600

### Volume (if available)

- volume: 3669156.00
- volume_MA20: 45921672.80
- volume_ratio: 0.08

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

- close: 11.60
- MA20 / MA60 / MA200: 13.07 / 13.67 / 12.76
- gap20 / gap60: -11.29% / -15.15%
- 5D return: -9.91%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041408
- ratio_MA60: 0.048439
- ratio_gap: -14.51%
- ratio_slope_proxy(20d): -0.002351

### Volume (if available)

- volume: 1918511.00
- volume_MA20: 16963895.55
- volume_ratio: 0.11

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

- 데이터 기준일(주가): **2026-11-09**
- 실행시간(UTC): **2026-11-09 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 31.0 bp / latest 3.42
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.6
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 7.22% / slope_proxy: 0.004969
- GDXJ/GLD gap: -0.67% / slope_proxy: 0.002107

## VZLA (Vizsla Silver)
- close: 3.415 | RSI14: 52.897015 | ATR14%: 5.76%
- MA20 gap: 6.03% | MA50 gap: -5.25% | MA200 gap: -6.55%
- vol_ratio(Volume/Vol20): 0.096589 | gap_open: 4.24%
- RS vs SILJ gap: 1.20% / slope_proxy: 0.000678
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
- close: 7.87 | RSI14: 50.546302 | ATR14%: 6.73%
- MA20 gap: 3.45% | MA50 gap: -8.14% | MA200 gap: -8.86%
- vol_ratio(Volume/Vol20): 0.202962 | gap_open: 5.45%
- SilverMarginGate: SI=52.779999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.09% / slope_proxy: 0.011943
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
- close: 20.059999 | RSI14: 61.026917 | ATR14%: 7.07%
- MA20 gap: 18.07% | MA50 gap: 4.41% | MA200 gap: -31.61%
- vol_ratio(Volume/Vol20): 0.236008 | gap_open: 5.17%
- RS vs SILJ gap: 7.54% / slope_proxy: -0.052313
- RS vs GDXJ gap: 3.36% / slope_proxy: -0.017631
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

- 실행시간(UTC): **2026-11-09 15:01:19**
- 데이터 기준일(주가): **2026-11-09**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **False**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.42 / 4주 변화 0.31 bp-ish / 2026-11-06
- IG OAS: 0.93 / 4주 변화 0.10 bp-ish / 2026-11-06
- 10Y Real Yield: 2.60 / 4주 변화 -0.32 bp-ish / 2026-11-05
- VIX: 28.18 / 4주 변화 12.77 / 2026-11-05
- NFCI: -0.46 / 4주 변화 0.04 / 2026-10-30

### Leadership ratios

- GDX/GLD: gap 2.67% / slope_proxy 4.85%
- GDXJ/GLD: gap -0.59% / slope_proxy 2.25%
- SILJ/SLV: gap 7.22% / slope_proxy 10.63%
- Gold breadth proxy: above50 69.23%, above200 53.85%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.36 | RSI14: 44.91 | ATR14%: 4.82%
- MA20/50/200 gap: 1.80% / -8.73% / 2.98%
- 5D return: 11.62% | 20D drawdown: -7.21% | vol_ratio: 0.05
- RS vs GDXJ: gap -7.17% / slope_proxy -8.20%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 45 | OverallScore: **53.9**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.80 | RSI14: 41.87 | ATR14%: 5.90%
- MA20/50/200 gap: -0.75% / -15.24% / -15.45%
- 5D return: 10.48% | 20D drawdown: -13.43% | vol_ratio: 0.27
- RS vs GDXJ: gap -12.89% / slope_proxy -14.35%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 45 | OverallScore: **51.1**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.87 | RSI14: 41.46 | ATR14%: 7.27%
- MA20/50/200 gap: -0.29% / -23.20% / -37.48%
- 5D return: 11.54% | 20D drawdown: -10.31% | vol_ratio: 0.10
- RS vs GDXJ: gap -24.12% / slope_proxy -11.26%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 45 | OverallScore: **45.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.75 | RSI14: 38.79 | ATR14%: 8.16%
- MA20/50/200 gap: -3.18% / -21.05% / -11.10%
- 5D return: 10.76% | 20D drawdown: -18.22% | vol_ratio: 0.30
- RS vs GDXJ: gap -18.91% / slope_proxy -17.55%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 45 | OverallScore: **39.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.44 | RSI14: 50.62 | ATR14%: 6.06%
- MA20/50/200 gap: 5.45% / -0.98% / 25.66%
- 5D return: 11.99% | 20D drawdown: -0.86% | vol_ratio: 0.15
- RS vs SILJ: gap 6.44% / slope_proxy 2.85%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 25 | OverallScore: **66.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.41 | RSI14: 55.33 | ATR14%: 5.93%
- MA20/50/200 gap: 6.03% / -5.25% / -6.55%
- 5D return: 11.97% | 20D drawdown: 0.00% | vol_ratio: 0.10
- RS vs SILJ: gap 1.20% / slope_proxy 3.55%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.13 | RSI14: 49.13 | ATR14%: 5.89%
- MA20/50/200 gap: 3.98% / -8.96% / -15.37%
- 5D return: 12.46% | 20D drawdown: -2.16% | vol_ratio: 0.12
- RS vs SILJ: gap -4.12% / slope_proxy 0.53%
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
- close: 15.41 | RSI14: 52.66 | ATR14%: 5.51%
- MA20/50/200 gap: 5.25% / -9.04% / -15.41%
- 5D return: 13.85% | 20D drawdown: -4.73% | vol_ratio: 0.06
- RS vs SILJ: gap -4.14% / slope_proxy -2.94%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.87 | RSI14: 46.05 | ATR14%: 6.61%
- MA20/50/200 gap: 3.45% / -8.14% / -8.86%
- 5D return: 13.24% | 20D drawdown: -7.08% | vol_ratio: 0.20
- RS vs SILJ: gap -2.09% / slope_proxy -5.34%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **43.6**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.22 | RSI14: 40.72 | ATR14%: 7.54%
- MA20/50/200 gap: -2.09% / -23.33% / -42.02%
- 5D return: 11.98% | 20D drawdown: -19.78% | vol_ratio: 0.14
- RS vs SILJ: gap -19.71% / slope_proxy -18.27%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.86 | RSI14: 42.98 | ATR14%: 5.93%
- MA20/50/200 gap: 0.88% / -14.42% / -28.49%
- 5D return: 10.84% | 20D drawdown: -8.91% | vol_ratio: 0.15
- RS vs SILJ: gap -11.06% / slope_proxy -4.88%
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
- close: 20.09 | RSI14: 65.36 | ATR14%: 6.95%
- MA20/50/200 gap: 18.23% / 4.56% / -31.51%
- 5D return: 23.03% | 20D drawdown: 0.00% | vol_ratio: 0.24
- RS vs SILJ: gap 7.70% / slope_proxy 16.49%
- FundamentalScore: 42 | TechnicalScore: 25 | RegimeScore: 25 | OverallScore: **32.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
