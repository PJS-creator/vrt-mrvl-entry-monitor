# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-18 03:01:43**
- 데이터 기준일(일봉): **2026-08-17**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-14** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 729.87
- Weekly RSI14: **61.96**
- 52W MA: 640.47 / gap: **13.96%**
- 104W MA gap: **27.25%**
- 52W MA 13W slope: **6.96%**
- VXN: **20.72** / 5D change: -2.10

## Daily trigger: 실제 매수 타이밍

- QQQ close: 729.87
- Daily RSI14: **58.91**
- 20D gap: **3.41%**
- 50D gap: **2.43%**
- 200D gap: **12.28%**
- MACD hist: 3.9740 / change: -0.3897
- ATR14%: **1.66%**
- 20D high drawdown: **-0.30%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
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

- 데이터 기준일(주가): **2026-08-17**
- 실행시간(UTC): **2026-08-18 03:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.67 / 4주 변화 -6.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.41 / 4주 변화 10.0 bp
- VIX (VIXCLS): 14.25
- NFCI: -0.549

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.050254
- MA60: 9.302495
- gap: -2.71%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.394448
- MA60: 0.395674
- gap: -0.31%
- MA60_slope_proxy: 0.015115
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-18 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 119.37 bp / 4주 변화 -2.11 bp
- CURVE_10s5s: 47.51 bp / 4주 변화 0.7 bp

## NWG Price
- close: 707.8
- MA50: 666.5408 / gap50: 6.19%
- MA200: 621.1876 / gap200: 13.94%

## Relative Strength
- RS vs FTSE gap: 6.46% / slope_proxy: 0.002982
- RS vs Peers gap: 3.39% / slope_proxy: 0.012361

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-18 03:01:26**

## Commodity Regime

- WTI ref (CL=F): 84.98 / 5D 3.47%
- Brent ref (BZ=F): 91.23 / 5D 4.00%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.25
- Gas ref (NG=F): 2.71 / 5D -3.19%

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

- close: 59.04
- MA20 / MA60 / MA200: 56.72 / 55.06 / 50.78
- gap20 / gap60: 4.08% / 7.23%
- 5D return: 0.66%
- 20D high/low: 59.06 / 53.81

### Relative Strength

- ratio: 0.943432
- ratio_MA60: 0.964691
- ratio_gap: -2.20%
- ratio_slope_proxy(20d): -0.013160

### Volume (if available)

- volume: 5524531.00
- volume_MA20: 8360571.55
- volume_ratio: 0.66

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.25
- MA20 / MA60 / MA200: 18.45 / 17.89 / 16.47
- gap20 / gap60: -1.09% / 2.03%
- 5D return: -0.44%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.537239
- ratio_MA60: 0.510494
- ratio_gap: 5.24%
- ratio_slope_proxy(20d): -0.007275

### Volume (if available)

- volume: 19798551.00
- volume_MA20: 15104407.55
- volume_ratio: 1.31

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

- close: 5.87
- MA20 / MA60 / MA200: 5.37 / 5.53 / 5.43
- gap20 / gap60: 9.37% / 6.10%
- 5D return: 2.62%
- 20D high/low: 5.87 / 4.95

### Relative Strength

- ratio: 0.013760
- ratio_MA60: 0.013902
- ratio_gap: -1.02%
- ratio_slope_proxy(20d): -0.000541

### Volume (if available)

- volume: 42543831.00
- volume_MA20: 46829616.55
- volume_ratio: 0.91

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.75
- MA20 / MA60 / MA200: 13.53 / 12.66 / 10.92
- gap20 / gap60: 1.60% / 8.62%
- 5D return: -3.58%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.051512
- ratio_MA60: 0.050865
- ratio_gap: 1.27%
- ratio_slope_proxy(20d): 0.000190

### Volume (if available)

- volume: 10384505.00
- volume_MA20: 15121485.25
- volume_ratio: 0.69

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-17**
- 실행시간(UTC): **2026-08-18 03:01:33**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.67
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.41
- VIX: 14.25
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 7.17% / slope_proxy: 0.016702
- GDXJ/GLD gap: 9.84% / slope_proxy: -0.002021

## VZLA (Vizsla Silver)
- close: 3.65 | RSI14: 56.34922 | ATR14%: 5.01%
- MA20 gap: 5.13% | MA50 gap: 8.51% | MA200 gap: -10.55%
- vol_ratio(Volume/Vol20): 1.209107 | gap_open: 0.53%
- RS vs SILJ gap: -4.19% / slope_proxy: 0.005208
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
- close: 8.75 | RSI14: 68.501606 | ATR14%: 5.70%
- MA20 gap: 19.32% | MA50 gap: 26.44% | MA200 gap: 2.60%
- vol_ratio(Volume/Vol20): 1.686816 | gap_open: 0.00%
- SilverMarginGate: SI=65.400002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.10% / slope_proxy: -0.002214
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
- close: 26.32 | RSI14: 59.325151 | ATR14%: 6.68%
- MA20 gap: 13.83% | MA50 gap: 13.69% | MA200 gap: -8.43%
- vol_ratio(Volume/Vol20): 1.069851 | gap_open: 0.89%
- RS vs SILJ gap: -3.51% / slope_proxy: -0.126384
- RS vs GDXJ gap: -7.05% / slope_proxy: -0.03306
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

