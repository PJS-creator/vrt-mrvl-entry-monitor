# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-09**
- 실행시간(UTC): **2026-03-10 03:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 26.0 bp / latest 3.13
- IG OAS 4주 변화: 8.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -8.0 bp / latest 1.8
- VIX: 29.49
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: -0.48% / slope_proxy: -0.002831
- GDXJ/GLD gap: -1.59% / slope_proxy: 0.013427

## VZLA (Vizsla Silver)
- close: 3.99 | RSI14: 41.082976 | ATR14%: 8.36%
- MA20 gap: 0.13% | MA50 gap: -20.99% | MA200 gap: -4.05%
- vol_ratio(Volume/Vol20): 0.405229 | gap_open: 3.00%
- RS vs SILJ gap: -27.00% / slope_proxy: -0.028919
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.1 | RSI14: 42.679789 | ATR14%: 10.57%
- MA20 gap: -8.13% | MA50 gap: -11.99% | MA200 gap: 48.46%
- vol_ratio(Volume/Vol20): 1.884312 | gap_open: 4.39%
- SilverMarginGate: SI=90.019997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -13.61% / slope_proxy: 0.009921
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 40.599998 | RSI14: 48.437988 | ATR14%: 14.50%
- MA20 gap: -4.21% | MA50 gap: 6.48% | MA200 gap: 182.88%
- vol_ratio(Volume/Vol20): 0.85391 | gap_open: 2.69%
- RS vs SILJ gap: 14.93% / slope_proxy: 0.246037
- RS vs GDXJ gap: 14.05% / slope_proxy: 0.064624
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
