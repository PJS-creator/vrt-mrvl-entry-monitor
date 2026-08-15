# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-15 15:01:09**
- 데이터 기준일(일봉): **2026-08-14**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-13** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 731.07
- Weekly RSI14: **62.31**
- 52W MA: 637.38 / gap: **14.70%**
- 104W MA gap: **28.01%**
- 52W MA 13W slope: **7.17%**
- VXN: **21.23** / 5D change: -2.72

## Daily trigger: 실제 매수 타이밍

- QQQ close: 731.07
- Daily RSI14: **59.60**
- 20D gap: **3.83%**
- 50D gap: **2.57%**
- 200D gap: **12.55%**
- MACD hist: 4.3638 / change: -0.1172
- ATR14%: **1.73%**
- 20D high drawdown: **-0.14%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-15 15:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.39 / 4주 변화 4.0 bp
- VIX (VIXCLS): 14.63
- NFCI: -0.549

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.021799
- MA60: 9.311917
- gap: -3.12%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.377701
- MA60: 0.394612
- gap: -4.29%
- MA60_slope_proxy: 0.014369
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-15 15:00:47**

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
- TERM_SPREAD_10Y_POLICY: 120.93 bp / 4주 변화 1.94 bp
- CURVE_10s5s: 47.78 bp / 4주 변화 0.58 bp

## NWG Price
- close: 707.8
- MA50: 666.5408 / gap50: 6.19%
- MA200: 621.1876 / gap200: 13.94%

## Relative Strength
- RS vs FTSE gap: 6.46% / slope_proxy: 0.002982
- RS vs Peers gap: 3.39% / slope_proxy: 0.012361

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-15 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 82.40 / 5D 5.40%
- Brent ref (BZ=F): 88.52 / 5D 5.95%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.12
- Gas ref (NG=F): 2.73 / 5D 2.67%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.36
- MA20 / MA60 / MA200: 56.53 / 55.05 / 50.69
- gap20 / gap60: 3.23% / 6.01%
- 5D return: 4.38%
- 20D high/low: 59.06 / 53.81

### Relative Strength

- ratio: 0.942659
- ratio_MA60: 0.965417
- ratio_gap: -2.36%
- ratio_slope_proxy(20d): -0.013418

### Volume (if available)

- volume: 6743600.00
- volume_MA20: 8478635.00
- volume_ratio: 0.80

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.88
- MA20 / MA60 / MA200: 18.45 / 17.91 / 16.44
- gap20 / gap60: -3.08% / -0.17%
- 5D return: -0.45%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.526967
- ratio_MA60: 0.510549
- ratio_gap: 3.22%
- ratio_slope_proxy(20d): -0.007337

### Volume (if available)

- volume: 10870100.00
- volume_MA20: 14767915.00
- volume_ratio: 0.74

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.76
- MA20 / MA60 / MA200: 5.32 / 5.56 / 5.42
- gap20 / gap60: 8.18% / 3.65%
- 5D return: 9.51%
- 20D high/low: 5.81 / 4.95

### Relative Strength

- ratio: 0.013671
- ratio_MA60: 0.013944
- ratio_gap: -1.96%
- ratio_slope_proxy(20d): -0.000518

### Volume (if available)

- volume: 46813700.00
- volume_MA20: 46035090.00
- volume_ratio: 1.02

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.99
- MA20 / MA60 / MA200: 13.56 / 12.66 / 10.90
- gap20 / gap60: 3.16% / 10.48%
- 5D return: 5.51%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.051502
- ratio_MA60: 0.050967
- ratio_gap: 1.05%
- ratio_slope_proxy(20d): 0.000392

### Volume (if available)

- volume: 13456400.00
- volume_MA20: 15779350.00
- volume_ratio: 0.85

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-15 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 1.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.39
- VIX: 14.63
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 9.32% / slope_proxy: 0.015747
- GDXJ/GLD gap: 8.99% / slope_proxy: -0.003101

## VZLA (Vizsla Silver)
- close: 3.76 | RSI14: 61.28576 | ATR14%: 4.91%
- MA20 gap: 9.08% | MA50 gap: 11.66% | MA200 gap: -7.90%
- vol_ratio(Volume/Vol20): 0.90165 | gap_open: 0.80%
- RS vs SILJ gap: -1.08% / slope_proxy: 0.005482
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

## SCZM (Santacruz Silver)
- close: 8.85 | RSI14: 70.455669 | ATR14%: 5.74%
- MA20 gap: 23.04% | MA50 gap: 28.37% | MA200 gap: 3.98%
- vol_ratio(Volume/Vol20): 0.66613 | gap_open: 1.49%
- SilverMarginGate: SI=64.987999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.53% / slope_proxy: -0.002692
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
- close: 27.07 | RSI14: 62.912349 | ATR14%: 6.73%
- MA20 gap: 19.02% | MA50 gap: 16.52% | MA200 gap: -5.52%
- vol_ratio(Volume/Vol20): 0.701832 | gap_open: 3.20%
- RS vs SILJ gap: -1.13% / slope_proxy: -0.129974
- RS vs GDXJ gap: -3.11% / slope_proxy: -0.033659
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

