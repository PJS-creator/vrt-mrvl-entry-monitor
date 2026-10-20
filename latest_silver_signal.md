# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-20**
- 실행시간(UTC): **2026-10-20 15:01:18**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 63.0 bp / latest 3.29
- IG OAS 4주 변화: 10.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 6.0 bp / latest 2.74
- VIX: 18.44
- NFCI: -0.499

### Leadership ratios
- SILJ/SLV gap: -2.01% / slope_proxy: 0.007308
- GDXJ/GLD gap: -2.49% / slope_proxy: 0.011203

## VZLA (Vizsla Silver)
- close: 3.298 | RSI14: 39.308745 | ATR14%: 5.41%
- MA20 gap: -7.51% | MA50 gap: -13.03% | MA200 gap: -14.34%
- vol_ratio(Volume/Vol20): 0.267535 | gap_open: 0.62%
- RS vs SILJ gap: -1.80% / slope_proxy: 0.001566
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
- close: 8.515 | RSI14: 46.917431 | ATR14%: 6.18%
- MA20 gap: -2.37% | MA50 gap: -6.70% | MA200 gap: -4.72%
- vol_ratio(Volume/Vol20): 0.154844 | gap_open: 2.03%
- SilverMarginGate: SI=58.384998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.24% / slope_proxy: 0.022867
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
- close: 17.620001 | RSI14: 41.465157 | ATR14%: 7.13%
- MA20 gap: -5.72% | MA50 gap: -19.26% | MA200 gap: -42.41%
- vol_ratio(Volume/Vol20): 0.274596 | gap_open: 2.14%
- RS vs SILJ gap: -10.54% / slope_proxy: -0.050893
- RS vs GDXJ gap: -14.35% / slope_proxy: -0.017494
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
