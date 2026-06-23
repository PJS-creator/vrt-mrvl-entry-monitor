# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-23 15:01:24**
- 데이터 기준일(일봉): **2026-06-23**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 719.55
- Weekly RSI14: **64.53**
- 52W MA: 617.69 / gap: **16.49%**
- 104W MA gap: **29.67%**
- 52W MA 13W slope: **8.52%**
- VXN: **27.67** / 5D change: 0.40

## Daily trigger: 실제 매수 타이밍

- QQQ close: 719.59
- Daily RSI14: **51.04**
- 20D gap: **-1.08%**
- 50D gap: **3.22%**
- 200D gap: **14.46%**
- MACD hist: -1.8902 / change: -0.8642
- ATR14%: **2.24%**
- 20D high drawdown: **-3.45%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

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

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-23 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.66 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.21 / 4주 변화 3.0 bp
- VIX (VIXCLS): 17.28
- NFCI: -0.505

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.599323
- MA60: 9.219549
- gap: 4.12%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.4519
- MA60: 0.347067
- gap: 30.21%
- MA60_slope_proxy: 0.070267
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-23 15:00:51**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **True**
- MacroGreen: **True**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 97.13 bp / 4주 변화 -14.53 bp
- CURVE_10s5s: 44.9 bp / 4주 변화 0.24 bp

## NWG Price
- close: 657.0
- MA50: 595.1331 / gap50: 10.40%
- MA200: 593.7604 / gap200: 10.65%

## Relative Strength
- RS vs FTSE gap: 10.42% / slope_proxy: 0.001122
- RS vs Peers gap: 1.09% / slope_proxy: -0.016789

## Why not today?
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-23 15:01:00**

## Commodity Regime

- WTI ref (CL=F): 73.30 / 5D -9.23%
- Brent ref (BZ=F): 76.99 / 5D -7.43%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.69
- Gas ref (NG=F): 3.21 / 5D 1.97%

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

- close: 52.00
- MA20 / MA60 / MA200: 55.94 / 57.55 / 48.80
- gap20 / gap60: -7.04% / -9.65%
- 5D return: -4.52%
- 20D high/low: 59.37 / 51.82

### Relative Strength

- ratio: 0.960030
- ratio_MA60: 1.003821
- ratio_gap: -4.36%
- ratio_slope_proxy(20d): 0.000035

### Volume (if available)

- volume: 2321753.00
- volume_MA20: 10004057.65
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.93
- MA20 / MA60 / MA200: 17.94 / 19.71 / 15.41
- gap20 / gap60: -5.61% / -14.06%
- 5D return: -2.34%
- 20D high/low: 19.25 / 16.75

### Relative Strength

- ratio: 0.496191
- ratio_MA60: 0.528526
- ratio_gap: -6.12%
- ratio_slope_proxy(20d): 0.005738

### Volume (if available)

- volume: 2186046.00
- volume_MA20: 14929987.30
- volume_ratio: 0.15

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.33
- MA20 / MA60 / MA200: 5.96 / 6.37 / 5.07
- gap20 / gap60: -10.51% / -16.37%
- 5D return: -8.58%
- 20D high/low: 6.48 / 5.31

### Relative Strength

- ratio: 0.013816
- ratio_MA60: 0.015094
- ratio_gap: -8.47%
- ratio_slope_proxy(20d): -0.000710

### Volume (if available)

- volume: 7011378.00
- volume_MA20: 29277603.90
- volume_ratio: 0.24

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

- close: 11.13
- MA20 / MA60 / MA200: 12.24 / 12.99 / 10.81
- gap20 / gap60: -9.07% / -14.29%
- 5D return: -4.87%
- 20D high/low: 13.27 / 11.02

### Relative Strength

- ratio: 0.047857
- ratio_MA60: 0.051579
- ratio_gap: -7.22%
- ratio_slope_proxy(20d): 0.000543

### Volume (if available)

- volume: 1773730.00
- volume_MA20: 13722206.50
- volume_ratio: 0.13

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

- 데이터 기준일(주가): **2026-06-23**
- 실행시간(UTC): **2026-06-23 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.66
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 3.0 bp / latest 2.21
- VIX: 17.28
- NFCI: -0.505

### Leadership ratios
- SILJ/SLV gap: 5.69% / slope_proxy: 0.000241
- GDXJ/GLD gap: -4.34% / slope_proxy: -0.00315

## VZLA (Vizsla Silver)
- close: 3.39 | RSI14: 44.462187 | ATR14%: 6.71%
- MA20 gap: -6.68% | MA50 gap: -3.95% | MA200 gap: -20.22%
- vol_ratio(Volume/Vol20): 0.227727 | gap_open: 5.40%
- RS vs SILJ gap: 10.02% / slope_proxy: 0.004567
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
- close: 6.71 | RSI14: 40.891392 | ATR14%: 9.03%
- MA20 gap: -8.14% | MA50 gap: -17.40% | MA200 gap: -21.14%
- vol_ratio(Volume/Vol20): 0.388434 | gap_open: 4.67%
- SilverMarginGate: SI=62.134998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.85% / slope_proxy: -0.010224
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
- close: 23.719999 | RSI14: 34.348396 | ATR14%: 10.61%
- MA20 gap: -16.31% | MA50 gap: -31.07% | MA200 gap: -7.97%
- vol_ratio(Volume/Vol20): 0.356218 | gap_open: 5.51%
- RS vs SILJ gap: -21.82% / slope_proxy: -0.076245
- RS vs GDXJ gap: -20.37% / slope_proxy: -0.01661
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

