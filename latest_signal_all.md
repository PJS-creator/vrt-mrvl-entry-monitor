# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-14 15:02:00**
- 데이터 기준일(일봉): **2026-10-14**
- 데이터 기준일(주봉): **2026-10-12**
- VXN 기준일: **2026-10-13** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 735.33
- Weekly RSI14: **59.41**
- 52W MA: 661.58 / gap: **11.15%**
- 104W MA gap: **24.11%**
- 52W MA 13W slope: **5.71%**
- VXN: **21.14** / 5D change: -0.01

## Daily trigger: 실제 매수 타이밍

- QQQ close: 735.33
- Daily RSI14: **48.65**
- 20D gap: **-1.00%**
- 50D gap: **1.24%**
- 200D gap: **9.31%**
- MACD hist: -1.6824 / change: -1.0269
- ATR14%: **1.20%**
- 20D high drawdown: **-3.20%**

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

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-14 15:01:22**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.11 / 4주 변화 40.0 bp
- IG OAS (BAMLC0A0CM): 0.83 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.91 / 4주 변화 31.0 bp
- VIX (VIXCLS): 15.27
- NFCI: -0.494

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.094484
- MA60: 8.627933
- gap: -6.18%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.446046
- MA60: 0.402808
- gap: 10.73%
- MA60_slope_proxy: 0.013292
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-14 15:01:26**

## Verdict
🟡 ENTRY (LOOSE): Risk+Curve + PriceConfirm (Demand monthly not confirmed)

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **True**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **True**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 163.68 bp / 4주 변화 1.69 bp
- CURVE_10s5s: 41.46 bp / 4주 변화 -1.32 bp

## NWG Price
- close: 665.4
- MA50: 687.4537 / gap50: -3.21%
- MA200: 635.4266 / gap200: 4.72%

## Relative Strength
- RS vs FTSE gap: -2.81% / slope_proxy: 0.000162
- RS vs Peers gap: 4.91% / slope_proxy: 0.014335

## Why not today?
- DemandGreen=FALSE (monthly)

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-14 15:01:33**

## Commodity Regime

- WTI ref (CL=F): 95.03 / 5D 7.65%
- Brent ref (BZ=F): 105.75 / 5D 5.54%
- Brent Tier: **>=90**
- Brent-WTI spread: 10.72
- Gas ref (NG=F): 3.18 / 5D -0.66%

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

- close: 61.80
- MA20 / MA60 / MA200: 58.30 / 58.41 / 54.42
- gap20 / gap60: 6.00% / 5.80%
- 5D return: 6.17%
- 20D high/low: 61.80 / 54.94

### Relative Strength

- ratio: 0.918208
- ratio_MA60: 0.939843
- ratio_gap: -2.30%
- ratio_slope_proxy(20d): -0.009305

### Volume (if available)

- volume: 2078925.00
- volume_MA20: 8927116.25
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 25.73
- MA20 / MA60 / MA200: 22.44 / 20.03 / 17.87
- gap20 / gap60: 14.66% / 28.45%
- 5D return: 7.26%
- 20D high/low: 25.73 / 20.37

### Relative Strength

- ratio: 0.609179
- ratio_MA60: 0.536807
- ratio_gap: 13.48%
- ratio_slope_proxy(20d): 0.030768

### Volume (if available)

- volume: 4745058.00
- volume_MA20: 23182972.90
- volume_ratio: 0.20

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

- close: 5.70
- MA20 / MA60 / MA200: 5.45 / 5.55 / 5.74
- gap20 / gap60: 4.54% / 2.62%
- 5D return: 5.66%
- 20D high/low: 5.70 / 5.17

### Relative Strength

- ratio: 0.014714
- ratio_MA60: 0.013833
- ratio_gap: 6.37%
- ratio_slope_proxy(20d): 0.000106

### Volume (if available)

- volume: 15872962.00
- volume_MA20: 36793988.10
- volume_ratio: 0.43

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.48
- MA20 / MA60 / MA200: 13.25 / 13.80 / 12.28
- gap20 / gap60: 1.77% / -2.29%
- 5D return: 3.33%
- 20D high/low: 14.42 / 12.54

### Relative Strength

- ratio: 0.047669
- ratio_MA60: 0.050598
- ratio_gap: -5.79%
- ratio_slope_proxy(20d): 0.000122

### Volume (if available)

- volume: 2736872.00
- volume_MA20: 12141228.60
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-14**
- 실행시간(UTC): **2026-10-14 15:01:41**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 40.0 bp / latest 3.11
- IG OAS 4주 변화: 3.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 31.0 bp / latest 2.91
- VIX: 15.27
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.11% / slope_proxy: 0.007583
- GDXJ/GLD gap: -5.17% / slope_proxy: 0.012761

