# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-24 03:01:22**
- 데이터 기준일(일봉): **2026-09-23**
- 데이터 기준일(주봉): **2026-09-21**
- VXN 기준일: **2026-09-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 741.21
- Weekly RSI14: **63.27**
- 52W MA: 652.91 / gap: **13.52%**
- 104W MA gap: **26.70%**
- 52W MA 13W slope: **5.85%**
- VXN: **20.18** / 5D change: -2.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 741.21
- Daily RSI14: **63.49**
- 20D gap: **3.29%**
- 50D gap: **4.29%**
- 200D gap: **11.81%**
- MACD hist: 3.5850 / change: 0.2999
- ATR14%: **1.34%**
- 20D high drawdown: **-0.84%**

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

- 데이터 기준일(주가): **2026-09-23**
- 실행시간(UTC): **2026-09-24 03:00:51**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.68 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.77 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.63 / 4주 변화 31.0 bp
- VIX (VIXCLS): 14.21
- NFCI: -0.555

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.428649
- MA60: 9.053453
- gap: -6.90%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.433814
- MA60: 0.388615
- gap: 11.63%
- MA60_slope_proxy: -0.015122
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-23**
- 실행시간(UTC): **2026-09-24 03:00:54**

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
- TERM_SPREAD_10Y_POLICY: 141.3 bp / 4주 변화 11.17 bp
- CURVE_10s5s: 38.92 bp / 4주 변화 -9.3 bp

## NWG Price
- close: 695.0
- MA50: 690.8092 / gap50: 0.61%
- MA200: 632.623 / gap200: 9.86%

## Relative Strength
- RS vs FTSE gap: 3.08% / slope_proxy: 0.001589
- RS vs Peers gap: 3.65% / slope_proxy: 0.010899

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-24 03:01:02**

## Commodity Regime

- WTI ref (CL=F): 91.39 / 5D -10.78%
- Brent ref (BZ=F): 97.39 / 5D -7.98%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.00
- Gas ref (NG=F): 3.18 / 5D 10.13%

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

- close: 57.36
- MA20 / MA60 / MA200: 59.85 / 56.75 / 52.96
- gap20 / gap60: -4.16% / 1.08%
- 5D return: -9.70%
- 20D high/low: 63.52 / 57.25

### Relative Strength

- ratio: 0.919673
- ratio_MA60: 0.947289
- ratio_gap: -2.92%
- ratio_slope_proxy(20d): -0.014873

### Volume (if available)

- volume: 7909300.00
- volume_MA20: 8041835.00
- volume_ratio: 0.98

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.14
- MA20 / MA60 / MA200: 20.26 / 18.39 / 16.97
- gap20 / gap60: 4.33% / 14.93%
- 5D return: -2.89%
- 20D high/low: 21.77 / 17.76

### Relative Strength

- ratio: 0.565694
- ratio_MA60: 0.511608
- ratio_gap: 10.57%
- ratio_slope_proxy(20d): 0.014995

### Volume (if available)

- volume: 27529900.00
- volume_MA20: 23573015.00
- volume_ratio: 1.17

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

- close: 5.47
- MA20 / MA60 / MA200: 5.73 / 5.47 / 5.64
- gap20 / gap60: -4.46% / -0.08%
- 5D return: -1.26%
- 20D high/low: 6.22 / 5.45

### Relative Strength

- ratio: 0.013825
- ratio_MA60: 0.013747
- ratio_gap: 0.57%
- ratio_slope_proxy(20d): -0.000089

### Volume (if available)

- volume: 34259200.00
- volume_MA20: 43228795.00
- volume_ratio: 0.79

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.27
- MA20 / MA60 / MA200: 14.53 / 13.63 / 11.78
- gap20 / gap60: -8.69% / -2.67%
- 5D return: -9.42%
- 20D high/low: 15.76 / 12.91

### Relative Strength

- ratio: 0.048500
- ratio_MA60: 0.050796
- ratio_gap: -4.52%
- ratio_slope_proxy(20d): 0.000421

### Volume (if available)

- volume: 17483300.00
- volume_MA20: 14647095.00
- volume_ratio: 1.19

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-23**
- 실행시간(UTC): **2026-09-24 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.68
- IG OAS 4주 변화: -4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 31.0 bp / latest 2.63
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 1.73% / slope_proxy: 0.021722
- GDXJ/GLD gap: 7.48% / slope_proxy: 0.014292

## VZLA (Vizsla Silver)
- close: 4.04 | RSI14: 55.484408 | ATR14%: 5.08%
- MA20 gap: 0.96% | MA50 gap: 9.56% | MA200 gap: 0.29%
- vol_ratio(Volume/Vol20): 1.275999 | gap_open: 1.47%
- RS vs SILJ gap: 7.32% / slope_proxy: 0.000427
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
- close: 8.88 | RSI14: 47.825728 | ATR14%: 7.11%
- MA20 gap: -6.56% | MA50 gap: 6.35% | MA200 gap: -1.27%
- vol_ratio(Volume/Vol20): 1.216939 | gap_open: 2.44%
- SilverMarginGate: SI=64.57 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.55% / slope_proxy: 0.017412
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
- close: 21.26 | RSI14: 44.013217 | ATR14%: 7.42%
- MA20 gap: -5.50% | MA50 gap: -6.95% | MA200 gap: -30.26%
- vol_ratio(Volume/Vol20): 0.888761 | gap_open: 6.04%
- RS vs SILJ gap: -10.83% / slope_proxy: -0.078901
- RS vs GDXJ gap: -13.91% / slope_proxy: -0.024706
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

