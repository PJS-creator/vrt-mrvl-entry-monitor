# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-14 03:01:13**
- 데이터 기준일(일봉): **2026-07-13**
- 데이터 기준일(주봉): **2026-07-13**
- VXN 기준일: **2026-07-10** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 711.74
- Weekly RSI14: **60.26**
- 52W MA: 626.83 / gap: **13.55%**
- 104W MA gap: **26.74%**
- 52W MA 13W slope: **8.18%**
- VXN: **24.89** / 5D change: -3.09

## Daily trigger: 실제 매수 타이밍

- QQQ close: 711.74
- Daily RSI14: **47.83**
- 20D gap: **-1.43%**
- 50D gap: **-0.54%**
- 200D gap: **11.70%**
- MACD hist: -1.5894 / change: -0.4203
- ATR14%: **2.16%**
- 20D high drawdown: **-4.23%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-13**
- 실행시간(UTC): **2026-07-14 03:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.77 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.32 / 4주 변화 15.0 bp
- VIX (VIXCLS): 15.03
- NFCI: -0.515

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.876332
- MA60: 9.550973
- gap: 3.41%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.371452
- MA60: 0.377718
- gap: -1.66%
- MA60_slope_proxy: 0.057115
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-13**
- 실행시간(UTC): **2026-07-14 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 114.2 bp / 4주 변화 1.16 bp
- CURVE_10s5s: 48.45 bp / 4주 변화 3.79 bp

## NWG Price
- close: 662.4
- MA50: 612.7171 / gap50: 8.11%
- MA200: 603.2178 / gap200: 9.81%

## Relative Strength
- RS vs FTSE gap: 7.95% / slope_proxy: 0.002372
- RS vs Peers gap: 0.95% / slope_proxy: -0.00717

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-14 03:00:58**

## Commodity Regime

- WTI ref (CL=F): 79.45 / 5D 15.90%
- Brent ref (BZ=F): 84.34 / 5D 17.16%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.89
- Gas ref (NG=F): 2.89 / 5D -10.82%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **False**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **False**
- **BRAZIL_RISK_OK**: **True**

## OXY

- **ENTRY**: **False**

### Trend

- close: 54.81
- MA20 / MA60 / MA200: 51.73 / 55.41 / 49.15
- gap20 / gap60: 5.95% / -1.09%
- 5D return: 12.29%
- 20D high/low: 56.54 / 47.94

### Relative Strength

- ratio: 0.965985
- ratio_MA60: 0.981979
- ratio_gap: -1.63%
- ratio_slope_proxy(20d): -0.027289

### Volume (if available)

- volume: 12725416.00
- volume_MA20: 10190530.80
- volume_ratio: 1.25

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.88
- MA20 / MA60 / MA200: 16.83 / 18.87 / 15.67
- gap20 / gap60: 6.26% / -5.24%
- 5D return: 9.96%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.505227
- ratio_MA60: 0.518362
- ratio_gap: -2.53%
- ratio_slope_proxy(20d): -0.014232

### Volume (if available)

- volume: 20368497.00
- volume_MA20: 15674304.85
- volume_ratio: 1.30

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.37
- MA20 / MA60 / MA200: 5.26 / 6.05 / 5.18
- gap20 / gap60: 2.13% / -11.28%
- 5D return: 8.92%
- 20D high/low: 6.04 / 4.87

### Relative Strength

- ratio: 0.014025
- ratio_MA60: 0.014553
- ratio_gap: -3.63%
- ratio_slope_proxy(20d): -0.000826

### Volume (if available)

- volume: 43455853.00
- volume_MA20: 37944507.65
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

- close: 13.36
- MA20 / MA60 / MA200: 11.50 / 12.33 / 10.67
- gap20 / gap60: 16.14% / 8.34%
- 5D return: 23.13%
- 20D high/low: 13.36 / 10.51

### Relative Strength

- ratio: 0.050743
- ratio_MA60: 0.050208
- ratio_gap: 1.07%
- ratio_slope_proxy(20d): -0.002140

### Volume (if available)

- volume: 20109673.00
- volume_MA20: 14036683.65
- volume_ratio: 1.43

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-13**
- 실행시간(UTC): **2026-07-14 03:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.69
- IG OAS 4주 변화: 3.0 bp / latest 0.77
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.32
- VIX: 15.03
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.28% / slope_proxy: 0.009193
- GDXJ/GLD gap: -5.65% / slope_proxy: -0.003129

## VZLA (Vizsla Silver)
- close: 3.02 | RSI14: 39.592099 | ATR14%: 6.73%
- MA20 gap: -8.83% | MA50 gap: -12.88% | MA200 gap: -28.19%
- vol_ratio(Volume/Vol20): 1.257862 | gap_open: 1.60%
- RS vs SILJ gap: 1.54% / slope_proxy: 0.005095
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
- close: 6.35 | RSI14: 41.667104 | ATR14%: 7.43%
- MA20 gap: -6.22% | MA50 gap: -16.07% | MA200 gap: -25.34%
- vol_ratio(Volume/Vol20): 0.674395 | gap_open: 2.77%
- SilverMarginGate: SI=57.860001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.82% / slope_proxy: -0.004893
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
- close: 20.43 | RSI14: 33.207415 | ATR14%: 9.81%
- MA20 gap: -13.13% | MA50 gap: -31.72% | MA200 gap: -23.85%
- vol_ratio(Volume/Vol20): 0.700475 | gap_open: 1.96%
- RS vs SILJ gap: -23.38% / slope_proxy: -0.101767
- RS vs GDXJ gap: -22.94% / slope_proxy: -0.022159
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

