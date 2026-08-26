# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-26**
- 실행시간(UTC): **2026-08-26 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -14.0 bp / latest 2.7
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 2.38
- VIX: 15.45
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 10.83% / slope_proxy: 0.022751
- GDXJ/GLD gap: 15.54% / slope_proxy: 0.003677

## VZLA (Vizsla Silver)
- close: 4.015 | RSI14: 64.38911 | ATR14%: 4.65%
- MA20 gap: 8.76% | MA50 gap: 17.11% | MA200 gap: -1.51%
- vol_ratio(Volume/Vol20): 0.134425 | gap_open: 2.48%
- RS vs SILJ gap: -2.87% / slope_proxy: 0.003167
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
- close: 9.66 | RSI14: 68.261417 | ATR14%: 5.44%
- MA20 gap: 12.93% | MA50 gap: 31.34% | MA200 gap: 11.18%
- vol_ratio(Volume/Vol20): 0.15815 | gap_open: 1.64%
- SilverMarginGate: SI=68.129997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.46% / slope_proxy: 0.003766
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

## HYMC (Hycroft Mining)
- close: 25.34 | RSI14: 51.627271 | ATR14%: 7.48%
- MA20 gap: 0.94% | MA50 gap: 9.16% | MA200 gap: -13.77%
- vol_ratio(Volume/Vol20): 0.403135 | gap_open: 3.37%
- RS vs SILJ gap: -11.27% / slope_proxy: -0.1095
- RS vs GDXJ gap: -15.83% / slope_proxy: -0.030896
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