- 실행시간(UTC): **2026-08-18 03:01:42**
- 데이터 기준일(주가): **2026-08-17**

## Verdict
**⏸ No confirmed entry; watchlist only**

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

- HY OAS: 2.67 / 4주 변화 -0.06 bp-ish / 2026-08-14
- IG OAS: 0.80 / 4주 변화 0.01 bp-ish / 2026-08-14
- 10Y Real Yield: 2.41 / 4주 변화 0.10 bp-ish / 2026-08-14
- VIX: 14.25 / 4주 변화 -4.52 / 2026-08-14
- NFCI: -0.55 / 4주 변화 -0.09 / 2026-08-07

### Leadership ratios

- GDX/GLD: gap 9.39% / slope_proxy 14.49%
- GDXJ/GLD: gap 9.84% / slope_proxy 14.61%
- SILJ/SLV: gap 7.17% / slope_proxy 6.31%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 100.00%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.84 | RSI14: 78.12 | ATR14%: 5.83%
- MA20/50/200 gap: 19.23% / 26.09% / 39.47%
- 5D return: 1.97% | 20D drawdown: -2.77% | vol_ratio: 1.05
- RS vs GDXJ: gap 8.21% / slope_proxy 12.25%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **77.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.99 | RSI14: 89.90 | ATR14%: 4.84%
- MA20/50/200 gap: 16.45% / 24.33% / 1.81%
- 5D return: 1.45% | 20D drawdown: -0.29% | vol_ratio: 0.94
- RS vs GDXJ: gap 5.78% / slope_proxy 7.52%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.60 | RSI14: 86.96 | ATR14%: 5.20%
- MA20/50/200 gap: 27.44% / 29.83% / 8.30%
- 5D return: 10.34% | 20D drawdown: 0.00% | vol_ratio: 2.67
- RS vs GDXJ: gap 11.34% / slope_proxy 15.61%
- FundamentalScore: 70 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **69.2**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.31 | RSI14: 69.64 | ATR14%: 5.78%
- MA20/50/200 gap: 16.23% / 27.77% / 25.26%
- 5D return: 5.96% | 20D drawdown: -0.86% | vol_ratio: 0.77
- RS vs GDXJ: gap 8.96% / slope_proxy -1.19%
- FundamentalScore: 55 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **48.5**
- Checks:
  - sector_ok: **False**
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
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.14 | RSI14: 73.11 | ATR14%: 5.85%
- MA20/50/200 gap: 14.74% / 20.28% / 5.40%
- 5D return: -0.98% | 20D drawdown: -4.88% | vol_ratio: 1.77
- RS vs SILJ: gap 6.22% / slope_proxy 3.64%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
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
- close: 18.82 | RSI14: 74.29 | ATR14%: 4.95%
- MA20/50/200 gap: 16.97% / 20.21% / 1.71%
- 5D return: 7.24% | 20D drawdown: 0.00% | vol_ratio: 1.12
- RS vs SILJ: gap 6.34% / slope_proxy 3.16%
- FundamentalScore: 78 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **72.8**
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.67 | RSI14: 76.51 | ATR14%: 6.03%
- MA20/50/200 gap: 15.16% / 29.34% / 55.92%
- 5D return: -4.48% | 20D drawdown: -4.89% | vol_ratio: 0.91
- RS vs SILJ: gap 17.61% / slope_proxy 16.06%
- FundamentalScore: 86 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **71.2**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.75 | RSI14: 79.76 | ATR14%: 6.15%
- MA20/50/200 gap: 19.32% / 26.44% / 2.60%
- 5D return: 4.17% | 20D drawdown: -2.56% | vol_ratio: 1.69
- RS vs SILJ: gap 11.10% / slope_proxy 15.55%
- FundamentalScore: 74 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **71.1**
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
- close: 3.65 | RSI14: 66.20 | ATR14%: 4.94%
- MA20/50/200 gap: 5.13% / 8.51% / -10.55%
- 5D return: -5.93% | 20D drawdown: -5.93% | vol_ratio: 1.21
- RS vs SILJ: gap -4.19% / slope_proxy -7.02%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **57.9**
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.20 | RSI14: 72.97 | ATR14%: 5.45%
- MA20/50/200 gap: 15.12% / 16.89% / 7.02%
- 5D return: -1.50% | 20D drawdown: -2.44% | vol_ratio: 0.96
- RS vs SILJ: gap 3.17% / slope_proxy -0.26%
- FundamentalScore: 60 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **50.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.16 | RSI14: 73.88 | ATR14%: 5.81%
- MA20/50/200 gap: 15.19% / 11.69% / -10.40%
- 5D return: 0.58% | 20D drawdown: -1.53% | vol_ratio: 0.98
- RS vs SILJ: gap -3.65% / slope_proxy 4.72%
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
- close: 26.32 | RSI14: 72.17 | ATR14%: 6.70%
- MA20/50/200 gap: 13.83% / 13.69% / -8.43%
- 5D return: -3.55% | 20D drawdown: -4.40% | vol_ratio: 1.07
- RS vs SILJ: gap -3.51% / slope_proxy 6.46%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
