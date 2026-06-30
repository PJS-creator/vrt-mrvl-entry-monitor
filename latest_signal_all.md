# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-30 03:01:30**
- 데이터 기준일(일봉): **2026-06-29**
- 데이터 기준일(주봉): **2026-06-29**
- VXN 기준일: **2026-06-26** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 724.08
- Weekly RSI14: **63.79**
- 52W MA: 620.70 / gap: **16.66%**
- 104W MA gap: **29.99%**
- 52W MA 13W slope: **8.45%**
- VXN: **30.82** / 5D change: 4.51

## Daily trigger: 실제 매수 타이밍

- QQQ close: 724.08
- Daily RSI14: **52.98**
- 20D gap: **0.08%**
- 50D gap: **2.88%**
- 200D gap: **14.68%**
- MACD hist: -3.1130 / change: 0.8698
- ATR14%: **2.29%**
- 20D high drawdown: **-2.85%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-29**
- 실행시간(UTC): **2026-06-30 03:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.83 / 4주 변화 11.0 bp
- IG OAS (BAMLC0A0CM): 0.77 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.18 / 4주 변화 11.0 bp
- VIX (VIXCLS): 18.41
- NFCI: -0.516

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.451047
- MA60: 9.320023
- gap: 1.41%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.439492
- MA60: 0.359321
- gap: 22.31%
- MA60_slope_proxy: 0.073024
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-29**
- 실행시간(UTC): **2026-06-30 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 93.2 bp / 4주 변화 -10.67 bp
- CURVE_10s5s: 45.45 bp / 4주 변화 -0.25 bp

## NWG Price
- close: 656.2
- MA50: 597.9651 / gap50: 9.74%
- MA200: 596.4555 / gap200: 10.02%

## Relative Strength
- RS vs FTSE gap: 8.87% / slope_proxy: 0.001649
- RS vs Peers gap: 2.70% / slope_proxy: -0.014763

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-30 03:00:59**

## Commodity Regime

- WTI ref (CL=F): 70.50 / 5D -5.77%
- Brent ref (BZ=F): 73.72 / 5D -5.37%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.22
- Gas ref (NG=F): 3.17 / 5D -2.46%

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

- close: 49.09
- MA20 / MA60 / MA200: 54.66 / 56.62 / 48.91
- gap20 / gap60: -10.18% / -13.30%
- 5D return: -5.60%
- 20D high/low: 59.37 / 49.09

### Relative Strength

- ratio: 0.916200
- ratio_MA60: 0.995550
- ratio_gap: -7.97%
- ratio_slope_proxy(20d): -0.011475

### Volume (if available)

- volume: 9610679.00
- volume_MA20: 9905018.95
- volume_ratio: 0.97

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.28
- MA20 / MA60 / MA200: 17.46 / 19.45 / 15.49
- gap20 / gap60: -6.73% / -16.28%
- 5D return: -4.29%
- 20D high/low: 18.72 / 16.28

### Relative Strength

- ratio: 0.471201
- ratio_MA60: 0.523941
- ratio_gap: -10.07%
- ratio_slope_proxy(20d): -0.004285

### Volume (if available)

- volume: 8325732.00
- volume_MA20: 14353186.60
- volume_ratio: 0.58

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.04
- MA20 / MA60 / MA200: 5.72 / 6.27 / 5.11
- gap20 / gap60: -11.90% / -19.59%
- 5D return: -6.84%
- 20D high/low: 6.25 / 5.04

### Relative Strength

- ratio: 0.013513
- ratio_MA60: 0.014900
- ratio_gap: -9.31%
- ratio_slope_proxy(20d): -0.000806

### Volume (if available)

- volume: 36369084.00
- volume_MA20: 31614439.20
- volume_ratio: 1.15

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

- close: 11.15
- MA20 / MA60 / MA200: 11.93 / 12.63 / 10.76
- gap20 / gap60: -6.52% / -11.73%
- 5D return: -0.98%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045702
- ratio_MA60: 0.050864
- ratio_gap: -10.15%
- ratio_slope_proxy(20d): -0.000811

### Volume (if available)

- volume: 9487949.00
- volume_MA20: 13966097.45
- volume_ratio: 0.68

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

- 데이터 기준일(주가): **2026-06-29**
- 실행시간(UTC): **2026-06-30 03:01:14**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 11.0 bp / latest 2.83
- IG OAS 4주 변화: 4.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 11.0 bp / latest 2.18
- VIX: 18.41
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 9.47% / slope_proxy: 0.006258
- GDXJ/GLD gap: -3.98% / slope_proxy: -0.001719

## VZLA (Vizsla Silver)
- close: 3.27 | RSI14: 43.463179 | ATR14%: 6.65%
- MA20 gap: -7.10% | MA50 gap: -6.89% | MA200 gap: -22.85%
- vol_ratio(Volume/Vol20): 0.464417 | gap_open: 0.91%
- RS vs SILJ gap: 7.66% / slope_proxy: 0.004565
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
- close: 6.51 | RSI14: 40.563107 | ATR14%: 8.30%
- MA20 gap: -6.85% | MA50 gap: -17.90% | MA200 gap: -23.56%
- vol_ratio(Volume/Vol20): 0.510439 | gap_open: 1.06%
- SilverMarginGate: SI=57.830002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.08% / slope_proxy: -0.009486
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
- close: 23.379999 | RSI14: 37.419954 | ATR14%: 10.06%
- MA20 gap: -11.03% | MA50 gap: -29.08% | MA200 gap: -10.46%
- vol_ratio(Volume/Vol20): 0.696631 | gap_open: 4.04%
- RS vs SILJ gap: -19.97% / slope_proxy: -0.078905
- RS vs GDXJ gap: -18.33% / slope_proxy: -0.016661
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

