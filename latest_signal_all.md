# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-11 15:00:55**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.81 / 4주 변화 -13.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -3.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 1.0 bp
- VIX (VIXCLS): 17.19
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.276524
- MA60: 8.428509
- gap: 21.93%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.297401
- MA60: 0.257527
- gap: 15.48%
- MA60_slope_proxy: 0.038125
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-11 15:00:58**

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
- TERM_SPREAD_10Y_POLICY: 113.01 bp / 4주 변화 13.29 bp
- CURVE_10s5s: 46.15 bp / 4주 변화 0.77 bp

## NWG Price
- close: 579.4
- MA50: 579.9431 / gap50: -0.09%
- MA200: 583.5705 / gap200: -0.71%

## Relative Strength
- RS vs FTSE gap: 0.48% / slope_proxy: -0.00235
- RS vs Peers gap: -3.68% / slope_proxy: -0.037349

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-11 15:01:04**

## ⚠️ DATA WARNING

- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 97.48 / 5D -8.40%
- Brent ref (BZ=F): 103.69 / 5D -9.39%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.21
- Gas ref (NG=F): 2.88 / 5D 0.45%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.95
- MA20 / MA60 / MA200: 56.86 / 56.80 / 47.19
- gap20 / gap60: -3.36% / -3.26%
- 5D return: -8.83%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.968282
- ratio_MA60: 0.990158
- ratio_gap: -2.21%
- ratio_slope_proxy(20d): 0.037701

### Volume (if available)

- volume: 3725382.00
- volume_MA20: 12658424.10
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.42
- MA20 / MA60 / MA200: 21.08 / 19.33 / 14.57
- gap20 / gap60: -3.12% / 5.64%
- 5D return: -7.22%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.528263
- ratio_MA60: 0.500996
- ratio_gap: 5.44%
- ratio_slope_proxy(20d): 0.044262

### Volume (if available)

- volume: 4145045.00
- volume_MA20: 19204372.25
- volume_ratio: 0.22

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.50
- MA20 / MA60 / MA200: 6.36 / 6.41 / 4.59
- gap20 / gap60: 2.17% / 1.32%
- 5D return: -5.60%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015209
- ratio_MA60: 0.015897
- ratio_gap: -4.33%
- ratio_slope_proxy(20d): 0.000232

### Volume (if available)

- volume: 7606898.00
- volume_MA20: 35362194.90
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.77
- MA20 / MA60 / MA200: 12.34 / 12.69 / 10.93
- gap20 / gap60: -4.65% / -7.32%
- 5D return: -14.56%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.048533
- ratio_MA60: 0.048824
- ratio_gap: -0.60%
- ratio_slope_proxy(20d): 0.000979

### Volume (if available)

- volume: 6133608.00
- volume_MA20: 19146120.40
- volume_ratio: 0.32

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

- 데이터 기준일(주가): **2026-05-11**
- 실행시간(UTC): **2026-05-11 15:01:37**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.81
- IG OAS 4주 변화: -3.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 1.0 bp / latest 1.96
- VIX: 17.19
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.28% / slope_proxy: 0.006063
- GDXJ/GLD gap: 3.51% / slope_proxy: -0.003945

## VZLA (Vizsla Silver)
- close: 3.685 | RSI14: 58.809262 | ATR14%: 5.63%
- MA20 gap: 7.30% | MA50 gap: 5.77% | MA200 gap: -12.53%
- vol_ratio(Volume/Vol20): 0.340264 | gap_open: 1.97%
- RS vs SILJ gap: -0.34% / slope_proxy: -0.014571
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
- close: 9.2499 | RSI14: 58.390917 | ATR14%: 7.06%
- MA20 gap: 7.97% | MA50 gap: 6.45% | MA200 gap: 15.73%
- vol_ratio(Volume/Vol20): 0.576025 | gap_open: 1.77%
- SilverMarginGate: SI=85.614998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.58% / slope_proxy: -0.02838
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
- close: 43.345501 | RSI14: 59.347947 | ATR14%: 8.52%
- MA20 gap: 10.88% | MA50 gap: 12.66% | MA200 gap: 98.43%
- vol_ratio(Volume/Vol20): 1.079115 | gap_open: 3.90%
- RS vs SILJ gap: 6.63% / slope_proxy: 0.033015
- RS vs GDXJ gap: 9.45% / slope_proxy: 0.005442
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
