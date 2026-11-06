# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **⏸ No entry today**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-06 15:01:40**
- 데이터 기준일(일봉): **2026-11-06**
- 데이터 기준일(주봉): **2026-11-02**
- VXN 기준일: **2026-11-05** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 662.52
- Weekly RSI14: **40.74**
- 52W MA: 665.14 / gap: **-0.39%**
- 104W MA gap: **10.83%**
- 52W MA 13W slope: **4.96%**
- VXN: **38.26** / 5D change: 13.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 662.52
- Daily RSI14: **34.27**
- 20D gap: **-6.42%**
- 50D gap: **-8.10%**
- 200D gap: **-2.55%**
- MACD hist: -6.2515 / change: -0.0122
- ATR14%: **2.33%**
- 20D high drawdown: **-11.20%**

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

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-06 15:00:53**

## MacroGreen
- **MacroGreen**: **False**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.32 / 4주 변화 23.0 bp
- IG OAS (BAMLC0A0CM): 0.91 / 4주 변화 9.0 bp
- 10Y Real Yield (DFII10): 2.64 / 4주 변화 -28.0 bp
- VIX (VIXCLS): 28.18
- NFCI: -0.459

## VRT 신규진입 룰
- ratio (VRT/SRVR): 6.775036
- MA60: 8.258033
- gap: -17.96%
- **VRT_ENTRY**: **False**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.305661
- MA60: 0.412731
- gap: -25.94%
- MA60_slope_proxy: 0.015076
- **MRVL_ENTRY**: **False**

## Verdict
⏸ No entry today

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-06 15:00:57**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **False**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 138.64 bp / 4주 변화 -24.88 bp
- CURVE_10s5s: 35.69 bp / 4주 변화 -8.55 bp

## NWG Price
- close: 589.0
- MA50: 662.788 / gap50: -11.13%
- MA200: 633.7236 / gap200: -7.06%

## Relative Strength
- RS vs FTSE gap: -10.95% / slope_proxy: -0.001786
- RS vs Peers gap: -2.06% / slope_proxy: 0.017245

## Why not today?
- RiskGreen=FALSE
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-06 15:01:09**

## Commodity Regime

- WTI ref (CL=F): 90.81 / 5D -12.78%
- Brent ref (BZ=F): 97.93 / 5D -16.75%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.12
- Gas ref (NG=F): 3.00 / 5D 3.35%

## Gates

- **RISK_OK_STRICT**: **False**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 56.59
- MA20 / MA60 / MA200: 61.52 / 59.91 / 56.09
- gap20 / gap60: -8.01% / -5.53%
- 5D return: -11.58%
- 20D high/low: 64.17 / 56.36

### Relative Strength

- ratio: 0.913308
- ratio_MA60: 0.928048
- ratio_gap: -1.59%
- ratio_slope_proxy(20d): -0.013655

### Volume (if available)

- volume: 829751.00
- volume_MA20: 8702147.55
- volume_ratio: 0.10

### Checks

- RISK_OK_STRICT: **False**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.90
- MA20 / MA60 / MA200: 23.36 / 21.45 / 18.83
- gap20 / gap60: -19.09% / -11.89%
- 5D return: -14.29%
- 20D high/low: 26.16 / 18.80

### Relative Strength

- ratio: 0.586774
- ratio_MA60: 0.571937
- ratio_gap: 2.59%
- ratio_slope_proxy(20d): 0.039939

### Volume (if available)

- volume: 2090980.00
- volume_MA20: 26018714.00
- volume_ratio: 0.08

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

- close: 5.25
- MA20 / MA60 / MA200: 5.97 / 5.75 / 5.89
- gap20 / gap60: -12.10% / -8.70%
- 5D return: -24.35%
- 20D high/low: 6.94 / 5.10

### Relative Strength

- ratio: 0.014763
- ratio_MA60: 0.014383
- ratio_gap: 2.64%
- ratio_slope_proxy(20d): 0.000600

### Volume (if available)

- volume: 5670037.00
- volume_MA20: 45974386.85
- volume_ratio: 0.12

### Checks

- RISK_OK_STRICT: **False**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.54
- MA20 / MA60 / MA200: 13.15 / 13.70 / 12.75
- gap20 / gap60: -12.23% / -15.79%
- 5D return: -21.97%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041384
- ratio_MA60: 0.048604
- ratio_gap: -14.85%
- ratio_slope_proxy(20d): -0.002287

### Volume (if available)

- volume: 1554367.00
- volume_MA20: 16691963.35
- volume_ratio: 0.09

### Checks

- RISK_OK_STRICT: **False**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-06**
- 실행시간(UTC): **2026-11-06 15:01:19**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 23.0 bp / latest 3.32
- IG OAS 4주 변화: 9.0 bp / latest 0.91
- 10Y Real Yield 4주 변화: -28.0 bp / latest 2.64
- VIX: 28.18
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: 1.84% / slope_proxy: 0.004681
- GDXJ/GLD gap: -5.27% / slope_proxy: 0.002712

## VZLA (Vizsla Silver)
- close: 3.18 | RSI14: 44.116236 | ATR14%: 6.01%
- MA20 gap: -1.21% | MA50 gap: -11.99% | MA200 gap: -13.35%
- vol_ratio(Volume/Vol20): 0.065585 | gap_open: 0.63%
- RS vs SILJ gap: 0.71% / slope_proxy: 0.000552
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
- close: 7.41 | RSI14: 45.069821 | ATR14%: 7.10%
- MA20 gap: -3.18% | MA50 gap: -13.82% | MA200 gap: -14.57%
- vol_ratio(Volume/Vol20): 0.055721 | gap_open: 1.44%
- SilverMarginGate: SI=52.005001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.55% / slope_proxy: 0.013171
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
- close: 17.58 | RSI14: 49.496576 | ATR14%: 7.47%
- MA20 gap: 4.39% | MA50 gap: -8.74% | MA200 gap: -40.37%
- vol_ratio(Volume/Vol20): 0.133828 | gap_open: 1.59%
- RS vs SILJ gap: 0.39% / slope_proxy: -0.052741
- RS vs GDXJ gap: -3.79% / slope_proxy: -0.017657
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