- 실행시간(UTC): **2026-06-23 15:01:21**
- 데이터 기준일(주가): **2026-06-23**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA**

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

- HY OAS: 2.66 / 4주 변화 -0.08 bp-ish / 2026-06-19
- IG OAS: 0.74 / 4주 변화 0.00 bp-ish / 2026-06-19
- 10Y Real Yield: 2.21 / 4주 변화 0.08 bp-ish / 2026-06-18
- VIX: 17.28 / 4주 변화 0.69 / 2026-06-22
- NFCI: -0.51 / 4주 변화 0.06 / 2026-06-12

### Leadership ratios

- GDX/GLD: gap -2.95% / slope_proxy -3.10%
- GDXJ/GLD: gap -4.13% / slope_proxy -4.71%
- SILJ/SLV: gap 5.77% / slope_proxy 9.05%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.76 | RSI14: 40.25 | ATR14%: 6.55%
- MA20/50/200 gap: -2.94% / -2.22% / 17.72%
- 5D return: -2.27% | 20D drawdown: -10.80% | vol_ratio: 0.21
- RS vs GDXJ: gap 15.59% / slope_proxy 3.15%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.26 | RSI14: 45.12 | ATR14%: 7.51%
- MA20/50/200 gap: -3.63% / -7.49% / -15.94%
- 5D return: -14.29% | 20D drawdown: -14.29% | vol_ratio: 0.35
- RS vs GDXJ: gap 4.74% / slope_proxy 4.62%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **51.5**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.29 | RSI14: 36.31 | ATR14%: 7.25%
- MA20/50/200 gap: -11.41% / -18.53% / -23.80%
- 5D return: -13.98% | 20D drawdown: -24.96% | vol_ratio: 0.35
- RS vs GDXJ: gap -7.82% / slope_proxy -5.44%
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
- close: 1.59 | RSI14: 32.14 | ATR14%: 6.51%
- MA20/50/200 gap: -8.04% / -14.20% / -4.75%
- 5D return: -9.14% | 20D drawdown: -19.29% | vol_ratio: 0.31
- RS vs GDXJ: gap 0.30% / slope_proxy -0.99%
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
- close: 18.69 | RSI14: 39.61 | ATR14%: 8.07%
- MA20/50/200 gap: -2.40% / 0.77% / 22.63%
- 5D return: -9.49% | 20D drawdown: -13.03% | vol_ratio: 0.32
- RS vs SILJ: gap 17.03% / slope_proxy 13.59%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.39 | RSI14: 30.40 | ATR14%: 7.00%
- MA20/50/200 gap: -6.54% / -3.81% / -20.10%
- 5D return: -6.99% | 20D drawdown: -17.80% | vol_ratio: 0.23
- RS vs SILJ: gap 10.10% / slope_proxy 3.89%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.11 | RSI14: 34.90 | ATR14%: 7.84%
- MA20/50/200 gap: -8.47% / -13.60% / -14.22%
- 5D return: -10.98% | 20D drawdown: -18.66% | vol_ratio: 0.36
- RS vs SILJ: gap -2.01% / slope_proxy -3.83%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **53.1**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.11 | RSI14: 35.50 | ATR14%: 8.44%
- MA20/50/200 gap: -7.15% / -10.39% / -6.27%
- 5D return: -10.61% | 20D drawdown: -17.72% | vol_ratio: 0.41
- RS vs SILJ: gap 2.19% / slope_proxy 0.72%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.19 | RSI14: 34.70 | ATR14%: 6.78%
- MA20/50/200 gap: -6.18% / -13.50% / -14.73%
- 5D return: -8.82% | 20D drawdown: -14.66% | vol_ratio: 0.23
- RS vs SILJ: gap -3.08% / slope_proxy -1.64%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **51.4**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.71 | RSI14: 35.99 | ATR14%: 9.45%
- MA20/50/200 gap: -8.14% / -17.40% / -21.14%
- 5D return: -11.13% | 20D drawdown: -19.45% | vol_ratio: 0.39
- RS vs SILJ: gap -5.92% / slope_proxy -5.11%
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
- close: 5.05 | RSI14: 33.09 | ATR14%: 9.15%
- MA20/50/200 gap: -8.93% / -14.56% / -10.03%
- 5D return: -12.33% | 20D drawdown: -21.46% | vol_ratio: 0.38
- RS vs SILJ: gap -1.68% / slope_proxy -1.90%
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
- close: 23.75 | RSI14: 25.65 | ATR14%: 10.30%
- MA20/50/200 gap: -16.19% / -30.97% / -7.83%
- 5D return: -14.67% | 20D drawdown: -29.76% | vol_ratio: 0.36
- RS vs SILJ: gap -21.77% / slope_proxy -18.60%
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
