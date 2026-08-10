# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-10 23:16:28**
- 데이터 기준일(일봉): **2026-08-10**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-07** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 720.87
- Weekly RSI14: **60.36**
- 52W MA: 637.18 / gap: **13.13%**
- 104W MA gap: **26.24%**
- 52W MA 13W slope: **7.14%**
- VXN: **22.82** / 5D change: -3.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 720.87
- Daily RSI14: **56.21**
- 20D gap: **2.86%**
- 50D gap: **0.96%**
- 200D gap: **11.37%**
- MACD hist: 4.5344 / change: 0.1133
- ATR14%: **1.97%**
- 20D high drawdown: **-0.41%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 23:16:02**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.4 / 4주 변화 8.0 bp
- VIX (VIXCLS): 14.9
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.586761
- MA60: 9.397656
- gap: -8.63%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.366274
- MA60: 0.39078
- gap: -6.27%
- MA60_slope_proxy: 0.013063
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-07**
- 실행시간(UTC): **2026-08-10 23:16:04**

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
- TERM_SPREAD_10Y_POLICY: 116.29 bp / 4주 변화 2.09 bp
- CURVE_10s5s: 48.25 bp / 4주 변화 -0.2 bp

## NWG Price
- close: 712.4
- MA50: 655.188 / gap50: 8.73%
- MA200: 617.8931 / gap200: 15.29%

## Relative Strength
- RS vs FTSE gap: 7.14% / slope_proxy: 0.002541
- RS vs Peers gap: 4.82% / slope_proxy: 0.004499

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-10 23:16:11**

## Commodity Regime

- WTI ref (CL=F): 82.05 / 5D 2.13%
- Brent ref (BZ=F): 87.58 / 5D 4.55%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.53
- Gas ref (NG=F): 2.77 / 5D -0.29%

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

- close: 58.65
- MA20 / MA60 / MA200: 55.69 / 55.09 / 50.35
- gap20 / gap60: 5.31% / 6.47%
- 5D return: 5.73%
- 20D high/low: 58.65 / 53.65

### Relative Strength

- ratio: 0.974576
- ratio_MA60: 0.967943
- ratio_gap: 0.69%
- ratio_slope_proxy(20d): -0.014036

### Volume (if available)

- volume: 7425208.00
- volume_MA20: 8563150.40
- volume_ratio: 0.87

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.33
- MA20 / MA60 / MA200: 18.44 / 18.06 / 16.31
- gap20 / gap60: -0.58% / 1.52%
- 5D return: -3.83%
- 20D high/low: 19.40 / 17.47

### Relative Strength

- ratio: 0.520887
- ratio_MA60: 0.512383
- ratio_gap: 1.66%
- ratio_slope_proxy(20d): -0.005979

### Volume (if available)

- volume: 11013616.00
- volume_MA20: 14467010.80
- volume_ratio: 0.76

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.72
- MA20 / MA60 / MA200: 5.21 / 5.66 / 5.38
- gap20 / gap60: 9.72% / 1.12%
- 5D return: 11.07%
- 20D high/low: 5.72 / 4.95

### Relative Strength

- ratio: 0.013906
- ratio_MA60: 0.014102
- ratio_gap: -1.39%
- ratio_slope_proxy(20d): -0.000451

### Volume (if available)

- volume: 59339703.00
- volume_MA20: 42324880.15
- volume_ratio: 1.40

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.26
- MA20 / MA60 / MA200: 13.47 / 12.69 / 10.82
- gap20 / gap60: 5.88% / 12.37%
- 5D return: 9.02%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.053674
- ratio_MA60: 0.051304
- ratio_gap: 4.62%
- ratio_slope_proxy(20d): 0.001097

### Volume (if available)

- volume: 12519804.00
- volume_MA20: 15022420.20
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-10**
- 실행시간(UTC): **2026-08-10 23:16:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.4
- VIX: 14.9
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 8.90% / slope_proxy: 0.012088
- GDXJ/GLD gap: 9.74% / slope_proxy: -0.006535

## VZLA (Vizsla Silver)
- close: 3.88 | RSI14: 66.802868 | ATR14%: 5.08%
- MA20 gap: 16.96% | MA50 gap: 14.68% | MA200 gap: -5.09%
- vol_ratio(Volume/Vol20): 1.130671 | gap_open: 0.27%
- RS vs SILJ gap: 2.64% / slope_proxy: 0.006083
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
- close: 8.98 | RSI14: 74.165618 | ATR14%: 5.74%
- MA20 gap: 31.82% | MA50 gap: 30.94% | MA200 gap: 6.05%
- vol_ratio(Volume/Vol20): 1.511159 | gap_open: 1.19%
- SilverMarginGate: SI=65.964996 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.25% / slope_proxy: -0.004267
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
- close: 27.290001 | RSI14: 65.465768 | ATR14%: 6.85%
- MA20 gap: 27.97% | MA50 gap: 15.17% | MA200 gap: -3.40%
- vol_ratio(Volume/Vol20): 1.130655 | gap_open: 0.94%
- RS vs SILJ gap: -2.34% / slope_proxy: -0.144443
- RS vs GDXJ gap: -4.94% / slope_proxy: -0.036195
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

