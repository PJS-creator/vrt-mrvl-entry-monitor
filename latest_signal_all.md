# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-08 03:01:10**
- 데이터 기준일(일봉): **2026-10-07**
- 데이터 기준일(주봉): **2026-10-05**
- VXN 기준일: **2026-10-06** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 757.73
- Weekly RSI14: **66.42**
- 52W MA: 659.13 / gap: **14.96%**
- 104W MA gap: **28.39%**
- 52W MA 13W slope: **5.76%**
- VXN: **21.15** / 5D change: -0.92

## Daily trigger: 실제 매수 타이밍

- QQQ close: 757.73
- Daily RSI14: **68.16**
- 20D gap: **3.30%**
- 50D gap: **5.11%**
- 200D gap: **13.17%**
- MACD hist: 2.2755 / change: -0.1432
- ATR14%: **1.20%**
- 20D high drawdown: **-0.25%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-08 03:00:42**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.03 / 4주 변화 36.0 bp
- IG OAS (BAMLC0A0CM): 0.83 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.91 / 4주 변화 48.0 bp
- VIX (VIXCLS): 15.01
- NFCI: -0.494

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.582521
- MA60: 8.763076
- gap: -2.06%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.455466
- MA60: 0.393933
- gap: 15.62%
- MA60_slope_proxy: -0.000161
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-08 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 161.34 bp / 4주 변화 25.55 bp
- CURVE_10s5s: 43.23 bp / 4주 변화 -3.66 bp

## NWG Price
- close: 668.4
- MA50: 692.2357 / gap50: -3.44%
- MA200: 635.2506 / gap200: 5.22%

## Relative Strength
- RS vs FTSE gap: -1.18% / slope_proxy: 0.000593
- RS vs Peers gap: 2.05% / slope_proxy: 0.010717

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-08 03:00:51**

## Commodity Regime

- WTI ref (CL=F): 89.86 / 5D -0.62%
- Brent ref (BZ=F): 102.33 / 5D -1.16%
- Brent Tier: **>=90**
- Brent-WTI spread: 12.47
- Gas ref (NG=F): 3.27 / 5D 8.23%

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

- close: 58.21
- MA20 / MA60 / MA200: 58.42 / 57.88 / 53.88
- gap20 / gap60: -0.36% / 0.58%
- 5D return: 5.22%
- 20D high/low: 63.52 / 54.94

### Relative Strength

- ratio: 0.918718
- ratio_MA60: 0.942495
- ratio_gap: -2.52%
- ratio_slope_proxy(20d): -0.008632

### Volume (if available)

- volume: 7117500.00
- volume_MA20: 9513960.00
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 23.99
- MA20 / MA60 / MA200: 21.43 / 19.38 / 17.52
- gap20 / gap60: 11.94% / 23.79%
- 5D return: 14.95%
- 20D high/low: 24.14 / 20.37

### Relative Strength

- ratio: 0.566203
- ratio_MA60: 0.528717
- ratio_gap: 7.09%
- ratio_slope_proxy(20d): 0.029243

### Volume (if available)

- volume: 30323300.00
- volume_MA20: 24318455.00
- volume_ratio: 1.25

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.39
- MA20 / MA60 / MA200: 5.47 / 5.51 / 5.70
- gap20 / gap60: -1.40% / -2.20%
- 5D return: 2.86%
- 20D high/low: 5.94 / 5.17

### Relative Strength

- ratio: 0.014127
- ratio_MA60: 0.013761
- ratio_gap: 2.66%
- ratio_slope_proxy(20d): 0.000027

### Volume (if available)

- volume: 19181600.00
- volume_MA20: 42526765.00
- volume_ratio: 0.45

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 13.05
- MA20 / MA60 / MA200: 13.72 / 13.81 / 12.12
- gap20 / gap60: -4.92% / -5.51%
- 5D return: 3.24%
- 20D high/low: 15.76 / 12.54

### Relative Strength

- ratio: 0.047943
- ratio_MA60: 0.050961
- ratio_gap: -5.92%
- ratio_slope_proxy(20d): 0.001088

### Volume (if available)

- volume: 11875200.00
- volume_MA20: 14318210.00
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-07**
- 실행시간(UTC): **2026-10-08 03:00:57**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 36.0 bp / latest 3.03
- IG OAS 4주 변화: 2.0 bp / latest 0.83
- 10Y Real Yield 4주 변화: 48.0 bp / latest 2.91
- VIX: 15.01
- NFCI: -0.494

### Leadership ratios
- SILJ/SLV gap: -2.55% / slope_proxy: 0.00967
- GDXJ/GLD gap: -1.23% / slope_proxy: 0.01194

## VZLA (Vizsla Silver)
- close: 3.42 | RSI14: 35.007594 | ATR14%: 5.76%
- MA20 gap: -11.02% | MA50 gap: -10.18% | MA200 gap: -13.48%
- vol_ratio(Volume/Vol20): 1.184851 | gap_open: 3.40%
- RS vs SILJ gap: 0.12% / slope_proxy: 0.002974
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
- close: 8.45 | RSI14: 43.302815 | ATR14%: 6.87%
- MA20 gap: -6.24% | MA50 gap: -5.40% | MA200 gap: -6.04%
- vol_ratio(Volume/Vol20): 1.38079 | gap_open: 4.46%
- SilverMarginGate: SI=60.544998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 8.75% / slope_proxy: 0.01941
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
- close: 17.959999 | RSI14: 34.962618 | ATR14%: 7.59%
- MA20 gap: -11.34% | MA50 gap: -20.97% | MA200 gap: -41.82%
- vol_ratio(Volume/Vol20): 0.980943 | gap_open: 5.32%
- RS vs SILJ gap: -12.46% / slope_proxy: -0.05952
- RS vs GDXJ gap: -14.95% / slope_proxy: -0.019577
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

