# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-26**
- 실행시간(UTC): **2026-03-26 15:01:17**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.17
- IG OAS 4주 변화: 7.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.06
- VIX: 25.33
- NFCI: -0.47504

### Leadership ratios
- SILJ/SLV gap: 0.86% / slope_proxy: -0.00519
- GDXJ/GLD gap: -7.39% / slope_proxy: 0.000799

## VZLA (Vizsla Silver)
- close: 3.1698 | RSI14: 33.594349 | ATR14%: 8.46%
- MA20 gap: -14.53% | MA50 gap: -29.13% | MA200 gap: -24.27%
- vol_ratio(Volume/Vol20): 0.194967 | gap_open: 4.63%
- RS vs SILJ gap: -19.02% / slope_proxy: -0.027303
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.66 | RSI14: 35.311498 | ATR14%: 11.39%
- MA20 gap: -18.30% | MA50 gap: -30.50% | MA200 gap: 6.24%
- vol_ratio(Volume/Vol20): 0.182207 | gap_open: 3.60%
- SilverMarginGate: SI=69.264999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -15.23% / slope_proxy: -0.01699
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 33.485001 | RSI14: 42.903975 | ATR14%: 13.47%
- MA20 gap: -16.20% | MA50 gap: -17.58% | MA200 gap: 102.81%
- vol_ratio(Volume/Vol20): 0.162018 | gap_open: 5.83%
- RS vs SILJ gap: 5.27% / slope_proxy: 0.216279
- RS vs GDXJ gap: 3.42% / slope_proxy: 0.056769
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trigger(Breakout/Retest)=FALSE
