# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-03 15:01:08**
- 데이터 기준일(일봉): **2026-07-02**
- 데이터 기준일(주봉): **2026-06-29**
- VXN 기준일: **2026-07-01** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 712.60
- Weekly RSI14: **62.06**
- 52W MA: 620.54 / gap: **14.84%**
- 104W MA gap: **27.94%**
- 52W MA 13W slope: **8.41%**
- VXN: **27.69** / 5D change: -2.49

## Daily trigger: 실제 매수 타이밍

- QQQ close: 712.60
- Daily RSI14: **48.25**
- 20D gap: **-1.12%**
- 50D gap: **0.58%**
- 200D gap: **12.49%**
- MACD hist: -2.1195 / change: -0.6487
- ATR14%: **2.32%**
- 20D high drawdown: **-4.12%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-02**
- 실행시간(UTC): **2026-07-03 15:00:47**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.74 / 4주 변화 -1.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.25 / 4주 변화 14.0 bp
- VIX (VIXCLS): 16.59
- NFCI: -0.504

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.654032
- MA60: 9.41465
- gap: 2.54%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.414138
- MA60: 0.367389
- gap: 12.72%
- MA60_slope_proxy: 0.070551
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-03**
- 실행시간(UTC): **2026-07-03 15:00:49**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 99.46 bp / 4주 변화 -14.63 bp
- CURVE_10s5s: 47.63 bp / 4주 변화 2.96 bp

## NWG Price
- close: 678.8
- MA50: 603.5011 / gap50: 12.48%
- MA200: 599.3967 / gap200: 13.25%

## Relative Strength
- RS vs FTSE gap: 9.63% / slope_proxy: 0.002091
- RS vs Peers gap: 3.81% / slope_proxy: -0.009874

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-03 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 68.69 / 5D -0.78%
- Brent ref (BZ=F): 72.05 / 5D 0.08%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.36
- Gas ref (NG=F): 3.24 / 5D 0.22%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 48.91
- MA20 / MA60 / MA200: 53.09 / 55.91 / 48.96
- gap20 / gap60: -7.87% / -12.52%
- 5D return: -4.49%
- 20D high/low: 58.40 / 47.94

### Relative Strength

- ratio: 0.919015
- ratio_MA60: 0.988369
- ratio_gap: -7.02%
- ratio_slope_proxy(20d): -0.021680

### Volume (if available)

- volume: 8548700.00
- volume_MA20: 9736315.00
- volume_ratio: 0.88

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.11
- MA20 / MA60 / MA200: 17.09 / 19.23 / 15.54
- gap20 / gap60: -5.76% / -16.22%
- 5D return: -2.48%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.467906
- ratio_MA60: 0.520521
- ratio_gap: -10.11%
- ratio_slope_proxy(20d): -0.010289

### Volume (if available)

- volume: 12175700.00
- volume_MA20: 14131640.00
- volume_ratio: 0.86

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.06
- MA20 / MA60 / MA200: 5.53 / 6.18 / 5.13
- gap20 / gap60: -8.46% / -18.17%
- 5D return: -2.88%
- 20D high/low: 6.25 / 4.87

### Relative Strength

- ratio: 0.014071
- ratio_MA60: 0.014755
- ratio_gap: -4.64%
- ratio_slope_proxy(20d): -0.000873

### Volume (if available)

- volume: 26459300.00
- volume_MA20: 33752310.00
- volume_ratio: 0.78

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.13
- MA20 / MA60 / MA200: 11.72 / 12.41 / 10.72
- gap20 / gap60: -5.00% / -10.32%
- 5D return: 2.77%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045249
- ratio_MA60: 0.050404
- ratio_gap: -10.23%
- ratio_slope_proxy(20d): -0.001555

### Volume (if available)

- volume: 6823100.00
- volume_MA20: 13301975.00
- volume_ratio: 0.51

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-03**
- 실행시간(UTC): **2026-07-03 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.74
- IG OAS 4주 변화: 2.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.25
- VIX: 16.59
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 8.38% / slope_proxy: 0.007288
- GDXJ/GLD gap: -2.34% / slope_proxy: -0.0019

## VZLA (Vizsla Silver)
- close: 3.34 | RSI14: 46.500424 | ATR14%: 6.42%
- MA20 gap: -2.14% | MA50 gap: -4.65% | MA200 gap: -21.02%
- vol_ratio(Volume/Vol20): 1.351179 | gap_open: 3.99%
- RS vs SILJ gap: 5.24% / slope_proxy: 0.004781
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.69 | RSI14: 43.567324 | ATR14%: 7.64%
- MA20 gap: -1.35% | MA50 gap: -14.11% | MA200 gap: -21.43%
- vol_ratio(Volume/Vol20): 1.248563 | gap_open: 3.19%
- SilverMarginGate: SI=62.799999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.73% / slope_proxy: -0.008399
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
- close: 23.620001 | RSI14: 38.953731 | ATR14%: 9.42%
- MA20 gap: -4.92% | MA50 gap: -25.77% | MA200 gap: -10.42%
- vol_ratio(Volume/Vol20): 0.685231 | gap_open: 4.51%
- RS vs SILJ gap: -20.98% / slope_proxy: -0.089211
- RS vs GDXJ gap: -19.84% / slope_proxy: -0.019533
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


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-07-03 15:01:07**
- 데이터 기준일(주가): **2026-07-03**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.74 / 4주 변화 -0.01 bp-ish / 2026-07-01
- IG OAS: 0.76 / 4주 변화 0.02 bp-ish / 2026-07-01
- 10Y Real Yield: 2.25 / 4주 변화 0.18 bp-ish / 2026-07-01
- VIX: 16.59 / 4주 변화 0.53 / 2026-07-01
- NFCI: -0.50 / 4주 변화 0.05 / 2026-06-26

