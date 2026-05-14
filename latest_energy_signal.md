# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-14 03:00:49**

## Commodity Regime

- WTI ref (CL=F): 101.45 / 5D 6.70%
- Brent ref (BZ=F): 105.99 / 5D 4.66%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.54
- Gas ref (NG=F): 2.87 / 5D 4.95%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 56.18
- MA20 / MA60 / MA200: 56.93 / 57.15 / 47.31
- gap20 / gap60: -1.33% / -1.70%
- 5D return: 1.92%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.974839
- ratio_MA60: 0.994210
- ratio_gap: -1.95%
- ratio_slope_proxy(20d): 0.038657

### Volume (if available)

- volume: 5737686.00
- volume_MA20: 12543169.30
- volume_ratio: 0.46

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **True**

### Trend

- close: 19.59
- MA20 / MA60 / MA200: 21.03 / 19.50 / 14.65
- gap20 / gap60: -6.86% / 0.44%
- 5D return: -6.31%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.532626
- ratio_MA60: 0.505741
- ratio_gap: 5.32%
- ratio_slope_proxy(20d): 0.045059

### Volume (if available)

- volume: 18217044.00
- volume_MA20: 19574917.20
- volume_ratio: 0.93

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.62
- MA20 / MA60 / MA200: 6.40 / 6.42 / 4.62
- gap20 / gap60: 3.41% / 3.12%
- 5D return: 6.26%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015133
- ratio_MA60: 0.015840
- ratio_gap: -4.46%
- ratio_slope_proxy(20d): 0.000103

### Volume (if available)

- volume: 26429388.00
- volume_MA20: 36397374.40
- volume_ratio: 0.73

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

- close: 13.00
- MA20 / MA60 / MA200: 12.41 / 12.83 / 10.91
- gap20 / gap60: 4.75% / 1.34%
- 5D return: 8.33%
- 20D high/low: 13.77 / 11.45

### Relative Strength

- ratio: 0.054307
- ratio_MA60: 0.049367
- ratio_gap: 10.01%
- ratio_slope_proxy(20d): 0.001182

### Volume (if available)

- volume: 31434489.00
- volume_MA20: 22031774.45
- volume_ratio: 1.43

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: PBR
