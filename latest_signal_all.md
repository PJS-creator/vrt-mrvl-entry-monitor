# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-15 15:08:11**
- 데이터 기준일(일봉): **2026-06-15**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-15** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 742.51
- Weekly RSI14: **71.12**
- 52W MA: 615.04 / gap: **20.73%**
- 104W MA gap: **34.22%**
- 52W MA 13W slope: **8.29%**
- VXN: **26.04** / 5D change: -1.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 742.51
- Daily RSI14: **62.14**
- 20D gap: **2.67%**
- 50D gap: **8.40%**
- 200D gap: **18.74%**
- MACD hist: -3.1972 / change: 2.0954
- ATR14%: **2.09%**
- 20D high drawdown: **-0.49%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-15 15:00:45**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -9.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -1.0 bp
- 10Y Real Yield (DFII10): 2.16 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.506

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.257185
- MA60: 9.120954
- gap: 1.49%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.457331
- MA60: 0.328339
- gap: 39.29%
- MA60_slope_proxy: 0.06307
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-15 15:02:07**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 113.04 bp / 4주 변화 -8.57 bp
- CURVE_10s5s: 44.66 bp / 4주 변화 -0.68 bp

## NWG Price
- close: 614.0
- MA50: 588.9091 / gap50: 4.26%
- MA200: 589.7663 / gap200: 4.11%

## Relative Strength
- RS vs FTSE gap: 4.80% / slope_proxy: 0.00014
- RS vs Peers gap: -0.50% / slope_proxy: -0.019963

## Why not today?
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-15 15:03:13**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DCOILBRENTEU failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DHHNGSP failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DTWEXBGS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 80.38 / 5D -11.96%
- Brent ref (BZ=F): 83.04 / 5D -11.89%
- Brent Tier: **80-90**
- Brent-WTI spread: 2.66
- Gas ref (NG=F): 3.11 / 5D -1.24%

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

- close: 54.82
- MA20 / MA60 / MA200: 57.61 / 58.30 / 48.64
- gap20 / gap60: -4.84% / -5.97%
- 5D return: -4.19%
- 20D high/low: 60.42 / 54.82

### Relative Strength

- ratio: 0.978754
- ratio_MA60: 1.001284
- ratio_gap: -2.25%
- ratio_slope_proxy(20d): 0.008579

### Volume (if available)

- volume: 4414372.00
- volume_MA20: 10489828.60
- volume_ratio: 0.42

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.52
- MA20 / MA60 / MA200: 18.73 / 19.91 / 15.29
- gap20 / gap60: -6.43% / -11.99%
- 5D return: -1.27%
- 20D high/low: 20.54 / 17.52

### Relative Strength

- ratio: 0.498932
- ratio_MA60: 0.526739
- ratio_gap: -5.28%
- ratio_slope_proxy(20d): 0.020274

### Volume (if available)

- volume: 5805281.00
- volume_MA20: 14944454.05
- volume_ratio: 0.39

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

- close: 5.86
- MA20 / MA60 / MA200: 6.40 / 6.47 / 5.01
- gap20 / gap60: -8.46% / -9.50%
- 5D return: -5.11%
- 20D high/low: 7.58 / 5.86

### Relative Strength

- ratio: 0.013945
- ratio_MA60: 0.015301
- ratio_gap: -8.86%
- ratio_slope_proxy(20d): -0.000527

### Volume (if available)

- volume: 8978427.00
- volume_MA20: 29770611.35
- volume_ratio: 0.30

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

- close: 12.16
- MA20 / MA60 / MA200: 13.02 / 13.45 / 10.87
- gap20 / gap60: -6.54% / -9.53%
- 5D return: -5.26%
- 20D high/low: 14.78 / 12.04

### Relative Strength

- ratio: 0.051886
- ratio_MA60: 0.052410
- ratio_gap: -1.00%
- ratio_slope_proxy(20d): 0.002605

### Volume (if available)

- volume: 9689997.00
- volume_MA20: 13694479.85
- volume_ratio: 0.71

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

- 데이터 기준일(주가): **2026-06-15**
- 실행시간(UTC): **2026-06-15 15:05:57**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.71
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 3.93% / slope_proxy: -0.006661
- GDXJ/GLD gap: 1.34% / slope_proxy: -0.007366

## VZLA (Vizsla Silver)
- close: 3.735 | RSI14: 54.158247 | ATR14%: 6.63%
- MA20 gap: 4.00% | MA50 gap: 6.61% | MA200 gap: -12.17%
- vol_ratio(Volume/Vol20): 0.414609 | gap_open: 7.80%
- RS vs SILJ gap: 9.91% / slope_proxy: 0.004378
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
- close: 7.65 | RSI14: 49.932885 | ATR14%: 8.14%
- MA20 gap: 1.20% | MA50 gap: -6.70% | MA200 gap: -9.61%
- vol_ratio(Volume/Vol20): 0.472819 | gap_open: 9.60%
- SilverMarginGate: SI=70.910004 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.10% / slope_proxy: -0.011629
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
- close: 28.639999 | RSI14: 43.621953 | ATR14%: 9.87%
- MA20 gap: -5.85% | MA50 gap: -19.57% | MA200 gap: 13.35%
- vol_ratio(Volume/Vol20): 0.54405 | gap_open: 11.30%
- RS vs SILJ gap: -16.84% / slope_proxy: -0.058373
- RS vs GDXJ gap: -15.11% / slope_proxy: -0.012493
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

