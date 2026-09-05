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

- 실행시간(UTC): **2026-09-05 00:22:29**
- 데이터 기준일(일봉): **2026-09-03**
- 데이터 기준일(주봉): **2026-08-31**
- VXN 기준일: **2026-09-03** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 718.96
- Weekly RSI14: **58.66**
- 52W MA: 645.81 / gap: **11.33%**
- 104W MA gap: **24.30%**
- 52W MA 13W slope: **6.49%**
- VXN: **20.16** / 5D change: -0.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.67
- Daily RSI14: **52.87**
- 20D gap: **-0.01%**
- 50D gap: **0.93%**
- 200D gap: **9.37%**
- MACD hist: -0.6769 / change: 0.4577
- ATR14%: **1.36%**
- 20D high drawdown: **-1.97%**

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

- 데이터 기준일(주가): **2026-09-03**
- 실행시간(UTC): **2026-09-05 00:21:57**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.65 / 4주 변화 -6.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 -1.0 bp
- VIX (VIXCLS): 14.32
- NFCI: -0.558

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.818724
- MA60: 9.287092
- gap: -5.04%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.377904
- MA60: 0.396719
- gap: -4.74%
- MA60_slope_proxy: 0.008235
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-03**
- 실행시간(UTC): **2026-09-05 00:22:00**

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
- TERM_SPREAD_10Y_POLICY: 142.1 bp / 4주 변화 29.08 bp
- CURVE_10s5s: 47.35 bp / 4주 변화 -1.96 bp

## NWG Price
- close: 697.4
- MA50: 683.236 / gap50: 2.07%
- MA200: 626.8897 / gap200: 11.25%

## Relative Strength
- RS vs FTSE gap: 1.80% / slope_proxy: 0.002618
- RS vs Peers gap: 0.59% / slope_proxy: 0.017653

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-05 00:22:06**

## Commodity Regime

- WTI ref (CL=F): 91.22 / 5D 9.38%
- Brent ref (BZ=F): 95.83 / 5D 7.30%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.61
- Gas ref (NG=F): 2.94 / 5D 1.77%

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

- close: 60.61
- MA20 / MA60 / MA200: 59.40 / 55.58 / 52.05
- gap20 / gap60: 2.03% / 9.06%
- 5D return: 2.43%
- 20D high/low: 61.52 / 55.91

### Relative Strength

- ratio: 0.937945
- ratio_MA60: 0.952225
- ratio_gap: -1.50%
- ratio_slope_proxy(20d): -0.015892

### Volume (if available)

- volume: 6670364.00
- volume_MA20: 7115298.20
- volume_ratio: 0.94

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.51
- MA20 / MA60 / MA200: 18.33 / 17.53 / 16.45
- gap20 / gap60: 11.87% / 16.99%
- 5D return: 12.38%
- 20D high/low: 20.86 / 17.25

### Relative Strength

- ratio: 0.537897
- ratio_MA60: 0.498350
- ratio_gap: 7.94%
- ratio_slope_proxy(20d): -0.000106

### Volume (if available)

- volume: 18778802.00
- volume_MA20: 20419180.10
- volume_ratio: 0.92

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

- close: 6.02
- MA20 / MA60 / MA200: 5.80 / 5.44 / 5.55
- gap20 / gap60: 3.74% / 10.61%
- 5D return: 4.88%
- 20D high/low: 6.22 / 5.26

### Relative Strength

- ratio: 0.014006
- ratio_MA60: 0.013769
- ratio_gap: 1.73%
- ratio_slope_proxy(20d): -0.000377

### Volume (if available)

- volume: 38938342.00
- volume_MA20: 41600492.10
- volume_ratio: 0.94

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

- close: 14.48
- MA20 / MA60 / MA200: 14.13 / 13.01 / 11.33
- gap20 / gap60: 2.47% / 11.31%
- 5D return: 0.00%
- 20D high/low: 15.11 / 13.22

### Relative Strength

- ratio: 0.049785
- ratio_MA60: 0.050075
- ratio_gap: -0.58%
- ratio_slope_proxy(20d): -0.001392

### Volume (if available)

- volume: 7446273.00
- volume_MA20: 13534828.65
- volume_ratio: 0.55

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

- 데이터 기준일(주가): **2026-09-04**
- 실행시간(UTC): **2026-09-05 00:22:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -1.0 bp / latest 2.42
- VIX: 14.32
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 9.96% / slope_proxy: 0.027162
- GDXJ/GLD gap: 15.56% / slope_proxy: 0.010102

## VZLA (Vizsla Silver)
- close: 4.17 | RSI14: 62.567521 | ATR14%: 4.83%
- MA20 gap: 6.83% | MA50 gap: 19.14% | MA200 gap: 2.54%
- vol_ratio(Volume/Vol20): 0.675115 | gap_open: 2.89%
- RS vs SILJ gap: 1.18% / slope_proxy: 0.001243
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
- close: 10.42 | RSI14: 68.304909 | ATR14%: 5.80%
- MA20 gap: 11.66% | MA50 gap: 35.75% | MA200 gap: 18.17%
- vol_ratio(Volume/Vol20): 0.870307 | gap_open: 3.14%
- SilverMarginGate: SI=66.82 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 17.82% / slope_proxy: 0.009897
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
- close: 23.299999 | RSI14: 46.325991 | ATR14%: 8.23%
- MA20 gap: -9.11% | MA50 gap: 0.95% | MA200 gap: -21.91%
- vol_ratio(Volume/Vol20): 0.996192 | gap_open: 4.09%
- RS vs SILJ gap: -15.55% / slope_proxy: -0.096476
- RS vs GDXJ gap: -18.68% / slope_proxy: -0.029026
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

