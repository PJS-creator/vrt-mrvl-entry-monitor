# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-29 02:17:04**
- 데이터 기준일(일봉): **2026-09-28**
- 데이터 기준일(주봉): **2026-09-28**
- VXN 기준일: **2026-09-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 736.53
- Weekly RSI14: **61.22**
- 52W MA: 655.59 / gap: **12.35%**
- 104W MA gap: **25.37%**
- 52W MA 13W slope: **5.76%**
- VXN: **20.18** / 5D change: -2.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 736.53
- Daily RSI14: **58.73**
- 20D gap: **2.10%**
- 50D gap: **3.33%**
- 200D gap: **10.80%**
- MACD hist: 2.7978 / change: -0.7422
- ATR14%: **1.33%**
- 20D high drawdown: **-1.46%**

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

- 데이터 기준일(주가): **2026-09-28**
- 실행시간(UTC): **2026-09-29 02:16:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.93 / 4주 변화 33.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.83 / 4주 변화 41.0 bp
- VIX (VIXCLS): 14.21
- NFCI: -0.555

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.517975
- MA60: 8.948561
- gap: -4.81%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.419826
- MA60: 0.388222
- gap: 8.14%
- MA60_slope_proxy: -0.014857
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-28**
- 실행시간(UTC): **2026-09-29 02:16:42**

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
- TERM_SPREAD_10Y_POLICY: 159.38 bp / 4주 변화 31.84 bp
- CURVE_10s5s: 41.94 bp / 4주 변화 -6.04 bp

## NWG Price
- close: 694.4
- MA50: 692.4878 / gap50: 0.28%
- MA200: 633.6472 / gap200: 9.59%

## Relative Strength
- RS vs FTSE gap: 1.29% / slope_proxy: 0.00125
- RS vs Peers gap: 3.40% / slope_proxy: 0.008742

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-29 02:16:49**

## Commodity Regime

- WTI ref (CL=F): 93.60 / 5D -2.28%
- Brent ref (BZ=F): 99.20 / 5D -1.14%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.60
- Gas ref (NG=F): 3.13 / 5D 10.54%

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

- close: 56.10
- MA20 / MA60 / MA200: 59.50 / 57.31 / 53.27
- gap20 / gap60: -5.72% / -2.11%
- 5D return: -2.01%
- 20D high/low: 63.52 / 56.10

### Relative Strength

- ratio: 0.903382
- ratio_MA60: 0.947226
- ratio_gap: -4.63%
- ratio_slope_proxy(20d): -0.009810

### Volume (if available)

- volume: 11859000.00
- volume_MA20: 8901470.00
- volume_ratio: 1.33

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.65
- MA20 / MA60 / MA200: 20.77 / 18.73 / 17.14
- gap20 / gap60: -0.59% / 10.28%
- 5D return: 0.10%
- 20D high/low: 21.77 / 19.35

### Relative Strength

- ratio: 0.570284
- ratio_MA60: 0.518423
- ratio_gap: 10.00%
- ratio_slope_proxy(20d): 0.022163

### Volume (if available)

- volume: 18484800.00
- volume_MA20: 22113065.00
- volume_ratio: 0.84

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.28
- MA20 / MA60 / MA200: 5.67 / 5.50 / 5.66
- gap20 / gap60: -6.93% / -3.92%
- 5D return: -3.12%
- 20D high/low: 6.22 / 5.28

### Relative Strength

- ratio: 0.013546
- ratio_MA60: 0.013757
- ratio_gap: -1.54%
- ratio_slope_proxy(20d): -0.000032

### Volume (if available)

- volume: 50398400.00
- volume_MA20: 44616895.00
- volume_ratio: 1.13

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

- close: 12.89
- MA20 / MA60 / MA200: 14.33 / 13.73 / 11.87
- gap20 / gap60: -10.03% / -6.09%
- 5D return: -5.64%
- 20D high/low: 15.76 / 12.62

### Relative Strength

- ratio: 0.047803
- ratio_MA60: 0.050918
- ratio_gap: -6.12%
- ratio_slope_proxy(20d): 0.000749

### Volume (if available)

- volume: 13299000.00
- volume_MA20: 15255235.00
- volume_ratio: 0.87

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

- 데이터 기준일(주가): **2026-09-28**
- 실행시간(UTC): **2026-09-29 02:16:53**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 33.0 bp / latest 2.93
- IG OAS 4주 변화: 2.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 41.0 bp / latest 2.83
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.83% / slope_proxy: 0.017949
- GDXJ/GLD gap: 4.13% / slope_proxy: 0.014556

## VZLA (Vizsla Silver)
- close: 3.82 | RSI14: 46.558076 | ATR14%: 5.54%
- MA20 gap: -4.28% | MA50 gap: 1.68% | MA200 gap: -4.68%
- vol_ratio(Volume/Vol20): 0.91343 | gap_open: 4.81%
- RS vs SILJ gap: 7.49% / slope_proxy: 0.001526
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
- close: 9.02 | RSI14: 49.005019 | ATR14%: 7.23%
- MA20 gap: -4.09% | MA50 gap: 4.96% | MA200 gap: 0.09%
- vol_ratio(Volume/Vol20): 1.500103 | gap_open: 7.17%
- SilverMarginGate: SI=60.945 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.55% / slope_proxy: 0.019278
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
- close: 19.6 | RSI14: 39.809071 | ATR14%: 8.30%
- MA20 gap: -9.52% | MA50 gap: -14.55% | MA200 gap: -36.10%
- vol_ratio(Volume/Vol20): 1.066325 | gap_open: 5.68%
- RS vs SILJ gap: -11.18% / slope_proxy: -0.070244
- RS vs GDXJ gap: -13.95% / slope_proxy: -0.022295
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