- 실행시간(UTC): **2026-08-15 15:01:07**
- 데이터 기준일(주가): **2026-08-14**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 0.00 bp-ish / 2026-08-13
- IG OAS: 0.79 / 4주 변화 0.01 bp-ish / 2026-08-13
- 10Y Real Yield: 2.39 / 4주 변화 0.04 bp-ish / 2026-08-13
- VIX: 14.63 / 4주 변화 -2.10 / 2026-08-13
- NFCI: -0.55 / 4주 변화 -0.09 / 2026-08-07

### Leadership ratios

- GDX/GLD: gap 8.34% / slope_proxy 16.45%
- GDXJ/GLD: gap 8.99% / slope_proxy 17.96%
- SILJ/SLV: gap 9.32% / slope_proxy 9.69%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 100.00%, above200 53.85%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.12 | RSI14: 83.49 | ATR14%: 5.57%
- MA20/50/200 gap: 24.82% / 30.22% / 43.90%
- 5D return: 6.08% | 20D drawdown: 0.00% | vol_ratio: 1.32
- RS vs GDXJ: gap 13.69% / slope_proxy 13.35%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **77.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.01 | RSI14: 91.18 | ATR14%: 4.83%
- MA20/50/200 gap: 18.80% / 24.96% / 2.19%
- 5D return: 4.47% | 20D drawdown: 0.00% | vol_ratio: 0.68
- RS vs GDXJ: gap 8.15% / slope_proxy 10.57%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **69.4**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.53 | RSI14: 82.81 | ATR14%: 5.23%
- MA20/50/200 gap: 24.59% / 24.67% / 3.63%
- 5D return: 12.50% | 20D drawdown: 0.00% | vol_ratio: 2.29
- RS vs GDXJ: gap 8.72% / slope_proxy 14.32%
- FundamentalScore: 70 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **69.2**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.33 | RSI14: 69.03 | ATR14%: 5.58%
- MA20/50/200 gap: 18.85% / 29.47% / 26.66%
- 5D return: 9.91% | 20D drawdown: 0.00% | vol_ratio: 2.91
- RS vs GDXJ: gap 11.92% / slope_proxy 2.78%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **62.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 25.92 | RSI14: 68.83 | ATR14%: 6.19%
- MA20/50/200 gap: 13.95% / 26.58% / 52.26%
- 5D return: -4.67% | 20D drawdown: -7.56% | vol_ratio: 1.97
- RS vs SILJ: gap 15.25% / slope_proxy 11.71%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.66 | RSI14: 78.10 | ATR14%: 5.26%
- MA20/50/200 gap: 22.45% / 26.71% / 10.92%
- 5D return: 11.74% | 20D drawdown: 0.00% | vol_ratio: 0.83
- RS vs SILJ: gap 11.93% / slope_proxy 12.95%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **69.4**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.85 | RSI14: 81.84 | ATR14%: 6.05%
- MA20/50/200 gap: 23.04% / 28.37% / 3.98%
- 5D return: 11.04% | 20D drawdown: -1.45% | vol_ratio: 0.67
- RS vs SILJ: gap 12.53% / slope_proxy 18.70%
- FundamentalScore: 74 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **65.8**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.02 | RSI14: 67.92 | ATR14%: 5.63%
- MA20/50/200 gap: 13.72% / 14.12% / 4.55%
- 5D return: 2.03% | 20D drawdown: -4.88% | vol_ratio: 1.00
- RS vs SILJ: gap 0.79% / slope_proxy 0.16%
- FundamentalScore: 60 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **59.5**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 18.37 | RSI14: 67.71 | ATR14%: 5.15%
- MA20/50/200 gap: 15.81% / 17.64% / -0.56%
- 5D return: 9.02% | 20D drawdown: 0.00% | vol_ratio: 0.99
- RS vs SILJ: gap 4.06% / slope_proxy 2.16%
- FundamentalScore: 78 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **58.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.76 | RSI14: 65.28 | ATR14%: 4.87%
- MA20/50/200 gap: 9.08% / 11.66% / -7.90%
- 5D return: 0.53% | 20D drawdown: -3.09% | vol_ratio: 0.90
- RS vs SILJ: gap -1.08% / slope_proxy -5.14%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **52.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.24 | RSI14: 70.97 | ATR14%: 5.81%
- MA20/50/200 gap: 18.83% / 13.10% / -8.92%
- 5D return: 4.59% | 20D drawdown: 0.00% | vol_ratio: 1.08
- RS vs SILJ: gap -2.18% / slope_proxy 10.75%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 27.07 | RSI14: 74.52 | ATR14%: 6.68%
- MA20/50/200 gap: 19.02% / 16.52% / -5.52%
- 5D return: 2.00% | 20D drawdown: -1.67% | vol_ratio: 0.70
- RS vs SILJ: gap -1.13% / slope_proxy 14.67%
- FundamentalScore: 42 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **33.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
