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

- 실행시간(UTC): **2026-10-21 15:01:22**
- 데이터 기준일(일봉): **2026-10-21**
- 데이터 기준일(주봉): **2026-10-19**
- VXN 기준일: **2026-10-20** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 723.65
- Weekly RSI14: **55.27**
- 52W MA: 663.20 / gap: **9.11%**
- 104W MA gap: **21.73%**
- 52W MA 13W slope: **5.58%**
- VXN: **25.22** / 5D change: 4.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 723.66
- Daily RSI14: **45.10**
- 20D gap: **-2.08%**
- 50D gap: **-0.37%**
- 200D gap: **7.17%**
- MACD hist: -4.3922 / change: 0.5978
- ATR14%: **1.47%**
- 20D high drawdown: **-4.74%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **True**
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

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-21 15:00:55**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DFII10 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.29 / 4주 변화 63.0 bp
- IG OAS (BAMLC0A0CM): 0.87 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.8 / 4주 변화 18.0 bp
- VIX (VIXCLS): 17.31
- NFCI: -0.496

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.679279
- MA60: 8.451728
- gap: -9.14%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.438519
- MA60: 0.409684
- gap: 7.04%
- MA60_slope_proxy: 0.021154
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-21 15:00:58**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 162.4 bp / 4주 변화 21.1 bp
- CURVE_10s5s: 40.62 bp / 4주 변화 1.7 bp

## NWG Price
- close: 647.8
- MA50: 681.9376 / gap50: -5.01%
- MA200: 635.4998 / gap200: 1.94%

## Relative Strength
- RS vs FTSE gap: -5.65% / slope_proxy: -0.000228
- RS vs Peers gap: 2.96% / slope_proxy: 0.018435

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-21 15:01:08**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DHHNGSP failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DTWEXBGS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED VXEWZCLS failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 97.74 / 5D 2.79%
- Brent ref (BZ=F): 109.04 / 5D 2.81%
- Brent Tier: **>=90**
- Brent-WTI spread: 11.30
- Gas ref (NG=F): 2.84 / 5D -11.10%

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

- close: 63.02
- MA20 / MA60 / MA200: 59.42 / 58.94 / 54.96
- gap20 / gap60: 6.06% / 6.93%
- 5D return: 2.62%
- 20D high/low: 63.02 / 54.94

### Relative Strength

- ratio: 0.923032
- ratio_MA60: 0.936550
- ratio_gap: -1.44%
- ratio_slope_proxy(20d): -0.010640

### Volume (if available)

- volume: 1850910.00
- volume_MA20: 8672085.50
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 25.93
- MA20 / MA60 / MA200: 23.66 / 20.68 / 18.24
- gap20 / gap60: 9.60% / 25.44%
- 5D return: -0.02%
- 20D high/low: 26.00 / 20.37

### Relative Strength

- ratio: 0.607377
- ratio_MA60: 0.545956
- ratio_gap: 11.25%
- ratio_slope_proxy(20d): 0.032933

### Volume (if available)

- volume: 4140174.00
- volume_MA20: 23152783.70
- volume_ratio: 0.18

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

- close: 5.96
- MA20 / MA60 / MA200: 5.50 / 5.59 / 5.78
- gap20 / gap60: 8.43% / 6.62%
- 5D return: 6.81%
- 20D high/low: 5.96 / 5.17

### Relative Strength

- ratio: 0.015169
- ratio_MA60: 0.013941
- ratio_gap: 8.81%
- ratio_slope_proxy(20d): 0.000188

### Volume (if available)

- volume: 9088385.00
- volume_MA20: 38501399.25
- volume_ratio: 0.24

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

- close: 12.78
- MA20 / MA60 / MA200: 13.00 / 13.70 / 12.43
- gap20 / gap60: -1.71% / -6.77%
- 5D return: -3.73%
- 20D high/low: 13.84 / 12.50

### Relative Strength

- ratio: 0.045156
- ratio_MA60: 0.049938
- ratio_gap: -9.58%
- ratio_slope_proxy(20d): -0.000885

### Volume (if available)

- volume: 4430528.00
- volume_MA20: 12773216.40
- volume_ratio: 0.35

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

- 데이터 기준일(주가): **2026-10-21**
- 실행시간(UTC): **2026-10-21 15:01:12**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED BAMLC0A0CM failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.
- FRED DFII10 failed (Error tokenizing data. C error: Expected 1 fields in line 5, saw 3
), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 63.0 bp / latest 3.29
- IG OAS 4주 변화: 10.0 bp / latest 0.87
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.8
- VIX: 17.31
- NFCI: -0.496

### Leadership ratios
- SILJ/SLV gap: -3.38% / slope_proxy: 0.007238
- GDXJ/GLD gap: -4.96% / slope_proxy: 0.010805

## VZLA (Vizsla Silver)
- close: 3.305 | RSI14: 39.769897 | ATR14%: 5.17%
- MA20 gap: -6.30% | MA50 gap: -12.59% | MA200 gap: -13.90%
- vol_ratio(Volume/Vol20): 0.168672 | gap_open: 1.23%
- RS vs SILJ gap: 0.80% / slope_proxy: 0.00139
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
- close: 8.18 | RSI14: 42.740457 | ATR14%: 6.13%
- MA20 gap: -5.69% | MA50 gap: -10.15% | MA200 gap: -8.37%
- vol_ratio(Volume/Vol20): 0.221338 | gap_open: 0.85%
- SilverMarginGate: SI=57.709999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 5.23% / slope_proxy: 0.022928
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

