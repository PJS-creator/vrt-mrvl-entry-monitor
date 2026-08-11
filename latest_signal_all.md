# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-11 15:01:12**
- 데이터 기준일(일봉): **2026-08-11**
- 데이터 기준일(주봉): **2026-08-10**
- VXN 기준일: **2026-08-10** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 722.09
- Weekly RSI14: **60.69**
- 52W MA: 637.21 / gap: **13.32%**
- 104W MA gap: **26.45%**
- 52W MA 13W slope: **7.14%**
- VXN: **23.04** / 5D change: -1.73

## Daily trigger: 실제 매수 타이밍

- QQQ close: 722.07
- Daily RSI14: **56.65**
- 20D gap: **3.02%**
- 50D gap: **1.17%**
- 200D gap: **11.46%**
- MACD hist: 4.4726 / change: -0.0618
- ATR14%: **1.87%**
- 20D high drawdown: **-0.25%**

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

- 데이터 기준일(주가): **2026-08-11**
- 실행시간(UTC): **2026-08-11 15:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.4 / 4주 변화 8.0 bp
- VIX (VIXCLS): 15.46
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.78096
- MA60: 9.362312
- gap: -6.21%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.366227
- MA60: 0.391624
- gap: -6.49%
- MA60_slope_proxy: 0.012617
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-11**
- 실행시간(UTC): **2026-08-11 15:00:47**

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
- TERM_SPREAD_10Y_POLICY: 116.18 bp / 4주 변화 4.37 bp
- CURVE_10s5s: 47.62 bp / 4주 변화 -0.51 bp

## NWG Price
- close: 708.8
- MA50: 659.82 / gap50: 7.42%
- MA200: 619.4083 / gap200: 14.43%

## Relative Strength
- RS vs FTSE gap: 6.38% / slope_proxy: 0.002769
- RS vs Peers gap: 4.19% / slope_proxy: 0.008593

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-11 15:00:54**

## Commodity Regime

- WTI ref (CL=F): 82.38 / 5D 8.72%
- Brent ref (BZ=F): 88.07 / 5D 10.98%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.69
- Gas ref (NG=F): 2.76 / 5D 2.98%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.23
- MA20 / MA60 / MA200: 55.92 / 55.13 / 50.44
- gap20 / gap60: 5.91% / 7.44%
- 5D return: 7.51%
- 20D high/low: 59.23 / 53.65

### Relative Strength

- ratio: 0.976024
- ratio_MA60: 0.967855
- ratio_gap: 0.84%
- ratio_slope_proxy(20d): -0.013300

### Volume (if available)

- volume: 1886940.00
- volume_MA20: 8201242.00
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

- close: 18.12
- MA20 / MA60 / MA200: 18.45 / 18.03 / 16.34
- gap20 / gap60: -1.75% / 0.52%
- 5D return: -3.18%
- 20D high/low: 19.40 / 17.47

### Relative Strength

- ratio: 0.523995
- ratio_MA60: 0.512222
- ratio_gap: 2.30%
- ratio_slope_proxy(20d): -0.005824

### Volume (if available)

- volume: 3642514.00
- volume_MA20: 14063670.70
- volume_ratio: 0.26

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.82
- MA20 / MA60 / MA200: 5.24 / 5.64 / 5.39
- gap20 / gap60: 11.00% / 3.13%
- 5D return: 11.40%
- 20D high/low: 5.82 / 4.95

### Relative Strength

- ratio: 0.014046
- ratio_MA60: 0.014075
- ratio_gap: -0.21%
- ratio_slope_proxy(20d): -0.000447

### Volume (if available)

- volume: 11768377.00
- volume_MA20: 41035198.85
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.28
- MA20 / MA60 / MA200: 13.47 / 12.69 / 10.84
- gap20 / gap60: -1.41% / 4.61%
- 5D return: 3.43%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.049925
- ratio_MA60: 0.051346
- ratio_gap: -2.77%
- ratio_slope_proxy(20d): 0.001002

### Volume (if available)

- volume: 8033590.00
- volume_MA20: 14853929.50
- volume_ratio: 0.54

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

- 데이터 기준일(주가): **2026-08-11**
- 실행시간(UTC): **2026-08-11 15:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.7
- IG OAS 4주 변화: 0.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.4
- VIX: 15.46
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 9.89% / slope_proxy: 0.01281
- GDXJ/GLD gap: 9.49% / slope_proxy: -0.006034

## VZLA (Vizsla Silver)
- close: 3.825 | RSI14: 64.458153 | ATR14%: 4.93%
- MA20 gap: 14.22% | MA50 gap: 13.10% | MA200 gap: -6.41%
- vol_ratio(Volume/Vol20): 0.197089 | gap_open: 0.77%
- RS vs SILJ gap: 0.79% / slope_proxy: 0.005999
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
- close: 9.025 | RSI14: 74.456174 | ATR14%: 5.62%
- MA20 gap: 30.07% | MA50 gap: 31.26% | MA200 gap: 6.38%
- vol_ratio(Volume/Vol20): 0.242724 | gap_open: 0.22%
- SilverMarginGate: SI=65.209999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.52% / slope_proxy: -0.003705
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
- close: 27.25 | RSI14: 65.288255 | ATR14%: 6.60%
- MA20 gap: 26.19% | MA50 gap: 15.56% | MA200 gap: -3.88%
- vol_ratio(Volume/Vol20): 0.191154 | gap_open: 0.29%
- RS vs SILJ gap: -2.20% / slope_proxy: -0.142276
- RS vs GDXJ gap: -4.51% / slope_proxy: -0.036051
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

