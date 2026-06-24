# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-24 15:01:11**
- 데이터 기준일(일봉): **2026-06-24**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-23** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 719.63
- Weekly RSI14: **64.55**
- 52W MA: 617.69 / gap: **16.50%**
- 104W MA gap: **29.68%**
- 52W MA 13W slope: **8.52%**
- VXN: **32.37** / 5D change: 6.45

## Daily trigger: 실제 매수 타이밍

- QQQ close: 719.63
- Daily RSI14: **51.12**
- 20D gap: **-0.96%**
- 50D gap: **2.93%**
- 200D gap: **14.34%**
- MACD hist: -2.6417 / change: -0.3724
- ATR14%: **2.18%**
- 20D high drawdown: **-3.45%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-24 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -1.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 0.0 bp
- 10Y Real Yield (DFII10): 2.28 / 4주 변화 12.0 bp
- VIX (VIXCLS): 19.49
- NFCI: -0.516

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.706953
- MA60: 9.242373
- gap: 5.03%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.440742
- MA60: 0.350134
- gap: 25.88%
- MA60_slope_proxy: 0.070918
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-24 15:00:48**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **True**
- MacroGreen: **True**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 103.3 bp / 4주 변화 -8.36 bp
- CURVE_10s5s: 45.6 bp / 4주 변화 0.94 bp

## NWG Price
- close: 649.2
- MA50: 595.8691 / gap50: 8.95%
- MA200: 594.4484 / gap200: 9.21%

## Relative Strength
- RS vs FTSE gap: 8.73% / slope_proxy: 0.001278
- RS vs Peers gap: 1.09% / slope_proxy: -0.016556

## Why not today?
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-24 15:00:55**

## Commodity Regime

- WTI ref (CL=F): 69.85 / 5D -8.15%
- Brent ref (BZ=F): 73.47 / 5D -6.95%
- Brent Tier: **70-80**
- Brent-WTI spread: 3.62
- Gas ref (NG=F): 3.23 / 5D -0.34%

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

- close: 50.73
- MA20 / MA60 / MA200: 55.63 / 57.32 / 48.83
- gap20 / gap60: -8.80% / -11.49%
- 5D return: -5.47%
- 20D high/low: 59.37 / 50.73

### Relative Strength

- ratio: 0.953081
- ratio_MA60: 1.002242
- ratio_gap: -4.91%
- ratio_slope_proxy(20d): -0.002251

### Volume (if available)

- volume: 2604244.00
- volume_MA20: 9984257.20
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.42
- MA20 / MA60 / MA200: 17.81 / 19.64 / 15.43
- gap20 / gap60: -7.78% / -16.40%
- 5D return: -3.69%
- 20D high/low: 18.82 / 16.42

### Relative Strength

- ratio: 0.487240
- ratio_MA60: 0.527276
- ratio_gap: -7.59%
- ratio_slope_proxy(20d): 0.002739

### Volume (if available)

- volume: 3299588.00
- volume_MA20: 14637459.40
- volume_ratio: 0.23

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.05
- MA20 / MA60 / MA200: 5.88 / 6.34 / 5.08
- gap20 / gap60: -14.15% / -20.37%
- 5D return: -9.66%
- 20D high/low: 6.25 / 5.05

### Relative Strength

- ratio: 0.013681
- ratio_MA60: 0.015044
- ratio_gap: -9.06%
- ratio_slope_proxy(20d): -0.000732

### Volume (if available)

- volume: 9736732.00
- volume_MA20: 28832406.60
- volume_ratio: 0.34

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

- close: 10.82
- MA20 / MA60 / MA200: 12.14 / 12.88 / 10.80
- gap20 / gap60: -10.89% / -15.97%
- 5D return: -2.43%
- 20D high/low: 13.27 / 10.82

### Relative Strength

- ratio: 0.047068
- ratio_MA60: 0.051379
- ratio_gap: -8.39%
- ratio_slope_proxy(20d): 0.000111

### Volume (if available)

- volume: 2133771.00
- volume_MA20: 13541683.55
- volume_ratio: 0.16

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

- 데이터 기준일(주가): **2026-06-24**
- 실행시간(UTC): **2026-06-24 15:01:02**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.71
- IG OAS 4주 변화: 0.0 bp / latest 0.74
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.28
- VIX: 19.49
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 6.01% / slope_proxy: 0.001466
- GDXJ/GLD gap: -5.40% / slope_proxy: -0.002518

## VZLA (Vizsla Silver)
- close: 3.1901 | RSI14: 39.409174 | ATR14%: 7.05%
- MA20 gap: -11.48% | MA50 gap: -9.53% | MA200 gap: -24.87%
- vol_ratio(Volume/Vol20): 0.330858 | gap_open: 2.99%
- RS vs SILJ gap: 8.60% / slope_proxy: 0.00455
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
- close: 6.365 | RSI14: 37.998402 | ATR14%: 9.27%
- MA20 gap: -11.79% | MA50 gap: -21.19% | MA200 gap: -25.22%
- vol_ratio(Volume/Vol20): 0.286463 | gap_open: 5.29%
- SilverMarginGate: SI=59.035 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.99% / slope_proxy: -0.009902
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
- close: 21.719999 | RSI14: 31.027714 | ATR14%: 11.34%
- MA20 gap: -21.70% | MA50 gap: -36.20% | MA200 gap: -15.98%
- vol_ratio(Volume/Vol20): 0.383045 | gap_open: 5.10%
- RS vs SILJ gap: -24.40% / slope_proxy: -0.079377
- RS vs GDXJ gap: -23.57% / slope_proxy: -0.017301
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