- 실행시간(UTC): **2026-08-10 23:16:27**
- 데이터 기준일(주가): **2026-08-10**

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

- HY OAS: 2.70 / 4주 변화 0.01 bp-ish / 2026-08-07
- IG OAS: 0.78 / 4주 변화 0.01 bp-ish / 2026-08-07
- 10Y Real Yield: 2.40 / 4주 변화 0.08 bp-ish / 2026-08-07
- VIX: 14.90 / 4주 변화 -0.13 / 2026-08-07
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 9.15% / slope_proxy 11.72%
- GDXJ/GLD: gap 9.74% / slope_proxy 11.63%
- SILJ/SLV: gap 8.90% / slope_proxy 5.41%
- Gold breadth proxy: above50 100.00%, above200 61.54%, count 13
- Silver breadth proxy: above50 100.00%, above200 53.85%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.65 | RSI14: 82.58 | ATR14%: 5.07%
- MA20/50/200 gap: 27.98% / 26.05% / 39.00%
- 5D return: 33.66% | 20D drawdown: 0.00% | vol_ratio: 1.47
- RS vs GDXJ: gap 9.16% / slope_proxy 8.44%
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
- close: 6.89 | RSI14: 86.74 | ATR14%: 5.25%
- MA20/50/200 gap: 25.43% / 23.17% / 0.74%
- 5D return: 27.83% | 20D drawdown: 0.00% | vol_ratio: 2.46
- RS vs GDXJ: gap 5.99% / slope_proxy 11.34%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
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
- close: 1.45 | RSI14: 82.26 | ATR14%: 5.32%
- MA20/50/200 gap: 23.67% / 18.68% / -1.74%
- 5D return: 28.32% | 20D drawdown: 0.00% | vol_ratio: 2.88
- RS vs GDXJ: gap 2.71% / slope_proxy 5.87%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **60.5**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.18 | RSI14: 68.18 | ATR14%: 5.67%
- MA20/50/200 gap: 14.23% / 22.53% / 19.60%
- 5D return: 15.96% | 20D drawdown: 0.00% | vol_ratio: 0.87
- RS vs GDXJ: gap 4.49% / slope_proxy -12.45%
- FundamentalScore: 55 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **48.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.92 | RSI14: 77.97 | ATR14%: 5.77%
- MA20/50/200 gap: 31.85% / 39.90% / 67.30%
- 5D return: 37.27% | 20D drawdown: 0.00% | vol_ratio: 1.10
- RS vs SILJ: gap 27.31% / slope_proxy 18.29%
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
- close: 10.24 | RSI14: 72.17 | ATR14%: 5.33%
- MA20/50/200 gap: 25.74% / 22.72% / 7.12%
- 5D return: 32.47% | 20D drawdown: 0.00% | vol_ratio: 1.31
- RS vs SILJ: gap 8.15% / slope_proxy 7.60%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
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
- close: 8.98 | RSI14: 78.14 | ATR14%: 5.81%
- MA20/50/200 gap: 31.82% / 30.94% / 6.05%
- 5D return: 33.43% | 20D drawdown: 0.00% | vol_ratio: 1.51
- RS vs SILJ: gap 14.25% / slope_proxy 17.29%
- FundamentalScore: 74 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **71.1**
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
- close: 7.31 | RSI14: 65.91 | ATR14%: 5.73%
- MA20/50/200 gap: 23.97% / 18.68% / 9.58%
- 5D return: 32.19% | 20D drawdown: 0.00% | vol_ratio: 1.61
- RS vs SILJ: gap 5.06% / slope_proxy 3.78%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **64.8**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.88 | RSI14: 67.66 | ATR14%: 5.07%
- MA20/50/200 gap: 16.96% / 14.68% / -5.09%
- 5D return: 19.02% | 20D drawdown: 0.00% | vol_ratio: 1.13
- RS vs SILJ: gap 2.64% / slope_proxy 2.94%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **61.4**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.55 | RSI14: 63.42 | ATR14%: 5.27%
- MA20/50/200 gap: 15.04% / 12.70% / -4.46%
- 5D return: 21.62% | 20D drawdown: 0.00% | vol_ratio: 1.03
- RS vs SILJ: gap -0.42% / slope_proxy -3.87%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **55.4**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.13 | RSI14: 68.12 | ATR14%: 6.13%
- MA20/50/200 gap: 23.14% / 8.80% / -10.49%
- 5D return: 25.43% | 20D drawdown: 0.00% | vol_ratio: 1.05
- RS vs SILJ: gap -5.42% / slope_proxy 3.70%
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
- close: 27.29 | RSI14: 72.64 | ATR14%: 6.43%
- MA20/50/200 gap: 27.97% / 15.17% / -3.40%
- 5D return: 32.35% | 20D drawdown: 0.00% | vol_ratio: 1.13
- RS vs SILJ: gap -2.34% / slope_proxy 5.99%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
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
