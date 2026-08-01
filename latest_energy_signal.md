# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-01 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 84.67 / 5D -5.20%
- Brent ref (BZ=F): 90.12 / 5D -6.88%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.45
- Gas ref (NG=F): 2.75 / 5D -4.32%

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

- close: 57.07
- MA20 / MA60 / MA200: 54.65 / 54.97 / 49.90
- gap20 / gap60: 4.43% / 3.82%
- 5D return: -0.40%
- 20D high/low: 57.60 / 48.81

### Relative Strength

- ratio: 0.958354
- ratio_MA60: 0.969286
- ratio_gap: -1.13%
- ratio_slope_proxy(20d): -0.019084

### Volume (if available)

- volume: 6810100.00
- volume_MA20: 9024970.00
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.40
- MA20 / MA60 / MA200: 18.01 / 18.23 / 16.10
- gap20 / gap60: 7.72% / 6.40%
- 5D return: 3.36%
- 20D high/low: 19.40 / 16.26

### Relative Strength

- ratio: 0.529331
- ratio_MA60: 0.513769
- ratio_gap: 3.03%
- ratio_slope_proxy(20d): -0.006752

### Volume (if available)

- volume: 11607200.00
- volume_MA20: 15541650.00
- volume_ratio: 0.75

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.32
- MA20 / MA60 / MA200: 5.18 / 5.77 / 5.32
- gap20 / gap60: 2.79% / -7.82%
- 5D return: -0.56%
- 20D high/low: 5.37 / 4.93

### Relative Strength

- ratio: 0.013825
- ratio_MA60: 0.014251
- ratio_gap: -2.99%
- ratio_slope_proxy(20d): -0.000505

### Volume (if available)

- volume: 62763100.00
- volume_MA20: 42281260.00
- volume_ratio: 1.48

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.38
- MA20 / MA60 / MA200: 13.14 / 12.58 / 10.69
- gap20 / gap60: 1.80% / 6.35%
- 5D return: -6.50%
- 20D high/low: 15.16 / 10.85

### Relative Strength

- ratio: 0.050765
- ratio_MA60: 0.051169
- ratio_gap: -0.79%
- ratio_slope_proxy(20d): 0.000764

### Volume (if available)

- volume: 10402400.00
- volume_MA20: 16325970.00
- volume_ratio: 0.64

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG
