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

- 실행시간(UTC): **2026-08-14 15:01:28**
- 데이터 기준일(일봉): **2026-08-14**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-13** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 730.76
- Weekly RSI14: **62.26**
- 52W MA: 637.37 / gap: **14.65%**
- 104W MA gap: **27.95%**
- 52W MA 13W slope: **7.17%**
- VXN: **21.23** / 5D change: -2.72

## Daily trigger: 실제 매수 타이밍

- QQQ close: 730.76
- Daily RSI14: **59.43**
- 20D gap: **3.78%**
- 50D gap: **2.52%**
- 200D gap: **12.51%**
- MACD hist: 4.3440 / change: -0.1370
- ATR14%: **1.71%**
- 20D high drawdown: **-0.18%**

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

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-14 15:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 10.0 bp
- VIX (VIXCLS): 14.63
- NFCI: -0.549

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.991324
- MA60: 9.352567
- gap: -3.86%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.375913
- MA60: 0.394582
- gap: -4.73%
- MA60_slope_proxy: 0.014339
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-14 15:01:06**

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
- TERM_SPREAD_10Y_POLICY: 120.93 bp / 4주 변화 1.94 bp
- CURVE_10s5s: 47.78 bp / 4주 변화 0.58 bp

## NWG Price
- close: 707.0
- MA50: 666.5248 / gap50: 6.07%
- MA200: 621.1836 / gap200: 13.81%

## Relative Strength
- RS vs FTSE gap: 7.12% / slope_proxy: 0.00284
- RS vs Peers gap: 3.23% / slope_proxy: 0.012334

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-14 15:01:13**

## Commodity Regime

- WTI ref (CL=F): 81.53 / 5D 4.29%
- Brent ref (BZ=F): 87.84 / 5D 5.13%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.31
- Gas ref (NG=F): 2.77 / 5D 4.02%

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

- close: 58.61
- MA20 / MA60 / MA200: 56.54 / 55.06 / 50.69
- gap20 / gap60: 3.65% / 6.46%
- 5D return: 4.83%
- 20D high/low: 59.06 / 53.81

### Relative Strength

- ratio: 0.947306
- ratio_MA60: 0.965494
- ratio_gap: -1.88%
- ratio_slope_proxy(20d): -0.013341

### Volume (if available)

- volume: 1859990.00
- volume_MA20: 8234379.50
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.01
- MA20 / MA60 / MA200: 18.46 / 17.91 / 16.44
- gap20 / gap60: -2.41% / 0.55%
- 5D return: 0.28%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.534533
- ratio_MA60: 0.510676
- ratio_gap: 4.67%
- ratio_slope_proxy(20d): -0.007211

### Volume (if available)

- volume: 2865280.00
- volume_MA20: 14367319.00
- volume_ratio: 0.20

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

- close: 5.89
- MA20 / MA60 / MA200: 5.33 / 5.56 / 5.42
- gap20 / gap60: 10.57% / 6.04%
- 5D return: 12.07%
- 20D high/low: 5.89 / 4.95

### Relative Strength

- ratio: 0.013989
- ratio_MA60: 0.013950
- ratio_gap: 0.29%
- ratio_slope_proxy(20d): -0.000512

### Volume (if available)

- volume: 11902569.00
- volume_MA20: 44289328.45
- volume_ratio: 0.27

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 14.07
- MA20 / MA60 / MA200: 13.56 / 12.66 / 10.90
- gap20 / gap60: 3.72% / 11.10%
- 5D return: 6.11%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.052065
- ratio_MA60: 0.051081
- ratio_gap: 1.93%
- ratio_slope_proxy(20d): 0.000600

### Volume (if available)

- volume: 4025114.00
- volume_MA20: 15307415.70
- volume_ratio: 0.26

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

- 데이터 기준일(주가): **2026-08-14**
- 실행시간(UTC): **2026-08-14 15:01:18**

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
- IG OAS 4주 변화: 1.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.42
- VIX: 14.63
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 9.34% / slope_proxy: 0.015749
- GDXJ/GLD gap: 9.47% / slope_proxy: -0.003079

## VZLA (Vizsla Silver)
- close: 3.85 | RSI14: 64.730863 | ATR14%: 4.75%
- MA20 gap: 12.23% | MA50 gap: 13.31% | MA200 gap: -5.88%
- vol_ratio(Volume/Vol20): 0.258738 | gap_open: 0.80%
- RS vs SILJ gap: 0.80% / slope_proxy: 0.005675
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
- close: 8.96 | RSI14: 71.040182 | ATR14%: 5.63%
- MA20 gap: 23.00% | MA50 gap: 28.40% | MA200 gap: 5.17%
- vol_ratio(Volume/Vol20): 0.277779 | gap_open: 1.49%
- SilverMarginGate: SI=65.400002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.46% / slope_proxy: -0.002013
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
- close: 27.620001 | RSI14: 64.379044 | ATR14%: 6.59%
- MA20 gap: 21.29% | MA50 gap: 18.83% | MA200 gap: -3.60%
- vol_ratio(Volume/Vol20): 0.1932 | gap_open: 3.42%
- RS vs SILJ gap: -0.01% / slope_proxy: -0.1298
- RS vs GDXJ gap: -1.76% / slope_proxy: -0.033605
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

