# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-28 06:19:06**
- 데이터 기준일(일봉): **2026-08-27**
- 데이터 기준일(주봉): **2026-08-24**
- VXN 기준일: **2026-08-26** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 721.11
- Weekly RSI14: **59.02**
- 52W MA: 643.10 / gap: **12.13%**
- 104W MA gap: **25.23%**
- 52W MA 13W slope: **6.65%**
- VXN: **21.42** / 5D change: -0.62

## Daily trigger: 실제 매수 타이밍

- QQQ close: 721.11
- Daily RSI14: **54.78**
- 20D gap: **0.64%**
- 50D gap: **1.26%**
- 200D gap: **10.31%**
- MACD hist: -0.5877 / change: 0.6138
- ATR14%: **1.46%**
- 20D high drawdown: **-1.50%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
- daily_b: **True**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉과 일봉 조건이 과열/공포를 크게 보이지 않음

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-27**
- 실행시간(UTC): **2026-08-28 06:18:16**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.67 / 4주 변화 -20.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 -1.0 bp
- 10Y Real Yield (DFII10): 2.34 / 4주 변화 -7.0 bp
- VIX (VIXCLS): 15.21
- NFCI: -0.566

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.438734
- MA60: 9.153273
- gap: -7.81%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.421379
- MA60: 0.40443
- gap: 4.19%
- MA60_slope_proxy: 0.020816
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-27**
- 실행시간(UTC): **2026-08-28 06:18:21**

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
- TERM_SPREAD_10Y_POLICY: 124.59 bp / 4주 변화 5.5 bp
- CURVE_10s5s: 48.28 bp / 4주 변화 2.39 bp

## NWG Price
- close: 692.0
- MA50: 679.6571 / gap50: 1.82%
- MA200: 625.08 / gap200: 10.71%

## Relative Strength
- RS vs FTSE gap: 1.35% / slope_proxy: 0.002914
- RS vs Peers gap: 1.67% / slope_proxy: 0.019071

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-28 06:18:37**

## Commodity Regime

- WTI ref (CL=F): 83.00 / 5D -4.66%
- Brent ref (BZ=F): 88.11 / 5D -6.65%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.11
- Gas ref (NG=F): 2.92 / 5D 5.41%

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

- close: 59.17
- MA20 / MA60 / MA200: 58.19 / 55.34 / 51.58
- gap20 / gap60: 1.69% / 6.91%
- 5D return: -3.82%
- 20D high/low: 61.52 / 53.81

### Relative Strength

- ratio: 0.949912
- ratio_MA60: 0.957006
- ratio_gap: -0.74%
- ratio_slope_proxy(20d): -0.012986

### Volume (if available)

- volume: 6107100.00
- volume_MA20: 8052355.00
- volume_ratio: 0.76

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.25
- MA20 / MA60 / MA200: 17.92 / 17.32 / 16.26
- gap20 / gap60: 1.82% / 5.35%
- 5D return: -1.18%
- 20D high/low: 18.85 / 17.25

### Relative Strength

- ratio: 0.510347
- ratio_MA60: 0.496156
- ratio_gap: 2.86%
- ratio_slope_proxy(20d): -0.003296

### Volume (if available)

- volume: 19617300.00
- volume_MA20: 17847750.00
- volume_ratio: 1.10

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

- close: 5.74
- MA20 / MA60 / MA200: 5.61 / 5.45 / 5.50
- gap20 / gap60: 2.24% / 5.26%
- 5D return: -4.49%
- 20D high/low: 6.01 / 5.14

### Relative Strength

- ratio: 0.013833
- ratio_MA60: 0.013797
- ratio_gap: 0.26%
- ratio_slope_proxy(20d): -0.000460

### Volume (if available)

- volume: 44262600.00
- volume_MA20: 41597640.00
- volume_ratio: 1.06

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

- close: 14.48
- MA20 / MA60 / MA200: 13.74 / 12.85 / 11.16
- gap20 / gap60: 5.39% / 12.67%
- 5D return: 1.33%
- 20D high/low: 14.48 / 12.43

### Relative Strength

- ratio: 0.051567
- ratio_MA60: 0.050351
- ratio_gap: 2.41%
- ratio_slope_proxy(20d): -0.000888

### Volume (if available)

- volume: 11855200.00
- volume_MA20: 13566250.00
- volume_ratio: 0.87

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

- 데이터 기준일(주가): **2026-08-28**
- 실행시간(UTC): **2026-08-28 06:18:52**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -20.0 bp / latest 2.67
- IG OAS 4주 변화: -1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: -7.0 bp / latest 2.34
- VIX: 15.21
- NFCI: -0.566

### Leadership ratios
- SILJ/SLV gap: 10.33% / slope_proxy: 0.023351
- GDXJ/GLD gap: 16.12% / slope_proxy: 0.004447

## VZLA (Vizsla Silver)
- close: 4.16 | RSI14: 68.258398 | ATR14%: 4.42%
- MA20 gap: 11.29% | MA50 gap: 21.01% | MA200 gap: 2.01%
- vol_ratio(Volume/Vol20): 1.265354 | gap_open: 0.75%
- RS vs SILJ gap: -1.46% / slope_proxy: 0.002838
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
- close: 10.02 | RSI14: 70.944936 | ATR14%: 5.31%
- MA20 gap: 14.98% | MA50 gap: 35.49% | MA200 gap: 15.01%
- vol_ratio(Volume/Vol20): 0.83007 | gap_open: 0.21%
- SilverMarginGate: SI=69.724998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 12.86% / slope_proxy: 0.004378
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
- close: 25.959999 | RSI14: 53.589599 | ATR14%: 7.29%
- MA20 gap: 2.18% | MA50 gap: 11.88% | MA200 gap: -11.93%
- vol_ratio(Volume/Vol20): 0.93497 | gap_open: 0.67%
- RS vs SILJ gap: -10.57% / slope_proxy: -0.106953
- RS vs GDXJ gap: -13.90% / slope_proxy: -0.030572
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

