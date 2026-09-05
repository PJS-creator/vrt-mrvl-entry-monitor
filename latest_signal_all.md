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

- 실행시간(UTC): **2026-09-05 03:01:14**
- 데이터 기준일(일봉): **2026-09-04**
- 데이터 기준일(주봉): **2026-08-31**
- VXN 기준일: **2026-09-03** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 718.96
- Weekly RSI14: **58.66**
- 52W MA: 645.81 / gap: **11.33%**
- 104W MA gap: **24.30%**
- 52W MA 13W slope: **6.49%**
- VXN: **20.16** / 5D change: -0.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 718.96
- Daily RSI14: **53.63**
- 20D gap: **0.20%**
- 50D gap: **1.11%**
- 200D gap: **9.47%**
- MACD hist: -0.2864 / change: 0.3905
- ATR14%: **1.31%**
- 20D high drawdown: **-1.79%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-09-04**
- 실행시간(UTC): **2026-09-05 03:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.65 / 4주 변화 -6.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 -1.0 bp
- VIX (VIXCLS): 14.32
- NFCI: -0.558

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.173643
- MA60: 9.295478
- gap: -1.31%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.394261
- MA60: 0.395917
- gap: -0.42%
- MA60_slope_proxy: 0.006062
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-04**
- 실행시간(UTC): **2026-09-05 03:00:46**

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
- TERM_SPREAD_10Y_POLICY: 142.1 bp / 4주 변화 29.08 bp
- CURVE_10s5s: 47.35 bp / 4주 변화 -1.96 bp

## NWG Price
- close: 697.4
- MA50: 683.236 / gap50: 2.07%
- MA200: 626.8897 / gap200: 11.25%

## Relative Strength
- RS vs FTSE gap: 1.80% / slope_proxy: 0.002618
- RS vs Peers gap: 0.59% / slope_proxy: 0.017653

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-05 03:00:53**

## Commodity Regime

- WTI ref (CL=F): 91.22 / 5D 9.38%
- Brent ref (BZ=F): 95.83 / 5D 7.30%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.61
- Gas ref (NG=F): 2.94 / 5D 1.77%

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

- close: 60.04
- MA20 / MA60 / MA200: 59.61 / 55.62 / 52.14
- gap20 / gap60: 0.72% / 7.94%
- 5D return: 1.59%
- 20D high/low: 61.52 / 57.70

### Relative Strength

- ratio: 0.937246
- ratio_MA60: 0.951390
- ratio_gap: -1.49%
- ratio_slope_proxy(20d): -0.016600

### Volume (if available)

- volume: 6886300.00
- volume_MA20: 7126095.00
- volume_ratio: 0.97

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.12
- MA20 / MA60 / MA200: 18.47 / 17.57 / 16.48
- gap20 / gap60: 8.95% / 14.49%
- 5D return: 8.58%
- 20D high/low: 20.86 / 17.25

### Relative Strength

- ratio: 0.531432
- ratio_MA60: 0.498444
- ratio_gap: 6.62%
- ratio_slope_proxy(20d): 0.000455

### Volume (if available)

- volume: 18780100.00
- volume_MA20: 20419245.00
- volume_ratio: 0.92

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

- close: 5.85
- MA20 / MA60 / MA200: 5.83 / 5.44 / 5.56
- gap20 / gap60: 0.30% / 7.54%
- 5D return: 0.86%
- 20D high/low: 6.22 / 5.60

### Relative Strength

- ratio: 0.013683
- ratio_MA60: 0.013760
- ratio_gap: -0.56%
- ratio_slope_proxy(20d): -0.000363

### Volume (if available)

- volume: 40656700.00
- volume_MA20: 41686410.00
- volume_ratio: 0.98

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

- close: 14.42
- MA20 / MA60 / MA200: 14.19 / 13.03 / 11.36
- gap20 / gap60: 1.63% / 10.69%
- 5D return: 1.69%
- 20D high/low: 15.11 / 13.22

### Relative Strength

- ratio: 0.049384
- ratio_MA60: 0.049981
- ratio_gap: -1.20%
- ratio_slope_proxy(20d): -0.001444

### Volume (if available)

- volume: 7469300.00
- volume_MA20: 13535980.00
- volume_ratio: 0.55

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

- 데이터 기준일(주가): **2026-09-04**
- 실행시간(UTC): **2026-09-05 03:01:00**

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
- VIX: 14.32
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 8.47% / slope_proxy: 0.027707
- GDXJ/GLD gap: 13.20% / slope_proxy: 0.011263

