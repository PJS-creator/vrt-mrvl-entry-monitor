# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-05-27 03:01:12**
- 데이터 기준일(일봉): **2026-05-26**
- 데이터 기준일(주봉): **2026-05-25**
- VXN 기준일: **2026-05-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 730.28
- Weekly RSI14: **76.39**
- 52W MA: 603.48 / gap: **21.01%**
- 104W MA gap: **33.80%**
- 52W MA 13W slope: **7.46%**
- VXN: **22.82** / 5D change: -2.51

## Daily trigger: 실제 매수 타이밍

- QQQ close: 730.28
- Daily RSI14: **75.34**
- 20D gap: **4.59%**
- 50D gap: **13.26%**
- 200D gap: **18.86%**
- MACD hist: -0.7131 / change: 0.6441
- ATR14%: **1.49%**
- 20D high drawdown: **0.00%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-26**
- 실행시간(UTC): **2026-05-27 03:00:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.74 / 4주 변화 -10.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.16 / 4주 변화 27.0 bp
- VIX (VIXCLS): 16.59
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.302413
- MA60: 8.846751
- gap: 5.15%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.345866
- MA60: 0.279216
- gap: 23.87%
- MA60_slope_proxy: 0.041169
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-26**
- 실행시간(UTC): **2026-05-27 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 117.93 bp / 4주 변화 5.83 bp
- CURVE_10s5s: 45.78 bp / 4주 변화 -0.81 bp

## NWG Price
- close: 596.4
- MA50: 575.8703 / gap50: 3.56%
- MA200: 586.1851 / gap200: 1.74%

## Relative Strength
- RS vs FTSE gap: 1.86% / slope_proxy: -0.001617
- RS vs Peers gap: -3.75% / slope_proxy: -0.032249

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-27 03:00:53**

## Commodity Regime

- WTI ref (CL=F): 92.30 / 5D -15.06%
- Brent ref (BZ=F): 95.27 / 5D -15.01%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.97
- Gas ref (NG=F): 3.00 / 5D -0.96%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **False**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.46
- MA20 / MA60 / MA200: 57.94 / 58.19 / 47.95
- gap20 / gap60: -0.83% / -1.26%
- 5D return: -3.75%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.993258
- ratio_MA60: 1.001908
- ratio_gap: -0.86%
- ratio_slope_proxy(20d): 0.031990

### Volume (if available)

- volume: 9107368.00
- volume_MA20: 12514198.40
- volume_ratio: 0.73

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.40
- MA20 / MA60 / MA200: 20.66 / 20.02 / 14.95
- gap20 / gap60: -6.10% / -3.12%
- 5D return: -6.28%
- 20D high/low: 22.03 / 19.40

### Relative Strength

- ratio: 0.531652
- ratio_MA60: 0.523591
- ratio_gap: 1.54%
- ratio_slope_proxy(20d): 0.046244

### Volume (if available)

- volume: 16042232.00
- volume_MA20: 17815341.60
- volume_ratio: 0.90

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.48
- MA20 / MA60 / MA200: 6.77 / 6.50 / 4.79
- gap20 / gap60: -4.34% / -0.38%
- 5D return: -14.51%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014621
- ratio_MA60: 0.015775
- ratio_gap: -7.32%
- ratio_slope_proxy(20d): -0.000063

### Volume (if available)

- volume: 32860524.00
- volume_MA20: 37245586.20
- volume_ratio: 0.88

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.89
- MA20 / MA60 / MA200: 13.08 / 13.40 / 10.87
- gap20 / gap60: -1.47% / -3.80%
- 5D return: -9.03%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.055074
- ratio_MA60: 0.051338
- ratio_gap: 7.28%
- ratio_slope_proxy(20d): 0.002848

### Volume (if available)

- volume: 14415483.00
- volume_MA20: 20674679.15
- volume_ratio: 0.70

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-26**
- 실행시간(UTC): **2026-05-27 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.74
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 27.0 bp / latest 2.16
- VIX: 16.59
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -2.79% / slope_proxy: -0.01055
- GDXJ/GLD gap: -0.27% / slope_proxy: -0.005381

## VZLA (Vizsla Silver)
- close: 3.72 | RSI14: 57.502294 | ATR14%: 5.91%
- MA20 gap: 6.39% | MA50 gap: 9.81% | MA200 gap: -12.15%
- vol_ratio(Volume/Vol20): 1.116972 | gap_open: 2.67%
- RS vs SILJ gap: 10.04% / slope_proxy: -0.002467
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
- close: 8.05 | RSI14: 42.850582 | ATR14%: 7.65%
- MA20 gap: -6.02% | MA50 gap: -3.93% | MA200 gap: -2.37%
- vol_ratio(Volume/Vol20): 1.439344 | gap_open: 0.50%
- SilverMarginGate: SI=77.105003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.21% / slope_proxy: -0.015281
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
- close: 33.220001 | RSI14: 41.905278 | ATR14%: 9.59%
- MA20 gap: -10.52% | MA50 gap: -10.28% | MA200 gap: 41.38%
- vol_ratio(Volume/Vol20): 0.708733 | gap_open: 3.65%
- RS vs SILJ gap: -9.69% / slope_proxy: 0.023945
- RS vs GDXJ gap: -7.90% / slope_proxy: 0.007278
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

