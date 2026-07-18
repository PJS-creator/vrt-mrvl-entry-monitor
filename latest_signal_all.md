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

- 실행시간(UTC): **2026-07-18 15:01:08**
- 데이터 기준일(일봉): **2026-07-17**
- 데이터 기준일(주봉): **2026-07-13**
- VXN 기준일: **2026-07-16** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 695.33
- Weekly RSI14: **56.12**
- 52W MA: 626.51 / gap: **10.98%**
- 104W MA gap: **23.85%**
- 52W MA 13W slope: **8.13%**
- VXN: **27.34** / 5D change: 0.43

## Daily trigger: 실제 매수 타이밍

- QQQ close: 695.33
- Daily RSI14: **42.07**
- 20D gap: **-3.20%**
- 50D gap: **-3.23%**
- 200D gap: **8.73%**
- MACD hist: -2.8143 / change: -0.9982
- ATR14%: **2.20%**
- 20D high drawdown: **-6.01%**

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

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-18 15:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.35 / 4주 변화 14.0 bp
- VIX (VIXCLS): 16.73
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.540692
- MA60: 9.612619
- gap: -0.75%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.339029
- MA60: 0.380243
- gap: -10.84%
- MA60_slope_proxy: 0.044024
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-18 15:00:41**

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
- TERM_SPREAD_10Y_POLICY: 118.99 bp / 4주 변화 20.05 bp
- CURVE_10s5s: 47.2 bp / 4주 변화 0.42 bp

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

- 실행시간(UTC): **2026-07-18 15:00:49**

## Commodity Regime

- WTI ref (CL=F): 82.49 / 5D 15.52%
- Brent ref (BZ=F): 88.10 / 5D 15.91%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.61
- Gas ref (NG=F): 2.91 / 5D -0.99%

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

- close: 54.86
- MA20 / MA60 / MA200: 51.69 / 55.35 / 49.30
- gap20 / gap60: 6.13% / -0.89%
- 5D return: 3.72%
- 20D high/low: 54.86 / 47.94

### Relative Strength

- ratio: 0.951110
- ratio_MA60: 0.978835
- ratio_gap: -2.83%
- ratio_slope_proxy(20d): -0.028142

### Volume (if available)

- volume: 7912900.00
- volume_MA20: 9959070.00
- volume_ratio: 0.79

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.97
- MA20 / MA60 / MA200: 16.91 / 18.68 / 15.77
- gap20 / gap60: 6.27% / -3.78%
- 5D return: 3.75%
- 20D high/low: 17.97 / 15.99

### Relative Strength

- ratio: 0.510077
- ratio_MA60: 0.517886
- ratio_gap: -1.51%
- ratio_slope_proxy(20d): -0.012696

### Volume (if available)

- volume: 15654800.00
- volume_MA20: 14950815.00
- volume_ratio: 1.05

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

- close: 5.14
- MA20 / MA60 / MA200: 5.14 / 6.00 / 5.22
- gap20 / gap60: -0.09% / -14.26%
- 5D return: -1.15%
- 20D high/low: 5.41 / 4.87

### Relative Strength

- ratio: 0.013562
- ratio_MA60: 0.014462
- ratio_gap: -6.22%
- ratio_slope_proxy(20d): -0.000766

### Volume (if available)

- volume: 36074700.00
- volume_MA20: 39766255.00
- volume_ratio: 0.91

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

- close: 13.80
- MA20 / MA60 / MA200: 11.79 / 12.41 / 10.64
- gap20 / gap60: 17.06% / 11.16%
- 5D return: 12.75%
- 20D high/low: 13.80 / 10.51

### Relative Strength

- ratio: 0.052551
- ratio_MA60: 0.050466
- ratio_gap: 4.13%
- ratio_slope_proxy(20d): -0.001577

### Volume (if available)

- volume: 21699700.00
- volume_MA20: 13339280.00
- volume_ratio: 1.63

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

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-18 15:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.71
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 14.0 bp / latest 2.35
- VIX: 16.73
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 3.80% / slope_proxy: 0.00874
- GDXJ/GLD gap: -8.32% / slope_proxy: -0.006909

## VZLA (Vizsla Silver)
- close: 3.07 | RSI14: 42.408359 | ATR14%: 6.49%
- MA20 gap: -4.48% | MA50 gap: -10.98% | MA200 gap: -26.64%
- vol_ratio(Volume/Vol20): 0.969017 | gap_open: 1.63%
- RS vs SILJ gap: 5.93% / slope_proxy: 0.005647
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
- close: 5.94 | RSI14: 37.216462 | ATR14%: 7.72%
- MA20 gap: -8.76% | MA50 gap: -20.02% | MA200 gap: -29.95%
- vol_ratio(Volume/Vol20): 1.331019 | gap_open: 2.68%
- SilverMarginGate: SI=56.037998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.99% / slope_proxy: -0.005959
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
- close: 19.049999 | RSI14: 34.110553 | ATR14%: 10.49%
- MA20 gap: -14.35% | MA50 gap: -33.38% | MA200 gap: -29.72%
- vol_ratio(Volume/Vol20): 0.778347 | gap_open: 0.79%
- RS vs SILJ gap: -23.51% / slope_proxy: -0.117893
- RS vs GDXJ gap: -23.55% / slope_proxy: -0.026119
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

