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

- 실행시간(UTC): **2026-06-05 15:07:30**
- 데이터 기준일(일봉): **2026-06-05**
- 데이터 기준일(주봉): **2026-06-01**
- VXN 기준일: **2026-06-05** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 723.77
- Weekly RSI14: **71.70**
- 52W MA: 607.41 / gap: **19.16%**
- 104W MA gap: **31.97%**
- 52W MA 13W slope: **7.75%**
- VXN: **24.91** / 5D change: 2.33

## Daily trigger: 실제 매수 타이밍

- QQQ close: 723.81
- Daily RSI14: **59.00**
- 20D gap: **0.12%**
- 50D gap: **8.32%**
- 200D gap: **16.57%**
- MACD hist: -2.0801 / change: -1.6149
- ATR14%: **1.46%**
- 20D high drawdown: **-3.00%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-05 15:00:44**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.74 / 4주 변화 -5.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.07 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.111364
- MA60: 9.060016
- gap: 0.57%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.491451
- MA60: 0.305765
- gap: 60.73%
- MA60_slope_proxy: 0.051724
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-05**
- 실행시간(UTC): **2026-06-05 15:01:46**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- close: 597.0
- MA50: 582.0931 / gap50: 2.56%
- MA200: 588.3977 / gap200: 1.46%

## Relative Strength
- RS vs FTSE gap: 2.67% / slope_proxy: -0.000269
- RS vs Peers gap: -2.21% / slope_proxy: -0.019321

## Why not today?
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-05 15:02:32**

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

- WTI ref (CL=F): 91.28 / 5D 4.49%
- Brent ref (BZ=F): 93.91 / 5D 2.02%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.63
- Gas ref (NG=F): 3.25 / 5D -1.22%

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

- close: 58.10
- MA20 / MA60 / MA200: 57.84 / 58.76 / 48.53
- gap20 / gap60: 0.46% / -1.13%
- 5D return: 2.60%
- 20D high/low: 60.70 / 53.03

### Relative Strength

- ratio: 0.992569
- ratio_MA60: 1.008245
- ratio_gap: -1.55%
- ratio_slope_proxy(20d): 0.021677

### Volume (if available)

- volume: 1609621.00
- volume_MA20: 10856526.05
- volume_ratio: 0.15

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.94
- MA20 / MA60 / MA200: 19.35 / 20.02 / 15.11
- gap20 / gap60: -7.26% / -10.39%
- 5D return: -3.68%
- 20D high/low: 20.59 / 17.94

### Relative Strength

- ratio: 0.521238
- ratio_MA60: 0.526962
- ratio_gap: -1.09%
- ratio_slope_proxy(20d): 0.033964

### Volume (if available)

- volume: 2949817.00
- volume_MA20: 15822240.85
- volume_ratio: 0.19

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

- close: 6.08
- MA20 / MA60 / MA200: 6.61 / 6.51 / 4.92
- gap20 / gap60: -8.04% / -6.64%
- 5D return: -1.85%
- 20D high/low: 7.58 / 6.08

### Relative Strength

- ratio: 0.014181
- ratio_MA60: 0.015560
- ratio_gap: -8.86%
- ratio_slope_proxy(20d): -0.000361

### Volume (if available)

- volume: 6935115.00
- volume_MA20: 31601010.75
- volume_ratio: 0.22

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

- close: 13.04
- MA20 / MA60 / MA200: 13.03 / 13.51 / 10.87
- gap20 / gap60: 0.13% / -3.45%
- 5D return: 8.35%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.054194
- ratio_MA60: 0.052240
- ratio_gap: 3.74%
- ratio_slope_proxy(20d): 0.003455

### Volume (if available)

- volume: 2527129.00
- volume_MA20: 17284976.45
- volume_ratio: 0.15

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
- 실행시간(UTC): **2026-06-05 15:05:16**

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
- SILJ/SLV gap: -1.22% / slope_proxy: -0.011468
- GDXJ/GLD gap: -7.53% / slope_proxy: -0.006774

## VZLA (Vizsla Silver)
- close: 3.545 | RSI14: 47.079548 | ATR14%: 6.76%
- MA20 gap: -3.53% | MA50 gap: 1.97% | MA200 gap: -16.66%
- vol_ratio(Volume/Vol20): 0.676802 | gap_open: 3.65%
- RS vs SILJ gap: 13.51% / slope_proxy: 0.002921
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
- close: 6.77 | RSI14: 33.040383 | ATR14%: 8.91%
- MA20 gap: -19.79% | MA50 gap: -18.96% | MA200 gap: -19.42%
- vol_ratio(Volume/Vol20): 0.742969 | gap_open: 3.56%
- SilverMarginGate: SI=69.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -9.94% / slope_proxy: -0.009234
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
- close: 27.51 | RSI14: 32.973306 | ATR14%: 10.79%
- MA20 gap: -21.65% | MA50 gap: -24.79% | MA200 gap: 11.72%
- vol_ratio(Volume/Vol20): 0.598151 | gap_open: 5.67%
- RS vs SILJ gap: -16.04% / slope_proxy: -0.01757
- RS vs GDXJ gap: -12.82% / slope_proxy: -0.001423
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

