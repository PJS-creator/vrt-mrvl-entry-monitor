# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-02 15:01:19**
- 데이터 기준일(일봉): **2026-09-02**
- 데이터 기준일(주봉): **2026-08-31**
- VXN 기준일: **2026-09-01** / source: `FRED: VXNCLS`

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
- Weekly RSI14: **55.65**
- 52W MA: 645.59 / gap: **9.57%**
- 104W MA gap: **22.32%**
- 52W MA 13W slope: **6.46%**
- VXN: **21.96** / 5D change: 0.17

## Daily trigger: 실제 매수 타이밍

- QQQ close: 707.37
- Daily RSI14: **46.42**
- 20D gap: **-1.41%**
- 50D gap: **-0.49%**
- 200D gap: **7.89%**
- MACD hist: -1.2539 / change: -0.3173
- ATR14%: **1.38%**
- 20D high drawdown: **-3.37%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-02 15:00:50**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.65 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.44 / 4주 변화 1.0 bp
- VIX (VIXCLS): 16.34
- NFCI: -0.558

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.423721
- MA60: 9.093528
- gap: -7.37%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.373454
- MA60: 0.397917
- gap: -6.15%
- MA60_slope_proxy: 0.010635
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-02 15:00:52**

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
- TERM_SPREAD_10Y_POLICY: 131.31 bp / 4주 변화 3.74 bp
- CURVE_10s5s: 46.96 bp / 4주 변화 0.08 bp

## NWG Price
- close: 692.8
- MA50: 682.3499 / gap50: 1.53%
- MA200: 626.423 / gap200: 10.60%

## Relative Strength
- RS vs FTSE gap: 1.83% / slope_proxy: 0.002684
- RS vs Peers gap: 0.99% / slope_proxy: 0.018789

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-02 15:01:03**

## Commodity Regime

- WTI ref (CL=F): 90.44 / 5D 9.98%
- Brent ref (BZ=F): 95.14 / 5D 8.31%
- Brent Tier: **>=90**
- Brent-WTI spread: 4.70
- Gas ref (NG=F): 2.96 / 5D 4.29%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **True**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 60.62
- MA20 / MA60 / MA200: 59.16 / 55.50 / 51.95
- gap20 / gap60: 2.47% / 9.23%
- 5D return: 3.41%
- 20D high/low: 61.52 / 55.91

### Relative Strength

- ratio: 0.936433
- ratio_MA60: 0.953070
- ratio_gap: -1.75%
- ratio_slope_proxy(20d): -0.015103

### Volume (if available)

- volume: 1426339.00
- volume_MA20: 7495616.95
- volume_ratio: 0.19

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.58
- MA20 / MA60 / MA200: 18.19 / 17.47 / 16.40
- gap20 / gap60: 13.09% / 17.75%
- 5D return: 15.85%
- 20D high/low: 20.58 / 17.25

### Relative Strength

- ratio: 0.541875
- ratio_MA60: 0.497876
- ratio_gap: 8.84%
- ratio_slope_proxy(20d): -0.000912

### Volume (if available)

- volume: 5675471.00
- volume_MA20: 19234863.55
- volume_ratio: 0.30

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.01
- MA20 / MA60 / MA200: 5.75 / 5.44 / 5.54
- gap20 / gap60: 4.61% / 10.64%
- 5D return: 7.41%
- 20D high/low: 6.01 / 5.16

### Relative Strength

- ratio: 0.013979
- ratio_MA60: 0.013763
- ratio_gap: 1.56%
- ratio_slope_proxy(20d): -0.000417

### Volume (if available)

- volume: 9149693.00
- volume_MA20: 39159334.65
- volume_ratio: 0.23

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.57
- MA20 / MA60 / MA200: 14.08 / 12.97 / 11.30
- gap20 / gap60: 3.53% / 12.35%
- 5D return: 1.92%
- 20D high/low: 15.11 / 13.22

### Relative Strength

- ratio: 0.049824
- ratio_MA60: 0.050114
- ratio_gap: -0.58%
- ratio_slope_proxy(20d): -0.001304

### Volume (if available)

- volume: 3717907.00
- volume_MA20: 13334125.35
- volume_ratio: 0.28

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-02**
- 실행시간(UTC): **2026-09-02 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.65
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 1.0 bp / latest 2.44
- VIX: 16.34
- NFCI: -0.558

### Leadership ratios
- SILJ/SLV gap: 9.68% / slope_proxy: 0.026416
- GDXJ/GLD gap: 14.05% / slope_proxy: 0.008671

## VZLA (Vizsla Silver)
- close: 4.085 | RSI14: 60.527672 | ATR14%: 4.87%
- MA20 gap: 5.60% | MA50 gap: 17.46% | MA200 gap: 0.40%
- vol_ratio(Volume/Vol20): 0.254717 | gap_open: 2.85%
- RS vs SILJ gap: 2.74% / slope_proxy: 0.001552
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
- close: 10.0 | RSI14: 65.138829 | ATR14%: 5.84%
- MA20 gap: 8.69% | MA50 gap: 31.74% | MA200 gap: 13.74%
- vol_ratio(Volume/Vol20): 0.558877 | gap_open: 1.96%
- SilverMarginGate: SI=65.754997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 17.83% / slope_proxy: 0.008647
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

