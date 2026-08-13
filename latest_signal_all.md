# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-13 23:22:25**
- 데이터 기준일(일봉): **2026-08-13**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-12** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 732.07
- Weekly RSI14: **62.47**
- 52W MA: 637.40 / gap: **14.85%**
- 104W MA gap: **28.18%**
- 52W MA 13W slope: **7.18%**
- VXN: **20.97** / 5D change: -3.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 732.07
- Daily RSI14: **60.14**
- 20D gap: **4.23%**
- 50D gap: **2.67%**
- 200D gap: **12.80%**
- MACD hist: 4.4810 / change: 0.2912
- ATR14%: **1.80%**
- 20D high drawdown: **0.00%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-13**
- 실행시간(UTC): **2026-08-13 23:22:03**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 10.0 bp
- VIX (VIXCLS): 14.55
- NFCI: -0.549

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.862921
- MA60: 9.309746
- gap: -4.80%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.377139
- MA60: 0.393717
- gap: -4.21%
- MA60_slope_proxy: 0.013698
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-12**
- 실행시간(UTC): **2026-08-13 23:22:05**

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
- TERM_SPREAD_10Y_POLICY: 119.62 bp / 4주 변화 0.76 bp
- CURVE_10s5s: 47.74 bp / 4주 변화 0.78 bp

## NWG Price
- close: 714.48
- MA50: 662.1728 / gap50: 7.90%
- MA200: 619.9553 / gap200: 15.25%

## Relative Strength
- RS vs FTSE gap: 7.21% / slope_proxy: 0.002855
- RS vs Peers gap: 4.17% / slope_proxy: 0.010038

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-13 23:22:10**

## Commodity Regime

- WTI ref (CL=F): 81.14 / 5D 4.98%
- Brent ref (BZ=F): 86.93 / 5D 5.38%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.79
- Gas ref (NG=F): 2.73 / 5D 3.45%

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

- close: 57.70
- MA20 / MA60 / MA200: 56.36 / 55.09 / 50.60
- gap20 / gap60: 2.38% / 4.75%
- 5D return: 2.96%
- 20D high/low: 59.06 / 53.81

### Relative Strength

- ratio: 0.944972
- ratio_MA60: 0.966254
- ratio_gap: -2.20%
- ratio_slope_proxy(20d): -0.013576

### Volume (if available)

- volume: 6642831.00
- volume_MA20: 8435461.55
- volume_ratio: 0.79

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.89
- MA20 / MA60 / MA200: 18.45 / 17.95 / 16.40
- gap20 / gap60: -3.05% / -0.34%
- 5D return: -3.40%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.529760
- ratio_MA60: 0.511994
- ratio_gap: 3.47%
- ratio_slope_proxy(20d): -0.006100

### Volume (if available)

- volume: 13014718.00
- volume_MA20: 14963075.90
- volume_ratio: 0.87

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.72
- MA20 / MA60 / MA200: 5.29 / 5.59 / 5.41
- gap20 / gap60: 8.06% / 2.41%
- 5D return: 10.85%
- 20D high/low: 5.81 / 4.95

### Relative Strength

- ratio: 0.013932
- ratio_MA60: 0.013992
- ratio_gap: -0.43%
- ratio_slope_proxy(20d): -0.000491

### Volume (if available)

- volume: 60385134.00
- volume_MA20: 45461766.70
- volume_ratio: 1.33

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.54
- MA20 / MA60 / MA200: 13.55 / 12.68 / 10.88
- gap20 / gap60: -0.08% / 6.82%
- 5D return: -0.29%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.050811
- ratio_MA60: 0.051168
- ratio_gap: -0.70%
- ratio_slope_proxy(20d): 0.000744

### Volume (if available)

- volume: 13833170.00
- volume_MA20: 16142063.50
- volume_ratio: 0.86

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

- 데이터 기준일(주가): **2026-08-13**
- 실행시간(UTC): **2026-08-13 23:22:15**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.42
- VIX: 14.55
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 8.72% / slope_proxy: 0.014629
- GDXJ/GLD gap: 7.81% / slope_proxy: -0.004116

## VZLA (Vizsla Silver)
- close: 3.74 | RSI14: 60.704554 | ATR14%: 4.98%
- MA20 gap: 9.60% | MA50 gap: 11.00% | MA200 gap: -8.42%
- vol_ratio(Volume/Vol20): 0.634052 | gap_open: 1.32%
- RS vs SILJ gap: -0.07% / slope_proxy: 0.005646
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
- close: 8.72 | RSI14: 68.273743 | ATR14%: 5.83%
- MA20 gap: 21.05% | MA50 gap: 26.40% | MA200 gap: 2.44%
- vol_ratio(Volume/Vol20): 0.755153 | gap_open: 2.82%
- SilverMarginGate: SI=64.635002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.42% / slope_proxy: -0.002608
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
- close: 26.57 | RSI14: 61.470106 | ATR14%: 6.91%
- MA20 gap: 18.91% | MA50 gap: 13.87% | MA200 gap: -6.93%
- vol_ratio(Volume/Vol20): 0.721097 | gap_open: 4.30%
- RS vs SILJ gap: -2.06% / slope_proxy: -0.133604
- RS vs GDXJ gap: -3.58% / slope_proxy: -0.034385
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

