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

- 실행시간(UTC): **2026-10-23 03:01:26**
- 데이터 기준일(일봉): **2026-10-22**
- 데이터 기준일(주봉): **2026-10-19**
- VXN 기준일: **2026-10-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 704.47
- Weekly RSI14: **50.61**
- 52W MA: 662.83 / gap: **6.28%**
- 104W MA gap: **18.54%**
- 52W MA 13W slope: **5.52%**
- VXN: **24.42** / 5D change: 1.72

## Daily trigger: 실제 매수 타이밍

- QQQ close: 704.47
- Daily RSI14: **36.62**
- 20D gap: **-4.44%**
- 50D gap: **-2.96%**
- 200D gap: **4.26%**
- MACD hist: -4.9806 / change: -0.6867
- ATR14%: **1.68%**
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

- 데이터 기준일(주가): **2026-10-22**
- 실행시간(UTC): **2026-10-23 03:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.27 / 4주 변화 54.0 bp
- IG OAS (BAMLC0A0CM): 0.88 / 4주 변화 11.0 bp
- 10Y Real Yield (DFII10): 2.76 / 4주 변화 0.0 bp
- VIX (VIXCLS): 16.68
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.190808
- MA60: 8.447548
- gap: -14.88%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.426999
- MA60: 0.41142
- gap: 3.79%
- MA60_slope_proxy: 0.023271
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-22**
- 실행시간(UTC): **2026-10-23 03:00:54**

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
- TERM_SPREAD_10Y_POLICY: 160.16 bp / 4주 변화 16.09 bp
- CURVE_10s5s: 38.98 bp / 4주 변화 -2.11 bp

## NWG Price
- close: 648.6
- MA50: 681.9536 / gap50: -4.89%
- MA200: 635.5038 / gap200: 2.06%

## Relative Strength
- RS vs FTSE gap: -5.55% / slope_proxy: -0.000227
- RS vs Peers gap: 2.91% / slope_proxy: 0.018427

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-23 03:01:04**

## Commodity Regime

- WTI ref (CL=F): 99.76 / 5D 1.83%
- Brent ref (BZ=F): 113.40 / 5D 7.06%
- Brent Tier: **>=90**
- Brent-WTI spread: 13.64
- Gas ref (NG=F): 2.76 / 5D -14.74%

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

- close: 62.50
- MA20 / MA60 / MA200: 59.62 / 59.04 / 55.06
- gap20 / gap60: 4.83% / 5.86%
- 5D return: 3.02%
- 20D high/low: 62.92 / 54.94

### Relative Strength

- ratio: 0.924967
- ratio_MA60: 0.935970
- ratio_gap: -1.18%
- ratio_slope_proxy(20d): -0.011412

### Volume (if available)

- volume: 8091600.00
- volume_MA20: 8881150.00
- volume_ratio: 0.91

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 25.62
- MA20 / MA60 / MA200: 23.89 / 20.80 / 18.31
- gap20 / gap60: 7.24% / 23.19%
- 5D return: 1.26%
- 20D high/low: 26.00 / 20.37

### Relative Strength

- ratio: 0.612186
- ratio_MA60: 0.547610
- ratio_gap: 11.79%
- ratio_slope_proxy(20d): 0.032762

### Volume (if available)

- volume: 13122200.00
- volume_MA20: 23613070.00
- volume_ratio: 0.56

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

- close: 6.08
- MA20 / MA60 / MA200: 5.53 / 5.61 / 5.79
- gap20 / gap60: 9.89% / 8.37%
- 5D return: 10.34%
- 20D high/low: 6.08 / 5.17

### Relative Strength

- ratio: 0.016127
- ratio_MA60: 0.013988
- ratio_gap: 15.29%
- ratio_slope_proxy(20d): 0.000225

### Volume (if available)

- volume: 54709900.00
- volume_MA20: 40242095.00
- volume_ratio: 1.36

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.81
- MA20 / MA60 / MA200: 12.98 / 13.70 / 12.46
- gap20 / gap60: -1.31% / -6.50%
- 5D return: 2.48%
- 20D high/low: 13.84 / 12.50

### Relative Strength

- ratio: 0.044633
- ratio_MA60: 0.049842
- ratio_gap: -10.45%
- ratio_slope_proxy(20d): -0.001003

### Volume (if available)

- volume: 19501000.00
- volume_MA20: 13524890.00
- volume_ratio: 1.44

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

- 데이터 기준일(주가): **2026-10-22**
- 실행시간(UTC): **2026-10-23 03:01:10**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 54.0 bp / latest 3.27
- IG OAS 4주 변화: 11.0 bp / latest 0.88
- 10Y Real Yield 4주 변화: 0.0 bp / latest 2.76
- VIX: 16.68
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -5.05% / slope_proxy: 0.007284
- GDXJ/GLD gap: -8.34% / slope_proxy: 0.010494