- 실행시간(UTC): **2026-05-27 03:01:09**
- 데이터 기준일(주가): **2026-05-26**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **True**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.74 / 4주 변화 -0.10 bp-ish / 2026-05-25
- IG OAS: 0.74 / 4주 변화 -0.07 bp-ish / 2026-05-25
- 10Y Real Yield: 2.16 / 4주 변화 0.27 bp-ish / 2026-05-22
- VIX: 16.59 / 4주 변화 -1.43 / 2026-05-25
- NFCI: -0.52 / 4주 변화 0.01 / 2026-05-15

### Leadership ratios

- GDX/GLD: gap -0.14% / slope_proxy 1.86%
- GDXJ/GLD: gap -0.27% / slope_proxy 1.85%
- SILJ/SLV: gap -2.79% / slope_proxy -2.32%
- Gold breadth proxy: above50 30.77%, above200 61.54%, count 13
- Silver breadth proxy: above50 46.15%, above200 84.62%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.62 | RSI14: 62.31 | ATR14%: 6.22%
- MA20/50/200 gap: 8.07% / 17.85% / 37.84%
- 5D return: 1.17% | 20D drawdown: -0.35% | vol_ratio: 1.19
- RS vs GDXJ: gap 23.15% / slope_proxy 14.39%
- FundamentalScore: 88 | TechnicalScore: 100 | RegimeScore: 30 | OverallScore: **80.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.84 | RSI14: 55.96 | ATR14%: 10.68%
- MA20/50/200 gap: -6.55% / 1.22% / 18.45%
- 5D return: -17.12% | 20D drawdown: -26.10% | vol_ratio: 2.48
- RS vs GDXJ: gap 5.73% / slope_proxy 7.04%
- FundamentalScore: 55 | TechnicalScore: 100 | RegimeScore: 30 | OverallScore: **65.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.41 | RSI14: 50.16 | ATR14%: 6.46%
- MA20/50/200 gap: -2.94% / -7.09% / -5.81%
- 5D return: 3.39% | 20D drawdown: -12.91% | vol_ratio: 1.12
- RS vs GDXJ: gap -5.92% / slope_proxy -2.70%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **53.4**
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.38 | RSI14: 55.56 | ATR14%: 5.87%
- MA20/50/200 gap: -1.22% / -1.86% / -4.00%
- 5D return: 5.34% | 20D drawdown: -10.39% | vol_ratio: 0.37
- RS vs GDXJ: gap 0.23% / slope_proxy 7.24%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **51.5**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.73 | RSI14: 57.06 | ATR14%: 7.49%
- MA20/50/200 gap: 1.53% / 11.13% / 30.99%
- 5D return: 1.24% | 20D drawdown: -12.56% | vol_ratio: 0.84
- RS vs SILJ: gap 13.57% / slope_proxy 7.92%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **83.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.60 | RSI14: 57.88 | ATR14%: 8.50%
- MA20/50/200 gap: -1.23% / 0.43% / 4.75%
- 5D return: 1.16% | 20D drawdown: -16.23% | vol_ratio: 0.67
- RS vs SILJ: gap 0.63% / slope_proxy 1.21%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **81.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.90 | RSI14: 58.17 | ATR14%: 7.93%
- MA20/50/200 gap: 0.58% / 2.52% / 9.88%
- 5D return: -0.58% | 20D drawdown: -13.43% | vol_ratio: 0.64
- RS vs SILJ: gap 2.96% / slope_proxy 4.47%
- FundamentalScore: 60 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **71.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.86 | RSI14: 53.79 | ATR14%: 9.59%
- MA20/50/200 gap: -4.91% / -2.41% / 10.02%
- 5D return: 0.86% | 20D drawdown: -20.92% | vol_ratio: 0.92
- RS vs SILJ: gap -5.30% / slope_proxy 0.46%
- FundamentalScore: 68 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **66.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, RelativeStrength(vs SILJ)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.72 | RSI14: 63.84 | ATR14%: 6.27%
- MA20/50/200 gap: 6.39% / 9.81% / -12.15%
- 5D return: 8.77% | 20D drawdown: -3.38% | vol_ratio: 1.12
- RS vs SILJ: gap 10.04% / slope_proxy 5.73%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 75 | OverallScore: **66.7**
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.05 | RSI14: 52.81 | ATR14%: 8.29%
- MA20/50/200 gap: -6.02% / -3.93% / -2.37%
- 5D return: -5.96% | 20D drawdown: -20.69% | vol_ratio: 1.44
- RS vs SILJ: gap -4.21% / slope_proxy -0.70%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **58.8**
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.58 | RSI14: 52.43 | ATR14%: 7.91%
- MA20/50/200 gap: -3.11% / -4.96% / 3.17%
- 5D return: 1.85% | 20D drawdown: -16.48% | vol_ratio: 0.61
- RS vs SILJ: gap -4.23% / slope_proxy -4.21%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 33.22 | RSI14: 46.15 | ATR14%: 10.55%
- MA20/50/200 gap: -10.52% / -10.28% / 41.38%
- 5D return: -4.62% | 20D drawdown: -26.44% | vol_ratio: 0.71
- RS vs SILJ: gap -9.69% / slope_proxy -9.45%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
