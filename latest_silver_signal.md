# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-17**
- 실행시간(UTC): **2026-08-17 22:56:37**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.41
- VIX: 14.25
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 7.17% / slope_proxy: 0.016702
- GDXJ/GLD gap: 9.84% / slope_proxy: -0.002021

## VZLA (Vizsla Silver)
- close: 3.65 | RSI14: 56.34922 | ATR14%: 5.01%
- MA20 gap: 5.13% | MA50 gap: 8.51% | MA200 gap: -10.55%
- vol_ratio(Volume/Vol20): 1.209107 | gap_open: 0.53%
- RS vs SILJ gap: -4.19% / slope_proxy: 0.005208
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
- close: 8.75 | RSI14: 68.501606 | ATR14%: 5.70%
- MA20 gap: 19.32% | MA50 gap: 26.44% | MA200 gap: 2.60%
- vol_ratio(Volume/Vol20): 1.686816 | gap_open: 0.00%
- SilverMarginGate: SI=65.860001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.10% / slope_proxy: -0.002214
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
- close: 26.32 | RSI14: 59.325151 | ATR14%: 6.68%
- MA20 gap: 13.83% | MA50 gap: 13.69% | MA200 gap: -8.43%
- vol_ratio(Volume/Vol20): 1.069958 | gap_open: 0.89%
- RS vs SILJ gap: -3.51% / slope_proxy: -0.126384
- RS vs GDXJ gap: -7.05% / slope_proxy: -0.03306
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
