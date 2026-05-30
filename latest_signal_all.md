# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **✅ Precious miners entry confirmed: EXK**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-05-30 15:06:33**
- 데이터 기준일(일봉): **2026-05-29**
- 데이터 기준일(주봉): **2026-05-25**
- VXN 기준일: **2026-05-29** / source: `Yahoo Finance ^VXN fallback; FRED error=504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 738.31
- Weekly RSI14: **77.35**
- 52W MA: 603.64 / gap: **22.31%**
- 104W MA gap: **35.26%**
- 52W MA 13W slope: **7.48%**
- VXN: **22.58** / 5D change: -0.16

## Daily trigger: 실제 매수 타이밍

- QQQ close: 738.31
- Daily RSI14: **77.20**
- 20D gap: **4.13%**
- 50D gap: **13.08%**
- 200D gap: **19.70%**
- MACD hist: 0.0232 / change: 0.2019
- ATR14%: **1.40%**
- 20D high drawdown: **0.00%**

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

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-30 15:00:36**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.73 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 2.06 / 4주 변화 12.0 bp
- VIX (VIXCLS): 15.74
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.090412
- MA60: 8.921317
- gap: 1.90%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.342277
- MA60: 0.286297
- gap: 19.55%
- MA60_slope_proxy: 0.042031
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-30 15:01:38**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- TERM_SPREAD_10Y_POLICY: 107.59 bp / 4주 변화 -17.94 bp
- CURVE_10s5s: 45.99 bp / 4주 변화 1.7 bp

## NWG Price
- close: 599.4
- MA50: 577.4358 / gap50: 3.80%
- MA200: 587.1723 / gap200: 2.08%

## Relative Strength
- RS vs FTSE gap: 3.15% / slope_proxy: -0.001131
- RS vs Peers gap: -3.73% / slope_proxy: -0.027043

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-30 15:02:24**

## ⚠️ DATA WARNING

- FRED DCOILWTICO failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO), using cached values if available.
- FRED DCOILBRENTEU failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTEU), using cached values if available.
- FRED DHHNGSP failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DHHNGSP), using cached values if available.
- FRED OVXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DTWEXBGS failed (502 Server Error: Bad Gateway for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VXEWZCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 87.36 / 5D -9.33%
- Brent ref (BZ=F): 92.05 / 5D -10.27%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.69
- Gas ref (NG=F): 3.29 / 5D 9.01%

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

- close: 56.63
- MA20 / MA60 / MA200: 57.48 / 58.36 / 48.15
- gap20 / gap60: -1.48% / -2.97%
- 5D return: -3.74%
- 20D high/low: 60.70 / 53.03

### Relative Strength

- ratio: 1.006040
- ratio_MA60: 1.004432
- ratio_gap: 0.16%
- ratio_slope_proxy(20d): 0.027588

### Volume (if available)

- volume: 14395100.00
- volume_MA20: 12446000.00
- volume_ratio: 1.16

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.77
- MA20 / MA60 / MA200: 20.23 / 20.12 / 15.06
- gap20 / gap60: -7.23% / -6.72%
- 5D return: -6.29%
- 20D high/low: 22.01 / 18.77

### Relative Strength

- ratio: 0.522696
- ratio_MA60: 0.527273
- ratio_gap: -0.87%
- ratio_slope_proxy(20d): 0.042508

### Volume (if available)

- volume: 16604400.00
- volume_MA20: 17524960.00
- volume_ratio: 0.95

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.19
- MA20 / MA60 / MA200: 6.67 / 6.50 / 4.84
- gap20 / gap60: -7.27% / -4.81%
- 5D return: -9.24%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014800
- ratio_MA60: 0.015705
- ratio_gap: -5.77%
- ratio_slope_proxy(20d): -0.000203

### Volume (if available)

- volume: 26937600.00
- volume_MA20: 35447195.00
- volume_ratio: 0.76

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

- close: 12.04
- MA20 / MA60 / MA200: 13.00 / 13.45 / 10.87
- gap20 / gap60: -7.38% / -10.48%
- 5D return: -11.21%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.053544
- ratio_MA60: 0.051746
- ratio_gap: 3.48%
- ratio_slope_proxy(20d): 0.003128

### Volume (if available)

- volume: 13923700.00
- volume_MA20: 19674730.00
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

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-30 15:04:30**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10), using cached values if available.
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
- HY OAS 4주 변화: -11.0 bp / latest 2.72
- IG OAS 4주 변화: -8.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.06
- VIX: 15.74
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 2.59% / slope_proxy: -0.013075
- GDXJ/GLD gap: 1.70% / slope_proxy: -0.006186

## VZLA (Vizsla Silver)
- close: 3.88 | RSI14: 60.927756 | ATR14%: 5.74%
- MA20 gap: 9.28% | MA50 gap: 14.06% | MA200 gap: -8.52%
- vol_ratio(Volume/Vol20): 0.871978 | gap_open: 0.26%
- RS vs SILJ gap: 10.88% / slope_proxy: 0.000205
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
- close: 8.15 | RSI14: 45.274778 | ATR14%: 7.30%
- MA20 gap: -5.18% | MA50 gap: -2.43% | MA200 gap: -1.87%
- vol_ratio(Volume/Vol20): 0.940641 | gap_open: 0.00%
- SilverMarginGate: SI=75.615997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.24% / slope_proxy: -0.011761
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
- close: 33.049999 | RSI14: 42.543264 | ATR14%: 9.05%
- MA20 gap: -9.99% | MA50 gap: -9.88% | MA200 gap: 38.08%
- vol_ratio(Volume/Vol20): 0.746063 | gap_open: 0.69%
- RS vs SILJ gap: -11.76% / slope_proxy: 0.008588
- RS vs GDXJ gap: -9.48% / slope_proxy: 0.00396
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

- 실행시간(UTC): **2026-05-30 15:06:22**
- 데이터 기준일(주가): **2026-05-29**

## Verdict
**✅ Precious miners entry confirmed: EXK**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **True**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.72 / 4주 변화 -0.11 bp-ish / 2026-05-28
- IG OAS: 0.73 / 4주 변화 -0.08 bp-ish / 2026-05-28
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: N/A

### Leadership ratios

- GDX/GLD: gap 0.61% / slope_proxy 4.22%
- GDXJ/GLD: gap 1.70% / slope_proxy 4.89%
- SILJ/SLV: gap 2.59% / slope_proxy 4.93%
- Gold breadth proxy: above50 15.38%, above200 92.31%, count 13
- Silver breadth proxy: above50 69.23%, above200 84.62%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.98 | RSI14: 48.59 | ATR14%: 5.72%
- MA20/50/200 gap: 5.43% / 1.96% / 2.06%
- 5D return: 17.71% | 20D drawdown: -5.16% | vol_ratio: 1.23
- RS vs GDXJ: gap 0.47% / slope_proxy 6.03%
- FundamentalScore: 82 | TechnicalScore: 80 | RegimeScore: 55 | OverallScore: **75.9**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.70 | RSI14: 56.90 | ATR14%: 6.20%
- MA20/50/200 gap: 6.77% / 17.08% / 37.71%
- 5D return: 0.58% | 20D drawdown: 0.00% | vol_ratio: 0.91
- RS vs GDXJ: gap 19.71% / slope_proxy 12.35%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.93 | RSI14: 51.70 | ATR14%: 9.66%
- MA20/50/200 gap: -3.45% / 5.30% / 22.77%
- 5D return: -5.85% | 20D drawdown: -22.49% | vol_ratio: 0.77
- RS vs GDXJ: gap 7.69% / slope_proxy 10.72%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 55 | OverallScore: **65.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, SectorBreadthProxy=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.39 | RSI14: 44.26 | ATR14%: 5.55%
- MA20/50/200 gap: -0.57% / -0.84% / -4.05%
- 5D return: 4.51% | 20D drawdown: -9.74% | vol_ratio: 0.77
- RS vs GDXJ: gap -1.17% / slope_proxy 1.17%
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

---

## Silver miners

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.97 | RSI14: 49.47 | ATR14%: 6.78%
- MA20/50/200 gap: 1.69% / 4.49% / 8.06%
- 5D return: 6.86% | 20D drawdown: -13.00% | vol_ratio: 0.58
- RS vs SILJ: gap 1.72% / slope_proxy 3.22%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 100 | OverallScore: **86.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **True**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 21.00 | RSI14: 57.27 | ATR14%: 6.85%
- MA20/50/200 gap: 11.34% / 22.58% / 45.23%
- 5D return: 22.95% | 20D drawdown: -1.96% | vol_ratio: 0.97
- RS vs SILJ: gap 22.34% / slope_proxy 8.29%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **81.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 6.16 | RSI14: 42.68 | ATR14%: 7.95%
- MA20/50/200 gap: -1.00% / 3.70% / 14.57%
- 5D return: 7.88% | 20D drawdown: -16.87% | vol_ratio: 0.65
- RS vs SILJ: gap -2.00% / slope_proxy -0.05%
- FundamentalScore: 68 | TechnicalScore: 60 | RegimeScore: 100 | OverallScore: **71.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: RelativeStrength(vs SILJ)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.32 | RSI14: 54.84 | ATR14%: 7.02%
- MA20/50/200 gap: 5.12% / 8.47% / 15.70%
- 5D return: 10.08% | 20D drawdown: -8.16% | vol_ratio: 0.62
- RS vs SILJ: gap 6.15% / slope_proxy 5.96%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **69.8**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.88 | RSI14: 59.20 | ATR14%: 5.99%
- MA20/50/200 gap: 9.28% / 14.06% / -8.52%
- 5D return: 14.79% | 20D drawdown: 0.00% | vol_ratio: 0.87
- RS vs SILJ: gap 10.88% / slope_proxy 6.81%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **66.4**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.77 | RSI14: 46.06 | ATR14%: 6.77%
- MA20/50/200 gap: -1.79% / -3.34% / 3.39%
- 5D return: 2.72% | 20D drawdown: -15.58% | vol_ratio: 1.28
- RS vs SILJ: gap -5.74% / slope_proxy -6.29%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 100 | OverallScore: **65.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.15 | RSI14: 39.47 | ATR14%: 7.44%
- MA20/50/200 gap: -5.18% / -2.43% / -1.87%
- 5D return: -0.37% | 20D drawdown: -19.70% | vol_ratio: 0.94
- RS vs SILJ: gap -5.24% / slope_proxy -4.87%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **58.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 33.05 | RSI14: 39.12 | ATR14%: 9.33%
- MA20/50/200 gap: -9.99% / -9.88% / 38.08%
- 5D return: -0.72% | 20D drawdown: -26.82% | vol_ratio: 0.75
- RS vs SILJ: gap -11.76% / slope_proxy -18.72%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **44.2**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