- 실행시간(UTC): **2026-11-06 15:01:38**
- 데이터 기준일(주가): **2026-11-06**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **False**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.32 / 4주 변화 0.23 bp-ish / 2026-11-04
- IG OAS: 0.91 / 4주 변화 0.09 bp-ish / 2026-11-04
- 10Y Real Yield: 2.64 / 4주 변화 -0.27 bp-ish / 2026-11-04
- VIX: 28.18 / 4주 변화 12.77 / 2026-11-05
- NFCI: -0.46 / 4주 변화 0.04 / 2026-10-30

### Leadership ratios

- GDX/GLD: gap -0.81% / slope_proxy -0.19%
- GDXJ/GLD: gap -5.27% / slope_proxy -4.48%
- SILJ/SLV: gap 1.90% / slope_proxy 3.72%
- Gold breadth proxy: above50 23.08%, above200 30.77%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.75 | RSI14: 30.77 | ATR14%: 4.99%
- MA20/50/200 gap: -5.94% / -15.67% / -4.46%
- 5D return: 3.47% | 20D drawdown: -15.67% | vol_ratio: 0.03
- RS vs GDXJ: gap -8.33% / slope_proxy -9.10%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **44.9**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.38 | RSI14: 28.42 | ATR14%: 6.16%
- MA20/50/200 gap: -8.71% / -21.87% / -21.74%
- 5D return: 2.87% | 20D drawdown: -22.92% | vol_ratio: 0.07
- RS vs GDXJ: gap -13.94% / slope_proxy -15.80%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **42.1**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.81 | RSI14: 30.14 | ATR14%: 7.54%
- MA20/50/200 gap: -8.50% / -29.85% / -42.37%
- 5D return: 3.21% | 20D drawdown: -21.08% | vol_ratio: 0.04
- RS vs GDXJ: gap -25.63% / slope_proxy -13.79%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **36.8**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.66 | RSI14: 33.03 | ATR14%: 8.22%
- MA20/50/200 gap: -9.29% / -25.74% / -15.80%
- 5D return: 8.50% | 20D drawdown: -24.55% | vol_ratio: 0.02
- RS vs GDXJ: gap -18.11% / slope_proxy -17.58%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 0 | OverallScore: **30.0**
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
- Why not today: RiskGreen=FALSE, GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 24.67 | RSI14: 42.33 | ATR14%: 6.28%
- MA20/50/200 gap: -1.47% / -7.66% / 17.45%
- 5D return: 7.17% | 20D drawdown: -7.50% | vol_ratio: 0.13
- RS vs SILJ: gap 6.31% / slope_proxy 4.33%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **57.7**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.18 | RSI14: 49.23 | ATR14%: 6.20%
- MA20/50/200 gap: -1.21% / -11.99% / -13.35%
- 5D return: 3.92% | 20D drawdown: -9.14% | vol_ratio: 0.07
- RS vs SILJ: gap 0.69% / slope_proxy 1.63%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 25 | OverallScore: **51.4**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.64 | RSI14: 41.42 | ATR14%: 6.16%
- MA20/50/200 gap: -2.37% / -14.86% / -20.67%
- 5D return: 6.03% | 20D drawdown: -10.48% | vol_ratio: 0.09
- RS vs SILJ: gap -3.96% / slope_proxy 0.13%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **47.1**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.57 | RSI14: 46.39 | ATR14%: 5.79%
- MA20/50/200 gap: -0.92% / -14.49% / -20.39%
- 5D return: 7.71% | 20D drawdown: -13.46% | vol_ratio: 0.08
- RS vs SILJ: gap -3.33% / slope_proxy -3.21%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **45.4**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.41 | RSI14: 39.09 | ATR14%: 7.01%
- MA20/50/200 gap: -3.18% / -13.82% / -14.57%
- 5D return: 9.45% | 20D drawdown: -16.65% | vol_ratio: 0.06
- RS vs SILJ: gap -1.57% / slope_proxy -6.77%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **43.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.95 | RSI14: 29.26 | ATR14%: 8.07%
- MA20/50/200 gap: -11.41% / -30.43% / -47.16%
- 5D return: 2.96% | 20D drawdown: -29.64% | vol_ratio: 0.13
- RS vs SILJ: gap -21.87% / slope_proxy -21.30%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **40.9**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.59 | RSI14: 35.51 | ATR14%: 6.29%
- MA20/50/200 gap: -5.11% / -19.81% / -32.61%
- 5D return: 5.76% | 20D drawdown: -15.00% | vol_ratio: 0.11
- RS vs SILJ: gap -10.59% / slope_proxy -4.93%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **37.2**
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
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 17.48 | RSI14: 54.03 | ATR14%: 7.41%
- MA20/50/200 gap: 3.82% / -9.25% / -40.70%
- 5D return: 6.46% | 20D drawdown: -4.32% | vol_ratio: 0.14
- RS vs SILJ: gap -0.19% / slope_proxy 7.02%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 25 | OverallScore: **29.2**
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
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: RiskGreen=FALSE, SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
