# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-23 15:01:23**
- 데이터 기준일(일봉): **2026-10-23**
- 데이터 기준일(주봉): **2026-10-19**
- VXN 기준일: **2026-10-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 708.08
- Weekly RSI14: **51.56**
- 52W MA: 662.90 / gap: **6.81%**
- 104W MA gap: **19.14%**
- 52W MA 13W slope: **5.53%**
- VXN: **28.72** / 5D change: 5.83

## Daily trigger: 실제 매수 타이밍

- QQQ close: 708.08
- Daily RSI14: **38.97**
- 20D gap: **-3.72%**
- 50D gap: **-2.40%**
- 200D gap: **4.73%**
- MACD hist: -4.9337 / change: 0.0469
- ATR14%: **1.63%**
- 20D high drawdown: **-6.79%**

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

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-23 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.4 / 4주 변화 60.0 bp
- IG OAS (BAMLC0A0CM): 0.89 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.76 / 4주 변화 0.0 bp
- VIX (VIXCLS): 19.03
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.046236
- MA60: 8.440899
- gap: -16.52%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.433399
- MA60: 0.412975
- gap: 4.95%
- MA60_slope_proxy: 0.024935
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-23 15:00:52**

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
- TERM_SPREAD_10Y_POLICY: 158.37 bp / 4주 변화 4.27 bp
- CURVE_10s5s: 38.32 bp / 4주 변화 -2.93 bp

## NWG Price
- close: 623.2
- MA50: 678.652 / gap50: -8.17%
- MA200: 635.3485 / gap200: -1.91%

## Relative Strength
- RS vs FTSE gap: -8.25% / slope_proxy: -0.00034
- RS vs Peers gap: 2.46% / slope_proxy: 0.020708

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-23 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 102.29 / 5D 0.87%
- Brent ref (BZ=F): 111.31 / 5D 1.32%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.02
- Gas ref (NG=F): 3.04 / 5D -2.34%

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

- close: 64.16
- MA20 / MA60 / MA200: 59.99 / 59.18 / 55.18
- gap20 / gap60: 6.96% / 8.41%
- 5D return: 2.86%
- 20D high/low: 64.16 / 54.94

### Relative Strength

- ratio: 0.925725
- ratio_MA60: 0.935561
- ratio_gap: -1.05%
- ratio_slope_proxy(20d): -0.011946

### Volume (if available)

- volume: 3754531.00
- volume_MA20: 8647361.55
- volume_ratio: 0.43

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 26.00
- MA20 / MA60 / MA200: 24.17 / 20.92 / 18.38
- gap20 / gap60: 7.59% / 24.30%
- 5D return: 0.02%
- 20D high/low: 26.00 / 20.65

### Relative Strength

- ratio: 0.621312
- ratio_MA60: 0.549490
- ratio_gap: 13.07%
- ratio_slope_proxy(20d): 0.032996

### Volume (if available)

- volume: 6967892.00
- volume_MA20: 23215284.60
- volume_ratio: 0.30

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

- close: 6.43
- MA20 / MA60 / MA200: 5.59 / 5.63 / 5.80
- gap20 / gap60: 15.20% / 14.24%
- 5D return: 14.50%
- 20D high/low: 6.43 / 5.17

### Relative Strength

- ratio: 0.016247
- ratio_MA60: 0.014034
- ratio_gap: 15.77%
- ratio_slope_proxy(20d): 0.000268

### Volume (if available)

- volume: 14373354.00
- volume_MA20: 39092442.70
- volume_ratio: 0.37

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.52
- MA20 / MA60 / MA200: 13.02 / 13.71 / 12.49
- gap20 / gap60: 3.77% / -1.39%
- 5D return: 6.25%
- 20D high/low: 13.84 / 12.50

### Relative Strength

- ratio: 0.045525
- ratio_MA60: 0.049746
- ratio_gap: -8.49%
- ratio_slope_proxy(20d): -0.001129

### Volume (if available)

- volume: 5973624.00
- volume_MA20: 13083971.20
- volume_ratio: 0.46

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-23 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 60.0 bp / latest 3.4
- IG OAS 4주 변화: 10.0 bp / latest 0.89
- 10Y Real Yield 4주 변화: 0.0 bp / latest 2.76
- VIX: 19.03
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.79% / slope_proxy: 0.007124
- GDXJ/GLD gap: -9.41% / slope_proxy: 0.009917

## VZLA (Vizsla Silver)
- close: 3.015 | RSI14: 32.76794 | ATR14%: 6.15%
- MA20 gap: -12.50% | MA50 gap: -19.71% | MA200 gap: -20.89%
- vol_ratio(Volume/Vol20): 0.663026 | gap_open: 0.63%
- RS vs SILJ gap: 0.19% / slope_proxy: 0.001169
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 6.94 | RSI14: 31.361164 | ATR14%: 7.75%
- MA20 gap: -17.93% | MA50 gap: -23.17% | MA200 gap: -21.97%
- vol_ratio(Volume/Vol20): 0.377303 | gap_open: 0.56%
- SilverMarginGate: SI=54.0 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.98% / slope_proxy: 0.021808
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 15.555 | RSI14: 32.327853 | ATR14%: 7.74%
- MA20 gap: -13.09% | MA50 gap: -26.44% | MA200 gap: -48.84%
- vol_ratio(Volume/Vol20): 0.342288 | gap_open: 0.89%
- RS vs SILJ gap: -10.93% / slope_proxy: -0.04965
- RS vs GDXJ gap: -14.86% / slope_proxy: -0.016855
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-10-23 15:01:20**
- 데이터 기준일(주가): **2026-10-23**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

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

