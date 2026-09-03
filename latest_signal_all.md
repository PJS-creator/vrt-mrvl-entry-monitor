# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-03 03:01:08**
- 데이터 기준일(일봉): **2026-09-02**
- 데이터 기준일(주봉): **2026-08-31**
- VXN 기준일: **2026-09-01** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 709.24
- Weekly RSI14: **56.15**
- 52W MA: 645.63 / gap: **9.85%**
- 104W MA gap: **22.64%**
- 52W MA 13W slope: **6.46%**
- VXN: **21.96** / 5D change: 0.17

## Daily trigger: 실제 매수 타이밍

- QQQ close: 709.24
- Daily RSI14: **47.62**
- 20D gap: **-1.16%**
- 50D gap: **-0.23%**
- 200D gap: **8.18%**
- MACD hist: -1.1345 / change: -0.1980
- ATR14%: **1.38%**
- 20D high drawdown: **-3.12%**

## Checks

- weekly_good: **True**
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

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-03 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.65 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.44 / 4주 변화 4.0 bp
- VIX (VIXCLS): 16.34
- NFCI: -0.558

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.40537
- MA60: 9.093222
- gap: -7.56%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.375091
- MA60: 0.397944
- gap: -5.74%
- MA60_slope_proxy: 0.010662
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-03 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 131.31 bp / 4주 변화 3.74 bp
- CURVE_10s5s: 46.96 bp / 4주 변화 0.08 bp

## NWG Price
- close: 682.8
- MA50: 681.6357 / gap50: 0.17%
- MA200: 625.9613 / gap200: 9.08%

## Relative Strength
- RS vs FTSE gap: 0.40% / slope_proxy: 0.002732
- RS vs Peers gap: 0.33% / slope_proxy: 0.019062

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-03 03:00:54**

## Commodity Regime

- WTI ref (CL=F): 91.01 / 5D 10.68%
- Brent ref (BZ=F): 95.46 / 5D 8.67%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.45
- Gas ref (NG=F): 3.01 / 5D 5.88%

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

- close: 60.91
- MA20 / MA60 / MA200: 59.17 / 55.50 / 51.96
- gap20 / gap60: 2.93% / 9.74%
- 5D return: 3.91%
- 20D high/low: 61.52 / 55.91

### Relative Strength

- ratio: 0.935638
- ratio_MA60: 0.953057
- ratio_gap: -1.83%
- ratio_slope_proxy(20d): -0.015116

### Volume (if available)

- volume: 5280500.00
- volume_MA20: 7688325.00
- volume_ratio: 0.69

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
- MA20 / MA60 / MA200: 18.21 / 17.48 / 16.41
- gap20 / gap60: 14.57% / 19.35%
- 5D return: 17.46%
- 20D high/low: 20.86 / 17.25

### Relative Strength

- ratio: 0.547650
- ratio_MA60: 0.497972
- ratio_gap: 9.98%
- ratio_slope_proxy(20d): -0.000816

### Volume (if available)

- volume: 24307100.00
- volume_MA20: 20168215.00
- volume_ratio: 1.21

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

- close: 6.22
- MA20 / MA60 / MA200: 5.76 / 5.44 / 5.54
- gap20 / gap60: 7.99% / 14.34%
- 5D return: 11.07%
- 20D high/low: 6.22 / 5.16

### Relative Strength

- ratio: 0.014247
- ratio_MA60: 0.013768
- ratio_gap: 3.48%
- ratio_slope_proxy(20d): -0.000412

### Volume (if available)

- volume: 53348100.00
- volume_MA20: 41371910.00
- volume_ratio: 1.29

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.73
- MA20 / MA60 / MA200: 14.09 / 12.97 / 11.30
- gap20 / gap60: 4.58% / 13.53%
- 5D return: 3.01%
- 20D high/low: 15.11 / 13.22

### Relative Strength

- ratio: 0.049787
- ratio_MA60: 0.050114
- ratio_gap: -0.65%
- ratio_slope_proxy(20d): -0.001305

### Volume (if available)

- volume: 13967200.00
- volume_MA20: 13847445.00
- volume_ratio: 1.01

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

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-03 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.44
- VIX: 16.34
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 10.48% / slope_proxy: 0.026483
- GDXJ/GLD gap: 14.35% / slope_proxy: 0.008685

## VZLA (Vizsla Silver)
- close: 4.15 | RSI14: 62.079789 | ATR14%: 4.85%
- MA20 gap: 7.19% | MA50 gap: 19.29% | MA200 gap: 1.99%
- vol_ratio(Volume/Vol20): 1.109579 | gap_open: 2.85%
- RS vs SILJ gap: 3.07% / slope_proxy: 0.001559
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
- close: 10.18 | RSI14: 66.51211 | ATR14%: 5.85%
- MA20 gap: 10.54% | MA50 gap: 34.05% | MA200 gap: 15.77%
- vol_ratio(Volume/Vol20): 1.167472 | gap_open: 1.96%
- SilverMarginGate: SI=66.375 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 18.44% / slope_proxy: 0.008675
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
- close: 23.209999 | RSI14: 46.013439 | ATR14%: 8.34%
- MA20 gap: -9.55% | MA50 gap: 0.69% | MA200 gap: -22.03%
- vol_ratio(Volume/Vol20): 1.099976 | gap_open: 2.70%
- RS vs SILJ gap: -14.30% / slope_proxy: -0.099468
- RS vs GDXJ gap: -16.75% / slope_proxy: -0.0298
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

