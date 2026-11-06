# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-06 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.32
- IG OAS 4주 변화: 9.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -28.0 bp / latest 2.64
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 1.84% / slope_proxy: 0.004681
- GDXJ/GLD gap: -5.27% / slope_proxy: 0.002712

## VZLA (Vizsla Silver)
- close: 3.18 | RSI14: 44.116236 | ATR14%: 6.01%
- MA20 gap: -1.21% | MA50 gap: -11.99% | MA200 gap: -13.35%
- vol_ratio(Volume/Vol20): 0.065585 | gap_open: 0.63%
- RS vs SILJ gap: 0.71% / slope_proxy: 0.000552
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
- close: 7.41 | RSI14: 45.069821 | ATR14%: 7.10%
- MA20 gap: -3.18% | MA50 gap: -13.82% | MA200 gap: -14.57%
- vol_ratio(Volume/Vol20): 0.055721 | gap_open: 1.44%
- SilverMarginGate: SI=52.005001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.55% / slope_proxy: 0.013171
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
- close: 17.58 | RSI14: 49.496576 | ATR14%: 7.47%
- MA20 gap: 4.39% | MA50 gap: -8.74% | MA200 gap: -40.37%
- vol_ratio(Volume/Vol20): 0.133828 | gap_open: 1.59%
- RS vs SILJ gap: 0.39% / slope_proxy: -0.052741
- RS vs GDXJ gap: -3.79% / slope_proxy: -0.017657
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