- 실행시간(UTC): **2026-07-18 15:01:06**
- 데이터 기준일(주가): **2026-07-17**

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

- HY OAS: 2.71 / 4주 변화 0.05 bp-ish / 2026-07-16
- IG OAS: 0.78 / 4주 변화 0.04 bp-ish / 2026-07-16
- 10Y Real Yield: 2.35 / 4주 변화 0.21 bp-ish / 2026-07-16
- VIX: 16.73 / 4주 변화 0.33 / 2026-07-16
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -6.97% / slope_proxy -9.17%
- GDXJ/GLD: gap -8.32% / slope_proxy -9.64%
- SILJ/SLV: gap 3.80% / slope_proxy -0.14%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.77 | RSI14: 64.37 | ATR14%: 8.03%
- MA20/50/200 gap: 3.48% / -3.44% / 0.19%
- 5D return: -14.08% | 20D drawdown: -14.08% | vol_ratio: 1.42
- RS vs GDXJ: gap 16.49% / slope_proxy 27.74%
- FundamentalScore: 55 | TechnicalScore: 80 | RegimeScore: 30 | OverallScore: **58.8**
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
- close: 6.85 | RSI14: 38.35 | ATR14%: 5.86%
- MA20/50/200 gap: -8.68% / -12.65% / 0.71%
- 5D return: -11.15% | 20D drawdown: -15.64% | vol_ratio: 1.03
- RS vs GDXJ: gap 3.90% / slope_proxy -1.78%
- FundamentalScore: 88 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **56.1**
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
- close: 4.95 | RSI14: 44.90 | ATR14%: 5.08%
- MA20/50/200 gap: -5.07% / -15.78% / -28.26%
- 5D return: -4.44% | 20D drawdown: -13.91% | vol_ratio: 0.88
- RS vs GDXJ: gap -2.40% / slope_proxy -0.10%
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
- close: 1.06 | RSI14: 39.62 | ATR14%: 7.04%
- MA20/50/200 gap: -9.48% / -17.51% / -29.43%
- 5D return: -7.83% | 20D drawdown: -19.08% | vol_ratio: 1.10
- RS vs GDXJ: gap -2.32% / slope_proxy -9.84%
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

---

## Silver miners

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.33 | RSI14: 38.56 | ATR14%: 5.86%
- MA20/50/200 gap: -7.17% / -13.12% / -21.21%
- 5D return: -9.42% | 20D drawdown: -12.94% | vol_ratio: 1.94
- RS vs SILJ: gap 1.75% / slope_proxy 5.37%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.75 | RSI14: 43.63 | ATR14%: 6.85%
- MA20/50/200 gap: -2.32% / -1.75% / 17.78%
- 5D return: -7.68% | 20D drawdown: -7.68% | vol_ratio: 0.74
- RS vs SILJ: gap 17.86% / slope_proxy 10.69%
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
- close: 7.41 | RSI14: 35.16 | ATR14%: 6.54%
- MA20/50/200 gap: -8.52% / -16.65% / -22.54%
- 5D return: -8.29% | 20D drawdown: -13.94% | vol_ratio: 1.00
- RS vs SILJ: gap -1.41% / slope_proxy 1.00%
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
- close: 3.07 | RSI14: 41.18 | ATR14%: 6.02%
- MA20/50/200 gap: -4.48% / -10.98% / -26.64%
- 5D return: -1.92% | 20D drawdown: -13.52% | vol_ratio: 0.97
- RS vs SILJ: gap 5.93% / slope_proxy 1.49%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 5.94 | RSI14: 36.44 | ATR14%: 6.69%
- MA20/50/200 gap: -8.76% / -20.02% / -29.95%
- 5D return: -8.76% | 20D drawdown: -16.92% | vol_ratio: 1.33
- RS vs SILJ: gap -5.99% / slope_proxy -2.50%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **49.8**
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
- close: 3.78 | RSI14: 27.90 | ATR14%: 8.62%
- MA20/50/200 gap: -16.75% / -29.79% / -34.07%
- 5D return: -12.09% | 20D drawdown: -29.48% | vol_ratio: 1.19
- RS vs SILJ: gap -17.03% / slope_proxy -17.23%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **47.1**
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
- close: 5.50 | RSI14: 38.52 | ATR14%: 7.21%
- MA20/50/200 gap: -9.29% / -15.59% / -17.17%
- 5D return: -9.09% | 20D drawdown: -16.41% | vol_ratio: 0.99
- RS vs SILJ: gap 0.12% / slope_proxy -1.30%
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
- close: 19.05 | RSI14: 30.36 | ATR14%: 9.22%
- MA20/50/200 gap: -14.35% / -33.38% / -29.72%
- 5D return: -10.90% | 20D drawdown: -26.76% | vol_ratio: 0.78
- RS vs SILJ: gap -23.51% / slope_proxy -14.04%
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
