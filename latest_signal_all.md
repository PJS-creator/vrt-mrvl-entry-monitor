# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-02 03:00:41**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.28 / 4주 변화 20.0 bp
- IG OAS (BAMLC0A0CM): 0.9 / 4주 변화 6.0 bp
- 10Y Real Yield (DFII10): 2.04 / 4주 변화 28.0 bp
- VIX (VIXCLS): 25.25
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.239199
- MA60: 7.108326
- gap: 15.91%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.27224
- MA60: 0.212035
- gap: 28.39%
- MA60_slope_proxy: -0.002049
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-02 03:02:23**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 113.06 bp / 4주 변화 51.26 bp
- CURVE_10s5s: 41.81 bp / 4주 변화 -18.23 bp

## NWG Price
- close: 583.2
- MA50: 602.476 / gap50: -3.20%
- MA200: 571.8369 / gap200: 1.99%

## Relative Strength
- RS vs FTSE gap: -4.68% / slope_proxy: -0.003344
- RS vs Peers gap: -3.76% / slope_proxy: -0.045263

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-02 03:03:49**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DCOILBRENTEU failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DTWEXBGS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 103.85 / 5D 14.98%
- Brent ref (BZ=F): 105.90 / 5D 3.60%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.05
- Gas ref (NG=F): 2.86 / 5D -2.98%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 62.23
- MA20 / MA60 / MA200: 59.34 / 50.61 / 45.24
- gap20 / gap60: 4.86% / 22.95%
- 5D return: 0.61%
- 20D high/low: 66.24 / 52.99

### Relative Strength

- ratio: 1.055282
- ratio_MA60: 0.939084
- ratio_gap: 12.37%
- ratio_slope_proxy(20d): 0.033440

### Volume (if available)

- volume: 26011124.00
- volume_MA20: 22735361.20
- volume_ratio: 1.14

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.08
- MA20 / MA60 / MA200: 19.28 / 16.20 / 13.48
- gap20 / gap60: 4.14% / 23.93%
- 5D return: 1.31%
- 20D high/low: 20.81 / 16.73

### Relative Strength

- ratio: 0.523326
- ratio_MA60: 0.440394
- ratio_gap: 18.83%
- ratio_slope_proxy(20d): 0.049251

### Volume (if available)

- volume: 58012092.00
- volume_MA20: 40585684.60
- volume_ratio: 1.43

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

- close: 6.50
- MA20 / MA60 / MA200: 6.43 / 5.69 / 4.10
- gap20 / gap60: 1.16% / 14.19%
- 5D return: -3.99%
- 20D high/low: 6.93 / 5.93

### Relative Strength

- ratio: 0.016408
- ratio_MA60: 0.015356
- ratio_gap: 6.85%
- ratio_slope_proxy(20d): 0.000733

### Volume (if available)

- volume: 40973003.00
- volume_MA20: 37860630.15
- volume_ratio: 1.08

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.68
- MA20 / MA60 / MA200: 14.34 / 10.90 / 11.38
- gap20 / gap60: 2.35% / 34.63%
- 5D return: -12.15%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.053219
- ratio_MA60: 0.046204
- ratio_gap: 15.18%
- ratio_slope_proxy(20d): 0.006314

### Volume (if available)

- volume: 36753051.00
- volume_MA20: 37369792.55
- volume_ratio: 0.98

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-01**
- 실행시간(UTC): **2026-04-02 03:07:13**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.28
- IG OAS 4주 변화: 6.0 bp / latest 0.9
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.04
- VIX: 25.25
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 2.90% / slope_proxy: -0.003757
- GDXJ/GLD gap: -1.79% / slope_proxy: -0.002792

## VZLA (Vizsla Silver)
- close: 3.33 | RSI14: 41.330638 | ATR14%: 7.43%
- MA20 gap: -4.84% | MA50 gap: -21.39% | MA200 gap: -20.34%
- vol_ratio(Volume/Vol20): 1.021581 | gap_open: 3.03%
- RS vs SILJ gap: -20.27% / slope_proxy: -0.027351
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

## SCZM (Santacruz Silver)
- close: 8.13 | RSI14: 42.901997 | ATR14%: 10.71%
- MA20 gap: -6.03% | MA50 gap: -24.19% | MA200 gap: 11.19%
- vol_ratio(Volume/Vol20): 1.140248 | gap_open: 3.62%
- SilverMarginGate: SI=72.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.90% / slope_proxy: -0.020222
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
- close: 35.049999 | RSI14: 47.417991 | ATR14%: 12.35%
- MA20 gap: -3.75% | MA50 gap: -13.10% | MA200 gap: 105.05%
- vol_ratio(Volume/Vol20): 0.607047 | gap_open: 3.41%
- RS vs SILJ gap: -2.41% / slope_proxy: 0.175695
- RS vs GDXJ gap: -5.55% / slope_proxy: 0.046068
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