- 실행시간(UTC): **2026-07-14 03:01:12**
- 데이터 기준일(주가): **2026-07-13**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

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

- HY OAS: 2.69 / 4주 변화 -0.02 bp-ish / 2026-07-10
- IG OAS: 0.77 / 4주 변화 0.03 bp-ish / 2026-07-10
- 10Y Real Yield: 2.32 / 4주 변화 0.11 bp-ish / 2026-07-10
- VIX: 15.03 / 4주 변화 -2.65 / 2026-07-10
- NFCI: -0.52 / 4주 변화 0.03 / 2026-07-03

### Leadership ratios

- GDX/GLD: gap -4.72% / slope_proxy -3.47%
- GDXJ/GLD: gap -5.65% / slope_proxy -3.66%
- SILJ/SLV: gap 5.28% / slope_proxy 6.74%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.24 | RSI14: 35.53 | ATR14%: 5.66%
- MA20/50/200 gap: -5.78% / -8.05% / 7.05%
- 5D return: -8.47% | 20D drawdown: -13.71% | vol_ratio: 1.56
- RS vs GDXJ: gap 7.36% / slope_proxy 4.25%
- FundamentalScore: 88 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **64.8**
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.00 | RSI14: 75.29 | ATR14%: 6.29%
- MA20/50/200 gap: 19.47% / 10.08% / 14.83%
- 5D return: 17.65% | 20D drawdown: -2.91% | vol_ratio: 2.15
- RS vs GDXJ: gap 29.61% / slope_proxy 35.84%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **53.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 4.97 | RSI14: 38.15 | ATR14%: 5.49%
- MA20/50/200 gap: -8.22% / -17.23% / -28.16%
- 5D return: -11.57% | 20D drawdown: -19.19% | vol_ratio: 0.76
- RS vs GDXJ: gap -5.83% / slope_proxy -2.30%
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
- close: 1.10 | RSI14: 34.33 | ATR14%: 7.60%
- MA20/50/200 gap: -10.86% / -15.79% / -27.04%
- 5D return: -12.00% | 20D drawdown: -25.17% | vol_ratio: 0.76
- RS vs GDXJ: gap -1.92% / slope_proxy -3.68%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **42.8**
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 19.12 | RSI14: 47.29 | ATR14%: 7.11%
- MA20/50/200 gap: -1.24% / 0.86% / 21.45%
- 5D return: -4.16% | 20D drawdown: -9.17% | vol_ratio: 0.54
- RS vs SILJ: gap 18.52% / slope_proxy 12.50%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.84 | RSI14: 40.27 | ATR14%: 6.36%
- MA20/50/200 gap: -6.07% / -12.83% / -18.04%
- 5D return: -7.87% | 20D drawdown: -15.70% | vol_ratio: 0.85
- RS vs SILJ: gap 0.68% / slope_proxy 0.47%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **61.9**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.25 | RSI14: 44.25 | ATR14%: 5.59%
- MA20/50/200 gap: -2.76% / -8.75% / -15.83%
- 5D return: -7.35% | 20D drawdown: -8.79% | vol_ratio: 0.72
- RS vs SILJ: gap 4.53% / slope_proxy 9.80%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.02 | RSI14: 32.88 | ATR14%: 6.35%
- MA20/50/200 gap: -8.83% / -12.88% / -28.19%
- 5D return: -7.65% | 20D drawdown: -18.16% | vol_ratio: 1.26
- RS vs SILJ: gap 1.54% / slope_proxy -7.39%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **53.9**
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.35 | RSI14: 37.18 | ATR14%: 6.30%
- MA20/50/200 gap: -6.22% / -16.07% / -25.34%
- 5D return: -6.75% | 20D drawdown: -20.33% | vol_ratio: 0.67
- RS vs SILJ: gap -3.82% / slope_proxy 0.15%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.04 | RSI14: 26.02 | ATR14%: 8.46%
- MA20/50/200 gap: -17.33% / -26.93% / -29.40%
- 5D return: -17.21% | 20D drawdown: -31.29% | vol_ratio: 0.88
- RS vs SILJ: gap -15.68% / slope_proxy -15.77%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.74 | RSI14: 40.00 | ATR14%: 7.16%
- MA20/50/200 gap: -8.42% / -12.62% / -13.34%
- 5D return: -12.77% | 20D drawdown: -17.41% | vol_ratio: 0.80
- RS vs SILJ: gap 0.78% / slope_proxy -1.11%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **43.2**
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 20.43 | RSI14: 30.52 | ATR14%: 8.47%
- MA20/50/200 gap: -13.13% / -31.72% / -23.85%
- 5D return: -13.03% | 20D drawdown: -26.62% | vol_ratio: 0.70
- RS vs SILJ: gap -23.38% / slope_proxy -12.69%
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
