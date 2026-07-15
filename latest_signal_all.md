# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-15 15:01:47**
- 데이터 기준일(일봉): **2026-07-15**
- 데이터 기준일(주봉): **2026-07-13**
- VXN 기준일: **2026-07-14** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 715.20
- Weekly RSI14: **61.22**
- 52W MA: 626.89 / gap: **14.09%**
- 104W MA gap: **27.35%**
- 52W MA 13W slope: **8.19%**
- VXN: **26.28** / 5D change: -1.64

## Daily trigger: 실제 매수 타이밍

- QQQ close: 715.20
- Daily RSI14: **49.16**
- 20D gap: **-0.92%**
- 50D gap: **-0.19%**
- 200D gap: **12.13%**
- MACD hist: -1.5735 / change: 0.0159
- ATR14%: **2.12%**
- 20D high drawdown: **-3.77%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **True**

## Why

- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-07-15**
- 실행시간(UTC): **2026-07-15 15:00:58**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.36 / 4주 변화 21.0 bp
- VIX (VIXCLS): 16.5
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.637274
- MA60: 9.588882
- gap: 0.50%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.356609
- MA60: 0.378775
- gap: -5.85%
- MA60_slope_proxy: 0.054362
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-15**
- 실행시간(UTC): **2026-07-15 15:01:03**

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
- TERM_SPREAD_10Y_POLICY: 120.03 bp / 4주 변화 16.41 bp
- CURVE_10s5s: 46.65 bp / 4주 변화 -1.22 bp

## NWG Price
- close: 658.0
- MA50: 618.0571 / gap50: 6.46%
- MA200: 605.3119 / gap200: 8.70%

## Relative Strength
- RS vs FTSE gap: 6.78% / slope_proxy: 0.002395
- RS vs Peers gap: -0.22% / slope_proxy: -0.004965

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-15 15:01:12**

## Commodity Regime

- WTI ref (CL=F): 78.82 / 5D 7.21%
- Brent ref (BZ=F): 83.72 / 5D 7.31%
- Brent Tier: **80-90**
- Brent-WTI spread: 4.90
- Gas ref (NG=F): 2.92 / 5D -9.22%

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

- close: 53.50
- MA20 / MA60 / MA200: 51.58 / 55.36 / 49.19
- gap20 / gap60: 3.72% / -3.36%
- 5D return: 3.52%
- 20D high/low: 54.81 / 47.94

### Relative Strength

- ratio: 0.951196
- ratio_MA60: 0.981037
- ratio_gap: -3.04%
- ratio_slope_proxy(20d): -0.027919

### Volume (if available)

- volume: 2100868.00
- volume_MA20: 9779463.40
- volume_ratio: 0.21

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.83
- MA20 / MA60 / MA200: 16.80 / 18.81 / 15.70
- gap20 / gap60: 6.11% / -5.24%
- 5D return: 6.99%
- 20D high/low: 17.88 / 15.99

### Relative Strength

- ratio: 0.495828
- ratio_MA60: 0.518020
- ratio_gap: -4.28%
- ratio_slope_proxy(20d): -0.014334

### Volume (if available)

- volume: 2868979.00
- volume_MA20: 15301018.95
- volume_ratio: 0.19

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

- close: 5.21
- MA20 / MA60 / MA200: 5.22 / 6.03 / 5.19
- gap20 / gap60: -0.03% / -13.57%
- 5D return: 3.88%
- 20D high/low: 5.83 / 4.87

### Relative Strength

- ratio: 0.013707
- ratio_MA60: 0.014521
- ratio_gap: -5.61%
- ratio_slope_proxy(20d): -0.000821

### Volume (if available)

- volume: 5687107.00
- volume_MA20: 37703645.35
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

- close: 12.87
- MA20 / MA60 / MA200: 11.49 / 12.34 / 10.66
- gap20 / gap60: 11.93% / 4.30%
- 5D return: 11.00%
- 20D high/low: 13.36 / 10.51

### Relative Strength

- ratio: 0.049944
- ratio_MA60: 0.050235
- ratio_gap: -0.58%
- ratio_slope_proxy(20d): -0.002085

### Volume (if available)

- volume: 3006430.00
- volume_MA20: 13719731.50
- volume_ratio: 0.22

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

- 데이터 기준일(주가): **2026-07-15**
- 실행시간(UTC): **2026-07-15 15:01:23**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 1.0 bp / latest 2.72
- IG OAS 4주 변화: 4.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 21.0 bp / latest 2.36
- VIX: 16.5
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 5.46% / slope_proxy: 0.009355
- GDXJ/GLD gap: -5.63% / slope_proxy: -0.003843

## VZLA (Vizsla Silver)
- close: 3.175 | RSI14: 45.655368 | ATR14%: 6.17%
- MA20 gap: -2.88% | MA50 gap: -8.16% | MA200 gap: -24.36%
- vol_ratio(Volume/Vol20): 0.183583 | gap_open: 0.00%
- RS vs SILJ gap: 5.16% / slope_proxy: 0.005335
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
- close: 6.41 | RSI14: 43.017961 | ATR14%: 6.95%
- MA20 gap: -4.19% | MA50 gap: -14.57% | MA200 gap: -24.58%
- vol_ratio(Volume/Vol20): 0.315085 | gap_open: 0.31%
- SilverMarginGate: SI=58.43 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.54% / slope_proxy: -0.005249
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
- close: 20.9 | RSI14: 37.069984 | ATR14%: 9.22%
- MA20 gap: -9.03% | MA50 gap: -28.60% | MA200 gap: -22.54%
- vol_ratio(Volume/Vol20): 0.142328 | gap_open: 1.01%
- RS vs SILJ gap: -21.24% / slope_proxy: -0.108809
- RS vs GDXJ gap: -21.72% / slope_proxy: -0.022726
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