- 실행시간(UTC): **2026-06-05 15:07:09**
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

- GDX/GLD: gap -4.92% / slope_proxy -7.27%
- GDXJ/GLD: gap -7.53% / slope_proxy -10.80%
- SILJ/SLV: gap -1.22% / slope_proxy 0.15%
- Gold breadth proxy: above50 0.00%, above200 15.38%, count 13
- Silver breadth proxy: above50 15.38%, above200 38.46%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.51 | RSI14: 42.36 | ATR14%: 7.56%
- MA20/50/200 gap: -9.34% / -1.87% / 17.07%
- 5D return: -13.68% | 20D drawdown: -13.68% | vol_ratio: 0.79
- RS vs GDXJ: gap 15.91% / slope_proxy 12.18%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **59.6**
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.90 | RSI14: 39.05 | ATR14%: 6.89%
- MA20/50/200 gap: -10.58% / -13.52% / -14.41%
- 5D return: -15.47% | 20D drawdown: -19.84% | vol_ratio: 0.56
- RS vs GDXJ: gap -1.86% / slope_proxy 3.29%
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
- close: 1.21 | RSI14: 32.79 | ATR14%: 6.29%
- MA20/50/200 gap: -12.98% / -13.77% / -17.47%
- 5D return: -12.95% | 20D drawdown: -21.43% | vol_ratio: 2.24
- RS vs GDXJ: gap -0.73% / slope_proxy 1.26%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.0**
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
- close: 1.79 | RSI14: 27.20 | ATR14%: 8.66%
- MA20/50/200 gap: -12.70% / -4.50% / 11.52%
- 5D return: -7.25% | 20D drawdown: -28.11% | vol_ratio: 0.23
- RS vs GDXJ: gap 13.01% / slope_proxy 18.66%
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
- close: 17.95 | RSI14: 44.65 | ATR14%: 7.68%
- MA20/50/200 gap: -7.02% / 0.84% / 21.80%
- 5D return: -14.52% | 20D drawdown: -16.47% | vol_ratio: 0.39
- RS vs SILJ: gap 15.65% / slope_proxy 7.94%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **74.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.55 | RSI14: 51.16 | ATR14%: 6.68%
- MA20/50/200 gap: -3.53% / 1.97% / -16.66%
- 5D return: -8.63% | 20D drawdown: -14.16% | vol_ratio: 0.68
- RS vs SILJ: gap 13.51% / slope_proxy 15.75%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.35 | RSI14: 33.90 | ATR14%: 6.87%
- MA20/50/200 gap: -14.89% / -12.99% / -10.45%
- 5D return: -16.28% | 20D drawdown: -27.17% | vol_ratio: 0.79
- RS vs SILJ: gap -3.25% / slope_proxy -3.27%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.15 | RSI14: 37.21 | ATR14%: 7.32%
- MA20/50/200 gap: -12.73% / -10.38% / -3.96%
- 5D return: -15.98% | 20D drawdown: -22.84% | vol_ratio: 0.50
- RS vs SILJ: gap 0.77% / slope_proxy 3.60%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **47.0**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.19 | RSI14: 34.77 | ATR14%: 6.08%
- MA20/50/200 gap: -14.87% / -16.90% / -12.76%
- 5D return: -14.49% | 20D drawdown: -27.81% | vol_ratio: 0.50
- RS vs SILJ: gap -8.25% / slope_proxy -5.09%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.77 | RSI14: 23.56 | ATR14%: 7.77%
- MA20/50/200 gap: -19.79% / -18.96% / -19.42%
- 5D return: -16.93% | 20D drawdown: -33.30% | vol_ratio: 0.74
- RS vs SILJ: gap -9.94% / slope_proxy -12.85%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **44.6**
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
- close: 5.20 | RSI14: 30.99 | ATR14%: 8.07%
- MA20/50/200 gap: -16.13% / -12.76% / -4.95%
- 5D return: -15.67% | 20D drawdown: -29.89% | vol_ratio: 0.48
- RS vs SILJ: gap -4.77% / slope_proxy -8.92%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **41.9**
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 27.51 | RSI14: 23.87 | ATR14%: 8.78%
- MA20/50/200 gap: -21.65% / -24.79% / 11.72%
- 5D return: -16.76% | 20D drawdown: -39.08% | vol_ratio: 0.60
- RS vs SILJ: gap -16.04% / slope_proxy -16.81%
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
