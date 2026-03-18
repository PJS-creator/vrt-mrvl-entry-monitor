# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-18**
- 실행시간(UTC): **2026-03-18 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 28.0 bp / latest 3.22
- IG OAS 4주 변화: 12.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 10.0 bp / latest 1.87
- VIX: 22.37
- NFCI: -0.48574

### Leadership ratios
- SILJ/SLV gap: -1.63% / slope_proxy: -0.005055
- GDXJ/GLD gap: -9.35% / slope_proxy: 0.008328

## VZLA (Vizsla Silver)
- close: 3.4301 | RSI14: 32.704536 | ATR14%: 8.49%
- MA20 gap: -13.29% | MA50 gap: -28.40% | MA200 gap: -18.17%
- vol_ratio(Volume/Vol20): 0.361853 | gap_open: 3.07%
- RS vs SILJ gap: -23.92% / slope_proxy: -0.027558
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
- close: 8.33 | RSI14: 33.757327 | ATR14%: 11.07%
- MA20 gap: -21.58% | MA50 gap: -26.84% | MA200 gap: 17.88%
- vol_ratio(Volume/Vol20): 0.357819 | gap_open: 1.73%
- SilverMarginGate: SI=76.550003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.85% / slope_proxy: -0.004754
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
- close: 37.41 | RSI14: 44.780601 | ATR14%: 13.46%
- MA20 gap: -14.58% | MA50 gap: -7.21% | MA200 gap: 138.89%
- vol_ratio(Volume/Vol20): 0.40321 | gap_open: 6.33%
- RS vs SILJ gap: 11.62% / slope_proxy: 0.257158
- RS vs GDXJ gap: 10.90% / slope_proxy: 0.067532
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
