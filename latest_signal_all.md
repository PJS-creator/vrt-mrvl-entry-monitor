# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-18 02:45:20**
- 데이터 기준일(일봉): **2026-09-17**
- 데이터 기준일(주봉): **2026-09-14**
- VXN 기준일: **2026-09-16** / source: `FRED: VXNCLS`

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
- VXN: **22.44** / 5D change: 0.12

## Daily trigger: 실제 매수 타이밍

- QQQ close: 716.92
- Daily RSI14: **53.05**
- 20D gap: **0.59%**
- 50D gap: **0.98%**
- 200D gap: **8.42%**
- MACD hist: -0.7077 / change: 0.7196
- ATR14%: **1.32%**
- 20D high drawdown: **-0.58%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-18 02:44:59**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -3.0 bp
- 10Y Real Yield (DFII10): 2.68 / 4주 변화 33.0 bp
- VIX (VIXCLS): 17.71
- NFCI: -0.56

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.100973
- MA60: 9.126311
- gap: -11.24%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.429461
- MA60: 0.389284
- gap: 10.32%
- MA60_slope_proxy: -0.008487
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-18 02:45:02**

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
- TERM_SPREAD_10Y_POLICY: 161.16 bp / 4주 변화 29.4 bp
- CURVE_10s5s: 43.28 bp / 4주 변화 -6.18 bp

## NWG Price
- close: 702.2
- MA50: 687.1123 / gap50: 2.20%
- MA200: 631.1339 / gap200: 11.26%

## Relative Strength
- RS vs FTSE gap: 2.86% / slope_proxy: 0.001723
- RS vs Peers gap: 4.49% / slope_proxy: 0.01128

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-18 02:45:07**

## Commodity Regime

- WTI ref (CL=F): 101.11 / 5D -1.34%
- Brent ref (BZ=F): 103.85 / 5D -3.51%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.74
- Gas ref (NG=F): 2.85 / 5D 0.74%

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

- close: 59.29
- MA20 / MA60 / MA200: 60.28 / 56.38 / 52.71
- gap20 / gap60: -1.64% / 5.16%
- 5D return: -3.06%
- 20D high/low: 63.52 / 58.14

### Relative Strength

- ratio: 0.919510
- ratio_MA60: 0.942953
- ratio_gap: -2.49%
- ratio_slope_proxy(20d): -0.015599

### Volume (if available)

- volume: 8780000.00
- volume_MA20: 7607550.00
- volume_ratio: 1.15

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.94
- MA20 / MA60 / MA200: 19.89 / 18.15 / 16.84
- gap20 / gap60: 5.28% / 15.38%
- 5D return: -2.06%
- 20D high/low: 21.77 / 17.76

### Relative Strength

- ratio: 0.554849
- ratio_MA60: 0.507211
- ratio_gap: 9.39%
- ratio_slope_proxy(20d): 0.011421

### Volume (if available)

- volume: 12777900.00
- volume_MA20: 23539725.00
- volume_ratio: 0.54

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

- close: 5.66
- MA20 / MA60 / MA200: 5.80 / 5.45 / 5.62
- gap20 / gap60: -2.34% / 3.91%
- 5D return: -1.91%
- 20D high/low: 6.22 / 5.45

### Relative Strength

- ratio: 0.014129
- ratio_MA60: 0.013733
- ratio_gap: 2.89%
- ratio_slope_proxy(20d): -0.000122

### Volume (if available)

- volume: 41115400.00
- volume_MA20: 40961280.00
- volume_ratio: 1.00

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

- close: 14.42
- MA20 / MA60 / MA200: 14.68 / 13.46 / 11.65
- gap20 / gap60: -1.77% / 7.15%
- 5D return: -6.72%
- 20D high/low: 15.76 / 14.03

### Relative Strength

- ratio: 0.053437
- ratio_MA60: 0.050570
- ratio_gap: 5.67%
- ratio_slope_proxy(20d): 0.000033

### Volume (if available)

- volume: 12871000.00
- volume_MA20: 13701630.00
- volume_ratio: 0.94

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

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-18 02:45:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.7
- IG OAS 4주 변화: -3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 33.0 bp / latest 2.68
- VIX: 17.71
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 2.90% / slope_proxy: 0.024716
- GDXJ/GLD gap: 8.88% / slope_proxy: 0.013806

## VZLA (Vizsla Silver)
- close: 4.01 | RSI14: 55.084962 | ATR14%: 5.39%
- MA20 gap: 0.75% | MA50 gap: 10.47% | MA200 gap: -0.81%
- vol_ratio(Volume/Vol20): 0.850593 | gap_open: 4.34%
- RS vs SILJ gap: 4.54% / slope_proxy: -0.00023
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

## SCZM (Santacruz Silver)
- close: 8.92 | RSI14: 48.294024 | ATR14%: 7.13%
- MA20 gap: -6.90% | MA50 gap: 8.90% | MA200 gap: -0.71%
- vol_ratio(Volume/Vol20): 1.203985 | gap_open: 5.42%
- SilverMarginGate: SI=66.394997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.54% / slope_proxy: 0.016523
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
- close: 21.51 | RSI14: 43.89851 | ATR14%: 7.78%
- MA20 gap: -7.62% | MA50 gap: -5.89% | MA200 gap: -29.11%
- vol_ratio(Volume/Vol20): 1.155758 | gap_open: 6.51%
- RS vs SILJ gap: -12.80% / slope_proxy: -0.0839
- RS vs GDXJ gap: -15.73% / slope_proxy: -0.026154
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

