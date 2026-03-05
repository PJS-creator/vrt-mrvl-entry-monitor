# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-03-05**
- 실행시간(UTC): **2026-03-05 07:02:20**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **True**
- GoldUptrend(GC=F): **True**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.08
- IG OAS 4주 변화: 10.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: -15.0 bp / latest 1.77
- VIX: 23.57
- NFCI: -0.52365

### Leadership ratios
- SILJ/SLV gap: 9.35% / slope_proxy: -0.003661
- GDXJ/GLD gap: 2.70% / slope_proxy: 0.014118

## VZLA (Vizsla Silver)
- close: 4.16 | RSI14: 44.006136 | ATR14%: 8.36%
- MA20 gap: 2.12% | MA50 gap: -19.18% | MA200 gap: 0.60%
- vol_ratio(Volume/Vol20): 0.240817 | gap_open: 2.97%
- RS vs SILJ gap: -30.06% / slope_proxy: -0.026831
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MinersLeadership(SILJ/SLV)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 10.36 | RSI14: 43.647732 | ATR14%: 10.85%
- MA20 gap: -7.38% | MA50 gap: -9.25% | MA200 gap: 55.20%
- vol_ratio(Volume/Vol20): 0.875545 | gap_open: 0.18%
- SilverMarginGate: SI=82.510002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -16.94% / slope_proxy: 0.017444
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
- close: 47.665001 | RSI14: 57.006966 | ATR14%: 12.41%
- MA20 gap: 14.18% | MA50 gap: 28.54% | MA200 gap: 245.59%
- vol_ratio(Volume/Vol20): 0.767618 | gap_open: 3.71%
- RS vs SILJ gap: 31.87% / slope_proxy: 0.248235
- RS vs GDXJ gap: 33.69% / slope_proxy: 0.065444
- Checks:
  - trend_ok: **True**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- Trigger(Breakout/Retest)=FALSE