- 실행시간(UTC): **2026-06-15 15:07:50**
- 데이터 기준일(주가): **2026-06-15**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, USAS, ASM**

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

- HY OAS: 2.71 / 4주 변화 -0.12 bp-ish / 2026-06-12
- IG OAS: 0.74 / 4주 변화 -0.01 bp-ish / 2026-06-12
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: N/A

### Leadership ratios

- GDX/GLD: gap 1.05% / slope_proxy 3.17%
- GDXJ/GLD: gap 1.34% / slope_proxy 2.51%
- SILJ/SLV: gap 3.93% / slope_proxy 8.46%
- Gold breadth proxy: above50 7.69%, above200 23.08%, count 13
- Silver breadth proxy: above50 23.08%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.09 | RSI14: 43.25 | ATR14%: 6.53%
- MA20/50/200 gap: 0.48% / 3.76% / 24.28%
- 5D return: 9.26% | 20D drawdown: -7.07% | vol_ratio: 0.27
- RS vs GDXJ: gap 11.28% / slope_proxy -3.10%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 55 | OverallScore: **71.6**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs GDXJ)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.10 | RSI14: 46.37 | ATR14%: 7.04%
- MA20/50/200 gap: -0.26% / -8.45% / -11.89%
- 5D return: 6.46% | 20D drawdown: -13.48% | vol_ratio: 0.40
- RS vs GDXJ: gap -5.48% / slope_proxy -6.72%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.38 | RSI14: 49.62 | ATR14%: 5.66%
- MA20/50/200 gap: 4.86% / -0.46% / -7.22%
- 5D return: 12.70% | 20D drawdown: -2.48% | vol_ratio: 0.21
- RS vs GDXJ: gap 3.32% / slope_proxy -0.35%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **47.8**
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
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.72 | RSI14: 42.86 | ATR14%: 7.27%
- MA20/50/200 gap: -8.07% / -8.34% / 5.04%
- 5D return: 2.99% | 20D drawdown: -23.56% | vol_ratio: 0.38
- RS vs GDXJ: gap -1.42% / slope_proxy -25.00%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 20.68 | RSI14: 56.84 | ATR14%: 7.12%
- MA20/50/200 gap: 11.77% / 13.72% / 37.86%
- 5D return: 18.10% | 20D drawdown: -3.77% | vol_ratio: 0.51
- RS vs SILJ: gap 20.31% / slope_proxy 12.70%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.82 | RSI14: 49.54 | ATR14%: 7.76%
- MA20/50/200 gap: 3.90% / -1.60% / 5.06%
- 5D return: 17.44% | 20D drawdown: -9.41% | vol_ratio: 0.58
- RS vs SILJ: gap 1.47% / slope_proxy 1.08%
- FundamentalScore: 68 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **64.3**
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
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.97 | RSI14: 50.79 | ATR14%: 7.38%
- MA20/50/200 gap: 5.53% / 1.83% / 7.94%
- 5D return: 16.64% | 20D drawdown: -6.00% | vol_ratio: 0.67
- RS vs SILJ: gap 5.87% / slope_proxy 1.33%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **60.8**
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.75 | RSI14: 50.67 | ATR14%: 6.99%
- MA20/50/200 gap: 4.40% / 7.03% / -11.82%
- 5D return: 9.01% | 20D drawdown: -9.20% | vol_ratio: 0.42
- RS vs SILJ: gap 10.34% / slope_proxy 10.55%
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
- close: 9.26 | RSI14: 46.99 | ATR14%: 6.90%
- MA20/50/200 gap: 2.64% / -2.37% / -1.48%
- 5D return: 15.11% | 20D drawdown: -7.17% | vol_ratio: 0.61
- RS vs SILJ: gap 0.28% / slope_proxy -1.68%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.61 | RSI14: 44.53 | ATR14%: 6.14%
- MA20/50/200 gap: 1.03% / -7.17% / -5.76%
- 5D return: 11.58% | 20D drawdown: -6.66% | vol_ratio: 0.44
- RS vs SILJ: gap -5.68% / slope_proxy -2.95%
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
- close: 7.66 | RSI14: 46.12 | ATR14%: 7.97%
- MA20/50/200 gap: 1.32% / -6.58% / -9.49%
- 5D return: 20.82% | 20D drawdown: -10.51% | vol_ratio: 0.48
- RS vs SILJ: gap -3.97% / slope_proxy -9.78%
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
- close: 28.67 | RSI14: 38.78 | ATR14%: 9.03%
- MA20/50/200 gap: -5.76% / -19.49% / 13.47%
- 5D return: 8.89% | 20D drawdown: -17.69% | vol_ratio: 0.54
- RS vs SILJ: gap -16.76% / slope_proxy -17.01%
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
