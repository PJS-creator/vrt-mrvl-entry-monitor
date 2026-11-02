# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-02**
- 실행시간(UTC): **2026-11-02 15:01:17**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.26
- IG OAS 4주 변화: 3.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: -25.0 bp / latest 2.63
- VIX: 19.42
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: 0.47% / slope_proxy: 0.005916
- GDXJ/GLD gap: -8.71% / slope_proxy: 0.006305

## VZLA (Vizsla Silver)
- close: 3.165 | RSI14: 41.627735 | ATR14%: 5.87%
- MA20 gap: -3.76% | MA50 gap: -14.11% | MA200 gap: -15.21%
- vol_ratio(Volume/Vol20): 0.092953 | gap_open: 3.27%
- RS vs SILJ gap: 3.73% / slope_proxy: 0.000404
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
- close: 7.215 | RSI14: 40.158887 | ATR14%: 7.00%
- MA20 gap: -9.33% | MA50 gap: -18.01% | MA200 gap: -17.86%
- vol_ratio(Volume/Vol20): 0.283969 | gap_open: 3.69%
- SilverMarginGate: SI=51.029999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.91% / slope_proxy: 0.01732
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
- close: 17.4 | RSI14: 46.921866 | ATR14%: 6.93%
- MA20 gap: 1.11% | MA50 gap: -12.95% | MA200 gap: -41.93%
- vol_ratio(Volume/Vol20): 0.174713 | gap_open: 3.41%
- RS vs SILJ gap: 0.68% / slope_proxy: -0.048291
- RS vs GDXJ gap: -1.81% / slope_proxy: -0.01642
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
