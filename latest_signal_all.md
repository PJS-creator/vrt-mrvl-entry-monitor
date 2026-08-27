# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA, EXK, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-27 03:33:05**
- 데이터 기준일(일봉): **2026-08-26**
- 데이터 기준일(주봉): **2026-08-24**
- VXN 기준일: **2026-08-25** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 711.37
- Weekly RSI14: **57.01**
- 52W MA: 642.92 / gap: **10.65%**
- 104W MA gap: **23.56%**
- 52W MA 13W slope: **6.61%**
- VXN: **21.79** / 5D change: -0.77

## Daily trigger: 실제 매수 타이밍

- QQQ close: 711.37
- Daily RSI14: **49.34**
- 20D gap: **-0.46%**
- 50D gap: **-0.13%**
- 200D gap: **8.91%**
- MACD hist: -1.2015 / change: -0.0750
- ATR14%: **1.49%**
- 20D high drawdown: **-2.83%**

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

- 데이터 기준일(주가): **2026-08-26**
- 실행시간(UTC): **2026-08-27 03:32:30**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -14.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.32 / 4주 변화 -9.0 bp
- VIX (VIXCLS): 15.45
- NFCI: -0.566

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.264724
- MA60: 9.173699
- gap: -9.91%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.441028
- MA60: 0.405072
- gap: 8.88%
- MA60_slope_proxy: 0.021746
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-26**
- 실행시간(UTC): **2026-08-27 03:32:34**

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
- TERM_SPREAD_10Y_POLICY: 130.13 bp / 4주 변화 7.98 bp
- CURVE_10s5s: 48.22 bp / 4주 변화 3.06 bp

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

- 실행시간(UTC): **2026-08-27 03:32:41**

## Commodity Regime

- WTI ref (CL=F): 81.78 / 5D -4.72%
- Brent ref (BZ=F): 86.42 / 5D -5.68%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.64
- Gas ref (NG=F): 2.92 / 5D 3.70%

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

- close: 58.62
- MA20 / MA60 / MA200: 58.03 / 55.34 / 51.48
- gap20 / gap60: 1.02% / 5.93%
- 5D return: -2.45%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.938972
- ratio_MA60: 0.958209
- ratio_gap: -2.01%
- ratio_slope_proxy(20d): -0.012924

### Volume (if available)

- volume: 6200554.00
- volume_MA20: 8060757.70
- volume_ratio: 0.77

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.76
- MA20 / MA60 / MA200: 17.94 / 17.32 / 16.23
- gap20 / gap60: -1.00% / 2.55%
- 5D return: -1.40%
- 20D high/low: 18.85 / 17.25

### Relative Strength

- ratio: 0.497200
- ratio_MA60: 0.496137
- ratio_gap: 0.21%
- ratio_slope_proxy(20d): -0.003985

### Volume (if available)

- volume: 28992149.00
- volume_MA20: 17595062.45
- volume_ratio: 1.65

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

- close: 5.60
- MA20 / MA60 / MA200: 5.58 / 5.46 / 5.49
- gap20 / gap60: 0.34% / 2.53%
- 5D return: -4.11%
- 20D high/low: 6.01 / 5.08

### Relative Strength

- ratio: 0.013831
- ratio_MA60: 0.013808
- ratio_gap: 0.17%
- ratio_slope_proxy(20d): -0.000481

### Volume (if available)

- volume: 23494553.00
- volume_MA20: 42056257.65
- volume_ratio: 0.56

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

- close: 14.30
- MA20 / MA60 / MA200: 13.68 / 12.82 / 11.13
- gap20 / gap60: 4.56% / 11.58%
- 5D return: 3.70%
- 20D high/low: 14.39 / 12.43

### Relative Strength

- ratio: 0.050338
- ratio_MA60: 0.050366
- ratio_gap: -0.06%
- ratio_slope_proxy(20d): -0.000860

### Volume (if available)

- volume: 15018100.00
- volume_MA20: 13449870.00
- volume_ratio: 1.12

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

- 데이터 기준일(주가): **2026-08-26**
- 실행시간(UTC): **2026-08-27 03:32:49**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -14.0 bp / latest 2.7
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -9.0 bp / latest 2.32
- VIX: 15.45
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 9.97% / slope_proxy: 0.022681
- GDXJ/GLD gap: 15.07% / slope_proxy: 0.003655

## VZLA (Vizsla Silver)
- close: 4.02 | RSI14: 64.633006 | ATR14%: 4.64%
- MA20 gap: 8.88% | MA50 gap: 17.26% | MA200 gap: -1.39%
- vol_ratio(Volume/Vol20): 0.473677 | gap_open: 2.48%
- RS vs SILJ gap: -2.49% / slope_proxy: 0.003175
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
- close: 9.63 | RSI14: 67.720284 | ATR14%: 5.45%
- MA20 gap: 12.60% | MA50 gap: 30.94% | MA200 gap: 10.83%
- vol_ratio(Volume/Vol20): 0.645641 | gap_open: 1.64%
- SilverMarginGate: SI=69.300003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.42% / slope_proxy: 0.003765
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
- close: 25.459999 | RSI14: 52.017102 | ATR14%: 7.50%
- MA20 gap: 1.39% | MA50 gap: 9.67% | MA200 gap: -13.36%
- vol_ratio(Volume/Vol20): 0.961605 | gap_open: 3.37%
- RS vs SILJ gap: -10.61% / slope_proxy: -0.109402
- RS vs GDXJ gap: -14.96% / slope_proxy: -0.030863
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

