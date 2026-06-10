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

- 실행시간(UTC): **2026-06-10 03:08:01**
- 데이터 기준일(일봉): **2026-06-09**
- 데이터 기준일(주봉): **2026-06-08**
- VXN 기준일: **2026-06-09** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 707.83
- Weekly RSI14: **66.00**
- 52W MA: 610.58 / gap: **15.93%**
- 104W MA gap: **28.58%**
- 52W MA 13W slope: **7.88%**
- VXN: **29.78** / 5D change: 6.51

## Daily trigger: 실제 매수 타이밍

- QQQ close: 707.83
- Daily RSI14: **49.54**
- 20D gap: **-1.96%**
- 50D gap: **5.09%**
- 200D gap: **13.74%**
- MACD hist: -5.5047 / change: -1.1514
- ATR14%: **2.01%**
- 20D high drawdown: **-5.14%**

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

- 데이터 기준일(주가): **2026-06-09**
- 실행시간(UTC): **2026-06-10 03:00:42**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 -4.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -3.0 bp
- 10Y Real Yield (DFII10): 2.07 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.494

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.626936
- MA60: 9.077758
- gap: -4.97%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.451566
- MA60: 0.313315
- gap: 44.13%
- MA60_slope_proxy: 0.055804
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-09**
- 실행시간(UTC): **2026-06-10 03:01:44**

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
- TERM_SPREAD_10Y_POLICY: 112.73 bp / 4주 변화 0.78 bp
- CURVE_10s5s: 44.64 bp / 4주 변화 0.2 bp

## NWG Price
- close: 593.0
- MA50: 584.3371 / gap50: 1.48%
- MA200: 588.7619 / gap200: 0.72%

## Relative Strength
- RS vs FTSE gap: 3.24% / slope_proxy: -0.000225
- RS vs Peers gap: 0.86% / slope_proxy: -0.019819

## Why not today?
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-10 03:02:31**

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

- WTI ref (CL=F): 88.99 / 5D -5.09%
- Brent ref (BZ=F): 92.30 / 5D -3.85%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.31
- Gas ref (NG=F): 3.13 / 5D -1.07%

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

- close: 56.55
- MA20 / MA60 / MA200: 58.07 / 58.70 / 48.65
- gap20 / gap60: -2.62% / -3.67%
- 5D return: -4.30%
- 20D high/low: 60.70 / 56.18

### Relative Strength

- ratio: 0.985363
- ratio_MA60: 1.007136
- ratio_gap: -2.16%
- ratio_slope_proxy(20d): 0.017041

### Volume (if available)

- volume: 11106949.00
- volume_MA20: 10842197.45
- volume_ratio: 1.02

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.82
- MA20 / MA60 / MA200: 19.08 / 19.99 / 15.17
- gap20 / gap60: -6.59% / -10.87%
- 5D return: -4.07%
- 20D high/low: 20.54 / 17.75

### Relative Strength

- ratio: 0.525354
- ratio_MA60: 0.527271
- ratio_gap: -0.36%
- ratio_slope_proxy(20d): 0.029962

### Volume (if available)

- volume: 15254240.00
- volume_MA20: 15953247.00
- volume_ratio: 0.96

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

- close: 5.87
- MA20 / MA60 / MA200: 6.55 / 6.50 / 4.95
- gap20 / gap60: -10.45% / -9.63%
- 5D return: -6.08%
- 20D high/low: 7.58 / 5.87

### Relative Strength

- ratio: 0.013951
- ratio_MA60: 0.015468
- ratio_gap: -9.81%
- ratio_slope_proxy(20d): -0.000429

### Volume (if available)

- volume: 24117279.00
- volume_MA20: 31451203.95
- volume_ratio: 0.77

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

- close: 12.47
- MA20 / MA60 / MA200: 13.13 / 13.50 / 10.87
- gap20 / gap60: -5.01% / -7.62%
- 5D return: 0.81%
- 20D high/low: 14.78 / 12.04

### Relative Strength

- ratio: 0.052089
- ratio_MA60: 0.052297
- ratio_gap: -0.40%
- ratio_slope_proxy(20d): 0.003366

### Volume (if available)

- volume: 11089767.00
- volume_MA20: 16828528.35
- volume_ratio: 0.66

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

- 데이터 기준일(주가): **2026-06-09**
- 실행시간(UTC): **2026-06-10 03:05:32**

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
- HY OAS 4주 변화: -4.0 bp / latest 2.75
- IG OAS 4주 변화: -3.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -1.25% / slope_proxy: -0.010618
- GDXJ/GLD gap: -8.73% / slope_proxy: -0.007539

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 42.596001 | ATR14%: 7.47%
- MA20 gap: -8.50% | MA50 gap: -4.42% | MA200 gap: -21.70%
- vol_ratio(Volume/Vol20): 1.057428 | gap_open: 0.58%
- RS vs SILJ gap: 12.96% / slope_proxy: 0.003398
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
- close: 6.1 | RSI14: 28.613273 | ATR14%: 10.08%
- MA20 gap: -24.88% | MA50 gap: -26.46% | MA200 gap: -27.58%
- vol_ratio(Volume/Vol20): 1.076305 | gap_open: 0.16%
- SilverMarginGate: SI=63.849998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.06% / slope_proxy: -0.009953
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
- close: 24.85 | RSI14: 29.193536 | ATR14%: 11.75%
- MA20 gap: -25.84% | MA50 gap: -31.53% | MA200 gap: 0.05%
- vol_ratio(Volume/Vol20): 1.234009 | gap_open: 2.05%
- RS vs SILJ gap: -18.82% / slope_proxy: -0.032494
- RS vs GDXJ gap: -17.45% / slope_proxy: -0.005359
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

