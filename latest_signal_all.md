# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: JAG.TO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-21 15:03:07**
- 데이터 기준일(일봉): **2026-07-21**
- 데이터 기준일(주봉): **2026-07-20**
- VXN 기준일: **2026-07-20** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 705.97
- Weekly RSI14: **58.13**
- 52W MA: 629.25 / gap: **12.19%**
- 104W MA gap: **25.22%**
- 52W MA 13W slope: **7.91%**
- VXN: **28.53** / 5D change: 1.23

## Daily trigger: 실제 매수 타이밍

- QQQ close: 705.98
- Daily RSI14: **46.89**
- 20D gap: **-1.20%**
- 50D gap: **-1.78%**
- 200D gap: **10.22%**
- MACD hist: -2.7271 / change: 0.5271
- ATR14%: **2.08%**
- 20D high drawdown: **-4.13%**

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

- 데이터 기준일(주가): **2026-07-21**
- 실행시간(UTC): **2026-07-21 15:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 4.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.31 / 4주 변화 10.0 bp
- VIX (VIXCLS): 18.65
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.822964
- MA60: 9.638607
- gap: 1.91%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.357389
- MA60: 0.380791
- gap: -6.15%
- MA60_slope_proxy: 0.037068
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-21**
- 실행시간(UTC): **2026-07-21 15:00:46**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- BoE IUDBEDR failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE IUDSOIA failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE IUDMNPY failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE IUDSNPY failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE LPMVTVX failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE LPMVQJW failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: None bp / 4주 변화 None bp
- CURVE_10s5s: None bp / 4주 변화 None bp

## NWG Price
- close: 674.367
- MA50: 625.4513 / gap50: 7.82%
- MA200: 608.0909 / gap200: 10.90%

## Relative Strength
- RS vs FTSE gap: 7.95% / slope_proxy: 0.0022
- RS vs Peers gap: 1.19% / slope_proxy: -0.003712

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-21 15:02:48**

## Commodity Regime

- WTI ref (CL=F): 84.43 / 5D 6.42%
- Brent ref (BZ=F): 91.33 / 5D 7.79%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.90
- Gas ref (NG=F): 2.86 / 5D -1.55%

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

- close: 56.06
- MA20 / MA60 / MA200: 52.06 / 55.30 / 49.39
- gap20 / gap60: 7.68% / 1.37%
- 5D return: 2.73%
- 20D high/low: 56.06 / 47.94

### Relative Strength

- ratio: 0.963313
- ratio_MA60: 0.976946
- ratio_gap: -1.40%
- ratio_slope_proxy(20d): -0.028355

### Volume (if available)

- volume: 2059884.00
- volume_MA20: 9302209.20
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.38
- MA20 / MA60 / MA200: 17.05 / 18.59 / 15.83
- gap20 / gap60: 7.80% / -1.12%
- 5D return: 2.57%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.520385
- ratio_MA60: 0.517635
- ratio_gap: 0.53%
- ratio_slope_proxy(20d): -0.011791

### Volume (if available)

- volume: 3688167.00
- volume_MA20: 14035198.35
- volume_ratio: 0.26

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

- close: 5.15
- MA20 / MA60 / MA200: 5.12 / 5.96 / 5.24
- gap20 / gap60: 0.64% / -13.63%
- 5D return: -3.01%
- 20D high/low: 5.37 / 4.87

### Relative Strength

- ratio: 0.013598
- ratio_MA60: 0.014432
- ratio_gap: -5.78%
- ratio_slope_proxy(20d): -0.000709

### Volume (if available)

- volume: 9879134.00
- volume_MA20: 36692056.70
- volume_ratio: 0.27

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

- close: 14.09
- MA20 / MA60 / MA200: 12.09 / 12.47 / 10.64
- gap20 / gap60: 16.54% / 13.06%
- 5D return: 6.54%
- 20D high/low: 14.29 / 10.51

### Relative Strength

- ratio: 0.053949
- ratio_MA60: 0.050624
- ratio_gap: 6.57%
- ratio_slope_proxy(20d): -0.001120

### Volume (if available)

- volume: 4378994.00
- volume_MA20: 12979394.70
- volume_ratio: 0.34

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

- 데이터 기준일(주가): **2026-07-21**
- 실행시간(UTC): **2026-07-21 15:02:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 4.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 18.65
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 1.92% / slope_proxy: 0.008293
- GDXJ/GLD gap: -5.84% / slope_proxy: -0.00817

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 49.882599 | ATR14%: 5.95%
- MA20 gap: 2.33% | MA50 gap: -5.35% | MA200 gap: -22.00%
- vol_ratio(Volume/Vol20): 0.334767 | gap_open: 3.49%
- RS vs SILJ gap: 8.13% / slope_proxy: 0.005961
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
- close: 6.385 | RSI14: 45.787228 | ATR14%: 6.85%
- MA20 gap: -0.54% | MA50 gap: -12.82% | MA200 gap: -24.55%
- vol_ratio(Volume/Vol20): 0.347768 | gap_open: 4.99%
- SilverMarginGate: SI=59.330002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.75% / slope_proxy: -0.005962
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
- close: 19.955 | RSI14: 38.77764 | ATR14%: 9.40%
- MA20 gap: -7.72% | MA50 gap: -28.21% | MA200 gap: -26.73%
- vol_ratio(Volume/Vol20): 0.231711 | gap_open: 3.04%
- RS vs SILJ gap: -21.21% / slope_proxy: -0.123885
- RS vs GDXJ gap: -21.68% / slope_proxy: -0.027638
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