## VZLA (Vizsla Silver)
- close: 3.205 | RSI14: 31.414542 | ATR14%: 5.70%
- MA20 gap: -14.24% | MA50 gap: -16.24% | MA200 gap: -17.73%
- vol_ratio(Volume/Vol20): 0.313182 | gap_open: 3.57%
- RS vs SILJ gap: -1.28% / slope_proxy: 0.002601
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.935 | RSI14: 39.346833 | ATR14%: 6.93%
- MA20 gap: -10.78% | MA50 gap: -13.00% | MA200 gap: -11.51%
- vol_ratio(Volume/Vol20): 0.637876 | gap_open: 5.08%
- SilverMarginGate: SI=56.314999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.32% / slope_proxy: 0.021528
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 16.76 | RSI14: 33.434877 | ATR14%: 7.42%
- MA20 gap: -14.33% | MA50 gap: -25.48% | MA200 gap: -45.46%
- vol_ratio(Volume/Vol20): 0.389289 | gap_open: 3.27%
- RS vs SILJ gap: -12.92% / slope_proxy: -0.051932
- RS vs GDXJ gap: -16.34% / slope_proxy: -0.017735
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-10-14 15:01:58**
- 데이터 기준일(주가): **2026-10-14**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

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

- HY OAS: 3.11 / 4주 변화 0.40 bp-ish / 2026-10-12
- IG OAS: 0.83 / 4주 변화 0.03 bp-ish / 2026-10-12
- 10Y Real Yield: 2.91 / 4주 변화 0.31 bp-ish / 2026-10-09
- VIX: 15.27 / 4주 변화 -1.93 / 2026-10-13
- NFCI: -0.49 / 4주 변화 0.01 / 2026-10-02

### Leadership ratios

- GDX/GLD: gap -2.53% / slope_proxy -7.21%
- GDXJ/GLD: gap -5.15% / slope_proxy -9.21%
- SILJ/SLV: gap -2.13% / slope_proxy -3.57%
- Gold breadth proxy: above50 0.00%, above200 7.69%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.59 | RSI14: 23.83 | ATR14%: 4.02%
- MA20/50/200 gap: -9.93% / -12.74% / 7.95%
- 5D return: -2.61% | 20D drawdown: -18.50% | vol_ratio: 0.37
- RS vs GDXJ: gap 1.42% / slope_proxy -4.26%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **50.9**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.37 | RSI14: 22.18 | ATR14%: 5.24%
- MA20/50/200 gap: -11.63% / -13.09% / -9.74%
- 5D return: -9.52% | 20D drawdown: -22.22% | vol_ratio: 0.55
- RS vs GDXJ: gap 0.90% / slope_proxy -4.22%
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
- close: 0.94 | RSI14: 22.58 | ATR14%: 8.36%
- MA20/50/200 gap: -18.54% / -31.19% / -35.96%
- 5D return: -6.00% | 20D drawdown: -38.16% | vol_ratio: 0.49
- RS vs GDXJ: gap -21.39% / slope_proxy -21.63%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.03 | RSI14: 14.46 | ATR14%: 6.16%
- MA20/50/200 gap: -13.98% / -15.48% / 1.77%
- 5D return: -8.14% | 20D drawdown: -26.98% | vol_ratio: 0.76
- RS vs GDXJ: gap -2.85% / slope_proxy -8.56%
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
- close: 25.29 | RSI14: 35.10 | ATR14%: 4.71%
- MA20/50/200 gap: -7.68% / -7.77% / 24.94%
- 5D return: -3.25% | 20D drawdown: -16.75% | vol_ratio: 0.29
- RS vs SILJ: gap 11.01% / slope_proxy 5.74%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **58.7**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.93 | RSI14: 37.45 | ATR14%: 6.51%
- MA20/50/200 gap: -10.78% / -13.00% / -11.51%
- 5D return: -6.09% | 20D drawdown: -16.91% | vol_ratio: 0.64
- RS vs SILJ: gap 5.32% / slope_proxy 7.19%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **53.3**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.84 | RSI14: 25.19 | ATR14%: 4.75%
- MA20/50/200 gap: -12.75% / -20.51% / -20.77%
- 5D return: -5.77% | 20D drawdown: -25.41% | vol_ratio: 0.28
- RS vs SILJ: gap -5.04% / slope_proxy -7.11%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.24 | RSI14: 25.12 | ATR14%: 4.50%
- MA20/50/200 gap: -12.29% / -17.80% / -20.00%
- 5D return: -6.99% | 20D drawdown: -19.89% | vol_ratio: 0.13
- RS vs SILJ: gap -1.98% / slope_proxy -3.11%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **46.4**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.20 | RSI14: 16.44 | ATR14%: 5.13%
- MA20/50/200 gap: -14.24% / -16.24% / -17.73%
- 5D return: -6.29% | 20D drawdown: -25.47% | vol_ratio: 0.31
- RS vs SILJ: gap -1.28% / slope_proxy -3.69%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **43.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.77 | RSI14: 24.79 | ATR14%: 5.95%
- MA20/50/200 gap: -16.99% / -23.59% / -35.38%
- 5D return: -9.71% | 20D drawdown: -28.42% | vol_ratio: 0.37
- RS vs SILJ: gap -9.02% / slope_proxy -10.34%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **41.9**
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
- close: 4.95 | RSI14: 21.02 | ATR14%: 4.84%
- MA20/50/200 gap: -13.33% / -24.45% / -28.99%
- 5D return: -7.05% | 20D drawdown: -23.81% | vol_ratio: 0.72
- RS vs SILJ: gap -10.79% / slope_proxy -5.27%
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
- close: 16.76 | RSI14: 25.79 | ATR14%: 6.33%
- MA20/50/200 gap: -14.33% / -25.48% / -45.46%
- 5D return: -6.68% | 20D drawdown: -26.13% | vol_ratio: 0.39
- RS vs SILJ: gap -12.92% / slope_proxy -6.11%
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
