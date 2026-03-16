# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-16 15:00:38**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.28 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 14.0 bp
- 10Y Real Yield (DFII10): 1.89 / 4주 변화 9.0 bp
- VIX (VIXCLS): 27.19
- NFCI: -0.5137

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.250434
- MA60: 6.61149
- gap: 24.79%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.230432
- MA60: 0.211321
- gap: 9.04%
- MA60_slope_proxy: -0.014347
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-16 15:00:47**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 97.58 bp / 4주 변화 27.32 bp
- CURVE_10s5s: 49.64 bp / 4주 변화 -8.79 bp

## NWG Price
- close: 574.0
- MA50: 625.476 / gap50: -8.23%
- MA200: 570.3604 / gap200: 0.64%

## Relative Strength
- RS vs FTSE gap: -9.45% / slope_proxy: -0.002405
- RS vs Peers gap: -1.66% / slope_proxy: -0.056167

## Why not today?
- RiskGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-03-16 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 95.02 / 5D 0.26%
- Brent ref (BZ=F): 97.60 / 5D -1.37%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.58
- Gas ref (NG=F): 3.06 / 5D -1.76%

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

- close: 57.80
- MA20 / MA60 / MA200: 52.97 / 46.32 / 44.06
- gap20 / gap60: 9.13% / 24.79%
- 5D return: 5.55%
- 20D high/low: 58.41 / 45.72

### Relative Strength

- ratio: 0.995959
- ratio_MA60: 0.909326
- ratio_gap: 9.53%
- ratio_slope_proxy(20d): 0.009278

### Volume (if available)

- volume: 6176252.00
- volume_MA20: 19569012.60
- volume_ratio: 0.32

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.05
- MA20 / MA60 / MA200: 17.08 / 14.56 / 12.96
- gap20 / gap60: 11.56% / 30.85%
- 5D return: 4.93%
- 20D high/low: 19.05 / 15.02

### Relative Strength

- ratio: 0.524353
- ratio_MA60: 0.406740
- ratio_gap: 28.92%
- ratio_slope_proxy(20d): 0.020384

### Volume (if available)

- volume: 7262546.00
- volume_MA20: 30490417.30
- volume_ratio: 0.24

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

- close: 6.29
- MA20 / MA60 / MA200: 6.29 / 5.19 / 3.88
- gap20 / gap60: -0.08% / 21.08%
- 5D return: 1.86%
- 20D high/low: 6.54 / 5.93

### Relative Strength

- ratio: 0.016760
- ratio_MA60: 0.014905
- ratio_gap: 12.45%
- ratio_slope_proxy(20d): 0.000577

### Volume (if available)

- volume: 7908637.00
- volume_MA20: 42418621.85
- volume_ratio: 0.19

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

- close: 12.47
- MA20 / MA60 / MA200: 10.88 / 9.12 / 11.33
- gap20 / gap60: 14.60% / 36.72%
- 5D return: 8.34%
- 20D high/low: 13.10 / 8.77

### Relative Strength

- ratio: 0.049476
- ratio_MA60: 0.042165
- ratio_gap: 17.34%
- ratio_slope_proxy(20d): 0.003911

### Volume (if available)

- volume: 6731371.00
- volume_MA20: 21040608.55
- volume_ratio: 0.32

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

- 데이터 기준일(주가): **2026-03-16**
- 실행시간(UTC): **2026-03-16 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.28
- IG OAS 4주 변화: 14.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.89
- VIX: 27.19
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: -1.34% / slope_proxy: -0.004424
- GDXJ/GLD gap: -7.28% / slope_proxy: 0.009957

## VZLA (Vizsla Silver)
- close: 3.6679 | RSI14: 37.116755 | ATR14%: 8.21%
- MA20 gap: -7.77% | MA50 gap: -24.74% | MA200 gap: -12.37%
- vol_ratio(Volume/Vol20): 0.124845 | gap_open: 0.00%
- RS vs SILJ gap: -23.95% / slope_proxy: -0.028159
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
- close: 9.12 | RSI14: 37.829516 | ATR14%: 10.41%
- MA20 gap: -14.84% | MA50 gap: -20.25% | MA200 gap: 30.23%
- vol_ratio(Volume/Vol20): 1.074393 | gap_open: 3.54%
- SilverMarginGate: SI=80.514999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.82% / slope_proxy: -0.00201
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
- close: 39.952499 | RSI14: 47.896647 | ATR14%: 13.15%
- MA20 gap: -8.49% | MA50 gap: 0.31% | MA200 gap: 161.04%
- vol_ratio(Volume/Vol20): 0.288242 | gap_open: 2.87%
- RS vs SILJ gap: 15.80% / slope_proxy: 0.255281
- RS vs GDXJ gap: 15.35% / slope_proxy: 0.067035
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
