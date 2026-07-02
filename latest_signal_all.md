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

- 실행시간(UTC): **2026-07-02 03:01:18**
- 데이터 기준일(일봉): **2026-07-01**
- 데이터 기준일(주봉): **2026-06-29**
- VXN 기준일: **2026-06-30** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 725.17
- Weekly RSI14: **64.05**
- 52W MA: 620.78 / gap: **16.82%**
- 104W MA gap: **30.17%**
- 52W MA 13W slope: **8.45%**
- VXN: **27.11** / 5D change: -5.26

## Daily trigger: 실제 매수 타이밍

- QQQ close: 725.17
- Daily RSI14: **52.60**
- 20D gap: **0.41%**
- 50D gap: **2.55%**
- 200D gap: **14.58%**
- MACD hist: -1.4708 / change: 0.2102
- ATR14%: **2.21%**
- 20D high drawdown: **-2.45%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-01**
- 실행시간(UTC): **2026-07-02 03:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.75 / 4주 변화 4.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.2 / 4주 변화 13.0 bp
- VIX (VIXCLS): 16.45
- NFCI: -0.504

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.880076
- MA60: 9.389787
- gap: 5.22%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.438465
- MA60: 0.365043
- gap: 20.11%
- MA60_slope_proxy: 0.072173
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-01**
- 실행시간(UTC): **2026-07-02 03:00:49**

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
- TERM_SPREAD_10Y_POLICY: 94.97 bp / 4주 변화 -16.99 bp
- CURVE_10s5s: 45.73 bp / 4주 변화 0.5 bp

## NWG Price
- close: 679.6
- MA50: 600.2331 / gap50: 13.22%
- MA200: 597.8556 / gap200: 13.67%

## Relative Strength
- RS vs FTSE gap: 12.26% / slope_proxy: 0.001894
- RS vs Peers gap: 4.82% / slope_proxy: -0.011997

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-02 03:00:58**

## Commodity Regime

- WTI ref (CL=F): 67.81 / 5D -3.60%
- Brent ref (BZ=F): 70.90 / 5D -3.85%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.09
- Gas ref (NG=F): 3.20 / 5D -0.71%

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

- close: 47.94
- MA20 / MA60 / MA200: 53.61 / 56.14 / 48.94
- gap20 / gap60: -10.57% / -14.61%
- 5D return: -6.17%
- 20D high/low: 59.37 / 47.94

### Relative Strength

- ratio: 0.907783
- ratio_MA60: 0.990534
- ratio_gap: -8.35%
- ratio_slope_proxy(20d): -0.018894

### Volume (if available)

- volume: 6265495.00
- volume_MA20: 9630514.75
- volume_ratio: 0.65

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 15.99
- MA20 / MA60 / MA200: 17.20 / 19.30 / 15.53
- gap20 / gap60: -7.02% / -17.15%
- 5D return: -2.80%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.467817
- ratio_MA60: 0.521661
- ratio_gap: -10.32%
- ratio_slope_proxy(20d): -0.008439

### Volume (if available)

- volume: 12221615.00
- volume_MA20: 14261765.75
- volume_ratio: 0.86

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 4.87
- MA20 / MA60 / MA200: 5.58 / 6.21 / 5.12
- gap20 / gap60: -12.78% / -21.59%
- 5D return: -3.37%
- 20D high/low: 6.25 / 4.87

### Relative Strength

- ratio: 0.013525
- ratio_MA60: 0.014794
- ratio_gap: -8.58%
- ratio_slope_proxy(20d): -0.000867

### Volume (if available)

- volume: 59949114.00
- volume_MA20: 34277260.70
- volume_ratio: 1.75

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 11.03
- MA20 / MA60 / MA200: 11.78 / 12.49 / 10.73
- gap20 / gap60: -6.41% / -11.70%
- 5D return: 4.95%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045220
- ratio_MA60: 0.050589
- ratio_gap: -10.61%
- ratio_slope_proxy(20d): -0.001250

### Volume (if available)

- volume: 8433312.00
- volume_MA20: 13550165.60
- volume_ratio: 0.62

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

- 데이터 기준일(주가): **2026-07-01**
- 실행시간(UTC): **2026-07-02 03:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 4.0 bp / latest 2.75
- IG OAS 4주 변화: 2.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.2
- VIX: 16.45
- NFCI: -0.504

### Leadership ratios
- SILJ/SLV gap: 7.96% / slope_proxy: 0.007016
- GDXJ/GLD gap: -5.13% / slope_proxy: -0.002001

## VZLA (Vizsla Silver)
- close: 3.26 | RSI14: 43.351426 | ATR14%: 6.49%
- MA20 gap: -5.21% | MA50 gap: -6.93% | MA200 gap: -22.98%
- vol_ratio(Volume/Vol20): 0.402925 | gap_open: 0.61%
- RS vs SILJ gap: 6.26% / slope_proxy: 0.004708
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
- close: 6.59 | RSI14: 41.946972 | ATR14%: 7.76%
- MA20 gap: -3.37% | MA50 gap: -15.78% | MA200 gap: -22.62%
- vol_ratio(Volume/Vol20): 0.428874 | gap_open: 0.00%
- SilverMarginGate: SI=60.595001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.25% / slope_proxy: -0.008968
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
- close: 23.07 | RSI14: 36.732887 | ATR14%: 9.71%
- MA20 gap: -8.70% | MA50 gap: -28.21% | MA200 gap: -12.22%
- vol_ratio(Volume/Vol20): 0.684769 | gap_open: 0.43%
- RS vs SILJ gap: -20.74% / slope_proxy: -0.085504
- RS vs GDXJ gap: -18.15% / slope_proxy: -0.018498
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

