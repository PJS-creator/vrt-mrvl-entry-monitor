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

- 실행시간(UTC): **2026-08-19 15:01:28**
- 데이터 기준일(일봉): **2026-08-19**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-18** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 718.52
- Weekly RSI14: **58.85**
- 52W MA: 640.25 / gap: **12.22%**
- 104W MA gap: **25.30%**
- 52W MA 13W slope: **6.93%**
- VXN: **22.56** / 5D change: 0.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 718.52
- Daily RSI14: **52.67**
- 20D gap: **1.64%**
- 50D gap: **0.79%**
- 200D gap: **10.39%**
- MACD hist: 1.8179 / change: -0.8948
- ATR14%: **1.67%**
- 20D high drawdown: **-1.85%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
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

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.82 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.44 / 4주 변화 9.0 bp
- VIX (VIXCLS): 15.84
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.364357
- MA60: 9.273233
- gap: -9.80%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.415183
- MA60: 0.397641
- gap: 4.41%
- MA60_slope_proxy: 0.016287
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 15:00:53**

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
- TERM_SPREAD_10Y_POLICY: 129.27 bp / 4주 변화 2.32 bp
- CURVE_10s5s: 48.77 bp / 4주 변화 1.39 bp

## NWG Price
- close: 684.9804
- MA50: 672.7224 / gap50: 1.82%
- MA200: 622.8415 / gap200: 9.98%

## Relative Strength
- RS vs FTSE gap: 2.28% / slope_proxy: 0.002995
- RS vs Peers gap: 1.88% / slope_proxy: 0.014967

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-19 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 85.08 / 5D 2.17%
- Brent ref (BZ=F): 91.96 / 5D 3.35%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.88
- Gas ref (NG=F): 2.83 / 5D 1.07%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.49
- MA20 / MA60 / MA200: 57.04 / 55.11 / 50.98
- gap20 / gap60: 6.05% / 9.76%
- 5D return: 3.31%
- 20D high/low: 60.49 / 53.81

### Relative Strength

- ratio: 0.944861
- ratio_MA60: 0.962946
- ratio_gap: -1.88%
- ratio_slope_proxy(20d): -0.013447

### Volume (if available)

- volume: 2350289.00
- volume_MA20: 8170629.45
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.83
- MA20 / MA60 / MA200: 18.43 / 17.84 / 16.54
- gap20 / gap60: 2.19% / 5.56%
- 5D return: 6.05%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.543343
- ratio_MA60: 0.510369
- ratio_gap: 6.46%
- ratio_slope_proxy(20d): -0.007141

### Volume (if available)

- volume: 5131785.00
- volume_MA20: 14629059.25
- volume_ratio: 0.35

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.91
- MA20 / MA60 / MA200: 5.43 / 5.50 / 5.45
- gap20 / gap60: 8.82% / 7.35%
- 5D return: 3.60%
- 20D high/low: 5.91 / 4.95

### Relative Strength

- ratio: 0.014065
- ratio_MA60: 0.013857
- ratio_gap: 1.50%
- ratio_slope_proxy(20d): -0.000572

### Volume (if available)

- volume: 12853479.00
- volume_MA20: 45420558.95
- volume_ratio: 0.28

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.90
- MA20 / MA60 / MA200: 13.50 / 12.67 / 10.98
- gap20 / gap60: 3.04% / 9.74%
- 5D return: 1.35%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.050817
- ratio_MA60: 0.050678
- ratio_gap: 0.27%
- ratio_slope_proxy(20d): -0.000201

### Volume (if available)

- volume: 4033335.00
- volume_MA20: 14240951.75
- volume_ratio: 0.28

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

- 데이터 기준일(주가): **2026-08-19**
- 실행시간(UTC): **2026-08-19 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.75
- IG OAS 4주 변화: 4.0 bp / latest 0.82
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.44
- VIX: 15.84
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 11.69% / slope_proxy: 0.018879
- GDXJ/GLD gap: 12.58% / slope_proxy: -0.000346

## VZLA (Vizsla Silver)
- close: 3.855 | RSI14: 61.720522 | ATR14%: 4.87%
- MA20 gap: 9.90% | MA50 gap: 14.19% | MA200 gap: -5.42%
- vol_ratio(Volume/Vol20): 0.416644 | gap_open: 4.48%
- RS vs SILJ gap: -3.26% / slope_proxy: 0.004667
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
- close: 9.4201 | RSI14: 70.475326 | ATR14%: 5.71%
- MA20 gap: 24.04% | MA50 gap: 34.64% | MA200 gap: 10.04%
- vol_ratio(Volume/Vol20): 0.961431 | gap_open: 4.78%
- SilverMarginGate: SI=65.599998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 14.37% / slope_proxy: -0.000882
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
- close: 27.24 | RSI14: 59.735773 | ATR14%: 7.01%
- MA20 gap: 15.55% | MA50 gap: 17.80% | MA200 gap: -5.81%
- vol_ratio(Volume/Vol20): 0.703703 | gap_open: 8.06%
- RS vs SILJ gap: -3.38% / slope_proxy: -0.122168
- RS vs GDXJ gap: -6.78% / slope_proxy: -0.032582
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

