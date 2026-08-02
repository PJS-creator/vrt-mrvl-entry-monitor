# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **✅ Entry condition met: VG**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: JAG.TO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-02 15:01:31**
- 데이터 기준일(일봉): **2026-07-31**
- 데이터 기준일(주봉): **2026-07-27**
- VXN 기준일: **2026-07-30** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 687.99
- Weekly RSI14: **54.24**
- 52W MA: 631.46 / gap: **8.95%**
- 104W MA gap: **21.57%**
- 52W MA 13W slope: **7.62%**
- VXN: **27.55** / 5D change: -0.51

## Daily trigger: 실제 매수 타이밍

- QQQ close: 687.99
- Daily RSI14: **45.12**
- 20D gap: **-1.86%**
- 50D gap: **-3.74%**
- 200D gap: **6.86%**
- MACD hist: -2.5607 / change: 1.2686
- ATR14%: **2.22%**
- 20D high drawdown: **-5.17%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-31**
- 실행시간(UTC): **2026-08-02 15:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.84 / 4주 변화 9.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.41 / 4주 변화 15.0 bp
- VIX (VIXCLS): 17.09
- NFCI: -0.554

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.825397
- MA60: 9.556771
- gap: -18.12%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.346993
- MA60: 0.384018
- gap: -9.64%
- MA60_slope_proxy: 0.016719
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-31**
- 실행시간(UTC): **2026-08-02 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 125.51 bp / 4주 변화 26.05 bp
- CURVE_10s5s: 44.43 bp / 4주 변화 -3.2 bp

## NWG Price
- close: 705.8
- MA50: 643.048 / gap50: 9.76%
- MA200: 613.4957 / gap200: 15.05%

## Relative Strength
- RS vs FTSE gap: 7.98% / slope_proxy: 0.002114
- RS vs Peers gap: 2.53% / slope_proxy: -0.002187

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-02 15:00:59**

## Commodity Regime

- WTI ref (CL=F): 84.67 / 5D -5.20%
- Brent ref (BZ=F): 90.12 / 5D -6.88%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.45
- Gas ref (NG=F): 2.75 / 5D -4.32%

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

- close: 57.07
- MA20 / MA60 / MA200: 54.65 / 54.97 / 49.90
- gap20 / gap60: 4.43% / 3.82%
- 5D return: -0.40%
- 20D high/low: 57.60 / 48.81

### Relative Strength

- ratio: 0.958354
- ratio_MA60: 0.969286
- ratio_gap: -1.13%
- ratio_slope_proxy(20d): -0.019084

### Volume (if available)

- volume: 6810100.00
- volume_MA20: 9024970.00
- volume_ratio: 0.75

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.40
- MA20 / MA60 / MA200: 18.01 / 18.23 / 16.10
- gap20 / gap60: 7.72% / 6.40%
- 5D return: 3.36%
- 20D high/low: 19.40 / 16.26

### Relative Strength

- ratio: 0.529331
- ratio_MA60: 0.513769
- ratio_gap: 3.03%
- ratio_slope_proxy(20d): -0.006752

### Volume (if available)

- volume: 11607200.00
- volume_MA20: 15541650.00
- volume_ratio: 0.75

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

- close: 5.32
- MA20 / MA60 / MA200: 5.18 / 5.77 / 5.32
- gap20 / gap60: 2.79% / -7.82%
- 5D return: -0.56%
- 20D high/low: 5.37 / 4.93

### Relative Strength

- ratio: 0.013825
- ratio_MA60: 0.014251
- ratio_gap: -2.99%
- ratio_slope_proxy(20d): -0.000505

### Volume (if available)

- volume: 62763100.00
- volume_MA20: 42281260.00
- volume_ratio: 1.48

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **True**

### Trend

- close: 13.38
- MA20 / MA60 / MA200: 13.14 / 12.58 / 10.69
- gap20 / gap60: 1.80% / 6.35%
- 5D return: -6.50%
- 20D high/low: 15.16 / 10.85

### Relative Strength

- ratio: 0.050765
- ratio_MA60: 0.051169
- ratio_gap: -0.79%
- ratio_slope_proxy(20d): 0.000764

### Volume (if available)

- volume: 10402400.00
- volume_MA20: 16325970.00
- volume_ratio: 0.64

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

✅ Entry condition met: VG


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-31**
- 실행시간(UTC): **2026-08-02 15:01:12**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 9.0 bp / latest 2.84
- IG OAS 4주 변화: 5.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 15.0 bp / latest 2.41
- VIX: 17.09
- NFCI: -0.554

### Leadership ratios
- SILJ/SLV gap: 0.91% / slope_proxy: 0.007656
- GDXJ/GLD gap: -4.91% / slope_proxy: -0.00868

## VZLA (Vizsla Silver)
- close: 3.14 | RSI14: 45.838584 | ATR14%: 5.98%
- MA20 gap: -1.23% | MA50 gap: -7.11% | MA200 gap: -23.80%
- vol_ratio(Volume/Vol20): 0.96659 | gap_open: 2.78%
- RS vs SILJ gap: 4.48% / slope_proxy: 0.006029
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
- close: 6.46 | RSI14: 48.282286 | ATR14%: 6.95%
- MA20 gap: 0.97% | MA50 gap: -6.16% | MA200 gap: -23.39%
- vol_ratio(Volume/Vol20): 0.701964 | gap_open: 3.83%
- SilverMarginGate: SI=57.785999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 1.86% / slope_proxy: -0.005054
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
- close: 19.530001 | RSI14: 40.566948 | ATR14%: 8.74%
- MA20 gap: -4.97% | MA50 gap: -21.11% | MA200 gap: -29.68%
- vol_ratio(Volume/Vol20): 0.706727 | gap_open: 2.79%
- RS vs SILJ gap: -16.86% / slope_proxy: -0.143044
- RS vs GDXJ gap: -18.90% / slope_proxy: -0.033856
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

