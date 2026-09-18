# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-18 15:01:11**
- 데이터 기준일(일봉): **2026-09-18**
- 데이터 기준일(주봉): **2026-09-14**
- VXN 기준일: **2026-09-17** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 716.92
- Weekly RSI14: **57.90**
- 52W MA: 650.65 / gap: **10.19%**
- 104W MA gap: **22.96%**
- 52W MA 13W slope: **5.90%**
- VXN: **19.96** / 5D change: -3.37

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.36
- Daily RSI14: **53.34**
- 20D gap: **0.61%**
- 50D gap: **1.06%**
- 200D gap: **8.40%**
- MACD hist: -0.1928 / change: 0.5150
- ATR14%: **1.26%**
- 20D high drawdown: **-0.52%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
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

- 데이터 기준일(주가): **2026-09-18**
- 실행시간(UTC): **2026-09-18 15:00:51**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -5.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.68 / 4주 변화 33.0 bp
- VIX (VIXCLS): 15.44
- NFCI: -0.56

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.314319
- MA60: 9.101308
- gap: -8.65%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.423323
- MA60: 0.38889
- gap: 8.85%
- MA60_slope_proxy: -0.010554
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-18**
- 실행시간(UTC): **2026-09-18 15:00:52**

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
- TERM_SPREAD_10Y_POLICY: 149.21 bp / 4주 변화 20.2 bp
- CURVE_10s5s: 43.54 bp / 4주 변화 -5.02 bp

## NWG Price
- close: 700.2
- MA50: 689.0888 / gap50: 1.61%
- MA200: 631.8425 / gap200: 10.82%

## Relative Strength
- RS vs FTSE gap: 2.66% / slope_proxy: 0.001625
- RS vs Peers gap: 4.21% / slope_proxy: 0.011235

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-18 15:00:59**

## Commodity Regime

- WTI ref (CL=F): 97.07 / 5D -2.98%
- Brent ref (BZ=F): 99.59 / 5D -4.80%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.52
- Gas ref (NG=F): 2.93 / 5D 3.57%

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

- close: 59.20
- MA20 / MA60 / MA200: 60.18 / 56.52 / 52.80
- gap20 / gap60: -1.62% / 4.74%
- 5D return: -3.68%
- 20D high/low: 63.52 / 58.14

### Relative Strength

- ratio: 0.916558
- ratio_MA60: 0.942406
- ratio_gap: -2.74%
- ratio_slope_proxy(20d): -0.015634

### Volume (if available)

- volume: 2752555.00
- volume_MA20: 7297292.75
- volume_ratio: 0.38

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.88
- MA20 / MA60 / MA200: 20.01 / 18.23 / 16.88
- gap20 / gap60: 4.32% / 14.51%
- 5D return: -1.53%
- 20D high/low: 21.77 / 17.76

### Relative Strength

- ratio: 0.560102
- ratio_MA60: 0.508678
- ratio_gap: 10.11%
- ratio_slope_proxy(20d): 0.012495

### Volume (if available)

- volume: 3930200.00
- volume_MA20: 22392000.00
- volume_ratio: 0.18

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

- close: 5.65
- MA20 / MA60 / MA200: 5.78 / 5.46 / 5.63
- gap20 / gap60: -2.21% / 3.54%
- 5D return: -0.35%
- 20D high/low: 6.22 / 5.45

### Relative Strength

- ratio: 0.014200
- ratio_MA60: 0.013743
- ratio_gap: 3.32%
- ratio_slope_proxy(20d): -0.000109

### Volume (if available)

- volume: 8946765.00
- volume_MA20: 39592583.25
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.37
- MA20 / MA60 / MA200: 14.69 / 13.52 / 11.68
- gap20 / gap60: -2.18% / 6.23%
- 5D return: -8.84%
- 20D high/low: 15.76 / 14.03

### Relative Strength

- ratio: 0.052709
- ratio_MA60: 0.050690
- ratio_gap: 3.98%
- ratio_slope_proxy(20d): 0.000218

### Volume (if available)

- volume: 2055013.00
- volume_MA20: 13038710.65
- volume_ratio: 0.16

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

- 데이터 기준일(주가): **2026-09-18**
- 실행시간(UTC): **2026-09-18 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -5.0 bp / latest 2.7
- IG OAS 4주 변화: -4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 33.0 bp / latest 2.68
- VIX: 15.44
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 0.02% / slope_proxy: 0.023604
- GDXJ/GLD gap: 7.40% / slope_proxy: 0.014058

## VZLA (Vizsla Silver)
- close: 3.965 | RSI14: 53.45121 | ATR14%: 5.32%
- MA20 gap: -0.50% | MA50 gap: 8.75% | MA200 gap: -1.79%
- vol_ratio(Volume/Vol20): 0.147902 | gap_open: 0.25%
- RS vs SILJ gap: 4.54% / slope_proxy: -6.4e-05
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
- close: 8.995 | RSI14: 49.090137 | ATR14%: 6.88%
- MA20 gap: -5.74% | MA50 gap: 9.19% | MA200 gap: 0.09%
- vol_ratio(Volume/Vol20): 0.38122 | gap_open: 1.57%
- SilverMarginGate: SI=66.864998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.44% / slope_proxy: 0.016654
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
- close: 21.059999 | RSI14: 42.24826 | ATR14%: 7.77%
- MA20 gap: -8.56% | MA50 gap: -7.80% | MA200 gap: -30.70%
- vol_ratio(Volume/Vol20): 0.253749 | gap_open: 2.74%
- RS vs SILJ gap: -13.28% / slope_proxy: -0.081955
- RS vs GDXJ gap: -16.37% / slope_proxy: -0.025681
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

