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

- 실행시간(UTC): **2026-09-22 15:01:13**
- 데이터 기준일(일봉): **2026-09-22**
- 데이터 기준일(주봉): **2026-09-21**
- VXN 기준일: **2026-09-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 744.72
- Weekly RSI14: **63.92**
- 52W MA: 652.97 / gap: **14.05%**
- 104W MA gap: **27.30%**
- 52W MA 13W slope: **5.86%**
- VXN: **20.39** / 5D change: -1.66

## Daily trigger: 실제 매수 타이밍

- QQQ close: 744.71
- Daily RSI14: **67.23**
- 20D gap: **4.03%**
- 50D gap: **4.86%**
- 200D gap: **12.44%**
- MACD hist: 3.1097 / change: 1.2350
- ATR14%: **1.33%**
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

- 데이터 기준일(주가): **2026-09-22**
- 실행시간(UTC): **2026-09-22 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.68 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.77 / 4주 변화 -4.0 bp
- 10Y Real Yield (DFII10): 2.68 / 4주 변화 28.0 bp
- VIX (VIXCLS): 14.87
- NFCI: -0.56

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.44463
- MA60: 9.053719
- gap: -6.73%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.436917
- MA60: 0.388791
- gap: 12.38%
- MA60_slope_proxy: -0.01344
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-22**
- 실행시간(UTC): **2026-09-22 15:00:51**

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
- TERM_SPREAD_10Y_POLICY: 150.6 bp / 4주 변화 20.54 bp
- CURVE_10s5s: 37.34 bp / 4주 변화 -12.1 bp

## NWG Price
- close: 698.8
- MA50: 690.8852 / gap50: 1.15%
- MA200: 632.642 / gap200: 10.46%

## Relative Strength
- RS vs FTSE gap: 1.74% / slope_proxy: 0.001528
- RS vs Peers gap: 3.98% / slope_proxy: 0.010953

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-22 15:00:59**

## Commodity Regime

- WTI ref (CL=F): 91.10 / 5D -13.92%
- Brent ref (BZ=F): 99.88 / 5D -8.16%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.78
- Gas ref (NG=F): 3.08 / 5D 5.69%

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

- close: 57.13
- MA20 / MA60 / MA200: 59.84 / 56.74 / 52.96
- gap20 / gap60: -4.51% / 0.69%
- 5D return: -10.05%
- 20D high/low: 63.52 / 57.13

### Relative Strength

- ratio: 0.915772
- ratio_MA60: 0.947224
- ratio_gap: -3.32%
- ratio_slope_proxy(20d): -0.014939

### Volume (if available)

- volume: 2400441.00
- volume_MA20: 7766392.05
- volume_ratio: 0.31

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.66
- MA20 / MA60 / MA200: 20.24 / 18.39 / 16.97
- gap20 / gap60: 2.06% / 12.34%
- 5D return: -5.12%
- 20D high/low: 21.77 / 17.76

### Relative Strength

- ratio: 0.545635
- ratio_MA60: 0.511274
- ratio_gap: 6.72%
- ratio_slope_proxy(20d): 0.014660

### Volume (if available)

- volume: 5358829.00
- volume_MA20: 22464461.45
- volume_ratio: 0.24

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.41
- MA20 / MA60 / MA200: 5.74 / 5.47 / 5.64
- gap20 / gap60: -5.68% / -1.02%
- 5D return: -8.92%
- 20D high/low: 6.22 / 5.41

### Relative Strength

- ratio: 0.013614
- ratio_MA60: 0.013743
- ratio_gap: -0.94%
- ratio_slope_proxy(20d): -0.000093

### Volume (if available)

- volume: 8107943.00
- volume_MA20: 40357227.15
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.46
- MA20 / MA60 / MA200: 14.60 / 13.61 / 11.75
- gap20 / gap60: -7.83% / -1.12%
- 5D return: -12.00%
- 20D high/low: 15.76 / 13.46

### Relative Strength

- ratio: 0.049066
- ratio_MA60: 0.050805
- ratio_gap: -3.42%
- ratio_slope_proxy(20d): 0.000431

### Volume (if available)

- volume: 2583722.00
- volume_MA20: 13584836.10
- volume_ratio: 0.19

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

- 데이터 기준일(주가): **2026-09-22**
- 실행시간(UTC): **2026-09-22 15:01:03**

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
- 10Y Real Yield 4주 변화: 28.0 bp / latest 2.68
- VIX: 14.87
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 2.30% / slope_proxy: 0.02177
- GDXJ/GLD gap: 8.93% / slope_proxy: 0.014362

## VZLA (Vizsla Silver)
- close: 4.085 | RSI14: 57.206789 | ATR14%: 4.86%
- MA20 gap: 2.03% | MA50 gap: 10.75% | MA200 gap: 1.40%
- vol_ratio(Volume/Vol20): 0.158244 | gap_open: 0.00%
- RS vs SILJ gap: 5.81% / slope_proxy: 0.000394
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
- close: 9.15 | RSI14: 50.386847 | ATR14%: 6.68%
- MA20 gap: -3.85% | MA50 gap: 9.52% | MA200 gap: 1.71%
- vol_ratio(Volume/Vol20): 0.177964 | gap_open: 0.22%
- SilverMarginGate: SI=66.114998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.01% / slope_proxy: 0.017434
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
- close: 21.09 | RSI14: 43.178049 | ATR14%: 7.31%
- MA20 gap: -6.22% | MA50 gap: -7.68% | MA200 gap: -30.81%
- vol_ratio(Volume/Vol20): 0.269442 | gap_open: 0.83%
- RS vs SILJ gap: -13.73% / slope_proxy: -0.079299
- RS vs GDXJ gap: -16.55% / slope_proxy: -0.024797
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

