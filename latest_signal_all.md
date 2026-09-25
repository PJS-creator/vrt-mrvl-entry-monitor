# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-25 15:01:14**
- 데이터 기준일(일봉): **2026-09-25**
- 데이터 기준일(주봉): **2026-09-21**
- VXN 기준일: **2026-09-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 743.02
- Weekly RSI14: **63.61**
- 52W MA: 652.94 / gap: **13.80%**
- 104W MA gap: **27.01%**
- 52W MA 13W slope: **5.85%**
- VXN: **20.18** / 5D change: -2.08

## Daily trigger: 실제 매수 타이밍

- QQQ close: 742.98
- Daily RSI14: **64.27**
- 20D gap: **3.16%**
- 50D gap: **4.36%**
- 200D gap: **11.87%**
- MACD hist: 3.4433 / change: -0.1134
- ATR14%: **1.28%**
- 20D high drawdown: **-0.60%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-09-25**
- 실행시간(UTC): **2026-09-25 15:00:52**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.8 / 4주 변화 17.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.76 / 4주 변화 42.0 bp
- VIX (VIXCLS): 14.21
- NFCI: -0.555

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.663941
- MA60: 8.969703
- gap: -3.41%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.430665
- MA60: 0.388106
- gap: 10.97%
- MA60_slope_proxy: -0.016325
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-25**
- 실행시간(UTC): **2026-09-25 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 154.1 bp / 4주 변화 27.89 bp
- CURVE_10s5s: 41.25 bp / 4주 변화 -7.06 bp

## NWG Price
- close: 691.42
- MA50: 692.4282 / gap50: -0.15%
- MA200: 633.6323 / gap200: 9.12%

## Relative Strength
- RS vs FTSE gap: 0.97% / slope_proxy: 0.001246
- RS vs Peers gap: 2.91% / slope_proxy: 0.008661

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-25 15:01:01**

## Commodity Regime

- WTI ref (CL=F): 93.92 / 5D -6.36%
- Brent ref (BZ=F): 99.34 / 5D -4.36%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.42
- Gas ref (NG=F): 3.17 / 5D 8.86%

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

- close: 57.20
- MA20 / MA60 / MA200: 59.66 / 57.19 / 53.20
- gap20 / gap60: -4.11% / 0.02%
- 5D return: -2.78%
- 20D high/low: 63.52 / 56.31

### Relative Strength

- ratio: 0.921941
- ratio_MA60: 0.947598
- ratio_gap: -2.71%
- ratio_slope_proxy(20d): -0.010699

### Volume (if available)

- volume: 1314637.00
- volume_MA20: 8174186.85
- volume_ratio: 0.16

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.40
- MA20 / MA60 / MA200: 20.67 / 18.64 / 17.10
- gap20 / gap60: -1.30% / 9.43%
- 5D return: -1.92%
- 20D high/low: 21.77 / 18.53

### Relative Strength

- ratio: 0.556921
- ratio_MA60: 0.516555
- ratio_gap: 7.81%
- ratio_slope_proxy(20d): 0.020400

### Volume (if available)

- volume: 4765504.00
- volume_MA20: 21785175.20
- volume_ratio: 0.22

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.37
- MA20 / MA60 / MA200: 5.70 / 5.49 / 5.65
- gap20 / gap60: -5.76% / -2.22%
- 5D return: -4.79%
- 20D high/low: 6.22 / 5.37

### Relative Strength

- ratio: 0.013636
- ratio_MA60: 0.013765
- ratio_gap: -0.94%
- ratio_slope_proxy(20d): -0.000032

### Volume (if available)

- volume: 4627140.00
- volume_MA20: 42202307.00
- volume_ratio: 0.11

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

- close: 13.02
- MA20 / MA60 / MA200: 14.41 / 13.70 / 11.84
- gap20 / gap60: -9.68% / -5.02%
- 5D return: -7.17%
- 20D high/low: 15.76 / 12.91

### Relative Strength

- ratio: 0.047955
- ratio_MA60: 0.050891
- ratio_gap: -5.77%
- ratio_slope_proxy(20d): 0.000672

### Volume (if available)

- volume: 3038346.00
- volume_MA20: 14309627.30
- volume_ratio: 0.21

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

- 데이터 기준일(주가): **2026-09-25**
- 실행시간(UTC): **2026-09-25 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 17.0 bp / latest 2.8
- IG OAS 4주 변화: 0.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 42.0 bp / latest 2.76
- VIX: 14.21
- NFCI: -0.555

### Leadership ratios
- SILJ/SLV gap: 0.67% / slope_proxy: 0.019031
- GDXJ/GLD gap: 6.01% / slope_proxy: 0.014762

## VZLA (Vizsla Silver)
- close: 3.935 | RSI14: 50.201708 | ATR14%: 5.26%
- MA20 gap: -1.61% | MA50 gap: 5.17% | MA200 gap: -1.98%
- vol_ratio(Volume/Vol20): 0.346848 | gap_open: 0.76%
- RS vs SILJ gap: 5.34% / slope_proxy: 0.001228
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
- close: 9.07 | RSI14: 49.642352 | ATR14%: 6.63%
- MA20 gap: -3.60% | MA50 gap: 6.41% | MA200 gap: 0.67%
- vol_ratio(Volume/Vol20): 0.121299 | gap_open: 1.01%
- SilverMarginGate: SI=64.580002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 9.01% / slope_proxy: 0.018592
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
- close: 21.2901 | RSI14: 45.395145 | ATR14%: 7.42%
- MA20 gap: -2.63% | MA50 gap: -7.12% | MA200 gap: -30.50%
- vol_ratio(Volume/Vol20): 0.177706 | gap_open: 0.05%
- RS vs SILJ gap: -8.69% / slope_proxy: -0.073035
- RS vs GDXJ gap: -11.84% / slope_proxy: -0.023091
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

