# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-07**
- 실행시간(UTC): **2026-07-08 03:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.72
- IG OAS 4주 변화: 0.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.24
- VIX: 15.57
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 3.70% / slope_proxy: 0.00775
- GDXJ/GLD gap: -5.67% / slope_proxy: -0.00193

## VZLA (Vizsla Silver)
- close: 3.09 | RSI14: 38.833284 | ATR14%: 6.90%
- MA20 gap: -8.34% | MA50 gap: -11.58% | MA200 gap: -26.83%
- vol_ratio(Volume/Vol20): 1.313095 | gap_open: 0.61%
- RS vs SILJ gap: 2.23% / slope_proxy: 0.005022
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.37 | RSI14: 40.029081 | ATR14%: 8.02%
- MA20 gap: -5.50% | MA50 gap: -17.27% | MA200 gap: -25.19%
- vol_ratio(Volume/Vol20): 1.044071 | gap_open: 2.35%
- SilverMarginGate: SI=60.415001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.25% / slope_proxy: -0.006859
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
- close: 21.709999 | RSI14: 34.149273 | ATR14%: 10.00%
- MA20 gap: -10.53% | MA50 gap: -30.32% | MA200 gap: -18.18%
- vol_ratio(Volume/Vol20): 0.627393 | gap_open: 2.08%
- RS vs SILJ gap: -22.57% / slope_proxy: -0.092558
- RS vs GDXJ gap: -22.68% / slope_proxy: -0.020307
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
