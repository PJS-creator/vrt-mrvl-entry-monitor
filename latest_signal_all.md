# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-02 00:30:39**
- 데이터 기준일(일봉): **2026-09-01**
- 데이터 기준일(주봉): **2026-08-31**
- VXN 기준일: **2026-08-31** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 707.64
- Weekly RSI14: **55.72**
- 52W MA: 645.60 / gap: **9.61%**
- 104W MA gap: **22.37%**
- 52W MA 13W slope: **6.46%**
- VXN: **20.18** / 5D change: -2.51

## Daily trigger: 실제 매수 타이밍

- QQQ close: 707.64
- Daily RSI14: **46.57**
- 20D gap: **-1.44%**
- 50D gap: **-0.47%**
- 200D gap: **8.02%**
- MACD hist: -0.9366 / change: -0.5279
- ATR14%: **1.44%**
- 20D high drawdown: **-3.34%**

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

- 데이터 기준일(주가): **2026-09-01**
- 실행시간(UTC): **2026-09-02 00:30:15**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.63 / 4주 변화 -15.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.44 / 4주 변화 1.0 bp
- VIX (VIXCLS): 14.92
- NFCI: -0.566

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.35684
- MA60: 9.113459
- gap: -8.30%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.385881
- MA60: 0.400918
- gap: -3.75%
- MA60_slope_proxy: 0.016197
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-01**
- 실행시간(UTC): **2026-09-02 00:30:17**

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
- TERM_SPREAD_10Y_POLICY: 127.54 bp / 4주 변화 2.87 bp
- CURVE_10s5s: 47.98 bp / 4주 변화 0.66 bp

## NWG Price
- close: 682.8
- MA50: 681.6357 / gap50: 0.17%
- MA200: 625.9613 / gap200: 9.08%

## Relative Strength
- RS vs FTSE gap: 0.02% / slope_proxy: 0.002868
- RS vs Peers gap: 0.33% / slope_proxy: 0.019062

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-02 00:30:22**

## Commodity Regime

- WTI ref (CL=F): 90.94 / 5D 10.42%
- Brent ref (BZ=F): 95.39 / 5D 7.69%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.45
- Gas ref (NG=F): 2.96 / 5D 6.86%

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

- close: 60.95
- MA20 / MA60 / MA200: 58.62 / 55.40 / 51.77
- gap20 / gap60: 3.98% / 10.02%
- 5D return: 1.40%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.941022
- ratio_MA60: 0.954710
- ratio_gap: -1.43%
- ratio_slope_proxy(20d): -0.014143

### Volume (if available)

- volume: 7118499.00
- volume_MA20: 8079029.95
- volume_ratio: 0.88

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.33
- MA20 / MA60 / MA200: 18.04 / 17.40 / 16.33
- gap20 / gap60: 12.70% / 16.86%
- 5D return: 12.51%
- 20D high/low: 20.33 / 17.25

### Relative Strength

- ratio: 0.555920
- ratio_MA60: 0.497301
- ratio_gap: 11.79%
- ratio_slope_proxy(20d): -0.001802

### Volume (if available)

- volume: 31038227.00
- volume_MA20: 19324191.35
- volume_ratio: 1.61

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

- close: 5.92
- MA20 / MA60 / MA200: 5.68 / 5.44 / 5.52
- gap20 / gap60: 4.28% / 8.79%
- 5D return: 2.60%
- 20D high/low: 6.01 / 5.14

### Relative Strength

- ratio: 0.013868
- ratio_MA60: 0.013778
- ratio_gap: 0.66%
- ratio_slope_proxy(20d): -0.000458

### Volume (if available)

- volume: 36347251.00
- volume_MA20: 40228477.55
- volume_ratio: 0.90

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

- close: 15.11
- MA20 / MA60 / MA200: 13.90 / 12.92 / 11.23
- gap20 / gap60: 8.68% / 16.95%
- 5D return: 5.00%
- 20D high/low: 15.11 / 12.43

### Relative Strength

- ratio: 0.051372
- ratio_MA60: 0.050246
- ratio_gap: 2.24%
- ratio_slope_proxy(20d): -0.001113

### Volume (if available)

- volume: 13861099.00
- volume_MA20: 13808114.95
- volume_ratio: 1.00

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-01**
- 실행시간(UTC): **2026-09-02 00:30:27**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -15.0 bp / latest 2.63
- IG OAS 4주 변화: 2.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 1.0 bp / latest 2.44
- VIX: 14.92
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 7.71% / slope_proxy: 0.02491
- GDXJ/GLD gap: 11.27% / slope_proxy: 0.007497

## VZLA (Vizsla Silver)
- close: 3.86 | RSI14: 54.690673 | ATR14%: 4.91%
- MA20 gap: 1.22% | MA50 gap: 11.77% | MA200 gap: -5.28%
- vol_ratio(Volume/Vol20): 1.036965 | gap_open: 3.95%
- RS vs SILJ gap: 1.00% / slope_proxy: 0.002179
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 9.2 | RSI14: 57.69794 | ATR14%: 6.09%
- MA20 gap: 2.42% | MA50 gap: 23.10% | MA200 gap: 5.13%
- vol_ratio(Volume/Vol20): 0.907626 | gap_open: 4.38%
- SilverMarginGate: SI=64.699997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.75% / slope_proxy: 0.006238
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
- close: 21.629999 | RSI14: 40.739831 | ATR14%: 9.02%
- MA20 gap: -15.67% | MA50 gap: -6.25% | MA200 gap: -26.98%
- vol_ratio(Volume/Vol20): 1.062096 | gap_open: 5.63%
- RS vs SILJ gap: -16.69% / slope_proxy: -0.103033
- RS vs GDXJ gap: -19.72% / slope_proxy: -0.030207
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

