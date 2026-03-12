# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-12 03:00:35**

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
- HY OAS (BAMLH0A0HYM2): 3.06 / 4주 변화 20.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 7.0 bp
- 10Y Real Yield (DFII10): 1.78 / 4주 변화 -9.0 bp
- VIX (VIXCLS): 24.93
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.264326
- MA60: 6.484351
- gap: 27.45%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.225519
- MA60: 0.211898
- gap: 6.43%
- MA60_slope_proxy: -0.016601
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-12 03:02:21**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 83.29 bp / 4주 변화 5.19 bp
- CURVE_10s5s: 49.01 bp / 4주 변화 -12.14 bp

## NWG Price
- close: 588.0
- MA50: 630.732 / gap50: -6.78%
- MA200: 569.723 / gap200: 3.21%

## Relative Strength
- RS vs FTSE gap: -8.05% / slope_proxy: -0.002143
- RS vs Peers gap: -5.37% / slope_proxy: -0.057965

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-12 03:03:47**

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

- WTI ref (CL=F): 94.94 / 5D 27.16%
- Brent ref (BZ=F): 96.04 / 5D 17.99%
- Brent Tier: **>=90**
- Brent-WTI spread: 1.10
- Gas ref (NG=F): 3.27 / 5D 12.17%

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

- close: 55.58
- MA20 / MA60 / MA200: 51.17 / 45.41 / 43.80
- gap20 / gap60: 8.62% / 22.40%
- 5D return: 4.17%
- 20D high/low: 55.58 / 45.28

### Relative Strength

- ratio: 0.975430
- ratio_MA60: 0.903918
- ratio_gap: 7.91%
- ratio_slope_proxy(20d): -0.000095

### Volume (if available)

- volume: 20841500.00
- volume_MA20: 18117725.00
- volume_ratio: 1.15

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.99
- MA20 / MA60 / MA200: 16.56 / 14.22 / 12.85
- gap20 / gap60: 14.65% / 33.53%
- 5D return: 13.24%
- 20D high/low: 18.99 / 15.02

### Relative Strength

- ratio: 0.504919
- ratio_MA60: 0.399329
- ratio_gap: 26.44%
- ratio_slope_proxy(20d): 0.012394

### Volume (if available)

- volume: 43475400.00
- volume_MA20: 29623835.00
- volume_ratio: 1.47

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

- close: 6.31
- MA20 / MA60 / MA200: 6.27 / 5.08 / 3.82
- gap20 / gap60: 0.61% / 24.31%
- 5D return: -0.94%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016389
- ratio_MA60: 0.014755
- ratio_gap: 11.07%
- ratio_slope_proxy(20d): 0.000521

### Volume (if available)

- volume: 28617500.00
- volume_MA20: 55441645.00
- volume_ratio: 0.52

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.46
- MA20 / MA60 / MA200: 10.38 / 8.78 / 11.32
- gap20 / gap60: 19.98% / 41.89%
- 5D return: 11.65%
- 20D high/low: 12.48 / 8.77

### Relative Strength

- ratio: 0.049776
- ratio_MA60: 0.041161
- ratio_gap: 20.93%
- ratio_slope_proxy(20d): 0.003301

### Volume (if available)

- volume: 20997700.00
- volume_MA20: 19209495.00
- volume_ratio: 1.09

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-11**
- 실행시간(UTC): **2026-03-12 03:07:10**

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
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.06
- IG OAS 4주 변화: 7.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -9.0 bp / latest 1.78
- VIX: 24.93
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -0.07% / slope_proxy: -0.003108
- GDXJ/GLD gap: -3.74% / slope_proxy: 0.012294

## VZLA (Vizsla Silver)
- close: 4.09 | RSI14: 43.917896 | ATR14%: 7.79%
- MA20 gap: 2.57% | MA50 gap: -17.92% | MA200 gap: -1.98%
- vol_ratio(Volume/Vol20): 0.342698 | gap_open: 2.17%
- RS vs SILJ gap: -23.69% / slope_proxy: -0.029039
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.17 | RSI14: 43.780416 | ATR14%: 10.24%
- MA20 gap: -6.41% | MA50 gap: -11.36% | MA200 gap: 47.61%
- vol_ratio(Volume/Vol20): 1.385753 | gap_open: 0.75%
- SilverMarginGate: SI=84.900002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -12.12% / slope_proxy: 0.004187
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 42.57 | RSI14: 50.594047 | ATR14%: 13.47%
- MA20 gap: -0.97% | MA50 gap: 9.50% | MA200 gap: 188.40%
- vol_ratio(Volume/Vol20): 0.545868 | gap_open: 4.26%
- RS vs SILJ gap: 17.74% / slope_proxy: 0.248962
- RS vs GDXJ gap: 18.05% / slope_proxy: 0.065352
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
