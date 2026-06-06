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

- 실행시간(UTC): **2026-06-06 03:06:57**
- 데이터 기준일(일봉): **2026-06-05**
- 데이터 기준일(주봉): **2026-06-01**
- VXN 기준일: **2026-06-05** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 705.06
- Weekly RSI14: **65.53**
- 52W MA: 607.05 / gap: **16.14%**
- 104W MA gap: **28.60%**
- 52W MA 13W slope: **7.69%**
- VXN: **30.47** / 5D change: 7.89

## Daily trigger: 실제 매수 타이밍

- QQQ close: 705.06
- Daily RSI14: **48.34**
- 20D gap: **-2.35%**
- 50D gap: **5.58%**
- 200D gap: **13.56%**
- MACD hist: -3.2766 / change: -2.8115
- ATR14%: **1.69%**
- 20D high drawdown: **-5.51%**

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

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-06 03:00:37**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.74 / 4주 변화 -5.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.07 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.494

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.888199
- MA60: 9.056296
- gap: -1.86%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.46248
- MA60: 0.305282
- gap: 51.49%
- MA60_slope_proxy: 0.051241
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-06 03:01:19**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 114.09 bp / 4주 변화 -0.23 bp
- CURVE_10s5s: 44.67 bp / 4주 변화 -1.28 bp

## NWG Price
- close: 593.8
- MA50: 582.0291 / gap50: 2.02%
- MA200: 588.3817 / gap200: 0.92%

## Relative Strength
- RS vs FTSE gap: 2.39% / slope_proxy: -0.000272
- RS vs Peers gap: -2.32% / slope_proxy: -0.019338

## Why not today?
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-06 03:01:45**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DCOILBRENTEU failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DTWEXBGS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 90.25 / 5D 3.31%
- Brent ref (BZ=F): 92.87 / 5D 0.89%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.62
- Gas ref (NG=F): 3.22 / 5D -2.13%

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

- close: 56.93
- MA20 / MA60 / MA200: 57.78 / 58.74 / 48.52
- gap20 / gap60: -1.47% / -3.08%
- 5D return: 0.53%
- 20D high/low: 60.70 / 53.03

### Relative Strength

- ratio: 0.987168
- ratio_MA60: 1.008155
- ratio_gap: -2.08%
- ratio_slope_proxy(20d): 0.021587

### Volume (if available)

- volume: 7066612.00
- volume_MA20: 11129375.60
- volume_ratio: 0.63

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.75
- MA20 / MA60 / MA200: 19.34 / 20.02 / 15.11
- gap20 / gap60: -8.20% / -11.33%
- 5D return: -4.71%
- 20D high/low: 20.59 / 17.75

### Relative Strength

- ratio: 0.521905
- ratio_MA60: 0.526973
- ratio_gap: -0.96%
- ratio_slope_proxy(20d): 0.033975

### Volume (if available)

- volume: 13344633.00
- volume_MA20: 16341981.65
- volume_ratio: 0.82

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

- close: 5.95
- MA20 / MA60 / MA200: 6.60 / 6.51 / 4.92
- gap20 / gap60: -9.86% / -8.54%
- 5D return: -3.88%
- 20D high/low: 7.58 / 5.95

### Relative Strength

- ratio: 0.014348
- ratio_MA60: 0.015563
- ratio_gap: -7.81%
- ratio_slope_proxy(20d): -0.000358

### Volume (if available)

- volume: 22084207.00
- volume_MA20: 32358465.35
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

- close: 12.80
- MA20 / MA60 / MA200: 13.02 / 13.51 / 10.87
- gap20 / gap60: -1.66% / -5.23%
- 5D return: 6.31%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.053597
- ratio_MA60: 0.052230
- ratio_gap: 2.62%
- ratio_slope_proxy(20d): 0.003445

### Volume (if available)

- volume: 10100935.00
- volume_MA20: 17663666.75
- volume_ratio: 0.57

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

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-06 03:04:45**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -5.0 bp / latest 2.74
- IG OAS 4주 변화: -5.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.87% / slope_proxy: -0.011591
- GDXJ/GLD gap: -9.26% / slope_proxy: -0.006856

## VZLA (Vizsla Silver)
- close: 3.36 | RSI14: 42.834143 | ATR14%: 7.38%
- MA20 gap: -8.33% | MA50 gap: -3.25% | MA200 gap: -21.00%
- vol_ratio(Volume/Vol20): 1.495125 | gap_open: 3.65%
- RS vs SILJ gap: 11.52% / slope_proxy: 0.002883
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
- close: 6.4 | RSI14: 30.584585 | ATR14%: 9.86%
- MA20 gap: -24.00% | MA50 gap: -23.32% | MA200 gap: -23.81%
- vol_ratio(Volume/Vol20): 1.959519 | gap_open: 3.56%
- SilverMarginGate: SI=67.995003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -11.75% / slope_proxy: -0.009318
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
- close: 26.43 | RSI14: 31.458615 | ATR14%: 11.38%
- MA20 gap: -24.61% | MA50 gap: -27.70% | MA200 gap: 7.35%
- vol_ratio(Volume/Vol20): 1.534465 | gap_open: 5.67%
- RS vs SILJ gap: -16.41% / slope_proxy: -0.017645
- RS vs GDXJ gap: -13.60% / slope_proxy: -0.001463
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-06-06 03:06:36**
- 데이터 기준일(주가): **2026-06-05**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA**

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