## HYMC (Hycroft Mining)
- close: 22.950001 | RSI14: 45.156746 | ATR14%: 8.43%
- MA20 gap: -10.52% | MA50 gap: -0.41% | MA200 gap: -22.90%
- vol_ratio(Volume/Vol20): 0.523009 | gap_open: 2.84%
- RS vs SILJ gap: -14.19% / slope_proxy: -0.099452
- RS vs GDXJ gap: -17.14% / slope_proxy: -0.029814
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

- 실행시간(UTC): **2026-09-02 15:01:18**
- 데이터 기준일(주가): **2026-09-02**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, SCZM, HL, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.65 / 4주 변화 -0.08 bp-ish / 2026-09-01
- IG OAS: 0.81 / 4주 변화 0.03 bp-ish / 2026-09-01
- 10Y Real Yield: 2.44 / 4주 변화 0.01 bp-ish / 2026-08-31
- VIX: 16.34 / 4주 변화 -0.16 / 2026-09-01
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-08-28

### Leadership ratios

- GDX/GLD: gap 13.61% / slope_proxy 12.67%
- GDXJ/GLD: gap 14.05% / slope_proxy 12.93%
- SILJ/SLV: gap 9.71% / slope_proxy 8.09%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 92.31%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.81 | RSI14: 50.78 | ATR14%: 5.51%
- MA20/50/200 gap: -2.91% / 16.03% / 33.29%
- 5D return: -10.16% | 20D drawdown: -11.38% | vol_ratio: 0.22
- RS vs GDXJ: gap 0.30% / slope_proxy -2.59%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **75.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.64 | RSI14: 61.35 | ATR14%: 4.83%
- MA20/50/200 gap: 4.31% / 25.27% / 9.52%
- 5D return: -2.92% | 20D drawdown: -6.49% | vol_ratio: 0.25
- RS vs GDXJ: gap 8.24% / slope_proxy 4.78%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.52 | RSI14: 56.92 | ATR14%: 5.43%
- MA20/50/200 gap: -0.82% / 16.46% / 2.19%
- 5D return: -4.40% | 20D drawdown: -7.88% | vol_ratio: 0.19
- RS vs GDXJ: gap -0.55% / slope_proxy -3.89%
- FundamentalScore: 70 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **67.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.80 | RSI14: 77.17 | ATR14%: 6.38%
- MA20/50/200 gap: 15.94% / 37.52% / 46.56%
- 5D return: 7.69% | 20D drawdown: 0.00% | vol_ratio: 0.80
- RS vs GDXJ: gap 21.32% / slope_proxy 24.76%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **57.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.74 | RSI14: 52.99 | ATR14%: 6.63%
- MA20/50/200 gap: 2.20% / 22.22% / 53.23%
- 5D return: -0.11% | 20D drawdown: -5.29% | vol_ratio: 0.32
- RS vs SILJ: gap 10.71% / slope_proxy -3.22%
- FundamentalScore: 86 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **74.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.83 | RSI14: 54.50 | ATR14%: 6.55%
- MA20/50/200 gap: 3.27% / 20.36% / 10.56%
- 5D return: -0.55% | 20D drawdown: -4.16% | vol_ratio: 0.39
- RS vs SILJ: gap 6.88% / slope_proxy 7.84%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.39 | RSI14: 62.89 | ATR14%: 5.61%
- MA20/50/200 gap: 6.12% / 21.22% / 7.85%
- 5D return: -1.50% | 20D drawdown: -4.85% | vol_ratio: 0.17
- RS vs SILJ: gap 7.77% / slope_proxy 13.03%
- FundamentalScore: 78 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **72.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.43 | RSI14: 58.24 | ATR14%: 5.85%
- MA20/50/200 gap: 2.55% / 15.50% / 7.78%
- 5D return: -2.04% | 20D drawdown: -3.82% | vol_ratio: 0.30
- RS vs SILJ: gap 1.59% / slope_proxy 2.46%
- FundamentalScore: 60 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **71.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 10.01 | RSI14: 64.18 | ATR14%: 6.08%
- MA20/50/200 gap: 8.79% / 31.87% / 13.85%
- 5D return: 3.95% | 20D drawdown: -0.10% | vol_ratio: 0.56
- RS vs SILJ: gap 17.91% / slope_proxy 10.43%
- FundamentalScore: 74 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **71.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.09 | RSI14: 61.02 | ATR14%: 4.90%
- MA20/50/200 gap: 5.60% / 17.46% / 0.40%
- 5D return: 1.62% | 20D drawdown: -1.80% | vol_ratio: 0.26
- RS vs SILJ: gap 2.71% / slope_proxy 1.75%
- FundamentalScore: 72 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **70.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.35 | RSI14: 55.68 | ATR14%: 6.17%
- MA20/50/200 gap: 1.80% / 14.76% / -8.42%
- 5D return: -3.95% | 20D drawdown: -6.80% | vol_ratio: 0.27
- RS vs SILJ: gap -1.43% / slope_proxy 0.72%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 22.97 | RSI14: 40.12 | ATR14%: 8.69%
- MA20/50/200 gap: -10.46% / -0.35% / -22.85%
- 5D return: -9.80% | 20D drawdown: -17.69% | vol_ratio: 0.52
- RS vs SILJ: gap -14.17% / slope_proxy -15.16%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
- Checks:
  - sector_ok: **False**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
