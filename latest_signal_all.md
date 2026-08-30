# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-30 15:01:20**
- 데이터 기준일(일봉): **2026-08-28**
- 데이터 기준일(주봉): **2026-08-24**
- VXN 기준일: **2026-08-27** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 716.43
- Weekly RSI14: **58.14**
- 52W MA: 643.01 / gap: **11.42%**
- 104W MA gap: **24.43%**
- 52W MA 13W slope: **6.63%**
- VXN: **20.24** / 5D change: -3.02

## Daily trigger: 실제 매수 타이밍

- QQQ close: 716.43
- Daily RSI14: **51.90**
- 20D gap: **-0.21%**
- 50D gap: **0.62%**
- 200D gap: **9.51%**
- MACD hist: -0.4934 / change: 0.0944
- ATR14%: **1.46%**
- 20D high drawdown: **-2.14%**

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

- 데이터 기준일(주가): **2026-08-28**
- 실행시간(UTC): **2026-08-30 15:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.63 / 4주 변화 -21.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 -1.0 bp
- 10Y Real Yield (DFII10): 2.34 / 4주 변화 -7.0 bp
- VIX (VIXCLS): 14.51
- NFCI: -0.566

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.234465
- MA60: 9.128005
- gap: -9.79%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.39164
- MA60: 0.403078
- gap: -2.84%
- MA60_slope_proxy: 0.019061
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-28**
- 실행시간(UTC): **2026-08-30 15:00:46**

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
- close: 678.4
- MA50: 680.4033 / gap50: -0.29%
- MA200: 625.3848 / gap200: 8.48%

## Relative Strength
- RS vs FTSE gap: 0.02% / slope_proxy: 0.002868
- RS vs Peers gap: 0.92% / slope_proxy: 0.01944

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-30 15:00:53**

## Commodity Regime

- WTI ref (CL=F): 83.40 / 5D -4.20%
- Brent ref (BZ=F): 88.10 / 5D -6.66%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.70
- Gas ref (NG=F): 2.89 / 5D 4.15%

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

- close: 59.10
- MA20 / MA60 / MA200: 58.29 / 55.34 / 51.67
- gap20 / gap60: 1.39% / 6.79%
- 5D return: -3.59%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.942884
- ratio_MA60: 0.955746
- ratio_gap: -1.35%
- ratio_slope_proxy(20d): -0.013540

### Volume (if available)

- volume: 4429000.00
- volume_MA20: 7931980.00
- volume_ratio: 0.56

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.53
- MA20 / MA60 / MA200: 17.91 / 17.34 / 16.29
- gap20 / gap60: 3.48% / 6.88%
- 5D return: -0.40%
- 20D high/low: 18.60 / 17.25

### Relative Strength

- ratio: 0.521238
- ratio_MA60: 0.496260
- ratio_gap: 5.03%
- ratio_slope_proxy(20d): -0.002870

### Volume (if available)

- volume: 22085100.00
- volume_MA20: 18371975.00
- volume_ratio: 1.20

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

- close: 5.80
- MA20 / MA60 / MA200: 5.64 / 5.45 / 5.51
- gap20 / gap60: 2.87% / 6.48%
- 5D return: -2.03%
- 20D high/low: 6.01 / 5.14

### Relative Strength

- ratio: 0.013865
- ratio_MA60: 0.013789
- ratio_gap: 0.55%
- ratio_slope_proxy(20d): -0.000461

### Volume (if available)

- volume: 34881300.00
- volume_MA20: 40202240.00
- volume_ratio: 0.87

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

- close: 14.18
- MA20 / MA60 / MA200: 13.78 / 12.88 / 11.19
- gap20 / gap60: 2.91% / 10.10%
- 5D return: -0.21%
- 20D high/low: 14.48 / 12.43

### Relative Strength

- ratio: 0.050225
- ratio_MA60: 0.050301
- ratio_gap: -0.15%
- ratio_slope_proxy(20d): -0.000979

### Volume (if available)

- volume: 6155200.00
- volume_MA20: 13353395.00
- volume_ratio: 0.46

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-28**
- 실행시간(UTC): **2026-08-30 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -21.0 bp / latest 2.63
- IG OAS 4주 변화: -1.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -7.0 bp / latest 2.34
- VIX: 14.51
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 10.02% / slope_proxy: 0.024269
- GDXJ/GLD gap: 14.38% / slope_proxy: 0.005396

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 60.611451 | ATR14%: 4.83%
- MA20 gap: 5.79% | MA50 gap: 16.07% | MA200 gap: -1.88%
- vol_ratio(Volume/Vol20): 1.365234 | gap_open: 0.96%
- RS vs SILJ gap: -0.86% / slope_proxy: 0.002476
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
- close: 9.52 | RSI14: 62.345883 | ATR14%: 5.98%
- MA20 gap: 7.36% | MA50 gap: 28.03% | MA200 gap: 9.02%
- vol_ratio(Volume/Vol20): 1.06365 | gap_open: 1.40%
- SilverMarginGate: SI=67.786003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.80% / slope_proxy: 0.005253
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
- close: 23.825001 | RSI14: 46.571271 | ATR14%: 8.27%
- MA20 gap: -7.01% | MA50 gap: 2.83% | MA200 gap: -19.39%
- vol_ratio(Volume/Vol20): 1.298157 | gap_open: 0.15%
- RS vs SILJ gap: -13.61% / slope_proxy: -0.105423
- RS vs GDXJ gap: -16.65% / slope_proxy: -0.030524
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

