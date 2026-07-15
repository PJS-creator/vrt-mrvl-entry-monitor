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

- 실행시간(UTC): **2026-07-15 03:01:16**
- 데이터 기준일(일봉): **2026-07-14**
- 데이터 기준일(주봉): **2026-07-13**
- VXN 기준일: **2026-07-13** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 719.71
- Weekly RSI14: **62.51**
- 52W MA: 626.98 / gap: **14.79%**
- 104W MA gap: **28.14%**
- 52W MA 13W slope: **8.21%**
- VXN: **27.30** / 5D change: 0.49

## Daily trigger: 실제 매수 타이밍

- QQQ close: 719.71
- Daily RSI14: **50.79**
- 20D gap: **-0.32%**
- 50D gap: **0.43%**
- 200D gap: **12.84%**
- MACD hist: -1.2854 / change: 0.3040
- ATR14%: **2.09%**
- 20D high drawdown: **-3.16%**

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

- 데이터 기준일(주가): **2026-07-14**
- 실행시간(UTC): **2026-07-15 03:00:52**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 3.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.36 / 4주 변화 21.0 bp
- VIX (VIXCLS): 17.16
- NFCI: -0.515

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.837329
- MA60: 9.573618
- gap: 2.75%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.370542
- MA60: 0.379007
- gap: -2.23%
- MA60_slope_proxy: 0.054594
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-13**
- 실행시간(UTC): **2026-07-15 03:00:54**

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
- TERM_SPREAD_10Y_POLICY: 111.81 bp / 4주 변화 5.25 bp
- CURVE_10s5s: 48.13 bp / 4주 변화 2.06 bp

## NWG Price
- close: 655.0
- MA50: 614.1131 / gap50: 6.66%
- MA200: 603.9678 / gap200: 8.45%

## Relative Strength
- RS vs FTSE gap: 6.60% / slope_proxy: 0.002391
- RS vs Peers gap: 0.51% / slope_proxy: -0.006402

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-15 03:01:02**

## Commodity Regime

- WTI ref (CL=F): 80.38 / 5D 14.11%
- Brent ref (BZ=F): 86.04 / 5D 16.02%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.66
- Gas ref (NG=F): 2.92 / 5D -10.66%

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

- close: 54.57
- MA20 / MA60 / MA200: 51.63 / 55.38 / 49.19
- gap20 / gap60: 5.69% / -1.46%
- 5D return: 5.59%
- 20D high/low: 54.81 / 47.94

### Relative Strength

- ratio: 0.958209
- ratio_MA60: 0.981154
- ratio_gap: -2.34%
- ratio_slope_proxy(20d): -0.027802

### Volume (if available)

- volume: 11115162.00
- volume_MA20: 10230178.10
- volume_ratio: 1.09

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.92
- MA20 / MA60 / MA200: 16.80 / 18.81 / 15.70
- gap20 / gap60: 6.64% / -4.75%
- 5D return: 7.56%
- 20D high/low: 17.92 / 15.99

### Relative Strength

- ratio: 0.497363
- ratio_MA60: 0.518046
- ratio_gap: -3.99%
- ratio_slope_proxy(20d): -0.014308

### Volume (if available)

- volume: 13028019.00
- volume_MA20: 15808970.95
- volume_ratio: 0.82

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

- close: 5.31
- MA20 / MA60 / MA200: 5.22 / 6.04 / 5.19
- gap20 / gap60: 1.69% / -12.02%
- 5D return: 5.78%
- 20D high/low: 5.83 / 4.87

### Relative Strength

- ratio: 0.013778
- ratio_MA60: 0.014523
- ratio_gap: -5.13%
- ratio_slope_proxy(20d): -0.000820

### Volume (if available)

- volume: 37610217.00
- volume_MA20: 39299800.85
- volume_ratio: 0.96

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

- close: 13.23
- MA20 / MA60 / MA200: 11.51 / 12.34 / 10.66
- gap20 / gap60: 14.92% / 7.20%
- 5D return: 14.15%
- 20D high/low: 13.36 / 10.51

### Relative Strength

- ratio: 0.049919
- ratio_MA60: 0.050234
- ratio_gap: -0.63%
- ratio_slope_proxy(20d): -0.002085

### Volume (if available)

- volume: 13706136.00
- volume_MA20: 14254716.80
- volume_ratio: 0.96

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-14**
- 실행시간(UTC): **2026-07-15 03:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 3.0 bp / latest 2.69
- IG OAS 4주 변화: 5.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.36
- VIX: 17.16
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.97% / slope_proxy: 0.009394
- GDXJ/GLD gap: -3.86% / slope_proxy: -0.00376

## VZLA (Vizsla Silver)
- close: 3.2 | RSI14: 46.42815 | ATR14%: 6.37%
- MA20 gap: -2.82% | MA50 gap: -7.59% | MA200 gap: -23.84%
- vol_ratio(Volume/Vol20): 0.800244 | gap_open: 3.31%
- RS vs SILJ gap: 4.48% / slope_proxy: 0.005117
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
- close: 6.5 | RSI14: 44.247589 | ATR14%: 7.16%
- MA20 gap: -3.67% | MA50 gap: -13.77% | MA200 gap: -23.56%
- vol_ratio(Volume/Vol20): 0.758217 | gap_open: 2.52%
- SilverMarginGate: SI=58.880001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.99% / slope_proxy: -0.005169
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
- close: 21.860001 | RSI14: 39.658463 | ATR14%: 9.10%
- MA20 gap: -6.27% | MA50 gap: -26.22% | MA200 gap: -18.76%
- vol_ratio(Volume/Vol20): 0.528509 | gap_open: 6.95%
- RS vs SILJ gap: -19.67% / slope_proxy: -0.103849
- RS vs GDXJ gap: -19.59% / slope_proxy: -0.022626
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