- 실행시간(UTC): **2026-09-05 00:22:26**
- 데이터 기준일(주가): **2026-09-04**

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

- HY OAS: 2.65 / 4주 변화 -0.06 bp-ish / 2026-09-03
- IG OAS: 0.81 / 4주 변화 0.03 bp-ish / 2026-09-03
- 10Y Real Yield: 2.42 / 4주 변화 -0.01 bp-ish / 2026-09-03
- VIX: 14.32 / 4주 변화 -0.83 / 2026-09-03
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-08-28

### Leadership ratios

- GDX/GLD: gap 15.40% / slope_proxy 9.67%
- GDXJ/GLD: gap 15.56% / slope_proxy 9.28%
- SILJ/SLV: gap 9.96% / slope_proxy 5.55%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 76.92%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.35 | RSI14: 52.85 | ATR14%: 5.02%
- MA20/50/200 gap: 1.55% / 21.52% / 40.15%
- 5D return: -5.22% | 20D drawdown: -6.50% | vol_ratio: 0.72
- RS vs GDXJ: gap 1.60% / slope_proxy -3.57%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.11 | RSI14: 67.18 | ATR14%: 4.84%
- MA20/50/200 gap: 8.31% / 30.41% / 15.88%
- 5D return: 5.05% | 20D drawdown: -0.73% | vol_ratio: 0.49
- RS vs GDXJ: gap 10.18% / slope_proxy 7.30%
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
- close: 1.56 | RSI14: 46.67 | ATR14%: 4.81%
- MA20/50/200 gap: 0.61% / 18.11% / 4.69%
- 5D return: 1.30% | 20D drawdown: -5.45% | vol_ratio: 0.22
- RS vs GDXJ: gap 0.62% / slope_proxy -1.92%
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
- close: 2.68 | RSI14: 66.37 | ATR14%: 6.50%
- MA20/50/200 gap: 7.98% / 28.67% / 39.49%
- 5D return: 0.75% | 20D drawdown: -3.94% | vol_ratio: 0.41
- RS vs GDXJ: gap 12.96% / slope_proxy 14.04%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **62.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 29.82 | RSI14: 63.50 | ATR14%: 6.05%
- MA20/50/200 gap: 8.81% / 29.86% / 63.82%
- 5D return: 1.81% | 20D drawdown: 0.00% | vol_ratio: 1.41
- RS vs SILJ: gap 14.18% / slope_proxy -1.33%
- FundamentalScore: 86 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **80.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.47 | RSI14: 56.67 | ATR14%: 6.23%
- MA20/50/200 gap: 7.86% / 26.33% / 16.85%
- 5D return: 1.50% | 20D drawdown: 0.00% | vol_ratio: 1.06
- RS vs SILJ: gap 8.92% / slope_proxy 8.17%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 21.21 | RSI14: 63.52 | ATR14%: 5.48%
- MA20/50/200 gap: 8.77% / 25.04% / 11.98%
- 5D return: -1.03% | 20D drawdown: -1.03% | vol_ratio: 0.80
- RS vs SILJ: gap 7.90% / slope_proxy 13.25%
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
- close: 10.42 | RSI14: 66.25 | ATR14%: 6.14%
- MA20/50/200 gap: 11.66% / 35.75% / 18.17%
- 5D return: 3.99% | 20D drawdown: 0.00% | vol_ratio: 0.87
- RS vs SILJ: gap 17.82% / slope_proxy 11.60%
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
- close: 7.69 | RSI14: 60.06 | ATR14%: 5.67%
- MA20/50/200 gap: 5.07% / 18.68% / 11.23%
- 5D return: -0.52% | 20D drawdown: -0.52% | vol_ratio: 1.16
- RS vs SILJ: gap 1.31% / slope_proxy 0.56%
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
- close: 4.17 | RSI14: 62.58 | ATR14%: 4.92%
- MA20/50/200 gap: 6.83% / 19.14% / 2.54%
- 5D return: 0.24% | 20D drawdown: 0.00% | vol_ratio: 0.68
- RS vs SILJ: gap 1.18% / slope_proxy 0.31%
- FundamentalScore: 72 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **70.2**
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
- close: 5.54 | RSI14: 55.68 | ATR14%: 5.96%
- MA20/50/200 gap: 4.48% / 18.31% / -5.30%
- 5D return: -3.48% | 20D drawdown: -3.48% | vol_ratio: 0.93
- RS vs SILJ: gap -1.39% / slope_proxy -0.52%
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
- close: 23.30 | RSI14: 39.57 | ATR14%: 8.58%
- MA20/50/200 gap: -9.11% / 0.95% / -21.91%
- 5D return: -10.25% | 20D drawdown: -16.49% | vol_ratio: 1.00
- RS vs SILJ: gap -15.55% / slope_proxy -21.02%
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
