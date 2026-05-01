# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-01 15:00:45**

## Commodity Regime

- WTI ref (CL=F): 101.51 / 5D 7.53%
- Brent ref (BZ=F): 108.38 / 5D 2.90%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.87
- Gas ref (NG=F): 2.77 / 5D 9.75%

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

- close: 58.97
- MA20 / MA60 / MA200: 58.05 / 55.79 / 46.80
- gap20 / gap60: 1.58% / 5.70%
- 5D return: 3.24%
- 20D high/low: 62.96 / 53.79

### Relative Strength

- ratio: 0.999576
- ratio_MA60: 0.978748
- ratio_gap: 2.13%
- ratio_slope_proxy(20d): 0.037221

### Volume (if available)

- volume: 4955582.00
- volume_MA20: 13012144.10
- volume_ratio: 0.38

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.76
- MA20 / MA60 / MA200: 21.03 / 18.75 / 14.30
- gap20 / gap60: 3.48% / 16.07%
- 5D return: 4.26%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.552635
- ratio_MA60: 0.487192
- ratio_gap: 13.43%
- ratio_slope_proxy(20d): 0.046272

### Volume (if available)

- volume: 3257455.00
- volume_MA20: 22226792.75
- volume_ratio: 0.15

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

- close: 6.65
- MA20 / MA60 / MA200: 6.41 / 6.33 / 4.48
- gap20 / gap60: 3.74% / 5.13%
- 5D return: 8.84%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015067
- ratio_MA60: 0.015914
- ratio_gap: -5.33%
- ratio_slope_proxy(20d): 0.000516

### Volume (if available)

- volume: 7522630.00
- volume_MA20: 30190036.50
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 12.94
- MA20 / MA60 / MA200: 12.92 / 12.45 / 11.01
- gap20 / gap60: 0.17% / 3.97%
- 5D return: 8.74%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048050
- ratio_MA60: 0.048556
- ratio_gap: -1.04%
- ratio_slope_proxy(20d): 0.002081

### Volume (if available)

- volume: 8085267.00
- volume_MA20: 22577913.35
- volume_ratio: 0.36

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: OXY, VG
