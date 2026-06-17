# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, EXK, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-17 15:01:15**
- 데이터 기준일(일봉): **2026-06-17**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-16** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 731.35
- Weekly RSI14: **69.60**
- 52W MA: 614.82 / gap: **18.95%**
- 104W MA gap: **32.23%**
- 52W MA 13W slope: **8.25%**
- VXN: **26.95** / 5D change: -2.83

## Daily trigger: 실제 매수 타이밍

- QQQ close: 731.35
- Daily RSI14: **56.83**
- 20D gap: **0.74%**
- 50D gap: **5.89%**
- 200D gap: **16.66%**
- MACD hist: -2.1430 / change: 0.4430
- ATR14%: **2.04%**
- 20D high drawdown: **-1.98%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-17**
- 실행시간(UTC): **2026-06-17 15:00:50**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -15.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -1.0 bp
- 10Y Real Yield (DFII10): 2.15 / 4주 변화 2.0 bp
- VIX (VIXCLS): 16.41
- NFCI: -0.505

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.211206
- MA60: 9.134644
- gap: 0.84%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.458707
- MA60: 0.336213
- gap: 36.43%
- MA60_slope_proxy: 0.066717
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-17**
- 실행시간(UTC): **2026-06-17 15:00:52**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **True**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 103.62 bp / 4주 변화 -31.64 bp
- CURVE_10s5s: 47.87 bp / 4주 변화 0.57 bp

## NWG Price
- close: 635.8
- MA50: 591.0411 / gap50: 7.57%
- MA200: 590.9563 / gap200: 7.59%

## Relative Strength
- RS vs FTSE gap: 7.51% / slope_proxy: 0.000449
- RS vs Peers gap: -0.74% / slope_proxy: -0.0201

## Why not today?
- CurveGreen=FALSE
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-17 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 77.29 / 5D -14.15%
- Brent ref (BZ=F): 80.97 / 5D -13.03%
- Brent Tier: **80-90**
- Brent-WTI spread: 3.68
- Gas ref (NG=F): 3.16 / 5D -0.82%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 53.61
- MA20 / MA60 / MA200: 56.96 / 58.08 / 48.71
- gap20 / gap60: -5.88% / -7.69%
- 5D return: -6.11%
- 20D high/low: 59.37 / 53.61

### Relative Strength

- ratio: 0.973312
- ratio_MA60: 0.999819
- ratio_gap: -2.65%
- ratio_slope_proxy(20d): 0.005833

### Volume (if available)

- volume: 2042453.00
- volume_MA20: 10144287.65
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.04
- MA20 / MA60 / MA200: 18.39 / 19.85 / 15.34
- gap20 / gap60: -7.34% / -14.18%
- 5D return: -5.94%
- 20D high/low: 19.88 / 17.04

### Relative Strength

- ratio: 0.486436
- ratio_MA60: 0.530485
- ratio_gap: -8.30%
- ratio_slope_proxy(20d): 0.013865

### Volume (if available)

- volume: 3365585.00
- volume_MA20: 14819704.25
- volume_ratio: 0.23

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.61
- MA20 / MA60 / MA200: 6.20 / 6.44 / 5.03
- gap20 / gap60: -9.54% / -12.92%
- 5D return: -6.62%
- 20D high/low: 7.34 / 5.59

### Relative Strength

- ratio: 0.013841
- ratio_MA60: 0.015224
- ratio_gap: -9.09%
- ratio_slope_proxy(20d): -0.000606

### Volume (if available)

- volume: 6871375.00
- volume_MA20: 27809973.75
- volume_ratio: 0.25

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

- close: 10.99
- MA20 / MA60 / MA200: 12.63 / 13.26 / 10.83
- gap20 / gap60: -13.02% / -17.13%
- 5D return: -17.19%
- 20D high/low: 14.01 / 10.99

### Relative Strength

- ratio: 0.048479
- ratio_MA60: 0.052055
- ratio_gap: -6.87%
- ratio_slope_proxy(20d): 0.001786

### Volume (if available)

- volume: 4331033.00
- volume_MA20: 13820741.65
- volume_ratio: 0.31

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-17**
- 실행시간(UTC): **2026-06-17 15:01:06**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.75
- 10Y Real Yield 4주 변화: 2.0 bp / latest 2.15
- VIX: 16.41
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 7.81% / slope_proxy: -0.005032
- GDXJ/GLD gap: 4.77% / slope_proxy: -0.005392

## VZLA (Vizsla Silver)
- close: 3.765 | RSI14: 55.012614 | ATR14%: 6.47%
- MA20 gap: 4.46% | MA50 gap: 7.23% | MA200 gap: -11.48%
- vol_ratio(Volume/Vol20): 0.301841 | gap_open: 1.37%
- RS vs SILJ gap: 7.05% / slope_proxy: 0.004377
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 8.08 | RSI14: 54.260701 | ATR14%: 7.80%
- MA20 gap: 7.30% | MA50 gap: -1.41% | MA200 gap: -4.70%
- vol_ratio(Volume/Vol20): 0.161171 | gap_open: 3.84%
- SilverMarginGate: SI=70.510002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.97% / slope_proxy: -0.011346
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
- close: 26.700001 | RSI14: 39.420316 | ATR14%: 10.35%
- MA20 gap: -10.92% | MA50 gap: -24.59% | MA200 gap: 5.22%
- vol_ratio(Volume/Vol20): 0.186581 | gap_open: 6.25%
- RS vs SILJ gap: -24.71% / slope_proxy: -0.063719
- RS vs GDXJ gap: -23.24% / slope_proxy: -0.013743
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-06-17 15:01:14**
- 데이터 기준일(주가): **2026-06-17**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, EXK, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 -0.09 bp-ish / 2026-06-16
- IG OAS: 0.75 / 4주 변화 0.00 bp-ish / 2026-06-16
- 10Y Real Yield: 2.15 / 4주 변화 0.05 bp-ish / 2026-06-15
- VIX: 16.41 / 4주 변화 -1.65 / 2026-06-16
- NFCI: -0.51 / 4주 변화 0.06 / 2026-06-12