- HY OAS: 3.40 / 4주 변화 0.60 bp-ish / 2026-10-22
- IG OAS: 0.89 / 4주 변화 0.10 bp-ish / 2026-10-22
- 10Y Real Yield: 2.76 / 4주 변화 0.13 bp-ish / 2026-10-21
- VIX: 19.03 / 4주 변화 3.36 / 2026-10-22
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-16

### Leadership ratios

- GDX/GLD: gap -5.56% / slope_proxy -5.78%
- GDXJ/GLD: gap -9.41% / slope_proxy -10.17%
- SILJ/SLV: gap -5.70% / slope_proxy -5.19%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.92 | RSI14: 32.10 | ATR14%: 4.82%
- MA20/50/200 gap: -11.65% / -18.64% / -1.63%
- 5D return: -11.80% | 20D drawdown: -16.98% | vol_ratio: 0.38
- RS vs GDXJ: gap -1.67% / slope_proxy -3.62%
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
- close: 5.51 | RSI14: 25.87 | ATR14%: 6.62%
- MA20/50/200 gap: -17.47% / -24.32% / -21.50%
- 5D return: -16.89% | 20D drawdown: -27.12% | vol_ratio: 0.28
- RS vs GDXJ: gap -7.96% / slope_proxy -11.22%
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
- close: 0.85 | RSI14: 30.43 | ATR14%: 7.69%
- MA20/50/200 gap: -14.10% / -34.60% / -41.32%
- 5D return: -12.37% | 20D drawdown: -29.75% | vol_ratio: 0.14
- RS vs GDXJ: gap -22.27% / slope_proxy -14.44%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.70 | RSI14: 23.60 | ATR14%: 7.61%
- MA20/50/200 gap: -19.98% / -28.89% / -14.55%
- 5D return: -20.56% | 20D drawdown: -33.07% | vol_ratio: 0.27
- RS vs GDXJ: gap -13.04% / slope_proxy -18.48%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **36.0**
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
- close: 23.66 | RSI14: 33.20 | ATR14%: 5.55%
- MA20/50/200 gap: -10.15% / -13.17% / 14.69%
- 5D return: -11.29% | 20D drawdown: -13.99% | vol_ratio: 0.38
- RS vs SILJ: gap 8.69% / slope_proxy 6.05%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **58.7**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.45 | RSI14: 31.68 | ATR14%: 5.27%
- MA20/50/200 gap: -10.86% / -22.42% / -24.20%
- 5D return: -9.53% | 20D drawdown: -16.80% | vol_ratio: 0.41
- RS vs SILJ: gap -3.01% / slope_proxy -1.06%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 13.87 | RSI14: 24.84 | ATR14%: 5.42%
- MA20/50/200 gap: -13.76% / -23.84% / -26.52%
- 5D return: -9.35% | 20D drawdown: -19.36% | vol_ratio: 0.15
- RS vs SILJ: gap -3.83% / slope_proxy -3.04%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **46.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.94 | RSI14: 26.48 | ATR14%: 7.26%
- MA20/50/200 gap: -17.93% / -23.17% / -21.97%
- 5D return: -16.79% | 20D drawdown: -23.82% | vol_ratio: 0.38
- RS vs SILJ: gap -3.03% / slope_proxy -8.51%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.02 | RSI14: 32.51 | ATR14%: 5.71%
- MA20/50/200 gap: -12.50% / -19.71% / -20.89%
- 5D return: -7.23% | 20D drawdown: -21.48% | vol_ratio: 0.66
- RS vs SILJ: gap 0.15% / slope_proxy -6.14%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **43.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.11 | RSI14: 18.53 | ATR14%: 7.51%
- MA20/50/200 gap: -23.03% / -34.27% / -46.14%
- 5D return: -17.86% | 20D drawdown: -31.00% | vol_ratio: 0.36
- RS vs SILJ: gap -18.23% / slope_proxy -17.95%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.64 | RSI14: 29.85 | ATR14%: 6.05%
- MA20/50/200 gap: -12.83% / -26.26% / -33.04%
- 5D return: -13.04% | 20D drawdown: -17.67% | vol_ratio: 0.58
- RS vs SILJ: gap -8.81% / slope_proxy -1.75%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **38.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.56 | RSI14: 31.94 | ATR14%: 6.92%
- MA20/50/200 gap: -13.06% / -26.42% / -48.82%
- 5D return: -9.38% | 20D drawdown: -20.61% | vol_ratio: 0.34
- RS vs SILJ: gap -10.94% / slope_proxy -5.60%
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