- 실행시간(UTC): **2026-08-02 15:01:28**
- 데이터 기준일(주가): **2026-07-31**

## Verdict
**🟡 Precious miners watch/add-on candidates: JAG.TO, AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 2.84 / 4주 변화 0.09 bp-ish / 2026-07-30
- IG OAS: 0.80 / 4주 변화 0.05 bp-ish / 2026-07-30
- 10Y Real Yield: 2.41 / 4주 변화 0.16 bp-ish / 2026-07-30
- VIX: 17.09 / 4주 변화 0.94 / 2026-07-30
- NFCI: -0.55 / 4주 변화 -0.07 / 2026-07-24

### Leadership ratios

- GDX/GLD: gap -3.35% / slope_proxy -3.21%
- GDXJ/GLD: gap -4.91% / slope_proxy -5.58%
- SILJ/SLV: gap 0.91% / slope_proxy -2.95%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.39 | RSI14: 65.00 | ATR14%: 5.30%
- MA20/50/200 gap: 3.19% / -3.43% / -21.23%
- 5D return: 1.13% | 20D drawdown: -4.09% | vol_ratio: 1.19
- RS vs GDXJ: gap 3.44% / slope_proxy 4.47%
- FundamentalScore: 82 | TechnicalScore: 55 | RegimeScore: 30 | OverallScore: **62.1**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.88 | RSI14: 42.86 | ATR14%: 6.76%
- MA20/50/200 gap: 0.83% / 5.74% / 4.07%
- 5D return: -1.05% | 20D drawdown: -8.74% | vol_ratio: 0.15
- RS vs GDXJ: gap 14.06% / slope_proxy 20.47%
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

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.10 | RSI14: 46.93 | ATR14%: 5.35%
- MA20/50/200 gap: -2.65% / -7.19% / 3.45%
- 5D return: 0.28% | 20D drawdown: -10.24% | vol_ratio: 0.78
- RS vs GDXJ: gap 1.80% / slope_proxy -2.22%
- FundamentalScore: 88 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **50.9**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.13 | RSI14: 54.05 | ATR14%: 5.63%
- MA20/50/200 gap: 0.49% / -7.42% / -23.56%
- 5D return: 3.67% | 20D drawdown: -9.60% | vol_ratio: 0.35
- RS vs GDXJ: gap 0.19% / slope_proxy -1.53%
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
- close: 19.65 | RSI14: 52.51 | ATR14%: 6.62%
- MA20/50/200 gap: 0.25% / 2.59% / 20.43%
- 5D return: -0.25% | 20D drawdown: -5.98% | vol_ratio: 0.90
- RS vs SILJ: gap 15.72% / slope_proxy 8.76%
- FundamentalScore: 86 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **74.5**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.52 | RSI14: 45.18 | ATR14%: 6.38%
- MA20/50/200 gap: -4.60% / -10.51% / -21.38%
- 5D return: -3.84% | 20D drawdown: -11.63% | vol_ratio: 1.43
- RS vs SILJ: gap -1.52% / slope_proxy -2.43%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.46 | RSI14: 51.77 | ATR14%: 6.59%
- MA20/50/200 gap: 0.97% / -6.16% / -23.39%
- 5D return: 2.70% | 20D drawdown: -5.14% | vol_ratio: 0.70
- RS vs SILJ: gap 1.86% / slope_proxy 4.74%
- FundamentalScore: 74 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **53.3**
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
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.14 | RSI14: 54.48 | ATR14%: 5.79%
- MA20/50/200 gap: -1.23% / -7.11% / -23.80%
- 5D return: -4.85% | 20D drawdown: -8.19% | vol_ratio: 0.97
- RS vs SILJ: gap 4.48% / slope_proxy 6.03%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **52.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.82 | RSI14: 45.05 | ATR14%: 7.48%
- MA20/50/200 gap: -6.25% / -21.24% / -33.31%
- 5D return: -3.78% | 20D drawdown: -21.72% | vol_ratio: 1.03
- RS vs SILJ: gap -14.59% / slope_proxy -13.57%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **47.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.12 | RSI14: 40.72 | ATR14%: 5.75%
- MA20/50/200 gap: -6.63% / -10.13% / -22.87%
- 5D return: -6.74% | 20D drawdown: -14.22% | vol_ratio: 0.66
- RS vs SILJ: gap -0.87% / slope_proxy -5.28%
- FundamentalScore: 78 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **46.4**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.33 | RSI14: 43.28 | ATR14%: 7.02%
- MA20/50/200 gap: -7.91% / -14.08% / -19.94%
- 5D return: -5.33% | 20D drawdown: -19.00% | vol_ratio: 0.91
- RS vs SILJ: gap -4.66% / slope_proxy -10.56%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **38.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 19.53 | RSI14: 46.57 | ATR14%: 8.22%
- MA20/50/200 gap: -4.97% / -21.11% / -29.68%
- 5D return: -3.41% | 20D drawdown: -16.86% | vol_ratio: 0.71
- RS vs SILJ: gap -16.86% / slope_proxy -8.20%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **30.2**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