- 실행시간(UTC): **2026-07-02 03:01:15**
- 데이터 기준일(주가): **2026-07-01**

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

- HY OAS: 2.75 / 4주 변화 0.04 bp-ish / 2026-06-30
- IG OAS: 0.76 / 4주 변화 0.02 bp-ish / 2026-06-30
- 10Y Real Yield: 2.20 / 4주 변화 0.13 bp-ish / 2026-06-30
- VIX: 16.45 / 4주 변화 0.68 / 2026-06-30
- NFCI: -0.50 / 4주 변화 0.05 / 2026-06-26

### Leadership ratios

- GDX/GLD: gap -4.65% / slope_proxy -2.80%
- GDXJ/GLD: gap -5.13% / slope_proxy -2.68%
- SILJ/SLV: gap 7.96% / slope_proxy 8.53%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.49 | RSI14: 60.25 | ATR14%: 6.10%
- MA20/50/200 gap: -1.94% / -4.90% / 12.28%
- 5D return: 2.88% | 20D drawdown: -10.73% | vol_ratio: 0.28
- RS vs GDXJ: gap 12.14% / slope_proxy 3.17%
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
- close: 5.17 | RSI14: 50.81 | ATR14%: 6.16%
- MA20/50/200 gap: -7.04% / -17.28% / -25.42%
- 5D return: -1.90% | 20D drawdown: -18.97% | vol_ratio: 0.80
- RS vs GDXJ: gap -5.50% / slope_proxy -10.78%
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
- close: 1.15 | RSI14: 50.00 | ATR14%: 8.70%
- MA20/50/200 gap: -8.29% / -13.61% / -23.64%
- 5D return: -6.50% | 20D drawdown: -21.77% | vol_ratio: 2.17
- RS vs GDXJ: gap -0.56% / slope_proxy -1.63%
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
- close: 1.61 | RSI14: 57.33 | ATR14%: 5.81%
- MA20/50/200 gap: -1.04% / -10.95% / -4.90%
- 5D return: 2.55% | 20D drawdown: -14.81% | vol_ratio: 0.97
- RS vs GDXJ: gap 4.34% / slope_proxy -3.53%
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
- close: 19.09 | RSI14: 61.62 | ATR14%: 7.68%
- MA20/50/200 gap: 1.95% / 2.47% / 23.44%
- 5D return: 11.51% | 20D drawdown: -9.31% | vol_ratio: 0.51
- RS vs SILJ: gap 17.59% / slope_proxy 10.61%
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
- close: 8.34 | RSI14: 60.70 | ATR14%: 6.77%
- MA20/50/200 gap: -0.58% / -9.10% / -12.38%
- 5D return: 8.17% | 20D drawdown: -10.32% | vol_ratio: 0.56
- RS vs SILJ: gap 2.50% / slope_proxy 3.55%
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
- close: 15.59 | RSI14: 62.30 | ATR14%: 5.84%
- MA20/50/200 gap: 0.55% / -8.67% / -13.19%
- 5D return: 7.37% | 20D drawdown: -7.37% | vol_ratio: 0.75
- RS vs SILJ: gap 1.87% / slope_proxy 6.48%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.36 | RSI14: 62.57 | ATR14%: 7.19%
- MA20/50/200 gap: 1.65% / -4.56% / -3.17%
- 5D return: 12.77% | 20D drawdown: -8.49% | vol_ratio: 0.55
- RS vs SILJ: gap 7.36% / slope_proxy 6.18%
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
- close: 6.59 | RSI14: 56.86 | ATR14%: 7.69%
- MA20/50/200 gap: -3.37% / -15.78% / -22.62%
- 5D return: 4.11% | 20D drawdown: -17.31% | vol_ratio: 0.43
- RS vs SILJ: gap -5.25% / slope_proxy 0.71%
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
- close: 3.26 | RSI14: 52.27 | ATR14%: 6.23%
- MA20/50/200 gap: -5.21% / -6.93% / -22.98%
- 5D return: 4.82% | 20D drawdown: -15.54% | vol_ratio: 0.40
- RS vs SILJ: gap 6.26% / slope_proxy -3.84%
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
- close: 4.74 | RSI14: 52.79 | ATR14%: 8.47%
- MA20/50/200 gap: -7.46% / -17.24% / -16.40%
- 5D return: 3.95% | 20D drawdown: -19.39% | vol_ratio: 0.52
- RS vs SILJ: gap -6.14% / slope_proxy -8.22%
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
- close: 23.07 | RSI14: 50.31 | ATR14%: 8.57%
- MA20/50/200 gap: -8.70% / -28.21% / -12.22%
- 5D return: 6.31% | 20D drawdown: -28.24% | vol_ratio: 0.68
- RS vs SILJ: gap -20.74% / slope_proxy -18.30%
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
