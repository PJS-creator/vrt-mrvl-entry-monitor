# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-29 03:01:03**
- 데이터 기준일(일봉): **2026-07-28**
- 데이터 기준일(주봉): **2026-07-27**
- VXN 기준일: **2026-07-27** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 675.49
- Weekly RSI14: **51.37**
- 52W MA: 631.22 / gap: **7.01%**
- 104W MA gap: **19.38%**
- 52W MA 13W slope: **7.58%**
- VXN: **28.65** / 5D change: 0.12

## Daily trigger: 실제 매수 타이밍

- QQQ close: 675.49
- Daily RSI14: **36.48**
- 20D gap: **-4.60%**
- 50D gap: **-5.71%**
- 200D gap: **5.11%**
- MACD hist: -4.1013 / change: -0.4148
- ATR14%: **2.12%**
- 20D high drawdown: **-8.27%**

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

- 데이터 기준일(주가): **2026-07-28**
- 실행시간(UTC): **2026-07-29 03:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.81 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.44 / 4주 변화 28.0 bp
- VIX (VIXCLS): 18.67
- NFCI: -0.552

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.712346
- MA60: 9.659316
- gap: -9.80%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.329437
- MA60: 0.383316
- gap: -14.06%
- MA60_slope_proxy: 0.024084
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-28**
- 실행시간(UTC): **2026-07-29 03:00:44**

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
- TERM_SPREAD_10Y_POLICY: 127.53 bp / 4주 변화 31.36 bp
- CURVE_10s5s: 45.75 bp / 4주 변화 -0.63 bp

## NWG Price
- close: 680.8
- MA50: 634.616 / gap50: 7.28%
- MA200: 610.7894 / gap200: 11.46%

## Relative Strength
- RS vs FTSE gap: 5.90% / slope_proxy: 0.002135
- RS vs Peers gap: -0.80% / slope_proxy: -0.003154

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-29 03:00:51**

## Commodity Regime

- WTI ref (CL=F): 82.17 / 5D -3.23%
- Brent ref (BZ=F): 87.15 / 5D -4.24%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.98
- Gas ref (NG=F): 2.68 / 5D -6.32%

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

- close: 53.93
- MA20 / MA60 / MA200: 53.47 / 55.11 / 49.69
- gap20 / gap60: 0.87% / -2.15%
- 5D return: -4.55%
- 20D high/low: 57.60 / 47.94

### Relative Strength

- ratio: 0.936773
- ratio_MA60: 0.971881
- ratio_gap: -3.61%
- ratio_slope_proxy(20d): -0.023668

### Volume (if available)

- volume: 6333936.00
- volume_MA20: 9171171.80
- volume_ratio: 0.69

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.07
- MA20 / MA60 / MA200: 17.57 / 18.37 / 15.99
- gap20 / gap60: 2.87% / -1.62%
- 5D return: -2.54%
- 20D high/low: 19.00 / 15.99

### Relative Strength

- ratio: 0.501248
- ratio_MA60: 0.515329
- ratio_gap: -2.73%
- ratio_slope_proxy(20d): -0.008612

### Volume (if available)

- volume: 19043936.00
- volume_MA20: 15549161.80
- volume_ratio: 1.22

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 4.99
- MA20 / MA60 / MA200: 5.15 / 5.85 / 5.29
- gap20 / gap60: -3.09% / -14.67%
- 5D return: -4.77%
- 20D high/low: 5.37 / 4.87

### Relative Strength

- ratio: 0.013437
- ratio_MA60: 0.014322
- ratio_gap: -6.18%
- ratio_slope_proxy(20d): -0.000578

### Volume (if available)

- volume: 44373401.00
- volume_MA20: 41219175.05
- volume_ratio: 1.08

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

- close: 12.17
- MA20 / MA60 / MA200: 12.82 / 12.58 / 10.65
- gap20 / gap60: -5.10% / -3.24%
- 5D return: -13.44%
- 20D high/low: 15.16 / 10.85

### Relative Strength

- ratio: 0.048259
- ratio_MA60: 0.051061
- ratio_gap: -5.49%
- ratio_slope_proxy(20d): 0.000197

### Volume (if available)

- volume: 13937447.00
- volume_MA20: 15665517.35
- volume_ratio: 0.89

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

- 데이터 기준일(주가): **2026-07-28**
- 실행시간(UTC): **2026-07-29 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.81
- IG OAS 4주 변화: 5.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.44
- VIX: 18.67
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 2.73% / slope_proxy: 0.007307
- GDXJ/GLD gap: -3.20% / slope_proxy: -0.008823

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 46.996429 | ATR14%: 6.08%
- MA20 gap: -0.28% | MA50 gap: -6.01% | MA200 gap: -22.99%
- vol_ratio(Volume/Vol20): 0.507798 | gap_open: 2.11%
- RS vs SILJ gap: 6.55% / slope_proxy: 0.006256
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
- close: 6.46 | RSI14: 47.922364 | ATR14%: 6.79%
- MA20 gap: 0.80% | MA50 gap: -7.75% | MA200 gap: -23.46%
- vol_ratio(Volume/Vol20): 1.248603 | gap_open: 0.16%
- SilverMarginGate: SI=58.035 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.53% / slope_proxy: -0.005172
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## HYMC (Hycroft Mining)
- close: 20.120001 | RSI14: 41.063176 | ATR14%: 8.90%
- MA20 gap: -4.72% | MA50 gap: -21.60% | MA200 gap: -27.08%
- vol_ratio(Volume/Vol20): 1.079131 | gap_open: 2.40%
- RS vs SILJ gap: -16.51% / slope_proxy: -0.134512
- RS vs GDXJ gap: -19.55% / slope_proxy: -0.030988
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

- 실행시간(UTC): **2026-07-29 03:01:02**
- 데이터 기준일(주가): **2026-07-28**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.81 / 4주 변화 0.01 bp-ish / 2026-07-27
- IG OAS: 0.81 / 4주 변화 0.05 bp-ish / 2026-07-27
- 10Y Real Yield: 2.44 / 4주 변화 0.26 bp-ish / 2026-07-27
- VIX: 18.67 / 4주 변화 1.02 / 2026-07-27
- NFCI: -0.55 / 4주 변화 -0.05 / 2026-07-17

### Leadership ratios

- GDX/GLD: gap -2.76% / slope_proxy -1.91%
- GDXJ/GLD: gap -3.20% / slope_proxy -1.76%
- SILJ/SLV: gap 2.73% / slope_proxy -3.68%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.40 | RSI14: 57.79 | ATR14%: 4.79%
- MA20/50/200 gap: 3.25% / -4.00% / -21.36%
- 5D return: 1.89% | 20D drawdown: -6.09% | vol_ratio: 1.14
- RS vs GDXJ: gap 2.19% / slope_proxy 6.14%
- FundamentalScore: 82 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **62.1**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.27 | RSI14: 45.65 | ATR14%: 4.84%
- MA20/50/200 gap: -0.85% / -5.71% / 6.21%
- 5D return: 2.83% | 20D drawdown: -8.09% | vol_ratio: 0.73
- RS vs GDXJ: gap 3.37% / slope_proxy 0.96%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.84 | RSI14: 53.47 | ATR14%: 7.96%
- MA20/50/200 gap: 0.27% / 2.40% / 2.25%
- 5D return: -1.08% | 20D drawdown: -10.68% | vol_ratio: 0.59
- RS vs GDXJ: gap 11.51% / slope_proxy 24.55%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **60.5**
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.12 | RSI14: 48.72 | ATR14%: 5.48%
- MA20/50/200 gap: -1.45% / -9.08% / -24.59%
- 5D return: 0.90% | 20D drawdown: -13.85% | vol_ratio: 0.49
- RS vs GDXJ: gap -2.04% / slope_proxy -0.46%
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
- close: 19.40 | RSI14: 51.32 | ATR14%: 6.51%
- MA20/50/200 gap: -0.59% / 1.83% / 19.83%
- 5D return: 0.73% | 20D drawdown: -7.18% | vol_ratio: 1.16
- RS vs SILJ: gap 15.63% / slope_proxy 9.98%
- FundamentalScore: 86 | TechnicalScore: 100 | RegimeScore: 30 | OverallScore: **79.7**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.75 | RSI14: 50.42 | ATR14%: 5.83%
- MA20/50/200 gap: -3.12% / -8.96% / -19.02%
- 5D return: -5.49% | 20D drawdown: -9.46% | vol_ratio: 1.33
- RS vs SILJ: gap 1.35% / slope_proxy 0.50%
- FundamentalScore: 82 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **62.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.46 | RSI14: 53.77 | ATR14%: 6.17%
- MA20/50/200 gap: 0.80% / -7.75% / -23.46%
- 5D return: -1.52% | 20D drawdown: -5.14% | vol_ratio: 1.25
- RS vs SILJ: gap 1.53% / slope_proxy 6.88%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **58.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.55 | RSI14: 45.00 | ATR14%: 5.42%
- MA20/50/200 gap: -5.09% / -8.33% / -20.42%
- 5D return: -4.84% | 20D drawdown: -11.60% | vol_ratio: 0.72
- RS vs SILJ: gap 1.82% / slope_proxy 1.25%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **55.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.19 | RSI14: 58.27 | ATR14%: 5.70%
- MA20/50/200 gap: -0.28% / -6.01% / -22.99%
- 5D return: -3.04% | 20D drawdown: -6.73% | vol_ratio: 0.51
- RS vs SILJ: gap 6.55% / slope_proxy 3.79%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **52.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.88 | RSI14: 42.73 | ATR14%: 7.33%
- MA20/50/200 gap: -8.08% / -22.03% / -32.34%
- 5D return: -6.05% | 20D drawdown: -20.65% | vol_ratio: 0.94
- RS vs SILJ: gap -14.40% / slope_proxy -11.74%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **41.9**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.50 | RSI14: 46.39 | ATR14%: 6.90%
- MA20/50/200 gap: -7.49% / -12.59% / -17.35%
- 5D return: -9.09% | 20D drawdown: -16.41% | vol_ratio: 0.75
- RS vs SILJ: gap -1.80% / slope_proxy -6.85%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **38.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 20.12 | RSI14: 47.44 | ATR14%: 7.97%
- MA20/50/200 gap: -4.72% / -21.60% / -27.08%
- 5D return: -2.90% | 20D drawdown: -14.82% | vol_ratio: 1.08
- RS vs SILJ: gap -16.51% / slope_proxy -7.68%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **35.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
