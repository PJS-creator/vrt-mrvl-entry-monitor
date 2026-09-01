# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-01 01:23:32**
- 데이터 기준일(일봉): **2026-08-31**
- 데이터 기준일(주봉): **2026-08-31**
- VXN 기준일: **2026-08-28** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 716.76
- Weekly RSI14: **58.21**
- 52W MA: 645.77 / gap: **10.99%**
- 104W MA gap: **23.92%**
- 52W MA 13W slope: **6.49%**
- VXN: **19.92** / 5D change: -2.06

## Daily trigger: 실제 매수 타이밍

- QQQ close: 716.76
- Daily RSI14: **52.09**
- 20D gap: **-0.28%**
- 50D gap: **0.73%**
- 200D gap: **9.48%**
- MACD hist: -0.4086 / change: 0.0847
- ATR14%: **1.40%**
- 20D high drawdown: **-2.09%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-31**
- 실행시간(UTC): **2026-09-01 01:23:05**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.6 / 4주 변화 -25.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 -5.0 bp
- VIX (VIXCLS): 14.43
- NFCI: -0.566

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.300289
- MA60: 9.11142
- gap: -8.90%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.380253
- MA60: 0.401014
- gap: -5.18%
- MA60_slope_proxy: 0.016293
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-28**
- 실행시간(UTC): **2026-09-01 01:23:09**

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
- TERM_SPREAD_10Y_POLICY: 126.21 bp / 4주 변화 0.7 bp
- CURVE_10s5s: 48.31 bp / 4주 변화 3.88 bp

## NWG Price
- close: 679.4
- MA50: 681.2374 / gap50: -0.27%
- MA200: 625.6615 / gap200: 8.59%

## Relative Strength
- RS vs FTSE gap: -0.28% / slope_proxy: 0.002805
- RS vs Peers gap: -0.35% / slope_proxy: 0.01911

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-01 01:23:16**

## Commodity Regime

- WTI ref (CL=F): 86.42 / 5D 1.66%
- Brent ref (BZ=F): 88.72 / 5D -3.74%
- Brent Tier: **80-90**
- Brent-WTI spread: 2.30
- Gas ref (NG=F): 2.93 / 5D 5.28%

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

- close: 60.18
- MA20 / MA60 / MA200: 58.53 / 55.37 / 51.76
- gap20 / gap60: 2.83% / 8.69%
- 5D return: 0.12%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.940901
- ratio_MA60: 0.954741
- ratio_gap: -1.45%
- ratio_slope_proxy(20d): -0.014112

### Volume (if available)

- volume: 8848804.00
- volume_MA20: 7941165.20
- volume_ratio: 1.11

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.35
- MA20 / MA60 / MA200: 17.95 / 17.37 / 16.32
- gap20 / gap60: 7.80% / 11.42%
- 5D return: 7.08%
- 20D high/low: 19.35 / 17.25

### Relative Strength

- ratio: 0.537052
- ratio_MA60: 0.496723
- ratio_gap: 8.12%
- ratio_slope_proxy(20d): -0.002380

### Volume (if available)

- volume: 21215832.00
- volume_MA20: 18876456.60
- volume_ratio: 1.12

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

- close: 5.81
- MA20 / MA60 / MA200: 5.67 / 5.44 / 5.52
- gap20 / gap60: 2.45% / 6.81%
- 5D return: 0.69%
- 20D high/low: 6.01 / 5.14

### Relative Strength

- ratio: 0.013537
- ratio_MA60: 0.013778
- ratio_gap: -1.74%
- ratio_slope_proxy(20d): -0.000458

### Volume (if available)

- volume: 27498015.00
- volume_MA20: 40153965.75
- volume_ratio: 0.68

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

- close: 14.64
- MA20 / MA60 / MA200: 13.86 / 12.90 / 11.23
- gap20 / gap60: 5.65% / 13.45%
- 5D return: 1.74%
- 20D high/low: 14.64 / 12.43

### Relative Strength

- ratio: 0.050190
- ratio_MA60: 0.050227
- ratio_gap: -0.07%
- ratio_slope_proxy(20d): -0.001132

### Volume (if available)

- volume: 12931591.00
- volume_MA20: 13422524.55
- volume_ratio: 0.96

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-31**
- 실행시간(UTC): **2026-09-01 01:23:22**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -25.0 bp / latest 2.6
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -5.0 bp / latest 2.42
- VIX: 14.43
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 8.24% / slope_proxy: 0.025074
- GDXJ/GLD gap: 13.46% / slope_proxy: 0.006405

## VZLA (Vizsla Silver)
- close: 4.05 | RSI14: 62.042537 | ATR14%: 4.70%
- MA20 gap: 6.01% | MA50 gap: 17.18% | MA200 gap: -0.64%
- vol_ratio(Volume/Vol20): 0.936059 | gap_open: 0.00%
- RS vs SILJ gap: 1.57% / slope_proxy: 0.002139
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
- close: 9.36 | RSI14: 59.846102 | ATR14%: 5.91%
- MA20 gap: 4.01% | MA50 gap: 25.13% | MA200 gap: 6.93%
- vol_ratio(Volume/Vol20): 0.443781 | gap_open: 2.73%
- SilverMarginGate: SI=67.379997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.93% / slope_proxy: 0.006136
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
- close: 23.43 | RSI14: 45.386951 | ATR14%: 8.10%
- MA20 gap: -9.05% | MA50 gap: 1.35% | MA200 gap: -20.94%
- vol_ratio(Volume/Vol20): 0.806828 | gap_open: 0.02%
- RS vs SILJ gap: -13.59% / slope_proxy: -0.102515
- RS vs GDXJ gap: -16.93% / slope_proxy: -0.030072
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

