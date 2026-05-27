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

- 실행시간(UTC): **2026-05-27 16:42:29**
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

- QQQ close: 729.12
- Weekly RSI14: **76.25**
- 52W MA: 603.46 / gap: **20.82%**
- 104W MA gap: **33.59%**
- 52W MA 13W slope: **7.45%**
- VXN: **23.90** / 5D change: -0.31

## Daily trigger: 실제 매수 타이밍

- QQQ close: 729.12
- Daily RSI14: **74.33**
- 20D gap: **3.89%**
- 50D gap: **12.63%**
- 200D gap: **18.52%**
- MACD hist: -0.5433 / change: 0.1698
- ATR14%: **1.47%**
- 20D high drawdown: **-0.16%**

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
- 실행시간(UTC): **2026-05-27 16:41:56**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 -13.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.16 / 4주 변화 27.0 bp
- VIX (VIXCLS): 17.01
- NFCI: -0.523

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.274657
- MA60: 8.872583
- gap: 4.53%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.339868
- MA60: 0.281566
- gap: 20.71%
- MA60_slope_proxy: 0.041579
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-05-27**
- 실행시간(UTC): **2026-05-27 16:41:58**

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

- 실행시간(UTC): **2026-05-27 16:42:06**

## Commodity Regime

- WTI ref (CL=F): 89.99 / 5D -16.50%
- Brent ref (BZ=F): 93.40 / 5D -16.07%
- Brent Tier: **>=90**
- Brent-WTI spread: 3.41
- Gas ref (NG=F): 3.13 / 5D 0.45%

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

- close: 57.30
- MA20 / MA60 / MA200: 57.87 / 58.25 / 48.01
- gap20 / gap60: -0.99% / -1.63%
- 5D return: -5.60%
- 20D high/low: 60.76 / 53.03

### Relative Strength

- ratio: 1.003063
- ratio_MA60: 1.002757
- ratio_gap: 0.03%
- ratio_slope_proxy(20d): 0.030758

### Volume (if available)

- volume: 5822416.00
- volume_MA20: 12240780.80
- volume_ratio: 0.48

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.03
- MA20 / MA60 / MA200: 20.55 / 20.05 / 14.99
- gap20 / gap60: -7.40% / -5.11%
- 5D return: -6.76%
- 20D high/low: 22.03 / 19.03

### Relative Strength

- ratio: 0.524729
- ratio_MA60: 0.524909
- ratio_gap: -0.03%
- ratio_slope_proxy(20d): 0.045509

### Volume (if available)

- volume: 9651952.00
- volume_MA20: 17476797.60
- volume_ratio: 0.55

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

- close: 6.24
- MA20 / MA60 / MA200: 6.75 / 6.50 / 4.81
- gap20 / gap60: -7.51% / -4.07%
- 5D return: -16.24%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014621
- ratio_MA60: 0.015756
- ratio_gap: -7.20%
- ratio_slope_proxy(20d): -0.000102

### Volume (if available)

- volume: 16100494.00
- volume_MA20: 35278974.70
- volume_ratio: 0.46

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

- close: 12.51
- MA20 / MA60 / MA200: 13.10 / 13.42 / 10.87
- gap20 / gap60: -4.54% / -6.80%
- 5D return: -15.39%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.053794
- ratio_MA60: 0.051472
- ratio_gap: 4.51%
- ratio_slope_proxy(20d): 0.002990

### Volume (if available)

- volume: 6329076.00
- volume_MA20: 20291708.80
- volume_ratio: 0.31

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
- 실행시간(UTC): **2026-05-27 16:42:16**

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
- 10Y Real Yield 4주 변화: 27.0 bp / latest 2.16
- VIX: 17.01
- NFCI: -0.523

### Leadership ratios
- SILJ/SLV gap: -1.11% / slope_proxy: -0.011748
- GDXJ/GLD gap: -1.20% / slope_proxy: -0.005975

## VZLA (Vizsla Silver)
- close: 3.7 | RSI14: 56.750442 | ATR14%: 5.83%
- MA20 gap: 5.40% | MA50 gap: 9.18% | MA200 gap: -12.67%
- vol_ratio(Volume/Vol20): 0.672084 | gap_open: 2.15%
- RS vs SILJ gap: 10.83% / slope_proxy: -0.001508
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
- close: 7.92 | RSI14: 41.486002 | ATR14%: 7.53%
- MA20 gap: -7.56% | MA50 gap: -5.26% | MA200 gap: -4.17%
- vol_ratio(Volume/Vol20): 0.56025 | gap_open: 3.60%
- SilverMarginGate: SI=75.07 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.15% / slope_proxy: -0.014057
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
- close: 32.580299 | RSI14: 40.792315 | ATR14%: 9.41%
- MA20 gap: -11.88% | MA50 gap: -11.69% | MA200 gap: 37.80%
- vol_ratio(Volume/Vol20): 0.361818 | gap_open: 3.64%
- RS vs SILJ gap: -9.75% / slope_proxy: 0.018256
- RS vs GDXJ gap: -7.07% / slope_proxy: 0.00598
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

