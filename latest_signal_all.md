# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-16 03:08:08**
- 데이터 기준일(일봉): **2026-06-15**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-15** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 744.00
- Weekly RSI14: **71.31**
- 52W MA: 615.07 / gap: **20.96%**
- 104W MA gap: **34.49%**
- 52W MA 13W slope: **8.29%**
- VXN: **25.92** / 5D change: -1.20

## Daily trigger: 실제 매수 타이밍

- QQQ close: 744.00
- Daily RSI14: **62.55**
- 20D gap: **2.87%**
- 50D gap: **8.62%**
- 200D gap: **18.98%**
- MACD hist: -3.1021 / change: 2.1905
- ATR14%: **2.11%**
- 20D high drawdown: **-0.29%**

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

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-16 03:00:41**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -9.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -1.0 bp
- 10Y Real Yield (DFII10): 2.16 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.506

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.228698
- MA60: 9.118614
- gap: 1.21%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.47733
- MA60: 0.328672
- gap: 45.23%
- MA60_slope_proxy: 0.063403
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-12**
- 실행시간(UTC): **2026-06-16 03:02:25**

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
- TERM_SPREAD_10Y_POLICY: 113.04 bp / 4주 변화 -8.57 bp
- CURVE_10s5s: 44.66 bp / 4주 변화 -0.68 bp

## NWG Price
- close: 614.2
- MA50: 587.6931 / gap50: 4.51%
- MA200: 589.3782 / gap200: 4.21%

## Relative Strength
- RS vs FTSE gap: 4.58% / slope_proxy: 3.9e-05
- RS vs Peers gap: -0.06% / slope_proxy: -0.020075

## Why not today?
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-16 03:03:13**

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

- WTI ref (CL=F): 80.76 / 5D -11.54%
- Brent ref (BZ=F): 83.03 / 5D -11.90%
- Brent Tier: **80-90**
- Brent-WTI spread: 2.27
- Gas ref (NG=F): 3.15 / 5D 0.10%

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

- close: 54.46
- MA20 / MA60 / MA200: 57.59 / 58.30 / 48.64
- gap20 / gap60: -5.43% / -6.58%
- 5D return: -4.82%
- 20D high/low: 60.42 / 54.46

### Relative Strength

- ratio: 0.980378
- ratio_MA60: 1.001311
- ratio_gap: -2.09%
- ratio_slope_proxy(20d): 0.008606

### Volume (if available)

- volume: 10583650.00
- volume_MA20: 10799242.50
- volume_ratio: 0.98

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.34
- MA20 / MA60 / MA200: 18.72 / 19.91 / 15.29
- gap20 / gap60: -7.37% / -12.90%
- 5D return: -2.31%
- 20D high/low: 20.54 / 17.34

### Relative Strength

- ratio: 0.500577
- ratio_MA60: 0.531701
- ratio_gap: -5.85%
- ratio_slope_proxy(20d): 0.020415

### Volume (if available)

- volume: 20987067.00
- volume_MA20: 15703648.35
- volume_ratio: 1.34

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

- close: 5.83
- MA20 / MA60 / MA200: 6.39 / 6.47 / 5.01
- gap20 / gap60: -8.83% / -9.88%
- 5D return: -5.51%
- 20D high/low: 7.58 / 5.83

### Relative Strength

- ratio: 0.014037
- ratio_MA60: 0.015302
- ratio_gap: -8.27%
- ratio_slope_proxy(20d): -0.000525

### Volume (if available)

- volume: 29982929.00
- volume_MA20: 30820891.45
- volume_ratio: 0.97

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

- close: 11.70
- MA20 / MA60 / MA200: 12.98 / 13.42 / 10.85
- gap20 / gap60: -9.84% / -12.82%
- 5D return: -8.75%
- 20D high/low: 14.76 / 11.70

### Relative Strength

- ratio: 0.049734
- ratio_MA60: 0.052303
- ratio_gap: -4.91%
- ratio_slope_proxy(20d): 0.002566

### Volume (if available)

- volume: 23985316.00
- volume_MA20: 14409410.80
- volume_ratio: 1.66

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

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-16 03:05:59**

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
- HY OAS 4주 변화: -9.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 3.91% / slope_proxy: -0.006662
- GDXJ/GLD gap: 1.08% / slope_proxy: -0.007378

## VZLA (Vizsla Silver)
- close: 3.65 | RSI14: 52.170709 | ATR14%: 6.79%
- MA20 gap: 1.76% | MA50 gap: 4.23% | MA200 gap: -14.17%
- vol_ratio(Volume/Vol20): 1.002904 | gap_open: 7.80%
- RS vs SILJ gap: 8.29% / slope_proxy: 0.004346
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 7.55 | RSI14: 48.905954 | ATR14%: 8.25%
- MA20 gap: -0.06% | MA50 gap: -7.90% | MA200 gap: -10.78%
- vol_ratio(Volume/Vol20): 0.923727 | gap_open: 9.60%
- SilverMarginGate: SI=69.574997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.59% / slope_proxy: -0.011652
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
- close: 27.84 | RSI14: 41.595139 | ATR14%: 10.20%
- MA20 gap: -8.36% | MA50 gap: -21.78% | MA200 gap: 10.20%
- vol_ratio(Volume/Vol20): 1.387253 | gap_open: 11.30%
- RS vs SILJ gap: -18.50% / slope_proxy: -0.058702
- RS vs GDXJ gap: -16.57% / slope_proxy: -0.012567
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