- HY OAS: 2.74 / 4주 변화 -0.07 bp-ish / 2026-06-04
- IG OAS: 0.74 / 4주 변화 -0.05 bp-ish / 2026-06-04
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: N/A

### Leadership ratios

- GDX/GLD: gap -6.42% / slope_proxy -8.76%
- GDXJ/GLD: gap -9.26% / slope_proxy -12.49%
- SILJ/SLV: gap -2.87% / slope_proxy -1.55%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 23.08%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.35 | RSI14: 40.93 | ATR14%: 7.80%
- MA20/50/200 gap: -11.19% / -3.92% / 14.59%
- 5D return: -15.52% | 20D drawdown: -15.52% | vol_ratio: 2.29
- RS vs GDXJ: gap 16.98% / slope_proxy 13.24%
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
- close: 1.20 | RSI14: 32.26 | ATR14%: 6.34%
- MA20/50/200 gap: -13.67% / -14.47% / -18.14%
- 5D return: -13.67% | 20D drawdown: -22.08% | vol_ratio: 4.63
- RS vs GDXJ: gap 1.50% / slope_proxy 3.58%
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
- close: 5.70 | RSI14: 37.09 | ATR14%: 7.37%
- MA20/50/200 gap: -13.48% / -16.40% / -17.30%
- 5D return: -18.34% | 20D drawdown: -22.55% | vol_ratio: 1.61
- RS vs GDXJ: gap -2.21% / slope_proxy 2.92%
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
- close: 1.71 | RSI14: 25.56 | ATR14%: 9.40%
- MA20/50/200 gap: -16.44% / -8.69% / 6.56%
- 5D return: -11.40% | 20D drawdown: -31.33% | vol_ratio: 0.97
- RS vs GDXJ: gap 11.38% / slope_proxy 16.92%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **44.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 17.14 | RSI14: 41.82 | ATR14%: 8.31%
- MA20/50/200 gap: -11.03% / -3.62% / 16.34%
- 5D return: -18.38% | 20D drawdown: -20.24% | vol_ratio: 1.07
- RS vs SILJ: gap 14.46% / slope_proxy 6.80%
- FundamentalScore: 86 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **64.0**
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
- close: 3.36 | RSI14: 46.70 | ATR14%: 7.29%
- MA20/50/200 gap: -8.33% / -3.25% / -21.00%
- 5D return: -13.40% | 20D drawdown: -18.64% | vol_ratio: 1.50
- RS vs SILJ: gap 11.52% / slope_proxy 13.68%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **57.6**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.00 | RSI14: 31.49 | ATR14%: 7.42%
- MA20/50/200 gap: -18.28% / -16.55% / -14.16%
- 5D return: -19.76% | 20D drawdown: -30.19% | vol_ratio: 1.72
- RS vs SILJ: gap -3.90% / slope_proxy -3.93%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.78 | RSI14: 33.06 | ATR14%: 6.51%
- MA20/50/200 gap: -17.10% / -19.14% / -15.13%
- 5D return: -16.83% | 20D drawdown: -29.79% | vol_ratio: 1.67
- RS vs SILJ: gap -7.54% / slope_proxy -4.34%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **51.6**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.40 | RSI14: 21.39 | ATR14%: 8.65%
- MA20/50/200 gap: -24.00% / -23.32% / -23.81%
- 5D return: -21.47% | 20D drawdown: -36.95% | vol_ratio: 1.96
- RS vs SILJ: gap -11.75% / slope_proxy -14.63%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.92 | RSI14: 28.20 | ATR14%: 8.96%
- MA20/50/200 gap: -20.39% / -17.30% / -9.95%
- 5D return: -20.13% | 20D drawdown: -33.60% | vol_ratio: 1.10
- RS vs SILJ: gap -6.51% / slope_proxy -10.62%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.84 | RSI14: 34.45 | ATR14%: 7.98%
- MA20/50/200 gap: -16.95% / -14.82% / -8.78%
- 5D return: -20.22% | 20D drawdown: -26.73% | vol_ratio: 1.33
- RS vs SILJ: gap -0.81% / slope_proxy 1.94%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **43.5**
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
- close: 26.43 | RSI14: 22.40 | ATR14%: 9.29%
- MA20/50/200 gap: -24.61% / -27.70% / 7.35%
- 5D return: -20.03% | 20D drawdown: -41.47% | vol_ratio: 1.53
- RS vs SILJ: gap -16.41% / slope_proxy -17.18%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **35.4**
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
