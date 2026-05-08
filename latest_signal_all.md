# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-07**
- 실행시간(UTC): **2026-05-08 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 -19.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.94 / 4주 변화 -2.0 bp
- VIX (VIXCLS): 17.39
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.697946
- MA60: 8.346285
- gap: 16.19%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.29626
- MA60: 0.254041
- gap: 16.62%
- MA60_slope_proxy: 0.03746
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-07**
- 실행시간(UTC): **2026-05-08 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 127.01 bp / 4주 변화 14.61 bp
- CURVE_10s5s: 45.63 bp / 4주 변화 3.93 bp

## NWG Price
- close: 572.253
- MA50: 581.1454 / gap50: -1.53%
- MA200: 582.7772 / gap200: -1.81%

## Relative Strength
- RS vs FTSE gap: -0.93% / slope_proxy: -0.002436
- RS vs Peers gap: -5.48% / slope_proxy: -0.039438

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-08 03:00:52**

## Commodity Regime

- WTI ref (CL=F): 95.48 / 5D -9.13%
- Brent ref (BZ=F): 100.86 / 5D -11.53%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.38
- Gas ref (NG=F): 2.78 / 5D 0.47%

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

- close: 53.94
- MA20 / MA60 / MA200: 57.27 / 56.54 / 47.09
- gap20 / gap60: -5.81% / -4.60%
- 5D return: -10.96%
- 20D high/low: 60.76 / 53.79

### Relative Strength

- ratio: 0.964075
- ratio_MA60: 0.986568
- ratio_gap: -2.28%
- ratio_slope_proxy(20d): 0.037241

### Volume (if available)

- volume: 18057809.00
- volume_MA20: 13065145.45
- volume_ratio: 1.38

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.37
- MA20 / MA60 / MA200: 21.20 / 19.17 / 14.49
- gap20 / gap60: -3.92% / 6.28%
- 5D return: -7.54%
- 20D high/low: 22.03 / 20.33

### Relative Strength

- ratio: 0.525000
- ratio_MA60: 0.496793
- ratio_gap: 5.68%
- ratio_slope_proxy(20d): 0.044879

### Volume (if available)

- volume: 26836521.00
- volume_MA20: 20961356.05
- volume_ratio: 1.28

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.17
- MA20 / MA60 / MA200: 6.37 / 6.40 / 4.56
- gap20 / gap60: -3.14% / -3.54%
- 5D return: -9.53%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014772
- ratio_MA60: 0.015921
- ratio_gap: -7.22%
- ratio_slope_proxy(20d): 0.000342

### Volume (if available)

- volume: 27975443.00
- volume_MA20: 35213872.15
- volume_ratio: 0.79

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.69
- MA20 / MA60 / MA200: 12.46 / 12.63 / 10.96
- gap20 / gap60: -6.21% / -7.41%
- 5D return: -11.91%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.047370
- ratio_MA60: 0.048672
- ratio_gap: -2.68%
- ratio_slope_proxy(20d): 0.001113

### Volume (if available)

- volume: 17521293.00
- volume_MA20: 20300274.65
- volume_ratio: 0.86

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

- 데이터 기준일(주가): **2026-05-07**
- 실행시간(UTC): **2026-05-08 03:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -19.0 bp / latest 2.75
- IG OAS 4주 변화: -5.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: -2.0 bp / latest 1.94
- VIX: 17.39
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -4.66% / slope_proxy: 0.009284
- GDXJ/GLD gap: -1.05% / slope_proxy: -0.004026

## VZLA (Vizsla Silver)
- close: 3.43 | RSI14: 50.182683 | ATR14%: 6.15%
- MA20 gap: 0.88% | MA50 gap: -2.30% | MA200 gap: -18.53%
- vol_ratio(Volume/Vol20): 1.007935 | gap_open: 3.18%
- RS vs SILJ gap: -0.31% / slope_proxy: -0.017192
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.83 | RSI14: 54.180391 | ATR14%: 7.52%
- MA20 gap: 4.09% | MA50 gap: 0.11% | MA200 gap: 11.18%
- vol_ratio(Volume/Vol20): 1.270169 | gap_open: 4.12%
- SilverMarginGate: SI=80.290001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.53% / slope_proxy: -0.029881
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## HYMC (Hycroft Mining)
- close: 38.880001 | RSI14: 51.789727 | ATR14%: 8.81%
- MA20 gap: 0.07% | MA50 gap: 0.10% | MA200 gap: 81.06%
- vol_ratio(Volume/Vol20): 1.289009 | gap_open: 5.18%
- RS vs SILJ gap: 3.45% / slope_proxy: 0.030815
- RS vs GDXJ gap: 3.93% / slope_proxy: 0.004245
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
