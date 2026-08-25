# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-25 23:00:08**
- 데이터 기준일(일봉): **2026-08-25**
- 데이터 기준일(주봉): **2026-08-24**
- VXN 기준일: **2026-08-24** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 710.72
- Weekly RSI14: **56.84**
- 52W MA: 642.90 / gap: **10.55%**
- 104W MA gap: **23.45%**
- 52W MA 13W slope: **6.61%**
- VXN: **22.69** / 5D change: 1.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 710.72
- Daily RSI14: **48.96**
- 20D gap: **-0.20%**
- 50D gap: **-0.31%**
- 200D gap: **8.90%**
- MACD hist: -1.1265 / change: -0.2376
- ATR14%: **1.55%**
- 20D high drawdown: **-2.92%**

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

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 22:59:36**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 -12.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.38 / 4주 변화 -6.0 bp
- VIX (VIXCLS): 15.85
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.98221
- MA60: 9.193131
- gap: -13.17%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.432478
- MA60: 0.403737
- gap: 7.12%
- MA60_slope_proxy: 0.020421
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 22:59:39**

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
- TERM_SPREAD_10Y_POLICY: 130.06 bp / 4주 변화 2.53 bp
- CURVE_10s5s: 49.44 bp / 4주 변화 3.69 bp

## NWG Price
- close: 690.2
- MA50: 678.575 / gap50: 1.71%
- MA200: 624.6643 / gap200: 10.49%

## Relative Strength
- RS vs FTSE gap: 1.18% / slope_proxy: 0.002932
- RS vs Peers gap: 1.94% / slope_proxy: 0.01824

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-25 22:59:45**

## Commodity Regime

- WTI ref (CL=F): 81.04 / 5D -4.59%
- Brent ref (BZ=F): 86.15 / 5D -5.35%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.11
- Gas ref (NG=F): 2.84 / 5D 2.45%

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

- close: 58.41
- MA20 / MA60 / MA200: 57.90 / 55.34 / 51.39
- gap20 / gap60: 0.88% / 5.55%
- 5D return: -2.32%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.941186
- ratio_MA60: 0.959742
- ratio_gap: -1.93%
- ratio_slope_proxy(20d): -0.012139

### Volume (if available)

- volume: 6810831.00
- volume_MA20: 8228311.55
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.85
- MA20 / MA60 / MA200: 18.45 / 17.83 / 16.67
- gap20 / gap60: -3.28% / 0.14%
- 5D return: -1.82%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.497492
- ratio_MA60: 0.510744
- ratio_gap: -2.59%
- ratio_slope_proxy(20d): -0.004585

### Volume (if available)

- volume: 28748632.00
- volume_MA20: 16843671.60
- volume_ratio: 1.71

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.75
- MA20 / MA60 / MA200: 5.55 / 5.47 / 5.49
- gap20 / gap60: 3.63% / 5.07%
- 5D return: -1.20%
- 20D high/low: 6.01 / 4.95

### Relative Strength

- ratio: 0.014173
- ratio_MA60: 0.013826
- ratio_gap: 2.52%
- ratio_slope_proxy(20d): -0.000496

### Volume (if available)

- volume: 29983467.00
- volume_MA20: 43431018.35
- volume_ratio: 0.69

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.07
- MA20 / MA60 / MA200: 13.61 / 12.79 / 11.10
- gap20 / gap60: 3.35% / 10.02%
- 5D return: -0.92%
- 20D high/low: 14.39 / 12.43

### Relative Strength

- ratio: 0.050466
- ratio_MA60: 0.050455
- ratio_gap: 0.02%
- ratio_slope_proxy(20d): -0.000717

### Volume (if available)

- volume: 13088732.00
- volume_MA20: 13399546.60
- volume_ratio: 0.98

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

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 22:59:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -12.0 bp / latest 2.69
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -6.0 bp / latest 2.38
- VIX: 15.85
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 10.44% / slope_proxy: 0.021896
- GDXJ/GLD gap: 16.10% / slope_proxy: 0.002779

## VZLA (Vizsla Silver)
- close: 4.04 | RSI14: 65.627331 | ATR14%: 4.71%
- MA20 gap: 10.78% | MA50 gap: 18.09% | MA200 gap: -0.88%
- vol_ratio(Volume/Vol20): 0.675793 | gap_open: 1.02%
- RS vs SILJ gap: -3.42% / slope_proxy: 0.003549
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
- close: 9.77 | RSI14: 70.321824 | ATR14%: 5.54%
- MA20 gap: 16.50% | MA50 gap: 33.60% | MA200 gap: 12.75%
- vol_ratio(Volume/Vol20): 0.546152 | gap_open: 1.88%
- SilverMarginGate: SI=69.040001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.74% / slope_proxy: 0.003062
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
- close: 26.08 | RSI14: 54.128844 | ATR14%: 7.38%
- MA20 gap: 5.18% | MA50 gap: 12.11% | MA200 gap: -10.97%
- vol_ratio(Volume/Vol20): 0.832846 | gap_open: 3.24%
- RS vs SILJ gap: -10.16% / slope_proxy: -0.113048
- RS vs GDXJ gap: -15.42% / slope_proxy: -0.031528
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

