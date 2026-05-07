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