### Leadership ratios

- GDX/GLD: gap 4.54% / slope_proxy 7.79%
- GDXJ/GLD: gap 4.77% / slope_proxy 8.03%
- SILJ/SLV: gap 7.81% / slope_proxy 13.22%
- Gold breadth proxy: above50 23.08%, above200 46.15%, count 13
- Silver breadth proxy: above50 53.85%, above200 76.92%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.44 | RSI14: 51.17 | ATR14%: 6.55%
- MA20/50/200 gap: 5.10% / 7.84% / 29.43%
- 5D return: 17.13% | 20D drawdown: -2.93% | vol_ratio: 0.16
- RS vs GDXJ: gap 11.85% / slope_proxy 0.27%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **73.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.49 | RSI14: 60.29 | ATR14%: 5.47%
- MA20/50/200 gap: 12.37% / 7.96% / 0.04%
- 5D return: 29.57% | 20D drawdown: 0.00% | vol_ratio: 0.43
- RS vs GDXJ: gap 7.88% / slope_proxy 6.94%
- FundamentalScore: 70 | TechnicalScore: 50 | RegimeScore: 55 | OverallScore: **60.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.19 | RSI14: 46.06 | ATR14%: 6.60%
- MA20/50/200 gap: 1.42% / -6.65% / -10.75%
- 5D return: 20.66% | 20D drawdown: -12.20% | vol_ratio: 0.16
- RS vs GDXJ: gap -6.87% / slope_proxy -3.57%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **53.1**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.72 | RSI14: 40.00 | ATR14%: 6.85%
- MA20/50/200 gap: -5.70% / -8.35% / 4.30%
- 5D return: 14.67% | 20D drawdown: -23.56% | vol_ratio: 0.12
- RS vs GDXJ: gap -5.05% / slope_proxy -22.84%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **41.0**
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
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 6.11 | RSI14: 50.71 | ATR14%: 7.20%
- MA20/50/200 gap: 8.62% / 2.92% / 9.64%
- 5D return: 33.81% | 20D drawdown: -4.90% | vol_ratio: 0.29
- RS vs SILJ: gap 3.08% / slope_proxy 0.52%
- FundamentalScore: 68 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **68.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.53 | RSI14: 48.07 | ATR14%: 6.47%
- MA20/50/200 gap: 5.64% / 0.67% / 1.15%
- 5D return: 28.50% | 20D drawdown: -4.36% | vol_ratio: 0.30
- RS vs SILJ: gap -0.05% / slope_proxy -1.71%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **65.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.26 | RSI14: 51.21 | ATR14%: 6.95%
- MA20/50/200 gap: 9.38% / 5.89% / 11.97%
- 5D return: 32.57% | 20D drawdown: -2.09% | vol_ratio: 0.44
- RS vs SILJ: gap 6.42% / slope_proxy 4.13%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **64.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 21.55 | RSI14: 57.24 | ATR14%: 6.64%
- MA20/50/200 gap: 14.15% / 17.22% / 42.56%
- 5D return: 34.02% | 20D drawdown: 0.00% | vol_ratio: 0.33
- RS vs SILJ: gap 20.47% / slope_proxy 21.16%
- FundamentalScore: 86 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **71.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.77 | RSI14: 53.35 | ATR14%: 7.01%
- MA20/50/200 gap: 4.46% / 7.23% / -11.48%
- 5D return: 13.06% | 20D drawdown: -8.84% | vol_ratio: 0.30
- RS vs SILJ: gap 7.05% / slope_proxy 7.27%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **61.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.18 | RSI14: 47.50 | ATR14%: 5.65%
- MA20/50/200 gap: 4.39% / -3.49% / -3.01%
- 5D return: 22.31% | 20D drawdown: -3.46% | vol_ratio: 0.29
- RS vs SILJ: gap -5.41% / slope_proxy -2.44%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **55.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.08 | RSI14: 52.79 | ATR14%: 7.89%
- MA20/50/200 gap: 7.30% / -1.41% / -4.70%
- 5D return: 32.46% | 20D drawdown: -3.58% | vol_ratio: 0.16
- RS vs SILJ: gap -1.97% / slope_proxy -8.81%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **53.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 26.70 | RSI14: 36.35 | ATR14%: 9.83%
- MA20/50/200 gap: -10.92% / -24.59% / 5.22%
- 5D return: 7.44% | 20D drawdown: -21.62% | vol_ratio: 0.19
- RS vs SILJ: gap -24.71% / slope_proxy -25.27%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
