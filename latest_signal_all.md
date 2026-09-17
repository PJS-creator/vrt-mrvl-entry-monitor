# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **✅ QLD/TIGER 레버리지 매수 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-17 15:01:22**
- 데이터 기준일(일봉): **2026-09-17**
- 데이터 기준일(주봉): **2026-09-14**
- VXN 기준일: **2026-09-16** / source: `FRED: VXNCLS`

## Verdict

**✅ QLD/TIGER 레버리지 매수 허용**
- Regime: **A: QLD 본격 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,200,000원** (60%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **800,000원** (40%)
- 대기자금: **0원** (0%)

## Weekly gate: 큰 환경

- QQQ close: 715.03
- Weekly RSI14: **57.46**
- 52W MA: 650.61 / gap: **9.90%**
- 104W MA gap: **22.64%**
- 52W MA 13W slope: **5.90%**
- VXN: **22.44** / 5D change: 0.12

## Daily trigger: 실제 매수 타이밍

- QQQ close: 715.03
- Daily RSI14: **51.86**
- 20D gap: **0.34%**
- 50D gap: **0.72%**
- 200D gap: **8.14%**
- MACD hist: -0.8283 / change: 0.5990
- ATR14%: **1.31%**
- 20D high drawdown: **-0.84%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
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

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-17 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -3.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 -3.0 bp
- 10Y Real Yield (DFII10): 2.62 / 4주 변화 21.0 bp
- VIX (VIXCLS): 17.71
- NFCI: -0.56

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.168673
- MA60: 9.127439
- gap: -10.50%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.431333
- MA60: 0.389315
- gap: 10.79%
- MA60_slope_proxy: -0.008456
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-17 15:00:52**

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
- TERM_SPREAD_10Y_POLICY: 161.16 bp / 4주 변화 29.4 bp
- CURVE_10s5s: 43.28 bp / 4주 변화 -6.18 bp

## NWG Price
- close: 713.0
- MA50: 688.3465 / gap50: 3.58%
- MA200: 631.5417 / gap200: 12.90%

## Relative Strength
- RS vs FTSE gap: 3.04% / slope_proxy: 0.001683
- RS vs Peers gap: 4.52% / slope_proxy: 0.011311

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-17 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 100.93 / 5D -1.51%
- Brent ref (BZ=F): 103.38 / 5D -3.95%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.45
- Gas ref (NG=F): 2.92 / 5D 3.07%

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

- close: 58.87
- MA20 / MA60 / MA200: 60.26 / 56.37 / 52.71
- gap20 / gap60: -2.30% / 4.43%
- 5D return: -3.74%
- 20D high/low: 63.52 / 58.14

### Relative Strength

- ratio: 0.920347
- ratio_MA60: 0.942967
- ratio_gap: -2.40%
- ratio_slope_proxy(20d): -0.015585

### Volume (if available)

- volume: 2510139.00
- volume_MA20: 7293551.95
- volume_ratio: 0.34

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.83
- MA20 / MA60 / MA200: 19.88 / 18.15 / 16.84
- gap20 / gap60: 4.73% / 14.76%
- 5D return: -2.60%
- 20D high/low: 21.77 / 17.76

### Relative Strength

- ratio: 0.556149
- ratio_MA60: 0.507233
- ratio_gap: 9.64%
- ratio_slope_proxy(20d): 0.011443

### Volume (if available)

- volume: 4104609.00
- volume_MA20: 23106060.45
- volume_ratio: 0.18

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

- close: 5.58
- MA20 / MA60 / MA200: 5.79 / 5.45 / 5.62
- gap20 / gap60: -3.57% / 2.56%
- 5D return: -3.21%
- 20D high/low: 6.22 / 5.45

### Relative Strength

- ratio: 0.013943
- ratio_MA60: 0.013730
- ratio_gap: 1.55%
- ratio_slope_proxy(20d): -0.000125

### Volume (if available)

- volume: 14110637.00
- volume_MA20: 39611041.85
- volume_ratio: 0.36

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

- close: 14.32
- MA20 / MA60 / MA200: 14.68 / 13.46 / 11.65
- gap20 / gap60: -2.39% / 6.45%
- 5D return: -7.34%
- 20D high/low: 15.76 / 14.03

### Relative Strength

- ratio: 0.053367
- ratio_MA60: 0.050568
- ratio_gap: 5.53%
- ratio_slope_proxy(20d): 0.000032

### Volume (if available)

- volume: 2817562.00
- volume_MA20: 13198368.10
- volume_ratio: 0.21

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

- 데이터 기준일(주가): **2026-09-17**
- 실행시간(UTC): **2026-09-17 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -3.0 bp / latest 2.7
- IG OAS 4주 변화: -3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.62
- VIX: 17.71
- NFCI: -0.56

### Leadership ratios
- SILJ/SLV gap: 2.34% / slope_proxy: 0.024669
- GDXJ/GLD gap: 8.36% / slope_proxy: 0.013781

## VZLA (Vizsla Silver)
- close: 3.9273 | RSI14: 52.613285 | ATR14%: 5.38%
- MA20 gap: -1.22% | MA50 gap: 8.24% | MA200 gap: -2.85%
- vol_ratio(Volume/Vol20): 0.229796 | gap_open: 4.34%
- RS vs SILJ gap: 2.55% / slope_proxy: -0.000273
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
- close: 8.87 | RSI14: 47.788589 | ATR14%: 7.17%
- MA20 gap: -7.40% | MA50 gap: 8.30% | MA200 gap: -1.26%
- vol_ratio(Volume/Vol20): 0.394827 | gap_open: 6.02%
- SilverMarginGate: SI=66.25 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.09% / slope_proxy: 0.016502
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
- close: 21.360001 | RSI14: 43.211932 | ATR14%: 7.83%
- MA20 gap: -8.23% | MA50 gap: -6.54% | MA200 gap: -29.60%
- vol_ratio(Volume/Vol20): 0.487609 | gap_open: 6.51%
- RS vs SILJ gap: -13.29% / slope_proxy: -0.083967
- RS vs GDXJ gap: -16.03% / slope_proxy: -0.026165
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

- 실행시간(UTC): **2026-09-17 15:01:21**
- 데이터 기준일(주가): **2026-09-17**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA**

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

- HY OAS: 2.70 / 4주 변화 -0.03 bp-ish / 2026-09-16
- IG OAS: 0.78 / 4주 변화 -0.03 bp-ish / 2026-09-16
- 10Y Real Yield: 2.62 / 4주 변화 0.18 bp-ish / 2026-09-15
- VIX: 17.71 / 4주 변화 2.82 / 2026-09-16
- NFCI: -0.56 / 4주 변화 -0.07 / 2026-09-11

### Leadership ratios

- GDX/GLD: gap 9.47% / slope_proxy -0.19%
- GDXJ/GLD: gap 8.36% / slope_proxy -0.69%
- SILJ/SLV: gap 2.34% / slope_proxy -1.05%
- Gold breadth proxy: above50 100.00%, above200 69.23%, count 13
- Silver breadth proxy: above50 84.62%, above200 23.08%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.33 | RSI14: 42.18 | ATR14%: 4.90%
- MA20/50/200 gap: 0.28% / 14.97% / 35.81%
- 5D return: 5.19% | 20D drawdown: -6.68% | vol_ratio: 0.25
- RS vs GDXJ: gap 7.31% / slope_proxy 3.11%
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
- close: 7.71 | RSI14: 43.15 | ATR14%: 5.30%
- MA20/50/200 gap: -1.41% / 16.47% / 9.14%
- 5D return: -2.90% | 20D drawdown: -7.55% | vol_ratio: 0.21
- RS vs GDXJ: gap 9.90% / slope_proxy 8.32%
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
- close: 2.56 | RSI14: 41.33 | ATR14%: 6.78%
- MA20/50/200 gap: -1.99% / 14.51% / 30.90%
- 5D return: -0.39% | 20D drawdown: -8.24% | vol_ratio: 0.43
- RS vs GDXJ: gap 9.55% / slope_proxy 9.07%
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
- close: 1.45 | RSI14: 37.88 | ATR14%: 5.32%
- MA20/50/200 gap: -5.01% / 6.51% / -3.08%
- 5D return: -1.36% | 20D drawdown: -12.12% | vol_ratio: 0.21
- RS vs GDXJ: gap -1.42% / slope_proxy -7.90%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **46.8**
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
- close: 28.26 | RSI14: 46.04 | ATR14%: 6.46%
- MA20/50/200 gap: 1.23% / 14.99% / 48.82%
- 5D return: -0.56% | 20D drawdown: -5.45% | vol_ratio: 0.36
- RS vs SILJ: gap 11.82% / slope_proxy 10.46%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.93 | RSI14: 42.76 | ATR14%: 5.76%
- MA20/50/200 gap: -1.22% / 8.24% / -2.85%
- 5D return: -1.82% | 20D drawdown: -5.82% | vol_ratio: 0.23
- RS vs SILJ: gap 2.55% / slope_proxy 6.78%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **56.4**
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
- close: 9.98 | RSI14: 36.08 | ATR14%: 6.03%
- MA20/50/200 gap: -6.25% / 5.52% / 0.55%
- 5D return: -5.13% | 20D drawdown: -12.99% | vol_ratio: 0.28
- RS vs SILJ: gap 0.73% / slope_proxy -4.27%
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
- close: 18.92 | RSI14: 36.54 | ATR14%: 5.74%
- MA20/50/200 gap: -6.02% / 7.01% / -1.32%
- 5D return: -5.52% | 20D drawdown: -11.74% | vol_ratio: 0.18
- RS vs SILJ: gap 1.82% / slope_proxy -4.40%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.87 | RSI14: 39.89 | ATR14%: 7.83%
- MA20/50/200 gap: -7.40% / 8.30% / -1.26%
- 5D return: -8.46% | 20D drawdown: -14.96% | vol_ratio: 0.39
- RS vs SILJ: gap 5.09% / slope_proxy -4.37%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **48.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.03 | RSI14: 37.43 | ATR14%: 6.27%
- MA20/50/200 gap: -4.22% / 5.94% / -14.82%
- 5D return: -1.28% | 20D drawdown: -12.46% | vol_ratio: 0.41
- RS vs SILJ: gap -1.19% / slope_proxy 0.71%
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
- close: 6.26 | RSI14: 29.08 | ATR14%: 6.78%
- MA20/50/200 gap: -12.11% / -4.72% / -10.66%
- 5D return: -12.15% | 20D drawdown: -19.08% | vol_ratio: 0.30
- RS vs SILJ: gap -10.52% / slope_proxy -13.40%
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
- close: 21.36 | RSI14: 29.82 | ATR14%: 7.50%
- MA20/50/200 gap: -8.23% / -6.54% / -29.60%
- 5D return: -0.14% | 20D drawdown: -21.09% | vol_ratio: 0.49
- RS vs SILJ: gap -13.29% / slope_proxy -14.02%
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
