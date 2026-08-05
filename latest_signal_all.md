# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-05 15:01:35**
- 데이터 기준일(일봉): **2026-08-05**
- 데이터 기준일(주봉): **2026-08-03**
- VXN 기준일: **2026-08-04** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 722.96
- Weekly RSI14: **60.93**
- 52W MA: 634.37 / gap: **13.96%**
- 104W MA gap: **27.15%**
- 52W MA 13W slope: **7.32%**
- VXN: **25.48** / 5D change: -3.13

## Daily trigger: 실제 매수 타이밍

- QQQ close: 722.96
- Daily RSI14: **57.68**
- 20D gap: **3.11%**
- 50D gap: **1.14%**
- 200D gap: **11.98%**
- MACD hist: 3.5635 / change: 1.6206
- ATR14%: **2.13%**
- 20D high drawdown: **-0.35%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **True**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-05 15:00:54**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.43 / 4주 변화 19.0 bp
- VIX (VIXCLS): 16.5
- NFCI: -0.529

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.974924
- MA60: 9.495749
- gap: -5.48%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.375136
- MA60: 0.387361
- gap: -3.16%
- MA60_slope_proxy: 0.014117
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-05 15:00:58**

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
- TERM_SPREAD_10Y_POLICY: 118.82 bp / 4주 변화 16.88 bp
- CURVE_10s5s: 47.26 bp / 4주 변화 -1.69 bp

## NWG Price
- close: 714.6
- MA50: 650.512 / gap50: 9.85%
- MA200: 616.1859 / gap200: 15.97%

## Relative Strength
- RS vs FTSE gap: 8.00% / slope_proxy: 0.002324
- RS vs Peers gap: 5.36% / slope_proxy: 0.000468

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-05 15:01:10**

## Commodity Regime

- WTI ref (CL=F): 75.06 / 5D -11.13%
- Brent ref (BZ=F): 78.89 / 5D -13.06%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.83
- Gas ref (NG=F): 2.67 / 5D -2.02%

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

- close: 53.99
- MA20 / MA60 / MA200: 55.17 / 55.03 / 50.11
- gap20 / gap60: -2.14% / -1.88%
- 5D return: -3.64%
- 20D high/low: 57.60 / 52.30

### Relative Strength

- ratio: 0.940429
- ratio_MA60: 0.968198
- ratio_gap: -2.87%
- ratio_slope_proxy(20d): -0.016034

### Volume (if available)

- volume: 1950254.00
- volume_MA20: 8050802.70
- volume_ratio: 0.24

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.53
- MA20 / MA60 / MA200: 18.32 / 18.15 / 16.21
- gap20 / gap60: 1.17% / 2.08%
- 5D return: -0.32%
- 20D high/low: 19.40 / 17.03

### Relative Strength

- ratio: 0.509069
- ratio_MA60: 0.513428
- ratio_gap: -0.85%
- ratio_slope_proxy(20d): -0.005725

### Volume (if available)

- volume: 3566651.00
- volume_MA20: 13989827.55
- volume_ratio: 0.25

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.12
- MA20 / MA60 / MA200: 5.19 / 5.72 / 5.34
- gap20 / gap60: -1.37% / -10.43%
- 5D return: 3.43%
- 20D high/low: 5.37 / 4.95

### Relative Strength

- ratio: 0.013268
- ratio_MA60: 0.014179
- ratio_gap: -6.42%
- ratio_slope_proxy(20d): -0.000461

### Volume (if available)

- volume: 6196550.00
- volume_MA20: 40949692.50
- volume_ratio: 0.15

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

- close: 12.39
- MA20 / MA60 / MA200: 13.32 / 12.63 / 10.75
- gap20 / gap60: -6.96% / -1.94%
- 5D return: -5.06%
- 20D high/low: 15.16 / 12.17

### Relative Strength

- ratio: 0.048591
- ratio_MA60: 0.051303
- ratio_gap: -5.29%
- ratio_slope_proxy(20d): 0.001121

### Volume (if available)

- volume: 2847904.00
- volume_MA20: 15337640.20
- volume_ratio: 0.19

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

- 데이터 기준일(주가): **2026-08-05**
- 실행시간(UTC): **2026-08-05 15:01:21**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 6.0 bp / latest 2.78
- IG OAS 4주 변화: 3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.43
- VIX: 16.5
- NFCI: -0.529

### Leadership ratios
- SILJ/SLV gap: 7.57% / slope_proxy: 0.009638
- GDXJ/GLD gap: 3.83% / slope_proxy: -0.007859

## VZLA (Vizsla Silver)
- close: 3.58 | RSI14: 60.373675 | ATR14%: 5.44%
- MA20 gap: 11.01% | MA50 gap: 5.84% | MA200 gap: -12.66%
- vol_ratio(Volume/Vol20): 0.624445 | gap_open: 5.00%
- RS vs SILJ gap: 2.55% / slope_proxy: 0.006073
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
- close: 7.79 | RSI14: 64.907165 | ATR14%: 6.15%
- MA20 gap: 19.61% | MA50 gap: 14.11% | MA200 gap: -7.62%
- vol_ratio(Volume/Vol20): 0.541913 | gap_open: 7.29%
- SilverMarginGate: SI=62.535 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 6.70% / slope_proxy: -0.0054
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