- 실행시간(UTC): **2026-06-16 03:07:46**
- 데이터 기준일(주가): **2026-06-15**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 -0.12 bp-ish / 2026-06-12
- IG OAS: 0.74 / 4주 변화 -0.01 bp-ish / 2026-06-12
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: -0.51 / 4주 변화 0.06 / 2026-06-05

### Leadership ratios

- GDX/GLD: gap 1.13% / slope_proxy 3.25%
- GDXJ/GLD: gap 1.08% / slope_proxy 2.24%
- SILJ/SLV: gap 3.91% / slope_proxy 8.44%
- Gold breadth proxy: above50 7.69%, above200 23.08%, count 13
- Silver breadth proxy: above50 15.38%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.94 | RSI14: 41.10 | ATR14%: 6.65%
- MA20/50/200 gap: -1.23% / 1.93% / 22.07%
- 5D return: 7.30% | 20D drawdown: -8.74% | vol_ratio: 0.63
- RS vs GDXJ: gap 10.47% / slope_proxy -3.82%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 55 | OverallScore: **71.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs GDXJ)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.37 | RSI14: 49.23 | ATR14%: 5.68%
- MA20/50/200 gap: 4.50% / -0.81% / -7.55%
- 5D return: 12.30% | 20D drawdown: -2.84% | vol_ratio: 0.49
- RS vs GDXJ: gap 4.04% / slope_proxy 0.35%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **56.5**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.93 | RSI14: 44.15 | ATR14%: 7.24%
- MA20/50/200 gap: -2.91% / -10.95% / -14.34%
- 5D return: 3.49% | 20D drawdown: -15.89% | vol_ratio: 0.78
- RS vs GDXJ: gap -7.10% / slope_proxy -8.35%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.69 | RSI14: 40.74 | ATR14%: 7.40%
- MA20/50/200 gap: -9.60% / -9.91% / 3.22%
- 5D return: 1.20% | 20D drawdown: -24.89% | vol_ratio: 0.64
- RS vs GDXJ: gap -2.09% / slope_proxy -25.52%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **41.0**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 20.65 | RSI14: 56.75 | ATR14%: 7.13%
- MA20/50/200 gap: 11.62% / 13.56% / 37.67%
- 5D return: 17.93% | 20D drawdown: -3.91% | vol_ratio: 0.98
- RS vs SILJ: gap 21.07% / slope_proxy 13.42%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.76 | RSI14: 48.65 | ATR14%: 7.85%
- MA20/50/200 gap: 2.80% / -2.68% / 3.90%
- 5D return: 16.13% | 20D drawdown: -10.42% | vol_ratio: 1.05
- RS vs SILJ: gap 1.14% / slope_proxy 0.74%
- FundamentalScore: 68 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **60.9**
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
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.83 | RSI14: 49.24 | ATR14%: 7.54%
- MA20/50/200 gap: 3.45% / -0.25% / 5.71%
- 5D return: 14.21% | 20D drawdown: -7.95% | vol_ratio: 1.22
- RS vs SILJ: gap 4.52% / slope_proxy 0.00%
- FundamentalScore: 60 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **57.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.65 | RSI14: 48.37 | ATR14%: 7.18%
- MA20/50/200 gap: 1.76% / 4.23% / -14.17%
- 5D return: 6.10% | 20D drawdown: -11.62% | vol_ratio: 1.00
- RS vs SILJ: gap 8.29% / slope_proxy 8.45%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **62.6**
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
- close: 9.11 | RSI14: 45.62 | ATR14%: 7.01%
- MA20/50/200 gap: 1.12% / -3.87% / -3.02%
- 5D return: 13.31% | 20D drawdown: -8.63% | vol_ratio: 1.08
- RS vs SILJ: gap -0.49% / slope_proxy -2.45%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.66 | RSI14: 44.81 | ATR14%: 6.12%
- MA20/50/200 gap: 1.29% / -6.92% / -5.51%
- 5D return: 11.89% | 20D drawdown: -6.40% | vol_ratio: 1.72
- RS vs SILJ: gap -4.69% / slope_proxy -1.92%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.55 | RSI14: 44.92 | ATR14%: 8.09%
- MA20/50/200 gap: -0.06% / -7.90% / -10.78%
- 5D return: 19.09% | 20D drawdown: -11.80% | vol_ratio: 0.92
- RS vs SILJ: gap -4.59% / slope_proxy -10.38%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 27.84 | RSI14: 36.16 | ATR14%: 9.34%
- MA20/50/200 gap: -8.36% / -21.78% / 10.20%
- 5D return: 5.73% | 20D drawdown: -20.07% | vol_ratio: 1.39
- RS vs SILJ: gap -18.50% / slope_proxy -18.78%
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
