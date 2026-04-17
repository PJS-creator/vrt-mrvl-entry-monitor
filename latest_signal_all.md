# Daily Signals (All-in-One)

## Quick Summary

- Core (VRT/MRVL): **✅ Entry condition met: MRVL**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-17 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.85 / 4주 변화 -35.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -11.0 bp
- 10Y Real Yield (DFII10): 1.9 / 4주 변화 4.0 bp
- VIX (VIXCLS): 18.17
- NFCI: -0.465

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.461738
- MA60: 7.575154
- gap: 11.70%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.29325
- MA60: 0.224046
- gap: 30.89%
- MA60_slope_proxy: 0.013362
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: MRVL

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-17 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 99.1 bp / 4주 변화 8.74 bp
- CURVE_10s5s: 45.74 bp / 4주 변화 -4.8 bp

## NWG Price
- close: 616.2
- MA50: 592.1073 / gap50: 4.07%
- MA200: 576.5444 / gap200: 6.88%

## Relative Strength
- RS vs FTSE gap: 0.03% / slope_proxy: -0.002931
- RS vs Peers gap: -1.78% / slope_proxy: -0.038871

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-04-17 03:00:56**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 89.83 / 5D -8.21%
- Brent ref (BZ=F): 98.21 / 5D 2.39%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.38
- Gas ref (NG=F): 2.66 / 5D -0.37%

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

- close: 56.87
- MA20 / MA60 / MA200: 60.91 / 53.38 / 46.04
- gap20 / gap60: -6.63% / 6.53%
- 5D return: -2.84%
- 20D high/low: 66.24 / 55.38

### Relative Strength

- ratio: 1.005125
- ratio_MA60: 0.957489
- ratio_gap: 4.98%
- ratio_slope_proxy(20d): 0.039466

### Volume (if available)

- volume: 9758503.00
- volume_MA20: 19108220.15
- volume_ratio: 0.51

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.50
- MA20 / MA60 / MA200: 20.47 / 17.66 / 13.90
- gap20 / gap60: 5.01% / 21.73%
- 5D return: 3.91%
- 20D high/low: 21.97 / 18.80

### Relative Strength

- ratio: 0.518447
- ratio_MA60: 0.465664
- ratio_gap: 11.34%
- ratio_slope_proxy(20d): 0.053609

### Volume (if available)

- volume: 30058527.00
- volume_MA20: 34473791.35
- volume_ratio: 0.87

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.35
- MA20 / MA60 / MA200: 6.55 / 6.06 / 4.28
- gap20 / gap60: -3.12% / 4.78%
- 5D return: -3.20%
- 20D high/low: 6.93 / 6.15

### Relative Strength

- ratio: 0.015578
- ratio_MA60: 0.015776
- ratio_gap: -1.26%
- ratio_slope_proxy(20d): 0.000785

### Volume (if available)

- volume: 21942295.00
- volume_MA20: 32035159.75
- volume_ratio: 0.68

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

- close: 12.68
- MA20 / MA60 / MA200: 14.90 / 11.91 / 11.22
- gap20 / gap60: -14.89% / 6.48%
- 5D return: -2.39%
- 20D high/low: 17.53 / 12.18

### Relative Strength

- ratio: 0.048261
- ratio_MA60: 0.048181
- ratio_gap: 0.17%
- ratio_slope_proxy(20d): 0.005347

### Volume (if available)

- volume: 18693764.00
- volume_MA20: 36017938.20
- volume_ratio: 0.52

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

- 데이터 기준일(주가): **2026-04-16**
- 실행시간(UTC): **2026-04-17 03:01:49**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -35.0 bp / latest 2.85
- IG OAS 4주 변화: -11.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 4.0 bp / latest 1.9
- VIX: 18.17
- NFCI: -0.465

### Leadership ratios
- SILJ/SLV gap: 0.02% / slope_proxy: 0.008578
- GDXJ/GLD gap: 1.40% / slope_proxy: -0.004511

## VZLA (Vizsla Silver)
- close: 3.43 | RSI14: 48.22525 | ATR14%: 5.88%
- MA20 gap: 5.72% | MA50 gap: -7.14% | MA200 gap: -18.12%
- vol_ratio(Volume/Vol20): 1.214015 | gap_open: 0.88%
- RS vs SILJ gap: -11.88% / slope_proxy: -0.027561
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 9.03 | RSI14: 53.197743 | ATR14%: 8.17%
- MA20 gap: 12.19% | MA50 gap: -5.96% | MA200 gap: 19.06%
- vol_ratio(Volume/Vol20): 0.6087 | gap_open: 0.91%
- SilverMarginGate: SI=78.565002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -8.03% / slope_proxy: -0.024372
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 40.720001 | RSI14: 56.036826 | ATR14%: 9.21%
- MA20 gap: 14.56% | MA50 gap: 4.54% | MA200 gap: 115.96%
- vol_ratio(Volume/Vol20): 0.462824 | gap_open: 2.50%
- RS vs SILJ gap: 6.43% / slope_proxy: 0.08774
- RS vs GDXJ gap: 3.59% / slope_proxy: 0.02171
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=True
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
