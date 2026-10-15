# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-15 03:01:01**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 40.0 bp / latest 3.16
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 26.0 bp / latest 2.88
- VIX: 15.27
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.05% / slope_proxy: 0.007588
- GDXJ/GLD gap: -6.20% / slope_proxy: 0.012709

## VZLA (Vizsla Silver)
- close: 3.17 | RSI14: 30.629651 | ATR14%: 5.92%
- MA20 gap: -15.14% | MA50 gap: -17.14% | MA200 gap: -18.62%
- vol_ratio(Volume/Vol20): 0.966438 | gap_open: 3.57%
- RS vs SILJ gap: -1.41% / slope_proxy: 0.002599
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
- close: 7.96 | RSI14: 39.559395 | ATR14%: 6.98%
- MA20 gap: -10.51% | MA50 gap: -12.73% | MA200 gap: -11.23%
- vol_ratio(Volume/Vol20): 1.555553 | gap_open: 4.96%
- SilverMarginGate: SI=56.244999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.65% / slope_proxy: 0.021596
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 16.344999 | RSI14: 32.133944 | ATR14%: 7.84%
- MA20 gap: -16.36% | MA50 gap: -27.30% | MA200 gap: -46.81%
- vol_ratio(Volume/Vol20): 1.407522 | gap_open: 3.24%
- RS vs SILJ gap: -14.24% / slope_proxy: -0.052103
- RS vs GDXJ gap: -17.71% / slope_proxy: -0.017779
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE
