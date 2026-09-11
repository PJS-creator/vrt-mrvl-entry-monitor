# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-11 00:30:51**
- 데이터 기준일(일봉): **2026-09-09**
- 데이터 기준일(주봉): **2026-09-07**
- VXN 기준일: **2026-09-09** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 708.69
- Weekly RSI14: **55.65**
- 52W MA: 648.21 / gap: **9.33%**
- 104W MA gap: **22.04%**
- 52W MA 13W slope: **6.23%**
- VXN: **22.32** / 5D change: 0.36

## Daily trigger: 실제 매수 타이밍

- QQQ close: 716.31
- Daily RSI14: **51.66**
- 20D gap: **-0.13%**
- 50D gap: **0.72%**
- 200D gap: **8.86%**
- MACD hist: -0.0881 / change: -0.0097
- ATR14%: **1.25%**
- 20D high drawdown: **-2.15%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-09-09**
- 실행시간(UTC): **2026-09-11 00:30:28**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.46 / 4주 변화 4.0 bp
- VIX (VIXCLS): 16.46
- NFCI: -0.564

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.557618
- MA60: 9.290457
- gap: -7.89%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.409218
- MA60: 0.394094
- gap: 3.84%
- MA60_slope_proxy: 0.002397
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-09**
- 실행시간(UTC): **2026-09-11 00:30:30**

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
- TERM_SPREAD_10Y_POLICY: 134.79 bp / 4주 변화 15.17 bp
- CURVE_10s5s: 45.95 bp / 4주 변화 -1.79 bp

## NWG Price
- close: 688.0
- MA50: 686.1169 / gap50: 0.27%
- MA200: 629.2072 / gap200: 9.34%

## Relative Strength
- RS vs FTSE gap: 1.31% / slope_proxy: 0.002311
- RS vs Peers gap: 0.17% / slope_proxy: 0.013659

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-11 00:30:37**

## Commodity Regime

- WTI ref (CL=F): 103.06 / 5D 13.24%
- Brent ref (BZ=F): 108.15 / 5D 13.09%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.09
- Gas ref (NG=F): 2.83 / 5D -4.30%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 61.30
- MA20 / MA60 / MA200: 59.82 / 55.79 / 52.34
- gap20 / gap60: 2.47% / 9.88%
- 5D return: 0.57%
- 20D high/low: 61.52 / 57.70

### Relative Strength

- ratio: 0.938601
- ratio_MA60: 0.949845
- ratio_gap: -1.18%
- ratio_slope_proxy(20d): -0.017897

### Volume (if available)

- volume: 8993813.00
- volume_MA20: 7113115.65
- volume_ratio: 1.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.93
- MA20 / MA60 / MA200: 18.79 / 17.68 / 16.57
- gap20 / gap60: 11.37% / 18.40%
- 5D return: 2.95%
- 20D high/low: 20.93 / 17.25

### Relative Strength

- ratio: 0.549777
- ratio_MA60: 0.499474
- ratio_gap: 10.07%
- ratio_slope_proxy(20d): 0.001789

### Volume (if available)

- volume: 34526373.00
- volume_MA20: 22641748.65
- volume_ratio: 1.52

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.71
- MA20 / MA60 / MA200: 5.83 / 5.43 / 5.57
- gap20 / gap60: -2.05% / 5.16%
- 5D return: -3.55%
- 20D high/low: 6.22 / 5.60

### Relative Strength

- ratio: 0.013299
- ratio_MA60: 0.013734
- ratio_gap: -3.17%
- ratio_slope_proxy(20d): -0.000340

### Volume (if available)

- volume: 42270398.00
- volume_MA20: 40238549.90
- volume_ratio: 1.05

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 15.29
- MA20 / MA60 / MA200: 14.32 / 13.10 / 11.44
- gap20 / gap60: 6.81% / 16.73%
- 5D return: 1.19%
- 20D high/low: 15.29 / 13.54

### Relative Strength

- ratio: 0.055413
- ratio_MA60: 0.050004
- ratio_gap: 10.82%
- ratio_slope_proxy(20d): -0.001340

### Volume (if available)

- volume: 17492597.00
- volume_MA20: 13229094.85
- volume_ratio: 1.32

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-10**
- 실행시간(UTC): **2026-09-11 00:30:40**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.46
- VIX: 16.46
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 7.08% / slope_proxy: 0.02825
- GDXJ/GLD gap: 13.62% / slope_proxy: 0.013112

## VZLA (Vizsla Silver)
- close: 4.09 | RSI14: 58.49109 | ATR14%: 4.90%
- MA20 gap: 3.82% | MA50 gap: 15.21% | MA200 gap: 0.76%
- vol_ratio(Volume/Vol20): 1.011902 | gap_open: 2.57%
- RS vs SILJ gap: 0.78% / slope_proxy: 0.000291
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 10.43 | RSI14: 65.453201 | ATR14%: 5.60%
- MA20 gap: 9.48% | MA50 gap: 32.17% | MA200 gap: 17.34%
- vol_ratio(Volume/Vol20): 1.019472 | gap_open: 1.50%
- SilverMarginGate: SI=63.994999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 18.15% / slope_proxy: 0.013118
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

## HYMC (Hycroft Mining)
- close: 22.809999 | RSI14: 44.990636 | ATR14%: 7.76%
- MA20 gap: -8.72% | MA50 gap: -1.13% | MA200 gap: -24.02%
- vol_ratio(Volume/Vol20): 0.998625 | gap_open: 1.92%
- RS vs SILJ gap: -15.03% / slope_proxy: -0.090366
- RS vs GDXJ gap: -17.17% / slope_proxy: -0.02728
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