- 실행시간(UTC): **2026-08-25 23:00:07**
- 데이터 기준일(주가): **2026-08-25**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA, ASM**

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

- HY OAS: 2.69 / 4주 변화 -0.12 bp-ish / 2026-08-24
- IG OAS: 0.81 / 4주 변화 0.00 bp-ish / 2026-08-24
- 10Y Real Yield: 2.38 / 4주 변화 -0.06 bp-ish / 2026-08-24
- VIX: 15.85 / 4주 변화 -2.82 / 2026-08-24
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 17.38% / slope_proxy 24.33%
- GDXJ/GLD: gap 16.10% / slope_proxy 24.03%
- SILJ/SLV: gap 10.44% / slope_proxy 14.74%
- Gold breadth proxy: above50 100.00%, above200 100.00%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 11.07 | RSI14: 84.58 | ATR14%: 5.43%
- MA20/50/200 gap: 19.56% / 35.12% / 53.47%
- 5D return: 13.89% | 20D drawdown: 0.00% | vol_ratio: 1.11
- RS vs GDXJ: gap 6.77% / slope_proxy 8.51%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **82.3**
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
- close: 7.87 | RSI14: 85.59 | ATR14%: 4.11%
- MA20/50/200 gap: 17.69% / 34.14% / 13.63%
- 5D return: 16.77% | 20D drawdown: -0.13% | vol_ratio: 0.58
- RS vs GDXJ: gap 4.74% / slope_proxy 3.79%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.71 | RSI14: 81.30 | ATR14%: 5.40%
- MA20/50/200 gap: 24.94% / 41.62% / 44.13%
- 5D return: 21.52% | 20D drawdown: 0.00% | vol_ratio: 1.11
- RS vs GDXJ: gap 12.43% / slope_proxy 4.89%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **67.5**
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.60 | RSI14: 73.21 | ATR14%: 5.07%
- MA20/50/200 gap: 12.04% / 24.65% / 7.86%
- 5D return: 4.58% | 20D drawdown: -3.03% | vol_ratio: 0.62
- RS vs GDXJ: gap -1.94% / slope_proxy 1.73%
- FundamentalScore: 70 | TechnicalScore: 25 | RegimeScore: 100 | OverallScore: **60.2**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.71 | RSI14: 61.24 | ATR14%: 5.61%
- MA20/50/200 gap: 10.07% / 27.40% / 57.54%
- 5D return: 10.88% | 20D drawdown: -1.18% | vol_ratio: 1.30
- RS vs SILJ: gap 8.28% / slope_proxy 4.38%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.49 | RSI14: 64.99 | ATR14%: 5.61%
- MA20/50/200 gap: 11.36% / 18.22% / 9.95%
- 5D return: 9.66% | 20D drawdown: -1.45% | vol_ratio: 0.52
- RS vs SILJ: gap -2.30% / slope_proxy 2.90%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **56.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.09 | RSI14: 68.59 | ATR14%: 6.22%
- MA20/50/200 gap: 14.99% / 26.71% / 14.29%
- 5D return: 14.80% | 20D drawdown: 0.00% | vol_ratio: 0.98
- RS vs SILJ: gap 5.28% / slope_proxy 6.21%
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
- close: 20.92 | RSI14: 74.17 | ATR14%: 4.90%
- MA20/50/200 gap: 18.88% / 28.25% / 11.66%
- 5D return: 16.55% | 20D drawdown: 0.00% | vol_ratio: 0.84
- RS vs SILJ: gap 6.70% / slope_proxy 7.04%
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
- close: 9.77 | RSI14: 73.63 | ATR14%: 5.84%
- MA20/50/200 gap: 16.50% / 33.60% / 12.75%
- 5D return: 16.73% | 20D drawdown: 0.00% | vol_ratio: 0.55
- RS vs SILJ: gap 11.74% / slope_proxy 12.10%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.04 | RSI14: 66.92 | ATR14%: 4.57%
- MA20/50/200 gap: 10.78% / 18.09% / -0.88%
- 5D return: 13.17% | 20D drawdown: 0.00% | vol_ratio: 0.68
- RS vs SILJ: gap -3.42% / slope_proxy -6.25%
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
- close: 5.62 | RSI14: 68.16 | ATR14%: 5.26%
- MA20/50/200 gap: 15.53% / 20.32% / -3.14%
- 5D return: 13.54% | 20D drawdown: 0.00% | vol_ratio: 1.17
- RS vs SILJ: gap -2.75% / slope_proxy 11.17%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
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
- close: 26.08 | RSI14: 54.76 | ATR14%: 7.59%
- MA20/50/200 gap: 5.18% / 12.11% / -10.97%
- 5D return: 7.81% | 20D drawdown: -6.52% | vol_ratio: 0.83
- RS vs SILJ: gap -10.16% / slope_proxy -1.45%
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
