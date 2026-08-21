# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-21 15:01:09**
- 데이터 기준일(일봉): **2026-08-21**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-20** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 712.14
- Weekly RSI14: **57.24**
- 52W MA: 640.13 / gap: **11.25%**
- 104W MA gap: **24.20%**
- 52W MA 13W slope: **6.91%**
- VXN: **23.26** / 5D change: 2.03

## Daily trigger: 실제 매수 타이밍

- QQQ close: 712.20
- Daily RSI14: **49.51**
- 20D gap: **0.43%**
- 50D gap: **-0.16%**
- 200D gap: **9.28%**
- MACD hist: -0.1130 / change: -0.6714
- ATR14%: **1.59%**
- 20D high drawdown: **-2.71%**

## Checks

- weekly_good: **False**
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

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-21 15:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.35 / 4주 변화 -4.0 bp
- VIX (VIXCLS): 16.01
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.145446
- MA60: 9.225372
- gap: -11.71%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.422175
- MA60: 0.40092
- gap: 5.30%
- MA60_slope_proxy: 0.018189
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-21 15:00:46**

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
- TERM_SPREAD_10Y_POLICY: 129.01 bp / 4주 변화 -0.23 bp
- CURVE_10s5s: 48.56 bp / 4주 변화 1.84 bp

## NWG Price
- close: 683.6
- MA50: 675.8548 / gap50: 1.15%
- MA200: 623.7629 / gap200: 9.59%

## Relative Strength
- RS vs FTSE gap: 1.16% / slope_proxy: 0.002953
- RS vs Peers gap: 1.26% / slope_proxy: 0.016538

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-21 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 86.37 / 5D 4.82%
- Brent ref (BZ=F): 93.85 / 5D 6.02%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.48
- Gas ref (NG=F): 2.81 / 5D 3.00%

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

- close: 61.50
- MA20 / MA60 / MA200: 57.42 / 55.26 / 51.19
- gap20 / gap60: 7.10% / 11.30%
- 5D return: 5.38%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.966070
- ratio_MA60: 0.961857
- ratio_gap: 0.44%
- ratio_slope_proxy(20d): -0.012894

### Volume (if available)

- volume: 1825097.00
- volume_MA20: 8128979.85
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.14
- MA20 / MA60 / MA200: 18.44 / 17.84 / 16.61
- gap20 / gap60: 3.82% / 7.29%
- 5D return: 7.05%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.547326
- ratio_MA60: 0.511091
- ratio_gap: 7.09%
- ratio_slope_proxy(20d): -0.006225

### Volume (if available)

- volume: 5887129.00
- volume_MA20: 15543151.45
- volume_ratio: 0.38

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

- close: 5.93
- MA20 / MA60 / MA200: 5.49 / 5.49 / 5.47
- gap20 / gap60: 8.08% / 8.06%
- 5D return: 2.95%
- 20D high/low: 6.01 / 4.95

### Relative Strength

- ratio: 0.014344
- ratio_MA60: 0.013849
- ratio_gap: 3.58%
- ratio_slope_proxy(20d): -0.000535

### Volume (if available)

- volume: 6225398.00
- volume_MA20: 44259919.90
- volume_ratio: 0.14

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

- close: 14.29
- MA20 / MA60 / MA200: 13.44 / 12.72 / 11.04
- gap20 / gap60: 6.25% / 12.26%
- 5D return: 2.11%
- 20D high/low: 14.29 / 12.17

### Relative Strength

- ratio: 0.051412
- ratio_MA60: 0.050567
- ratio_gap: 1.67%
- ratio_slope_proxy(20d): -0.000576

### Volume (if available)

- volume: 3260017.00
- volume_MA20: 13472500.85
- volume_ratio: 0.24

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

- 데이터 기준일(주가): **2026-08-21**
- 실행시간(UTC): **2026-08-21 15:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.75
- IG OAS 4주 변화: 3.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: -4.0 bp / latest 2.35
- VIX: 16.01
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 7.49% / slope_proxy: 0.020489
- GDXJ/GLD gap: 14.94% / slope_proxy: 0.001333

## VZLA (Vizsla Silver)
- close: 3.8906 | RSI14: 62.292462 | ATR14%: 4.79%
- MA20 gap: 8.96% | MA50 gap: 14.38% | MA200 gap: -4.49%
- vol_ratio(Volume/Vol20): 0.253995 | gap_open: 3.36%
- RS vs SILJ gap: -4.19% / slope_proxy: 0.004095
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
- close: 9.715 | RSI14: 71.253203 | ATR14%: 5.71%
- MA20 gap: 20.54% | MA50 gap: 34.93% | MA200 gap: 12.72%
- vol_ratio(Volume/Vol20): 0.467983 | gap_open: 5.12%
- SilverMarginGate: SI=69.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.95% / slope_proxy: 0.001683
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
- close: 26.4 | RSI14: 55.860531 | ATR14%: 7.36%
- MA20 gap: 9.10% | MA50 gap: 13.63% | MA200 gap: -9.30%
- vol_ratio(Volume/Vol20): 0.421003 | gap_open: 4.82%
- RS vs SILJ gap: -7.24% / slope_proxy: -0.117213
- RS vs GDXJ gap: -12.83% / slope_proxy: -0.03191
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