- 실행시간(UTC): **2026-09-01 01:23:31**
- 데이터 기준일(주가): **2026-08-31**

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

- HY OAS: 2.60 / 4주 변화 -0.25 bp-ish / 2026-08-28
- IG OAS: 0.79 / 4주 변화 0.00 bp-ish / 2026-08-28
- 10Y Real Yield: 2.42 / 4주 변화 -0.05 bp-ish / 2026-08-28
- VIX: 14.43 / 4주 변화 -1.56 / 2026-08-28
- NFCI: -0.57 / 4주 변화 -0.10 / 2026-08-21

### Leadership ratios

- GDX/GLD: gap 13.68% / slope_proxy 15.82%
- GDXJ/GLD: gap 13.46% / slope_proxy 14.99%
- SILJ/SLV: gap 8.24% / slope_proxy 7.47%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.06 | RSI14: 52.45 | ATR14%: 5.50%
- MA20/50/200 gap: 1.42% / 20.00% / 37.46%
- 5D return: -8.04% | 20D drawdown: -9.12% | vol_ratio: 0.67
- RS vs GDXJ: gap 2.50% / slope_proxy 7.15%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **84.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.65 | RSI14: 64.73 | ATR14%: 4.54%
- MA20/50/200 gap: 6.61% / 27.06% / 9.87%
- 5D return: -2.67% | 20D drawdown: -6.36% | vol_ratio: 0.80
- RS vs GDXJ: gap 8.02% / slope_proxy 4.72%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.51 | RSI14: 55.17 | ATR14%: 5.39%
- MA20/50/200 gap: -0.17% / 16.40% / 1.59%
- 5D return: -7.93% | 20D drawdown: -8.48% | vol_ratio: 0.45
- RS vs GDXJ: gap -1.75% / slope_proxy -3.76%
- FundamentalScore: 70 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **67.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.61 | RSI14: 70.59 | ATR14%: 5.64%
- MA20/50/200 gap: 12.14% / 31.14% / 37.31%
- 5D return: -1.14% | 20D drawdown: -3.69% | vol_ratio: 0.61
- RS vs GDXJ: gap 13.50% / slope_proxy 16.16%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **57.2**
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
- close: 27.92 | RSI14: 50.34 | ATR14%: 5.90%
- MA20/50/200 gap: 4.04% / 24.79% / 55.59%
- 5D return: 5.04% | 20D drawdown: -4.68% | vol_ratio: 0.60
- RS vs SILJ: gap 12.18% / slope_proxy 1.58%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.71 | RSI14: 51.19 | ATR14%: 6.31%
- MA20/50/200 gap: 4.00% / 20.23% / 9.61%
- 5D return: -0.46% | 20D drawdown: -5.22% | vol_ratio: 0.88
- RS vs SILJ: gap 5.84% / slope_proxy 7.12%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 19.87 | RSI14: 61.74 | ATR14%: 5.35%
- MA20/50/200 gap: 5.50% / 19.33% / 5.35%
- 5D return: -2.60% | 20D drawdown: -7.28% | vol_ratio: 0.64
- RS vs SILJ: gap 5.21% / slope_proxy 7.56%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.36 | RSI14: 53.83 | ATR14%: 6.08%
- MA20/50/200 gap: 4.01% / 25.13% / 6.93%
- 5D return: -2.19% | 20D drawdown: -6.59% | vol_ratio: 0.44
- RS vs SILJ: gap 10.93% / slope_proxy 8.31%
- FundamentalScore: 74 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **71.1**
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.30 | RSI14: 48.64 | ATR14%: 5.81%
- MA20/50/200 gap: 2.13% / 14.16% / 6.19%
- 5D return: -0.82% | 20D drawdown: -5.56% | vol_ratio: 0.60
- RS vs SILJ: gap -0.36% / slope_proxy 2.91%
- FundamentalScore: 60 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **63.0**
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
- close: 4.05 | RSI14: 58.87 | ATR14%: 4.61%
- MA20/50/200 gap: 6.01% / 17.18% / -0.64%
- 5D return: 3.05% | 20D drawdown: -2.64% | vol_ratio: 0.94
- RS vs SILJ: gap 1.57% / slope_proxy -0.76%
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
- close: 5.37 | RSI14: 55.20 | ATR14%: 5.71%
- MA20/50/200 gap: 3.37% / 15.28% / -7.92%
- 5D return: -0.37% | 20D drawdown: -6.45% | vol_ratio: 0.71
- RS vs SILJ: gap -1.66% / slope_proxy 1.91%
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
- close: 23.43 | RSI14: 37.24 | ATR14%: 8.42%
- MA20/50/200 gap: -9.05% / 1.35% / -20.94%
- 5D return: -8.97% | 20D drawdown: -16.02% | vol_ratio: 0.81
- RS vs SILJ: gap -13.59% / slope_proxy -12.70%
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
