# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-12 23:21:10**
- 데이터 기준일(일봉): **2026-08-12**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-11** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 723.70
- Weekly RSI14: **61.06**
- 52W MA: 637.24 / gap: **13.57%**
- 104W MA gap: **26.73%**
- 52W MA 13W slope: **7.15%**
- VXN: **22.38** / 5D change: -3.10

## Daily trigger: 실제 매수 타이밍

- QQQ close: 723.70
- Daily RSI14: **57.09**
- 20D gap: **3.23%**
- 50D gap: **1.46%**
- 200D gap: **11.61%**
- MACD hist: 4.1898 / change: -0.0520
- ATR14%: **1.85%**
- 20D high drawdown: **-0.02%**

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

- 데이터 기준일(주가): **2026-08-12**
- 실행시간(UTC): **2026-08-12 23:20:41**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 0.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.43 / 4주 변화 10.0 bp
- VIX (VIXCLS): 15.28
- NFCI: -0.549

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.975962
- MA60: 9.365562
- gap: -4.16%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.371185
- MA60: 0.392585
- gap: -5.45%
- MA60_slope_proxy: 0.012773
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-11**
- 실행시간(UTC): **2026-08-12 23:20:44**

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
- TERM_SPREAD_10Y_POLICY: 122.18 bp / 4주 변화 2.15 bp
- CURVE_10s5s: 47.39 bp / 4주 변화 0.74 bp

## NWG Price
- close: 707.4
- MA50: 659.792 / gap50: 7.22%
- MA200: 619.4013 / gap200: 14.21%

## Relative Strength
- RS vs FTSE gap: 6.34% / slope_proxy: 0.002768
- RS vs Peers gap: 4.12% / slope_proxy: 0.008582

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-12 23:20:51**

## Commodity Regime

- WTI ref (CL=F): 82.71 / 5D 9.96%
- Brent ref (BZ=F): 88.50 / 5D 11.39%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.79
- Gas ref (NG=F): 2.79 / 5D 3.91%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 58.55
- MA20 / MA60 / MA200: 56.15 / 55.11 / 50.52
- gap20 / gap60: 4.27% / 6.23%
- 5D return: 8.81%
- 20D high/low: 59.06 / 53.65

### Relative Strength

- ratio: 0.959364
- ratio_MA60: 0.966972
- ratio_gap: -0.79%
- ratio_slope_proxy(20d): -0.013708

### Volume (if available)

- volume: 6447617.00
- volume_MA20: 8376045.85
- volume_ratio: 0.77

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.76
- MA20 / MA60 / MA200: 18.43 / 17.99 / 16.37
- gap20 / gap60: -3.65% / -1.30%
- 5D return: -3.27%
- 20D high/low: 19.40 / 17.47

### Relative Strength

- ratio: 0.524513
- ratio_MA60: 0.511840
- ratio_gap: 2.48%
- ratio_slope_proxy(20d): -0.006255

### Volume (if available)

- volume: 13862842.00
- volume_MA20: 14937467.10
- volume_ratio: 0.93

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.70
- MA20 / MA60 / MA200: 5.26 / 5.62 / 5.40
- gap20 / gap60: 8.29% / 1.49%
- 5D return: 10.89%
- 20D high/low: 5.81 / 4.95

### Relative Strength

- ratio: 0.013793
- ratio_MA60: 0.014038
- ratio_gap: -1.74%
- ratio_slope_proxy(20d): -0.000465

### Volume (if available)

- volume: 45087543.00
- volume_MA20: 44019192.15
- volume_ratio: 1.02

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.72
- MA20 / MA60 / MA200: 13.51 / 12.69 / 10.86
- gap20 / gap60: 1.57% / 8.15%
- 5D return: 10.38%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.051173
- ratio_MA60: 0.051215
- ratio_gap: -0.08%
- ratio_slope_proxy(20d): 0.000792

### Volume (if available)

- volume: 18774869.00
- volume_MA20: 15928873.45
- volume_ratio: 1.18

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

- 데이터 기준일(주가): **2026-08-12**
- 실행시간(UTC): **2026-08-12 23:21:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 0.0 bp / latest 2.72
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.43
- VIX: 15.28
- NFCI: -0.549

### Leadership ratios
- SILJ/SLV gap: 10.01% / slope_proxy: 0.013568
- GDXJ/GLD gap: 9.62% / slope_proxy: -0.005087

## VZLA (Vizsla Silver)
- close: 3.8 | RSI14: 63.354092 | ATR14%: 4.96%
- MA20 gap: 12.46% | MA50 gap: 12.52% | MA200 gap: -6.99%
- vol_ratio(Volume/Vol20): 0.613145 | gap_open: 2.61%
- RS vs SILJ gap: -0.74% / slope_proxy: 0.005809
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
- close: 8.87 | RSI14: 72.159234 | ATR14%: 5.86%
- MA20 gap: 27.98% | MA50 gap: 29.07% | MA200 gap: 4.57%
- vol_ratio(Volume/Vol20): 0.820273 | gap_open: 4.67%
- SilverMarginGate: SI=65.360001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.77% / slope_proxy: -0.003828
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
- close: 27.450001 | RSI14: 65.641857 | ATR14%: 6.84%
- MA20 gap: 25.13% | MA50 gap: 16.92% | MA200 gap: -3.52%
- vol_ratio(Volume/Vol20): 1.211516 | gap_open: 7.77%
- RS vs SILJ gap: -1.72% / slope_proxy: -0.13854
- RS vs GDXJ gap: -3.88% / slope_proxy: -0.035433
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