## VZLA (Vizsla Silver)
- close: 4.0 | RSI14: 55.976941 | ATR14%: 5.07%
- MA20 gap: 2.13% | MA50 gap: 13.71% | MA200 gap: -1.58%
- vol_ratio(Volume/Vol20): 0.998983 | gap_open: 3.60%
- RS vs SILJ gap: -0.71% / slope_proxy: 0.000911
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
- close: 9.94 | RSI14: 61.243092 | ATR14%: 6.09%
- MA20 gap: 5.64% | MA50 gap: 28.33% | MA200 gap: 12.43%
- vol_ratio(Volume/Vol20): 0.897891 | gap_open: 3.74%
- SilverMarginGate: SI=66.82 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.44% / slope_proxy: 0.011172
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
- close: 22.690001 | RSI14: 44.447723 | ATR14%: 8.17%
- MA20 gap: -10.82% | MA50 gap: -1.77% | MA200 gap: -24.11%
- vol_ratio(Volume/Vol20): 0.883588 | gap_open: 3.86%
- RS vs SILJ gap: -15.56% / slope_proxy: -0.093317
- RS vs GDXJ gap: -18.36% / slope_proxy: -0.028112
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

- 실행시간(UTC): **2026-09-05 03:01:11**
- 데이터 기준일(주가): **2026-09-04**

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
- VIX: 14.32 / 4주 변화 -0.83 / 2026-09-03
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-08-28

### Leadership ratios

- GDX/GLD: gap 13.40% / slope_proxy 8.55%
- GDXJ/GLD: gap 13.20% / slope_proxy 7.50%
- SILJ/SLV: gap 8.47% / slope_proxy 5.33%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 92.31%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.18 | RSI14: 54.34 | ATR14%: 4.95%
- MA20/50/200 gap: -0.44% / 18.72% / 37.40%
- 5D return: -0.10% | 20D drawdown: -8.04% | vol_ratio: 0.50
- RS vs GDXJ: gap 2.34% / slope_proxy -2.89%
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
- close: 8.11 | RSI14: 67.18 | ATR14%: 4.84%
- MA20/50/200 gap: 8.31% / 30.41% / 15.88%
- 5D return: 5.05% | 20D drawdown: -0.73% | vol_ratio: 0.49
- RS vs GDXJ: gap 12.92% / slope_proxy 8.36%
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
- close: 1.56 | RSI14: 46.67 | ATR14%: 4.81%
- MA20/50/200 gap: 0.61% / 18.11% / 4.69%
- 5D return: 1.30% | 20D drawdown: -5.45% | vol_ratio: 0.22
- RS vs GDXJ: gap 0.60% / slope_proxy -0.96%
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
- close: 2.68 | RSI14: 66.37 | ATR14%: 6.50%
- MA20/50/200 gap: 7.98% / 28.67% / 39.49%
- 5D return: 0.75% | 20D drawdown: -3.94% | vol_ratio: 0.41
- RS vs GDXJ: gap 13.69% / slope_proxy 13.17%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **62.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.12 | RSI14: 58.31 | ATR14%: 6.18%
- MA20/50/200 gap: 3.80% / 21.65% / 13.08%
- 5D return: 3.35% | 20D drawdown: -3.05% | vol_ratio: 0.92
- RS vs SILJ: gap 7.70% / slope_proxy 2.39%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.68 | RSI14: 58.79 | ATR14%: 5.69%
- MA20/50/200 gap: 5.02% / 21.13% / 8.99%
- 5D return: 1.47% | 20D drawdown: -3.50% | vol_ratio: 0.50
- RS vs SILJ: gap 7.32% / slope_proxy 11.10%
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
- close: 9.94 | RSI14: 61.42 | ATR14%: 6.60%
- MA20/50/200 gap: 5.64% / 28.33% / 12.43%
- 5D return: 4.41% | 20D drawdown: -4.61% | vol_ratio: 0.90
- RS vs SILJ: gap 14.44% / slope_proxy 4.37%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.33 | RSI14: 51.85 | ATR14%: 6.01%
- MA20/50/200 gap: -0.16% / 12.61% / 5.82%
- 5D return: -1.87% | 20D drawdown: -5.17% | vol_ratio: 1.10
- RS vs SILJ: gap -1.33% / slope_proxy -5.46%
- FundamentalScore: 60 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **68.2**
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 28.91 | RSI14: 57.67 | ATR14%: 6.26%
- MA20/50/200 gap: 5.16% / 24.74% / 58.00%
- 5D return: 3.36% | 20D drawdown: -3.05% | vol_ratio: 0.78
- RS vs SILJ: gap 12.58% / slope_proxy -2.37%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.00 | RSI14: 60.36 | ATR14%: 5.24%
- MA20/50/200 gap: 2.13% / 13.71% / -1.58%
- 5D return: 0.00% | 20D drawdown: -4.08% | vol_ratio: 1.00
- RS vs SILJ: gap -0.71% / slope_proxy -2.80%
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
- close: 5.36 | RSI14: 53.65 | ATR14%: 6.04%
- MA20/50/200 gap: 0.75% / 14.18% / -8.51%
- 5D return: -1.47% | 20D drawdown: -6.62% | vol_ratio: 0.61
- RS vs SILJ: gap -2.29% / slope_proxy -1.49%
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
- close: 22.69 | RSI14: 39.88 | ATR14%: 8.84%
- MA20/50/200 gap: -10.82% / -1.77% / -24.11%
- 5D return: -4.76% | 20D drawdown: -18.67% | vol_ratio: 0.88
- RS vs SILJ: gap -15.56% / slope_proxy -21.61%
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
