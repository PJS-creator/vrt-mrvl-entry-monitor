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

- 실행시간(UTC): **2026-08-24 22:59:10**
- 데이터 기준일(일봉): **2026-08-24**
- 데이터 기준일(주봉): **2026-08-24**
- VXN 기준일: **2026-08-21** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 706.32
- Weekly RSI14: **55.71**
- 52W MA: 642.82 / gap: **9.88%**
- 104W MA gap: **22.70%**
- 52W MA 13W slope: **6.60%**
- VXN: **21.98** / 5D change: 1.26

## Daily trigger: 실제 매수 타이밍

- QQQ close: 706.32
- Daily RSI14: **46.44**
- 20D gap: **-0.57%**
- 50D gap: **-0.96%**
- 200D gap: **8.30%**
- MACD hist: -0.8889 / change: -0.8550
- ATR14%: **1.60%**
- 20D high drawdown: **-3.52%**

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

- 데이터 기준일(주가): **2026-08-24**
- 실행시간(UTC): **2026-08-24 22:58:37**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -9.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.4 / 4주 변화 -3.0 bp
- VIX (VIXCLS): 15.13
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.107154
- MA60: 9.211904
- gap: -11.99%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.419331
- MA60: 0.402232
- gap: 4.25%
- MA60_slope_proxy: 0.018976
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-24**
- 실행시간(UTC): **2026-08-24 22:58:40**

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
- TERM_SPREAD_10Y_POLICY: 129.78 bp / 4주 변화 -4.56 bp
- CURVE_10s5s: 48.68 bp / 4주 변화 3.39 bp

## NWG Price
- close: 688.8
- MA50: 677.3409 / gap50: 1.69%
- MA200: 624.2056 / gap200: 10.35%

## Relative Strength
- RS vs FTSE gap: 1.43% / slope_proxy: 0.002946
- RS vs Peers gap: 1.32% / slope_proxy: 0.017492

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-24 22:58:46**

## Commodity Regime

- WTI ref (CL=F): 85.09 / 5D 0.70%
- Brent ref (BZ=F): 92.13 / 5D 1.39%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.04
- Gas ref (NG=F): 2.80 / 5D 4.24%

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

- close: 60.11
- MA20 / MA60 / MA200: 57.67 / 55.31 / 51.29
- gap20 / gap60: 4.22% / 8.69%
- 5D return: 1.81%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.952464
- ratio_MA60: 0.960866
- ratio_gap: -0.87%
- ratio_slope_proxy(20d): -0.012372

### Volume (if available)

- volume: 6911668.00
- volume_MA20: 8282798.40
- volume_ratio: 0.83

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.60
- MA20 / MA60 / MA200: 18.47 / 17.84 / 16.64
- gap20 / gap60: 0.73% / 4.27%
- 5D return: 1.92%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.528860
- ratio_MA60: 0.511180
- ratio_gap: 3.46%
- ratio_slope_proxy(20d): -0.005060

### Volume (if available)

- volume: 19892852.00
- volume_MA20: 16361437.60
- volume_ratio: 1.22

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

- close: 5.77
- MA20 / MA60 / MA200: 5.51 / 5.48 / 5.48
- gap20 / gap60: 4.71% / 5.29%
- 5D return: -1.70%
- 20D high/low: 6.01 / 4.95

### Relative Strength

- ratio: 0.014118
- ratio_MA60: 0.013836
- ratio_gap: 2.03%
- ratio_slope_proxy(20d): -0.000516

### Volume (if available)

- volume: 37011611.00
- volume_MA20: 44251975.55
- volume_ratio: 0.84

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

- close: 14.39
- MA20 / MA60 / MA200: 13.52 / 12.75 / 11.07
- gap20 / gap60: 6.44% / 12.82%
- 5D return: 4.65%
- 20D high/low: 14.39 / 12.17

### Relative Strength

- ratio: 0.051248
- ratio_MA60: 0.050507
- ratio_gap: 1.47%
- ratio_slope_proxy(20d): -0.000665

### Volume (if available)

- volume: 12319915.00
- volume_MA20: 13502195.75
- volume_ratio: 0.91

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-24**
- 실행시간(UTC): **2026-08-24 22:58:54**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -9.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: -3.0 bp / latest 2.4
- VIX: 15.13
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 8.30% / slope_proxy: 0.021118
- GDXJ/GLD gap: 14.71% / slope_proxy: 0.002045

## VZLA (Vizsla Silver)
- close: 3.93 | RSI14: 62.696422 | ATR14%: 4.79%
- MA20 gap: 9.03% | MA50 gap: 15.18% | MA200 gap: -3.55%
- vol_ratio(Volume/Vol20): 1.04627 | gap_open: 1.77%
- RS vs SILJ gap: -3.79% / slope_proxy: 0.003869
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
- close: 9.57 | RSI14: 68.728213 | ATR14%: 5.68%
- MA20 gap: 16.41% | MA50 gap: 31.87% | MA200 gap: 10.74%
- vol_ratio(Volume/Vol20): 0.73077 | gap_open: 1.40%
- SilverMarginGate: SI=69.18 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.36% / slope_proxy: 0.002482
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
- close: 25.74 | RSI14: 53.160546 | ATR14%: 7.58%
- MA20 gap: 5.07% | MA50 gap: 10.68% | MA200 gap: -11.85%
- vol_ratio(Volume/Vol20): 0.985225 | gap_open: 0.66%
- RS vs SILJ gap: -9.63% / slope_proxy: -0.115318
- RS vs GDXJ gap: -15.60% / slope_proxy: -0.031867
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