- 실행시간(UTC): **2026-08-12 23:21:08**
- 데이터 기준일(주가): **2026-08-12**

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

- HY OAS: 2.72 / 4주 변화 0.00 bp-ish / 2026-08-11
- IG OAS: 0.79 / 4주 변화 0.00 bp-ish / 2026-08-11
- 10Y Real Yield: 2.43 / 4주 변화 0.10 bp-ish / 2026-08-11
- VIX: 15.28 / 4주 변화 -1.22 / 2026-08-11
- NFCI: -0.55 / 4주 변화 -0.09 / 2026-08-07

### Leadership ratios

- GDX/GLD: gap 8.90% / slope_proxy 14.82%
- GDXJ/GLD: gap 9.62% / slope_proxy 16.24%
- SILJ/SLV: gap 10.01% / slope_proxy 8.03%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 100.00%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.99 | RSI14: 86.26 | ATR14%: 5.06%
- MA20/50/200 gap: 28.02% / 29.58% / 42.98%
- 5D return: 21.83% | 20D drawdown: 0.00% | vol_ratio: 1.89
- RS vs GDXJ: gap 11.51% / slope_proxy 11.61%
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
- close: 6.93 | RSI14: 84.00 | ATR14%: 4.93%
- MA20/50/200 gap: 21.80% / 23.95% / 1.21%
- 5D return: 11.06% | 20D drawdown: -0.14% | vol_ratio: 0.57
- RS vs GDXJ: gap 5.84% / slope_proxy 12.89%
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
- close: 1.45 | RSI14: 80.36 | ATR14%: 5.34%
- MA20/50/200 gap: 21.85% / 18.56% / -1.73%
- 5D return: 16.00% | 20D drawdown: 0.00% | vol_ratio: 1.21
- RS vs GDXJ: gap 2.06% / slope_proxy 8.52%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **60.5**
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
- close: 2.17 | RSI14: 57.73 | ATR14%: 5.27%
- MA20/50/200 gap: 12.76% / 21.36% / 18.51%
- 5D return: 11.86% | 20D drawdown: -0.46% | vol_ratio: 0.75
- RS vs GDXJ: gap 2.90% / slope_proxy -7.72%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 28.04 | RSI14: 80.78 | ATR14%: 5.38%
- MA20/50/200 gap: 27.57% / 38.52% / 66.29%
- 5D return: 11.85% | 20D drawdown: 0.00% | vol_ratio: 0.77
- RS vs SILJ: gap 25.02% / slope_proxy 18.11%
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
- close: 10.61 | RSI14: 80.68 | ATR14%: 5.08%
- MA20/50/200 gap: 26.28% / 26.71% / 10.70%
- 5D return: 18.42% | 20D drawdown: 0.00% | vol_ratio: 0.84
- RS vs SILJ: gap 10.68% / slope_proxy 11.88%
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
- close: 8.87 | RSI14: 75.06 | ATR14%: 6.07%
- MA20/50/200 gap: 27.98% / 29.07% / 4.57%
- 5D return: 23.19% | 20D drawdown: -1.22% | vol_ratio: 0.82
- RS vs SILJ: gap 11.77% / slope_proxy 16.25%
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
- close: 7.14 | RSI14: 70.77 | ATR14%: 5.41%
- MA20/50/200 gap: 18.47% / 15.95% / 6.68%
- 5D return: 10.19% | 20D drawdown: -3.25% | vol_ratio: 2.09
- RS vs SILJ: gap 1.54% / slope_proxy 2.34%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 18.10 | RSI14: 66.95 | ATR14%: 4.98%
- MA20/50/200 gap: 16.77% / 16.15% / -1.73%
- 5D return: 9.43% | 20D drawdown: 0.00% | vol_ratio: 1.09
- RS vs SILJ: gap 1.67% / slope_proxy -1.55%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **55.4**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.80 | RSI14: 69.44 | ATR14%: 4.81%
- MA20/50/200 gap: 12.46% / 12.52% / -6.99%
- 5D return: 5.85% | 20D drawdown: -2.06% | vol_ratio: 0.61
- RS vs SILJ: gap -0.74% / slope_proxy -2.24%
- FundamentalScore: 72 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **47.4**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.19 | RSI14: 71.32 | ATR14%: 5.79%
- MA20/50/200 gap: 21.52% / 11.05% / -9.61%
- 5D return: 7.90% | 20D drawdown: 0.00% | vol_ratio: 0.88
- RS vs SILJ: gap -4.52% / slope_proxy 9.60%
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
- close: 27.45 | RSI14: 77.59 | ATR14%: 6.44%
- MA20/50/200 gap: 25.13% / 16.92% / -3.52%
- 5D return: 12.13% | 20D drawdown: -0.29% | vol_ratio: 1.21
- RS vs SILJ: gap -1.72% / slope_proxy 17.60%
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
