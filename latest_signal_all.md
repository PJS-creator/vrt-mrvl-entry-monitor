# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-20 15:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 -4.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -6.0 bp
- 10Y Real Yield (DFII10): 2.13 / 4주 변화 22.0 bp
- VIX (VIXCLS): 18.06
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.623156
- MA60: 8.770932
- gap: 9.72%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.336134
- MA60: 0.271983
- gap: 23.59%
- MA60_slope_proxy: 0.040298
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-20 15:00:42**

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
- TERM_SPREAD_10Y_POLICY: 135.26 bp / 4주 변화 31.97 bp
- CURVE_10s5s: 47.3 bp / 4주 변화 -2.54 bp

## NWG Price
- close: 575.539
- MA50: 575.5471 / gap50: -0.00%
- MA200: 585.1498 / gap200: -1.64%

## Relative Strength
- RS vs FTSE gap: -0.82% / slope_proxy: -0.002019
- RS vs Peers gap: -4.67% / slope_proxy: -0.035328

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-20 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 100.88 / 5D -0.14%
- Brent ref (BZ=F): 107.46 / 5D 1.73%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.58
- Gas ref (NG=F): 3.03 / 5D 5.76%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.14
- MA20 / MA60 / MA200: 57.86 / 57.87 / 47.71
- gap20 / gap60: 3.95% / 3.92%
- 5D return: 7.05%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.990179
- ratio_MA60: 0.999338
- ratio_gap: -0.92%
- ratio_slope_proxy(20d): 0.034945

### Volume (if available)

- volume: 3613192.00
- volume_MA20: 11774109.60
- volume_ratio: 0.31

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.23
- MA20 / MA60 / MA200: 20.86 / 19.87 / 14.85
- gap20 / gap60: -3.04% / 1.81%
- 5D return: 3.27%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.552355
- ratio_MA60: 0.517950
- ratio_gap: 6.64%
- ratio_slope_proxy(20d): 0.046898

### Volume (if available)

- volume: 3824905.00
- volume_MA20: 17320150.25
- volume_ratio: 0.22

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 7.46
- MA20 / MA60 / MA200: 6.71 / 6.49 / 4.73
- gap20 / gap60: 11.19% / 14.89%
- 5D return: 12.69%
- 20D high/low: 7.58 / 6.06

### Relative Strength

- ratio: 0.016361
- ratio_MA60: 0.015832
- ratio_gap: 3.35%
- ratio_slope_proxy(20d): 0.000005

### Volume (if available)

- volume: 7207473.00
- volume_MA20: 37261458.65
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.12
- MA20 / MA60 / MA200: 12.92 / 13.20 / 10.88
- gap20 / gap60: 9.25% / 6.95%
- 5D return: 8.62%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.057275
- ratio_MA60: 0.050587
- ratio_gap: 13.22%
- ratio_slope_proxy(20d): 0.002248

### Volume (if available)

- volume: 6916783.00
- volume_MA20: 20755054.15
- volume_ratio: 0.33

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-20**
- 실행시간(UTC): **2026-05-20 15:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -4.0 bp / latest 2.83
- IG OAS 4주 변화: -6.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 22.0 bp / latest 2.13
- VIX: 18.06
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -5.56% / slope_proxy: -0.003858
- GDXJ/GLD gap: -5.01% / slope_proxy: -0.00401

## VZLA (Vizsla Silver)
- close: 3.375 | RSI14: 45.979915 | ATR14%: 6.39%
- MA20 gap: -3.04% | MA50 gap: -1.00% | MA200 gap: -20.23%
- vol_ratio(Volume/Vol20): 0.265192 | gap_open: 1.84%
- RS vs SILJ gap: 3.91% / slope_proxy: -0.005973
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
- close: 8.14 | RSI14: 43.434532 | ATR14%: 8.45%
- MA20 gap: -5.53% | MA50 gap: -3.97% | MA200 gap: -0.55%
- vol_ratio(Volume/Vol20): 0.461909 | gap_open: 3.28%
- SilverMarginGate: SI=76.375 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.42% / slope_proxy: -0.019177
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
- close: 33.665001 | RSI14: 41.676284 | ATR14%: 10.55%
- MA20 gap: -11.09% | MA50 gap: -10.12% | MA200 gap: 46.02%
- vol_ratio(Volume/Vol20): 0.346658 | gap_open: 3.30%
- RS vs SILJ gap: -5.81% / slope_proxy: 0.026788
- RS vs GDXJ gap: -3.84% / slope_proxy: 0.007307
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