### Leadership ratios

- GDX/GLD: gap -2.27% / slope_proxy -1.27%
- GDXJ/GLD: gap -2.34% / slope_proxy 0.03%
- SILJ/SLV: gap 8.38% / slope_proxy 9.86%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.65 | RSI14: 55.40 | ATR14%: 5.76%
- MA20/50/200 gap: 0.52% / -2.86% / 14.44%
- 5D return: 4.65% | 20D drawdown: -8.82% | vol_ratio: 0.54
- RS vs GDXJ: gap 8.55% / slope_proxy 1.20%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **59.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.64 | RSI14: 49.79 | ATR14%: 5.78%
- MA20/50/200 gap: 2.80% / -8.70% / -18.63%
- 5D return: 13.71% | 20D drawdown: -8.29% | vol_ratio: 0.08
- RS vs GDXJ: gap -4.79% / slope_proxy -5.44%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **48.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.72 | RSI14: 54.93 | ATR14%: 5.52%
- MA20/50/200 gap: 7.10% / -4.64% / 0.93%
- 5D return: 19.44% | 20D drawdown: -1.71% | vol_ratio: 0.24
- RS vs GDXJ: gap 1.22% / slope_proxy -6.51%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **44.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.27 | RSI14: 47.95 | ATR14%: 7.71%
- MA20/50/200 gap: 1.97% / -4.31% / -15.77%
- 5D return: 11.40% | 20D drawdown: -13.61% | vol_ratio: 0.18
- RS vs GDXJ: gap 1.58% / slope_proxy -1.10%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **42.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 19.62 | RSI14: 58.86 | ATR14%: 7.51%
- MA20/50/200 gap: 4.79% / 5.05% / 26.55%
- 5D return: 7.33% | 20D drawdown: -6.79% | vol_ratio: 0.91
- RS vs SILJ: gap 16.53% / slope_proxy 11.55%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.56 | RSI14: 55.99 | ATR14%: 6.56%
- MA20/50/200 gap: 2.41% / -6.53% / -10.17%
- 5D return: 6.47% | 20D drawdown: -7.96% | vol_ratio: 0.76
- RS vs SILJ: gap 1.93% / slope_proxy 2.44%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **61.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.33 | RSI14: 61.06 | ATR14%: 5.57%
- MA20/50/200 gap: 5.44% / -4.14% / -9.18%
- 5D return: 7.79% | 20D drawdown: -2.97% | vol_ratio: 0.90
- RS vs SILJ: gap 3.50% / slope_proxy 7.52%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **60.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.69 | RSI14: 50.00 | ATR14%: 7.37%
- MA20/50/200 gap: -1.35% / -14.11% / -21.43%
- 5D return: 3.88% | 20D drawdown: -16.06% | vol_ratio: 1.25
- RS vs SILJ: gap -6.73% / slope_proxy -2.33%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **54.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.34 | RSI14: 44.25 | ATR14%: 6.00%
- MA20/50/200 gap: -2.14% / -4.65% / -21.02%
- 5D return: 6.71% | 20D drawdown: -13.02% | vol_ratio: 1.35
- RS vs SILJ: gap 5.24% / slope_proxy -3.62%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **53.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.89 | RSI14: 48.20 | ATR14%: 8.24%
- MA20/50/200 gap: -3.60% / -14.29% / -13.90%
- 5D return: 2.09% | 20D drawdown: -16.84% | vol_ratio: 1.03
- RS vs SILJ: gap -6.21% / slope_proxy -6.90%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **52.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.57 | RSI14: 59.19 | ATR14%: 6.93%
- MA20/50/200 gap: 5.22% / -1.28% / -0.12%
- 5D return: 12.12% | 20D drawdown: -5.47% | vol_ratio: 0.83
- RS vs SILJ: gap 7.30% / slope_proxy 7.06%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **52.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 23.62 | RSI14: 43.95 | ATR14%: 8.16%
- MA20/50/200 gap: -4.92% / -25.77% / -10.42%
- 5D return: 7.90% | 20D drawdown: -22.10% | vol_ratio: 0.69
- RS vs SILJ: gap -20.98% / slope_proxy -13.67%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **35.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