- 실행시간(UTC): **2026-08-30 15:01:17**
- 데이터 기준일(주가): **2026-08-28**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **True**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.63 / 4주 변화 -0.21 bp-ish / 2026-08-27
- IG OAS: 0.79 / 4주 변화 -0.01 bp-ish / 2026-08-27
- 10Y Real Yield: 2.34 / 4주 변화 -0.07 bp-ish / 2026-08-27
- VIX: 14.51 / 4주 변화 -2.58 / 2026-08-27
- NFCI: -0.57 / 4주 변화 -0.10 / 2026-08-21

### Leadership ratios

- GDX/GLD: gap 15.14% / slope_proxy 19.12%
- GDXJ/GLD: gap 14.38% / slope_proxy 18.67%
- SILJ/SLV: gap 10.02% / slope_proxy 11.62%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.19 | RSI14: 57.54 | ATR14%: 5.40%
- MA20/50/200 gap: 4.22% / 22.12% / 39.68%
- 5D return: -3.32% | 20D drawdown: -7.95% | vol_ratio: 1.17
- RS vs GDXJ: gap 3.23% / slope_proxy 8.12%
- FundamentalScore: 88 | TechnicalScore: 80 | RegimeScore: 100 | OverallScore: **87.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.72 | RSI14: 67.36 | ATR14%: 4.48%
- MA20/50/200 gap: 9.31% / 29.04% / 10.97%
- 5D return: -2.03% | 20D drawdown: -5.51% | vol_ratio: 2.62
- RS vs GDXJ: gap 8.30% / slope_proxy 6.08%
- FundamentalScore: 82 | TechnicalScore: 80 | RegimeScore: 100 | OverallScore: **84.9**
- Checks:
  - sector_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.54 | RSI14: 58.18 | ATR14%: 5.22%
- MA20/50/200 gap: 3.11% / 19.05% / 3.62%
- 5D return: -5.52% | 20D drawdown: -6.67% | vol_ratio: 0.50
- RS vs GDXJ: gap -0.49% / slope_proxy 0.93%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **65.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.66 | RSI14: 70.00 | ATR14%: 5.45%
- MA20/50/200 gap: 16.11% / 34.97% / 40.24%
- 5D return: 6.83% | 20D drawdown: -1.85% | vol_ratio: 0.73
- RS vs GDXJ: gap 15.26% / slope_proxy 4.79%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **62.2**
- Checks:
  - sector_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.97 | RSI14: 50.21 | ATR14%: 5.82%
- MA20/50/200 gap: 5.71% / 25.92% / 56.61%
- 5D return: 4.95% | 20D drawdown: -4.51% | vol_ratio: 1.77
- RS vs SILJ: gap 11.61% / slope_proxy 7.68%
- FundamentalScore: 86 | TechnicalScore: 80 | RegimeScore: 75 | OverallScore: **81.7**
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
- close: 10.76 | RSI14: 54.87 | ATR14%: 6.37%
- MA20/50/200 gap: 6.02% / 21.36% / 10.29%
- 5D return: 1.32% | 20D drawdown: -4.78% | vol_ratio: 1.47
- RS vs SILJ: gap 5.25% / slope_proxy 9.00%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.52 | RSI14: 57.03 | ATR14%: 6.06%
- MA20/50/200 gap: 7.36% / 28.03% / 9.02%
- 5D return: -1.60% | 20D drawdown: -4.99% | vol_ratio: 1.06
- RS vs SILJ: gap 11.80% / slope_proxy 10.76%
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
- close: 20.38 | RSI14: 66.28 | ATR14%: 5.09%
- MA20/50/200 gap: 9.79% / 22.97% / 8.20%
- 5D return: -1.64% | 20D drawdown: -4.90% | vol_ratio: 0.75
- RS vs SILJ: gap 6.84% / slope_proxy 10.59%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.47 | RSI14: 52.82 | ATR14%: 5.54%
- MA20/50/200 gap: 5.82% / 17.10% / 8.87%
- 5D return: 0.95% | 20D drawdown: -3.36% | vol_ratio: 1.23
- RS vs SILJ: gap 0.79% / slope_proxy 5.77%
- FundamentalScore: 60 | TechnicalScore: 80 | RegimeScore: 75 | OverallScore: **70.0**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.00 | RSI14: 54.84 | ATR14%: 4.59%
- MA20/50/200 gap: 5.79% / 16.07% / -1.89%
- 5D return: 1.01% | 20D drawdown: -3.85% | vol_ratio: 1.37
- RS vs SILJ: gap -0.86% / slope_proxy -3.92%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **57.9**
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
- close: 5.44 | RSI14: 57.21 | ATR14%: 5.61%
- MA20/50/200 gap: 6.02% / 16.79% / -6.63%
- 5D return: 0.93% | 20D drawdown: -5.23% | vol_ratio: 1.20
- RS vs SILJ: gap -1.78% / slope_proxy 4.15%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **56.1**
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
- close: 23.83 | RSI14: 39.11 | ATR14%: 8.32%
- MA20/50/200 gap: -7.01% / 2.83% / -19.39%
- 5D return: -11.99% | 20D drawdown: -14.61% | vol_ratio: 1.30
- RS vs SILJ: gap -13.61% / slope_proxy -9.53%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **44.4**
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
