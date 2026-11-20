# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-20 03:43:04**
- 데이터 기준일(일봉): **2026-11-19**
- 데이터 기준일(주봉): **2026-11-16**
- VXN 기준일: **2026-11-18** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 645.04
- Weekly RSI14: **39.36**
- 52W MA: 667.54 / gap: **-3.37%**
- 104W MA gap: **7.34%**
- 52W MA 13W slope: **4.39%**
- VXN: **33.12** / 5D change: 6.38

## Daily trigger: 실제 매수 타이밍

- QQQ close: 645.04
- Daily RSI14: **33.92**
- 20D gap: **-5.60%**
- 50D gap: **-9.53%**
- 200D gap: **-5.42%**
- MACD hist: -2.2264 / change: -0.7347
- ATR14%: **2.67%**
- 20D high drawdown: **-11.10%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-20 03:42:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.47 / 4주 변화 20.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.88 / 4주 변화 12.0 bp
- VIX (VIXCLS): 24.56
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.139239
- MA60: 8.042288
- gap: -11.23%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.309444
- MA60: 0.398509
- gap: -22.35%
- MA60_slope_proxy: -0.012911
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-20 03:42:45**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 135.2 bp / 4주 변화 -24.96 bp
- CURVE_10s5s: 35.2 bp / 4주 변화 -3.78 bp

## NWG Price
- close: 588.8
- MA50: 647.336 / gap50: -9.04%
- MA200: 630.7098 / gap200: -6.64%

## Relative Strength
- RS vs FTSE gap: -8.69% / slope_proxy: -0.002746
- RS vs Peers gap: -0.77% / slope_proxy: 0.004732

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-20 03:42:51**

## Commodity Regime

- WTI ref (CL=F): 82.71 / 5D -6.80%
- Brent ref (BZ=F): 89.77 / 5D -6.31%
- Brent Tier: **80-90**
- Brent-WTI spread: 7.06
- Gas ref (NG=F): 3.25 / 5D -2.54%

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

- close: 53.81
- MA20 / MA60 / MA200: 59.03 / 59.46 / 56.64
- gap20 / gap60: -8.84% / -9.51%
- 5D return: -7.86%
- 20D high/low: 64.17 / 53.76

### Relative Strength

- ratio: 0.883725
- ratio_MA60: 0.920430
- ratio_gap: -3.99%
- ratio_slope_proxy(20d): -0.015540

### Volume (if available)

- volume: 9311500.00
- volume_MA20: 11033000.00
- volume_ratio: 0.84

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.29
- MA20 / MA60 / MA200: 19.74 / 21.40 / 18.97
- gap20 / gap60: -17.46% / -23.86%
- 5D return: -10.00%
- 20D high/low: 26.16 / 16.29

### Relative Strength

- ratio: 0.552016
- ratio_MA60: 0.578226
- ratio_gap: -4.53%
- ratio_slope_proxy(20d): 0.030616

### Volume (if available)

- volume: 21678700.00
- volume_MA20: 28459850.00
- volume_ratio: 0.76

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 4.77
- MA20 / MA60 / MA200: 5.71 / 5.65 / 5.90
- gap20 / gap60: -16.49% / -15.63%
- 5D return: -10.34%
- 20D high/low: 6.94 / 4.77

### Relative Strength

- ratio: 0.013798
- ratio_MA60: 0.014433
- ratio_gap: -4.40%
- ratio_slope_proxy(20d): 0.000445

### Volume (if available)

- volume: 42391000.00
- volume_MA20: 41418905.00
- volume_ratio: 1.02

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.13
- MA20 / MA60 / MA200: 12.92 / 13.46 / 12.88
- gap20 / gap60: -6.11% / -9.88%
- 5D return: -8.52%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041067
- ratio_MA60: 0.047278
- ratio_gap: -13.14%
- ratio_slope_proxy(20d): -0.002677

### Volume (if available)

- volume: 11746500.00
- volume_MA20: 15241835.00
- volume_ratio: 0.77

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-20 03:42:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 20.0 bp / latest 3.47
- IG OAS 4주 변화: 5.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.88
- VIX: 24.56
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: 0.93% / slope_proxy: 0.003328
- GDXJ/GLD gap: -12.81% / slope_proxy: -0.005522

## VZLA (Vizsla Silver)
- close: 2.98 | RSI14: 40.006438 | ATR14%: 6.48%
- MA20 gap: -5.71% | MA50 gap: -14.13% | MA200 gap: -16.21%
- vol_ratio(Volume/Vol20): 2.242756 | gap_open: 2.69%
- RS vs SILJ gap: 8.04% / slope_proxy: 0.002575
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
- close: 6.8 | RSI14: 43.134274 | ATR14%: 8.58%
- MA20 gap: -5.50% | MA50 gap: -16.78% | MA200 gap: -19.03%
- vol_ratio(Volume/Vol20): 1.936839 | gap_open: 4.18%
- SilverMarginGate: SI=41.494999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 4.23% / slope_proxy: 0.005454
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
- close: 15.25 | RSI14: 40.490826 | ATR14%: 9.74%
- MA20 gap: -9.84% | MA50 gap: -16.99% | MA200 gap: -46.19%
- vol_ratio(Volume/Vol20): 1.331188 | gap_open: 5.67%
- RS vs SILJ gap: 2.91% / slope_proxy: -0.046911
- RS vs GDXJ gap: -0.14% / slope_proxy: -0.015732
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

