# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-21 03:01:10**
- 데이터 기준일(일봉): **2026-07-20**
- 데이터 기준일(주봉): **2026-07-20**
- VXN 기준일: **2026-07-17** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 696.06
- Weekly RSI14: **56.27**
- 52W MA: 629.06 / gap: **10.65%**
- 104W MA gap: **23.48%**
- 52W MA 13W slope: **7.88%**
- VXN: **29.03** / 5D change: 4.14

## Daily trigger: 실제 매수 타이밍

- QQQ close: 696.06
- Daily RSI14: **42.40**
- 20D gap: **-2.80%**
- 50D gap: **-3.13%**
- 200D gap: **8.76%**
- MACD hist: -3.2542 / change: -0.4399
- ATR14%: **2.15%**
- 20D high drawdown: **-5.68%**

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

- 데이터 기준일(주가): **2026-07-20**
- 실행시간(UTC): **2026-07-21 03:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.73 / 4주 변화 7.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.31 / 4주 변화 10.0 bp
- VIX (VIXCLS): 18.77
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.622897
- MA60: 9.627322
- gap: -0.05%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.348836
- MA60: 0.380559
- gap: -8.34%
- MA60_slope_proxy: 0.040396
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-20**
- 실행시간(UTC): **2026-07-21 03:00:48**

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
- TERM_SPREAD_10Y_POLICY: 121.48 bp / 4주 변화 24.35 bp
- CURVE_10s5s: 46.81 bp / 4주 변화 1.91 bp

## NWG Price
- close: 669.4
- MA50: 621.88 / gap50: 7.64%
- MA200: 606.769 / gap200: 10.32%

## Relative Strength
- RS vs FTSE gap: 7.26% / slope_proxy: 0.002266
- RS vs Peers gap: 1.08% / slope_proxy: -0.00415

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-21 03:00:54**

## Commodity Regime

- WTI ref (CL=F): 82.36 / 5D 5.40%
- Brent ref (BZ=F): 88.77 / 5D 6.57%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.41
- Gas ref (NG=F): 2.85 / 5D -1.66%

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

- close: 55.19
- MA20 / MA60 / MA200: 51.86 / 55.33 / 49.34
- gap20 / gap60: 6.43% / -0.25%
- 5D return: 0.69%
- 20D high/low: 55.19 / 47.94

### Relative Strength

- ratio: 0.952537
- ratio_MA60: 0.977850
- ratio_gap: -2.59%
- ratio_slope_proxy(20d): -0.028482

### Volume (if available)

- volume: 7858696.00
- volume_MA20: 9658734.80
- volume_ratio: 0.81

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.19
- MA20 / MA60 / MA200: 16.98 / 18.63 / 15.80
- gap20 / gap60: 7.11% / -2.37%
- 5D return: 1.73%
- 20D high/low: 18.19 / 15.99

### Relative Strength

- ratio: 0.512683
- ratio_MA60: 0.517769
- ratio_gap: -0.98%
- ratio_slope_proxy(20d): -0.012149

### Volume (if available)

- volume: 11991304.00
- volume_MA20: 14458450.20
- volume_ratio: 0.83

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.02
- MA20 / MA60 / MA200: 5.13 / 5.98 / 5.23
- gap20 / gap60: -2.14% / -16.02%
- 5D return: -6.52%
- 20D high/low: 5.41 / 4.87

### Relative Strength

- ratio: 0.013380
- ratio_MA60: 0.014443
- ratio_gap: -7.36%
- ratio_slope_proxy(20d): -0.000743

### Volume (if available)

- volume: 26657809.00
- volume_MA20: 37742195.45
- volume_ratio: 0.71

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

- close: 14.29
- MA20 / MA60 / MA200: 11.95 / 12.45 / 10.64
- gap20 / gap60: 19.56% / 14.80%
- 5D return: 6.96%
- 20D high/low: 14.29 / 10.51

### Relative Strength

- ratio: 0.053935
- ratio_MA60: 0.050565
- ratio_gap: 6.66%
- ratio_slope_proxy(20d): -0.001346

### Volume (if available)

- volume: 20419261.00
- volume_MA20: 13370118.05
- volume_ratio: 1.53

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-20**
- 실행시간(UTC): **2026-07-21 03:01:00**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 7.0 bp / latest 2.73
- IG OAS 4주 변화: 5.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 18.77
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 3.07% / slope_proxy: 0.008603
- GDXJ/GLD gap: -8.43% / slope_proxy: -0.007656

## VZLA (Vizsla Silver)
- close: 3.15 | RSI14: 45.760006 | ATR14%: 6.18%
- MA20 gap: -1.38% | MA50 gap: -8.49% | MA200 gap: -24.62%
- vol_ratio(Volume/Vol20): 0.700061 | gap_open: 0.65%
- RS vs SILJ gap: 8.63% / slope_proxy: 0.005779
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
- close: 6.01 | RSI14: 38.649306 | ATR14%: 7.32%
- MA20 gap: -6.87% | MA50 gap: -18.48% | MA200 gap: -29.04%
- vol_ratio(Volume/Vol20): 0.920286 | gap_open: 0.00%
- SilverMarginGate: SI=57.755001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.45% / slope_proxy: -0.006052
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
- close: 18.76 | RSI14: 33.440461 | ATR14%: 10.20%
- MA20 gap: -14.26% | MA50 gap: -33.41% | MA200 gap: -30.95%
- vol_ratio(Volume/Vol20): 0.523596 | gap_open: 1.52%
- RS vs SILJ gap: -23.89% / slope_proxy: -0.121844
- RS vs GDXJ gap: -23.71% / slope_proxy: -0.027083
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

