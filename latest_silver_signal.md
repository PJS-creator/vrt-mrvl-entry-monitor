# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-17**
- 실행시간(UTC): **2026-03-18 03:01:07**

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
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.87
- VIX: 23.51
- NFCI: -0.5137

### Leadership ratios
- SILJ/SLV gap: 0.19% / slope_proxy: -0.004749
- GDXJ/GLD gap: -7.60% / slope_proxy: 0.00917

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 35.19634 | ATR14%: 8.22%
- MA20 gap: -9.87% | MA50 gap: -25.94% | MA200 gap: -14.54%
- vol_ratio(Volume/Vol20): 0.565242 | gap_open: 1.10%
- RS vs SILJ gap: -24.78% / slope_proxy: -0.027914
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
- close: 8.65 | RSI14: 35.401153 | ATR14%: 10.88%
- MA20 gap: -19.04% | MA50 gap: -24.23% | MA200 gap: 22.96%
- vol_ratio(Volume/Vol20): 0.647437 | gap_open: 1.12%
- SilverMarginGate: SI=79.175003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -17.65% / slope_proxy: -0.003478
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
- close: 40.279999 | RSI14: 48.405155 | ATR14%: 12.67%
- MA20 gap: -8.37% | MA50 gap: 0.37% | MA200 gap: 160.07%
- vol_ratio(Volume/Vol20): 0.604856 | gap_open: 0.74%
- RS vs SILJ gap: 15.97% / slope_proxy: 0.258239
- RS vs GDXJ gap: 15.33% / slope_proxy: 0.067799
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
