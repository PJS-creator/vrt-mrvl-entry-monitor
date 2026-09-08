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

- 실행시간(UTC): **2026-09-08 15:01:40**
- 데이터 기준일(일봉): **2026-09-08**
- 데이터 기준일(주봉): **2026-09-07**
- VXN 기준일: **2026-09-04** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 718.95
- Weekly RSI14: **58.66**
- 52W MA: 648.41 / gap: **10.88%**
- 104W MA gap: **23.79%**
- 52W MA 13W slope: **6.26%**
- VXN: **20.04** / 5D change: 0.12

## Daily trigger: 실제 매수 타이밍

- QQQ close: 718.96
- Daily RSI14: **53.63**
- 20D gap: **0.21%**
- 50D gap: **1.07%**
- 200D gap: **9.36%**
- MACD hist: -0.0404 / change: 0.2459
- ATR14%: **1.28%**
- 20D high drawdown: **-1.79%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
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

- 데이터 기준일(주가): **2026-09-08**
- 실행시간(UTC): **2026-09-08 15:00:58**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.65 / 4주 변화 -6.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 -1.0 bp
- VIX (VIXCLS): 15.3
- NFCI: -0.558

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.321136
- MA60: 9.299596
- gap: 0.23%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.398015
- MA60: 0.394876
- gap: 0.79%
- MA60_slope_proxy: 0.004096
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-08**
- 실행시간(UTC): **2026-09-08 15:01:03**

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
- TERM_SPREAD_10Y_POLICY: 132.37 bp / 4주 변화 16.19 bp
- CURVE_10s5s: 46.55 bp / 4주 변화 -1.07 bp

## NWG Price
- close: 693.2
- MA50: 685.6307 / gap50: 1.10%
- MA200: 628.6456 / gap200: 10.27%

## Relative Strength
- RS vs FTSE gap: 0.78% / slope_proxy: 0.002403
- RS vs Peers gap: -0.38% / slope_proxy: 0.014536

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-08 15:01:12**

## Commodity Regime

- WTI ref (CL=F): 92.78 / 5D 8.19%
- Brent ref (BZ=F): 97.82 / 5D 8.10%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.04
- Gas ref (NG=F): 2.88 / 5D -1.84%

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

- close: 61.05
- MA20 / MA60 / MA200: 59.73 / 55.72 / 52.24
- gap20 / gap60: 2.22% / 9.58%
- 5D return: 1.45%
- 20D high/low: 61.52 / 57.70

### Relative Strength

- ratio: 0.941480
- ratio_MA60: 0.950779
- ratio_gap: -0.98%
- ratio_slope_proxy(20d): -0.017164

### Volume (if available)

- volume: 1929682.00
- volume_MA20: 6751759.10
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.86
- MA20 / MA60 / MA200: 18.62 / 17.63 / 16.52
- gap20 / gap60: 12.03% / 18.35%
- 5D return: 7.80%
- 20D high/low: 20.86 / 17.25

### Relative Strength

- ratio: 0.537213
- ratio_MA60: 0.498832
- ratio_gap: 7.69%
- ratio_slope_proxy(20d): 0.001049

### Volume (if available)

- volume: 9298257.00
- volume_MA20: 20266992.85
- volume_ratio: 0.46

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.87
- MA20 / MA60 / MA200: 5.84 / 5.44 / 5.57
- gap20 / gap60: 0.51% / 7.96%
- 5D return: 1.03%
- 20D high/low: 6.22 / 5.60

### Relative Strength

- ratio: 0.013512
- ratio_MA60: 0.013749
- ratio_gap: -1.73%
- ratio_slope_proxy(20d): -0.000353

### Volume (if available)

- volume: 8944633.00
- volume_MA20: 39163946.65
- volume_ratio: 0.23

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

- close: 14.72
- MA20 / MA60 / MA200: 14.21 / 13.06 / 11.40
- gap20 / gap60: 3.56% / 12.69%
- 5D return: 0.53%
- 20D high/low: 15.11 / 13.22

### Relative Strength

- ratio: 0.053055
- ratio_MA60: 0.049980
- ratio_gap: 6.15%
- ratio_slope_proxy(20d): -0.001434

### Volume (if available)

- volume: 6303692.00
- volume_MA20: 13107509.60
- volume_ratio: 0.48

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-08**
- 실행시간(UTC): **2026-09-08 15:01:25**

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
- VIX: 15.3
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 8.84% / slope_proxy: 0.028197
- GDXJ/GLD gap: 13.90% / slope_proxy: 0.012314