- 실행시간(UTC): **2026-06-30 03:01:27**
- 데이터 기준일(주가): **2026-06-29**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

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

- HY OAS: 2.83 / 4주 변화 0.09 bp-ish / 2026-06-26
- IG OAS: 0.77 / 4주 변화 0.03 bp-ish / 2026-06-26
- 10Y Real Yield: 2.18 / 4주 변화 0.12 bp-ish / 2026-06-26
- VIX: 18.41 / 4주 변화 3.09 / 2026-06-26
- NFCI: -0.52 / 4주 변화 0.05 / 2026-06-19

### Leadership ratios

- GDX/GLD: gap -3.59% / slope_proxy -2.58%
- GDXJ/GLD: gap -3.98% / slope_proxy -3.98%
- SILJ/SLV: gap 9.47% / slope_proxy 8.62%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.36 | RSI14: 49.44 | ATR14%: 6.50%
- MA20/50/200 gap: -5.04% / -6.95% / 10.77%
- 5D return: -9.36% | 20D drawdown: -13.92% | vol_ratio: 0.54
- RS vs GDXJ: gap 10.46% / slope_proxy 0.62%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **59.6**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.20 | RSI14: 45.49 | ATR14%: 6.37%
- MA20/50/200 gap: -7.88% / -17.50% / -25.02%
- 5D return: -6.47% | 20D drawdown: -23.98% | vol_ratio: 0.67
- RS vs GDXJ: gap -5.74% / slope_proxy -14.29%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **48.1**
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
- close: 1.15 | RSI14: 48.72 | ATR14%: 8.20%
- MA20/50/200 gap: -9.13% / -13.97% / -23.57%
- 5D return: -12.21% | 20D drawdown: -21.77% | vol_ratio: 2.36
- RS vs GDXJ: gap -1.32% / slope_proxy -2.46%
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
- close: 1.51 | RSI14: 42.86 | ATR14%: 6.29%
- MA20/50/200 gap: -8.21% / -16.75% / -10.53%
- 5D return: -3.82% | 20D drawdown: -23.35% | vol_ratio: 1.90
- RS vs GDXJ: gap -2.55% / slope_proxy -8.61%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.77 | RSI14: 54.48 | ATR14%: 8.08%
- MA20/50/200 gap: -0.84% / 0.94% / 21.96%
- 5D return: -4.91% | 20D drawdown: -12.66% | vol_ratio: 0.77
- RS vs SILJ: gap 17.45% / slope_proxy 7.55%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 55 | OverallScore: **79.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.40 | RSI14: 53.69 | ATR14%: 6.06%
- MA20/50/200 gap: -2.04% / -10.61% / -14.04%
- 5D return: -3.63% | 20D drawdown: -13.48% | vol_ratio: 0.79
- RS vs SILJ: gap 0.94% / slope_proxy 3.83%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **60.1**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.23 | RSI14: 51.98 | ATR14%: 7.06%
- MA20/50/200 gap: -3.62% / -11.01% / -13.34%
- 5D return: -3.74% | 20D drawdown: -16.45% | vol_ratio: 0.71
- RS vs SILJ: gap 1.70% / slope_proxy -0.38%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **53.1**
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.27 | RSI14: 53.71 | ATR14%: 7.46%
- MA20/50/200 gap: -1.37% / -6.65% / -4.25%
- 5D return: -2.34% | 20D drawdown: -15.50% | vol_ratio: 0.78
- RS vs SILJ: gap 6.75% / slope_proxy 1.72%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **52.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.51 | RSI14: 51.99 | ATR14%: 8.25%
- MA20/50/200 gap: -6.85% / -17.90% / -23.56%
- 5D return: -7.79% | 20D drawdown: -21.85% | vol_ratio: 0.51
- RS vs SILJ: gap -6.08% / slope_proxy -5.42%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **49.6**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.27 | RSI14: 44.30 | ATR14%: 6.47%
- MA20/50/200 gap: -7.10% / -6.89% / -22.85%
- 5D return: -7.10% | 20D drawdown: -20.82% | vol_ratio: 0.46
- RS vs SILJ: gap 7.66% / slope_proxy -4.51%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **48.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.69 | RSI14: 46.02 | ATR14%: 8.88%
- MA20/50/200 gap: -11.22% / -19.13% / -17.01%
- 5D return: -12.01% | 20D drawdown: -27.06% | vol_ratio: 0.91
- RS vs SILJ: gap -6.67% / slope_proxy -11.26%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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
- close: 23.38 | RSI14: 41.63 | ATR14%: 9.23%
- MA20/50/200 gap: -11.03% / -29.08% / -10.46%
- 5D return: -6.67% | 20D drawdown: -30.87% | vol_ratio: 0.70
- RS vs SILJ: gap -19.97% / slope_proxy -15.80%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **35.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
