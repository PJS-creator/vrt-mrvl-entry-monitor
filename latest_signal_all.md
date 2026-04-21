# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-21 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.87 / 4주 변화 -32.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 1.9 / 4주 변화 -11.0 bp
- VIX (VIXCLS): 18.87
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.107476
- MA60: 7.722265
- gap: 17.94%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.324309
- MA60: 0.229579
- gap: 41.26%
- MA60_slope_proxy: 0.01936
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-21 15:00:52**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- BoE IUDBEDR failed (BoE returned HTML instead of CSV (likely blocked/cookie page).), using cached values if available.
- BoE IUDSOIA failed (BoE returned HTML instead of CSV (likely blocked/cookie page).), using cached values if available.
- BoE IUDMNPY failed (BoE returned HTML instead of CSV (likely blocked/cookie page).), using cached values if available.
- BoE IUDSNPY failed (BoE returned HTML instead of CSV (likely blocked/cookie page).), using cached values if available.
- BoE LPMVTVX failed (BoE returned HTML instead of CSV (likely blocked/cookie page).), using cached values if available.
- BoE LPMVQJW failed (BoE returned HTML instead of CSV (likely blocked/cookie page).), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: None bp / 4주 변화 None bp
- CURVE_10s5s: None bp / 4주 변화 None bp

## NWG Price
- close: 604.2
- MA50: 588.8512 / gap50: 2.61%
- MA200: 578.4352 / gap200: 4.45%

## Relative Strength
- RS vs FTSE gap: -0.71% / slope_proxy: -0.00267
- RS vs Peers gap: -4.20% / slope_proxy: -0.038805

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-21 15:00:57**

## Commodity Regime

- WTI ref (CL=F): 88.42 / 5D -3.13%
- Brent ref (BZ=F): 91.74 / 5D -3.22%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.32
- Gas ref (NG=F): 2.69 / 5D 3.69%

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

- close: 55.24
- MA20 / MA60 / MA200: 60.05 / 53.94 / 46.21
- gap20 / gap60: -8.01% / 2.42%
- 5D return: -0.24%
- 20D high/low: 66.24 / 53.79

### Relative Strength

- ratio: 0.998193
- ratio_MA60: 0.962307
- ratio_gap: 3.73%
- ratio_slope_proxy(20d): 0.038790

### Volume (if available)

- volume: 2440166.00
- volume_MA20: 17322418.30
- volume_ratio: 0.14

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.20
- MA20 / MA60 / MA200: 20.70 / 18.01 / 14.03
- gap20 / gap60: 2.40% / 17.71%
- 5D return: 0.90%
- 20D high/low: 21.97 / 19.75

### Relative Strength

- ratio: 0.513007
- ratio_MA60: 0.471555
- ratio_gap: 8.79%
- ratio_slope_proxy(20d): 0.051699

### Volume (if available)

- volume: 3696614.00
- volume_MA20: 31067220.70
- volume_ratio: 0.12

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.99
- MA20 / MA60 / MA200: 6.49 / 6.12 / 4.33
- gap20 / gap60: -7.76% / -2.22%
- 5D return: -3.00%
- 20D high/low: 6.93 / 5.89

### Relative Strength

- ratio: 0.014697
- ratio_MA60: 0.015820
- ratio_gap: -7.10%
- ratio_slope_proxy(20d): 0.000725

### Volume (if available)

- volume: 5850639.00
- volume_MA20: 30037816.95
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

- close: 11.84
- MA20 / MA60 / MA200: 14.34 / 12.01 / 11.16
- gap20 / gap60: -17.48% / -1.49%
- 5D return: -5.40%
- 20D high/low: 17.53 / 11.45

### Relative Strength

- ratio: 0.046545
- ratio_MA60: 0.048181
- ratio_gap: -3.39%
- ratio_slope_proxy(20d): 0.004400

### Volume (if available)

- volume: 4832033.00
- volume_MA20: 27937331.65
- volume_ratio: 0.17

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

- 데이터 기준일(주가): **2026-04-21**
- 실행시간(UTC): **2026-04-21 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -32.0 bp / latest 2.87
- IG OAS 4주 변화: -7.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -11.0 bp / latest 1.9
- VIX: 18.87
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: -0.23% / slope_proxy: 0.011426
- GDXJ/GLD gap: -0.18% / slope_proxy: -0.003831

## VZLA (Vizsla Silver)
- close: 3.39 | RSI14: 46.407605 | ATR14%: 5.77%
- MA20 gap: 2.74% | MA50 gap: -6.50% | MA200 gap: -19.22%
- vol_ratio(Volume/Vol20): 0.315511 | gap_open: 1.14%
- RS vs SILJ gap: -8.50% / slope_proxy: -0.026659
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 8.755 | RSI14: 49.800544 | ATR14%: 8.05%
- MA20 gap: 5.66% | MA50 gap: -7.50% | MA200 gap: 14.11%
- vol_ratio(Volume/Vol20): 0.250219 | gap_open: 1.10%
- SilverMarginGate: SI=77.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.23% / slope_proxy: -0.027403
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
- close: 38.856998 | RSI14: 50.28084 | ATR14%: 9.90%
- MA20 gap: 4.46% | MA50 gap: -1.22% | MA200 gap: 99.84%
- vol_ratio(Volume/Vol20): 0.602452 | gap_open: 1.30%
- RS vs SILJ gap: 3.57% / slope_proxy: 0.073503
- RS vs GDXJ gap: 1.88% / slope_proxy: 0.016829
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
