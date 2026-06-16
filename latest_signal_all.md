# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, USAS**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-16 15:08:40**
- 데이터 기준일(일봉): **2026-06-16**
- 데이터 기준일(주봉): **2026-06-15**
- VXN 기준일: **2026-06-16** / source: `Yahoo Finance ^VXN fallback; FRED error=HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 737.66
- Weekly RSI14: **70.48**
- 52W MA: 614.94 / gap: **19.96%**
- 104W MA gap: **33.36%**
- 52W MA 13W slope: **8.27%**
- VXN: **25.69** / 5D change: -1.43

## Daily trigger: 실제 매수 타이밍

- QQQ close: 737.66
- Daily RSI14: **59.61**
- 20D gap: **1.77%**
- 50D gap: **7.22%**
- 200D gap: **17.81%**
- MACD hist: -2.0882 / change: 1.0139
- ATR14%: **2.05%**
- 20D high drawdown: **-1.14%**

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
- 실행시간(UTC): **2026-06-16 15:00:55**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.66 / 4주 변화 -17.0 bp
- IG OAS (BAMLC0A0CM): 0.75 / 4주 변화 -1.0 bp
- 10Y Real Yield (DFII10): 2.16 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.506

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.997653
- MA60: 9.131085
- gap: -1.46%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.474813
- MA60: 0.32863
- gap: 44.48%
- MA60_slope_proxy: 0.063361
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-16**
- 실행시간(UTC): **2026-06-16 15:02:22**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

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
- close: 627.7002
- MA50: 589.8151 / gap50: 6.42%
- MA200: 590.3568 / gap200: 6.33%

## Relative Strength
- RS vs FTSE gap: 6.55% / slope_proxy: 0.000156
- RS vs Peers gap: -0.38% / slope_proxy: -0.020064

## Why not today?
- CurveGreen=FALSE
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-16 15:03:08**

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

- WTI ref (CL=F): 76.28 / 5D -13.51%
- Brent ref (BZ=F): 80.01 / 5D -12.51%
- Brent Tier: **80-90**
- Brent-WTI spread: 3.73
- Gas ref (NG=F): 3.20 / 5D 1.85%

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

- close: 53.60
- MA20 / MA60 / MA200: 57.55 / 58.28 / 48.64
- gap20 / gap60: -6.85% / -8.02%
- 5D return: -6.31%
- 20D high/low: 60.42 / 53.60

### Relative Strength

- ratio: 0.972779
- ratio_MA60: 1.001184
- ratio_gap: -2.84%
- ratio_slope_proxy(20d): 0.008479

### Volume (if available)

- volume: 2732407.00
- volume_MA20: 10406680.35
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.11
- MA20 / MA60 / MA200: 18.71 / 19.90 / 15.29
- gap20 / gap60: -8.54% / -14.03%
- 5D return: -3.60%
- 20D high/low: 20.54 / 17.11

### Relative Strength

- ratio: 0.498115
- ratio_MA60: 0.531660
- ratio_gap: -6.31%
- ratio_slope_proxy(20d): 0.020374

### Volume (if available)

- volume: 8015737.00
- volume_MA20: 15055081.85
- volume_ratio: 0.53

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

- close: 5.64
- MA20 / MA60 / MA200: 6.30 / 6.46 / 5.02
- gap20 / gap60: -10.37% / -12.61%
- 5D return: -3.83%
- 20D high/low: 7.45 / 5.64

### Relative Strength

- ratio: 0.013755
- ratio_MA60: 0.015264
- ratio_gap: -9.89%
- ratio_slope_proxy(20d): -0.000563

### Volume (if available)

- volume: 10585319.00
- volume_MA20: 28431500.95
- volume_ratio: 0.37

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

- close: 11.46
- MA20 / MA60 / MA200: 12.96 / 13.42 / 10.85
- gap20 / gap60: -11.57% / -14.55%
- 5D return: -10.59%
- 20D high/low: 14.76 / 11.46

### Relative Strength

- ratio: 0.049338
- ratio_MA60: 0.052296
- ratio_gap: -5.66%
- ratio_slope_proxy(20d): 0.002560

### Volume (if available)

- volume: 4925622.00
- volume_MA20: 13456426.10
- volume_ratio: 0.37

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
- 실행시간(UTC): **2026-06-16 15:05:51**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLC0A0CM failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
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
- HY OAS 4주 변화: -17.0 bp / latest 2.66
- IG OAS 4주 변화: -1.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.16
- VIX: 16.05
- NFCI: -0.506

### Leadership ratios
- SILJ/SLV gap: 5.82% / slope_proxy: -0.006519
- GDXJ/GLD gap: 2.44% / slope_proxy: -0.007314

## VZLA (Vizsla Silver)
- close: 3.6265 | RSI14: 51.50582 | ATR14%: 6.62%
- MA20 gap: 0.81% | MA50 gap: 3.37% | MA200 gap: -14.73%
- vol_ratio(Volume/Vol20): 0.268284 | gap_open: 0.00%
- RS vs SILJ gap: 6.07% / slope_proxy: 0.004357
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
- close: 7.6 | RSI14: 49.464092 | ATR14%: 7.97%
- MA20 gap: 1.25% | MA50 gap: -7.16% | MA200 gap: -10.33%
- vol_ratio(Volume/Vol20): 0.161025 | gap_open: 0.66%
- SilverMarginGate: SI=69.824997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.12% / slope_proxy: -0.011491
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
- close: 26.5 | RSI14: 39.062003 | ATR14%: 10.62%
- MA20 gap: -11.56% | MA50 gap: -25.15% | MA200 gap: 4.44%
- vol_ratio(Volume/Vol20): 0.464218 | gap_open: 0.72%
- RS vs SILJ gap: -23.16% / slope_proxy: -0.063414
- RS vs GDXJ gap: -21.66% / slope_proxy: -0.012823
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

- 실행시간(UTC): **2026-06-16 15:08:19**
- 데이터 기준일(주가): **2026-06-16**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, USAS**

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
- IG OAS: N/A
- 10Y Real Yield: N/A
- VIX: N/A
- NFCI: N/A

### Leadership ratios

- GDX/GLD: gap 2.70% / slope_proxy 4.88%
- GDXJ/GLD: gap 2.44% / slope_proxy 3.64%
- SILJ/SLV: gap 5.82% / slope_proxy 10.48%
- Gold breadth proxy: above50 7.69%, above200 30.77%, count 13
- Silver breadth proxy: above50 15.38%, above200 61.54%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.09 | RSI14: 46.49 | ATR14%: 6.48%
- MA20/50/200 gap: 0.90% / 3.41% / 24.02%
- 5D return: 12.21% | 20D drawdown: -7.01% | vol_ratio: 0.21
- RS vs GDXJ: gap 10.94% / slope_proxy -3.41%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.43 | RSI14: 53.52 | ATR14%: 5.54%
- MA20/50/200 gap: 8.83% / 3.44% / -3.53%
- 5D return: 17.21% | 20D drawdown: 0.00% | vol_ratio: 0.42
- RS vs GDXJ: gap 6.98% / slope_proxy 3.24%
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
- close: 6.08 | RSI14: 46.12 | ATR14%: 6.88%
- MA20/50/200 gap: -0.57% / -8.74% / -12.18%
- 5D return: 6.11% | 20D drawdown: -13.76% | vol_ratio: 0.22
- RS vs GDXJ: gap -6.13% / slope_proxy -7.38%
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
- close: 1.72 | RSI14: 40.37 | ATR14%: 7.21%
- MA20/50/200 gap: -7.01% / -8.59% / 4.37%
- 5D return: 5.86% | 20D drawdown: -23.78% | vol_ratio: 0.35
- RS vs GDXJ: gap -2.07% / slope_proxy -25.50%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.82 | RSI14: 49.54 | ATR14%: 7.73%
- MA20/50/200 gap: 3.90% / -1.60% / 5.06%
- 5D return: 17.44% | 20D drawdown: -9.41% | vol_ratio: 0.30
- RS vs SILJ: gap 0.96% / slope_proxy 0.56%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 20.82 | RSI14: 57.26 | ATR14%: 7.14%
- MA20/50/200 gap: 12.49% / 14.47% / 38.79%
- 5D return: 18.90% | 20D drawdown: -3.12% | vol_ratio: 0.37
- RS vs SILJ: gap 20.51% / slope_proxy 12.88%
- FundamentalScore: 86 | TechnicalScore: 50 | RegimeScore: 55 | OverallScore: **67.2**
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
- close: 3.63 | RSI14: 50.16 | ATR14%: 7.18%
- MA20/50/200 gap: 0.81% / 3.37% / -14.73%
- 5D return: 8.90% | 20D drawdown: -12.19% | vol_ratio: 0.27
- RS vs SILJ: gap 6.07% / slope_proxy 6.26%
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
- close: 9.20 | RSI14: 46.53 | ATR14%: 6.79%
- MA20/50/200 gap: 2.12% / -2.89% / -2.01%
- 5D return: 14.49% | 20D drawdown: -7.67% | vol_ratio: 0.28
- RS vs SILJ: gap -0.75% / slope_proxy -2.71%
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
- close: 16.74 | RSI14: 45.27 | ATR14%: 6.10%
- MA20/50/200 gap: 1.72% / -6.51% / -5.08%
- 5D return: 12.39% | 20D drawdown: -5.98% | vol_ratio: 0.27
- RS vs SILJ: gap -5.48% / slope_proxy -2.75%
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
- close: 7.60 | RSI14: 47.98 | ATR14%: 8.06%
- MA20/50/200 gap: 1.25% / -7.16% / -10.33%
- 5D return: 24.59% | 20D drawdown: -9.31% | vol_ratio: 0.16
- RS vs SILJ: gap -5.12% / slope_proxy -11.79%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.78 | RSI14: 48.68 | ATR14%: 7.36%
- MA20/50/200 gap: 2.74% / -0.96% / 4.94%
- 5D return: 13.38% | 20D drawdown: -8.63% | vol_ratio: 0.49
- RS vs SILJ: gap 2.45% / slope_proxy -2.01%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **43.2**
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 26.48 | RSI14: 35.94 | ATR14%: 10.10%
- MA20/50/200 gap: -11.63% / -25.21% / 4.36%
- 5D return: 6.56% | 20D drawdown: -22.27% | vol_ratio: 0.46
- RS vs SILJ: gap -23.22% / slope_proxy -23.78%
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
