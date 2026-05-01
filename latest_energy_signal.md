# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-01 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 106.00 / 5D 10.59%
- Brent ref (BZ=F): 111.90 / 5D 6.50%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.90
- Gas ref (NG=F): 2.77 / 5D 6.04%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.58
- MA20 / MA60 / MA200: 58.26 / 55.58 / 46.72
- gap20 / gap60: 3.99% / 8.99%
- 5D return: 4.76%
- 20D high/low: 62.97 / 53.79

### Relative Strength

- ratio: 1.015591
- ratio_MA60: 0.976845
- ratio_gap: 3.97%
- ratio_slope_proxy(20d): 0.037761

### Volume (if available)

- volume: 10367662.00
- volume_MA20: 13752403.10
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 22.03
- MA20 / MA60 / MA200: 20.96 / 18.63 / 14.25
- gap20 / gap60: 5.09% / 18.22%
- 5D return: 4.18%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.554912
- ratio_MA60: 0.484765
- ratio_gap: 14.47%
- ratio_slope_proxy(20d): 0.046939

### Volume (if available)

- volume: 14058792.00
- volume_MA20: 23548644.60
- volume_ratio: 0.60

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

- close: 6.82
- MA20 / MA60 / MA200: 6.41 / 6.30 / 4.46
- gap20 / gap60: 6.44% / 8.19%
- 5D return: 12.54%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015215
- ratio_MA60: 0.015909
- ratio_gap: -4.36%
- ratio_slope_proxy(20d): 0.000553

### Volume (if available)

- volume: 38457287.00
- volume_MA20: 31787459.35
- volume_ratio: 1.21

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.27
- MA20 / MA60 / MA200: 13.00 / 12.39 / 11.03
- gap20 / gap60: 2.05% / 7.11%
- 5D return: 2.47%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048263
- ratio_MA60: 0.048505
- ratio_gap: -0.50%
- ratio_slope_proxy(20d): 0.002301

### Volume (if available)

- volume: 17967428.00
- volume_MA20: 23788886.40
- volume_ratio: 0.76

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG
