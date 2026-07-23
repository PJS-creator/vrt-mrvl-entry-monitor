# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-23 03:01:28**
- 데이터 기준일(일봉): **2026-07-22**
- 데이터 기준일(주봉): **2026-07-20**
- VXN 기준일: **2026-07-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 705.35
- Weekly RSI14: **58.02**
- 52W MA: 629.24 / gap: **12.10%**
- 104W MA gap: **25.11%**
- 52W MA 13W slope: **7.91%**
- VXN: **26.66** / 5D change: 0.38

## Daily trigger: 실제 매수 타이밍

- QQQ close: 705.35
- Daily RSI14: **46.71**
- 20D gap: **-1.25%**
- 50D gap: **-1.86%**
- 200D gap: **10.03%**
- MACD hist: -2.1795 / change: 0.3567
- ATR14%: **2.02%**
- 20D high drawdown: **-4.22%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-23 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.37 / 4주 변화 8.0 bp
- VIX (VIXCLS): 17.05
- NFCI: -0.552

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.762075
- MA60: 9.649547
- gap: 1.17%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.359493
- MA60: 0.381354
- gap: -5.73%
- MA60_slope_proxy: 0.034428
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-23 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 126.95 bp / 4주 변화 23.65 bp
- CURVE_10s5s: 47.38 bp / 4주 변화 1.78 bp

## NWG Price
- close: 679.0
- MA50: 625.544 / gap50: 8.55%
- MA200: 608.1141 / gap200: 11.66%

## Relative Strength
- RS vs FTSE gap: 8.46% / slope_proxy: 0.002205
- RS vs Peers gap: 1.32% / slope_proxy: -0.003691

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-23 03:00:56**

## Commodity Regime

- WTI ref (CL=F): 88.41 / 5D 11.07%
- Brent ref (BZ=F): 96.21 / 5D 13.25%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.80
- Gas ref (NG=F): 2.96 / 5D 1.27%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 57.50
- MA20 / MA60 / MA200: 52.35 / 55.32 / 49.46
- gap20 / gap60: 9.85% / 3.94%
- 5D return: 6.94%
- 20D high/low: 57.50 / 47.94

### Relative Strength

- ratio: 0.971284
- ratio_MA60: 0.976393
- ratio_gap: -0.52%
- ratio_slope_proxy(20d): -0.027412

### Volume (if available)

- volume: 7511888.00
- volume_MA20: 9458679.40
- volume_ratio: 0.79

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.89
- MA20 / MA60 / MA200: 17.15 / 18.56 / 15.86
- gap20 / gap60: 10.14% / 1.78%
- 5D return: 5.77%
- 20D high/low: 18.89 / 15.99

### Relative Strength

- ratio: 0.515838
- ratio_MA60: 0.517510
- ratio_gap: -0.32%
- ratio_slope_proxy(20d): -0.011058

### Volume (if available)

- volume: 12287237.00
- volume_MA20: 14670111.85
- volume_ratio: 0.84

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.30
- MA20 / MA60 / MA200: 5.12 / 5.95 / 5.25
- gap20 / gap60: 3.48% / -10.93%
- 5D return: 1.92%
- 20D high/low: 5.37 / 4.87

### Relative Strength

- ratio: 0.013643
- ratio_MA60: 0.014428
- ratio_gap: -5.44%
- ratio_slope_proxy(20d): -0.000665

### Volume (if available)

- volume: 42522582.00
- volume_MA20: 39200069.10
- volume_ratio: 1.08

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

- close: 14.82
- MA20 / MA60 / MA200: 12.27 / 12.52 / 10.65
- gap20 / gap60: 20.75% / 18.41%
- 5D return: 14.79%
- 20D high/low: 14.82 / 10.51

### Relative Strength

- ratio: 0.055423
- ratio_MA60: 0.050769
- ratio_gap: 9.17%
- ratio_slope_proxy(20d): -0.000810

### Volume (if available)

- volume: 20851838.00
- volume_MA20: 14173541.90
- volume_ratio: 1.47

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-23 03:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.37
- VIX: 17.05
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 5.74% / slope_proxy: 0.00851
- GDXJ/GLD gap: -2.33% / slope_proxy: -0.008495

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 55.517527 | ATR14%: 5.78%
- MA20 gap: 7.34% | MA50 gap: -0.49% | MA200 gap: -17.95%
- vol_ratio(Volume/Vol20): 1.304874 | gap_open: 0.30%
- RS vs SILJ gap: 7.77% / slope_proxy: 0.006108
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
- close: 6.76 | RSI14: 51.644069 | ATR14%: 6.54%
- MA20 gap: 5.04% | MA50 gap: -7.17% | MA200 gap: -20.09%
- vol_ratio(Volume/Vol20): 0.910165 | gap_open: 2.29%
- SilverMarginGate: SI=59.970001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.95% / slope_proxy: -0.005826
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
- close: 21.700001 | RSI14: 45.44196 | ATR14%: 8.75%
- MA20 gap: 0.51% | MA50 gap: -21.02% | MA200 gap: -20.56%
- vol_ratio(Volume/Vol20): 0.828288 | gap_open: 1.64%
- RS vs SILJ gap: -17.97% / slope_proxy: -0.125497
- RS vs GDXJ gap: -18.61% / slope_proxy: -0.028017
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

- 실행시간(UTC): **2026-07-23 03:01:26**
- 데이터 기준일(주가): **2026-07-22**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.69 / 4주 변화 -0.02 bp-ish / 2026-07-21
- IG OAS: 0.78 / 4주 변화 0.04 bp-ish / 2026-07-21
- 10Y Real Yield: 2.37 / 4주 변화 0.09 bp-ish / 2026-07-21
- VIX: 17.05 / 4주 변화 -2.44 / 2026-07-21
- NFCI: -0.55 / 4주 변화 -0.05 / 2026-07-17

### Leadership ratios

- GDX/GLD: gap -2.37% / slope_proxy -0.78%
- GDXJ/GLD: gap -2.33% / slope_proxy 1.02%
- SILJ/SLV: gap 5.74% / slope_proxy -0.50%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.29 | RSI14: 46.38 | ATR14%: 5.16%
- MA20/50/200 gap: -1.07% / -6.43% / 6.89%
- 5D return: 0.69% | 20D drawdown: -7.84% | vol_ratio: 0.52
- RS vs GDXJ: gap 0.58% / slope_proxy -4.32%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 30 | OverallScore: **66.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs GDXJ)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.02 | RSI14: 69.39 | ATR14%: 7.28%
- MA20/50/200 gap: 15.07% / 10.08% / 13.18%
- 5D return: 6.32% | 20D drawdown: -1.94% | vol_ratio: 1.20
- RS vs GDXJ: gap 20.02% / slope_proxy 28.66%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **53.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.40 | RSI14: 48.78 | ATR14%: 4.75%
- MA20/50/200 gap: 4.34% / -6.38% / -21.60%
- 5D return: 8.87% | 20D drawdown: -6.09% | vol_ratio: 0.92
- RS vs GDXJ: gap -1.90% / slope_proxy 2.47%
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
- close: 1.13 | RSI14: 40.38 | ATR14%: 6.23%
- MA20/50/200 gap: -1.27% / -10.50% / -24.46%
- 5D return: 2.73% | 20D drawdown: -13.08% | vol_ratio: 0.66
- RS vs GDXJ: gap -4.73% / slope_proxy -8.13%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **42.8**
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 20.90 | RSI14: 59.30 | ATR14%: 6.21%
- MA20/50/200 gap: 8.66% / 9.21% / 30.35%
- 5D return: 5.82% | 20D drawdown: 0.00% | vol_ratio: 1.51
- RS vs SILJ: gap 19.13% / slope_proxy 17.82%
- FundamentalScore: 86 | TechnicalScore: 100 | RegimeScore: 30 | OverallScore: **79.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.34 | RSI14: 50.00 | ATR14%: 5.84%
- MA20/50/200 gap: 3.68% / -5.02% / -12.86%
- 5D return: 4.77% | 20D drawdown: -2.57% | vol_ratio: 1.33
- RS vs SILJ: gap 2.11% / slope_proxy 4.40%
- FundamentalScore: 82 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **62.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.69 | RSI14: 50.78 | ATR14%: 5.48%
- MA20/50/200 gap: 2.21% / -3.76% / -13.94%
- 5D return: 1.49% | 20D drawdown: -4.68% | vol_ratio: 0.87
- RS vs SILJ: gap 2.70% / slope_proxy 4.29%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **55.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.42 | RSI14: 55.48 | ATR14%: 5.61%
- MA20/50/200 gap: 7.34% / -0.49% / -17.95%
- 5D return: 6.88% | 20D drawdown: 0.00% | vol_ratio: 1.30
- RS vs SILJ: gap 7.77% / slope_proxy 6.13%
- FundamentalScore: 72 | TechnicalScore: 75 | RegimeScore: 30 | OverallScore: **64.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.26 | RSI14: 48.52 | ATR14%: 6.44%
- MA20/50/200 gap: 4.06% / -3.12% / -5.87%
- 5D return: 5.56% | 20D drawdown: -4.86% | vol_ratio: 1.76
- RS vs SILJ: gap 4.82% / slope_proxy 7.12%
- FundamentalScore: 60 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **52.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.18 | RSI14: 39.23 | ATR14%: 7.69%
- MA20/50/200 gap: -4.23% / -20.16% / -27.13%
- 5D return: 3.72% | 20D drawdown: -14.52% | vol_ratio: 1.72
- RS vs SILJ: gap -14.69% / slope_proxy -11.53%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **47.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.76 | RSI14: 52.77 | ATR14%: 6.09%
- MA20/50/200 gap: 5.04% / -7.17% / -20.09%
- 5D return: 6.46% | 20D drawdown: -0.73% | vol_ratio: 0.91
- RS vs SILJ: gap -0.95% / slope_proxy 3.07%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **44.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.70 | RSI14: 45.26 | ATR14%: 7.97%
- MA20/50/200 gap: 0.51% / -21.02% / -20.56%
- 5D return: 3.88% | 20D drawdown: -8.59% | vol_ratio: 0.83
- RS vs SILJ: gap -17.97% / slope_proxy -3.49%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **30.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