- 실행시간(UTC): **2026-09-18 02:45:19**
- 데이터 기준일(주가): **2026-09-17**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.70 / 4주 변화 -0.03 bp-ish / 2026-09-16
- IG OAS: 0.78 / 4주 변화 -0.03 bp-ish / 2026-09-16
- 10Y Real Yield: 2.68 / 4주 변화 0.27 bp-ish / 2026-09-16
- VIX: 17.71 / 4주 변화 2.82 / 2026-09-16
- NFCI: -0.56 / 4주 변화 -0.07 / 2026-09-11

### Leadership ratios

- GDX/GLD: gap 9.82% / slope_proxy 0.14%
- GDXJ/GLD: gap 8.88% / slope_proxy -0.21%
- SILJ/SLV: gap 2.90% / slope_proxy -0.50%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 84.62%, above200 30.77%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.50 | RSI14: 44.67 | ATR14%: 4.84%
- MA20/50/200 gap: 1.85% / 16.82% / 38.03%
- 5D return: 6.92% | 20D drawdown: -5.15% | vol_ratio: 0.91
- RS vs GDXJ: gap 8.68% / slope_proxy 4.46%
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
- close: 7.69 | RSI14: 42.81 | ATR14%: 5.34%
- MA20/50/200 gap: -1.65% / 16.17% / 8.86%
- 5D return: -3.15% | 20D drawdown: -7.79% | vol_ratio: 0.77
- RS vs GDXJ: gap 9.26% / slope_proxy 7.68%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **81.6**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.62 | RSI14: 45.68 | ATR14%: 6.84%
- MA20/50/200 gap: 0.19% / 17.13% / 33.94%
- 5D return: 1.95% | 20D drawdown: -6.09% | vol_ratio: 1.03
- RS vs GDXJ: gap 11.70% / slope_proxy 11.25%
- FundamentalScore: 55 | TechnicalScore: 100 | RegimeScore: 75 | OverallScore: **74.8**
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
- close: 1.44 | RSI14: 36.92 | ATR14%: 5.38%
- MA20/50/200 gap: -5.64% / 5.79% / -3.75%
- 5D return: -2.04% | 20D drawdown: -12.73% | vol_ratio: 1.27
- RS vs GDXJ: gap -2.42% / slope_proxy -8.84%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **57.0**
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
- close: 28.82 | RSI14: 48.27 | ATR14%: 6.38%
- MA20/50/200 gap: 3.14% / 17.22% / 51.75%
- 5D return: 1.41% | 20D drawdown: -3.58% | vol_ratio: 1.05
- RS vs SILJ: gap 13.85% / slope_proxy 12.50%
- FundamentalScore: 86 | TechnicalScore: 80 | RegimeScore: 50 | OverallScore: **76.7**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.01 | RSI14: 45.56 | ATR14%: 5.76%
- MA20/50/200 gap: 0.75% / 10.47% / -0.81%
- 5D return: 0.25% | 20D drawdown: -3.84% | vol_ratio: 0.85
- RS vs SILJ: gap 4.54% / slope_proxy 8.88%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 18.96 | RSI14: 36.85 | ATR14%: 5.73%
- MA20/50/200 gap: -5.81% / 7.26% / -1.08%
- 5D return: -5.29% | 20D drawdown: -11.53% | vol_ratio: 1.97
- RS vs SILJ: gap 1.93% / slope_proxy -4.30%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **55.6**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.92 | RSI14: 40.42 | ATR14%: 7.79%
- MA20/50/200 gap: -6.90% / 8.90% / -0.71%
- 5D return: -7.95% | 20D drawdown: -14.48% | vol_ratio: 1.20
- RS vs SILJ: gap 5.54% / slope_proxy -3.96%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **53.8**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.17 | RSI14: 38.54 | ATR14%: 5.93%
- MA20/50/200 gap: -4.55% / 7.48% / 2.45%
- 5D return: -3.33% | 20D drawdown: -11.33% | vol_ratio: 0.71
- RS vs SILJ: gap 2.49% / slope_proxy -2.58%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **52.1**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.06 | RSI14: 38.19 | ATR14%: 6.31%
- MA20/50/200 gap: -3.58% / 6.66% / -14.23%
- 5D return: -0.59% | 20D drawdown: -11.85% | vol_ratio: 1.03
- RS vs SILJ: gap -0.64% / slope_proxy 1.28%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **51.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.29 | RSI14: 29.78 | ATR14%: 6.76%
- MA20/50/200 gap: -11.64% / -4.20% / -10.16%
- 5D return: -11.66% | 20D drawdown: -18.63% | vol_ratio: 0.72
- RS vs SILJ: gap -10.14% / slope_proxy -13.03%
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
- close: 21.51 | RSI14: 30.74 | ATR14%: 7.45%
- MA20/50/200 gap: -7.62% / -5.89% / -29.11%
- 5D return: 0.56% | 20D drawdown: -20.54% | vol_ratio: 1.16
- RS vs SILJ: gap -12.80% / slope_proxy -13.53%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **39.4**
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
