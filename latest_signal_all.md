# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-30 15:01:17**
- 데이터 기준일(일봉): **2026-06-30**
- 데이터 기준일(주봉): **2026-06-29**
- VXN 기준일: **2026-06-29** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 731.34
- Weekly RSI14: **64.85**
- 52W MA: 620.84 / gap: **17.80%**
- 104W MA gap: **31.27%**
- 52W MA 13W slope: **8.47%**
- VXN: **29.37** / 5D change: 1.70

## Daily trigger: 실제 매수 타이밍

- QQQ close: 731.34
- Daily RSI14: **55.33**
- 20D gap: **1.16%**
- 50D gap: **3.67%**
- 200D gap: **15.69%**
- MACD hist: -2.0039 / change: 1.1091
- ATR14%: **2.20%**
- 20D high drawdown: **-1.88%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-30**
- 실행시간(UTC): **2026-06-30 15:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.8 / 4주 변화 8.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.18 / 4주 변화 11.0 bp
- VIX (VIXCLS): 17.65
- NFCI: -0.516

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.251973
- MA60: 9.354316
- gap: 9.60%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.453627
- MA60: 0.362333
- gap: 25.20%
- MA60_slope_proxy: 0.073208
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-30**
- 실행시간(UTC): **2026-06-30 15:00:47**

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
- TERM_SPREAD_10Y_POLICY: 96.17 bp / 4주 변화 -6.43 bp
- CURVE_10s5s: 46.38 bp / 4주 변화 -0.39 bp

## NWG Price
- close: 666.0
- MA50: 598.7651 / gap50: 11.23%
- MA200: 597.1406 / gap200: 11.53%

## Relative Strength
- RS vs FTSE gap: 9.97% / slope_proxy: 0.001743
- RS vs Peers gap: 3.52% / slope_proxy: -0.013436

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-30 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 70.42 / 5D -3.81%
- Brent ref (BZ=F): 73.89 / 5D -4.14%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.47
- Gas ref (NG=F): 3.30 / 5D 4.89%

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

- close: 49.36
- MA20 / MA60 / MA200: 54.19 / 56.40 / 48.93
- gap20 / gap60: -8.92% / -12.48%
- 5D return: -5.49%
- 20D high/low: 59.37 / 49.09

### Relative Strength

- ratio: 0.922014
- ratio_MA60: 0.993158
- ratio_gap: -7.16%
- ratio_slope_proxy(20d): -0.015270

### Volume (if available)

- volume: 1638296.00
- volume_MA20: 9373354.80
- volume_ratio: 0.17

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.20
- MA20 / MA60 / MA200: 17.33 / 19.38 / 15.51
- gap20 / gap60: -6.52% / -16.40%
- 5D return: -4.87%
- 20D high/low: 18.58 / 16.20

### Relative Strength

- ratio: 0.472579
- ratio_MA60: 0.522918
- ratio_gap: -9.63%
- ratio_slope_proxy(20d): -0.006499

### Volume (if available)

- volume: 2329679.00
- volume_MA20: 13737973.95
- volume_ratio: 0.17

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.04
- MA20 / MA60 / MA200: 5.66 / 6.24 / 5.12
- gap20 / gap60: -10.95% / -19.25%
- 5D return: -4.73%
- 20D high/low: 6.25 / 5.04

### Relative Strength

- ratio: 0.013465
- ratio_MA60: 0.014849
- ratio_gap: -9.32%
- ratio_slope_proxy(20d): -0.000835

### Volume (if available)

- volume: 11982818.00
- volume_MA20: 30648590.90
- volume_ratio: 0.39

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

- close: 11.23
- MA20 / MA60 / MA200: 11.86 / 12.58 / 10.75
- gap20 / gap60: -5.24% / -10.66%
- 5D return: 0.22%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.046455
- ratio_MA60: 0.050769
- ratio_gap: -8.50%
- ratio_slope_proxy(20d): -0.001012

### Volume (if available)

- volume: 1531212.00
- volume_MA20: 13284895.60
- volume_ratio: 0.12

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

- 데이터 기준일(주가): **2026-06-30**
- 실행시간(UTC): **2026-06-30 15:01:04**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.8
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 11.0 bp / latest 2.18
- VIX: 17.65
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 6.77% / slope_proxy: 0.006677
- GDXJ/GLD gap: -5.43% / slope_proxy: -0.001832

## VZLA (Vizsla Silver)
- close: 3.325 | RSI14: 45.458749 | ATR14%: 6.39%
- MA20 gap: -4.56% | MA50 gap: -5.22% | MA200 gap: -21.50%
- vol_ratio(Volume/Vol20): 0.172018 | gap_open: 0.31%
- RS vs SILJ gap: 8.69% / slope_proxy: 0.004688
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
- close: 6.5101 | RSI14: 40.564621 | ATR14%: 7.97%
- MA20 gap: -5.75% | MA50 gap: -17.34% | MA200 gap: -23.55%
- vol_ratio(Volume/Vol20): 0.127649 | gap_open: 0.46%
- SilverMarginGate: SI=60.455002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.43% / slope_proxy: -0.00918
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

