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

- 실행시간(UTC): **2026-09-01 15:01:22**
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

- QQQ close: 710.11
- Weekly RSI14: **56.38**
- 52W MA: 645.64 / gap: **9.98%**
- 104W MA gap: **22.79%**
- 52W MA 13W slope: **6.46%**
- VXN: **20.18** / 5D change: -2.51

## Daily trigger: 실제 매수 타이밍

- QQQ close: 710.11
- Daily RSI14: **47.95**
- 20D gap: **-1.11%**
- 50D gap: **-0.13%**
- 200D gap: **8.39%**
- MACD hist: -0.7789 / change: -0.3703
- ATR14%: **1.42%**
- 20D high drawdown: **-3.00%**

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
- 실행시간(UTC): **2026-09-01 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.6 / 4주 변화 -25.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.42 / 4주 변화 -5.0 bp
- VIX (VIXCLS): 14.92
- NFCI: -0.566

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.227438
- MA60: 9.100438
- gap: -9.59%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.381605
- MA60: 0.399668
- gap: -4.52%
- MA60_slope_proxy: 0.013555
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-01**
- 실행시간(UTC): **2026-09-01 15:00:52**

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
- close: 680.8
- MA50: 681.5957 / gap50: -0.12%
- MA200: 625.9513 / gap200: 8.76%

## Relative Strength
- RS vs FTSE gap: 0.22% / slope_proxy: 0.00273
- RS vs Peers gap: 0.39% / slope_proxy: 0.019071

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-01 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 87.67 / 5D 6.45%
- Brent ref (BZ=F): 92.19 / 5D 4.08%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.52
- Gas ref (NG=F): 2.88 / 5D 3.94%

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
- MA20 / MA60 / MA200: 58.82 / 55.44 / 51.86
- gap20 / gap60: 3.62% / 9.94%
- 5D return: 4.35%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.946061
- ratio_MA60: 0.954013
- ratio_gap: -0.83%
- ratio_slope_proxy(20d): -0.014420

### Volume (if available)

- volume: 1570162.00
- volume_MA20: 7570918.10
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.02
- MA20 / MA60 / MA200: 18.04 / 17.41 / 16.36
- gap20 / gap60: 11.00% / 15.00%
- 5D return: 12.18%
- 20D high/low: 20.02 / 17.25

### Relative Strength

- ratio: 0.542389
- ratio_MA60: 0.497232
- ratio_gap: 9.08%
- ratio_slope_proxy(20d): -0.001754

### Volume (if available)

- volume: 7338976.00
- volume_MA20: 18509733.80
- volume_ratio: 0.40

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

- close: 5.91
- MA20 / MA60 / MA200: 5.71 / 5.44 / 5.53
- gap20 / gap60: 3.59% / 8.66%
- 5D return: 2.78%
- 20D high/low: 6.01 / 5.14

### Relative Strength

- ratio: 0.013786
- ratio_MA60: 0.013768
- ratio_gap: 0.13%
- ratio_slope_proxy(20d): -0.000443

### Volume (if available)

- volume: 9050335.00
- volume_MA20: 38735751.75
- volume_ratio: 0.23

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

- close: 14.98
- MA20 / MA60 / MA200: 13.96 / 12.94 / 11.26
- gap20 / gap60: 7.31% / 15.79%
- 5D return: 6.50%
- 20D high/low: 14.98 / 12.43

### Relative Strength

- ratio: 0.051700
- ratio_MA60: 0.050195
- ratio_gap: 3.00%
- ratio_slope_proxy(20d): -0.001206

### Volume (if available)

- volume: 4319835.00
- volume_MA20: 13072091.75
- volume_ratio: 0.33

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
- 실행시간(UTC): **2026-09-01 15:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -25.0 bp / latest 2.6
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: -5.0 bp / latest 2.42
- VIX: 14.92
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 8.64% / slope_proxy: 0.025791
- GDXJ/GLD gap: 13.18% / slope_proxy: 0.007586

## VZLA (Vizsla Silver)
- close: 3.945 | RSI14: 57.331739 | ATR14%: 4.86%
- MA20 gap: 2.53% | MA50 gap: 13.86% | MA200 gap: -3.12%
- vol_ratio(Volume/Vol20): 0.299053 | gap_open: 3.95%
- RS vs SILJ gap: 0.81% / slope_proxy: 0.001833
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
- close: 9.15 | RSI14: 56.636351 | ATR14%: 6.11%
- MA20 gap: 0.59% | MA50 gap: 21.64% | MA200 gap: 4.34%
- vol_ratio(Volume/Vol20): 0.305968 | gap_open: 4.38%
- SilverMarginGate: SI=65.389999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 10.13% / slope_proxy: 0.007218
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
- close: 22.290001 | RSI14: 42.062375 | ATR14%: 8.45%
- MA20 gap: -13.46% | MA50 gap: -3.35% | MA200 gap: -24.95%
- vol_ratio(Volume/Vol20): 0.327011 | gap_open: 5.63%
- RS vs SILJ gap: -15.78% / slope_proxy: -0.100435
- RS vs GDXJ gap: -18.89% / slope_proxy: -0.029853
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