- 실행시간(UTC): **2026-06-24 15:01:10**
- 데이터 기준일(주가): **2026-06-24**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.71 / 4주 변화 0.00 bp-ish / 2026-06-23
- IG OAS: 0.74 / 4주 변화 0.00 bp-ish / 2026-06-23
- 10Y Real Yield: 2.28 / 4주 변화 0.10 bp-ish / 2026-06-22
- VIX: 19.49 / 4주 변화 2.48 / 2026-06-23
- NFCI: -0.52 / 4주 변화 0.05 / 2026-06-19

### Leadership ratios

- GDX/GLD: gap -4.30% / slope_proxy -2.38%
- GDXJ/GLD: gap -5.41% / slope_proxy -3.87%
- SILJ/SLV: gap 5.97% / slope_proxy 8.64%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.33 | RSI14: 39.37 | ATR14%: 6.85%
- MA20/50/200 gap: -7.54% / -7.68% / 10.98%
- 5D return: -12.63% | 20D drawdown: -15.75% | vol_ratio: 0.47
- RS vs GDXJ: gap 13.63% / slope_proxy 1.50%
- FundamentalScore: 88 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **59.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.21 | RSI14: 42.77 | ATR14%: 7.94%
- MA20/50/200 gap: -7.33% / -11.13% / -19.69%
- 5D return: -13.93% | 20D drawdown: -18.03% | vol_ratio: 0.35
- RS vs GDXJ: gap 4.75% / slope_proxy 5.55%
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
- close: 5.07 | RSI14: 30.79 | ATR14%: 7.64%
- MA20/50/200 gap: -14.23% / -21.31% / -26.95%
- 5D return: -14.07% | 20D drawdown: -28.09% | vol_ratio: 0.61
- RS vs GDXJ: gap -7.36% / slope_proxy -6.06%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.53 | RSI14: 29.07 | ATR14%: 6.82%
- MA20/50/200 gap: -10.58% / -16.96% / -8.60%
- 5D return: -7.27% | 20D drawdown: -22.34% | vol_ratio: 0.23
- RS vs GDXJ: gap 0.72% / slope_proxy -5.40%
- FundamentalScore: 55 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **36.0**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 17.00 | RSI14: 40.06 | ATR14%: 8.61%
- MA20/50/200 gap: -10.71% / -8.30% / 11.33%
- 5D return: -19.24% | 20D drawdown: -20.89% | vol_ratio: 0.36
- RS vs SILJ: gap 11.37% / slope_proxy 5.98%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **63.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.19 | RSI14: 31.58 | ATR14%: 7.21%
- MA20/50/200 gap: -11.35% / -9.40% / -24.76%
- 5D return: -13.41% | 20D drawdown: -22.64% | vol_ratio: 0.33
- RS vs SILJ: gap 8.77% / slope_proxy 3.00%
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
- close: 7.71 | RSI14: 36.68 | ATR14%: 7.89%
- MA20/50/200 gap: -11.99% / -17.51% / -18.52%
- 5D return: -17.10% | 20D drawdown: -22.67% | vol_ratio: 0.32
- RS vs SILJ: gap -1.95% / slope_proxy -3.45%
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
- close: 14.64 | RSI14: 37.21 | ATR14%: 6.85%
- MA20/50/200 gap: -8.74% / -16.21% / -17.97%
- 5D return: -12.47% | 20D drawdown: -17.78% | vol_ratio: 0.26
- RS vs SILJ: gap -1.63% / slope_proxy 0.83%
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
- close: 6.36 | RSI14: 39.66 | ATR14%: 9.40%
- MA20/50/200 gap: -11.79% / -21.19% / -25.22%
- 5D return: -20.14% | 20D drawdown: -23.59% | vol_ratio: 0.29
- RS vs SILJ: gap -5.99% / slope_proxy -4.64%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.61 | RSI14: 33.96 | ATR14%: 9.69%
- MA20/50/200 gap: -15.89% / -21.76% / -18.08%
- 5D return: -21.68% | 20D drawdown: -28.38% | vol_ratio: 0.40
- RS vs SILJ: gap -5.56% / slope_proxy -8.29%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **46.9**
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
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.68 | RSI14: 36.93 | ATR14%: 8.69%
- MA20/50/200 gap: -12.65% / -16.26% / -12.87%
- 5D return: -18.26% | 20D drawdown: -23.44% | vol_ratio: 0.31
- RS vs SILJ: gap -0.04% / slope_proxy -0.75%
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
- close: 21.72 | RSI14: 25.20 | ATR14%: 11.15%
- MA20/50/200 gap: -21.70% / -36.20% / -15.98%
- 5D return: -18.25% | 20D drawdown: -35.78% | vol_ratio: 0.38
- RS vs SILJ: gap -24.40% / slope_proxy -20.74%
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