- 실행시간(UTC): **2026-09-29 02:17:02**
- 데이터 기준일(주가): **2026-09-28**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.93 / 4주 변화 0.33 bp-ish / 2026-09-25
- IG OAS: 0.81 / 4주 변화 0.02 bp-ish / 2026-09-25
- 10Y Real Yield: 2.83 / 4주 변화 0.49 bp-ish / 2026-09-25
- VIX: 14.21 / 4주 변화 -1.24 / 2026-09-22
- NFCI: -0.56 / 4주 변화 -0.05 / 2026-09-18

### Leadership ratios

- GDX/GLD: gap 4.27% / slope_proxy -3.58%
- GDXJ/GLD: gap 4.13% / slope_proxy -3.61%
- SILJ/SLV: gap 0.83% / slope_proxy -3.63%
- Gold breadth proxy: above50 23.08%, above200 30.77%, count 13
- Silver breadth proxy: above50 30.77%, above200 23.08%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.43 | RSI14: 39.08 | ATR14%: 4.98%
- MA20/50/200 gap: -6.50% / 0.55% / 21.43%
- 5D return: -7.09% | 20D drawdown: -10.53% | vol_ratio: 1.22
- RS vs GDXJ: gap 4.51% / slope_proxy 5.10%
- FundamentalScore: 88 | TechnicalScore: 100 | RegimeScore: 30 | OverallScore: **80.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.14 | RSI14: 38.44 | ATR14%: 5.49%
- MA20/50/200 gap: -7.95% / 2.23% / 0.77%
- 5D return: -7.99% | 20D drawdown: -14.39% | vol_ratio: 0.58
- RS vs GDXJ: gap 7.50% / slope_proxy 4.65%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **56.9**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.36 | RSI14: 32.67 | ATR14%: 6.17%
- MA20/50/200 gap: -9.67% / 1.11% / 18.83%
- 5D return: -13.55% | 20D drawdown: -15.41% | vol_ratio: 1.36
- RS vs GDXJ: gap 5.12% / slope_proxy 1.38%
- FundamentalScore: 55 | TechnicalScore: 80 | RegimeScore: 30 | OverallScore: **58.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.14 | RSI14: 25.61 | ATR14%: 8.24%
- MA20/50/200 gap: -20.14% / -18.03% / -23.56%
- 5D return: -22.45% | 20D drawdown: -28.75% | vol_ratio: 1.25
- RS vs GDXJ: gap -15.47% / slope_proxy -15.35%
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.53 | RSI14: 40.11 | ATR14%: 6.45%
- MA20/50/200 gap: -6.03% / 2.72% / 35.93%
- 5D return: -7.50% | 20D drawdown: -12.67% | vol_ratio: 1.09
- RS vs SILJ: gap 10.67% / slope_proxy 7.90%
- FundamentalScore: 86 | TechnicalScore: 100 | RegimeScore: 30 | OverallScore: **79.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.02 | RSI14: 42.75 | ATR14%: 7.61%
- MA20/50/200 gap: -4.09% / 4.96% / 0.09%
- 5D return: -0.11% | 20D drawdown: -13.52% | vol_ratio: 1.50
- RS vs SILJ: gap 13.55% / slope_proxy 9.43%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **58.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.96 | RSI14: 27.35 | ATR14%: 6.72%
- MA20/50/200 gap: -12.30% / -7.75% / -9.98%
- 5D return: -11.55% | 20D drawdown: -21.88% | vol_ratio: 1.10
- RS vs SILJ: gap -1.88% / slope_proxy -5.00%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **53.4**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.82 | RSI14: 41.56 | ATR14%: 5.73%
- MA20/50/200 gap: -4.28% / 1.68% / -4.68%
- 5D return: -6.14% | 20D drawdown: -11.16% | vol_ratio: 0.91
- RS vs SILJ: gap 7.49% / slope_proxy 7.10%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **52.4**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.01 | RSI14: 28.52 | ATR14%: 5.90%
- MA20/50/200 gap: -11.62% / -6.01% / -11.47%
- 5D return: -7.30% | 20D drawdown: -19.80% | vol_ratio: 1.11
- RS vs SILJ: gap -0.70% / slope_proxy -2.79%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **51.6**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.50 | RSI14: 38.10 | ATR14%: 7.02%
- MA20/50/200 gap: -10.79% / -7.40% / -23.85%
- 5D return: -10.36% | 20D drawdown: -18.77% | vol_ratio: 1.04
- RS vs SILJ: gap -2.48% / slope_proxy -4.85%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.61 | RSI14: 24.47 | ATR14%: 6.75%
- MA20/50/200 gap: -15.18% / -14.99% / -20.07%
- 5D return: -9.22% | 20D drawdown: -27.05% | vol_ratio: 0.84
- RS vs SILJ: gap -11.16% / slope_proxy -12.74%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **38.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 19.60 | RSI14: 36.09 | ATR14%: 7.69%
- MA20/50/200 gap: -9.52% / -14.55% / -36.10%
- 5D return: -4.53% | 20D drawdown: -16.35% | vol_ratio: 1.07
- RS vs SILJ: gap -11.18% / slope_proxy -5.01%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **35.4**
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
