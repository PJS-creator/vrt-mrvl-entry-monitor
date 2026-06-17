# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-17 03:01:09**
- 데이터 기준일(일봉): **2026-06-16**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-15** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 729.86
- Weekly RSI14: **69.39**
- 52W MA: 614.79 / gap: **18.72%**
- 104W MA gap: **31.97%**
- 52W MA 13W slope: **8.25%**
- VXN: **25.92** / 5D change: -1.20

## Daily trigger: 실제 매수 타이밍

- QQQ close: 729.86
- Daily RSI14: **56.35**
- 20D gap: **0.75%**
- 50D gap: **6.11%**
- 200D gap: **16.57%**
- MACD hist: -2.5860 / change: 0.5162
- ATR14%: **2.14%**
- 20D high drawdown: **-2.18%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **True**

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

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-17 03:00:38**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.66 / 4주 변화 -17.0 bp
- IG OAS (BAMLC0A0CM): 0.73 / 4주 변화 -2.0 bp
- 10Y Real Yield (DFII10): 2.15 / 4주 변화 2.0 bp
- VIX (VIXCLS): 16.2
- NFCI: -0.506

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.829944
- MA60: 9.12829
- gap: -3.27%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.452386
- MA60: 0.332406
- gap: 36.09%
- MA60_slope_proxy: 0.065172
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-17 03:00:41**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **True**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 106.56 bp / 4주 변화 -31.07 bp
- CURVE_10s5s: 46.07 bp / 4주 변화 -1.35 bp

## NWG Price
- close: 614.8
- MA50: 588.9251 / gap50: 4.39%
- MA200: 589.7703 / gap200: 4.24%

## Relative Strength
- RS vs FTSE gap: 5.00% / slope_proxy: 0.000142
- RS vs Peers gap: -0.78% / slope_proxy: -0.020005

## Why not today?
- CurveGreen=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-17 03:00:48**

## Commodity Regime

- WTI ref (CL=F): 75.43 / 5D -14.48%
- Brent ref (BZ=F): 79.09 / 5D -13.52%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.66
- Gas ref (NG=F): 3.25 / 5D 3.57%

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

- close: 53.67
- MA20 / MA60 / MA200: 57.30 / 58.18 / 48.68
- gap20 / gap60: -6.34% / -7.76%
- 5D return: -4.65%
- 20D high/low: 60.42 / 53.67

### Relative Strength

- ratio: 0.969472
- ratio_MA60: 1.000376
- ratio_gap: -3.09%
- ratio_slope_proxy(20d): 0.007021

### Volume (if available)

- volume: 8436923.00
- volume_MA20: 10610956.15
- volume_ratio: 0.80

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.05
- MA20 / MA60 / MA200: 18.55 / 19.88 / 15.31
- gap20 / gap60: -8.07% / -14.25%
- 5D return: -4.32%
- 20D high/low: 20.25 / 17.05

### Relative Strength

- ratio: 0.495495
- ratio_MA60: 0.531059
- ratio_gap: -6.70%
- ratio_slope_proxy(20d): 0.017023

### Volume (if available)

- volume: 22493408.00
- volume_MA20: 15706625.40
- volume_ratio: 1.43

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.59
- MA20 / MA60 / MA200: 6.30 / 6.46 / 5.02
- gap20 / gap60: -11.21% / -13.45%
- 5D return: -4.77%
- 20D high/low: 7.45 / 5.59

### Relative Strength

- ratio: 0.013762
- ratio_MA60: 0.015264
- ratio_gap: -9.84%
- ratio_slope_proxy(20d): -0.000563

### Volume (if available)

- volume: 26877755.00
- volume_MA20: 29247707.75
- volume_ratio: 0.92

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

- close: 11.09
- MA20 / MA60 / MA200: 12.82 / 13.34 / 10.84
- gap20 / gap60: -13.52% / -16.88%
- 5D return: -10.94%
- 20D high/low: 14.76 / 11.09

### Relative Strength

- ratio: 0.048038
- ratio_MA60: 0.052165
- ratio_gap: -7.91%
- ratio_slope_proxy(20d): 0.002189

### Volume (if available)

- volume: 17753727.00
- volume_MA20: 14334521.35
- volume_ratio: 1.24

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

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-17 03:00:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -17.0 bp / latest 2.66
- IG OAS 4주 변화: -2.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 2.0 bp / latest 2.15
- VIX: 16.2
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 5.95% / slope_proxy: -0.005172
- GDXJ/GLD gap: 2.90% / slope_proxy: -0.006354