## VZLA (Vizsla Silver)
- close: 3.19 | RSI14: 37.153239 | ATR14%: 5.63%
- MA20 gap: -8.66% | MA50 gap: -15.38% | MA200 gap: -16.61%
- vol_ratio(Volume/Vol20): 1.28736 | gap_open: 3.57%
- RS vs SILJ gap: 3.99% / slope_proxy: 0.001324
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
- close: 7.13 | RSI14: 32.78557 | ATR14%: 7.76%
- MA20 gap: -16.93% | MA50 gap: -21.38% | MA200 gap: -19.98%
- vol_ratio(Volume/Vol20): 1.664324 | gap_open: 5.39%
- SilverMarginGate: SI=54.259998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -2.08% / slope_proxy: 0.022519
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
- close: 15.76 | RSI14: 33.069107 | ATR14%: 7.85%
- MA20 gap: -13.37% | MA50 gap: -26.24% | MA200 gap: -48.29%
- vol_ratio(Volume/Vol20): 0.882517 | gap_open: 5.08%
- RS vs SILJ gap: -11.73% / slope_proxy: -0.050006
- RS vs GDXJ gap: -15.60% / slope_proxy: -0.017051
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

- 실행시간(UTC): **2026-10-23 03:01:24**
- 데이터 기준일(주가): **2026-10-22**

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

- HY OAS: 3.27 / 4주 변화 0.54 bp-ish / 2026-10-21
- IG OAS: 0.88 / 4주 변화 0.11 bp-ish / 2026-10-21
- 10Y Real Yield: 2.76 / 4주 변화 0.13 bp-ish / 2026-10-21
- VIX: 16.68 / 4주 변화 1.50 / 2026-10-21
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-16

### Leadership ratios

- GDX/GLD: gap -4.48% / slope_proxy -6.22%
- GDXJ/GLD: gap -8.34% / slope_proxy -10.91%
- SILJ/SLV: gap -5.05% / slope_proxy -4.63%
- Gold breadth proxy: above50 0.00%, above200 15.38%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.02 | RSI14: 31.33 | ATR14%: 4.74%
- MA20/50/200 gap: -11.55% / -17.92% / -0.27%
- 5D return: -10.29% | 20D drawdown: -19.64% | vol_ratio: 2.36
- RS vs GDXJ: gap -2.08% / slope_proxy -3.83%
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
- close: 5.67 | RSI14: 26.91 | ATR14%: 6.54%
- MA20/50/200 gap: -16.36% / -22.42% / -19.34%
- 5D return: -11.54% | 20D drawdown: -25.00% | vol_ratio: 1.26
- RS vs GDXJ: gap -6.96% / slope_proxy -11.19%
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
- close: 0.84 | RSI14: 31.91 | ATR14%: 8.50%
- MA20/50/200 gap: -17.00% / -35.96% / -42.15%
- 5D return: -10.64% | 20D drawdown: -35.38% | vol_ratio: 2.00
- RS vs GDXJ: gap -24.87% / slope_proxy -23.49%
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
- close: 1.78 | RSI14: 25.61 | ATR14%: 7.02%
- MA20/50/200 gap: -17.88% / -25.83% / -10.61%
- 5D return: -14.42% | 20D drawdown: -30.47% | vol_ratio: 1.79
- RS vs GDXJ: gap -10.68% / slope_proxy -17.67%
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
- close: 23.86 | RSI14: 33.57 | ATR14%: 5.50%
- MA20/50/200 gap: -10.21% / -12.65% / 15.91%
- 5D return: -8.23% | 20D drawdown: -16.19% | vol_ratio: 1.34
- RS vs SILJ: gap 7.95% / slope_proxy 3.55%
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
- close: 14.11 | RSI14: 25.04 | ATR14%: 5.44%
- MA20/50/200 gap: -13.43% / -22.85% / -25.39%
- 5D return: -9.32% | 20D drawdown: -22.43% | vol_ratio: 1.14
- RS vs SILJ: gap -3.99% / slope_proxy -4.16%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **51.6**
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
- close: 7.13 | RSI14: 29.98 | ATR14%: 7.16%
- MA20/50/200 gap: -16.93% / -21.38% / -19.98%
- 5D return: -14.30% | 20D drawdown: -24.79% | vol_ratio: 1.66
- RS vs SILJ: gap -2.08% / slope_proxy -7.08%
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
- close: 3.19 | RSI14: 34.33 | ATR14%: 5.26%
- MA20/50/200 gap: -8.66% / -15.38% / -16.61%
- 5D return: -3.92% | 20D drawdown: -19.24% | vol_ratio: 1.29
- RS vs SILJ: gap 3.99% / slope_proxy -0.22%
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
- close: 7.65 | RSI14: 33.79 | ATR14%: 5.08%
- MA20/50/200 gap: -9.57% / -20.86% / -22.33%
- 5D return: -7.72% | 20D drawdown: -18.53% | vol_ratio: 0.93
- RS vs SILJ: gap -2.27% / slope_proxy 0.66%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.19 | RSI14: 19.70 | ATR14%: 7.34%
- MA20/50/200 gap: -22.58% / -33.03% / -44.79%
- 5D return: -17.36% | 20D drawdown: -33.95% | vol_ratio: 1.63
- RS vs SILJ: gap -17.75% / slope_proxy -18.40%
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
- close: 4.77 | RSI14: 32.59 | ATR14%: 5.87%
- MA20/50/200 gap: -11.38% / -24.66% / -31.17%
- 5D return: -8.09% | 20D drawdown: -19.70% | vol_ratio: 1.30
- RS vs SILJ: gap -8.06% / slope_proxy -0.78%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.76 | RSI14: 33.35 | ATR14%: 6.98%
- MA20/50/200 gap: -13.37% / -26.24% / -48.29%
- 5D return: -9.53% | 20D drawdown: -26.63% | vol_ratio: 0.88
- RS vs SILJ: gap -11.73% / slope_proxy -9.35%
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
