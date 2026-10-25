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

- 실행시간(UTC): **2026-10-25 00:32:00**
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

- QQQ close: 704.40
- Weekly RSI14: **50.59**
- 52W MA: 662.83 / gap: **6.27%**
- 104W MA gap: **18.53%**
- 52W MA 13W slope: **5.52%**
- VXN: **28.72** / 5D change: 5.83

## Daily trigger: 실제 매수 타이밍

- QQQ close: 704.40
- Daily RSI14: **36.59**
- 20D gap: **-4.19%**
- 50D gap: **-2.90%**
- 200D gap: **4.19%**
- MACD hist: -5.1683 / change: -0.1876
- ATR14%: **1.64%**
- 20D high drawdown: **-7.27%**

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
- 실행시간(UTC): **2026-10-25 00:30:13**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.4 / 4주 변화 60.0 bp
- IG OAS (BAMLC0A0CM): 0.89 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.64 / 4주 변화 -21.0 bp
- VIX (VIXCLS): 19.03
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.073899
- MA60: 8.44136
- gap: -16.20%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.433441
- MA60: 0.412976
- gap: 4.96%
- MA60_slope_proxy: 0.024935
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-25 00:30:16**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- BoE IUDMNPY failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.
- BoE IUDSNPY failed (HTTPSConnectionPool(host='www.bankofengland.co.uk', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- close: 627.4
- MA50: 678.736 / gap50: -7.56%
- MA200: 635.3695 / gap200: -1.25%

## Relative Strength
- RS vs FTSE gap: -7.96% / slope_proxy: -0.000336
- RS vs Peers gap: 2.54% / slope_proxy: 0.020721

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-25 00:31:42**

## Commodity Regime

- WTI ref (CL=F): 103.27 / 5D 1.83%
- Brent ref (BZ=F): 116.72 / 5D 6.24%
- Brent Tier: **>=90**
- Brent-WTI spread: 13.45
- Gas ref (NG=F): 2.64 / 5D -15.28%

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

- close: 64.17
- MA20 / MA60 / MA200: 59.99 / 59.18 / 55.18
- gap20 / gap60: 6.97% / 8.43%
- 5D return: 2.87%
- 20D high/low: 64.17 / 54.94

### Relative Strength

- ratio: 0.925573
- ratio_MA60: 0.935559
- ratio_gap: -1.07%
- ratio_slope_proxy(20d): -0.011948

### Volume (if available)

- volume: 11644400.00
- volume_MA20: 9041855.00
- volume_ratio: 1.29

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 26.16
- MA20 / MA60 / MA200: 24.18 / 20.92 / 18.38
- gap20 / gap60: 8.19% / 25.03%
- 5D return: 0.62%
- 20D high/low: 26.16 / 20.65

### Relative Strength

- ratio: 0.614229
- ratio_MA60: 0.549372
- ratio_gap: 11.81%
- ratio_slope_proxy(20d): 0.032878

### Volume (if available)

- volume: 25124900.00
- volume_MA20: 24123135.00
- volume_ratio: 1.04

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

- close: 6.41
- MA20 / MA60 / MA200: 5.58 / 5.63 / 5.80
- gap20 / gap60: 14.78% / 13.80%
- 5D return: 14.06%
- 20D high/low: 6.41 / 5.17

### Relative Strength

- ratio: 0.016131
- ratio_MA60: 0.014032
- ratio_gap: 14.96%
- ratio_slope_proxy(20d): 0.000266

### Volume (if available)

- volume: 45944000.00
- volume_MA20: 40673980.00
- volume_ratio: 1.13

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.00
- MA20 / MA60 / MA200: 13.05 / 13.71 / 12.49
- gap20 / gap60: 7.29% / 2.09%
- 5D return: 10.06%
- 20D high/low: 14.00 / 12.50

### Relative Strength

- ratio: 0.046874
- ratio_MA60: 0.049769
- ratio_gap: -5.82%
- ratio_slope_proxy(20d): -0.001106

### Volume (if available)

- volume: 22590600.00
- volume_MA20: 13915855.00
- volume_ratio: 1.62

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

- 데이터 기준일(주가): **2026-10-23**
- 실행시간(UTC): **2026-10-25 00:31:47**

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
- 10Y Real Yield 4주 변화: -21.0 bp / latest 2.64
- VIX: 19.03
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.91% / slope_proxy: 0.007114
- GDXJ/GLD gap: -9.48% / slope_proxy: 0.009913

## VZLA (Vizsla Silver)
- close: 3.09 | RSI14: 34.513834 | ATR14%: 6.00%
- MA20 gap: -10.42% | MA50 gap: -17.75% | MA200 gap: -18.93%
- vol_ratio(Volume/Vol20): 1.75812 | gap_open: 0.63%
- RS vs SILJ gap: 2.86% / slope_proxy: 0.001228
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
- close: 6.95 | RSI14: 31.433038 | ATR14%: 7.76%
- MA20 gap: -17.82% | MA50 gap: -23.06% | MA200 gap: -21.86%
- vol_ratio(Volume/Vol20): 1.094708 | gap_open: 0.56%
- SilverMarginGate: SI=53.710999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.64% / slope_proxy: 0.021826
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
- close: 15.44 | RSI14: 31.926394 | ATR14%: 7.80%
- MA20 gap: -13.70% | MA50 gap: -26.98% | MA200 gap: -49.22%
- vol_ratio(Volume/Vol20): 0.855872 | gap_open: 1.65%
- RS vs SILJ gap: -11.39% / slope_proxy: -0.049709
- RS vs GDXJ gap: -15.41% / slope_proxy: -0.016873
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

- 실행시간(UTC): **2026-10-25 00:31:58**
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
- 10Y Real Yield: 2.64 / 4주 변화 -0.12 bp-ish / 2026-10-22
- VIX: 19.03 / 4주 변화 3.36 / 2026-10-22
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-16

### Leadership ratios

- GDX/GLD: gap -5.72% / slope_proxy -5.94%
- GDXJ/GLD: gap -9.48% / slope_proxy -10.24%
- SILJ/SLV: gap -5.91% / slope_proxy -5.40%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.97 | RSI14: 32.60 | ATR14%: 4.79%
- MA20/50/200 gap: -11.12% / -18.14% / -1.01%
- 5D return: -11.25% | 20D drawdown: -16.46% | vol_ratio: 1.03
- RS vs GDXJ: gap -0.98% / slope_proxy -2.93%
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
- close: 5.50 | RSI14: 25.78 | ATR14%: 6.64%
- MA20/50/200 gap: -17.62% / -24.45% / -21.64%
- 5D return: -17.04% | 20D drawdown: -27.25% | vol_ratio: 1.16
- RS vs GDXJ: gap -8.05% / slope_proxy -11.31%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.84 | RSI14: 28.89 | ATR14%: 7.87%
- MA20/50/200 gap: -15.07% / -35.35% / -42.01%
- 5D return: -13.40% | 20D drawdown: -30.58% | vol_ratio: 0.38
- RS vs GDXJ: gap -23.11% / slope_proxy -15.37%
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
- close: 1.75 | RSI14: 25.00 | ATR14%: 7.39%
- MA20/50/200 gap: -17.72% / -26.83% / -12.05%
- 5D return: -18.22% | 20D drawdown: -31.10% | vol_ratio: 0.77
- RS vs GDXJ: gap -10.45% / slope_proxy -16.01%
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
- close: 23.77 | RSI14: 33.57 | ATR14%: 5.56%
- MA20/50/200 gap: -9.75% / -12.78% / 15.22%
- 5D return: -10.87% | 20D drawdown: -13.60% | vol_ratio: 0.79
- RS vs SILJ: gap 9.46% / slope_proxy 6.82%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.95 | RSI14: 26.54 | ATR14%: 7.27%
- MA20/50/200 gap: -17.82% / -23.06% / -21.86%
- 5D return: -16.67% | 20D drawdown: -23.71% | vol_ratio: 1.09
- RS vs SILJ: gap -2.64% / slope_proxy -8.14%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.09 | RSI14: 34.33 | ATR14%: 5.57%
- MA20/50/200 gap: -10.42% / -17.75% / -18.93%
- 5D return: -4.92% | 20D drawdown: -19.53% | vol_ratio: 1.76
- RS vs SILJ: gap 2.86% / slope_proxy -3.56%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.9**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.47 | RSI14: 31.83 | ATR14%: 5.26%
- MA20/50/200 gap: -10.69% / -22.27% / -24.05%
- 5D return: -9.34% | 20D drawdown: -16.63% | vol_ratio: 0.91
- RS vs SILJ: gap -2.57% / slope_proxy -0.60%
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
- close: 13.85 | RSI14: 24.76 | ATR14%: 5.43%
- MA20/50/200 gap: -13.88% / -23.95% / -26.62%
- 5D return: -9.48% | 20D drawdown: -19.48% | vol_ratio: 0.98
- RS vs SILJ: gap -3.73% / slope_proxy -2.93%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.64 | RSI14: 29.91 | ATR14%: 6.03%
- MA20/50/200 gap: -12.74% / -26.18% / -32.96%
- 5D return: -12.95% | 20D drawdown: -17.58% | vol_ratio: 1.30
- RS vs SILJ: gap -8.48% / slope_proxy -1.39%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **43.5**
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.07 | RSI14: 18.22 | ATR14%: 7.58%
- MA20/50/200 gap: -23.87% / -35.00% / -46.75%
- 5D return: -18.78% | 20D drawdown: -31.78% | vol_ratio: 0.86
- RS vs SILJ: gap -18.93% / slope_proxy -18.66%
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
- close: 15.44 | RSI14: 31.52 | ATR14%: 6.97%
- MA20/50/200 gap: -13.70% / -26.98% / -49.22%
- 5D return: -10.08% | 20D drawdown: -21.22% | vol_ratio: 0.86
- RS vs SILJ: gap -11.39% / slope_proxy -6.08%
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
