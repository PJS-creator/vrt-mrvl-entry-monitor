# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-04 15:01:35**
- 데이터 기준일(일봉): **2026-11-04**
- 데이터 기준일(주봉): **2026-11-02**
- VXN 기준일: **2026-11-03** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 685.28
- Weekly RSI14: **45.69**
- 52W MA: 665.57 / gap: **2.96%**
- 104W MA gap: **14.60%**
- 52W MA 13W slope: **5.03%**
- VXN: **30.53** / 5D change: 5.62

## Daily trigger: 실제 매수 타이밍

- QQQ close: 699.29
- Daily RSI14: **42.35**
- 20D gap: **-2.58%**
- 50D gap: **-3.34%**
- 200D gap: **2.92%**
- MACD hist: -3.5348 / change: 1.0403
- ATR14%: **1.84%**
- 20D high drawdown: **-6.92%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-11-04**
- 실행시간(UTC): **2026-11-04 15:00:55**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.4 / 4주 변화 37.0 bp
- IG OAS (BAMLC0A0CM): 0.93 / 4주 변화 10.0 bp
- 10Y Real Yield (DFII10): 2.62 / 4주 변화 -33.0 bp
- VIX (VIXCLS): 20.83
- NFCI: -0.459

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.495974
- MA60: 8.348346
- gap: -10.21%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.316037
- MA60: 0.415121
- gap: -23.87%
- MA60_slope_proxy: 0.021273
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-04**
- 실행시간(UTC): **2026-11-04 15:00:59**

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
- TERM_SPREAD_10Y_POLICY: 141.77 bp / 4주 변화 -19.57 bp
- CURVE_10s5s: 35.12 bp / 4주 변화 -8.11 bp

## NWG Price
- close: 610.0
- MA50: 666.532 / gap50: -8.48%
- MA200: 634.304 / gap200: -3.83%

## Relative Strength
- RS vs FTSE gap: -10.16% / slope_proxy: -0.001501
- RS vs Peers gap: -0.46% / slope_proxy: 0.019744

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-04 15:01:07**

## Commodity Regime

- WTI ref (CL=F): 93.24 / 5D -9.28%
- Brent ref (BZ=F): 100.66 / 5D -12.71%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.42
- Gas ref (NG=F): 2.89 / 5D 2.66%

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

- close: 58.48
- MA20 / MA60 / MA200: 61.95 / 59.97 / 55.96
- gap20 / gap60: -5.60% / -2.49%
- 5D return: -6.97%
- 20D high/low: 64.17 / 58.48

### Relative Strength

- ratio: 0.907089
- ratio_MA60: 0.929443
- ratio_gap: -2.41%
- ratio_slope_proxy(20d): -0.013053

### Volume (if available)

- volume: 1425632.00
- volume_MA20: 8340641.60
- volume_ratio: 0.17

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.45
- MA20 / MA60 / MA200: 24.02 / 21.41 / 18.78
- gap20 / gap60: -14.85% / -4.50%
- 5D return: -7.17%
- 20D high/low: 26.16 / 20.45

### Relative Strength

- ratio: 0.633519
- ratio_MA60: 0.569786
- ratio_gap: 11.19%
- ratio_slope_proxy(20d): 0.041069

### Volume (if available)

- volume: 3208459.00
- volume_MA20: 25724622.95
- volume_ratio: 0.12

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.63
- MA20 / MA60 / MA200: 6.02 / 5.77 / 5.88
- gap20 / gap60: -6.35% / -2.36%
- 5D return: -16.02%
- 20D high/low: 6.94 / 5.51

### Relative Strength

- ratio: 0.015183
- ratio_MA60: 0.014359
- ratio_gap: 5.74%
- ratio_slope_proxy(20d): 0.000598

### Volume (if available)

- volume: 6365722.00
- volume_MA20: 42301336.10
- volume_ratio: 0.15

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

- close: 12.20
- MA20 / MA60 / MA200: 13.33 / 13.78 / 12.73
- gap20 / gap60: -8.49% / -11.48%
- 5D return: -15.02%
- 20D high/low: 14.79 / 12.20

### Relative Strength

- ratio: 0.040838
- ratio_MA60: 0.048918
- ratio_gap: -16.52%
- ratio_slope_proxy(20d): -0.002043

### Volume (if available)

- volume: 3725278.00
- volume_MA20: 15728833.90
- volume_ratio: 0.24

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

- 데이터 기준일(주가): **2026-11-04**
- 실행시간(UTC): **2026-11-04 15:01:16**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 37.0 bp / latest 3.4
- IG OAS 4주 변화: 10.0 bp / latest 0.93
- 10Y Real Yield 4주 변화: -33.0 bp / latest 2.62
- VIX: 20.83
- NFCI: -0.459

### Leadership ratios
- SILJ/SLV gap: -0.14% / slope_proxy: 0.005066
- GDXJ/GLD gap: -8.22% / slope_proxy: 0.004303