## HYMC (Hycroft Mining)
- close: 17.07 | RSI14: 38.137729 | ATR14%: 7.03%
- MA20 gap: -7.46% | MA50 gap: -20.97% | MA200 gap: -44.10%
- vol_ratio(Volume/Vol20): 0.162878 | gap_open: 1.65%
- RS vs SILJ gap: -10.89% / slope_proxy: -0.050647
- RS vs GDXJ gap: -14.30% / slope_proxy: -0.017333
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

- 실행시간(UTC): **2026-10-21 15:01:21**
- 데이터 기준일(주가): **2026-10-21**

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

- HY OAS: N/A
- IG OAS: N/A
- 10Y Real Yield: N/A
- VIX: 17.31 / 4주 변화 3.10 / 2026-10-20
- NFCI: -0.50 / 4주 변화 0.01 / 2026-10-16

### Leadership ratios

- GDX/GLD: gap -1.71% / slope_proxy -3.55%
- GDXJ/GLD: gap -4.96% / slope_proxy -7.15%
- SILJ/SLV: gap -3.38% / slope_proxy -2.92%
- Gold breadth proxy: above50 0.00%, above200 23.08%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.67 | RSI14: 37.84 | ATR14%: 3.98%
- MA20/50/200 gap: -5.39% / -11.61% / 7.93%
- 5D return: 1.40% | 20D drawdown: -13.65% | vol_ratio: 0.16
- RS vs GDXJ: gap -0.26% / slope_proxy -3.74%
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
- close: 6.24 | RSI14: 31.86 | ATR14%: 5.58%
- MA20/50/200 gap: -9.28% / -14.91% / -11.34%
- 5D return: -2.19% | 20D drawdown: -18.96% | vol_ratio: 0.08
- RS vs GDXJ: gap -3.57% / slope_proxy -8.57%
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
- close: 0.94 | RSI14: 35.29 | ATR14%: 7.60%
- MA20/50/200 gap: -9.55% / -29.36% / -35.76%
- 5D return: -0.53% | 20D drawdown: -28.08% | vol_ratio: 0.15
- RS vs GDXJ: gap -21.66% / slope_proxy -17.59%
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
- close: 1.97 | RSI14: 29.17 | ATR14%: 5.95%
- MA20/50/200 gap: -10.92% / -18.18% / -1.16%
- 5D return: -3.90% | 20D drawdown: -24.81% | vol_ratio: 0.27
- RS vs GDXJ: gap -7.09% / slope_proxy -15.17%
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
- close: 26.23 | RSI14: 45.22 | ATR14%: 4.50%
- MA20/50/200 gap: -1.98% / -4.24% / 27.69%
- 5D return: 3.19% | 20D drawdown: -7.87% | vol_ratio: 0.12
- RS vs SILJ: gap 11.36% / slope_proxy 7.37%
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
- close: 8.18 | RSI14: 41.74 | ATR14%: 5.54%
- MA20/50/200 gap: -5.69% / -10.15% / -8.37%
- 5D return: 2.76% | 20D drawdown: -13.71% | vol_ratio: 0.22
- RS vs SILJ: gap 5.23% / slope_proxy 4.88%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **53.3**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.21 | RSI14: 42.08 | ATR14%: 4.37%
- MA20/50/200 gap: -3.76% / -15.57% / -16.76%
- 5D return: 4.85% | 20D drawdown: -12.57% | vol_ratio: 0.12
- RS vs SILJ: gap -1.91% / slope_proxy 2.51%
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
- close: 15.10 | RSI14: 32.14 | ATR14%: 4.72%
- MA20/50/200 gap: -8.42% / -17.79% / -20.33%
- 5D return: 1.34% | 20D drawdown: -16.99% | vol_ratio: 0.14
- RS vs SILJ: gap -3.94% / slope_proxy -3.74%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.31 | RSI14: 32.27 | ATR14%: 4.97%
- MA20/50/200 gap: -6.30% / -12.59% / -13.90%
- 5D return: 4.26% | 20D drawdown: -16.33% | vol_ratio: 0.17
- RS vs SILJ: gap 0.80% / slope_proxy -4.06%
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
- close: 3.58 | RSI14: 25.30 | ATR14%: 5.92%
- MA20/50/200 gap: -14.64% / -25.46% / -38.15%
- 5D return: -3.24% | 20D drawdown: -25.88% | vol_ratio: 0.33
- RS vs SILJ: gap -13.87% / slope_proxy -12.51%
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
- close: 5.16 | RSI14: 40.54 | ATR14%: 5.07%
- MA20/50/200 gap: -5.09% / -19.09% / -25.62%
- 5D return: 5.74% | 20D drawdown: -13.13% | vol_ratio: 0.14
- RS vs SILJ: gap -7.14% / slope_proxy -0.14%
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
- close: 17.07 | RSI14: 37.84 | ATR14%: 6.11%
- MA20/50/200 gap: -7.46% / -20.97% / -44.10%
- 5D return: 4.44% | 20D drawdown: -20.53% | vol_ratio: 0.16
- RS vs SILJ: gap -10.89% / slope_proxy -6.54%
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
