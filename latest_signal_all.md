# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-10 15:01:16**
- 데이터 기준일(일봉): **2026-07-10**
- 데이터 기준일(주봉): **2026-07-06**
- VXN 기준일: **2026-07-09** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 720.14
- Weekly RSI14: **63.37**
- 52W MA: 623.78 / gap: **15.45%**
- 104W MA gap: **28.78%**
- 52W MA 13W slope: **8.40%**
- VXN: **26.91** / 5D change: -0.78

## Daily trigger: 실제 매수 타이밍

- QQQ close: 720.14
- Daily RSI14: **51.00**
- 20D gap: **-0.27%**
- 50D gap: **0.79%**
- 200D gap: **13.12%**
- MACD hist: -1.5118 / change: 0.3358
- ATR14%: **2.11%**
- 20D high drawdown: **-3.10%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-10**
- 실행시간(UTC): **2026-07-10 15:00:48**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -10.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.31 / 4주 변화 10.0 bp
- VIX (VIXCLS): 15.84
- NFCI: -0.515

## VRT 신규진입 룰
- ratio (VRT/SRVR): 10.236623
- MA60: 9.52278
- gap: 7.50%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.387043
- MA60: 0.376588
- gap: 2.78%
- MA60_slope_proxy: 0.059772
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-10**
- 실행시간(UTC): **2026-07-10 15:00:50**

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
- TERM_SPREAD_10Y_POLICY: 120.45 bp / 4주 변화 5.24 bp
- CURVE_10s5s: 47.92 bp / 4주 변화 3.08 bp

## NWG Price
- close: 666.4
- MA50: 612.7971 / gap50: 8.75%
- MA200: 603.2378 / gap200: 10.47%

## Relative Strength
- RS vs FTSE gap: 8.62% / slope_proxy: 0.002378
- RS vs Peers gap: 1.47% / slope_proxy: -0.007087

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-10 15:00:58**

## Commodity Regime

- WTI ref (CL=F): 71.82 / 5D 4.56%
- Brent ref (BZ=F): 76.32 / 5D 6.30%
- Brent Tier: **70-80**
- Brent-WTI spread: 4.50
- Gas ref (NG=F): 2.89 / 5D -9.45%

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

- close: 52.49
- MA20 / MA60 / MA200: 51.74 / 55.42 / 49.10
- gap20 / gap60: 1.43% / -5.29%
- 5D return: 7.31%
- 20D high/low: 56.54 / 47.94

### Relative Strength

- ratio: 0.956359
- ratio_MA60: 0.982546
- ratio_gap: -2.67%
- ratio_slope_proxy(20d): -0.027015

### Volume (if available)

- volume: 1701337.00
- volume_MA20: 9910336.85
- volume_ratio: 0.17

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.20
- MA20 / MA60 / MA200: 16.84 / 18.99 / 15.75
- gap20 / gap60: 2.17% / -9.42%
- 5D return: 6.80%
- 20D high/low: 18.38 / 15.99

### Relative Strength

- ratio: 0.480721
- ratio_MA60: 0.520470
- ratio_gap: -7.64%
- ratio_slope_proxy(20d): -0.015821

### Volume (if available)

- volume: 3135749.00
- volume_MA20: 14883817.45
- volume_ratio: 0.21

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.13
- MA20 / MA60 / MA200: 5.29 / 6.06 / 5.17
- gap20 / gap60: -2.98% / -15.41%
- 5D return: 1.38%
- 20D high/low: 6.04 / 4.87

### Relative Strength

- ratio: 0.013614
- ratio_MA60: 0.014572
- ratio_gap: -6.57%
- ratio_slope_proxy(20d): -0.000855

### Volume (if available)

- volume: 12032008.00
- volume_MA20: 35374835.40
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

- close: 12.26
- MA20 / MA60 / MA200: 11.47 / 12.31 / 10.68
- gap20 / gap60: 6.89% / -0.40%
- 5D return: 10.18%
- 20D high/low: 13.06 / 10.51

### Relative Strength

- ratio: 0.047520
- ratio_MA60: 0.050124
- ratio_gap: -5.19%
- ratio_slope_proxy(20d): -0.002127

### Volume (if available)

- volume: 3707189.00
- volume_MA20: 13731754.45
- volume_ratio: 0.27

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-07-10**
- 실행시간(UTC): **2026-07-10 15:01:05**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -10.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 10.0 bp / latest 2.31
- VIX: 15.84
- NFCI: -0.515

### Leadership ratios
- SILJ/SLV gap: 5.19% / slope_proxy: 0.008602
- GDXJ/GLD gap: -4.85% / slope_proxy: -0.002739

## VZLA (Vizsla Silver)
- close: 3.1245 | RSI14: 42.528661 | ATR14%: 6.52%
- MA20 gap: -6.30% | MA50 gap: -10.06% | MA200 gap: -25.79%
- vol_ratio(Volume/Vol20): 0.264045 | gap_open: 0.95%
- RS vs SILJ gap: 2.33% / slope_proxy: 0.005147
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
- close: 6.5 | RSI14: 43.547637 | ATR14%: 7.40%
- MA20 gap: -4.24% | MA50 gap: -14.39% | MA200 gap: -23.62%
- vol_ratio(Volume/Vol20): 0.178578 | gap_open: 1.20%
- SilverMarginGate: SI=60.110001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -4.42% / slope_proxy: -0.004909
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
- close: 21.299999 | RSI14: 35.356873 | ATR14%: 9.54%
- MA20 gap: -10.32% | MA50 gap: -29.46% | MA200 gap: -20.40%
- vol_ratio(Volume/Vol20): 0.148976 | gap_open: 0.00%
- RS vs SILJ gap: -22.87% / slope_proxy: -0.099863
- RS vs GDXJ gap: -22.77% / slope_proxy: -0.02175
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