- 실행시간(UTC): **2026-09-24 03:01:20**
- 데이터 기준일(주가): **2026-09-23**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.68 / 4주 변화 -0.02 bp-ish / 2026-09-22
- IG OAS: 0.77 / 4주 변화 -0.04 bp-ish / 2026-09-22
- 10Y Real Yield: 2.63 / 4주 변화 0.25 bp-ish / 2026-09-22
- VIX: 14.21 / 4주 변화 -1.24 / 2026-09-22
- NFCI: -0.56 / 4주 변화 -0.05 / 2026-09-18

### Leadership ratios

- GDX/GLD: gap 7.49% / slope_proxy -2.04%
- GDXJ/GLD: gap 7.48% / slope_proxy -2.76%
- SILJ/SLV: gap 1.73% / slope_proxy -3.93%
- Gold breadth proxy: above50 92.31%, above200 69.23%, count 13
- Silver breadth proxy: above50 69.23%, above200 23.08%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.07 | RSI14: 58.06 | ATR14%: 4.62%
- MA20/50/200 gap: -1.74% / 10.06% / 31.15%
- 5D return: -1.08% | 20D drawdown: -9.03% | vol_ratio: 0.75
- RS vs GDXJ: gap 5.67% / slope_proxy 1.93%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **79.3**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.70 | RSI14: 55.51 | ATR14%: 4.99%
- MA20/50/200 gap: -1.48% / 13.74% / 8.89%
- 5D return: 1.72% | 20D drawdown: -7.67% | vol_ratio: 0.38
- RS vs GDXJ: gap 10.49% / slope_proxy 9.63%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **60.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.62 | RSI14: 46.67 | ATR14%: 6.35%
- MA20/50/200 gap: -0.51% / 14.75% / 32.99%
- 5D return: 6.07% | 20D drawdown: -6.09% | vol_ratio: 0.92
- RS vs GDXJ: gap 11.99% / slope_proxy 8.33%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **64.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.28 | RSI14: 38.55 | ATR14%: 7.11%
- MA20/50/200 gap: -14.30% / -7.07% / -14.39%
- 5D return: -7.25% | 20D drawdown: -20.50% | vol_ratio: 1.46
- RS vs GDXJ: gap -11.34% / slope_proxy -10.36%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **52.0**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 28.19 | RSI14: 57.76 | ATR14%: 5.96%
- MA20/50/200 gap: -0.04% / 12.28% / 46.72%
- 5D return: 5.58% | 20D drawdown: -5.69% | vol_ratio: 0.90
- RS vs SILJ: gap 12.44% / slope_proxy 13.46%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **78.5**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.88 | RSI14: 47.41 | ATR14%: 7.67%
- MA20/50/200 gap: -6.56% / 6.35% / -1.27%
- 5D return: 2.78% | 20D drawdown: -14.86% | vol_ratio: 1.22
- RS vs SILJ: gap 6.55% / slope_proxy 1.37%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 50 | OverallScore: **62.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.04 | RSI14: 56.43 | ATR14%: 5.37%
- MA20/50/200 gap: 0.96% / 9.56% / 0.29%
- 5D return: 7.45% | 20D drawdown: -3.12% | vol_ratio: 1.28
- RS vs SILJ: gap 7.32% / slope_proxy 11.53%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 50 | OverallScore: **61.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.26 | RSI14: 39.92 | ATR14%: 6.43%
- MA20/50/200 gap: -11.96% / -3.25% / -6.81%
- 5D return: -3.94% | 20D drawdown: -19.27% | vol_ratio: 1.50
- RS vs SILJ: gap -4.70% / slope_proxy -6.87%
- FundamentalScore: 82 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **57.4**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 18.27 | RSI14: 33.24 | ATR14%: 5.44%
- MA20/50/200 gap: -7.32% / 1.95% / -4.83%
- 5D return: 1.56% | 20D drawdown: -14.75% | vol_ratio: 1.93
- RS vs SILJ: gap 0.30% / slope_proxy -2.60%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **55.6**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.85 | RSI14: 46.21 | ATR14%: 6.36%
- MA20/50/200 gap: -6.71% / 1.27% / -17.88%
- 5D return: 3.41% | 20D drawdown: -15.51% | vol_ratio: 1.01
- RS vs SILJ: gap -2.02% / slope_proxy -3.75%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 50 | OverallScore: **51.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.04 | RSI14: 35.17 | ATR14%: 6.40%
- MA20/50/200 gap: -12.85% / -8.19% / -13.85%
- 5D return: -1.63% | 20D drawdown: -21.86% | vol_ratio: 0.86
- RS vs SILJ: gap -11.23% / slope_proxy -10.06%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **42.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.26 | RSI14: 47.93 | ATR14%: 6.79%
- MA20/50/200 gap: -5.50% / -6.95% / -30.26%
- 5D return: 2.71% | 20D drawdown: -18.48% | vol_ratio: 0.89
- RS vs SILJ: gap -10.83% / slope_proxy -9.08%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **34.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