- 실행시간(UTC): **2026-08-28 06:19:04**
- 데이터 기준일(주가): **2026-08-27**

## Verdict
**🟡 Precious miners watch/add-on candidates: ASM**

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

- HY OAS: 2.67 / 4주 변화 -0.20 bp-ish / 2026-08-26
- IG OAS: 0.80 / 4주 변화 -0.01 bp-ish / 2026-08-26
- 10Y Real Yield: 2.34 / 4주 변화 -0.07 bp-ish / 2026-08-26
- VIX: 15.21 / 4주 변화 -5.45 / 2026-08-26
- NFCI: -0.57 / 4주 변화 -0.10 / 2026-08-21

### Leadership ratios

- GDX/GLD: gap 16.24% / slope_proxy 23.03%
- GDXJ/GLD: gap 16.12% / slope_proxy 24.23%
- SILJ/SLV: gap 10.33% / slope_proxy 14.82%
- Gold breadth proxy: above50 100.00%, above200 92.31%, count 13
- Silver breadth proxy: above50 100.00%, above200 76.92%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.92 | RSI14: 73.31 | ATR14%: 4.73%
- MA20/50/200 gap: 13.48% / 31.52% / 50.18%
- 5D return: 4.00% | 20D drawdown: -1.36% | vol_ratio: 0.37
- RS vs GDXJ: gap 5.83% / slope_proxy 8.85%
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
- close: 8.17 | RSI14: 84.43 | ATR14%: 4.00%
- MA20/50/200 gap: 17.53% / 37.39% / 17.56%
- 5D return: 9.52% | 20D drawdown: 0.00% | vol_ratio: 0.63
- RS vs GDXJ: gap 9.48% / slope_proxy 9.15%
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
- close: 1.61 | RSI14: 66.67 | ATR14%: 4.77%
- MA20/50/200 gap: 9.12% / 24.73% / 8.39%
- 5D return: -2.42% | 20D drawdown: -2.42% | vol_ratio: 0.33
- RS vs GDXJ: gap -0.59% / slope_proxy 0.25%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **65.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.69 | RSI14: 73.17 | ATR14%: 5.15%
- MA20/50/200 gap: 19.42% / 37.91% / 42.19%
- 5D return: 9.35% | 20D drawdown: -0.74% | vol_ratio: 0.44
- RS vs GDXJ: gap 11.79% / slope_proxy 4.58%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.73 | RSI14: 64.12 | ATR14%: 5.23%
- MA20/50/200 gap: 11.19% / 21.41% / 12.90%
- 5D return: 1.71% | 20D drawdown: 0.00% | vol_ratio: 0.88
- RS vs SILJ: gap -0.23% / slope_proxy 5.36%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 29.29 | RSI14: 59.37 | ATR14%: 5.38%
- MA20/50/200 gap: 12.47% / 32.79% / 64.79%
- 5D return: 8.80% | 20D drawdown: 0.00% | vol_ratio: 1.87
- RS vs SILJ: gap 12.28% / slope_proxy 8.29%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.16 | RSI14: 67.21 | ATR14%: 4.24%
- MA20/50/200 gap: 11.29% / 21.01% / 2.01%
- 5D return: 7.49% | 20D drawdown: 0.00% | vol_ratio: 1.27
- RS vs SILJ: gap -1.46% / slope_proxy -3.75%
- FundamentalScore: 72 | TechnicalScore: 75 | RegimeScore: 75 | OverallScore: **73.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **True**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, RelativeStrength(vs SILJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.30 | RSI14: 66.00 | ATR14%: 5.94%
- MA20/50/200 gap: 13.15% / 28.00% / 16.00%
- 5D return: 3.01% | 20D drawdown: 0.00% | vol_ratio: 0.86
- RS vs SILJ: gap 5.85% / slope_proxy 9.16%
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
- close: 21.43 | RSI14: 77.46 | ATR14%: 4.63%
- MA20/50/200 gap: 17.42% / 29.98% / 13.94%
- 5D return: 2.93% | 20D drawdown: 0.00% | vol_ratio: 0.89
- RS vs SILJ: gap 7.67% / slope_proxy 10.26%
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
- close: 10.02 | RSI14: 70.66 | ATR14%: 5.52%
- MA20/50/200 gap: 14.98% / 35.49% / 15.01%
- 5D return: 2.66% | 20D drawdown: 0.00% | vol_ratio: 0.83
- RS vs SILJ: gap 12.86% / slope_proxy 12.68%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.74 | RSI14: 68.53 | ATR14%: 4.99%
- MA20/50/200 gap: 13.66% / 23.06% / -1.39%
- 5D return: 9.33% | 20D drawdown: 0.00% | vol_ratio: 0.99
- RS vs SILJ: gap -1.16% / slope_proxy 9.16%
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
- close: 25.96 | RSI14: 48.00 | ATR14%: 7.30%
- MA20/50/200 gap: 2.18% / 11.88% / -11.93%
- 5D return: -0.69% | 20D drawdown: -6.95% | vol_ratio: 0.93
- RS vs SILJ: gap -10.57% / slope_proxy -3.43%
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
