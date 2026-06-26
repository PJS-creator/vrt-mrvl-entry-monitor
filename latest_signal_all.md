# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-26 15:01:15**
- 데이터 기준일(일봉): **2026-06-26**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-25** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 715.59
- Weekly RSI14: **63.42**
- 52W MA: 617.61 / gap: **15.86%**
- 104W MA gap: **28.96%**
- 52W MA 13W slope: **8.51%**
- VXN: **30.91** / 5D change: 2.35

## Daily trigger: 실제 매수 타이밍

- QQQ close: 711.06
- Daily RSI14: **48.21**
- 20D gap: **-1.84%**
- 50D gap: **1.26%**
- 200D gap: **12.74%**
- MACD hist: -3.6931 / change: -0.3324
- ATR14%: **2.30%**
- 20D high drawdown: **-4.60%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-26 15:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.23 / 4주 변화 14.0 bp
- VIX (VIXCLS): 18.89
- NFCI: -0.516

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.362257
- MA60: 9.300744
- gap: 0.66%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.434265
- MA60: 0.356499
- gap: 21.81%
- MA60_slope_proxy: 0.072647
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-26 15:00:47**

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
- TERM_SPREAD_10Y_POLICY: 91.83 bp / 4주 변화 -15.76 bp
- CURVE_10s5s: 44.05 bp / 4주 변화 -1.94 bp

## NWG Price
- close: 652.2
- MA50: 597.0811 / gap50: 9.23%
- MA200: 595.7835 / gap200: 9.47%

## Relative Strength
- RS vs FTSE gap: 8.42% / slope_proxy: 0.001528
- RS vs Peers gap: 2.02% / slope_proxy: -0.015611

## Why not today?
- CurveGreen=FALSE
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-26 15:00:55**

## Commodity Regime

- WTI ref (CL=F): 69.01 / 5D -9.91%
- Brent ref (BZ=F): 72.48 / 5D -9.23%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.47
- Gas ref (NG=F): 3.34 / 5D 3.43%

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

- close: 50.32
- MA20 / MA60 / MA200: 55.04 / 56.84 / 48.89
- gap20 / gap60: -8.57% / -11.47%
- 5D return: -2.89%
- 20D high/low: 59.37 / 50.32

### Relative Strength

- ratio: 0.933408
- ratio_MA60: 0.997995
- ratio_gap: -6.47%
- ratio_slope_proxy(20d): -0.008190

### Volume (if available)

- volume: 2168945.00
- volume_MA20: 9613142.25
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.32
- MA20 / MA60 / MA200: 17.57 / 19.50 / 15.47
- gap20 / gap60: -7.16% / -16.35%
- 5D return: -2.60%
- 20D high/low: 18.72 / 16.32

### Relative Strength

- ratio: 0.472146
- ratio_MA60: 0.524813
- ratio_gap: -10.04%
- ratio_slope_proxy(20d): -0.002112

### Volume (if available)

- volume: 2820421.00
- volume_MA20: 14299511.05
- volume_ratio: 0.20

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.15
- MA20 / MA60 / MA200: 5.78 / 6.29 / 5.10
- gap20 / gap60: -10.90% / -18.16%
- 5D return: -3.01%
- 20D high/low: 6.25 / 5.04

### Relative Strength

- ratio: 0.013714
- ratio_MA60: 0.014950
- ratio_gap: -8.27%
- ratio_slope_proxy(20d): -0.000786

### Volume (if available)

- volume: 5873509.00
- volume_MA20: 28987810.45
- volume_ratio: 0.20

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

- close: 10.88
- MA20 / MA60 / MA200: 11.97 / 12.69 / 10.77
- gap20 / gap60: -9.09% / -14.26%
- 5D return: -1.27%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045559
- ratio_MA60: 0.050994
- ratio_gap: -10.66%
- ratio_slope_proxy(20d): -0.000537

### Volume (if available)

- volume: 1663130.00
- volume_MA20: 13844646.50
- volume_ratio: 0.12

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

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-26 15:01:05**

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
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.23
- VIX: 18.89
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 10.22% / slope_proxy: 0.005131
- GDXJ/GLD gap: -3.09% / slope_proxy: -0.001645

## VZLA (Vizsla Silver)
- close: 3.2701 | RSI14: 43.409983 | ATR14%: 6.74%
- MA20 gap: -7.88% | MA50 gap: -6.97% | MA200 gap: -22.89%
- vol_ratio(Volume/Vol20): 0.194285 | gap_open: 1.28%
- RS vs SILJ gap: 5.62% / slope_proxy: 0.004421
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
- close: 6.705 | RSI14: 42.776977 | ATR14%: 8.38%
- MA20 gap: -5.24% | MA50 gap: -16.00% | MA200 gap: -21.27%
- vol_ratio(Volume/Vol20): 0.151942 | gap_open: 3.26%
- SilverMarginGate: SI=59.830002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.45% / slope_proxy: -0.00961
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
- close: 23.370001 | RSI14: 36.968218 | ATR14%: 10.05%
- MA20 gap: -12.61% | MA50 gap: -29.84% | MA200 gap: -10.19%
- vol_ratio(Volume/Vol20): 0.375656 | gap_open: 1.32%
- RS vs SILJ gap: -21.99% / slope_proxy: -0.079367
- RS vs GDXJ gap: -20.67% / slope_proxy: -0.017004
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