- 실행시간(UTC): **2026-08-13 23:22:24**
- 데이터 기준일(주가): **2026-08-13**

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

- HY OAS: 2.71 / 4주 변화 0.00 bp-ish / 2026-08-12
- IG OAS: 0.79 / 4주 변화 0.00 bp-ish / 2026-08-12
- 10Y Real Yield: 2.42 / 4주 변화 0.10 bp-ish / 2026-08-12
- VIX: 14.55 / 4주 변화 -1.12 / 2026-08-12
- NFCI: -0.55 / 4주 변화 -0.09 / 2026-08-07

### Leadership ratios

- GDX/GLD: gap 7.14% / slope_proxy 14.29%
- GDXJ/GLD: gap 7.81% / slope_proxy 16.07%
- SILJ/SLV: gap 8.72% / slope_proxy 8.05%
- Gold breadth proxy: above50 100.00%, above200 61.54%, count 13
- Silver breadth proxy: above50 100.00%, above200 46.15%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.75 | RSI14: 83.21 | ATR14%: 5.35%
- MA20/50/200 gap: 22.66% / 24.69% / 39.62%
- 5D return: 12.59% | 20D drawdown: -2.40% | vol_ratio: 1.12
- RS vs GDXJ: gap 12.26% / slope_proxy 12.29%
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
- close: 7.00 | RSI14: 96.80 | ATR14%: 4.83%
- MA20/50/200 gap: 22.12% / 23.03% / 1.99%
- 5D return: 11.64% | 20D drawdown: 0.00% | vol_ratio: 0.76
- RS vs GDXJ: gap 9.97% / slope_proxy 15.94%
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
- close: 1.43 | RSI14: 88.00 | ATR14%: 5.24%
- MA20/50/200 gap: 17.17% / 15.23% / -3.41%
- 5D return: 5.15% | 20D drawdown: -1.38% | vol_ratio: 0.73
- RS vs GDXJ: gap 3.50% / slope_proxy 7.02%
- FundamentalScore: 70 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **55.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.11 | RSI14: 59.57 | ATR14%: 5.28%
- MA20/50/200 gap: 9.04% / 17.82% / 15.02%
- 5D return: 9.33% | 20D drawdown: -3.21% | vol_ratio: 0.59
- RS vs GDXJ: gap 3.28% / slope_proxy -7.31%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **53.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.94 | RSI14: 75.82 | ATR14%: 5.70%
- MA20/50/200 gap: 20.33% / 32.37% / 59.00%
- 5D return: 6.90% | 20D drawdown: -3.92% | vol_ratio: 1.35
- RS vs SILJ: gap 22.26% / slope_proxy 16.11%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.31 | RSI14: 77.01 | ATR14%: 5.35%
- MA20/50/200 gap: 20.68% / 22.99% / 7.44%
- 5D return: 16.76% | 20D drawdown: -2.83% | vol_ratio: 0.87
- RS vs SILJ: gap 10.02% / slope_proxy 12.43%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.72 | RSI14: 80.00 | ATR14%: 6.13%
- MA20/50/200 gap: 21.89% / 25.26% / 2.53%
- 5D return: 9.41% | 20D drawdown: -3.75% | vol_ratio: 0.75
- RS vs SILJ: gap 12.04% / slope_proxy 17.08%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.91 | RSI14: 67.49 | ATR14%: 5.67%
- MA20/50/200 gap: 13.33% / 12.40% / 3.09%
- 5D return: 8.31% | 20D drawdown: -6.37% | vol_ratio: 1.20
- RS vs SILJ: gap 0.67% / slope_proxy 1.52%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **64.8**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.74 | RSI14: 69.23 | ATR14%: 4.91%
- MA20/50/200 gap: 10.06% / 9.94% / -8.60%
- 5D return: 5.95% | 20D drawdown: -3.61% | vol_ratio: 0.64
- RS vs SILJ: gap 0.34% / slope_proxy -0.35%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.73 | RSI14: 65.44 | ATR14%: 5.16%
- MA20/50/200 gap: 13.21% / 13.79% / -3.87%
- 5D return: 11.79% | 20D drawdown: -2.04% | vol_ratio: 0.72
- RS vs SILJ: gap 1.97% / slope_proxy -0.02%
- FundamentalScore: 78 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **50.1**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.05 | RSI14: 70.00 | ATR14%: 5.98%
- MA20/50/200 gap: 16.45% / 8.70% / -12.13%
- 5D return: 8.14% | 20D drawdown: -2.70% | vol_ratio: 0.93
- RS vs SILJ: gap -4.61% / slope_proxy 7.96%
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
- close: 26.57 | RSI14: 73.96 | ATR14%: 6.72%
- MA20/50/200 gap: 18.91% / 13.87% / -6.93%
- 5D return: 11.64% | 20D drawdown: -3.49% | vol_ratio: 0.72
- RS vs SILJ: gap -2.06% / slope_proxy 12.71%
- FundamentalScore: 42 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **33.9**
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