- 실행시간(UTC): **2026-07-15 03:01:15**
- 데이터 기준일(주가): **2026-07-14**

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

- HY OAS: 2.69 / 4주 변화 0.03 bp-ish / 2026-07-13
- IG OAS: 0.78 / 4주 변화 0.05 bp-ish / 2026-07-13
- 10Y Real Yield: 2.36 / 4주 변화 0.20 bp-ish / 2026-07-13
- VIX: 17.16 / 4주 변화 0.96 / 2026-07-13
- NFCI: -0.52 / 4주 변화 0.03 / 2026-07-03

### Leadership ratios

- GDX/GLD: gap -3.91% / slope_proxy -6.43%
- GDXJ/GLD: gap -3.86% / slope_proxy -6.31%
- SILJ/SLV: gap 5.97% / slope_proxy 3.99%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.37 | RSI14: 43.84 | ATR14%: 5.51%
- MA20/50/200 gap: -3.95% / -6.38% / 8.79%
- 5D return: -4.66% | 20D drawdown: -12.16% | vol_ratio: 0.78
- RS vs GDXJ: gap 5.68% / slope_proxy 5.57%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.97 | RSI14: 72.73 | ATR14%: 6.85%
- MA20/50/200 gap: 16.71% / 8.09% / 12.66%
- 5D return: 13.22% | 20D drawdown: -4.37% | vol_ratio: 0.64
- RS vs GDXJ: gap 23.23% / slope_proxy 26.54%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 30 | OverallScore: **48.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 4.97 | RSI14: 43.18 | ATR14%: 5.38%
- MA20/50/200 gap: -7.40% / -16.83% / -28.11%
- 5D return: -6.05% | 20D drawdown: -19.19% | vol_ratio: 0.54
- RS vs GDXJ: gap -8.50% / slope_proxy -6.77%
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
- close: 1.10 | RSI14: 38.98 | ATR14%: 7.53%
- MA20/50/200 gap: -9.87% / -15.48% / -26.99%
- 5D return: -6.78% | 20D drawdown: -25.17% | vol_ratio: 0.43
- RS vs GDXJ: gap -4.89% / slope_proxy -10.32%
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
- close: 20.04 | RSI14: 58.46 | ATR14%: 6.65%
- MA20/50/200 gap: 3.15% / 5.40% / 26.93%
- 5D return: 6.71% | 20D drawdown: -4.80% | vol_ratio: 0.74
- RS vs SILJ: gap 20.25% / slope_proxy 11.40%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.08 | RSI14: 51.04 | ATR14%: 6.00%
- MA20/50/200 gap: -2.90% / -9.93% / -15.56%
- 5D return: 0.75% | 20D drawdown: -13.12% | vol_ratio: 0.98
- RS vs SILJ: gap 0.95% / slope_proxy 1.81%
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
- close: 15.50 | RSI14: 53.78 | ATR14%: 5.34%
- MA20/50/200 gap: -1.24% / -6.97% / -14.56%
- 5D return: -0.39% | 20D drawdown: -7.30% | vol_ratio: 0.89
- RS vs SILJ: gap 3.40% / slope_proxy 6.79%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.20 | RSI14: 44.90 | ATR14%: 6.01%
- MA20/50/200 gap: -2.82% / -7.59% / -23.84%
- 5D return: 3.56% | 20D drawdown: -13.28% | vol_ratio: 0.80
- RS vs SILJ: gap 4.48% / slope_proxy 0.64%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **57.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.98 | RSI14: 51.61 | ATR14%: 6.64%
- MA20/50/200 gap: -4.27% / -8.84% / -9.82%
- 5D return: -1.48% | 20D drawdown: -13.96% | vol_ratio: 0.60
- RS vs SILJ: gap 2.14% / slope_proxy 0.50%
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
- close: 6.50 | RSI14: 47.58 | ATR14%: 5.96%
- MA20/50/200 gap: -3.67% / -13.77% / -23.56%
- 5D return: 2.04% | 20D drawdown: -18.44% | vol_ratio: 0.76
- RS vs SILJ: gap -3.99% / slope_proxy -1.18%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.20 | RSI14: 35.54 | ATR14%: 7.86%
- MA20/50/200 gap: -13.10% / -23.61% / -26.67%
- 5D return: -4.11% | 20D drawdown: -28.57% | vol_ratio: 0.63
- RS vs SILJ: gap -14.39% / slope_proxy -16.30%
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
- close: 21.86 | RSI14: 44.38 | ATR14%: 7.85%
- MA20/50/200 gap: -6.27% / -26.22% / -18.76%
- 5D return: 0.69% | 20D drawdown: -21.48% | vol_ratio: 0.53
- RS vs SILJ: gap -19.67% / slope_proxy -9.87%
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