- 실행시간(UTC): **2026-06-26 15:01:12**
- 데이터 기준일(주가): **2026-06-26**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

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

- HY OAS: 2.78 / 4주 변화 0.06 bp-ish / 2026-06-25
- IG OAS: 0.76 / 4주 변화 0.03 bp-ish / 2026-06-25
- 10Y Real Yield: 2.23 / 4주 변화 0.13 bp-ish / 2026-06-24
- VIX: 18.89 / 4주 변화 3.15 / 2026-06-25
- NFCI: -0.52 / 4주 변화 0.05 / 2026-06-19

### Leadership ratios

- GDX/GLD: gap -2.58% / slope_proxy -3.17%
- GDXJ/GLD: gap -3.06% / slope_proxy -5.14%
- SILJ/SLV: gap 10.22% / slope_proxy 8.82%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.47 | RSI14: 51.71 | ATR14%: 6.28%
- MA20/50/200 gap: -4.45% / -5.73% / 12.65%
- 5D return: -7.89% | 20D drawdown: -14.14% | vol_ratio: 0.10
- RS vs GDXJ: gap 9.81% / slope_proxy 0.81%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.20 | RSI14: 48.81 | ATR14%: 8.07%
- MA20/50/200 gap: -6.10% / -10.71% / -20.19%
- 5D return: -6.25% | 20D drawdown: -18.37% | vol_ratio: 0.27
- RS vs GDXJ: gap 0.10% / slope_proxy 1.36%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.13 | RSI14: 39.93 | ATR14%: 6.88%
- MA20/50/200 gap: -10.57% / -19.20% / -26.04%
- 5D return: -8.39% | 20D drawdown: -27.23% | vol_ratio: 0.14
- RS vs GDXJ: gap -9.61% / slope_proxy -13.71%
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
- close: 1.52 | RSI14: 40.74 | ATR14%: 6.53%
- MA20/50/200 gap: -8.74% / -16.60% / -9.68%
- 5D return: -6.17% | 20D drawdown: -22.84% | vol_ratio: 0.11
- RS vs GDXJ: gap -4.34% / slope_proxy -7.54%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **36.0**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 19.46 | RSI14: 58.90 | ATR14%: 7.38%
- MA20/50/200 gap: 2.30% / 4.78% / 26.77%
- 5D return: -2.11% | 20D drawdown: -9.45% | vol_ratio: 0.28
- RS vs SILJ: gap 19.81% / slope_proxy 8.64%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 55 | OverallScore: **79.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.64 | RSI14: 56.16 | ATR14%: 5.82%
- MA20/50/200 gap: -1.29% / -9.61% / -12.59%
- 5D return: -2.01% | 20D drawdown: -12.13% | vol_ratio: 0.17
- RS vs SILJ: gap 0.21% / slope_proxy 3.19%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.49 | RSI14: 54.97 | ATR14%: 6.71%
- MA20/50/200 gap: -1.70% / -8.55% / -10.52%
- 5D return: -1.42% | 20D drawdown: -14.87% | vol_ratio: 0.23
- RS vs SILJ: gap 2.62% / slope_proxy -0.19%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.70 | RSI14: 53.53 | ATR14%: 8.09%
- MA20/50/200 gap: -5.24% / -16.00% / -21.27%
- 5D return: -6.22% | 20D drawdown: -19.51% | vol_ratio: 0.15
- RS vs SILJ: gap -5.45% / slope_proxy -3.55%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **49.6**
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
- close: 3.27 | RSI14: 47.10 | ATR14%: 6.49%
- MA20/50/200 gap: -7.88% / -6.97% / -22.89%
- 5D return: -7.88% | 20D drawdown: -20.82% | vol_ratio: 0.19
- RS vs SILJ: gap 5.62% / slope_proxy -1.19%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **48.6**
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
- close: 4.96 | RSI14: 50.58 | ATR14%: 8.30%
- MA20/50/200 gap: -7.53% / -15.03% / -12.09%
- 5D return: -7.46% | 20D drawdown: -22.86% | vol_ratio: 0.31
- RS vs SILJ: gap -3.48% / slope_proxy -5.60%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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
- close: 6.22 | RSI14: 54.81 | ATR14%: 7.43%
- MA20/50/200 gap: -2.94% / -7.60% / -4.78%
- 5D return: -4.82% | 20D drawdown: -16.11% | vol_ratio: 0.37
- RS vs SILJ: gap 3.89% / slope_proxy -0.30%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **43.2**
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
- close: 23.37 | RSI14: 41.00 | ATR14%: 8.94%
- MA20/50/200 gap: -12.61% / -29.84% / -10.19%
- 5D return: -10.15% | 20D drawdown: -30.90% | vol_ratio: 0.38
- RS vs SILJ: gap -21.99% / slope_proxy -17.10%
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
