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

- 실행시간(UTC): **2026-07-20 15:01:38**
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

- QQQ close: 699.16
- Weekly RSI14: **56.87**
- 52W MA: 629.12 / gap: **11.13%**
- 104W MA gap: **24.02%**
- 52W MA 13W slope: **7.89%**
- VXN: **29.03** / 5D change: 4.14

## Daily trigger: 실제 매수 타이밍

- QQQ close: 698.93
- Daily RSI14: **43.68**
- 20D gap: **-2.42%**
- 50D gap: **-2.74%**
- 200D gap: **9.20%**
- MACD hist: -3.0710 / change: -0.2567
- ATR14%: **2.14%**
- 20D high drawdown: **-5.29%**

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
- 실행시간(UTC): **2026-07-20 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.35 / 4주 변화 14.0 bp
- VIX (VIXCLS): 18.77
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.66052
- MA60: 9.627949
- gap: 0.34%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.34787
- MA60: 0.380543
- gap: -8.59%
- MA60_slope_proxy: 0.04038
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-20**
- 실행시간(UTC): **2026-07-20 15:00:52**

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
- close: 665.0
- MA50: 623.584 / gap50: 6.64%
- MA200: 607.456 / gap200: 9.47%

## Relative Strength
- RS vs FTSE gap: 7.02% / slope_proxy: 0.00222
- RS vs Peers gap: 1.10% / slope_proxy: -0.004008

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-20 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 81.73 / 5D 4.59%
- Brent ref (BZ=F): 88.17 / 5D 5.85%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.44
- Gas ref (NG=F): 2.85 / 5D -1.76%

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

- close: 55.09
- MA20 / MA60 / MA200: 51.85 / 55.32 / 49.34
- gap20 / gap60: 6.24% / -0.42%
- 5D return: 0.51%
- 20D high/low: 55.09 / 47.94

### Relative Strength

- ratio: 0.948519
- ratio_MA60: 0.977783
- ratio_gap: -2.99%
- ratio_slope_proxy(20d): -0.028549

### Volume (if available)

- volume: 1748286.00
- volume_MA20: 9352894.30
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.17
- MA20 / MA60 / MA200: 16.98 / 18.63 / 15.80
- gap20 / gap60: 6.97% / -2.50%
- 5D return: 1.59%
- 20D high/low: 18.17 / 15.99

### Relative Strength

- ratio: 0.511979
- ratio_MA60: 0.517758
- ratio_gap: -1.12%
- ratio_slope_proxy(20d): -0.012161

### Volume (if available)

- volume: 3058372.00
- volume_MA20: 14010938.60
- volume_ratio: 0.22

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
- MA20 / MA60 / MA200: 5.14 / 5.98 / 5.23
- gap20 / gap60: 0.17% / -13.96%
- 5D return: -4.19%
- 20D high/low: 5.41 / 4.87

### Relative Strength

- ratio: 0.013557
- ratio_MA60: 0.014446
- ratio_gap: -6.16%
- ratio_slope_proxy(20d): -0.000740

### Volume (if available)

- volume: 5653803.00
- volume_MA20: 36691025.15
- volume_ratio: 0.15

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

- close: 14.07
- MA20 / MA60 / MA200: 11.94 / 12.44 / 10.64
- gap20 / gap60: 17.82% / 13.07%
- 5D return: 5.31%
- 20D high/low: 14.07 / 10.51

### Relative Strength

- ratio: 0.053146
- ratio_MA60: 0.050552
- ratio_gap: 5.13%
- ratio_slope_proxy(20d): -0.001359

### Volume (if available)

- volume: 5670183.00
- volume_MA20: 12631164.15
- volume_ratio: 0.45

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
- 실행시간(UTC): **2026-07-20 15:01:15**

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
- VIX: 18.77
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 1.90% / slope_proxy: 0.008514
- GDXJ/GLD gap: -8.23% / slope_proxy: -0.007647

## VZLA (Vizsla Silver)
- close: 3.14 | RSI14: 45.362542 | ATR14%: 6.12%
- MA20 gap: -1.68% | MA50 gap: -8.78% | MA200 gap: -24.86%
- vol_ratio(Volume/Vol20): 0.222975 | gap_open: 0.65%
- RS vs SILJ gap: 8.81% / slope_proxy: 0.005783
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
- close: 5.86 | RSI14: 36.24893 | ATR14%: 7.45%
- MA20 gap: -9.09% | MA50 gap: -20.48% | MA200 gap: -30.80%
- vol_ratio(Volume/Vol20): 0.347001 | gap_open: 0.00%
- SilverMarginGate: SI=57.215 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.35% / slope_proxy: -0.006137
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
- close: 18.629999 | RSI14: 33.148543 | ATR14%: 10.27%
- MA20 gap: -14.83% | MA50 gap: -33.87% | MA200 gap: -31.43%
- vol_ratio(Volume/Vol20): 0.115563 | gap_open: 1.52%
- RS vs SILJ gap: -24.04% / slope_proxy: -0.121872
- RS vs GDXJ gap: -24.41% / slope_proxy: -0.027114
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

