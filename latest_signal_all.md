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

- 실행시간(UTC): **2026-07-22 15:01:58**
- 데이터 기준일(일봉): **2026-07-22**
- 데이터 기준일(주봉): **2026-07-20**
- VXN 기준일: **2026-07-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 707.37
- Weekly RSI14: **58.38**
- 52W MA: 629.28 / gap: **12.41%**
- 104W MA gap: **25.46%**
- 52W MA 13W slope: **7.91%**
- VXN: **26.66** / 5D change: 0.38

## Daily trigger: 실제 매수 타이밍

- QQQ close: 707.37
- Daily RSI14: **47.48**
- 20D gap: **-0.98%**
- 50D gap: **-1.59%**
- 200D gap: **10.34%**
- MACD hist: -2.0506 / change: 0.4857
- ATR14%: **2.01%**
- 20D high drawdown: **-3.94%**

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

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-22 15:01:02**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 -2.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.35 / 4주 변화 7.0 bp
- VIX (VIXCLS): 17.05
- NFCI: -0.552

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.71216
- MA60: 9.648715
- gap: 0.66%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.364142
- MA60: 0.381431
- gap: -4.53%
- MA60_slope_proxy: 0.034506
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-22 15:01:06**

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
- TERM_SPREAD_10Y_POLICY: 126.95 bp / 4주 변화 23.65 bp
- CURVE_10s5s: 47.38 bp / 4주 변화 1.78 bp

## NWG Price
- close: 687.4
- MA50: 628.036 / gap50: 9.45%
- MA200: 608.8222 / gap200: 12.91%

## Relative Strength
- RS vs FTSE gap: 8.04% / slope_proxy: 0.00221
- RS vs Peers gap: 0.73% / slope_proxy: -0.003306

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-22 15:01:20**

## Commodity Regime

- WTI ref (CL=F): 86.89 / 5D 9.16%
- Brent ref (BZ=F): 93.97 / 5D 10.62%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.08
- Gas ref (NG=F): 2.91 / 5D -0.38%

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

- close: 57.62
- MA20 / MA60 / MA200: 52.35 / 55.32 / 49.46
- gap20 / gap60: 10.06% / 4.15%
- 5D return: 7.16%
- 20D high/low: 57.62 / 47.94

### Relative Strength

- ratio: 0.968810
- ratio_MA60: 0.976352
- ratio_gap: -0.77%
- ratio_slope_proxy(20d): -0.027453

### Volume (if available)

- volume: 2198135.00
- volume_MA20: 9192676.75
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.92
- MA20 / MA60 / MA200: 17.15 / 18.56 / 15.86
- gap20 / gap60: 10.33% / 1.96%
- 5D return: 5.96%
- 20D high/low: 18.92 / 15.99

### Relative Strength

- ratio: 0.525184
- ratio_MA60: 0.517666
- ratio_gap: 1.45%
- ratio_slope_proxy(20d): -0.010902

### Volume (if available)

- volume: 4937405.00
- volume_MA20: 14302375.25
- volume_ratio: 0.35

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.33
- MA20 / MA60 / MA200: 5.12 / 5.95 / 5.25
- gap20 / gap60: 4.12% / -10.36%
- 5D return: 2.60%
- 20D high/low: 5.37 / 4.87

### Relative Strength

- ratio: 0.013608
- ratio_MA60: 0.014427
- ratio_gap: -5.68%
- ratio_slope_proxy(20d): -0.000666

### Volume (if available)

- volume: 9405269.00
- volume_MA20: 37543688.45
- volume_ratio: 0.25

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

- close: 14.62
- MA20 / MA60 / MA200: 12.26 / 12.51 / 10.64
- gap20 / gap60: 19.22% / 16.85%
- 5D return: 13.25%
- 20D high/low: 14.62 / 10.51

### Relative Strength

- ratio: 0.055053
- ratio_MA60: 0.050763
- ratio_gap: 8.45%
- ratio_slope_proxy(20d): -0.000816

### Volume (if available)

- volume: 5126849.00
- volume_MA20: 13386572.45
- volume_ratio: 0.38

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

- 데이터 기준일(주가): **2026-07-22**
- 실행시간(UTC): **2026-07-22 15:01:36**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -2.0 bp / latest 2.69
- IG OAS 4주 변화: 4.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 7.0 bp / latest 2.35
- VIX: 17.05
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 5.80% / slope_proxy: 0.008515
- GDXJ/GLD gap: -1.75% / slope_proxy: -0.008468

## VZLA (Vizsla Silver)
- close: 3.45 | RSI14: 56.42208 | ATR14%: 5.58%
- MA20 gap: 8.24% | MA50 gap: 0.37% | MA200 gap: -17.24%
- vol_ratio(Volume/Vol20): 0.381911 | gap_open: 0.30%
- RS vs SILJ gap: 7.58% / slope_proxy: 0.006104
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
- close: 6.78 | RSI14: 51.930588 | ATR14%: 6.42%
- MA20 gap: 5.34% | MA50 gap: -6.90% | MA200 gap: -19.86%
- vol_ratio(Volume/Vol20): 0.292216 | gap_open: 2.29%
- SilverMarginGate: SI=60.505001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.69% / slope_proxy: -0.005859
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
- close: 21.809999 | RSI14: 45.82571 | ATR14%: 8.71%
- MA20 gap: 0.99% | MA50 gap: -20.63% | MA200 gap: -20.16%
- vol_ratio(Volume/Vol20): 0.3485 | gap_open: 1.64%
- RS vs SILJ gap: -18.42% / slope_proxy: -0.125574
- RS vs GDXJ gap: -19.06% / slope_proxy: -0.028037
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