- 실행시간(UTC): **2026-08-27 03:33:04**
- 데이터 기준일(주가): **2026-08-26**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA, EXK, ASM**

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

- HY OAS: 2.70 / 4주 변화 -0.14 bp-ish / 2026-08-25
- IG OAS: 0.81 / 4주 변화 0.00 bp-ish / 2026-08-25
- 10Y Real Yield: 2.32 / 4주 변화 -0.09 bp-ish / 2026-08-25
- VIX: 15.45 / 4주 변화 -2.76 / 2026-08-25
- NFCI: -0.57 / 4주 변화 -0.10 / 2026-08-21

### Leadership ratios

- GDX/GLD: gap 15.46% / slope_proxy 19.41%
- GDXJ/GLD: gap 15.07% / slope_proxy 20.09%
- SILJ/SLV: gap 9.97% / slope_proxy 12.63%
- Gold breadth proxy: above50 100.00%, above200 92.31%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.92 | RSI14: 79.43 | ATR14%: 5.19%
- MA20/50/200 gap: 15.57% / 32.32% / 50.77%
- 5D return: 5.00% | 20D drawdown: -1.36% | vol_ratio: 0.61
- RS vs GDXJ: gap 7.54% / slope_proxy 9.41%
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
- close: 7.87 | RSI14: 85.40 | ATR14%: 4.26%
- MA20/50/200 gap: 15.56% / 33.25% / 13.42%
- 5D return: 5.07% | 20D drawdown: -0.13% | vol_ratio: 0.58
- RS vs GDXJ: gap 7.06% / slope_proxy 5.16%
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
- close: 1.59 | RSI14: 70.91 | ATR14%: 5.19%
- MA20/50/200 gap: 9.54% / 23.45% / 7.10%
- 5D return: -3.05% | 20D drawdown: -3.64% | vol_ratio: 0.72
- RS vs GDXJ: gap -0.35% / slope_proxy 0.59%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **65.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.60 | RSI14: 75.19 | ATR14%: 5.81%
- MA20/50/200 gap: 17.81% / 34.59% / 37.85%
- 5D return: 5.69% | 20D drawdown: -4.06% | vol_ratio: 0.67
- RS vs GDXJ: gap 10.01% / slope_proxy 4.42%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **62.2**
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.77 | RSI14: 61.01 | ATR14%: 5.57%
- MA20/50/200 gap: 8.47% / 26.85% / 57.08%
- 5D return: 1.91% | 20D drawdown: -0.96% | vol_ratio: 1.05
- RS vs SILJ: gap 9.57% / slope_proxy 4.53%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.89 | RSI14: 67.76 | ATR14%: 6.32%
- MA20/50/200 gap: 11.00% / 23.92% / 12.02%
- 5D return: -0.91% | 20D drawdown: -1.80% | vol_ratio: 0.71
- RS vs SILJ: gap 4.70% / slope_proxy 8.09%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.59 | RSI14: 67.95 | ATR14%: 5.69%
- MA20/50/200 gap: 10.93% / 19.51% / 11.14%
- 5D return: 0.26% | 20D drawdown: -0.13% | vol_ratio: 0.82
- RS vs SILJ: gap 0.38% / slope_proxy 5.86%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.70 | RSI14: 78.14 | ATR14%: 4.89%
- MA20/50/200 gap: 15.48% / 26.27% / 10.28%
- 5D return: 0.78% | 20D drawdown: -1.05% | vol_ratio: 0.94
- RS vs SILJ: gap 6.82% / slope_proxy 6.93%
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
- close: 9.63 | RSI14: 70.96 | ATR14%: 5.77%
- MA20/50/200 gap: 12.60% / 30.94% / 10.83%
- 5D return: 0.94% | 20D drawdown: -1.43% | vol_ratio: 0.65
- RS vs SILJ: gap 11.42% / slope_proxy 9.55%
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
- close: 4.02 | RSI14: 68.99 | ATR14%: 4.62%
- MA20/50/200 gap: 8.88% / 17.26% / -1.39%
- 5D return: 3.34% | 20D drawdown: -0.50% | vol_ratio: 0.47
- RS vs SILJ: gap -2.49% / slope_proxy -4.31%
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
- close: 5.57 | RSI14: 71.03 | ATR14%: 5.23%
- MA20/50/200 gap: 12.30% / 19.34% / -4.15%
- 5D return: 3.34% | 20D drawdown: -0.89% | vol_ratio: 0.79
- RS vs SILJ: gap -2.00% / slope_proxy 9.03%
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
- close: 25.46 | RSI14: 54.95 | ATR14%: 7.91%
- MA20/50/200 gap: 1.39% / 9.67% / -13.36%
- 5D return: -8.75% | 20D drawdown: -8.75% | vol_ratio: 0.96
- RS vs SILJ: gap -10.61% / slope_proxy -2.16%
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