- 실행시간(UTC): **2026-07-21 15:03:06**
- 데이터 기준일(주가): **2026-07-21**

## Verdict
**🟡 Precious miners watch/add-on candidates: JAG.TO, AYA, EXK, HL**

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

- HY OAS: 2.69 / 4주 변화 0.04 bp-ish / 2026-07-20
- IG OAS: 0.78 / 4주 변화 0.04 bp-ish / 2026-07-20
- 10Y Real Yield: 2.31 / 4주 변화 0.08 bp-ish / 2026-07-17
- VIX: 18.65 / 4주 변화 1.37 / 2026-07-20
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -5.25% / slope_proxy -4.52%
- GDXJ/GLD: gap -5.82% / slope_proxy -3.93%
- SILJ/SLV: gap 1.94% / slope_proxy -1.39%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.25 | RSI14: 51.83 | ATR14%: 5.12%
- MA20/50/200 gap: 1.62% / -9.56% / -23.81%
- 5D return: 5.63% | 20D drawdown: -8.70% | vol_ratio: 0.38
- RS vs GDXJ: gap 0.18% / slope_proxy 4.84%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **56.9**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.88 | RSI14: 65.52 | ATR14%: 7.71%
- MA20/50/200 gap: 8.42% / 2.55% / 5.72%
- 5D return: -4.57% | 20D drawdown: -8.74% | vol_ratio: 0.08
- RS vs GDXJ: gap 18.13% / slope_proxy 32.95%
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
- close: 7.07 | RSI14: 45.49 | ATR14%: 5.42%
- MA20/50/200 gap: -4.39% / -9.51% / 3.70%
- 5D return: -4.14% | 20D drawdown: -10.68% | vol_ratio: 0.24
- RS vs GDXJ: gap 2.76% / slope_proxy -3.59%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.09 | RSI14: 44.64 | ATR14%: 6.45%
- MA20/50/200 gap: -5.09% / -14.20% / -27.21%
- 5D return: -0.91% | 20D drawdown: -16.15% | vol_ratio: 0.27
- RS vs GDXJ: gap -3.27% / slope_proxy -7.62%
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
- close: 18.86 | RSI14: 49.49 | ATR14%: 6.73%
- MA20/50/200 gap: -1.15% / -1.24% / 17.97%
- 5D return: -5.89% | 20D drawdown: -7.14% | vol_ratio: 0.22
- RS vs SILJ: gap 13.68% / slope_proxy 9.81%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **74.5**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.86 | RSI14: 43.74 | ATR14%: 6.02%
- MA20/50/200 gap: -1.94% / -10.82% / -17.88%
- 5D return: -2.78% | 20D drawdown: -8.24% | vol_ratio: 0.29
- RS vs SILJ: gap 1.17% / slope_proxy 3.98%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **56.9**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.94 | RSI14: 45.74 | ATR14%: 5.59%
- MA20/50/200 gap: -2.40% / -8.68% / -17.99%
- 5D return: -3.65% | 20D drawdown: -9.26% | vol_ratio: 0.17
- RS vs SILJ: gap 2.74% / slope_proxy 5.08%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **55.1**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.26 | RSI14: 48.31 | ATR14%: 5.78%
- MA20/50/200 gap: 2.33% / -5.35% / -22.00%
- 5D return: 1.72% | 20D drawdown: -2.84% | vol_ratio: 0.33
- RS vs SILJ: gap 8.13% / slope_proxy 3.02%
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
- close: 5.86 | RSI14: 42.10 | ATR14%: 6.68%
- MA20/50/200 gap: -2.04% / -9.36% / -11.72%
- 5D return: -1.92% | 20D drawdown: -10.87% | vol_ratio: 0.43
- RS vs SILJ: gap 3.36% / slope_proxy 5.76%
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
- close: 6.39 | RSI14: 48.12 | ATR14%: 6.29%
- MA20/50/200 gap: -0.54% / -12.82% / -24.55%
- 5D return: -1.77% | 20D drawdown: -6.24% | vol_ratio: 0.35
- RS vs SILJ: gap -1.75% / slope_proxy 2.26%
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
- close: 3.99 | RSI14: 34.98 | ATR14%: 7.88%
- MA20/50/200 gap: -9.18% / -24.46% / -30.42%
- 5D return: -5.00% | 20D drawdown: -18.57% | vol_ratio: 0.26
- RS vs SILJ: gap -14.61% / slope_proxy -13.66%
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
- close: 19.95 | RSI14: 36.80 | ATR14%: 8.55%
- MA20/50/200 gap: -7.72% / -28.21% / -26.73%
- 5D return: -8.71% | 20D drawdown: -15.94% | vol_ratio: 0.23
- RS vs SILJ: gap -21.21% / slope_proxy -8.57%
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