## VZLA (Vizsla Silver)
- close: 4.145 | RSI14: 59.860665 | ATR14%: 4.84%
- MA20 gap: 5.48% | MA50 gap: 17.26% | MA200 gap: 2.04%
- vol_ratio(Volume/Vol20): 0.222099 | gap_open: 0.00%
- RS vs SILJ gap: 2.19% / slope_proxy: 0.000587
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
- close: 10.095 | RSI14: 62.588178 | ATR14%: 5.81%
- MA20 gap: 6.66% | MA50 gap: 29.16% | MA200 gap: 13.88%
- vol_ratio(Volume/Vol20): 0.175636 | gap_open: 0.40%
- SilverMarginGate: SI=66.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.97% / slope_proxy: 0.012074
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
- close: 23.075001 | RSI14: 45.937582 | ATR14%: 7.84%
- MA20 gap: -8.55% | MA50 gap: -0.04% | MA200 gap: -22.98%
- vol_ratio(Volume/Vol20): 0.26391 | gap_open: 1.06%
- RS vs SILJ gap: -14.34% / slope_proxy: -0.091217
- RS vs GDXJ gap: -16.66% / slope_proxy: -0.027479
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

- 실행시간(UTC): **2026-09-08 15:01:37**
- 데이터 기준일(주가): **2026-09-08**

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
- VIX: 15.30 / 4주 변화 -0.16 / 2026-09-07
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-08-28

### Leadership ratios

- GDX/GLD: gap 14.48% / slope_proxy 9.99%
- GDXJ/GLD: gap 13.90% / slope_proxy 8.28%
- SILJ/SLV: gap 8.87% / slope_proxy 3.88%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 92.31%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.24 | RSI14: 56.72 | ATR14%: 4.76%
- MA20/50/200 gap: -0.15% / 18.64% / 37.74%
- 5D return: 1.78% | 20D drawdown: -7.51% | vol_ratio: 0.17
- RS vs GDXJ: gap 2.62% / slope_proxy -5.00%
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
- close: 8.04 | RSI14: 71.10 | ATR14%: 4.73%
- MA20/50/200 gap: 6.55% / 28.01% / 14.71%
- 5D return: 5.10% | 20D drawdown: -1.59% | vol_ratio: 0.29
- RS vs GDXJ: gap 11.51% / slope_proxy 6.31%
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
- close: 1.59 | RSI14: 55.36 | ATR14%: 4.67%
- MA20/50/200 gap: 2.09% / 19.57% / 6.61%
- 5D return: 5.30% | 20D drawdown: -3.64% | vol_ratio: 0.47
- RS vs GDXJ: gap 2.29% / slope_proxy 0.62%
- FundamentalScore: 70 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **76.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.85 | RSI14: 75.41 | ATR14%: 6.19%
- MA20/50/200 gap: 13.30% / 35.01% / 47.86%
- 5D return: 9.20% | 20D drawdown: 0.00% | vol_ratio: 0.47
- RS vs GDXJ: gap 20.07% / slope_proxy 23.36%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.58 | RSI14: 63.44 | ATR14%: 5.48%
- MA20/50/200 gap: 3.74% / 19.86% / 8.30%
- 5D return: 3.60% | 20D drawdown: -3.94% | vol_ratio: 0.11
- RS vs SILJ: gap 5.86% / slope_proxy 9.20%
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
- close: 10.10 | RSI14: 67.30 | ATR14%: 6.46%
- MA20/50/200 gap: 6.66% / 29.16% / 13.88%
- 5D return: 7.85% | 20D drawdown: -3.12% | vol_ratio: 0.18
- RS vs SILJ: gap 14.97% / slope_proxy 4.98%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 29.45 | RSI14: 66.58 | ATR14%: 5.91%
- MA20/50/200 gap: 6.84% / 26.04% / 60.13%
- 5D return: 5.50% | 20D drawdown: -1.22% | vol_ratio: 0.14
- RS vs SILJ: gap 13.29% / slope_proxy -0.32%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **67.7**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.23 | RSI14: 64.20 | ATR14%: 5.94%
- MA20/50/200 gap: 4.34% / 22.08% / 13.98%
- 5D return: 4.86% | 20D drawdown: -2.09% | vol_ratio: 0.16
- RS vs SILJ: gap 7.75% / slope_proxy -0.09%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **65.9**
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
- close: 7.41 | RSI14: 59.07 | ATR14%: 5.70%
- MA20/50/200 gap: 0.93% / 13.47% / 6.83%
- 5D return: 1.58% | 20D drawdown: -4.08% | vol_ratio: 0.27
- RS vs SILJ: gap -0.92% / slope_proxy -5.34%
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
- close: 4.14 | RSI14: 66.38 | ATR14%: 5.11%
- MA20/50/200 gap: 5.48% / 17.26% / 2.04%
- 5D return: 2.35% | 20D drawdown: -0.60% | vol_ratio: 0.22
- RS vs SILJ: gap 2.19% / slope_proxy 1.97%
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
- close: 5.34 | RSI14: 57.53 | ATR14%: 5.96%
- MA20/50/200 gap: 0.09% / 13.40% / -9.06%
- 5D return: -0.65% | 20D drawdown: -7.06% | vol_ratio: 0.31
- RS vs SILJ: gap -3.23% / slope_proxy -2.21%
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
- close: 23.08 | RSI14: 46.56 | ATR14%: 8.33%
- MA20/50/200 gap: -8.55% / -0.04% / -22.98%
- 5D return: -1.52% | 20D drawdown: -17.29% | vol_ratio: 0.26
- RS vs SILJ: gap -14.34% / slope_proxy -21.03%
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
