# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-05-28 15:01:17**
- 데이터 기준일(일봉): **2026-05-28**
- 데이터 기준일(주봉): **2026-05-25**
- VXN 기준일: **2026-05-27** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 733.42
- Weekly RSI14: **76.78**
- 52W MA: 603.54 / gap: **21.52%**
- 104W MA gap: **34.37%**
- 52W MA 13W slope: **7.47%**
- VXN: **23.39** / 5D change: -0.70

## Daily trigger: 실제 매수 타이밍

- QQQ close: 733.42
- Daily RSI14: **75.82**
- 20D gap: **3.97%**
- 50D gap: **12.84%**
- 200D gap: **19.06%**
- MACD hist: -0.3176 / change: 0.2046
- ATR14%: **1.42%**
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

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-28 15:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.1 / 4주 변화 18.0 bp
- VIX (VIXCLS): 16.29
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.960276
- MA60: 8.896488
- gap: 0.72%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.329681
- MA60: 0.283655
- gap: 16.23%
- MA60_slope_proxy: 0.041657
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-28 15:00:48**

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
- TERM_SPREAD_10Y_POLICY: 109.28 bp / 4주 변화 -10.65 bp
- CURVE_10s5s: 45.09 bp / 4주 변화 -1.62 bp

## NWG Price
- close: 590.2
- MA50: 576.9113 / gap50: 2.30%
- MA200: 586.8572 / gap200: 0.57%

## Relative Strength
- RS vs FTSE gap: 1.45% / slope_proxy: -0.001335
- RS vs Peers gap: -4.21% / slope_proxy: -0.028866

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-28 15:00:56**

## Commodity Regime

- WTI ref (CL=F): 89.44 / 5D -8.98%
- Brent ref (BZ=F): 93.18 / 5D -11.27%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.74
- Gas ref (NG=F): 3.21 / 5D 7.02%

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

- close: 57.38
- MA20 / MA60 / MA200: 57.68 / 58.31 / 48.08
- gap20 / gap60: -0.53% / -1.59%
- 5D return: -2.53%
- 20D high/low: 60.70 / 53.03

### Relative Strength

- ratio: 1.007412
- ratio_MA60: 1.003610
- ratio_gap: 0.38%
- ratio_slope_proxy(20d): 0.029067

### Volume (if available)

- volume: 4984163.00
- volume_MA20: 12078443.15
- volume_ratio: 0.41

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.90
- MA20 / MA60 / MA200: 20.40 / 20.09 / 15.02
- gap20 / gap60: -7.35% / -5.91%
- 5D return: -4.69%
- 20D high/low: 22.03 / 18.90

### Relative Strength

- ratio: 0.521374
- ratio_MA60: 0.525972
- ratio_gap: -0.87%
- ratio_slope_proxy(20d): 0.043800

### Volume (if available)

- volume: 3107062.00
- volume_MA20: 17015128.10
- volume_ratio: 0.18

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
- MA20 / MA60 / MA200: 6.71 / 6.51 / 4.82
- gap20 / gap60: -7.68% / -4.84%
- 5D return: -15.67%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014691
- ratio_MA60: 0.015734
- ratio_gap: -6.63%
- ratio_slope_proxy(20d): -0.000153

### Volume (if available)

- volume: 5486544.00
- volume_MA20: 34586697.20
- volume_ratio: 0.16

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

- close: 12.54
- MA20 / MA60 / MA200: 13.06 / 13.43 / 10.87
- gap20 / gap60: -4.03% / -6.69%
- 5D return: -10.66%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.054519
- ratio_MA60: 0.051600
- ratio_gap: 5.66%
- ratio_slope_proxy(20d): 0.003037

### Volume (if available)

- volume: 3675563.00
- volume_MA20: 19607403.15
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-28 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -11.0 bp / latest 2.71
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.1
- VIX: 16.29
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: -0.30% / slope_proxy: -0.012559
- GDXJ/GLD gap: -1.55% / slope_proxy: -0.006125

## VZLA (Vizsla Silver)
- close: 3.7 | RSI14: 56.27047 | ATR14%: 5.75%
- MA20 gap: 5.07% | MA50 gap: 9.15% | MA200 gap: -12.70%
- vol_ratio(Volume/Vol20): 0.383895 | gap_open: 1.38%
- RS vs SILJ gap: 10.06% / slope_proxy: -0.000659
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

## SCZM (Santacruz Silver)
- close: 7.9 | RSI14: 41.84125 | ATR14%: 7.35%
- MA20 gap: -7.82% | MA50 gap: -5.30% | MA200 gap: -4.63%
- vol_ratio(Volume/Vol20): 0.358114 | gap_open: 0.26%
- SilverMarginGate: SI=74.93 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.66% / slope_proxy: -0.013277
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
- close: 32.119999 | RSI14: 40.165794 | ATR14%: 9.18%
- MA20 gap: -12.81% | MA50 gap: -12.52% | MA200 gap: 35.05%
- vol_ratio(Volume/Vol20): 0.241303 | gap_open: 1.81%
- RS vs SILJ gap: -11.17% / slope_proxy: 0.012201
- RS vs GDXJ gap: -7.99% / slope_proxy: 0.004634
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