- 실행시간(UTC): **2026-07-10 15:01:15**
- 데이터 기준일(주가): **2026-07-10**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

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

- HY OAS: 2.70 / 4주 변화 -0.10 bp-ish / 2026-07-08
- IG OAS: 0.76 / 4주 변화 0.01 bp-ish / 2026-07-08
- 10Y Real Yield: 2.31 / 4주 변화 0.10 bp-ish / 2026-07-08
- VIX: 15.84 / 4주 변화 -3.60 / 2026-07-09
- NFCI: -0.52 / 4주 변화 0.03 / 2026-07-03

### Leadership ratios

- GDX/GLD: gap -4.60% / slope_proxy -0.36%
- GDXJ/GLD: gap -4.85% / slope_proxy 0.37%
- SILJ/SLV: gap 5.19% / slope_proxy 9.13%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.65 | RSI14: 41.29 | ATR14%: 5.19%
- MA20/50/200 gap: -0.47% / -2.82% / 13.29%
- 5D return: 0.00% | 20D drawdown: -8.82% | vol_ratio: 0.08
- RS vs GDXJ: gap 10.08% / slope_proxy 6.76%
- FundamentalScore: 88 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **75.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.06 | RSI14: 76.19 | ATR14%: 5.55%
- MA20/50/200 gap: 24.36% / 13.76% / 18.75%
- 5D return: 20.47% | 20D drawdown: 0.00% | vol_ratio: 1.26
- RS vs GDXJ: gap 29.79% / slope_proxy 31.58%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **53.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.17 | RSI14: 40.77 | ATR14%: 5.39%
- MA20/50/200 gap: -5.11% / -14.31% / -25.31%
- 5D return: -10.09% | 20D drawdown: -15.93% | vol_ratio: 0.22
- RS vs GDXJ: gap -5.43% / slope_proxy -3.44%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.17 | RSI14: 41.27 | ATR14%: 6.90%
- MA20/50/200 gap: -6.02% / -10.78% / -22.45%
- 5D return: -10.00% | 20D drawdown: -20.41% | vol_ratio: 0.15
- RS vs GDXJ: gap 0.83% / slope_proxy -2.52%
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
- close: 19.97 | RSI14: 50.45 | ATR14%: 6.62%
- MA20/50/200 gap: 3.68% / 5.64% / 27.17%
- 5D return: 1.78% | 20D drawdown: -5.13% | vol_ratio: 0.17
- RS vs SILJ: gap 21.03% / slope_proxy 18.43%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 55 | OverallScore: **72.5**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.20 | RSI14: 43.88 | ATR14%: 5.93%
- MA20/50/200 gap: -1.98% / -9.06% / -14.27%
- 5D return: -4.21% | 20D drawdown: -11.83% | vol_ratio: 0.19
- RS vs SILJ: gap 2.38% / slope_proxy 4.94%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **61.9**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.68 | RSI14: 47.58 | ATR14%: 5.28%
- MA20/50/200 gap: 0.08% / -6.44% / -13.39%
- 5D return: -4.01% | 20D drawdown: -6.25% | vol_ratio: 0.08
- RS vs SILJ: gap 4.50% / slope_proxy 8.40%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **60.1**
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
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.09 | RSI14: 42.93 | ATR14%: 6.51%
- MA20/50/200 gap: -3.02% / -7.41% / -7.95%
- 5D return: -7.28% | 20D drawdown: -12.35% | vol_ratio: 0.21
- RS vs SILJ: gap 4.01% / slope_proxy 5.60%
- FundamentalScore: 60 | TechnicalScore: 40 | RegimeScore: 55 | OverallScore: **52.0**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.50 | RSI14: 38.01 | ATR14%: 6.06%
- MA20/50/200 gap: -4.24% / -14.39% / -23.62%
- 5D return: -2.84% | 20D drawdown: -18.44% | vol_ratio: 0.18
- RS vs SILJ: gap -4.42% / slope_proxy 0.72%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.12 | RSI14: 34.64 | ATR14%: 5.89%
- MA20/50/200 gap: -6.30% / -10.06% / -25.79%
- 5D return: -6.45% | 20D drawdown: -15.33% | vol_ratio: 0.26
- RS vs SILJ: gap 2.33% / slope_proxy -6.66%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 55 | OverallScore: **48.6**
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
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.39 | RSI14: 29.47 | ATR14%: 7.62%
- MA20/50/200 gap: -11.21% / -21.13% / -23.32%
- 5D return: -10.33% | 20D drawdown: -25.43% | vol_ratio: 0.25
- RS vs SILJ: gap -11.27% / slope_proxy -8.91%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.30 | RSI14: 30.29 | ATR14%: 7.99%
- MA20/50/200 gap: -10.32% / -29.46% / -20.40%
- 5D return: -9.82% | 20D drawdown: -23.49% | vol_ratio: 0.15
- RS vs SILJ: gap -22.87% / slope_proxy -12.35%
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
