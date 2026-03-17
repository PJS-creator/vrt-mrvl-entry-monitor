# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-17 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 3.27
- IG OAS 4주 변화: 15.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: 15.0 bp / latest 1.92
- VIX: 23.51
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: 0.23% / slope_proxy: -0.004746
- GDXJ/GLD gap: -6.49% / slope_proxy: 0.009226

## VZLA (Vizsla Silver)
- close: 3.64 | RSI14: 36.35466 | ATR14%: 7.90%
- MA20 gap: -8.43% | MA50 gap: -24.72% | MA200 gap: -13.12%
- vol_ratio(Volume/Vol20): 0.11272 | gap_open: 1.10%
- RS vs SILJ gap: -24.62% / slope_proxy: -0.02791
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
- close: 8.9266 | RSI14: 36.943224 | ATR14%: 10.32%
- MA20 gap: -16.56% | MA50 gap: -21.85% | MA200 gap: 26.86%
- vol_ratio(Volume/Vol20): 0.145402 | gap_open: 1.12%
- SilverMarginGate: SI=80.764999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.26% / slope_proxy: -0.003399
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
- close: 40.145 | RSI14: 48.222104 | ATR14%: 12.60%
- MA20 gap: -8.66% | MA50 gap: 0.04% | MA200 gap: 159.21%
- vol_ratio(Volume/Vol20): 0.230483 | gap_open: 0.74%
- RS vs SILJ gap: 13.96% / slope_proxy: 0.257862
- RS vs GDXJ gap: 13.36% / slope_proxy: 0.067706
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