- 실행시간(UTC): **2026-08-19 15:01:25**
- 데이터 기준일(주가): **2026-08-19**

## Verdict
**⏸ No confirmed entry; watchlist only**

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

- HY OAS: 2.75 / 4주 변화 0.06 bp-ish / 2026-08-18
- IG OAS: 0.82 / 4주 변화 0.04 bp-ish / 2026-08-18
- 10Y Real Yield: 2.44 / 4주 변화 0.09 bp-ish / 2026-08-17
- VIX: 15.84 / 4주 변화 -1.21 / 2026-08-18
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 12.98% / slope_proxy 16.34%
- GDXJ/GLD: gap 12.58% / slope_proxy 16.23%
- SILJ/SLV: gap 11.81% / slope_proxy 10.55%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.26 | RSI14: 79.50 | ATR14%: 5.68%
- MA20/50/200 gap: 20.22% / 29.73% / 44.48%
- 5D return: 2.70% | 20D drawdown: 0.00% | vol_ratio: 0.27
- RS vs GDXJ: gap 7.71% / slope_proxy 11.62%
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
- close: 7.50 | RSI14: 86.69 | ATR14%: 4.88%
- MA20/50/200 gap: 20.93% / 32.08% / 9.04%
- 5D return: 8.23% | 20D drawdown: 0.00% | vol_ratio: 0.50
- RS vs GDXJ: gap 8.50% / slope_proxy 11.16%
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
- close: 1.66 | RSI14: 82.93 | ATR14%: 5.51%
- MA20/50/200 gap: 26.77% / 33.27% / 12.27%
- 5D return: 14.48% | 20D drawdown: 0.00% | vol_ratio: 1.66
- RS vs GDXJ: gap 10.31% / slope_proxy 15.56%
- FundamentalScore: 70 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **74.2**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.41 | RSI14: 74.42 | ATR14%: 5.75%
- MA20/50/200 gap: 18.28% / 31.46% / 30.00%
- 5D return: 11.06% | 20D drawdown: 0.00% | vol_ratio: 0.88
- RS vs GDXJ: gap 8.98% / slope_proxy -4.52%
- FundamentalScore: 55 | TechnicalScore: 25 | RegimeScore: 100 | OverallScore: **53.5**
- Checks:
  - sector_ok: **True**
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
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.48 | RSI14: 71.27 | ATR14%: 6.26%
- MA20/50/200 gap: 15.59% / 31.00% / 59.22%
- 5D return: -2.00% | 20D drawdown: -2.00% | vol_ratio: 0.62
- RS vs SILJ: gap 14.51% / slope_proxy 9.42%
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
- close: 10.91 | RSI14: 74.17 | ATR14%: 5.89%
- MA20/50/200 gap: 20.75% / 28.10% / 13.21%
- 5D return: 2.87% | 20D drawdown: 0.00% | vol_ratio: 0.52
- RS vs SILJ: gap 9.10% / slope_proxy 9.56%
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
- close: 20.27 | RSI14: 74.72 | ATR14%: 5.20%
- MA20/50/200 gap: 23.21% / 28.08% / 9.17%
- 5D return: 11.99% | 20D drawdown: 0.00% | vol_ratio: 0.31
- RS vs SILJ: gap 9.26% / slope_proxy 5.05%
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
- close: 9.44 | RSI14: 79.81 | ATR14%: 6.17%
- MA20/50/200 gap: 24.28% / 34.92% / 10.27%
- 5D return: 6.43% | 20D drawdown: 0.00% | vol_ratio: 0.96
- RS vs SILJ: gap 14.45% / slope_proxy 15.25%
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
- close: 7.59 | RSI14: 73.70 | ATR14%: 5.74%
- MA20/50/200 gap: 19.27% / 22.11% / 12.34%
- 5D return: 6.23% | 20D drawdown: 0.00% | vol_ratio: 0.70
- RS vs SILJ: gap 3.76% / slope_proxy 5.84%
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
- close: 3.86 | RSI14: 69.28 | ATR14%: 4.83%
- MA20/50/200 gap: 9.90% / 14.19% / -5.42%
- 5D return: 1.45% | 20D drawdown: -0.64% | vol_ratio: 0.42
- RS vs SILJ: gap -3.40% / slope_proxy -5.53%
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
- close: 5.39 | RSI14: 75.66 | ATR14%: 5.86%
- MA20/50/200 gap: 17.76% / 16.54% / -6.49%
- 5D return: 3.95% | 20D drawdown: 0.00% | vol_ratio: 0.56
- RS vs SILJ: gap -3.18% / slope_proxy 5.51%
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
- close: 27.24 | RSI14: 70.73 | ATR14%: 7.21%
- MA20/50/200 gap: 15.55% / 17.80% / -5.81%
- 5D return: -0.77% | 20D drawdown: -1.05% | vol_ratio: 0.70
- RS vs SILJ: gap -3.52% / slope_proxy 5.61%
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
