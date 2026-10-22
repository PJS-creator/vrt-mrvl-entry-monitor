# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-22 03:01:17**
- 데이터 기준일(일봉): **2026-10-21**
- 데이터 기준일(주봉): **2026-10-19**
- VXN 기준일: **2026-10-21** / source: `Yahoo Finance ^VXN fallback; FRED error=Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 725.20
- Weekly RSI14: **55.61**
- 52W MA: 663.23 / gap: **9.34%**
- 104W MA gap: **21.99%**
- 52W MA 13W slope: **5.58%**
- VXN: **24.42** / 5D change: 1.72

## Daily trigger: 실제 매수 타이밍

- QQQ close: 725.20
- Daily RSI14: **46.07**
- 20D gap: **-1.88%**
- 50D gap: **-0.16%**
- 200D gap: **7.39%**
- MACD hist: -4.2939 / change: 0.6961
- ATR14%: **1.51%**
- 20D high drawdown: **-4.54%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-22 03:00:52**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DFII10 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VIXCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED NFCI failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.29 / 4주 변화 63.0 bp
- IG OAS (BAMLC0A0CM): 0.87 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.8 / 4주 변화 18.0 bp
- VIX (VIXCLS): 17.31
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.692168
- MA60: 8.451943
- gap: -8.99%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.439662
- MA60: 0.409703
- gap: 7.31%
- MA60_slope_proxy: 0.021173
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-22 03:00:55**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VIXCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED NFCI failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 162.4 bp / 4주 변화 21.1 bp
- CURVE_10s5s: 40.62 bp / 4주 변화 1.7 bp

## NWG Price
- close: 641.4
- MA50: 683.1272 / gap50: -6.11%
- MA200: 635.421 / gap200: 0.94%

## Relative Strength
- RS vs FTSE gap: -6.45% / slope_proxy: -0.000209
- RS vs Peers gap: 2.73% / slope_proxy: 0.016991

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-22 03:01:00**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DCOILBRENTEU failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DHHNGSP failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED OVXCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VIXCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DTWEXBGS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED NFCI failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VXEWZCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 98.23 / 5D 3.30%
- Brent ref (BZ=F): 110.38 / 5D 4.07%
- Brent Tier: **>=90**
- Brent-WTI spread: 12.15
- Gas ref (NG=F): 2.78 / 5D -13.13%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 62.70
- MA20 / MA60 / MA200: 59.40 / 58.93 / 54.96
- gap20 / gap60: 5.55% / 6.40%
- 5D return: 2.10%
- 20D high/low: 62.92 / 54.94

### Relative Strength

- ratio: 0.919894
- ratio_MA60: 0.936497
- ratio_gap: -1.77%
- ratio_slope_proxy(20d): -0.010692

### Volume (if available)

- volume: 7773800.00
- volume_MA20: 8968770.00
- volume_ratio: 0.87

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 25.66
- MA20 / MA60 / MA200: 23.65 / 20.67 / 18.23
- gap20 / gap60: 8.50% / 24.14%
- 5D return: -1.08%
- 20D high/low: 26.00 / 20.37

### Relative Strength

- ratio: 0.603623
- ratio_MA60: 0.545893
- ratio_gap: 10.58%
- ratio_slope_proxy(20d): 0.032871

### Volume (if available)

- volume: 16163500.00
- volume_MA20: 23753950.00
- volume_ratio: 0.68

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.04
- MA20 / MA60 / MA200: 5.50 / 5.59 / 5.78
- gap20 / gap60: 9.81% / 8.02%
- 5D return: 8.24%
- 20D high/low: 6.04 / 5.17

### Relative Strength

- ratio: 0.015346
- ratio_MA60: 0.013944
- ratio_gap: 10.06%
- ratio_slope_proxy(20d): 0.000191

### Volume (if available)

- volume: 31835500.00
- volume_MA20: 39638755.00
- volume_ratio: 0.80

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.85
- MA20 / MA60 / MA200: 13.00 / 13.70 / 12.43
- gap20 / gap60: -1.16% / -6.23%
- 5D return: -3.16%
- 20D high/low: 13.84 / 12.50

### Relative Strength

- ratio: 0.045211
- ratio_MA60: 0.049939
- ratio_gap: -9.47%
- ratio_slope_proxy(20d): -0.000884

### Volume (if available)

- volume: 17074900.00
- volume_MA20: 13406005.00
- volume_ratio: 1.27

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

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-22 03:01:05**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DFII10 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VIXCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED NFCI failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 63.0 bp / latest 3.29
- IG OAS 4주 변화: 10.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.8
- VIX: 17.31
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -3.51% / slope_proxy: 0.007227
- GDXJ/GLD gap: -4.20% / slope_proxy: 0.010843

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 42.254116 | ATR14%: 5.19%
- MA20 gap: -4.82% | MA50 gap: -11.16% | MA200 gap: -12.47%
- vol_ratio(Volume/Vol20): 0.849666 | gap_open: 1.23%
- RS vs SILJ gap: 1.87% / slope_proxy: 0.001414
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
- close: 8.17 | RSI14: 42.625916 | ATR14%: 6.25%
- MA20 gap: -5.80% | MA50 gap: -10.25% | MA200 gap: -8.48%
- vol_ratio(Volume/Vol20): 0.585127 | gap_open: 0.85%
- SilverMarginGate: SI=56.724998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.51% / slope_proxy: 0.02289
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

## HYMC (Hycroft Mining)
- close: 17.129999 | RSI14: 38.555078 | ATR14%: 7.06%
- MA20 gap: -7.15% | MA50 gap: -20.70% | MA200 gap: -43.91%
- vol_ratio(Volume/Vol20): 0.6938 | gap_open: 1.65%
- RS vs SILJ gap: -11.09% / slope_proxy: -0.050672
- RS vs GDXJ gap: -14.80% / slope_proxy: -0.017348
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

- 실행시간(UTC): **2026-10-22 03:01:15**
- 데이터 기준일(주가): **2026-10-21**

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

- HY OAS: N/A
- IG OAS: N/A
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: N/A

### Leadership ratios

- GDX/GLD: gap -1.10% / slope_proxy -2.94%
- GDXJ/GLD: gap -4.20% / slope_proxy -6.39%
- SILJ/SLV: gap -3.51% / slope_proxy -3.04%
- Gold breadth proxy: above50 0.00%, above200 23.08%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.76 | RSI14: 39.69 | ATR14%: 3.96%
- MA20/50/200 gap: -4.46% / -10.71% / 9.05%
- 5D return: 2.46% | 20D drawdown: -12.75% | vol_ratio: 0.56
- RS vs GDXJ: gap -0.18% / slope_proxy -3.66%
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
- close: 6.29 | RSI14: 32.89 | ATR14%: 5.57%
- MA20/50/200 gap: -8.58% / -14.24% / -10.63%
- 5D return: -1.41% | 20D drawdown: -18.31% | vol_ratio: 0.41
- RS vs GDXJ: gap -3.71% / slope_proxy -8.71%
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
- close: 0.94 | RSI14: 35.71 | ATR14%: 7.60%
- MA20/50/200 gap: -9.09% / -28.99% / -35.42%
- 5D return: 0.00% | 20D drawdown: -27.69% | vol_ratio: 0.39
- RS vs GDXJ: gap -21.98% / slope_proxy -17.93%
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
- close: 1.93 | RSI14: 27.63 | ATR14%: 6.33%
- MA20/50/200 gap: -12.65% / -19.81% / -3.16%
- 5D return: -5.85% | 20D drawdown: -26.34% | vol_ratio: 0.93
- RS vs GDXJ: gap -9.79% / slope_proxy -17.67%
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
- close: 26.59 | RSI14: 47.84 | ATR14%: 4.47%
- MA20/50/200 gap: -0.70% / -2.95% / 29.43%
- 5D return: 4.60% | 20D drawdown: -6.60% | vol_ratio: 0.81
- RS vs SILJ: gap 12.23% / slope_proxy 8.22%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.17 | RSI14: 41.61 | ATR14%: 5.66%
- MA20/50/200 gap: -5.80% / -10.25% / -8.48%
- 5D return: 2.64% | 20D drawdown: -13.82% | vol_ratio: 0.59
- RS vs SILJ: gap 4.51% / slope_proxy 4.16%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **53.3**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.31 | RSI14: 44.59 | ATR14%: 4.34%
- MA20/50/200 gap: -2.64% / -14.56% / -15.75%
- 5D return: 6.13% | 20D drawdown: -11.50% | vol_ratio: 0.69
- RS vs SILJ: gap -1.29% / slope_proxy 3.17%
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
- close: 3.60 | RSI14: 25.61 | ATR14%: 5.99%
- MA20/50/200 gap: -14.18% / -25.05% / -37.81%
- 5D return: -2.70% | 20D drawdown: -25.47% | vol_ratio: 1.33
- RS vs SILJ: gap -13.88% / slope_proxy -12.52%
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
- close: 15.14 | RSI14: 32.65 | ATR14%: 4.74%
- MA20/50/200 gap: -8.19% / -17.58% / -20.12%
- 5D return: 1.61% | 20D drawdown: -16.77% | vol_ratio: 0.98
- RS vs SILJ: gap -4.23% / slope_proxy -4.03%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.36 | RSI14: 35.11 | ATR14%: 4.99%
- MA20/50/200 gap: -4.82% / -11.16% / -12.47%
- 5D return: 5.99% | 20D drawdown: -14.94% | vol_ratio: 0.85
- RS vs SILJ: gap 1.87% / slope_proxy -3.02%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **43.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.21 | RSI14: 41.85 | ATR14%: 5.05%
- MA20/50/200 gap: -4.22% / -18.32% / -24.91%
- 5D return: 6.76% | 20D drawdown: -12.29% | vol_ratio: 0.74
- RS vs SILJ: gap -6.79% / slope_proxy 0.25%
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
- close: 17.13 | RSI14: 38.33 | ATR14%: 6.14%
- MA20/50/200 gap: -7.15% / -20.70% / -43.91%
- 5D return: 4.80% | 20D drawdown: -20.25% | vol_ratio: 0.69
- RS vs SILJ: gap -11.09% / slope_proxy -6.75%
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