- 실행시간(UTC): **2026-05-27 16:42:27**
- 데이터 기준일(주가): **2026-05-27**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **True**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.72 / 4주 변화 -0.13 bp-ish / 2026-05-26
- IG OAS: 0.74 / 4주 변화 -0.07 bp-ish / 2026-05-26
- 10Y Real Yield: 2.16 / 4주 변화 0.27 bp-ish / 2026-05-22
- VIX: 17.01 / 4주 변화 -0.82 / 2026-05-26
- NFCI: -0.52 / 4주 변화 0.01 / 2026-05-15

### Leadership ratios

- GDX/GLD: gap -1.05% / slope_proxy 2.35%
- GDXJ/GLD: gap -1.20% / slope_proxy 2.41%
- SILJ/SLV: gap -1.09% / slope_proxy 0.04%
- Gold breadth proxy: above50 7.69%, above200 61.54%, count 13
- Silver breadth proxy: above50 23.08%, above200 84.62%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.58 | RSI14: 57.77 | ATR14%: 6.04%
- MA20/50/200 gap: 6.87% / 16.73% / 36.73%
- 5D return: 8.06% | 20D drawdown: -0.81% | vol_ratio: 0.38
- RS vs GDXJ: gap 24.87% / slope_proxy 18.83%
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
- 5D return: -13.43% | 20D drawdown: -24.90% | vol_ratio: 0.46
- RS vs GDXJ: gap 9.81% / slope_proxy 10.84%
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
- close: 6.33 | RSI14: 41.16 | ATR14%: 6.19%
- MA20/50/200 gap: -3.96% / -7.88% / -7.13%
- 5D return: 1.77% | 20D drawdown: -13.99% | vol_ratio: 1.12
- RS vs GDXJ: gap -4.69% / slope_proxy -1.66%
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
- close: 1.36 | RSI14: 47.37 | ATR14%: 5.59%
- MA20/50/200 gap: -2.68% / -3.12% / -5.65%
- 5D return: 0.74% | 20D drawdown: -11.69% | vol_ratio: 0.19
- RS vs GDXJ: gap 1.19% / slope_proxy 3.30%
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

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 18.74 | RSI14: 53.47 | ATR14%: 7.45%
- MA20/50/200 gap: 1.07% / 10.81% / 30.61%
- 5D return: 13.44% | 20D drawdown: -12.51% | vol_ratio: 0.30
- RS vs SILJ: gap 14.97% / slope_proxy 7.00%
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
- close: 9.41 | RSI14: 50.89 | ATR14%: 8.33%
- MA20/50/200 gap: -3.23% / -1.34% / 2.50%
- 5D return: 4.50% | 20D drawdown: -17.84% | vol_ratio: 0.30
- RS vs SILJ: gap 0.21% / slope_proxy 1.35%
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
- close: 6.77 | RSI14: 49.44 | ATR14%: 7.69%
- MA20/50/200 gap: -1.59% / 0.64% / 7.53%
- 5D return: 4.45% | 20D drawdown: -15.08% | vol_ratio: 0.30
- RS vs SILJ: gap 2.55% / slope_proxy 4.09%
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
- close: 5.86 | RSI14: 40.37 | ATR14%: 8.68%
- MA20/50/200 gap: -5.06% / -1.91% / 9.70%
- 5D return: 3.72% | 20D drawdown: -20.92% | vol_ratio: 0.36
- RS vs SILJ: gap -3.48% / slope_proxy 2.08%
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
- close: 3.70 | RSI14: 57.69 | ATR14%: 6.11%
- MA20/50/200 gap: 5.40% / 9.18% / -12.67%
- 5D return: 13.50% | 20D drawdown: -3.90% | vol_ratio: 0.67
- RS vs SILJ: gap 10.83% / slope_proxy 4.26%
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
- close: 17.11 | RSI14: 44.96 | ATR14%: 7.33%
- MA20/50/200 gap: -5.49% / -7.20% / 0.16%
- 5D return: 4.61% | 20D drawdown: -18.69% | vol_ratio: 0.36
- RS vs SILJ: gap -5.28% / slope_proxy -6.14%
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
- close: 7.92 | RSI14: 39.70 | ATR14%: 7.82%
- MA20/50/200 gap: -7.56% / -5.26% / -4.17%
- 5D return: -3.77% | 20D drawdown: -21.97% | vol_ratio: 0.56
- RS vs SILJ: gap -4.15% / slope_proxy -1.84%
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
- close: 32.58 | RSI14: 35.15 | ATR14%: 10.09%
- MA20/50/200 gap: -11.88% / -11.69% / 37.80%
- 5D return: -1.82% | 20D drawdown: -27.86% | vol_ratio: 0.36
- RS vs SILJ: gap -9.75% / slope_proxy -8.75%
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
