# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-17 15:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.27 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.94 / 4주 변화 15.0 bp
- 10Y Real Yield (DFII10): 1.92 / 4주 변화 15.0 bp
- VIX (VIXCLS): 23.51
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.191522
- MA60: 6.65711
- gap: 23.05%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.231407
- MA60: 0.211188
- gap: 9.57%
- MA60_slope_proxy: -0.013767
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-17 15:00:45**

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
- TERM_SPREAD_10Y_POLICY: 101.01 bp / 4주 변화 34.32 bp
- CURVE_10s5s: 49.78 bp / 4주 변화 -9.04 bp

## NWG Price
- close: 587.6
- MA50: 624.004 / gap50: -5.83%
- MA200: 570.6469 / gap200: 2.97%

## Relative Strength
- RS vs FTSE gap: -7.87% / slope_proxy: -0.002511
- RS vs Peers gap: -0.84% / slope_proxy: -0.055481

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-17 15:00:52**

## Commodity Regime

- WTI ref (CL=F): 93.33 / 5D 11.84%
- Brent ref (BZ=F): 101.01 / 5D 15.05%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.68
- Gas ref (NG=F): 3.04 / 5D 0.56%

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

- close: 57.91
- MA20 / MA60 / MA200: 53.55 / 46.60 / 44.14
- gap20 / gap60: 8.15% / 24.28%
- 5D return: 9.02%
- 20D high/low: 58.41 / 46.89

### Relative Strength

- ratio: 0.985031
- ratio_MA60: 0.910445
- ratio_gap: 8.19%
- ratio_slope_proxy(20d): 0.011752

### Volume (if available)

- volume: 3911217.00
- volume_MA20: 19796995.85
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.86
- MA20 / MA60 / MA200: 17.33 / 14.70 / 13.00
- gap20 / gap60: 14.64% / 35.14%
- 5D return: 10.42%
- 20D high/low: 19.86 / 15.29

### Relative Strength

- ratio: 0.536167
- ratio_MA60: 0.409334
- ratio_gap: 30.99%
- ratio_slope_proxy(20d): 0.023269

### Volume (if available)

- volume: 10992969.00
- volume_MA20: 31455328.45
- volume_ratio: 0.35

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

- close: 6.37
- MA20 / MA60 / MA200: 6.30 / 5.23 / 3.89
- gap20 / gap60: 1.08% / 21.72%
- 5D return: 3.33%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016511
- ratio_MA60: 0.014945
- ratio_gap: 10.48%
- ratio_slope_proxy(20d): 0.000592

### Volume (if available)

- volume: 9833135.00
- volume_MA20: 40018136.75
- volume_ratio: 0.25

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

- close: 12.85
- MA20 / MA60 / MA200: 11.06 / 9.22 / 11.32
- gap20 / gap60: 16.12% / 39.31%
- 5D return: 12.83%
- 20D high/low: 13.08 / 9.30

### Relative Strength

- ratio: 0.050541
- ratio_MA60: 0.042419
- ratio_gap: 19.15%
- ratio_slope_proxy(20d): 0.004170

### Volume (if available)

- volume: 5013378.00
- volume_MA20: 21334573.90
- volume_ratio: 0.23

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

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-17 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.27
- IG OAS 4주 변화: 15.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.92
- VIX: 23.51
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: 0.23% / slope_proxy: -0.004746
- GDXJ/GLD gap: -6.49% / slope_proxy: 0.009226

## VZLA (Vizsla Silver)
- close: 3.64 | RSI14: 36.35466 | ATR14%: 7.90%
- MA20 gap: -8.43% | MA50 gap: -24.72% | MA200 gap: -13.12%
- vol_ratio(Volume/Vol20): 0.11272 | gap_open: 1.10%
- RS vs SILJ gap: -24.62% / slope_proxy: -0.02791
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 8.9266 | RSI14: 36.943224 | ATR14%: 10.32%
- MA20 gap: -16.56% | MA50 gap: -21.85% | MA200 gap: 26.86%
- vol_ratio(Volume/Vol20): 0.145402 | gap_open: 1.12%
- SilverMarginGate: SI=80.764999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.26% / slope_proxy: -0.003399
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
- close: 40.145 | RSI14: 48.222104 | ATR14%: 12.60%
- MA20 gap: -8.66% | MA50 gap: 0.04% | MA200 gap: 159.21%
- vol_ratio(Volume/Vol20): 0.230483 | gap_open: 0.74%
- RS vs SILJ gap: 13.96% / slope_proxy: 0.257862
- RS vs GDXJ gap: 13.36% / slope_proxy: 0.067706
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
