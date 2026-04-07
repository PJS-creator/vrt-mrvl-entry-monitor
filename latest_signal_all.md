# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-07 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.05 / 4주 변화 -14.0 bp
- IG OAS (BAMLC0A0CM): 0.85 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 1.99 / 4주 변화 19.0 bp
- VIX (VIXCLS): 24.17
- NFCI: -0.4337

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.030043
- MA60: 7.221939
- gap: 11.19%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.27243
- MA60: 0.214616
- gap: 26.94%
- MA60_slope_proxy: 0.002233
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-07 15:00:49**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 103.02 bp / 4주 변화 34.9 bp
- CURVE_10s5s: 43.43 bp / 4주 변화 -14.86 bp

## NWG Price
- close: 572.0
- MA50: 599.4343 / gap50: -4.58%
- MA200: 572.5723 / gap200: -0.10%

## Relative Strength
- RS vs FTSE gap: -6.24% / slope_proxy: -0.003361
- RS vs Peers gap: -4.18% / slope_proxy: -0.043201

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-07 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 115.99 / 5D 12.74%
- Brent ref (BZ=F): 110.45 / 5D -2.07%
- Brent Tier: **>=90**
- Brent-WTI spread: -5.54
- Gas ref (NG=F): 2.85 / 5D -1.35%

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

- close: 63.73
- MA20 / MA60 / MA200: 60.74 / 51.69 / 45.52
- gap20 / gap60: 4.92% / 23.30%
- 5D return: -3.79%
- 20D high/low: 66.24 / 53.12

### Relative Strength

- ratio: 1.050350
- ratio_MA60: 0.945946
- ratio_gap: 11.04%
- ratio_slope_proxy(20d): 0.038194

### Volume (if available)

- volume: 4130484.00
- volume_MA20: 20694779.20
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.00
- MA20 / MA60 / MA200: 19.78 / 16.66 / 13.60
- gap20 / gap60: 6.18% / 26.04%
- 5D return: 0.91%
- 20D high/low: 21.00 / 17.99

### Relative Strength

- ratio: 0.551109
- ratio_MA60: 0.449848
- ratio_gap: 22.51%
- ratio_slope_proxy(20d): 0.054164

### Volume (if available)

- volume: 5465798.00
- volume_MA20: 35676814.90
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

- close: 6.62
- MA20 / MA60 / MA200: 6.50 / 5.81 / 4.15
- gap20 / gap60: 1.71% / 13.88%
- 5D return: -0.53%
- 20D high/low: 6.93 / 6.16

### Relative Strength

- ratio: 0.016368
- ratio_MA60: 0.015491
- ratio_gap: 5.67%
- ratio_slope_proxy(20d): 0.000805

### Volume (if available)

- volume: 5658782.00
- volume_MA20: 35484959.10
- volume_ratio: 0.16

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 16.58
- MA20 / MA60 / MA200: 14.89 / 11.34 / 11.35
- gap20 / gap60: 11.35% / 46.26%
- 5D return: -1.84%
- 20D high/low: 17.53 / 11.38

### Relative Strength

- ratio: 0.057327
- ratio_MA60: 0.047147
- ratio_gap: 21.59%
- ratio_slope_proxy(20d): 0.006513

### Volume (if available)

- volume: 7992869.00
- volume_MA20: 35581693.45
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-04-07**
- 실행시간(UTC): **2026-04-07 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -14.0 bp / latest 3.05
- IG OAS 4주 변화: 0.0 bp / latest 0.85
- 10Y Real Yield 4주 변화: 19.0 bp / latest 1.99
- VIX: 24.17
- NFCI: -0.43366

### Leadership ratios
- SILJ/SLV gap: 6.49% / slope_proxy: -0.00044
- GDXJ/GLD gap: -2.77% / slope_proxy: -0.004352

## VZLA (Vizsla Silver)
- close: 3.1701 | RSI14: 37.926684 | ATR14%: 7.36%
- MA20 gap: -6.29% | MA50 gap: -21.71% | MA200 gap: -24.10%
- vol_ratio(Volume/Vol20): 0.281167 | gap_open: 1.21%
- RS vs SILJ gap: -19.67% / slope_proxy: -0.027472
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
- close: 7.67 | RSI14: 40.639822 | ATR14%: 10.65%
- MA20 gap: -7.91% | MA50 gap: -25.88% | MA200 gap: 3.86%
- vol_ratio(Volume/Vol20): 0.185449 | gap_open: 0.61%
- SilverMarginGate: SI=71.095001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -19.63% / slope_proxy: -0.02208
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
- close: 35.1782 | RSI14: 47.555473 | ATR14%: 11.61%
- MA20 gap: -1.61% | MA50 gap: -11.47% | MA200 gap: 100.08%
- vol_ratio(Volume/Vol20): 0.195585 | gap_open: 2.64%
- RS vs SILJ gap: -0.64% / slope_proxy: 0.151625
- RS vs GDXJ gap: -2.33% / slope_proxy: 0.039979
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