- 실행시간(UTC): **2026-09-18 15:01:09**
- 데이터 기준일(주가): **2026-09-18**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.70 / 4주 변화 -0.05 bp-ish / 2026-09-17
- IG OAS: 0.78 / 4주 변화 -0.04 bp-ish / 2026-09-17
- 10Y Real Yield: 2.68 / 4주 변화 0.27 bp-ish / 2026-09-16
- VIX: 15.44 / 4주 변화 -0.57 / 2026-09-17
- NFCI: -0.56 / 4주 변화 -0.07 / 2026-09-11

### Leadership ratios

- GDX/GLD: gap 7.72% / slope_proxy -2.52%
- GDXJ/GLD: gap 7.40% / slope_proxy -2.00%
- SILJ/SLV: gap 0.01% / slope_proxy -2.50%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 84.62%, above200 30.77%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.25 | RSI14: 50.87 | ATR14%: 4.62%
- MA20/50/200 gap: -0.46% / 13.41% / 34.33%
- 5D return: 1.69% | 20D drawdown: -7.41% | vol_ratio: 0.21
- RS vs GDXJ: gap 6.89% / slope_proxy 5.25%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **79.3**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.57 | RSI14: 47.51 | ATR14%: 5.19%
- MA20/50/200 gap: -3.25% / 13.53% / 7.14%
- 5D return: -4.18% | 20D drawdown: -9.23% | vol_ratio: 0.17
- RS vs GDXJ: gap 8.25% / slope_proxy 3.97%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **60.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.61 | RSI14: 46.84 | ATR14%: 6.68%
- MA20/50/200 gap: -0.48% / 15.81% / 33.12%
- 5D return: 3.16% | 20D drawdown: -6.45% | vol_ratio: 0.19
- RS vs GDXJ: gap 11.66% / slope_proxy 13.45%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **64.5**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.46 | RSI14: 43.33 | ATR14%: 5.06%
- MA20/50/200 gap: -3.73% / 6.74% / -2.42%
- 5D return: 0.69% | 20D drawdown: -10.98% | vol_ratio: 0.17
- RS vs GDXJ: gap -0.09% / slope_proxy -3.06%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **46.8**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 28.04 | RSI14: 50.27 | ATR14%: 6.30%
- MA20/50/200 gap: 0.14% / 13.29% / 47.09%
- 5D return: 0.25% | 20D drawdown: -6.19% | vol_ratio: 0.22
- RS vs SILJ: gap 11.58% / slope_proxy 13.00%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **78.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.04 | RSI14: 42.04 | ATR14%: 5.57%
- MA20/50/200 gap: -5.36% / 5.71% / 1.11%
- 5D return: -1.38% | 20D drawdown: -12.47% | vol_ratio: 0.15
- RS vs SILJ: gap 2.29% / slope_proxy 1.53%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **60.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.06 | RSI14: 45.67 | ATR14%: 7.15%
- MA20/50/200 gap: -5.14% / 9.90% / 0.76%
- 5D return: -6.17% | 20D drawdown: -13.18% | vol_ratio: 0.38
- RS vs SILJ: gap 8.15% / slope_proxy 0.52%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **57.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.96 | RSI14: 48.89 | ATR14%: 5.51%
- MA20/50/200 gap: -0.50% / 8.75% / -1.79%
- 5D return: -0.13% | 20D drawdown: -4.92% | vol_ratio: 0.15
- RS vs SILJ: gap 4.54% / slope_proxy 7.54%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **56.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.05 | RSI14: 42.55 | ATR14%: 6.01%
- MA20/50/200 gap: -3.50% / 6.29% / -14.34%
- 5D return: 0.10% | 20D drawdown: -11.93% | vol_ratio: 0.31
- RS vs SILJ: gap 0.63% / slope_proxy 0.72%
- FundamentalScore: 68 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **54.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 18.68 | RSI14: 40.16 | ATR14%: 5.46%
- MA20/50/200 gap: -6.68% / 5.36% / -2.56%
- 5D return: -5.54% | 20D drawdown: -12.81% | vol_ratio: 0.17
- RS vs SILJ: gap 1.58% / slope_proxy -3.15%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **50.4**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.28 | RSI14: 32.03 | ATR14%: 6.31%
- MA20/50/200 gap: -10.94% / -4.38% / -10.34%
- 5D return: -3.22% | 20D drawdown: -18.75% | vol_ratio: 0.18
- RS vs SILJ: gap -9.06% / slope_proxy -8.85%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **42.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.06 | RSI14: 35.99 | ATR14%: 7.00%
- MA20/50/200 gap: -8.56% / -7.80% / -30.70%
- 5D return: -0.57% | 20D drawdown: -22.20% | vol_ratio: 0.25
- RS vs SILJ: gap -13.28% / slope_proxy -16.44%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **34.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