- 실행시간(UTC): **2026-11-20 03:43:03**
- 데이터 기준일(주가): **2026-11-19**

## Verdict
**🟡 Precious miners watch/add-on candidates: SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.47 / 4주 변화 0.20 bp-ish / 2026-11-18
- IG OAS: 0.93 / 4주 변화 0.05 bp-ish / 2026-11-18
- 10Y Real Yield: 2.88 / 4주 변화 0.11 bp-ish / 2026-11-18
- VIX: 24.56 / 4주 변화 7.88 / 2026-11-18
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -7.39% / slope_proxy -1.81%
- GDXJ/GLD: gap -12.81% / slope_proxy -5.51%
- SILJ/SLV: gap 0.93% / slope_proxy 6.93%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.74 | RSI14: 35.25 | ATR14%: 6.74%
- MA20/50/200 gap: -12.39% / -23.24% / -16.93%
- 5D return: -14.03% | 20D drawdown: -19.76% | vol_ratio: 2.01
- RS vs GDXJ: gap -6.09% / slope_proxy -5.58%
- FundamentalScore: 88 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **56.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 3.48 | RSI14: 27.03 | ATR14%: 11.82%
- MA20/50/200 gap: -31.67% / -44.79% / -48.05%
- 5D return: -31.63% | 20D drawdown: -40.92% | vol_ratio: 2.03
- RS vs GDXJ: gap -29.90% / slope_proxy -26.76%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **53.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.57 | RSI14: 27.66 | ATR14%: 12.03%
- MA20/50/200 gap: -27.06% / -43.01% / -57.37%
- 5D return: -27.85% | 20D drawdown: -36.67% | vol_ratio: 1.49
- RS vs GDXJ: gap -30.30% / slope_proxy -21.45%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.20 | RSI14: 34.86 | ATR14%: 11.49%
- MA20/50/200 gap: -25.07% / -40.75% / -38.24%
- 5D return: -23.57% | 20D drawdown: -33.33% | vol_ratio: 2.27
- RS vs GDXJ: gap -25.49% / slope_proxy -20.63%
- FundamentalScore: 55 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **41.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.80 | RSI14: 46.43 | ATR14%: 9.06%
- MA20/50/200 gap: -5.50% / -16.78% / -19.03%
- 5D return: -7.61% | 20D drawdown: -15.95% | vol_ratio: 1.94
- RS vs SILJ: gap 4.23% / slope_proxy 8.13%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **63.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 2.98 | RSI14: 40.00 | ATR14%: 6.98%
- MA20/50/200 gap: -5.71% / -14.13% / -16.21%
- 5D return: -8.02% | 20D drawdown: -14.86% | vol_ratio: 2.24
- RS vs SILJ: gap 8.04% / slope_proxy 5.91%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **62.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.90 | RSI14: 36.78 | ATR14%: 8.76%
- MA20/50/200 gap: -19.86% / -26.40% / -10.88%
- 5D return: -17.32% | 20D drawdown: -29.40% | vol_ratio: 1.91
- RS vs SILJ: gap -0.62% / slope_proxy -3.64%
- FundamentalScore: 86 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **60.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.08 | RSI14: 37.07 | ATR14%: 8.56%
- MA20/50/200 gap: -19.03% / -27.25% / -35.33%
- 5D return: -22.35% | 20D drawdown: -27.10% | vol_ratio: 1.37
- RS vs SILJ: gap -3.92% / slope_proxy -2.78%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **58.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 11.15 | RSI14: 35.77 | ATR14%: 8.01%
- MA20/50/200 gap: -18.63% / -29.14% / -37.09%
- 5D return: -16.48% | 20D drawdown: -27.64% | vol_ratio: 1.09
- RS vs SILJ: gap -8.99% / slope_proxy -6.23%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **56.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.05 | RSI14: 31.86 | ATR14%: 12.16%
- MA20/50/200 gap: -27.36% / -45.49% / -61.57%
- 5D return: -26.52% | 20D drawdown: -37.69% | vol_ratio: 1.55
- RS vs SILJ: gap -30.13% / slope_proxy -22.88%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **52.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.25 | RSI14: 42.82 | ATR14%: 11.14%
- MA20/50/200 gap: -9.84% / -16.99% / -46.19%
- 5D return: -18.45% | 20D drawdown: -28.30% | vol_ratio: 1.33
- RS vs SILJ: gap 2.91% / slope_proxy 9.71%
- FundamentalScore: 42 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **49.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.65 | RSI14: 36.14 | ATR14%: 8.00%
- MA20/50/200 gap: -17.87% / -29.44% / -44.28%
- 5D return: -17.05% | 20D drawdown: -25.66% | vol_ratio: 1.33
- RS vs SILJ: gap -10.10% / slope_proxy -8.25%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **48.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