- 실행시간(UTC): **2026-08-14 15:01:26**
- 데이터 기준일(주가): **2026-08-14**

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

- HY OAS: 2.71 / 4주 변화 0.00 bp-ish / 2026-08-13
- IG OAS: 0.79 / 4주 변화 0.01 bp-ish / 2026-08-13
- 10Y Real Yield: 2.42 / 4주 변화 0.10 bp-ish / 2026-08-12
- VIX: 14.63 / 4주 변화 -2.10 / 2026-08-13
- NFCI: -0.55 / 4주 변화 -0.09 / 2026-08-07

### Leadership ratios

- GDX/GLD: gap 8.49% / slope_proxy 16.61%
- GDXJ/GLD: gap 9.47% / slope_proxy 18.49%
- SILJ/SLV: gap 9.34% / slope_proxy 9.72%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 100.00%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.14 | RSI14: 85.92 | ATR14%: 5.49%
- MA20/50/200 gap: 25.39% / 29.20% / 44.72%
- 5D return: 6.29% | 20D drawdown: 0.00% | vol_ratio: 0.36
- RS vs GDXJ: gap 13.32% / slope_proxy 13.81%
- FundamentalScore: 88 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **72.1**
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
- close: 7.14 | RSI14: 96.60 | ATR14%: 4.41%
- MA20/50/200 gap: 22.25% / 25.42% / 3.96%
- 5D return: 6.41% | 20D drawdown: 0.00% | vol_ratio: 0.38
- RS vs GDXJ: gap 9.28% / slope_proxy 18.95%
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
- close: 1.49 | RSI14: 84.48 | ATR14%: 5.03%
- MA20/50/200 gap: 19.58% / 21.28% / 0.92%
- 5D return: 2.76% | 20D drawdown: 0.00% | vol_ratio: 0.32
- RS vs GDXJ: gap 5.28% / slope_proxy 9.08%
- FundamentalScore: 70 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **64.0**
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
- close: 2.35 | RSI14: 67.80 | ATR14%: 5.65%
- MA20/50/200 gap: 20.02% / 30.53% / 28.31%
- 5D return: 10.85% | 20D drawdown: 0.00% | vol_ratio: 1.89
- RS vs GDXJ: gap 12.57% / slope_proxy -1.23%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **53.8**
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.13 | RSI14: 73.91 | ATR14%: 6.08%
- MA20/50/200 gap: 15.18% / 27.31% / 54.33%
- 5D return: -3.89% | 20D drawdown: -6.81% | vol_ratio: 0.96
- RS vs SILJ: gap 16.15% / slope_proxy 10.22%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.72 | RSI14: 78.37 | ATR14%: 5.23%
- MA20/50/200 gap: 23.10% / 27.41% / 11.55%
- 5D return: 12.37% | 20D drawdown: 0.00% | vol_ratio: 0.30
- RS vs SILJ: gap 11.60% / slope_proxy 12.61%
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
- close: 18.56 | RSI14: 68.36 | ATR14%: 5.10%
- MA20/50/200 gap: 16.91% / 18.80% / 0.44%
- 5D return: 10.12% | 20D drawdown: 0.00% | vol_ratio: 0.13
- RS vs SILJ: gap 4.20% / slope_proxy 2.30%
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
- close: 8.96 | RSI14: 81.03 | ATR14%: 6.05%
- MA20/50/200 gap: 23.00% / 28.40% / 5.17%
- 5D return: 6.67% | 20D drawdown: -1.10% | vol_ratio: 0.28
- RS vs SILJ: gap 12.46% / slope_proxy 18.49%
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
- close: 7.16 | RSI14: 69.05 | ATR14%: 5.52%
- MA20/50/200 gap: 15.78% / 16.26% / 6.55%
- 5D return: 4.00% | 20D drawdown: -3.05% | vol_ratio: 0.39
- RS vs SILJ: gap 1.83% / slope_proxy 1.20%
- FundamentalScore: 60 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **59.5**
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
- close: 3.86 | RSI14: 67.43 | ATR14%: 4.74%
- MA20/50/200 gap: 11.68% / 14.42% / -5.59%
- 5D return: 3.07% | 20D drawdown: -0.64% | vol_ratio: 0.26
- RS vs SILJ: gap 0.51% / slope_proxy -3.58%
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
- close: 5.22 | RSI14: 70.76 | ATR14%: 5.82%
- MA20/50/200 gap: 18.41% / 12.67% / -9.27%
- 5D return: 4.19% | 20D drawdown: 0.00% | vol_ratio: 0.37
- RS vs SILJ: gap -3.38% / slope_proxy 9.38%
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
- close: 27.62 | RSI14: 75.51 | ATR14%: 6.55%
- MA20/50/200 gap: 21.29% / 18.83% / -3.60%
- 5D return: 4.07% | 20D drawdown: 0.00% | vol_ratio: 0.19
- RS vs SILJ: gap -0.01% / slope_proxy 15.99%
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