- 실행시간(UTC): **2026-10-08 03:01:09**
- 데이터 기준일(주가): **2026-10-07**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.03 / 4주 변화 0.36 bp-ish / 2026-10-06
- IG OAS: 0.83 / 4주 변화 0.02 bp-ish / 2026-10-06
- 10Y Real Yield: 2.91 / 4주 변화 0.48 bp-ish / 2026-10-06
- VIX: 15.01 / 4주 변화 -0.71 / 2026-10-06
- NFCI: -0.49 / 4주 변화 0.01 / 2026-10-02

### Leadership ratios

- GDX/GLD: gap 0.41% / slope_proxy -6.16%
- GDXJ/GLD: gap -1.23% / slope_proxy -7.26%
- SILJ/SLV: gap -2.55% / slope_proxy -8.43%
- Gold breadth proxy: above50 0.00%, above200 23.08%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.82 | RSI14: 16.40 | ATR14%: 4.13%
- MA20/50/200 gap: -9.89% / -8.77% / 11.90%
- 5D return: -6.07% | 20D drawdown: -16.32% | vol_ratio: 0.84
- RS vs GDXJ: gap 1.53% / slope_proxy 2.13%
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
- close: 6.66 | RSI14: 29.15 | ATR14%: 5.13%
- MA20/50/200 gap: -10.41% / -7.84% / -5.88%
- 5D return: -5.67% | 20D drawdown: -18.68% | vol_ratio: 1.11
- RS vs GDXJ: gap 3.11% / slope_proxy -4.62%
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
- close: 0.95 | RSI14: 18.18 | ATR14%: 9.85%
- MA20/50/200 gap: -23.79% / -31.15% / -35.68%
- 5D return: -10.38% | 20D drawdown: -37.50% | vol_ratio: 1.57
- RS vs GDXJ: gap -24.25% / slope_proxy -26.52%
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
- close: 2.13 | RSI14: 23.08 | ATR14%: 6.44%
- MA20/50/200 gap: -12.69% / -10.53% / 6.69%
- 5D return: -6.17% | 20D drawdown: -23.38% | vol_ratio: 0.83
- RS vs GDXJ: gap -1.50% / slope_proxy -5.76%
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
- close: 26.14 | RSI14: 36.86 | ATR14%: 5.14%
- MA20/50/200 gap: -5.46% / -2.60% / 31.02%
- 5D return: -2.83% | 20D drawdown: -13.96% | vol_ratio: 0.71
- RS vs SILJ: gap 11.27% / slope_proxy 7.31%
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
- close: 8.45 | RSI14: 44.70 | ATR14%: 6.76%
- MA20/50/200 gap: -6.24% / -5.40% / -6.04%
- 5D return: -4.30% | 20D drawdown: -12.80% | vol_ratio: 1.38
- RS vs SILJ: gap 8.75% / slope_proxy 1.74%
- FundamentalScore: 74 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **58.6**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.39 | RSI14: 25.71 | ATR14%: 4.71%
- MA20/50/200 gap: -9.16% / -10.75% / -14.41%
- 5D return: -3.76% | 20D drawdown: -18.13% | vol_ratio: 1.08
- RS vs SILJ: gap 0.36% / slope_proxy -4.48%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.42 | RSI14: 27.13 | ATR14%: 5.49%
- MA20/50/200 gap: -11.02% / -10.18% / -13.48%
- 5D return: -9.76% | 20D drawdown: -20.47% | vol_ratio: 1.18
- RS vs SILJ: gap 0.12% / slope_proxy -0.24%
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
- close: 8.32 | RSI14: 22.55 | ATR14%: 5.61%
- MA20/50/200 gap: -11.23% / -15.14% / -16.23%
- 5D return: -3.03% | 20D drawdown: -20.91% | vol_ratio: 0.79
- RS vs SILJ: gap -4.20% / slope_proxy -7.73%
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
- close: 4.17 | RSI14: 29.11 | ATR14%: 6.20%
- MA20/50/200 gap: -11.61% / -15.13% / -28.95%
- 5D return: -4.36% | 20D drawdown: -20.72% | vol_ratio: 1.02
- RS vs SILJ: gap -4.40% / slope_proxy -4.42%
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
- close: 5.32 | RSI14: 25.87 | ATR14%: 5.03%
- MA20/50/200 gap: -10.96% / -18.98% / -23.99%
- 5D return: -4.14% | 20D drawdown: -25.28% | vol_ratio: 0.90
- RS vs SILJ: gap -9.90% / slope_proxy -12.82%
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
- close: 17.96 | RSI14: 31.91 | ATR14%: 7.01%
- MA20/50/200 gap: -11.34% / -20.97% / -41.82%
- 5D return: -5.67% | 20D drawdown: -20.85% | vol_ratio: 0.98
- RS vs SILJ: gap -12.46% / slope_proxy -2.04%
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