- 실행시간(UTC): **2026-09-25 15:01:13**
- 데이터 기준일(주가): **2026-09-25**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.80 / 4주 변화 0.17 bp-ish / 2026-09-24
- IG OAS: 0.79 / 4주 변화 0.00 bp-ish / 2026-09-24
- 10Y Real Yield: 2.76 / 4주 변화 0.44 bp-ish / 2026-09-23
- VIX: 14.21 / 4주 변화 -1.24 / 2026-09-22
- NFCI: -0.56 / 4주 변화 -0.05 / 2026-09-18

### Leadership ratios

- GDX/GLD: gap 5.91% / slope_proxy -3.26%
- GDXJ/GLD: gap 6.01% / slope_proxy -2.60%
- SILJ/SLV: gap 0.68% / slope_proxy -5.12%
- Gold breadth proxy: above50 76.92%, above200 69.23%, count 13
- Silver breadth proxy: above50 61.54%, above200 23.08%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.16 | RSI14: 49.64 | ATR14%: 4.30%
- MA20/50/200 gap: 0.27% / 8.89% / 31.14%
- 5D return: -3.61% | 20D drawdown: -3.61% | vol_ratio: 0.08
- RS vs GDXJ: gap 6.86% / slope_proxy 6.67%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **79.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.52 | RSI14: 40.33 | ATR14%: 5.00%
- MA20/50/200 gap: -3.39% / 8.40% / 6.13%
- 5D return: -2.08% | 20D drawdown: -9.83% | vol_ratio: 0.02
- RS vs GDXJ: gap 7.61% / slope_proxy 4.21%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **60.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.57 | RSI14: 43.53 | ATR14%: 5.64%
- MA20/50/200 gap: -2.24% / 10.59% / 29.57%
- 5D return: -1.53% | 20D drawdown: -7.89% | vol_ratio: 0.33
- RS vs GDXJ: gap 8.85% / slope_proxy 3.37%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **64.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.26 | RSI14: 29.37 | ATR14%: 7.26%
- MA20/50/200 gap: -12.77% / -9.00% / -15.28%
- 5D return: -16.78% | 20D drawdown: -20.94% | vol_ratio: 0.34
- RS vs GDXJ: gap -11.38% / slope_proxy -12.12%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **46.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 28.50 | RSI14: 48.23 | ATR14%: 5.64%
- MA20/50/200 gap: 0.69% / 11.01% / 46.50%
- 5D return: 0.14% | 20D drawdown: -6.19% | vol_ratio: 0.17
- RS vs SILJ: gap 13.39% / slope_proxy 11.19%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 50 | OverallScore: **78.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.07 | RSI14: 42.38 | ATR14%: 6.81%
- MA20/50/200 gap: -3.60% / 6.41% / 0.67%
- 5D return: -4.83% | 20D drawdown: -13.04% | vol_ratio: 0.12
- RS vs SILJ: gap 9.01% / slope_proxy 3.96%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **57.3**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.94 | RSI14: 47.95 | ATR14%: 5.36%
- MA20/50/200 gap: -1.50% / 5.28% / -1.87%
- 5D return: -3.45% | 20D drawdown: -8.39% | vol_ratio: 0.35
- RS vs SILJ: gap 5.46% / slope_proxy 7.46%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 50 | OverallScore: **56.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.28 | RSI14: 28.40 | ATR14%: 6.07%
- MA20/50/200 gap: -9.91% / -4.12% / -6.76%
- 5D return: -9.11% | 20D drawdown: -19.09% | vol_ratio: 0.17
- RS vs SILJ: gap -3.45% / slope_proxy -5.89%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **52.1**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 18.15 | RSI14: 31.96 | ATR14%: 5.15%
- MA20/50/200 gap: -6.53% / 0.57% / -5.56%
- 5D return: -4.10% | 20D drawdown: -14.45% | vol_ratio: 0.09
- RS vs SILJ: gap 0.62% / slope_proxy -2.85%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **50.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.74 | RSI14: 38.55 | ATR14%: 6.41%
- MA20/50/200 gap: -6.72% / -2.03% / -19.73%
- 5D return: -8.40% | 20D drawdown: -14.35% | vol_ratio: 0.40
- RS vs SILJ: gap -2.51% / slope_proxy -4.82%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **45.9**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.88 | RSI14: 25.91 | ATR14%: 6.22%
- MA20/50/200 gap: -12.29% / -10.86% / -16.23%
- 5D return: -7.84% | 20D drawdown: -23.54% | vol_ratio: 0.27
- RS vs SILJ: gap -11.83% / slope_proxy -14.11%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **42.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.29 | RSI14: 43.19 | ATR14%: 6.72%
- MA20/50/200 gap: -2.63% / -7.12% / -30.50%
- 5D return: -0.51% | 20D drawdown: -10.64% | vol_ratio: 0.18
- RS vs SILJ: gap -8.69% / slope_proxy -2.49%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 50 | OverallScore: **34.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
