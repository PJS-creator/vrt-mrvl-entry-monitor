# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-25 15:01:31**
- 데이터 기준일(일봉): **2026-08-25**
- 데이터 기준일(주봉): **2026-08-24**
- VXN 기준일: **2026-08-24** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 709.43
- Weekly RSI14: **56.51**
- 52W MA: 642.88 / gap: **10.35%**
- 104W MA gap: **23.23%**
- 52W MA 13W slope: **6.61%**
- VXN: **22.69** / 5D change: 1.18

## Daily trigger: 실제 매수 타이밍

- QQQ close: 709.43
- Daily RSI14: **48.25**
- 20D gap: **-0.37%**
- 50D gap: **-0.49%**
- 200D gap: **8.70%**
- MACD hist: -1.2088 / change: -0.3200
- ATR14%: **1.55%**
- 20D high drawdown: **-3.09%**

## Checks

- weekly_good: **False**
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

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 15:00:46**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.69 / 4주 변화 -12.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.4 / 4주 변화 -3.0 bp
- VIX (VIXCLS): 15.85
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.115956
- MA60: 9.19536
- gap: -11.74%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.439133
- MA60: 0.403847
- gap: 8.74%
- MA60_slope_proxy: 0.020532
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 130.06 bp / 4주 변화 2.53 bp
- CURVE_10s5s: 49.44 bp / 4주 변화 3.69 bp

## NWG Price
- close: 690.0
- MA50: 677.3649 / gap50: 1.87%
- MA200: 624.2116 / gap200: 10.54%

## Relative Strength
- RS vs FTSE gap: 1.32% / slope_proxy: 0.002945
- RS vs Peers gap: 2.09% / slope_proxy: 0.017617

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-25 15:00:59**

## Commodity Regime

- WTI ref (CL=F): 82.61 / 5D -2.74%
- Brent ref (BZ=F): 88.07 / 5D -3.24%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.46
- Gas ref (NG=F): 2.77 / 5D -0.18%

## Gates

- **RISK_OK_STRICT**: **True**
- **RISK_OK_SOFT**: **True**
- **OVX_OK**: **True**
- **WTI_TREND_UP**: **True**
- **BRENT_TREND_UP**: **False**
- **OIL_TREND_UP**: **True**
- **BRAZIL_RISK_OK**: **False**

## OXY

- **ENTRY**: **False**

### Trend

- close: 59.13
- MA20 / MA60 / MA200: 57.93 / 55.35 / 51.39
- gap20 / gap60: 2.07% / 6.83%
- 5D return: -1.11%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.943819
- ratio_MA60: 0.959786
- ratio_gap: -1.66%
- ratio_slope_proxy(20d): -0.012095

### Volume (if available)

- volume: 1916278.00
- volume_MA20: 7982588.90
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.78
- MA20 / MA60 / MA200: 18.45 / 17.82 / 16.67
- gap20 / gap60: -3.64% / -0.25%
- 5D return: -2.20%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.505257
- ratio_MA60: 0.510873
- ratio_gap: -1.10%
- ratio_slope_proxy(20d): -0.004456

### Volume (if available)

- volume: 7317951.00
- volume_MA20: 15772137.55
- volume_ratio: 0.46

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

- close: 5.79
- MA20 / MA60 / MA200: 5.55 / 5.47 / 5.49
- gap20 / gap60: 4.23% / 5.70%
- 5D return: -0.60%
- 20D high/low: 6.01 / 4.95

### Relative Strength

- ratio: 0.014148
- ratio_MA60: 0.013825
- ratio_gap: 2.33%
- ratio_slope_proxy(20d): -0.000497

### Volume (if available)

- volume: 8633859.00
- volume_MA20: 42363537.95
- volume_ratio: 0.20

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **True**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.04
- MA20 / MA60 / MA200: 13.61 / 12.79 / 11.10
- gap20 / gap60: 3.17% / 9.83%
- 5D return: -1.09%
- 20D high/low: 14.39 / 12.43

### Relative Strength

- ratio: 0.050239
- ratio_MA60: 0.050451
- ratio_gap: -0.42%
- ratio_slope_proxy(20d): -0.000720

### Volume (if available)

- volume: 2579952.00
- volume_MA20: 12873552.60
- volume_ratio: 0.20

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

- 데이터 기준일(주가): **2026-08-25**
- 실행시간(UTC): **2026-08-25 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -12.0 bp / latest 2.69
- IG OAS 4주 변화: 0.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 2.4
- VIX: 15.85
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 9.63% / slope_proxy: 0.021831
- GDXJ/GLD gap: 15.08% / slope_proxy: 0.002732

## VZLA (Vizsla Silver)
- close: 3.985 | RSI14: 64.221797 | ATR14%: 4.64%
- MA20 gap: 9.35% | MA50 gap: 16.52% | MA200 gap: -2.22%
- vol_ratio(Volume/Vol20): 0.19187 | gap_open: 1.02%
- RS vs SILJ gap: -2.97% / slope_proxy: 0.003559
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

