# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-04 15:00:52**

## ⚠️ DATA WARNING

- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 102.51 / 5D 6.37%
- Brent ref (BZ=F): 111.44 / 5D 2.97%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.93
- Gas ref (NG=F): 2.87 / 5D 12.55%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.30
- MA20 / MA60 / MA200: 57.86 / 56.03 / 46.88
- gap20 / gap60: 2.49% / 5.84%
- 5D return: 3.54%
- 20D high/low: 62.94 / 53.79

### Relative Strength

- ratio: 1.005000
- ratio_MA60: 0.981046
- ratio_gap: 2.44%
- ratio_slope_proxy(20d): 0.037101

### Volume (if available)

- volume: 2365166.00
- volume_MA20: 12990668.30
- volume_ratio: 0.18

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.88
- MA20 / MA60 / MA200: 21.09 / 18.87 / 14.35
- gap20 / gap60: 3.71% / 15.95%
- 5D return: 4.37%
- 20D high/low: 22.03 / 19.86

### Relative Strength

- ratio: 0.554499
- ratio_MA60: 0.489791
- ratio_gap: 13.21%
- ratio_slope_proxy(20d): 0.045751

### Volume (if available)

- volume: 2785757.00
- volume_MA20: 21907432.85
- volume_ratio: 0.13

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.79
- MA20 / MA60 / MA200: 6.43 / 6.36 / 4.50
- gap20 / gap60: 5.60% / 6.77%
- 5D return: 4.14%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015346
- ratio_MA60: 0.015941
- ratio_gap: -3.73%
- ratio_slope_proxy(20d): 0.000498

### Volume (if available)

- volume: 5811177.00
- volume_MA20: 30631008.85
- volume_ratio: 0.19

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

- close: 13.10
- MA20 / MA60 / MA200: 12.77 / 12.50 / 11.00
- gap20 / gap60: 2.58% / 4.72%
- 5D return: 7.42%
- 20D high/low: 15.99 / 11.45

### Relative Strength

- ratio: 0.048180
- ratio_MA60: 0.048605
- ratio_gap: -0.88%
- ratio_slope_proxy(20d): 0.001776

### Volume (if available)

- volume: 4919106.00
- volume_MA20: 22137565.30
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG
