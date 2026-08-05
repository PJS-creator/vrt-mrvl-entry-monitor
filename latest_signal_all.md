# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, EXK, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-05 03:01:20**
- 데이터 기준일(일봉): **2026-08-04**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-08-03** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 723.85
- Weekly RSI14: **61.08**
- 52W MA: 634.39 / gap: **14.10%**
- 104W MA gap: **27.30%**
- 52W MA 13W slope: **7.33%**
- VXN: **24.77** / 5D change: -3.88

## Daily trigger: 실제 매수 타이밍

- QQQ close: 723.85
- Daily RSI14: **58.06**
- 20D gap: **3.32%**
- 50D gap: **1.28%**
- 200D gap: **12.23%**
- MACD hist: 1.9429 / change: 2.7361
- ATR14%: **2.22%**
- 20D high drawdown: **-0.23%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-04**
- 실행시간(UTC): **2026-08-05 03:00:52**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.43 / 4주 변화 19.0 bp
- VIX (VIXCLS): 15.86
- NFCI: -0.554

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.453805
- MA60: 9.50852
- gap: -11.09%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.379688
- MA60: 0.386113
- gap: -1.66%
- MA60_slope_proxy: 0.014479
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-03**
- 실행시간(UTC): **2026-08-05 03:00:54**

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
- TERM_SPREAD_10Y_POLICY: 127.57 bp / 4주 변화 26.05 bp
- CURVE_10s5s: 46.88 bp / 4주 변화 -1.83 bp

## NWG Price
- close: 722.8
- MA50: 645.82 / gap50: 11.92%
- MA200: 614.3698 / gap200: 17.65%

## Relative Strength
- RS vs FTSE gap: 10.38% / slope_proxy: 0.002156
- RS vs Peers gap: 3.54% / slope_proxy: -0.001687

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-05 03:01:04**

## Commodity Regime

- WTI ref (CL=F): 74.51 / 5D -5.99%
- Brent ref (BZ=F): 78.30 / 5D -6.89%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.79
- Gas ref (NG=F): 2.69 / 5D 1.20%

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

- close: 55.09
- MA20 / MA60 / MA200: 55.15 / 55.01 / 50.04
- gap20 / gap60: -0.11% / 0.15%
- 5D return: 2.15%
- 20D high/low: 57.60 / 52.30

### Relative Strength

- ratio: 0.941388
- ratio_MA60: 0.968433
- ratio_gap: -2.79%
- ratio_slope_proxy(20d): -0.016747

### Volume (if available)

- volume: 6632981.00
- volume_MA20: 8874724.05
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.72
- MA20 / MA60 / MA200: 18.25 / 18.18 / 16.17
- gap20 / gap60: 2.56% / 2.97%
- 5D return: 3.60%
- 20D high/low: 19.40 / 17.03

### Relative Strength

- ratio: 0.518703
- ratio_MA60: 0.513621
- ratio_gap: 0.99%
- ratio_slope_proxy(20d): -0.005821

### Volume (if available)

- volume: 13718394.00
- volume_MA20: 15061554.70
- volume_ratio: 0.91

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.22
- MA20 / MA60 / MA200: 5.20 / 5.74 / 5.34
- gap20 / gap60: 0.45% / -9.02%
- 5D return: 4.61%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013311
- ratio_MA60: 0.014211
- ratio_gap: -6.33%
- ratio_slope_proxy(20d): -0.000463

### Volume (if available)

- volume: 37407274.00
- volume_MA20: 42768523.70
- volume_ratio: 0.87

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

- close: 12.84
- MA20 / MA60 / MA200: 13.32 / 12.62 / 10.73
- gap20 / gap60: -3.58% / 1.75%
- 5D return: 5.51%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.049905
- ratio_MA60: 0.051289
- ratio_gap: -2.70%
- ratio_slope_proxy(20d): 0.001083

### Volume (if available)

- volume: 11313810.00
- volume_MA20: 16537565.50
- volume_ratio: 0.68

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

- 데이터 기준일(주가): **2026-08-04**
- 실행시간(UTC): **2026-08-05 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.78
- IG OAS 4주 변화: 3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.43
- VIX: 15.86
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 6.04% / slope_proxy: 0.008811
- GDXJ/GLD gap: 1.08% / slope_proxy: -0.008342

## VZLA (Vizsla Silver)
- close: 3.4 | RSI14: 55.131682 | ATR14%: 5.60%
- MA20 gap: 6.45% | MA50 gap: 0.65% | MA200 gap: -17.19%
- vol_ratio(Volume/Vol20): 1.337957 | gap_open: 2.76%
- RS vs SILJ gap: 3.84% / slope_proxy: 0.006085
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
- close: 7.2 | RSI14: 58.684479 | ATR14%: 6.42%
- MA20 gap: 11.88% | MA50 gap: 5.39% | MA200 gap: -14.59%
- vol_ratio(Volume/Vol20): 1.200868 | gap_open: 2.97%
- SilverMarginGate: SI=61.005001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.88% / slope_proxy: -0.005324
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
- close: 22.360001 | RSI14: 52.412805 | ATR14%: 7.69%
- MA20 gap: 9.39% | MA50 gap: -7.86% | MA200 gap: -19.87%
- vol_ratio(Volume/Vol20): 0.896334 | gap_open: 3.69%
- RS vs SILJ gap: -10.88% / slope_proxy: -0.145923
- RS vs GDXJ gap: -11.86% / slope_proxy: -0.034908
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