- 실행시간(UTC): **2026-07-22 15:01:56**
- 데이터 기준일(주가): **2026-07-22**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

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

- HY OAS: 2.69 / 4주 변화 -0.02 bp-ish / 2026-07-21
- IG OAS: 0.78 / 4주 변화 0.04 bp-ish / 2026-07-21
- 10Y Real Yield: 2.35 / 4주 변화 0.14 bp-ish / 2026-07-20
- VIX: 17.05 / 4주 변화 -2.44 / 2026-07-21
- NFCI: -0.55 / 4주 변화 -0.05 / 2026-07-17

### Leadership ratios

- GDX/GLD: gap -1.97% / slope_proxy -0.37%
- GDXJ/GLD: gap -1.75% / slope_proxy 1.63%
- SILJ/SLV: gap 5.82% / slope_proxy -0.42%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 15.38%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.44 | RSI14: 49.14 | ATR14%: 4.93%
- MA20/50/200 gap: 0.86% / -4.54% / 9.07%
- 5D return: 2.76% | 20D drawdown: -5.94% | vol_ratio: 0.21
- RS vs GDXJ: gap 1.54% / slope_proxy -3.39%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 30 | OverallScore: **66.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs GDXJ)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.93 | RSI14: 66.29 | ATR14%: 7.40%
- MA20/50/200 gap: 10.22% / 5.28% / 8.17%
- 5D return: 1.58% | 20D drawdown: -6.31% | vol_ratio: 0.30
- RS vs GDXJ: gap 13.58% / slope_proxy 21.63%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.46 | RSI14: 50.24 | ATR14%: 4.70%
- MA20/50/200 gap: 5.44% / -5.36% / -20.74%
- 5D return: 10.08% | 20D drawdown: -5.04% | vol_ratio: 0.40
- RS vs GDXJ: gap -1.86% / slope_proxy 2.51%
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
- close: 1.16 | RSI14: 43.64 | ATR14%: 6.07%
- MA20/50/200 gap: 1.22% / -8.17% / -22.46%
- 5D return: 5.45% | 20D drawdown: -10.77% | vol_ratio: 0.20
- RS vs GDXJ: gap -3.26% / slope_proxy -6.69%
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
- close: 20.55 | RSI14: 57.78 | ATR14%: 6.20%
- MA20/50/200 gap: 6.94% / 7.42% / 28.18%
- 5D return: 4.05% | 20D drawdown: 0.00% | vol_ratio: 0.46
- RS vs SILJ: gap 15.96% / slope_proxy 14.63%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **67.5**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.52 | RSI14: 52.31 | ATR14%: 5.68%
- MA20/50/200 gap: 5.86% / -2.96% / -10.93%
- 5D return: 7.10% | 20D drawdown: -0.41% | vol_ratio: 0.58
- RS vs SILJ: gap 3.26% / slope_proxy 5.59%
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
- close: 16.01 | RSI14: 53.16 | ATR14%: 5.32%
- MA20/50/200 gap: 4.22% / -1.81% / -12.17%
- 5D return: 3.59% | 20D drawdown: -2.70% | vol_ratio: 0.16
- RS vs SILJ: gap 3.71% / slope_proxy 5.33%
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
- close: 3.45 | RSI14: 56.38 | ATR14%: 5.41%
- MA20/50/200 gap: 8.24% / 0.37% / -17.24%
- 5D return: 7.81% | 20D drawdown: 0.00% | vol_ratio: 0.38
- RS vs SILJ: gap 7.58% / slope_proxy 5.94%
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
- close: 6.36 | RSI14: 50.07 | ATR14%: 6.21%
- MA20/50/200 gap: 5.72% / -1.53% / -4.29%
- 5D return: 7.34% | 20D drawdown: -3.27% | vol_ratio: 0.58
- RS vs SILJ: gap 5.44% / slope_proxy 7.77%
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
- close: 6.78 | RSI14: 53.07 | ATR14%: 5.97%
- MA20/50/200 gap: 5.34% / -6.90% / -19.86%
- 5D return: 6.77% | 20D drawdown: -0.44% | vol_ratio: 0.29
- RS vs SILJ: gap -1.69% / slope_proxy 2.29%
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
- close: 4.38 | RSI14: 43.58 | ATR14%: 7.29%
- MA20/50/200 gap: 0.13% / -16.40% / -23.66%
- 5D return: 8.69% | 20D drawdown: -10.43% | vol_ratio: 0.50
- RS vs SILJ: gap -11.59% / slope_proxy -8.27%
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
- close: 21.81 | RSI14: 45.68 | ATR14%: 7.93%
- MA20/50/200 gap: 0.99% / -20.63% / -20.16%
- 5D return: 4.40% | 20D drawdown: -8.13% | vol_ratio: 0.35
- RS vs SILJ: gap -18.42% / slope_proxy -4.02%
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