## SCZM (Santacruz Silver)
- close: 9.64 | RSI14: 69.305088 | ATR14%: 5.47%
- MA20 gap: 15.04% | MA50 gap: 31.87% | MA200 gap: 11.25%
- vol_ratio(Volume/Vol20): 0.101324 | gap_open: 1.88%
- SilverMarginGate: SI=68.099998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.30% / slope_proxy: 0.003087
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
- close: 25.870001 | RSI14: 53.535569 | ATR14%: 7.39%
- MA20 gap: 4.38% | MA50 gap: 11.23% | MA200 gap: -11.69%
- vol_ratio(Volume/Vol20): 0.250305 | gap_open: 3.24%
- RS vs SILJ gap: -9.23% / slope_proxy: -0.11291
- RS vs GDXJ gap: -14.79% / slope_proxy: -0.031503
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

- 실행시간(UTC): **2026-08-25 15:01:27**
- 데이터 기준일(주가): **2026-08-25**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **True**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.69 / 4주 변화 -0.12 bp-ish / 2026-08-24
- IG OAS: 0.81 / 4주 변화 0.00 bp-ish / 2026-08-24
- 10Y Real Yield: 2.40 / 4주 변화 -0.03 bp-ish / 2026-08-21
- VIX: 15.85 / 4주 변화 -2.82 / 2026-08-24
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 16.33% / slope_proxy 23.20%
- GDXJ/GLD: gap 15.08% / slope_proxy 22.93%
- SILJ/SLV: gap 9.63% / slope_proxy 13.87%
- Gold breadth proxy: above50 100.00%, above200 92.31%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.93 | RSI14: 83.77 | ATR14%: 5.47%
- MA20/50/200 gap: 18.09% / 33.39% / 51.47%
- 5D return: 12.40% | 20D drawdown: -0.14% | vol_ratio: 0.40
- RS vs GDXJ: gap 7.03% / slope_proxy 8.78%
- FundamentalScore: 88 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **77.1**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.83 | RSI14: 84.42 | ATR14%: 4.13%
- MA20/50/200 gap: 17.13% / 33.47% / 13.05%
- 5D return: 16.17% | 20D drawdown: -0.63% | vol_ratio: 0.25
- RS vs GDXJ: gap 5.84% / slope_proxy 4.89%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **74.4**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.63 | RSI14: 77.36 | ATR14%: 4.93%
- MA20/50/200 gap: 14.03% / 26.93% / 9.87%
- 5D return: 6.54% | 20D drawdown: -1.21% | vol_ratio: 0.14
- RS vs GDXJ: gap 1.42% / slope_proxy 5.28%
- FundamentalScore: 70 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **69.0**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.65 | RSI14: 80.34 | ATR14%: 5.36%
- MA20/50/200 gap: 22.35% / 38.57% / 40.96%
- 5D return: 18.83% | 20D drawdown: 0.00% | vol_ratio: 0.64
- RS vs GDXJ: gap 11.69% / slope_proxy 4.19%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **62.2**
- Checks:
  - sector_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 26.78 | RSI14: 57.93 | ATR14%: 5.57%
- MA20/50/200 gap: 6.59% / 23.25% / 52.32%
- 5D return: 7.18% | 20D drawdown: -4.48% | vol_ratio: 0.17
- RS vs SILJ: gap 6.65% / slope_proxy 2.78%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.43 | RSI14: 64.40 | ATR14%: 5.58%
- MA20/50/200 gap: 10.59% / 17.37% / 9.15%
- 5D return: 8.86% | 20D drawdown: -2.17% | vol_ratio: 0.16
- RS vs SILJ: gap -1.23% / slope_proxy 4.05%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **56.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.88 | RSI14: 67.39 | ATR14%: 6.20%
- MA20/50/200 gap: 12.94% / 24.37% / 12.14%
- 5D return: 12.63% | 20D drawdown: -1.00% | vol_ratio: 0.34
- RS vs SILJ: gap 5.21% / slope_proxy 6.14%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **69.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.53 | RSI14: 73.00 | ATR14%: 4.88%
- MA20/50/200 gap: 16.77% / 25.89% / 9.57%
- 5D return: 14.35% | 20D drawdown: -1.41% | vol_ratio: 0.12
- RS vs SILJ: gap 6.65% / slope_proxy 6.98%
- FundamentalScore: 78 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **67.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.64 | RSI14: 72.70 | ATR14%: 5.78%
- MA20/50/200 gap: 15.04% / 31.87% / 11.25%
- 5D return: 15.17% | 20D drawdown: -1.23% | vol_ratio: 0.10
- RS vs SILJ: gap 12.30% / slope_proxy 12.67%
- FundamentalScore: 74 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **65.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.98 | RSI14: 65.49 | ATR14%: 4.50%
- MA20/50/200 gap: 9.35% / 16.52% / -2.22%
- 5D return: 11.62% | 20D drawdown: 0.00% | vol_ratio: 0.19
- RS vs SILJ: gap -2.97% / slope_proxy -5.80%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **52.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.44 | RSI14: 65.37 | ATR14%: 5.09%
- MA20/50/200 gap: 12.04% / 16.55% / -6.23%
- 5D return: 9.90% | 20D drawdown: 0.00% | vol_ratio: 0.36
- RS vs SILJ: gap -4.08% / slope_proxy 9.62%
- FundamentalScore: 68 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **45.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 25.87 | RSI14: 54.18 | ATR14%: 7.59%
- MA20/50/200 gap: 4.38% / 11.23% / -11.69%
- 5D return: 6.95% | 20D drawdown: -7.28% | vol_ratio: 0.25
- RS vs SILJ: gap -9.23% / slope_proxy -0.42%
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