- 실행시간(UTC): **2026-08-05 03:01:19**
- 데이터 기준일(주가): **2026-08-04**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, EXK, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.78 / 4주 변화 0.06 bp-ish / 2026-08-03
- IG OAS: 0.78 / 4주 변화 0.03 bp-ish / 2026-08-03
- 10Y Real Yield: 2.43 / 4주 변화 0.19 bp-ish / 2026-08-03
- VIX: 15.86 / 4주 변화 0.29 / 2026-08-03
- NFCI: -0.55 / 4주 변화 -0.07 / 2026-07-24

### Leadership ratios

- GDX/GLD: gap 1.04% / slope_proxy 6.05%
- GDXJ/GLD: gap 1.08% / slope_proxy 6.69%
- SILJ/SLV: gap 6.04% / slope_proxy 4.70%
- Gold breadth proxy: above50 15.38%, above200 0.00%, count 13
- Silver breadth proxy: above50 30.77%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.82 | RSI14: 73.22 | ATR14%: 5.22%
- MA20/50/200 gap: 11.21% / 4.32% / -14.86%
- 5D return: 7.58% | 20D drawdown: 0.00% | vol_ratio: 1.87
- RS vs GDXJ: gap 4.54% / slope_proxy 6.79%
- FundamentalScore: 82 | TechnicalScore: 75 | RegimeScore: 55 | OverallScore: **74.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.48 | RSI14: 55.00 | ATR14%: 4.90%
- MA20/50/200 gap: 3.22% / -1.68% / 8.79%
- 5D return: 2.89% | 20D drawdown: -3.61% | vol_ratio: 1.04
- RS vs GDXJ: gap -0.04% / slope_proxy -6.08%
- FundamentalScore: 88 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **69.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.25 | RSI14: 65.31 | ATR14%: 5.49%
- MA20/50/200 gap: 11.16% / 2.54% / -15.32%
- 5D return: 9.65% | 20D drawdown: 0.00% | vol_ratio: 1.45
- RS vs GDXJ: gap 3.65% / slope_proxy 2.82%
- FundamentalScore: 70 | TechnicalScore: 75 | RegimeScore: 55 | OverallScore: **68.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.79 | RSI14: 40.00 | ATR14%: 6.62%
- MA20/50/200 gap: -4.23% / 0.97% / -1.02%
- 5D return: -4.28% | 20D drawdown: -13.11% | vol_ratio: 1.72
- RS vs GDXJ: gap 1.35% / slope_proxy -0.14%
- FundamentalScore: 55 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **46.2**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.33 | RSI14: 54.91 | ATR14%: 5.87%
- MA20/50/200 gap: 5.99% / -0.25% / -12.82%
- 5D return: 7.48% | 20D drawdown: -0.12% | vol_ratio: 1.31
- RS vs SILJ: gap 0.64% / slope_proxy 1.12%
- FundamentalScore: 82 | TechnicalScore: 75 | RegimeScore: 55 | OverallScore: **74.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.20 | RSI14: 61.97 | ATR14%: 6.24%
- MA20/50/200 gap: 11.88% / 5.39% / -14.59%
- 5D return: 11.46% | 20D drawdown: 0.00% | vol_ratio: 1.20
- RS vs SILJ: gap 4.88% / slope_proxy 8.14%
- FundamentalScore: 74 | TechnicalScore: 75 | RegimeScore: 55 | OverallScore: **70.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 22.90 | RSI14: 62.51 | ATR14%: 6.04%
- MA20/50/200 gap: 15.50% / 18.42% / 39.57%
- 5D return: 18.04% | 20D drawdown: 0.00% | vol_ratio: 2.41
- RS vs SILJ: gap 22.94% / slope_proxy 12.25%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.40 | RSI14: 57.04 | ATR14%: 5.38%
- MA20/50/200 gap: 6.45% / 0.65% / -17.19%
- 5D return: 6.58% | 20D drawdown: -0.58% | vol_ratio: 1.34
- RS vs SILJ: gap 3.84% / slope_proxy 7.65%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **62.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.39 | RSI14: 57.32 | ATR14%: 6.75%
- MA20/50/200 gap: 8.78% / -8.43% / -23.30%
- 5D return: 13.14% | 20D drawdown: -1.57% | vol_ratio: 1.60
- RS vs SILJ: gap -8.76% / slope_proxy -2.27%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.39 | RSI14: 49.50 | ATR14%: 5.42%
- MA20/50/200 gap: 2.51% / -1.46% / -15.98%
- 5D return: 5.77% | 20D drawdown: -2.72% | vol_ratio: 0.80
- RS vs SILJ: gap -0.31% / slope_proxy -4.42%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **51.4**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.91 | RSI14: 49.70 | ATR14%: 6.44%
- MA20/50/200 gap: 3.19% / -4.12% / -11.19%
- 5D return: 7.45% | 20D drawdown: -5.59% | vol_ratio: 1.17
- RS vs SILJ: gap -2.52% / slope_proxy -3.34%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **48.5**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 22.36 | RSI14: 55.43 | ATR14%: 7.08%
- MA20/50/200 gap: 9.39% / -7.86% / -19.87%
- 5D return: 11.13% | 20D drawdown: 0.00% | vol_ratio: 0.90
- RS vs SILJ: gap -10.88% / slope_proxy 0.80%
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