## HYMC (Hycroft Mining)
- close: 24.450001 | RSI14: 59.082522 | ATR14%: 7.39%
- MA20 gap: 18.56% | MA50 gap: 1.41% | MA200 gap: -12.62%
- vol_ratio(Volume/Vol20): 0.826719 | gap_open: 7.71%
- RS vs SILJ gap: -7.87% / slope_proxy: -0.145693
- RS vs GDXJ gap: -9.39% / slope_proxy: -0.035034
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

- 실행시간(UTC): **2026-08-05 15:01:34**
- 데이터 기준일(주가): **2026-08-05**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO**

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

- HY OAS: 2.78 / 4주 변화 0.06 bp-ish / 2026-08-03
- IG OAS: 0.78 / 4주 변화 0.03 bp-ish / 2026-08-03
- 10Y Real Yield: 2.43 / 4주 변화 0.19 bp-ish / 2026-08-03
- VIX: 16.50 / 4주 변화 0.37 / 2026-08-04
- NFCI: -0.53 / 4주 변화 -0.06 / 2026-07-31

### Leadership ratios

- GDX/GLD: gap 3.94% / slope_proxy 6.88%
- GDXJ/GLD: gap 3.83% / slope_proxy 6.81%
- SILJ/SLV: gap 7.57% / slope_proxy 4.34%
- Gold breadth proxy: above50 92.31%, above200 30.77%, count 13
- Silver breadth proxy: above50 92.31%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.96 | RSI14: 69.77 | ATR14%: 4.76%
- MA20/50/200 gap: 9.48% / 4.67% / 15.59%
- 5D return: 11.64% | 20D drawdown: 0.00% | vol_ratio: 0.44
- RS vs GDXJ: gap -0.72% / slope_proxy -6.83%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **68.6**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.27 | RSI14: 78.85 | ATR14%: 5.46%
- MA20/50/200 gap: 18.69% / 12.36% / -8.26%
- 5D return: 16.11% | 20D drawdown: 0.00% | vol_ratio: 1.06
- RS vs GDXJ: gap 5.27% / slope_proxy 6.57%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **65.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.87 | RSI14: 48.35 | ATR14%: 6.11%
- MA20/50/200 gap: -0.29% / 5.94% / 3.25%
- 5D return: 1.63% | 20D drawdown: -9.22% | vol_ratio: 0.37
- RS vs GDXJ: gap -1.28% / slope_proxy -7.34%
- FundamentalScore: 55 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **60.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.35 | RSI14: 71.19 | ATR14%: 5.37%
- MA20/50/200 gap: 19.15% / 10.86% / -8.50%
- 5D return: 20.54% | 20D drawdown: 0.00% | vol_ratio: 0.75
- RS vs GDXJ: gap 4.55% / slope_proxy 4.78%
- FundamentalScore: 70 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **55.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 24.73 | RSI14: 72.28 | ATR14%: 5.87%
- MA20/50/200 gap: 22.99% / 26.93% / 50.20%
- 5D return: 28.67% | 20D drawdown: 0.00% | vol_ratio: 0.63
- RS vs SILJ: gap 23.97% / slope_proxy 14.60%
- FundamentalScore: 86 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **71.2**
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
- close: 3.58 | RSI14: 67.35 | ATR14%: 5.25%
- MA20/50/200 gap: 11.01% / 5.84% / -12.66%
- 5D return: 14.74% | 20D drawdown: 0.00% | vol_ratio: 0.63
- RS vs SILJ: gap 2.53% / slope_proxy 4.32%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **61.4**
- Checks:
  - sector_ok: **False**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.95 | RSI14: 68.62 | ATR14%: 5.54%
- MA20/50/200 gap: 12.99% / 7.25% / -6.27%
- 5D return: 18.39% | 20D drawdown: 0.00% | vol_ratio: 0.43
- RS vs SILJ: gap 1.60% / slope_proxy 0.01%
- FundamentalScore: 82 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **60.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.79 | RSI14: 74.01 | ATR14%: 6.00%
- MA20/50/200 gap: 19.61% / 14.11% / -7.62%
- 5D return: 23.45% | 20D drawdown: 0.00% | vol_ratio: 0.54
- RS vs SILJ: gap 6.68% / slope_proxy 7.54%
- FundamentalScore: 74 | TechnicalScore: 25 | RegimeScore: 75 | OverallScore: **57.1**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 16.61 | RSI14: 64.24 | ATR14%: 5.24%
- MA20/50/200 gap: 10.12% / 6.43% / -9.33%
- 5D return: 17.42% | 20D drawdown: 0.00% | vol_ratio: 0.24
- RS vs SILJ: gap 1.12% / slope_proxy -3.11%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **55.4**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.79 | RSI14: 70.43 | ATR14%: 6.32%
- MA20/50/200 gap: 17.85% / 0.33% / -16.30%
- 5D return: 30.87% | 20D drawdown: 0.00% | vol_ratio: 0.68
- RS vs SILJ: gap -6.12% / slope_proxy -1.11%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.48 | RSI14: 63.91 | ATR14%: 6.07%
- MA20/50/200 gap: 12.42% / 5.16% / -2.60%
- 5D return: 22.98% | 20D drawdown: 0.00% | vol_ratio: 0.89
- RS vs SILJ: gap 0.37% / slope_proxy -2.96%
- FundamentalScore: 60 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **42.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 24.45 | RSI14: 72.83 | ATR14%: 6.56%
- MA20/50/200 gap: 18.56% / 1.41% / -12.62%
- 5D return: 27.61% | 20D drawdown: 0.00% | vol_ratio: 0.83
- RS vs SILJ: gap -7.88% / slope_proxy 3.27%
- FundamentalScore: 42 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **33.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
