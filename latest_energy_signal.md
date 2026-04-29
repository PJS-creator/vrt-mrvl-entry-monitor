# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-29 03:00:54**

## Commodity Regime

- WTI ref (CL=F): 99.05 / 5D 7.51%
- Brent ref (BZ=F): 103.87 / 5D 5.47%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.82
- Gas ref (NG=F): 2.67 / 5D -0.93%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **True**

### Trend

- close: 58.61
- MA20 / MA60 / MA200: 58.55 / 55.04 / 46.54
- gap20 / gap60: 0.10% / 6.49%
- 5D return: 4.05%
- 20D high/low: 65.00 / 53.79

### Relative Strength

- ratio: 1.015595
- ratio_MA60: 0.971999
- ratio_gap: 4.49%
- ratio_slope_proxy(20d): 0.038007

### Volume (if available)

- volume: 10417943.00
- volume_MA20: 15593867.15
- volume_ratio: 0.67

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.23
- MA20 / MA60 / MA200: 20.80 / 18.41 / 14.16
- gap20 / gap60: 2.08% / 15.34%
- 5D return: 0.97%
- 20D high/low: 21.84 / 19.86

### Relative Strength

- ratio: 0.534895
- ratio_MA60: 0.479400
- ratio_gap: 11.58%
- ratio_slope_proxy(20d): 0.047134

### Volume (if available)

- volume: 13616232.00
- volume_MA20: 27080661.60
- volume_ratio: 0.50

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **True**

### Trend

- close: 6.79
- MA20 / MA60 / MA200: 6.38 / 6.24 / 4.42
- gap20 / gap60: 6.51% / 8.86%
- 5D return: 12.23%
- 20D high/low: 6.79 / 5.89

### Relative Strength

- ratio: 0.015376
- ratio_MA60: 0.015857
- ratio_gap: -3.04%
- ratio_slope_proxy(20d): 0.000579

### Volume (if available)

- volume: 53641748.00
- volume_MA20: 31903912.40
- volume_ratio: 1.68

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.16
- MA20 / MA60 / MA200: 13.20 / 12.26 / 11.06
- gap20 / gap60: -7.90% / -0.79%
- 5D return: 0.58%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.045890
- ratio_MA60: 0.048370
- ratio_gap: -5.13%
- ratio_slope_proxy(20d): 0.002811

### Volume (if available)

- volume: 14238365.00
- volume_MA20: 25761773.25
- volume_ratio: 0.55

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: OXY, RIG
