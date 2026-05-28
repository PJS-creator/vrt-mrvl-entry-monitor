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

- 실행시간(UTC): **2026-05-28 03:01:07**
- 데이터 기준일(일봉): **2026-05-27**
- 데이터 기준일(주봉): **2026-05-25**
- VXN 기준일: **2026-05-26** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 729.45
- Weekly RSI14: **76.29**
- 52W MA: 603.47 / gap: **20.88%**
- 104W MA gap: **33.65%**
- 52W MA 13W slope: **7.45%**
- VXN: **23.90** / 5D change: -0.31

## Daily trigger: 실제 매수 타이밍

- QQQ close: 729.45
- Daily RSI14: **74.62**
- 20D gap: **3.94%**
- 50D gap: **12.68%**
- 200D gap: **18.57%**
- MACD hist: -0.5222 / change: 0.1909
- ATR14%: **1.47%**
- 20D high drawdown: **-0.11%**

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

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-28 03:00:40**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 -13.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.1 / 4주 변화 18.0 bp
- VIX (VIXCLS): 17.01
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.239526
- MA60: 8.871997
- gap: 4.14%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.333669
- MA60: 0.281462
- gap: 18.55%
- MA60_slope_proxy: 0.041475
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-28 03:00:43**

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
- TERM_SPREAD_10Y_POLICY: 111.66 bp / 4주 변화 -1.24 bp
- CURVE_10s5s: 44.66 bp / 4주 변화 -1.35 bp

## NWG Price
- close: 599.6
- MA50: 576.4068 / gap50: 4.02%
- MA200: 586.5702 / gap200: 2.22%

## Relative Strength
- RS vs FTSE gap: 2.30% / slope_proxy: -0.001486
- RS vs Peers gap: -4.24% / slope_proxy: -0.030313

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-05-28 03:00:50**

## Commodity Regime

- WTI ref (CL=F): 90.73 / 5D -15.81%
- Brent ref (BZ=F): 94.36 / 5D -15.20%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.63
- Gas ref (NG=F): 3.08 / 5D -1.12%

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

- close: 56.89
- MA20 / MA60 / MA200: 57.85 / 58.24 / 48.01
- gap20 / gap60: -1.66% / -2.32%
- 5D return: -6.28%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 0.998245
- ratio_MA60: 1.002677
- ratio_gap: -0.44%
- ratio_slope_proxy(20d): 0.030678

### Volume (if available)

- volume: 11299561.00
- volume_MA20: 12515578.05
- volume_ratio: 0.90

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.96
- MA20 / MA60 / MA200: 20.55 / 20.05 / 14.99
- gap20 / gap60: -7.73% / -5.45%
- 5D return: -7.10%
- 20D high/low: 22.03 / 18.96

### Relative Strength

- ratio: 0.525062
- ratio_MA60: 0.524915
- ratio_gap: 0.03%
- ratio_slope_proxy(20d): 0.045515

### Volume (if available)

- volume: 16783100.00
- volume_MA20: 17833355.00
- volume_ratio: 0.94

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

- close: 6.18
- MA20 / MA60 / MA200: 6.74 / 6.50 / 4.80
- gap20 / gap60: -8.36% / -4.98%
- 5D return: -17.05%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014523
- ratio_MA60: 0.015754
- ratio_gap: -7.81%
- ratio_slope_proxy(20d): -0.000103

### Volume (if available)

- volume: 25752396.00
- volume_MA20: 35761569.80
- volume_ratio: 0.72

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

- close: 12.37
- MA20 / MA60 / MA200: 13.09 / 13.42 / 10.87
- gap20 / gap60: -5.52% / -7.79%
- 5D return: -16.31%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.053557
- ratio_MA60: 0.051468
- ratio_gap: 4.06%
- ratio_slope_proxy(20d): 0.002986

### Volume (if available)

- volume: 13391665.00
- volume_MA20: 20645548.25
- volume_ratio: 0.65

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

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-28 03:00:55**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -13.0 bp / latest 2.72
- IG OAS 4주 변화: -7.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 18.0 bp / latest 2.1
- VIX: 17.01
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -1.93% / slope_proxy: -0.011809
- GDXJ/GLD gap: -2.24% / slope_proxy: -0.006024

## VZLA (Vizsla Silver)
- close: 3.62 | RSI14: 53.929865 | ATR14%: 5.95%
- MA20 gap: 3.24% | MA50 gap: 6.87% | MA200 gap: -14.55%
- vol_ratio(Volume/Vol20): 1.012944 | gap_open: 2.15%
- RS vs SILJ gap: 9.64% / slope_proxy: -0.001531
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE

## SCZM (Santacruz Silver)
- close: 7.79 | RSI14: 40.205651 | ATR14%: 7.66%
- MA20 gap: -9.01% | MA50 gap: -6.79% | MA200 gap: -5.74%
- vol_ratio(Volume/Vol20): 0.997355 | gap_open: 3.60%
- SilverMarginGate: SI=73.370003 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.69% / slope_proxy: -0.014082
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
- close: 31.98 | RSI14: 39.800365 | ATR14%: 9.58%
- MA20 gap: -13.43% | MA50 gap: -13.29% | MA200 gap: 35.28%
- vol_ratio(Volume/Vol20): 0.659474 | gap_open: 3.64%
- RS vs SILJ gap: -10.43% / slope_proxy: 0.018115
- RS vs GDXJ gap: -7.74% / slope_proxy: 0.005946
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