- 실행시간(UTC): **2026-08-24 22:59:07**
- 데이터 기준일(주가): **2026-08-24**

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

- HY OAS: 2.70 / 4주 변화 -0.09 bp-ish / 2026-08-21
- IG OAS: 0.81 / 4주 변화 0.01 bp-ish / 2026-08-21
- 10Y Real Yield: 2.40 / 4주 변화 -0.03 bp-ish / 2026-08-21
- VIX: 15.13 / 4주 변화 -3.45 / 2026-08-21
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 15.84% / slope_proxy 20.78%
- GDXJ/GLD: gap 14.71% / slope_proxy 19.48%
- SILJ/SLV: gap 8.30% / slope_proxy 10.22%
- Gold breadth proxy: above50 100.00%, above200 92.31%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.94 | RSI14: 86.50 | ATR14%: 5.73%
- MA20/50/200 gap: 20.63% / 34.67% / 52.30%
- 5D return: 11.18% | 20D drawdown: 0.00% | vol_ratio: 1.24
- RS vs GDXJ: gap 7.55% / slope_proxy 9.03%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **82.3**
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
- close: 7.86 | RSI14: 87.78 | ATR14%: 4.49%
- MA20/50/200 gap: 19.74% / 34.99% / 13.69%
- 5D return: 12.45% | 20D drawdown: -0.25% | vol_ratio: 0.58
- RS vs GDXJ: gap 6.51% / slope_proxy 7.68%
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
- close: 1.64 | RSI14: 81.97 | ATR14%: 5.20%
- MA20/50/200 gap: 16.73% / 28.37% / 10.66%
- 5D return: 2.50% | 20D drawdown: -0.61% | vol_ratio: 2.00
- RS vs GDXJ: gap 2.26% / slope_proxy 6.62%
- FundamentalScore: 70 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **74.2**
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
- close: 2.64 | RSI14: 82.44 | ATR14%: 5.57%
- MA20/50/200 gap: 24.12% / 39.51% / 40.96%
- 5D return: 14.29% | 20D drawdown: 0.00% | vol_ratio: 2.29
- RS vs GDXJ: gap 11.77% / slope_proxy 4.63%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **67.5**
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
- close: 26.58 | RSI14: 64.40 | ATR14%: 6.02%
- MA20/50/200 gap: 7.35% / 23.22% / 51.88%
- 5D return: -0.34% | 20D drawdown: -5.21% | vol_ratio: 0.95
- RS vs SILJ: gap 6.77% / slope_proxy 3.32%
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
- close: 7.36 | RSI14: 69.03 | ATR14%: 6.04%
- MA20/50/200 gap: 11.07% / 16.57% / 8.31%
- 5D return: 2.22% | 20D drawdown: -3.16% | vol_ratio: 0.64
- RS vs SILJ: gap -1.72% / slope_proxy 0.92%
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
- close: 10.76 | RSI14: 70.15 | ATR14%: 6.40%
- MA20/50/200 gap: 13.54% / 23.64% / 11.11%
- 5D return: 6.11% | 20D drawdown: -2.09% | vol_ratio: 1.25
- RS vs SILJ: gap 4.72% / slope_proxy 4.70%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
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
- close: 20.40 | RSI14: 75.85 | ATR14%: 5.20%
- MA20/50/200 gap: 18.06% / 25.93% / 9.14%
- 5D return: 8.40% | 20D drawdown: -2.02% | vol_ratio: 0.65
- RS vs SILJ: gap 6.77% / slope_proxy 5.73%
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
- close: 9.57 | RSI14: 76.99 | ATR14%: 6.17%
- MA20/50/200 gap: 16.41% / 31.87% / 10.74%
- 5D return: 9.37% | 20D drawdown: -1.95% | vol_ratio: 0.73
- RS vs SILJ: gap 12.36% / slope_proxy 11.72%
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
- close: 3.93 | RSI14: 68.79 | ATR14%: 4.76%
- MA20/50/200 gap: 9.03% / 15.18% / -3.55%
- 5D return: 7.67% | 20D drawdown: -0.76% | vol_ratio: 1.05
- RS vs SILJ: gap -3.79% / slope_proxy -7.09%
- FundamentalScore: 72 | TechnicalScore: 30 | RegimeScore: 75 | OverallScore: **57.9**
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
- close: 5.39 | RSI14: 70.66 | ATR14%: 5.51%
- MA20/50/200 gap: 12.82% / 15.56% / -6.95%
- 5D return: 4.46% | 20D drawdown: 0.00% | vol_ratio: 0.81
- RS vs SILJ: gap -4.70% / slope_proxy 4.76%
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
- close: 25.74 | RSI14: 59.09 | ATR14%: 8.07%
- MA20/50/200 gap: 5.07% / 10.68% / -11.85%
- 5D return: -2.20% | 20D drawdown: -7.74% | vol_ratio: 0.99
- RS vs SILJ: gap -9.63% / slope_proxy -3.52%
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