- 실행시간(UTC): **2026-09-03 03:01:05**
- 데이터 기준일(주가): **2026-09-02**

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

- HY OAS: 2.65 / 4주 변화 -0.08 bp-ish / 2026-09-01
- IG OAS: 0.81 / 4주 변화 0.03 bp-ish / 2026-09-01
- 10Y Real Yield: 2.44 / 4주 변화 0.04 bp-ish / 2026-09-01
- VIX: 16.34 / 4주 변화 -0.16 / 2026-09-01
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-08-28

### Leadership ratios

- GDX/GLD: gap 13.49% / slope_proxy 12.55%
- GDXJ/GLD: gap 14.35% / slope_proxy 13.24%
- SILJ/SLV: gap 10.48% / slope_proxy 8.86%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.89 | RSI14: 51.78 | ATR14%: 5.47%
- MA20/50/200 gap: -2.16% / 16.96% / 34.37%
- 5D return: -9.43% | 20D drawdown: -10.66% | vol_ratio: 0.73
- RS vs GDXJ: gap 0.46% / slope_proxy -2.43%
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
- close: 7.68 | RSI14: 61.89 | ATR14%: 4.81%
- MA20/50/200 gap: 4.82% / 25.91% / 10.09%
- 5D return: -2.41% | 20D drawdown: -6.00% | vol_ratio: 0.56
- RS vs GDXJ: gap 8.10% / slope_proxy 4.65%
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
- close: 1.53 | RSI14: 57.58 | ATR14%: 5.39%
- MA20/50/200 gap: -0.20% / 17.21% / 2.86%
- 5D return: -3.77% | 20D drawdown: -7.27% | vol_ratio: 0.48
- RS vs GDXJ: gap -0.54% / slope_proxy -3.89%
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
- close: 2.79 | RSI14: 76.98 | ATR14%: 6.40%
- MA20/50/200 gap: 15.55% / 37.05% / 46.04%
- 5D return: 7.31% | 20D drawdown: 0.00% | vol_ratio: 1.75
- RS vs GDXJ: gap 20.13% / slope_proxy 23.51%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **62.5**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 10.18 | RSI14: 65.47 | ATR14%: 6.10%
- MA20/50/200 gap: 10.54% / 34.05% / 15.77%
- 5D return: 5.71% | 20D drawdown: 0.00% | vol_ratio: 1.17
- RS vs SILJ: gap 18.44% / slope_proxy 10.94%
- FundamentalScore: 74 | TechnicalScore: 100 | RegimeScore: 75 | OverallScore: **83.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.13 | RSI14: 56.74 | ATR14%: 6.44%
- MA20/50/200 gap: 5.98% / 23.61% / 13.60%
- 5D return: 2.20% | 20D drawdown: -1.50% | vol_ratio: 1.16
- RS vs SILJ: gap 8.47% / slope_proxy 9.47%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 28.35 | RSI14: 55.04 | ATR14%: 6.49%
- MA20/50/200 gap: 4.33% / 24.84% / 56.57%
- 5D return: 2.09% | 20D drawdown: -3.21% | vol_ratio: 1.13
- RS vs SILJ: gap 11.75% / slope_proxy -2.29%
- FundamentalScore: 86 | TechnicalScore: 55 | RegimeScore: 75 | OverallScore: **73.0**
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.77 | RSI14: 64.21 | ATR14%: 5.61%
- MA20/50/200 gap: 7.99% / 23.42% / 9.85%
- 5D return: 0.34% | 20D drawdown: -3.08% | vol_ratio: 0.76
- RS vs SILJ: gap 8.43% / slope_proxy 13.74%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.50 | RSI14: 59.08 | ATR14%: 5.80%
- MA20/50/200 gap: 3.40% / 16.48% / 8.72%
- 5D return: -1.19% | 20D drawdown: -2.98% | vol_ratio: 0.97
- RS vs SILJ: gap 1.24% / slope_proxy 2.10%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **64.8**
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
- close: 4.15 | RSI14: 62.58 | ATR14%: 4.88%
- MA20/50/200 gap: 7.19% / 19.29% / 1.99%
- 5D return: 3.23% | 20D drawdown: -0.24% | vol_ratio: 1.11
- RS vs SILJ: gap 3.07% / slope_proxy 2.11%
- FundamentalScore: 72 | TechnicalScore: 100 | RegimeScore: 75 | OverallScore: **82.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.43 | RSI14: 56.99 | ATR14%: 6.09%
- MA20/50/200 gap: 3.25% / 16.44% / -7.05%
- 5D return: -2.51% | 20D drawdown: -5.40% | vol_ratio: 0.74
- RS vs SILJ: gap -1.18% / slope_proxy 0.99%
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
- close: 23.21 | RSI14: 40.91 | ATR14%: 8.60%
- MA20/50/200 gap: -9.55% / 0.70% / -22.03%
- 5D return: -8.84% | 20D drawdown: -16.81% | vol_ratio: 1.10
- RS vs SILJ: gap -14.30% / slope_proxy -15.30%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **44.4**
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
