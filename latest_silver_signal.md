# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 22:59:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -12.0 bp / latest 2.69
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 2.38
- VIX: 15.85
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 10.44% / slope_proxy: 0.021896
- GDXJ/GLD gap: 16.10% / slope_proxy: 0.002779

## VZLA (Vizsla Silver)
- close: 4.04 | RSI14: 65.627331 | ATR14%: 4.71%
- MA20 gap: 10.78% | MA50 gap: 18.09% | MA200 gap: -0.88%
- vol_ratio(Volume/Vol20): 0.675793 | gap_open: 1.02%
- RS vs SILJ gap: -3.42% / slope_proxy: 0.003549
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
- close: 9.77 | RSI14: 70.321824 | ATR14%: 5.54%
- MA20 gap: 16.50% | MA50 gap: 33.60% | MA200 gap: 12.75%
- vol_ratio(Volume/Vol20): 0.546152 | gap_open: 1.88%
- SilverMarginGate: SI=69.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.74% / slope_proxy: 0.003062
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
- close: 26.08 | RSI14: 54.128844 | ATR14%: 7.38%
- MA20 gap: 5.18% | MA50 gap: 12.11% | MA200 gap: -10.97%
- vol_ratio(Volume/Vol20): 0.832846 | gap_open: 3.24%
- RS vs SILJ gap: -10.16% / slope_proxy: -0.113048
- RS vs GDXJ gap: -15.42% / slope_proxy: -0.031528
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