- 실행시간(UTC): **2026-08-21 15:01:08**
- 데이터 기준일(주가): **2026-08-21**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

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

- HY OAS: 2.75 / 4주 변화 -0.02 bp-ish / 2026-08-20
- IG OAS: 0.82 / 4주 변화 0.03 bp-ish / 2026-08-20
- 10Y Real Yield: 2.35 / 4주 변화 -0.04 bp-ish / 2026-08-19
- VIX: 16.01 / 4주 변화 -2.69 / 2026-08-20
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 16.36% / slope_proxy 20.28%
- GDXJ/GLD: gap 14.89% / slope_proxy 18.40%
- SILJ/SLV: gap 7.53% / slope_proxy 8.26%
- Gold breadth proxy: above50 100.00%, above200 92.31%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.32 | RSI14: 82.70 | ATR14%: 5.87%
- MA20/50/200 gap: 16.33% / 28.25% / 44.28%
- 5D return: 1.98% | 20D drawdown: -1.71% | vol_ratio: 0.31
- RS vs GDXJ: gap 3.09% / slope_proxy 7.75%
- FundamentalScore: 88 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **77.1**
- Checks:
  - sector_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.60 | RSI14: 89.05 | ATR14%: 4.60%
- MA20/50/200 gap: 18.32% / 31.77% / 10.16%
- 5D return: 8.42% | 20D drawdown: 0.00% | vol_ratio: 0.29
- RS vs GDXJ: gap 4.64% / slope_proxy 5.89%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **74.4**
- Checks:
  - sector_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.63 | RSI14: 84.72 | ATR14%: 5.50%
- MA20/50/200 gap: 18.33% / 28.45% / 10.07%
- 5D return: 6.54% | 20D drawdown: -1.21% | vol_ratio: 0.54
- RS vs GDXJ: gap 3.15% / slope_proxy 11.05%
- FundamentalScore: 70 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **69.0**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.47 | RSI14: 73.98 | ATR14%: 5.60%
- MA20/50/200 gap: 18.24% / 32.06% / 32.37%
- 5D return: 6.01% | 20D drawdown: 0.00% | vol_ratio: 0.49
- RS vs GDXJ: gap 6.48% / slope_proxy -3.46%
- FundamentalScore: 55 | TechnicalScore: 25 | RegimeScore: 100 | OverallScore: **53.5**
- Checks:
  - sector_ok: **True**
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
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.69 | RSI14: 70.85 | ATR14%: 6.42%
- MA20/50/200 gap: 9.11% / 24.78% / 53.23%
- 5D return: 2.97% | 20D drawdown: -4.81% | vol_ratio: 0.35
- RS vs SILJ: gap 8.28% / slope_proxy 1.52%
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
- close: 10.86 | RSI14: 75.10 | ATR14%: 6.27%
- MA20/50/200 gap: 16.22% / 25.55% / 12.37%
- 5D return: 1.92% | 20D drawdown: -1.14% | vol_ratio: 0.43
- RS vs SILJ: gap 6.41% / slope_proxy 7.17%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **69.4**
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.64 | RSI14: 79.83 | ATR14%: 5.26%
- MA20/50/200 gap: 21.31% / 28.28% / 10.68%
- 5D return: 12.36% | 20D drawdown: -0.87% | vol_ratio: 0.18
- RS vs SILJ: gap 8.85% / slope_proxy 6.41%
- FundamentalScore: 78 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **67.6**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.72 | RSI14: 81.65 | ATR14%: 6.21%
- MA20/50/200 gap: 20.54% / 34.93% / 12.72%
- 5D return: 9.77% | 20D drawdown: -0.46% | vol_ratio: 0.47
- RS vs SILJ: gap 14.95% / slope_proxy 20.58%
- FundamentalScore: 74 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **65.8**
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
- close: 7.49 | RSI14: 74.05 | ATR14%: 6.00%
- MA20/50/200 gap: 14.32% / 19.04% / 10.39%
- 5D return: 6.62% | 20D drawdown: -1.51% | vol_ratio: 0.48
- RS vs SILJ: gap 0.48% / slope_proxy 3.02%
- FundamentalScore: 60 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **59.5**
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
- close: 3.89 | RSI14: 71.74 | ATR14%: 4.78%
- MA20/50/200 gap: 8.96% / 14.38% / -4.49%
- 5D return: 3.47% | 20D drawdown: 0.00% | vol_ratio: 0.25
- RS vs SILJ: gap -4.19% / slope_proxy -8.22%
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
- close: 5.28 | RSI14: 72.80 | ATR14%: 5.83%
- MA20/50/200 gap: 12.20% / 13.45% / -8.70%
- 5D return: 0.76% | 20D drawdown: -2.04% | vol_ratio: 0.58
- RS vs SILJ: gap -6.35% / slope_proxy 1.60%
- FundamentalScore: 68 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **45.6**
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
- close: 26.40 | RSI14: 65.76 | ATR14%: 7.79%
- MA20/50/200 gap: 9.10% / 13.63% / -9.30%
- 5D return: -2.48% | 20D drawdown: -5.38% | vol_ratio: 0.42
- RS vs SILJ: gap -7.24% / slope_proxy 1.20%
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