- 실행시간(UTC): **2026-07-20 15:01:36**
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

- HY OAS: 2.71 / 4주 변화 0.05 bp-ish / 2026-07-16
- IG OAS: 0.78 / 4주 변화 0.04 bp-ish / 2026-07-16
- 10Y Real Yield: 2.35 / 4주 변화 0.21 bp-ish / 2026-07-16
- VIX: 18.77 / 4주 변화 1.99 / 2026-07-17
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -7.11% / slope_proxy -8.89%
- GDXJ/GLD: gap -8.23% / slope_proxy -9.43%
- SILJ/SLV: gap 1.92% / slope_proxy -1.84%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.89 | RSI14: 40.93 | ATR14%: 5.58%
- MA20/50/200 gap: -7.40% / -11.90% / 1.22%
- 5D return: -4.83% | 20D drawdown: -15.15% | vol_ratio: 0.28
- RS vs GDXJ: gap 4.54% / slope_proxy -2.00%
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
- close: 4.99 | RSI14: 44.62 | ATR14%: 4.97%
- MA20/50/200 gap: -3.74% / -14.59% / -27.64%
- 5D return: 0.40% | 20D drawdown: -13.22% | vol_ratio: 0.20
- RS vs GDXJ: gap -1.11% / slope_proxy 1.45%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.77 | RSI14: 65.12 | ATR14%: 7.91%
- MA20/50/200 gap: 3.03% / -3.43% / -0.12%
- 5D return: -11.50% | 20D drawdown: -14.08% | vol_ratio: 0.06
- RS vs GDXJ: gap 16.32% / slope_proxy 25.95%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **44.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.04 | RSI14: 40.00 | ATR14%: 7.14%
- MA20/50/200 gap: -9.86% / -18.21% / -30.31%
- 5D return: -5.00% | 20D drawdown: -20.23% | vol_ratio: 0.09
- RS vs GDXJ: gap -3.44% / slope_proxy -8.31%
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
- close: 17.99 | RSI14: 45.15 | ATR14%: 7.04%
- MA20/50/200 gap: -5.81% / -5.73% / 12.78%
- 5D return: -5.91% | 20D drawdown: -11.42% | vol_ratio: 0.36
- RS vs SILJ: gap 13.33% / slope_proxy 6.57%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.16 | RSI14: 38.38 | ATR14%: 5.83%
- MA20/50/200 gap: -7.71% / -13.70% / -22.16%
- 5D return: -7.11% | 20D drawdown: -13.94% | vol_ratio: 0.12
- RS vs SILJ: gap 1.31% / slope_proxy 3.65%
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
- close: 3.14 | RSI14: 45.02 | ATR14%: 5.83%
- MA20/50/200 gap: -1.53% / -8.64% / -24.74%
- 5D return: 4.14% | 20D drawdown: -10.65% | vol_ratio: 0.22
- RS vs SILJ: gap 8.96% / slope_proxy 4.48%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.32 | RSI14: 35.33 | ATR14%: 6.41%
- MA20/50/200 gap: -8.85% / -17.24% / -23.41%
- 5D return: -6.57% | 20D drawdown: -14.43% | vol_ratio: 0.20
- RS vs SILJ: gap -1.85% / slope_proxy 0.18%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.49 | RSI14: 35.73 | ATR14%: 7.03%
- MA20/50/200 gap: -8.59% / -15.32% / -17.26%
- 5D return: -4.27% | 20D drawdown: -16.49% | vol_ratio: 0.26
- RS vs SILJ: gap 0.75% / slope_proxy 0.09%
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
- close: 5.86 | RSI14: 36.73 | ATR14%: 6.65%
- MA20/50/200 gap: -9.09% / -20.48% / -30.80%
- 5D return: -7.72% | 20D drawdown: -17.00% | vol_ratio: 0.35
- RS vs SILJ: gap -6.37% / slope_proxy -2.94%
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
- close: 3.74 | RSI14: 28.93 | ATR14%: 8.43%
- MA20/50/200 gap: -16.06% / -29.76% / -34.71%
- 5D return: -7.34% | 20D drawdown: -29.77% | vol_ratio: 0.35
- RS vs SILJ: gap -16.96% / slope_proxy -17.87%
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
- close: 18.63 | RSI14: 30.21 | ATR14%: 9.06%
- MA20/50/200 gap: -14.83% / -33.87% / -31.43%
- 5D return: -8.81% | 20D drawdown: -25.63% | vol_ratio: 0.12
- RS vs SILJ: gap -24.06% / slope_proxy -13.03%
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