- 실행시간(UTC): **2026-09-01 15:01:19**
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

- HY OAS: 2.60 / 4주 변화 -0.25 bp-ish / 2026-08-28
- IG OAS: 0.79 / 4주 변화 0.00 bp-ish / 2026-08-28
- 10Y Real Yield: 2.42 / 4주 변화 -0.05 bp-ish / 2026-08-28
- VIX: 14.92 / 4주 변화 -0.94 / 2026-08-31
- NFCI: -0.57 / 4주 변화 -0.10 / 2026-08-21

### Leadership ratios

- GDX/GLD: gap 13.63% / slope_proxy 12.65%
- GDXJ/GLD: gap 13.18% / slope_proxy 11.60%
- SILJ/SLV: gap 8.65% / slope_proxy 6.06%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 92.31%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.78 | RSI14: 47.12 | ATR14%: 5.57%
- MA20/50/200 gap: -2.53% / 16.20% / 33.26%
- 5D return: -11.65% | 20D drawdown: -11.65% | vol_ratio: 0.13
- RS vs GDXJ: gap 1.50% / slope_proxy 4.08%
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
- close: 7.35 | RSI14: 57.78 | ATR14%: 4.92%
- MA20/50/200 gap: 1.35% / 21.37% / 5.48%
- 5D return: -6.61% | 20D drawdown: -10.04% | vol_ratio: 0.18
- RS vs GDXJ: gap 5.75% / slope_proxy 2.79%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.50 | RSI14: 54.24 | ATR14%: 5.40%
- MA20/50/200 gap: -1.64% / 15.24% / 0.88%
- 5D return: -6.25% | 20D drawdown: -9.09% | vol_ratio: 0.14
- RS vs GDXJ: gap -0.46% / slope_proxy -2.32%
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
- close: 2.65 | RSI14: 70.34 | ATR14%: 5.96%
- MA20/50/200 gap: 11.79% / 31.79% / 39.11%
- 5D return: -2.21% | 20D drawdown: -2.21% | vol_ratio: 0.74
- RS vs GDXJ: gap 17.07% / slope_proxy 19.20%
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
- close: 10.44 | RSI14: 48.35 | ATR14%: 6.54%
- MA20/50/200 gap: 0.31% / 16.65% / 6.68%
- 5D return: -5.91% | 20D drawdown: -7.65% | vol_ratio: 0.28
- RS vs SILJ: gap 4.89% / slope_proxy 5.08%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.15 | RSI14: 53.55 | ATR14%: 6.28%
- MA20/50/200 gap: 0.59% / 21.64% / 4.34%
- 5D return: -6.35% | 20D drawdown: -8.68% | vol_ratio: 0.31
- RS vs SILJ: gap 10.13% / slope_proxy 3.72%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.68 | RSI14: 48.47 | ATR14%: 6.35%
- MA20/50/200 gap: 2.23% / 22.84% / 53.55%
- 5D return: -0.11% | 20D drawdown: -5.50% | vol_ratio: 0.48
- RS vs SILJ: gap 12.74% / slope_proxy -0.38%
- FundamentalScore: 86 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **74.7**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 19.64 | RSI14: 58.64 | ATR14%: 5.57%
- MA20/50/200 gap: 3.09% / 17.40% / 3.99%
- 5D return: -6.14% | 20D drawdown: -8.38% | vol_ratio: 0.16
- RS vs SILJ: gap 5.71% / slope_proxy 7.11%
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
- close: 7.21 | RSI14: 51.25 | ATR14%: 5.79%
- MA20/50/200 gap: -0.03% / 12.47% / 4.71%
- 5D return: -3.74% | 20D drawdown: -6.73% | vol_ratio: 0.26
- RS vs SILJ: gap 0.19% / slope_proxy 0.39%
- FundamentalScore: 60 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **71.8**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.94 | RSI14: 55.30 | ATR14%: 4.79%
- MA20/50/200 gap: 2.40% / 13.72% / -3.24%
- 5D return: -2.48% | 20D drawdown: -5.29% | vol_ratio: 0.30
- RS vs SILJ: gap 0.68% / slope_proxy -0.97%
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
- close: 5.22 | RSI14: 50.54 | ATR14%: 6.00%
- MA20/50/200 gap: -0.41% / 12.01% / -10.64%
- 5D return: -7.21% | 20D drawdown: -9.15% | vol_ratio: 0.24
- RS vs SILJ: gap -2.53% / slope_proxy -2.17%
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
- close: 22.30 | RSI14: 34.95 | ATR14%: 8.52%
- MA20/50/200 gap: -13.42% / -3.30% / -24.92%
- 5D return: -14.49% | 20D drawdown: -20.07% | vol_ratio: 0.33
- RS vs SILJ: gap -15.74% / slope_proxy -17.81%
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