- 실행시간(UTC): **2026-09-02 00:30:36**
- 데이터 기준일(주가): **2026-09-01**

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

- HY OAS: 2.63 / 4주 변화 -0.15 bp-ish / 2026-08-31
- IG OAS: 0.80 / 4주 변화 0.02 bp-ish / 2026-08-31
- 10Y Real Yield: 2.44 / 4주 변화 0.01 bp-ish / 2026-08-31
- VIX: 14.92 / 4주 변화 -0.94 / 2026-08-31
- NFCI: -0.57 / 4주 변화 -0.10 / 2026-08-21

### Leadership ratios

- GDX/GLD: gap 12.11% / slope_proxy 11.11%
- GDXJ/GLD: gap 11.27% / slope_proxy 9.69%
- SILJ/SLV: gap 7.71% / slope_proxy 6.91%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 92.31%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.57 | RSI14: 45.96 | ATR14%: 5.99%
- MA20/50/200 gap: -3.22% / 14.32% / 30.82%
- 5D return: -12.52% | 20D drawdown: -13.55% | vol_ratio: 0.75
- RS vs GDXJ: gap 2.03% / slope_proxy 6.64%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **84.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.40 | RSI14: 58.65 | ATR14%: 4.97%
- MA20/50/200 gap: 3.36% / 23.03% / 6.31%
- 5D return: -5.85% | 20D drawdown: -9.42% | vol_ratio: 2.27
- RS vs GDXJ: gap 9.30% / slope_proxy 5.98%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.68 | RSI14: 72.22 | ATR14%: 6.13%
- MA20/50/200 gap: 15.10% / 34.63% / 40.99%
- 5D return: 1.52% | 20D drawdown: -1.11% | vol_ratio: 1.20
- RS vs GDXJ: gap 21.79% / slope_proxy 24.79%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.47 | RSI14: 51.61 | ATR14%: 5.73%
- MA20/50/200 gap: -2.58% / 13.44% / -1.08%
- 5D return: -10.37% | 20D drawdown: -10.91% | vol_ratio: 0.44
- RS vs GDXJ: gap 0.06% / slope_proxy -1.98%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **51.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.37 | RSI14: 44.48 | ATR14%: 6.62%
- MA20/50/200 gap: -1.45% / 18.03% / 47.01%
- 5D return: -0.79% | 20D drawdown: -9.97% | vol_ratio: 1.34
- RS vs SILJ: gap 10.58% / slope_proxy 0.12%
- FundamentalScore: 86 | TechnicalScore: 100 | RegimeScore: 75 | OverallScore: **88.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.24 | RSI14: 46.82 | ATR14%: 6.68%
- MA20/50/200 gap: -0.31% / 15.09% / 4.83%
- 5D return: -4.83% | 20D drawdown: -9.38% | vol_ratio: 0.89
- RS vs SILJ: gap 5.60% / slope_proxy 6.88%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **81.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 19.11 | RSI14: 56.92 | ATR14%: 5.83%
- MA20/50/200 gap: 1.80% / 14.94% / 1.36%
- 5D return: -6.32% | 20D drawdown: -10.83% | vol_ratio: 0.79
- RS vs SILJ: gap 5.61% / slope_proxy 7.96%
- FundamentalScore: 78 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **79.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.20 | RSI14: 51.72 | ATR14%: 6.26%
- MA20/50/200 gap: 2.42% / 23.10% / 5.13%
- 5D return: -3.87% | 20D drawdown: -8.18% | vol_ratio: 0.91
- RS vs SILJ: gap 13.75% / slope_proxy 11.10%
- FundamentalScore: 74 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **78.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.01 | RSI14: 44.27 | ATR14%: 6.14%
- MA20/50/200 gap: -1.61% / 9.78% / 2.00%
- 5D return: -4.76% | 20D drawdown: -9.31% | vol_ratio: 0.74
- RS vs SILJ: gap -0.13% / slope_proxy 3.13%
- FundamentalScore: 60 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **63.0**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.86 | RSI14: 51.13 | ATR14%: 4.81%
- MA20/50/200 gap: 1.22% / 11.77% / -5.28%
- 5D return: -1.78% | 20D drawdown: -7.21% | vol_ratio: 1.04
- RS vs SILJ: gap 1.00% / slope_proxy -1.29%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.05 | RSI14: 48.22 | ATR14%: 6.29%
- MA20/50/200 gap: -2.42% / 8.59% / -13.38%
- 5D return: -6.31% | 20D drawdown: -12.02% | vol_ratio: 0.80
- RS vs SILJ: gap -3.46% / slope_proxy 0.02%
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
- close: 21.63 | RSI14: 33.48 | ATR14%: 9.37%
- MA20/50/200 gap: -15.67% / -6.25% / -26.98%
- 5D return: -15.97% | 20D drawdown: -22.47% | vol_ratio: 1.06
- RS vs SILJ: gap -16.69% / slope_proxy -15.89%
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