- 실행시간(UTC): **2026-07-21 03:01:09**
- 데이터 기준일(주가): **2026-07-20**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA, HL**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.73 / 4주 변화 0.07 bp-ish / 2026-07-17
- IG OAS: 0.79 / 4주 변화 0.05 bp-ish / 2026-07-17
- 10Y Real Yield: 2.31 / 4주 변화 0.08 bp-ish / 2026-07-17
- VIX: 18.77 / 4주 변화 1.99 / 2026-07-17
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -7.34% / slope_proxy -9.12%
- GDXJ/GLD: gap -8.43% / slope_proxy -9.63%
- SILJ/SLV: gap 3.07% / slope_proxy -0.72%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.78 | RSI14: 65.52 | ATR14%: 8.19%
- MA20/50/200 gap: 3.58% / -2.89% / 0.44%
- 5D return: -11.00% | 20D drawdown: -13.59% | vol_ratio: 0.53
- RS vs GDXJ: gap 17.24% / slope_proxy 26.96%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **53.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.93 | RSI14: 41.83 | ATR14%: 5.63%
- MA20/50/200 gap: -6.89% / -11.40% / 1.80%
- 5D return: -4.28% | 20D drawdown: -14.66% | vol_ratio: 0.82
- RS vs GDXJ: gap 5.38% / slope_proxy -1.19%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **50.9**
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
- close: 4.95 | RSI14: 43.46 | ATR14%: 5.05%
- MA20/50/200 gap: -4.48% / -15.26% / -28.21%
- 5D return: -0.40% | 20D drawdown: -13.91% | vol_ratio: 0.44
- RS vs GDXJ: gap -1.66% / slope_proxy 0.88%
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
- close: 1.05 | RSI14: 40.38 | ATR14%: 7.11%
- MA20/50/200 gap: -9.44% / -17.83% / -29.98%
- 5D return: -4.55% | 20D drawdown: -19.85% | vol_ratio: 0.32
- RS vs GDXJ: gap -2.75% / slope_proxy -7.65%
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
- close: 18.44 | RSI14: 47.83 | ATR14%: 6.88%
- MA20/50/200 gap: -3.57% / -3.42% / 15.58%
- 5D return: -3.56% | 20D drawdown: -9.21% | vol_ratio: 1.08
- RS vs SILJ: gap 15.58% / slope_proxy 8.73%
- FundamentalScore: 86 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **64.0**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.29 | RSI14: 39.31 | ATR14%: 5.78%
- MA20/50/200 gap: -6.93% / -12.96% / -21.48%
- 5D return: -6.30% | 20D drawdown: -13.18% | vol_ratio: 2.24
- RS vs SILJ: gap 1.72% / slope_proxy 4.08%
- FundamentalScore: 78 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **60.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.50 | RSI14: 38.19 | ATR14%: 6.32%
- MA20/50/200 gap: -6.77% / -15.29% / -21.59%
- 5D return: -4.34% | 20D drawdown: -12.38% | vol_ratio: 1.24
- RS vs SILJ: gap -0.00% / slope_proxy 2.10%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.15 | RSI14: 45.24 | ATR14%: 5.90%
- MA20/50/200 gap: -1.38% / -8.49% / -24.62%
- 5D return: 4.30% | 20D drawdown: -10.51% | vol_ratio: 0.70
- RS vs SILJ: gap 8.63% / slope_proxy 4.16%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **52.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.57 | RSI14: 37.41 | ATR14%: 6.99%
- MA20/50/200 gap: -7.40% / -14.19% / -16.13%
- 5D return: -2.96% | 20D drawdown: -15.35% | vol_ratio: 0.79
- RS vs SILJ: gap 1.63% / slope_proxy 0.98%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **47.0**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.01 | RSI14: 39.75 | ATR14%: 6.54%
- MA20/50/200 gap: -6.87% / -18.48% / -29.04%
- 5D return: -5.35% | 20D drawdown: -14.87% | vol_ratio: 0.92
- RS vs SILJ: gap -4.45% / slope_proxy -0.92%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **44.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.76 | RSI14: 29.15 | ATR14%: 8.39%
- MA20/50/200 gap: -15.70% / -29.45% / -34.42%
- 5D return: -6.93% | 20D drawdown: -29.46% | vol_ratio: 0.85
- RS vs SILJ: gap -16.97% / slope_proxy -17.89%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **41.9**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 18.76 | RSI14: 30.54 | ATR14%: 9.00%
- MA20/50/200 gap: -14.26% / -33.41% / -30.95%
- 5D return: -8.17% | 20D drawdown: -25.11% | vol_ratio: 0.52
- RS vs SILJ: gap -23.89% / slope_proxy -12.83%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **30.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