- 실행시간(UTC): **2026-05-28 03:01:04**
- 데이터 기준일(주가): **2026-05-27**

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

- HY OAS: 2.72 / 4주 변화 -0.13 bp-ish / 2026-05-26
- IG OAS: 0.74 / 4주 변화 -0.07 bp-ish / 2026-05-26
- 10Y Real Yield: 2.10 / 4주 변화 0.19 bp-ish / 2026-05-26
- VIX: 17.01 / 4주 변화 -0.82 / 2026-05-26
- NFCI: -0.52 / 4주 변화 0.01 / 2026-05-15

### Leadership ratios

- GDX/GLD: gap -2.09% / slope_proxy 1.26%
- GDXJ/GLD: gap -2.24% / slope_proxy 1.32%
- SILJ/SLV: gap -1.93% / slope_proxy -0.82%
- Gold breadth proxy: above50 7.69%, above200 53.85%, count 13
- Silver breadth proxy: above50 15.38%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.35 | RSI14: 54.71 | ATR14%: 6.25%
- MA20/50/200 gap: 4.15% / 13.67% / 33.09%
- 5D return: 5.16% | 20D drawdown: -3.47% | vol_ratio: 0.80
- RS vs GDXJ: gap 22.95% / slope_proxy 16.96%
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
- close: 1.87 | RSI14: 54.30 | ATR14%: 10.39%
- MA20/50/200 gap: -5.36% / 2.69% / 19.91%
- 5D return: -13.43% | 20D drawdown: -24.90% | vol_ratio: 0.56
- RS vs GDXJ: gap 11.04% / slope_proxy 12.10%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.24 | RSI14: 39.86 | ATR14%: 6.28%
- MA20/50/200 gap: -5.26% / -9.17% / -8.44%
- 5D return: 0.32% | 20D drawdown: -15.22% | vol_ratio: 1.50
- RS vs GDXJ: gap -4.97% / slope_proxy -1.95%
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
- close: 1.32 | RSI14: 44.26 | ATR14%: 5.93%
- MA20/50/200 gap: -5.41% / -5.92% / -8.41%
- 5D return: -2.22% | 20D drawdown: -14.29% | vol_ratio: 0.38
- RS vs GDXJ: gap -0.64% / slope_proxy 1.40%
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
- close: 18.72 | RSI14: 53.37 | ATR14%: 7.46%
- MA20/50/200 gap: 0.97% / 10.70% / 30.48%
- 5D return: 13.32% | 20D drawdown: -12.61% | vol_ratio: 0.68
- RS vs SILJ: gap 16.09% / slope_proxy 8.05%
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
- close: 9.32 | RSI14: 50.08 | ATR14%: 8.42%
- MA20/50/200 gap: -4.16% / -2.32% / 1.47%
- 5D return: 3.44% | 20D drawdown: -18.67% | vol_ratio: 0.51
- RS vs SILJ: gap 0.28% / slope_proxy 1.43%
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
- close: 6.68 | RSI14: 48.28 | ATR14%: 7.80%
- MA20/50/200 gap: -2.81% / -0.65% / 6.14%
- 5D return: 3.09% | 20D drawdown: -16.19% | vol_ratio: 0.48
- RS vs SILJ: gap 2.32% / slope_proxy 3.85%
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
- close: 5.86 | RSI14: 40.37 | ATR14%: 8.74%
- MA20/50/200 gap: -5.06% / -1.91% / 9.70%
- 5D return: 3.72% | 20D drawdown: -20.92% | vol_ratio: 0.62
- RS vs SILJ: gap -2.44% / slope_proxy 3.20%
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
- close: 3.62 | RSI14: 54.88 | ATR14%: 6.25%
- MA20/50/200 gap: 3.24% / 6.87% / -14.55%
- 5D return: 11.04% | 20D drawdown: -5.97% | vol_ratio: 1.01
- RS vs SILJ: gap 9.64% / slope_proxy 3.12%
- FundamentalScore: 72 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **62.6**
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
- close: 16.94 | RSI14: 44.21 | ATR14%: 7.42%
- MA20/50/200 gap: -6.41% / -8.13% / -0.86%
- 5D return: 3.55% | 20D drawdown: -19.52% | vol_ratio: 0.66
- RS vs SILJ: gap -5.22% / slope_proxy -6.08%
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
- close: 7.79 | RSI14: 38.44 | ATR14%: 7.96%
- MA20/50/200 gap: -9.01% / -6.79% / -5.74%
- 5D return: -5.35% | 20D drawdown: -23.25% | vol_ratio: 1.00
- RS vs SILJ: gap -4.69% / slope_proxy -2.39%
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
- close: 31.98 | RSI14: 34.30 | ATR14%: 10.27%
- MA20/50/200 gap: -13.43% / -13.29% / 35.28%
- 5D return: -3.63% | 20D drawdown: -29.19% | vol_ratio: 0.66
- RS vs SILJ: gap -10.43% / slope_proxy -9.46%
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