- 실행시간(UTC): **2026-05-28 15:01:14**
- 데이터 기준일(주가): **2026-05-28**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **True**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 -0.11 bp-ish / 2026-05-27
- IG OAS: 0.74 / 4주 변화 -0.07 bp-ish / 2026-05-27
- 10Y Real Yield: 2.10 / 4주 변화 0.19 bp-ish / 2026-05-26
- VIX: 16.29 / 4주 변화 -2.52 / 2026-05-27
- NFCI: -0.51 / 4주 변화 0.04 / 2026-05-22

### Leadership ratios

- GDX/GLD: gap -1.18% / slope_proxy 1.19%
- GDXJ/GLD: gap -1.55% / slope_proxy 0.90%
- SILJ/SLV: gap -0.30% / slope_proxy 0.06%
- Gold breadth proxy: above50 7.69%, above200 61.54%, count 13
- Silver breadth proxy: above50 30.77%, above200 76.92%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.45 | RSI14: 57.81 | ATR14%: 6.05%
- MA20/50/200 gap: 4.59% / 14.49% / 34.23%
- 5D return: 3.43% | 20D drawdown: -2.31% | vol_ratio: 0.31
- RS vs GDXJ: gap 22.52% / slope_proxy 15.86%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **68.3**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.86 | RSI14: 52.22 | ATR14%: 9.87%
- MA20/50/200 gap: -6.34% / 1.94% / 18.82%
- 5D return: -11.85% | 20D drawdown: -25.30% | vol_ratio: 0.21
- RS vs GDXJ: gap 9.08% / slope_proxy 11.83%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **60.5**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.36 | RSI14: 45.60 | ATR14%: 5.59%
- MA20/50/200 gap: -2.92% / -3.29% / -6.22%
- 5D return: 1.12% | 20D drawdown: -12.01% | vol_ratio: 0.22
- RS vs GDXJ: gap 0.93% / slope_proxy 0.18%
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
- close: 6.39 | RSI14: 44.03 | ATR14%: 5.84%
- MA20/50/200 gap: -2.99% / -6.64% / -6.38%
- 5D return: 6.68% | 20D drawdown: -13.18% | vol_ratio: 0.18
- RS vs GDXJ: gap -3.58% / slope_proxy -0.04%
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 19.17 | RSI14: 52.51 | ATR14%: 7.06%
- MA20/50/200 gap: 2.73% / 12.84% / 33.13%
- 5D return: 13.03% | 20D drawdown: -10.50% | vol_ratio: 0.19
- RS vs SILJ: gap 16.58% / slope_proxy 9.33%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.52 | RSI14: 44.08 | ATR14%: 7.01%
- MA20/50/200 gap: -2.42% / -0.08% / 3.42%
- 5D return: 1.70% | 20D drawdown: -16.93% | vol_ratio: 0.33
- RS vs SILJ: gap 0.83% / slope_proxy 1.64%
- FundamentalScore: 82 | TechnicalScore: 85 | RegimeScore: 55 | OverallScore: **77.6**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.82 | RSI14: 49.55 | ATR14%: 7.23%
- MA20/50/200 gap: -1.13% / 1.54% / 8.20%
- 5D return: 0.66% | 20D drawdown: -14.37% | vol_ratio: 0.29
- RS vs SILJ: gap 2.88% / slope_proxy 4.45%
- FundamentalScore: 60 | TechnicalScore: 85 | RegimeScore: 55 | OverallScore: **67.8**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.97 | RSI14: 43.82 | ATR14%: 8.06%
- MA20/50/200 gap: -3.56% / 0.48% / 11.51%
- 5D return: 7.27% | 20D drawdown: -19.37% | vol_ratio: 0.22
- RS vs SILJ: gap -1.73% / slope_proxy 2.95%
- FundamentalScore: 68 | TechnicalScore: 60 | RegimeScore: 55 | OverallScore: **62.6**
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
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, RelativeStrength(vs SILJ)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.70 | RSI14: 57.99 | ATR14%: 5.89%
- MA20/50/200 gap: 5.07% / 9.15% / -12.70%
- 5D return: 9.14% | 20D drawdown: -3.90% | vol_ratio: 0.38
- RS vs SILJ: gap 10.06% / slope_proxy 7.89%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.12 | RSI14: 45.52 | ATR14%: 6.92%
- MA20/50/200 gap: -5.29% / -6.88% / -0.06%
- 5D return: -0.32% | 20D drawdown: -18.65% | vol_ratio: 0.31
- RS vs SILJ: gap -5.66% / slope_proxy -6.34%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.90 | RSI14: 38.74 | ATR14%: 7.34%
- MA20/50/200 gap: -7.82% / -5.30% / -4.63%
- 5D return: -5.73% | 20D drawdown: -22.17% | vol_ratio: 0.36
- RS vs SILJ: gap -4.66% / slope_proxy -0.94%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 32.16 | RSI14: 36.05 | ATR14%: 9.52%
- MA20/50/200 gap: -12.70% / -12.42% / 35.22%
- 5D return: -5.59% | 20D drawdown: -28.79% | vol_ratio: 0.24
- RS vs SILJ: gap -11.06% / slope_proxy -13.07%
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
- Why not today: SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