- 실행시간(UTC): **2026-08-11 15:01:11**
- 데이터 기준일(주가): **2026-08-11**

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

- HY OAS: 2.70 / 4주 변화 0.01 bp-ish / 2026-08-10
- IG OAS: 0.78 / 4주 변화 0.00 bp-ish / 2026-08-10
- 10Y Real Yield: 2.40 / 4주 변화 0.08 bp-ish / 2026-08-07
- VIX: 15.46 / 4주 변화 -1.70 / 2026-08-10
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 8.76% / slope_proxy 12.74%
- GDXJ/GLD: gap 9.49% / slope_proxy 13.54%
- SILJ/SLV: gap 9.89% / slope_proxy 5.82%
- Gold breadth proxy: above50 100.00%, above200 61.54%, count 13
- Silver breadth proxy: above50 100.00%, above200 53.85%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.69 | RSI14: 81.72 | ATR14%: 4.86%
- MA20/50/200 gap: 26.51% / 26.18% / 39.08%
- 5D return: 29.48% | 20D drawdown: 0.00% | vol_ratio: 0.30
- RS vs GDXJ: gap 9.13% / slope_proxy 8.75%
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
- close: 7.02 | RSI14: 85.54 | ATR14%: 4.90%
- MA20/50/200 gap: 25.46% / 25.47% / 2.58%
- 5D return: 20.62% | 20D drawdown: 0.00% | vol_ratio: 0.33
- RS vs GDXJ: gap 7.92% / slope_proxy 17.00%
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
- close: 1.46 | RSI14: 80.70 | ATR14%: 5.11%
- MA20/50/200 gap: 22.64% / 19.36% / -1.06%
- 5D return: 16.80% | 20D drawdown: 0.00% | vol_ratio: 0.27
- RS vs GDXJ: gap 3.38% / slope_proxy 9.94%
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
- close: 2.15 | RSI14: 63.81 | ATR14%: 5.51%
- MA20/50/200 gap: 12.21% / 20.54% / 17.66%
- 5D return: 20.11% | 20D drawdown: -1.38% | vol_ratio: 0.21
- RS vs GDXJ: gap 2.74% / slope_proxy -9.60%
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
- close: 27.89 | RSI14: 75.17 | ATR14%: 5.54%
- MA20/50/200 gap: 29.29% / 38.76% / 66.23%
- 5D return: 21.77% | 20D drawdown: -0.13% | vol_ratio: 0.25
- RS vs SILJ: gap 26.07% / slope_proxy 18.39%
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
- close: 10.43 | RSI14: 72.47 | ATR14%: 5.15%
- MA20/50/200 gap: 26.25% / 24.86% / 8.97%
- 5D return: 25.21% | 20D drawdown: 0.00% | vol_ratio: 0.25
- RS vs SILJ: gap 9.80% / slope_proxy 9.87%
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
- close: 9.02 | RSI14: 77.32 | ATR14%: 5.82%
- MA20/50/200 gap: 30.07% / 31.26% / 6.38%
- 5D return: 25.35% | 20D drawdown: 0.00% | vol_ratio: 0.24
- RS vs SILJ: gap 14.52% / slope_proxy 19.17%
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
- close: 7.35 | RSI14: 64.38 | ATR14%: 5.39%
- MA20/50/200 gap: 23.22% / 19.31% / 9.99%
- 5D return: 24.37% | 20D drawdown: 0.00% | vol_ratio: 0.28
- RS vs SILJ: gap 5.31% / slope_proxy 3.93%
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
- close: 3.83 | RSI14: 62.70 | ATR14%: 4.82%
- MA20/50/200 gap: 14.22% / 13.10% / -6.41%
- 5D return: 12.50% | 20D drawdown: -1.42% | vol_ratio: 0.20
- RS vs SILJ: gap 0.79% / slope_proxy 0.22%
- FundamentalScore: 72 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **56.1**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.58 | RSI14: 61.76 | ATR14%: 5.08%
- MA20/50/200 gap: 14.49% / 12.95% / -4.39%
- 5D return: 14.26% | 20D drawdown: 0.00% | vol_ratio: 0.12
- RS vs SILJ: gap -0.43% / slope_proxy -4.63%
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
- close: 5.11 | RSI14: 66.91 | ATR14%: 5.90%
- MA20/50/200 gap: 21.22% / 8.75% / -11.01%
- 5D return: 16.29% | 20D drawdown: -0.49% | vol_ratio: 0.29
- RS vs SILJ: gap -5.68% / slope_proxy 6.21%
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
- close: 27.25 | RSI14: 70.45 | ATR14%: 6.24%
- MA20/50/200 gap: 26.19% / 15.56% / -3.88%
- 5D return: 21.87% | 20D drawdown: -0.15% | vol_ratio: 0.19
- RS vs SILJ: gap -2.20% / slope_proxy 9.38%
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