## VZLA (Vizsla Silver)
- close: 3.69 | RSI14: 53.199045 | ATR14%: 6.53%
- MA20 gap: 2.49% | MA50 gap: 5.14% | MA200 gap: -13.24%
- vol_ratio(Volume/Vol20): 0.737338 | gap_open: 0.00%
- RS vs SILJ gap: 7.18% / slope_proxy: 0.004379
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 7.97 | RSI14: 53.243688 | ATR14%: 7.80%
- MA20 gap: 5.91% | MA50 gap: -2.73% | MA200 gap: -5.99%
- vol_ratio(Volume/Vol20): 0.715407 | gap_open: 0.66%
- SilverMarginGate: SI=70.355003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.24% / slope_proxy: -0.011313
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
- close: 26.57 | RSI14: 39.186669 | ATR14%: 10.60%
- MA20 gap: -11.34% | MA50 gap: -24.96% | MA200 gap: 4.71%
- vol_ratio(Volume/Vol20): 1.084545 | gap_open: 0.72%
- RS vs SILJ gap: -23.47% / slope_proxy: -0.063476
- RS vs GDXJ gap: -21.92% / slope_proxy: -0.013677
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-06-17 03:01:04**
- 데이터 기준일(주가): **2026-06-16**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.66 / 4주 변화 -0.20 bp-ish / 2026-06-15
- IG OAS: 0.73 / 4주 변화 -0.03 bp-ish / 2026-06-15
- 10Y Real Yield: 2.15 / 4주 변화 0.05 bp-ish / 2026-06-15
- VIX: 16.20 / 4주 변화 -1.62 / 2026-06-15
- NFCI: -0.51 / 4주 변화 0.06 / 2026-06-05

### Leadership ratios

- GDX/GLD: gap 2.98% / slope_proxy 7.76%
- GDXJ/GLD: gap 2.90% / slope_proxy 7.37%
- SILJ/SLV: gap 5.95% / slope_proxy 11.23%
- Gold breadth proxy: above50 7.69%, above200 46.15%, count 13
- Silver breadth proxy: above50 23.08%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.39 | RSI14: 50.50 | ATR14%: 6.47%
- MA20/50/200 gap: 4.45% / 7.16% / 28.59%
- 5D return: 16.37% | 20D drawdown: -3.56% | vol_ratio: 0.77
- RS vs GDXJ: gap 13.58% / slope_proxy 1.84%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **73.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.47 | RSI14: 60.87 | ATR14%: 5.52%
- MA20/50/200 gap: 11.45% / 6.49% / -1.05%
- 5D return: 25.64% | 20D drawdown: 0.00% | vol_ratio: 0.99
- RS vs GDXJ: gap 8.90% / slope_proxy 8.15%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **56.5**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.15 | RSI14: 48.92 | ATR14%: 6.99%
- MA20/50/200 gap: 0.74% / -7.50% / -11.25%
- 5D return: 12.84% | 20D drawdown: -12.77% | vol_ratio: 0.81
- RS vs GDXJ: gap -5.63% / slope_proxy -4.39%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.75 | RSI14: 42.86 | ATR14%: 7.06%
- MA20/50/200 gap: -5.20% / -6.76% / 6.49%
- 5D return: 8.02% | 20D drawdown: -22.22% | vol_ratio: 0.95
- RS vs GDXJ: gap -1.09% / slope_proxy -24.02%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **41.0**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.95 | RSI14: 53.01 | ATR14%: 7.58%
- MA20/50/200 gap: 5.26% / 1.45% / 7.35%
- 5D return: 20.45% | 20D drawdown: -6.33% | vol_ratio: 1.14
- RS vs SILJ: gap 4.04% / slope_proxy 1.76%
- FundamentalScore: 60 | TechnicalScore: 80 | RegimeScore: 55 | OverallScore: **66.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.88 | RSI14: 50.26 | ATR14%: 7.62%
- MA20/50/200 gap: 4.88% / -0.78% / 5.74%
- 5D return: 24.58% | 20D drawdown: -8.55% | vol_ratio: 0.93
- RS vs SILJ: gap 1.28% / slope_proxy -1.26%
- FundamentalScore: 68 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **55.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 21.05 | RSI14: 57.97 | ATR14%: 6.90%
- MA20/50/200 gap: 13.00% / 15.15% / 39.79%
- 5D return: 26.20% | 20D drawdown: -2.05% | vol_ratio: 1.13
- RS vs SILJ: gap 20.22% / slope_proxy 20.90%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.69 | RSI14: 51.67 | ATR14%: 7.09%
- MA20/50/200 gap: 2.49% / 5.14% / -13.24%
- 5D return: 10.81% | 20D drawdown: -10.65% | vol_ratio: 0.74
- RS vs SILJ: gap 7.18% / slope_proxy 7.40%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.72 | RSI14: 48.67 | ATR14%: 6.09%
- MA20/50/200 gap: 1.82% / -6.33% / -5.40%
- 5D return: 15.23% | 20D drawdown: -6.07% | vol_ratio: 1.09
- RS vs SILJ: gap -5.98% / slope_proxy -3.03%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **56.6**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.30 | RSI14: 49.82 | ATR14%: 6.90%
- MA20/50/200 gap: 3.33% / -1.82% / -1.17%
- 5D return: 18.77% | 20D drawdown: -6.72% | vol_ratio: 0.77
- RS vs SILJ: gap -0.40% / slope_proxy -2.07%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.97 | RSI14: 51.77 | ATR14%: 7.89%
- MA20/50/200 gap: 5.91% / -2.73% / -5.99%
- 5D return: 30.66% | 20D drawdown: -4.89% | vol_ratio: 0.72
- RS vs SILJ: gap -1.24% / slope_proxy -8.12%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 26.57 | RSI14: 36.11 | ATR14%: 10.07%
- MA20/50/200 gap: -11.34% / -24.96% / 4.71%
- 5D return: 6.92% | 20D drawdown: -22.00% | vol_ratio: 1.08
- RS vs SILJ: gap -23.47% / slope_proxy -24.03%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **40.4**
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