## HYMC (Hycroft Mining)
- close: 23.379999 | RSI14: 37.419954 | ATR14%: 9.69%
- MA20 gap: -9.40% | MA50 gap: -28.18% | MA200 gap: -10.75%
- vol_ratio(Volume/Vol20): 0.180057 | gap_open: 0.21%
- RS vs SILJ gap: -19.98% / slope_proxy: -0.081527
- RS vs GDXJ gap: -17.13% / slope_proxy: -0.017344
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

- 실행시간(UTC): **2026-06-30 15:01:13**
- 데이터 기준일(주가): **2026-06-30**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.80 / 4주 변화 0.08 bp-ish / 2026-06-29
- IG OAS: 0.76 / 4주 변화 0.03 bp-ish / 2026-06-29
- 10Y Real Yield: 2.18 / 4주 변화 0.12 bp-ish / 2026-06-26
- VIX: 17.65 / 4주 변화 1.60 / 2026-06-29
- NFCI: -0.52 / 4주 변화 0.05 / 2026-06-19

### Leadership ratios

- GDX/GLD: gap -5.03% / slope_proxy -5.51%
- GDXJ/GLD: gap -5.43% / slope_proxy -6.24%
- SILJ/SLV: gap 6.79% / slope_proxy 4.35%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.23 | RSI14: 50.29 | ATR14%: 6.05%
- MA20/50/200 gap: -5.95% / -8.35% / 8.61%
- 5D return: -6.23% | 20D drawdown: -15.44% | vol_ratio: 0.17
- RS vs GDXJ: gap 9.18% / slope_proxy 0.29%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.21 | RSI14: 51.63 | ATR14%: 6.11%
- MA20/50/200 gap: -6.35% / -16.65% / -24.85%
- 5D return: -1.14% | 20D drawdown: -18.34% | vol_ratio: 0.57
- RS vs GDXJ: gap -4.34% / slope_proxy -9.66%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **48.1**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.12 | RSI14: 48.10 | ATR14%: 8.93%
- MA20/50/200 gap: -10.58% / -15.83% / -25.62%
- 5D return: -8.94% | 20D drawdown: -23.81% | vol_ratio: 1.23
- RS vs GDXJ: gap -2.66% / slope_proxy -3.74%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.0**
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.58 | RSI14: 55.56 | ATR14%: 5.83%
- MA20/50/200 gap: -2.80% / -12.58% / -6.66%
- 5D return: 0.64% | 20D drawdown: -16.40% | vol_ratio: 0.58
- RS vs GDXJ: gap 2.90% / slope_proxy -4.88%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **36.0**
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
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.55 | RSI14: 56.95 | ATR14%: 7.79%
- MA20/50/200 gap: -1.46% / -0.28% / 20.25%
- 5D return: 1.87% | 20D drawdown: -13.68% | vol_ratio: 0.15
- RS vs SILJ: gap 15.02% / slope_proxy 3.79%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **63.7**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.37 | RSI14: 55.70 | ATR14%: 6.64%
- MA20/50/200 gap: -1.17% / -9.14% / -11.97%
- 5D return: 4.49% | 20D drawdown: -15.03% | vol_ratio: 0.24
- RS vs SILJ: gap 2.97% / slope_proxy 2.17%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **61.9**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.41 | RSI14: 56.91 | ATR14%: 5.72%
- MA20/50/200 gap: -1.28% / -10.09% / -14.06%
- 5D return: 2.29% | 20D drawdown: -13.40% | vol_ratio: 0.12
- RS vs SILJ: gap 0.73% / slope_proxy 4.13%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **60.1**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.36 | RSI14: 57.84 | ATR14%: 6.97%
- MA20/50/200 gap: 0.86% / -4.84% / -2.95%
- 5D return: 8.25% | 20D drawdown: -14.22% | vol_ratio: 0.31
- RS vs SILJ: gap 7.70% / slope_proxy 3.14%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **52.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.51 | RSI14: 55.09 | ATR14%: 7.76%
- MA20/50/200 gap: -5.75% / -17.34% / -23.55%
- 5D return: -1.66% | 20D drawdown: -21.85% | vol_ratio: 0.13
- RS vs SILJ: gap -6.41% / slope_proxy -6.03%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **49.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.33 | RSI14: 49.83 | ATR14%: 6.00%
- MA20/50/200 gap: -4.56% / -5.22% / -21.50%
- 5D return: -0.75% | 20D drawdown: -19.49% | vol_ratio: 0.17
- RS vs SILJ: gap 8.71% / slope_proxy -3.20%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **48.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.74 | RSI14: 50.29 | ATR14%: 8.32%
- MA20/50/200 gap: -9.00% / -17.77% / -16.29%
- 5D return: -3.29% | 20D drawdown: -26.30% | vol_ratio: 0.26
- RS vs SILJ: gap -6.08% / slope_proxy -11.39%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 23.38 | RSI14: 45.45 | ATR14%: 8.60%
- MA20/50/200 gap: -9.40% / -28.18% / -10.75%
- 5D return: 1.04% | 20D drawdown: -30.87% | vol_ratio: 0.18
- RS vs SILJ: gap -19.96% / slope_proxy -16.88%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **35.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
