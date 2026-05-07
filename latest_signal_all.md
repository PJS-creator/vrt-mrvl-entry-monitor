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
- 실행시간(UTC): **2026-05-07 15:00:51**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 -19.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.96 / 4주 변화 0.0 bp
- VIX (VIXCLS): 17.39
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.80186
- MA60: 8.348017
- gap: 17.42%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.305215
- MA60: 0.25419
- gap: 20.07%
- MA60_slope_proxy: 0.037609
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-07**
- 실행시간(UTC): **2026-05-07 15:00:58**

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
- close: 574.0
- MA50: 581.1804 / gap50: -1.24%
- MA200: 582.7859 / gap200: -1.51%

## Relative Strength
- RS vs FTSE gap: -0.86% / slope_proxy: -0.002436
- RS vs Peers gap: -4.95% / slope_proxy: -0.039351

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-07 15:01:06**

## Commodity Regime

- WTI ref (CL=F): 91.36 / 5D -13.05%
- Brent ref (BZ=F): 97.30 / 5D -14.66%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.94
- Gas ref (NG=F): 2.79 / 5D 0.65%

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

- close: 53.45
- MA20 / MA60 / MA200: 57.24 / 56.53 / 47.09
- gap20 / gap60: -6.62% / -5.45%
- 5D return: -11.77%
- 20D high/low: 60.76 / 53.45

### Relative Strength

- ratio: 0.965847
- ratio_MA60: 0.986598
- ratio_gap: -2.10%
- ratio_slope_proxy(20d): 0.037271

### Volume (if available)

- volume: 4742363.00
- volume_MA20: 12396598.15
- volume_ratio: 0.38

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.93
- MA20 / MA60 / MA200: 21.18 / 19.16 / 14.49
- gap20 / gap60: -5.89% / 4.02%
- 5D return: -9.53%
- 20D high/low: 22.03 / 19.93

### Relative Strength

- ratio: 0.509852
- ratio_MA60: 0.496540
- ratio_gap: 2.68%
- ratio_slope_proxy(20d): 0.044626

### Volume (if available)

- volume: 7759548.00
- volume_MA20: 20006042.40
- volume_ratio: 0.39

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.07
- MA20 / MA60 / MA200: 6.36 / 6.39 / 4.55
- gap20 / gap60: -4.64% / -5.08%
- 5D return: -11.00%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.014604
- ratio_MA60: 0.015918
- ratio_gap: -8.26%
- ratio_slope_proxy(20d): 0.000340

### Volume (if available)

- volume: 8693771.00
- volume_MA20: 34249578.55
- volume_ratio: 0.25

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

- close: 11.31
- MA20 / MA60 / MA200: 12.44 / 12.62 / 10.95
- gap20 / gap60: -9.08% / -10.33%
- 5D return: -14.73%
- 20D high/low: 13.77 / 11.31

### Relative Strength

- ratio: 0.046265
- ratio_MA60: 0.048654
- ratio_gap: -4.91%
- ratio_slope_proxy(20d): 0.001094

### Volume (if available)

- volume: 6515118.00
- volume_MA20: 19748535.90
- volume_ratio: 0.33

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
- 실행시간(UTC): **2026-05-07 15:01:12**

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
- 10Y Real Yield 4주 변화: 0.0 bp / latest 1.96
- VIX: 17.39
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -2.02% / slope_proxy: 0.009487
- GDXJ/GLD gap: 2.78% / slope_proxy: -0.00384

## VZLA (Vizsla Silver)
- close: 3.67 | RSI14: 57.950037 | ATR14%: 5.69%
- MA20 gap: 7.56% | MA50 gap: 4.40% | MA200 gap: -12.85%
- vol_ratio(Volume/Vol20): 0.409383 | gap_open: 3.18%
- RS vs SILJ gap: 0.22% / slope_proxy: -0.017182
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
- close: 9.4 | RSI14: 59.184897 | ATR14%: 7.07%
- MA20 gap: 10.44% | MA50 gap: 6.44% | MA200 gap: 18.31%
- vol_ratio(Volume/Vol20): 0.677783 | gap_open: 4.12%
- SilverMarginGate: SI=82.504997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 0.56% / slope_proxy: -0.02988
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
- close: 42.450001 | RSI14: 57.898731 | ATR14%: 7.89%
- MA20 gap: 8.75% | MA50 gap: 9.09% | MA200 gap: 97.52%
- vol_ratio(Volume/Vol20): 0.478633 | gap_open: 5.18%
- RS vs SILJ gap: 6.09% / slope_proxy: 0.031359
- RS vs GDXJ gap: 7.74% / slope_proxy: 0.004443
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