## VZLA (Vizsla Silver)
- close: 3.185 | RSI14: 43.650863 | ATR14%: 5.76%
- MA20 gap: -1.89% | MA50 gap: -12.68% | MA200 gap: -13.91%
- vol_ratio(Volume/Vol20): 0.124729 | gap_open: 7.26%
- RS vs SILJ gap: 2.77% / slope_proxy: 0.000404
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
- close: 7.3162 | RSI14: 43.079233 | ATR14%: 6.79%
- MA20 gap: -5.93% | MA50 gap: -15.80% | MA200 gap: -16.22%
- vol_ratio(Volume/Vol20): 0.289764 | gap_open: 9.01%
- SilverMarginGate: SI=52.200001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -0.97% / slope_proxy: 0.015142
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
- close: 17.27 | RSI14: 47.341516 | ATR14%: 7.09%
- MA20 gap: 1.76% | MA50 gap: -11.87% | MA200 gap: -41.92%
- vol_ratio(Volume/Vol20): 0.231037 | gap_open: 9.01%
- RS vs SILJ gap: -0.56% / slope_proxy: -0.050003
- RS vs GDXJ gap: -3.51% / slope_proxy: -0.016854
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

- 실행시간(UTC): **2026-11-04 15:01:33**
- 데이터 기준일(주가): **2026-11-04**

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

- HY OAS: 3.40 / 4주 변화 0.37 bp-ish / 2026-11-03
- IG OAS: 0.93 / 4주 변화 0.10 bp-ish / 2026-11-03
- 10Y Real Yield: 2.62 / 4주 변화 -0.30 bp-ish / 2026-11-02
- VIX: 20.83 / 4주 변화 5.82 / 2026-11-03
- NFCI: -0.46 / 4주 변화 0.04 / 2026-10-30

### Leadership ratios

- GDX/GLD: gap -4.29% / slope_proxy -2.72%
- GDXJ/GLD: gap -8.23% / slope_proxy -6.54%
- SILJ/SLV: gap -0.16% / slope_proxy 1.20%
- Gold breadth proxy: above50 0.00%, above200 15.38%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.73 | RSI14: 29.07 | ATR14%: 4.88%
- MA20/50/200 gap: -7.65% / -17.00% / -4.63%
- 5D return: -4.57% | 20D drawdown: -17.41% | vol_ratio: 0.22
- RS vs GDXJ: gap -5.86% / slope_proxy -6.00%
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
- close: 5.30 | RSI14: 31.31 | ATR14%: 6.05%
- MA20/50/200 gap: -11.98% / -24.12% / -23.25%
- 5D return: -10.02% | 20D drawdown: -24.07% | vol_ratio: 0.27
- RS vs GDXJ: gap -12.71% / slope_proxy -14.29%
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
- close: 0.80 | RSI14: 31.58 | ATR14%: 7.59%
- MA20/50/200 gap: -10.36% / -32.12% / -43.16%
- 5D return: -10.11% | 20D drawdown: -21.57% | vol_ratio: 0.10
- RS vs GDXJ: gap -24.68% / slope_proxy -9.30%
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
- close: 1.68 | RSI14: 31.13 | ATR14%: 8.38%
- MA20/50/200 gap: -10.40% / -26.14% / -15.00%
- 5D return: -5.08% | 20D drawdown: -23.64% | vol_ratio: 0.33
- RS vs GDXJ: gap -14.65% / slope_proxy -15.05%
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
- close: 24.91 | RSI14: 45.07 | ATR14%: 5.66%
- MA20/50/200 gap: -1.26% / -7.26% / 18.99%
- 5D return: -1.50% | 20D drawdown: -9.15% | vol_ratio: 0.16
- RS vs SILJ: gap 9.60% / slope_proxy 6.27%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.17 | RSI14: 43.93 | ATR14%: 5.65%
- MA20/50/200 gap: -2.18% / -12.95% / -14.18%
- 5D return: -2.61% | 20D drawdown: -10.56% | vol_ratio: 0.12
- RS vs SILJ: gap 2.45% / slope_proxy 2.74%
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
- close: 7.57 | RSI14: 38.38 | ATR14%: 5.49%
- MA20/50/200 gap: -4.38% / -16.94% / -21.87%
- 5D return: -5.02% | 20D drawdown: -12.49% | vol_ratio: 0.36
- RS vs SILJ: gap -3.58% / slope_proxy -0.82%
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
- close: 14.45 | RSI14: 40.74 | ATR14%: 5.17%
- MA20/50/200 gap: -3.17% / -16.45% / -21.71%
- 5D return: -3.15% | 20D drawdown: -15.35% | vol_ratio: 0.23
- RS vs SILJ: gap -2.45% / slope_proxy -3.01%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.32 | RSI14: 36.49 | ATR14%: 6.32%
- MA20/50/200 gap: -5.93% / -15.80% / -16.22%
- 5D return: -2.45% | 20D drawdown: -19.69% | vol_ratio: 0.29
- RS vs SILJ: gap -0.97% / slope_proxy -3.12%
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
- close: 2.90 | RSI14: 22.64 | ATR14%: 7.57%
- MA20/50/200 gap: -16.08% / -33.25% / -48.49%
- 5D return: -9.22% | 20D drawdown: -33.37% | vol_ratio: 0.37
- RS vs SILJ: gap -22.63% / slope_proxy -23.07%
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
- close: 4.59 | RSI14: 35.42 | ATR14%: 5.86%
- MA20/50/200 gap: -6.83% / -21.54% / -32.95%
- 5D return: -4.28% | 20D drawdown: -17.39% | vol_ratio: 0.34
- RS vs SILJ: gap -9.76% / slope_proxy -5.71%
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
- close: 17.27 | RSI14: 48.95 | ATR14%: 6.67%
- MA20/50/200 gap: 1.76% / -11.87% / -41.92%
- 5D return: -0.97% | 20D drawdown: -10.01% | vol_ratio: 0.23
- RS vs SILJ: gap -0.56% / slope_proxy 6.49%
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