- 실행시간(UTC): **2026-06-10 03:07:39**
- 데이터 기준일(주가): **2026-06-09**

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

- HY OAS: 2.75 / 4주 변화 -0.07 bp-ish / 2026-06-08
- IG OAS: N/A
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: N/A

### Leadership ratios

- GDX/GLD: gap -6.49% / slope_proxy -11.51%
- GDXJ/GLD: gap -8.73% / slope_proxy -15.09%
- SILJ/SLV: gap -1.25% / slope_proxy 0.01%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 15.38%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.21 | RSI14: 41.08 | ATR14%: 7.66%
- MA20/50/200 gap: -11.92% / -6.35% / 11.88%
- 5D return: -15.67% | 20D drawdown: -17.13% | vol_ratio: 1.39
- RS vs GDXJ: gap 14.88% / slope_proxy 14.44%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.45 | RSI14: 39.73 | ATR14%: 7.61%
- MA20/50/200 gap: -15.23% / -19.58% / -21.06%
- 5D return: -20.32% | 20D drawdown: -25.95% | vol_ratio: 1.03
- RS vs GDXJ: gap -4.92% / slope_proxy -2.74%
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
- close: 1.62 | RSI14: 27.87 | ATR14%: 9.66%
- MA20/50/200 gap: -19.88% / -13.81% / 0.26%
- 5D return: -17.77% | 20D drawdown: -34.94% | vol_ratio: 0.45
- RS vs GDXJ: gap 6.34% / slope_proxy 10.35%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.17 | RSI14: 33.33 | ATR14%: 6.38%
- MA20/50/200 gap: -13.94% / -16.31% / -20.49%
- 5D return: -15.22% | 20D drawdown: -24.03% | vol_ratio: 0.82
- RS vs GDXJ: gap 0.14% / slope_proxy -1.16%
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
- close: 16.68 | RSI14: 50.71 | ATR14%: 8.15%
- MA20/50/200 gap: -12.28% / -7.09% / 12.56%
- 5D return: -22.38% | 20D drawdown: -22.38% | vol_ratio: 0.68
- RS vs SILJ: gap 13.34% / slope_proxy 4.82%
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
- close: 3.33 | RSI14: 51.69 | ATR14%: 7.55%
- MA20/50/200 gap: -8.50% / -4.42% / -21.70%
- 5D return: -19.37% | 20D drawdown: -19.37% | vol_ratio: 1.06
- RS vs SILJ: gap 12.96% / slope_proxy 15.12%
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
- close: 7.83 | RSI14: 36.41 | ATR14%: 7.24%
- MA20/50/200 gap: -17.71% / -18.05% / -16.20%
- 5D return: -20.51% | 20D drawdown: -31.68% | vol_ratio: 1.22
- RS vs SILJ: gap -3.30% / slope_proxy -9.06%
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
- close: 14.51 | RSI14: 37.91 | ATR14%: 6.51%
- MA20/50/200 gap: -16.29% / -20.11% / -17.02%
- 5D return: -18.48% | 20D drawdown: -31.07% | vol_ratio: 1.27
- RS vs SILJ: gap -6.54% / slope_proxy -6.11%
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
- close: 6.10 | RSI14: 22.34 | ATR14%: 9.03%
- MA20/50/200 gap: -24.88% / -26.46% / -27.58%
- 5D return: -26.77% | 20D drawdown: -39.90% | vol_ratio: 1.08
- RS vs SILJ: gap -13.06% / slope_proxy -20.01%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.77 | RSI14: 40.83 | ATR14%: 7.89%
- MA20/50/200 gap: -16.35% / -15.87% / -10.16%
- 5D return: -22.24% | 20D drawdown: -27.60% | vol_ratio: 1.21
- RS vs SILJ: gap 0.52% / slope_proxy -3.64%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.72 | RSI14: 32.97 | ATR14%: 8.89%
- MA20/50/200 gap: -21.02% / -20.36% / -14.03%
- 5D return: -26.59% | 20D drawdown: -36.30% | vol_ratio: 0.96
- RS vs SILJ: gap -7.14% / slope_proxy -15.22%
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
- close: 24.85 | RSI14: 24.33 | ATR14%: 9.51%
- MA20/50/200 gap: -25.84% / -31.53% / 0.05%
- 5D return: -26.52% | 20D drawdown: -44.97% | vol_ratio: 1.23
- RS vs SILJ: gap -18.82% / slope_proxy -26.76%
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