- 실행시간(UTC): **2026-09-11 00:30:49**
- 데이터 기준일(주가): **2026-09-10**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

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

- HY OAS: 2.71 / 4주 변화 0.00 bp-ish / 2026-09-09
- IG OAS: 0.81 / 4주 변화 0.02 bp-ish / 2026-09-09
- 10Y Real Yield: 2.46 / 4주 변화 0.03 bp-ish / 2026-09-09
- VIX: 16.46 / 4주 변화 1.91 / 2026-09-09
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-09-04

### Leadership ratios

- GDX/GLD: gap 13.86% / slope_proxy 9.78%
- GDXJ/GLD: gap 13.62% / slope_proxy 8.59%
- SILJ/SLV: gap 7.08% / slope_proxy 3.01%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 92.31%, above200 76.92%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.94 | RSI14: 57.23 | ATR14%: 4.89%
- MA20/50/200 gap: 3.68% / 24.14% / 12.87%
- 5D return: 3.39% | 20D drawdown: -4.80% | vol_ratio: 1.17
- RS vs GDXJ: gap 15.32% / slope_proxy 11.26%
- FundamentalScore: 82 | TechnicalScore: 80 | RegimeScore: 75 | OverallScore: **79.9**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.26 | RSI14: 47.87 | ATR14%: 4.35%
- MA20/50/200 gap: -0.07% / 18.12% / 37.57%
- 5D return: 7.21% | 20D drawdown: -7.32% | vol_ratio: 0.52
- RS vs GDXJ: gap 2.67% / slope_proxy -5.05%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **75.6**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.57 | RSI14: 55.45 | ATR14%: 6.92%
- MA20/50/200 gap: 0.45% / 19.35% / 32.62%
- 5D return: -7.89% | 20D drawdown: -7.89% | vol_ratio: 0.65
- RS vs GDXJ: gap 14.13% / slope_proxy 15.88%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **69.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: GoldUptrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.47 | RSI14: 32.69 | ATR14%: 4.79%
- MA20/50/200 gap: -5.83% / 9.47% / -1.59%
- 5D return: -3.92% | 20D drawdown: -10.91% | vol_ratio: 0.40
- RS vs GDXJ: gap -0.23% / slope_proxy -1.18%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **51.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 29.89 | RSI14: 61.34 | ATR14%: 5.52%
- MA20/50/200 gap: 8.08% / 26.73% / 61.63%
- 5D return: 13.35% | 20D drawdown: 0.00% | vol_ratio: 0.75
- RS vs SILJ: gap 14.25% / slope_proxy 0.66%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 10.43 | RSI14: 60.72 | ATR14%: 5.80%
- MA20/50/200 gap: 9.48% / 32.17% / 17.34%
- 5D return: 13.37% | 20D drawdown: 0.00% | vol_ratio: 1.02
- RS vs SILJ: gap 18.15% / slope_proxy 11.03%
- FundamentalScore: 74 | TechnicalScore: 80 | RegimeScore: 75 | OverallScore: **76.3**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.85 | RSI14: 52.01 | ATR14%: 4.79%
- MA20/50/200 gap: 4.29% / 20.66% / 9.50%
- 5D return: 9.11% | 20D drawdown: -2.71% | vol_ratio: 0.80
- RS vs SILJ: gap 6.83% / slope_proxy 8.77%
- FundamentalScore: 78 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **72.8**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.15 | RSI14: 51.94 | ATR14%: 5.48%
- MA20/50/200 gap: 3.38% / 20.47% / 12.98%
- 5D return: 8.89% | 20D drawdown: -2.79% | vol_ratio: 1.04
- RS vs SILJ: gap 6.68% / slope_proxy -0.77%
- FundamentalScore: 82 | TechnicalScore: 55 | RegimeScore: 75 | OverallScore: **71.2**
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
- close: 7.36 | RSI14: 45.78 | ATR14%: 5.26%
- MA20/50/200 gap: 0.27% / 12.30% / 5.84%
- 5D return: 4.99% | 20D drawdown: -4.79% | vol_ratio: 1.14
- RS vs SILJ: gap -1.72% / slope_proxy -2.66%
- FundamentalScore: 60 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **68.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.09 | RSI14: 57.25 | ATR14%: 4.94%
- MA20/50/200 gap: 3.82% / 15.21% / 0.76%
- 5D return: 5.96% | 20D drawdown: -1.92% | vol_ratio: 1.01
- RS vs SILJ: gap 0.78% / slope_proxy 1.63%
- FundamentalScore: 72 | TechnicalScore: 80 | RegimeScore: 75 | OverallScore: **75.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.33 | RSI14: 48.74 | ATR14%: 5.80%
- MA20/50/200 gap: -0.06% / 13.05% / -9.24%
- 5D return: 5.54% | 20D drawdown: -7.14% | vol_ratio: 0.81
- RS vs SILJ: gap -3.15% / slope_proxy -3.03%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
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
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 22.81 | RSI14: 29.66 | ATR14%: 7.60%
- MA20/50/200 gap: -8.72% / -1.13% / -24.02%
- 5D return: 5.46% | 20D drawdown: -18.24% | vol_ratio: 1.00
- RS vs SILJ: gap -15.03% / slope_proxy -21.53%
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
