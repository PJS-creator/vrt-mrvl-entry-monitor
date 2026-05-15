# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-15 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.76 / 4주 변화 -10.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 1.99 / 4주 변화 9.0 bp
- VIX (VIXCLS): 17.26
- NFCI: -0.524

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.835901
- MA60: 8.65517
- gap: 25.20%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.318041
- MA60: 0.265271
- gap: 19.89%
- MA60_slope_proxy: 0.03963
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-15 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 127.79 bp / 4주 변화 28.44 bp
- CURVE_10s5s: 46.22 bp / 4주 변화 0.15 bp

## NWG Price
- close: 558.4
- MA50: 576.4344 / gap50: -3.13%
- MA200: 584.4206 / gap200: -4.45%

## Relative Strength
- RS vs FTSE gap: -2.14% / slope_proxy: -0.00218
- RS vs Peers gap: -5.44% / slope_proxy: -0.036823

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-15 15:00:58**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 100.54 / 5D 5.37%
- Brent ref (BZ=F): 109.35 / 5D 7.96%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.81
- Gas ref (NG=F): 2.96 / 5D 7.36%

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

- close: 58.60
- MA20 / MA60 / MA200: 57.17 / 57.44 / 47.44
- gap20 / gap60: 2.50% / 2.02%
- 5D return: 10.50%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.991038
- ratio_MA60: 0.997090
- ratio_gap: -0.61%
- ratio_slope_proxy(20d): 0.038209

### Volume (if available)

- volume: 4051348.00
- volume_MA20: 11532672.40
- volume_ratio: 0.35

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.74
- MA20 / MA60 / MA200: 20.92 / 19.65 / 14.72
- gap20 / gap60: -5.65% / 0.47%
- 5D return: -2.90%
- 20D high/low: 22.03 / 19.59

### Relative Strength

- ratio: 0.547951
- ratio_MA60: 0.510327
- ratio_gap: 7.37%
- ratio_slope_proxy(20d): 0.045538

### Volume (if available)

- volume: 2934023.00
- volume_MA20: 16788061.15
- volume_ratio: 0.17

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.85
- MA20 / MA60 / MA200: 6.47 / 6.44 / 4.66
- gap20 / gap60: 5.79% / 6.38%
- 5D return: 7.03%
- 20D high/low: 6.96 / 5.89

### Relative Strength

- ratio: 0.015585
- ratio_MA60: 0.015821
- ratio_gap: -1.49%
- ratio_slope_proxy(20d): 0.000025

### Volume (if available)

- volume: 3698285.00
- volume_MA20: 34506264.25
- volume_ratio: 0.11

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

- close: 13.89
- MA20 / MA60 / MA200: 12.55 / 12.95 / 10.89
- gap20 / gap60: 10.73% / 7.27%
- 5D return: 21.35%
- 20D high/low: 13.89 / 11.45

### Relative Strength

- ratio: 0.056975
- ratio_MA60: 0.049774
- ratio_gap: 14.47%
- ratio_slope_proxy(20d): 0.001449

### Volume (if available)

- volume: 8611834.00
- volume_MA20: 20660121.70
- volume_ratio: 0.42

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

- 데이터 기준일(주가): **2026-05-15**
- 실행시간(UTC): **2026-05-15 15:01:33**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.76
- IG OAS 4주 변화: -5.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 9.0 bp / latest 1.99
- VIX: 17.26
- NFCI: -0.524

### Leadership ratios
- SILJ/SLV gap: -2.63% / slope_proxy: 0.000242
- GDXJ/GLD gap: -2.19% / slope_proxy: -0.003437

## VZLA (Vizsla Silver)
- close: 3.485 | RSI14: 48.601168 | ATR14%: 6.39%
- MA20 gap: -0.22% | MA50 gap: 1.01% | MA200 gap: -17.51%
- vol_ratio(Volume/Vol20): 0.265443 | gap_open: 5.59%
- RS vs SILJ gap: 2.98% / slope_proxy: -0.009595
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
- close: 8.835 | RSI14: 49.875181 | ATR14%: 8.04%
- MA20 gap: 1.47% | MA50 gap: 2.78% | MA200 gap: 8.88%
- vol_ratio(Volume/Vol20): 0.449856 | gap_open: 9.38%
- SilverMarginGate: SI=76.695 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 2.60% / slope_proxy: -0.023271
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
- close: 36.360001 | RSI14: 45.319704 | ATR14%: 10.39%
- MA20 gap: -6.74% | MA50 gap: -4.09% | MA200 gap: 60.89%
- vol_ratio(Volume/Vol20): 0.445419 | gap_open: 6.76%
- RS vs SILJ gap: -2.84% / slope_proxy: 0.028311
- RS vs GDXJ gap: -0.34% / slope_proxy: 0.006467
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