- 실행시간(UTC): **2026-07-15 15:01:45**
- 데이터 기준일(주가): **2026-07-15**

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

- HY OAS: 2.72 / 4주 변화 0.01 bp-ish / 2026-07-14
- IG OAS: 0.79 / 4주 변화 0.04 bp-ish / 2026-07-14
- 10Y Real Yield: 2.36 / 4주 변화 0.20 bp-ish / 2026-07-13
- VIX: 16.50 / 4주 변화 0.09 / 2026-07-14
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -5.22% / slope_proxy -7.73%
- GDXJ/GLD: gap -5.76% / slope_proxy -8.20%
- SILJ/SLV: gap 5.45% / slope_proxy 3.48%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.29 | RSI14: 50.21 | ATR14%: 5.26%
- MA20/50/200 gap: -4.59% / -7.35% / 7.43%
- 5D return: -2.41% | 20D drawdown: -13.11% | vol_ratio: 0.23
- RS vs GDXJ: gap 6.53% / slope_proxy 6.44%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.88 | RSI14: 65.98 | ATR14%: 6.76%
- MA20/50/200 gap: 11.67% / 3.25% / 7.55%
- 5D return: 8.05% | 20D drawdown: -8.74% | vol_ratio: 0.16
- RS vs GDXJ: gap 19.93% / slope_proxy 23.09%
- FundamentalScore: 55 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **53.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.03 | RSI14: 44.69 | ATR14%: 5.13%
- MA20/50/200 gap: -6.33% / -15.84% / -27.24%
- 5D return: -4.91% | 20D drawdown: -18.21% | vol_ratio: 0.31
- RS vs GDXJ: gap -5.66% / slope_proxy -3.82%
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
- close: 1.12 | RSI14: 46.30 | ATR14%: 7.05%
- MA20/50/200 gap: -6.90% / -13.66% / -25.62%
- 5D return: -0.88% | 20D drawdown: -20.00% | vol_ratio: 0.11
- RS vs GDXJ: gap -1.35% / slope_proxy -6.93%
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
- close: 19.54 | RSI14: 56.45 | ATR14%: 6.83%
- MA20/50/200 gap: 0.71% / 2.83% / 23.78%
- 5D return: 4.05% | 20D drawdown: -7.17% | vol_ratio: 0.10
- RS vs SILJ: gap 19.31% / slope_proxy 10.51%
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
- Why not today: SilverUptrend=FALSE, SectorBreadthProxy=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.96 | RSI14: 49.23 | ATR14%: 6.06%
- MA20/50/200 gap: -4.27% / -11.24% / -16.81%
- 5D return: -0.75% | 20D drawdown: -14.41% | vol_ratio: 0.32
- RS vs SILJ: gap 1.18% / slope_proxy 2.05%
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
- close: 15.19 | RSI14: 51.04 | ATR14%: 5.35%
- MA20/50/200 gap: -3.15% / -8.83% / -16.29%
- 5D return: -2.41% | 20D drawdown: -9.18% | vol_ratio: 0.10
- RS vs SILJ: gap 3.07% / slope_proxy 6.45%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.17 | RSI14: 52.59 | ATR14%: 5.59%
- MA20/50/200 gap: -2.88% / -8.16% / -24.36%
- 5D return: 7.26% | 20D drawdown: -13.96% | vol_ratio: 0.18
- RS vs SILJ: gap 5.16% / slope_proxy 2.49%
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 5.88 | RSI14: 50.00 | ATR14%: 6.74%
- MA20/50/200 gap: -5.80% / -10.33% / -11.32%
- 5D return: -3.13% | 20D drawdown: -15.40% | vol_ratio: 0.14
- RS vs SILJ: gap 2.19% / slope_proxy 0.55%
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
- close: 6.41 | RSI14: 51.75 | ATR14%: 5.81%
- MA20/50/200 gap: -4.19% / -14.57% / -24.58%
- 5D return: 2.72% | 20D drawdown: -19.57% | vol_ratio: 0.32
- RS vs SILJ: gap -3.54% / slope_proxy -4.20%
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
- close: 4.03 | RSI14: 30.84 | ATR14%: 8.10%
- MA20/50/200 gap: -16.47% / -26.66% / -29.63%
- 5D return: -7.99% | 20D drawdown: -31.46% | vol_ratio: 0.26
- RS vs SILJ: gap -16.39% / slope_proxy -18.29%
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
- close: 20.90 | RSI14: 46.33 | ATR14%: 7.83%
- MA20/50/200 gap: -9.03% / -28.60% / -22.54%
- 5D return: 0.53% | 20D drawdown: -21.34% | vol_ratio: 0.14
- RS vs SILJ: gap -21.24% / slope_proxy -6.30%
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