- 실행시간(UTC): **2026-09-22 15:01:12**
- 데이터 기준일(주가): **2026-09-22**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.68 / 4주 변화 -0.02 bp-ish / 2026-09-18
- IG OAS: 0.77 / 4주 변화 -0.04 bp-ish / 2026-09-18
- 10Y Real Yield: 2.68 / 4주 변화 0.33 bp-ish / 2026-09-18
- VIX: 14.87 / 4주 변화 -0.98 / 2026-09-21
- NFCI: -0.56 / 4주 변화 -0.07 / 2026-09-11

### Leadership ratios

- GDX/GLD: gap 8.79% / slope_proxy -2.49%
- GDXJ/GLD: gap 8.93% / slope_proxy -1.43%
- SILJ/SLV: gap 2.30% / slope_proxy -3.38%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 84.62%, above200 46.15%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.20 | RSI14: 60.26 | ATR14%: 4.50%
- MA20/50/200 gap: -0.54% / 11.45% / 32.83%
- 5D return: 0.20% | 20D drawdown: -7.86% | vol_ratio: 0.21
- RS vs GDXJ: gap 4.57% / slope_proxy 0.85%
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
- close: 7.89 | RSI14: 58.78 | ATR14%: 4.76%
- MA20/50/200 gap: 0.82% / 16.49% / 11.56%
- 5D return: 4.23% | 20D drawdown: -5.40% | vol_ratio: 0.14
- RS vs GDXJ: gap 10.58% / slope_proxy 9.72%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **76.6**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.68 | RSI14: 50.00 | ATR14%: 5.86%
- MA20/50/200 gap: 1.65% / 17.32% / 36.02%
- 5D return: 8.50% | 20D drawdown: -3.94% | vol_ratio: 0.13
- RS vs GDXJ: gap 11.89% / slope_proxy 8.24%
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
- close: 1.37 | RSI14: 43.24 | ATR14%: 5.97%
- MA20/50/200 gap: -8.54% / -0.67% / -8.40%
- 5D return: -0.72% | 20D drawdown: -14.91% | vol_ratio: 1.67
- RS vs GDXJ: gap -7.38% / slope_proxy -6.29%
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
- close: 29.14 | RSI14: 61.85 | ATR14%: 5.48%
- MA20/50/200 gap: 3.15% / 15.98% / 51.63%
- 5D return: 9.14% | 20D drawdown: -2.51% | vol_ratio: 0.10
- RS vs SILJ: gap 13.29% / slope_proxy 14.33%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 50 | OverallScore: **71.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.15 | RSI14: 49.59 | ATR14%: 7.22%
- MA20/50/200 gap: -3.85% / 9.52% / 1.71%
- 5D return: 5.90% | 20D drawdown: -12.27% | vol_ratio: 0.18
- RS vs SILJ: gap 7.01% / slope_proxy 1.82%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **57.3**
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
- close: 4.09 | RSI14: 58.12 | ATR14%: 5.15%
- MA20/50/200 gap: 2.03% / 10.75% / 1.40%
- 5D return: 8.64% | 20D drawdown: -2.04% | vol_ratio: 0.16
- RS vs SILJ: gap 5.81% / slope_proxy 9.93%
- FundamentalScore: 72 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **72.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.19 | RSI14: 49.32 | ATR14%: 5.33%
- MA20/50/200 gap: -3.59% / 6.21% / 2.45%
- 5D return: 5.65% | 20D drawdown: -11.20% | vol_ratio: 0.24
- RS vs SILJ: gap 2.06% / slope_proxy -0.15%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **52.1**
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
- close: 18.58 | RSI14: 46.68 | ATR14%: 5.35%
- MA20/50/200 gap: -6.25% / 4.08% / -3.14%
- 5D return: -0.51% | 20D drawdown: -13.28% | vol_ratio: 0.12
- RS vs SILJ: gap -0.52% / slope_proxy -3.41%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **50.4**
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
- close: 5.07 | RSI14: 50.50 | ATR14%: 5.81%
- MA20/50/200 gap: -2.60% / 5.87% / -14.09%
- 5D return: 8.21% | 20D drawdown: -11.59% | vol_ratio: 0.21
- RS vs SILJ: gap -0.09% / slope_proxy -1.82%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **45.9**
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
- close: 6.22 | RSI14: 37.51 | ATR14%: 6.03%
- MA20/50/200 gap: -10.39% / -5.53% / -11.32%
- 5D return: 1.28% | 20D drawdown: -19.55% | vol_ratio: 0.24
- RS vs SILJ: gap -10.92% / slope_proxy -9.73%
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
- close: 21.09 | RSI14: 46.92 | ATR14%: 6.67%
- MA20/50/200 gap: -6.22% / -7.68% / -30.81%
- 5D return: 1.88% | 20D drawdown: -19.13% | vol_ratio: 0.27
- RS vs SILJ: gap -13.73% / slope_proxy -12.08%
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
