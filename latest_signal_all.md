# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-29 15:01:20**
- 데이터 기준일(일봉): **2026-10-29**
- 데이터 기준일(주봉): **2026-10-26**
- VXN 기준일: **2026-10-28** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **B: QLD 부분 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **500,000원** (25%)
- 대기자금: **0원** (0%)

## Weekly gate: 큰 환경

- QQQ close: 715.65
- Weekly RSI14: **53.47**
- 52W MA: 664.55 / gap: **7.69%**
- 104W MA gap: **19.97%**
- 52W MA 13W slope: **5.35%**
- VXN: **23.78** / 5D change: -0.64

## Daily trigger: 실제 매수 타이밍

- QQQ close: 715.66
- Daily RSI14: **44.60**
- 20D gap: **-2.12%**
- 50D gap: **-1.30%**
- 200D gap: **5.55%**
- MACD hist: -1.7842 / change: 0.2684
- ATR14%: **1.57%**
- 20D high drawdown: **-5.79%**

## Checks

- weekly_good: **True**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **True**
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

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-29 15:00:52**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.14 / 4주 변화 2.0 bp
- IG OAS (BAMLC0A0CM): 0.86 / 4주 변화 2.0 bp
- 10Y Real Yield (DFII10): 2.64 / 4주 변화 -27.0 bp
- VIX (VIXCLS): 16.91
- NFCI: -0.487

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.693249
- MA60: 8.403866
- gap: 3.44%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.392671
- MA60: 0.417178
- gap: -5.87%
- MA60_slope_proxy: 0.027343
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-29 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 155.46 bp / 4주 변화 -5.94 bp
- CURVE_10s5s: 36.02 bp / 4주 변화 -6.81 bp

## NWG Price
- close: 638.6
- MA50: 674.172 / gap50: -5.28%
- MA200: 635.5056 / gap200: 0.49%

## Relative Strength
- RS vs FTSE gap: -6.31% / slope_proxy: -0.000777
- RS vs Peers gap: 5.32% / slope_proxy: 0.023732

## Why not today?
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-29 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 100.29 / 5D 0.82%
- Brent ref (BZ=F): 109.56 / 5D -3.19%
- Brent Tier: **>=90**
- Brent-WTI spread: 9.27
- Gas ref (NG=F): 2.90 / 5D 3.90%

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

- close: 62.36
- MA20 / MA60 / MA200: 61.38 / 59.71 / 55.59
- gap20 / gap60: 1.60% / 4.44%
- 5D return: -0.22%
- 20D high/low: 64.17 / 58.08

### Relative Strength

- ratio: 0.913164
- ratio_MA60: 0.933624
- ratio_gap: -2.19%
- ratio_slope_proxy(20d): -0.011645

### Volume (if available)

- volume: 1291704.00
- volume_MA20: 8107655.20
- volume_ratio: 0.16

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.67
- MA20 / MA60 / MA200: 24.45 / 21.18 / 18.60
- gap20 / gap60: -11.38% / 2.31%
- 5D return: -15.44%
- 20D high/low: 26.16 / 21.65

### Relative Strength

- ratio: 0.654433
- ratio_MA60: 0.559341
- ratio_gap: 17.00%
- ratio_slope_proxy(20d): 0.036169

### Volume (if available)

- volume: 10241318.00
- volume_MA20: 29111180.90
- volume_ratio: 0.35

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

- close: 6.68
- MA20 / MA60 / MA200: 5.86 / 5.72 / 5.85
- gap20 / gap60: 14.09% / 16.68%
- 5D return: 9.87%
- 20D high/low: 6.71 / 5.17

### Relative Strength

- ratio: 0.016345
- ratio_MA60: 0.014212
- ratio_gap: 15.01%
- ratio_slope_proxy(20d): 0.000454

### Volume (if available)

- volume: 8864020.00
- volume_MA20: 39804351.00
- volume_ratio: 0.22

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.72
- MA20 / MA60 / MA200: 13.34 / 13.80 / 12.63
- gap20 / gap60: 10.36% / 6.68%
- 5D return: 14.91%
- 20D high/low: 14.72 / 12.50

### Relative Strength

- ratio: 0.047521
- ratio_MA60: 0.049561
- ratio_gap: -4.12%
- ratio_slope_proxy(20d): -0.001421

### Volume (if available)

- volume: 4836723.00
- volume_MA20: 13624651.15
- volume_ratio: 0.35

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-10-29**
- 실행시간(UTC): **2026-10-29 15:01:08**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 2.0 bp / latest 3.14
- IG OAS 4주 변화: 2.0 bp / latest 0.86
- 10Y Real Yield 4주 변화: -27.0 bp / latest 2.64
- VIX: 16.91
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -0.38% / slope_proxy: 0.006424
- GDXJ/GLD gap: -8.84% / slope_proxy: 0.008095

## VZLA (Vizsla Silver)
- close: 3.245 | RSI14: 42.293927 | ATR14%: 5.36%
- MA20 gap: -2.59% | MA50 gap: -12.68% | MA200 gap: -13.72%
- vol_ratio(Volume/Vol20): 0.219382 | gap_open: 3.07%
- RS vs SILJ gap: 4.24% / slope_proxy: 0.000383
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## SCZM (Santacruz Silver)
- close: 7.2 | RSI14: 37.141041 | ATR14%: 6.86%
- MA20 gap: -11.58% | MA50 gap: -19.17% | MA200 gap: -18.42%
- vol_ratio(Volume/Vol20): 0.147267 | gap_open: 3.47%
- SilverMarginGate: SI=52.68 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.11% / slope_proxy: 0.019026
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: pullback=False, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- MinersLeadership(SILJ/SLV)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs SILJ)=FALSE
- Trigger(Pullback/Breakout)=FALSE

## HYMC (Hycroft Mining)
- close: 17.42 | RSI14: 45.740267 | ATR14%: 6.74%
- MA20 gap: 0.11% | MA50 gap: -14.52% | MA200 gap: -42.20%
- vol_ratio(Volume/Vol20): 0.297502 | gap_open: 3.33%
- RS vs SILJ gap: -2.10% / slope_proxy: -0.048368
- RS vs GDXJ gap: -4.22% / slope_proxy: -0.016565
- Checks:
  - trend_ok: **False**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- Trend(MA200/MA50)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-10-29 15:01:18**
- 데이터 기준일(주가): **2026-10-29**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA**

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

- HY OAS: 3.14 / 4주 변화 0.02 bp-ish / 2026-10-28
- IG OAS: 0.86 / 4주 변화 0.02 bp-ish / 2026-10-28
- 10Y Real Yield: 2.64 / 4주 변화 -0.26 bp-ish / 2026-10-27
- VIX: 16.91 / 4주 변화 0.57 / 2026-10-28
- NFCI: -0.49 / 4주 변화 0.02 / 2026-10-23

### Leadership ratios

- GDX/GLD: gap -5.01% / slope_proxy -4.12%
- GDXJ/GLD: gap -8.84% / slope_proxy -8.59%
- SILJ/SLV: gap -0.38% / slope_proxy 1.35%
- Gold breadth proxy: above50 0.00%, above200 7.69%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.80 | RSI14: 24.51 | ATR14%: 4.64%
- MA20/50/200 gap: -10.18% / -18.53% / -3.54%
- 5D return: -2.74% | 20D drawdown: -16.67% | vol_ratio: 0.40
- RS vs GDXJ: gap -4.85% / slope_proxy -5.04%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 5.69 | RSI14: 32.06 | ATR14%: 5.99%
- MA20/50/200 gap: -10.73% / -20.80% / -18.39%
- 5D return: 0.35% | 20D drawdown: -19.18% | vol_ratio: 0.05
- RS vs GDXJ: gap -6.23% / slope_proxy -8.54%
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
- close: 0.85 | RSI14: 39.56 | ATR14%: 7.48%
- MA20/50/200 gap: -9.75% / -32.23% / -40.86%
- 5D return: 0.60% | 20D drawdown: -17.96% | vol_ratio: 0.16
- RS vs GDXJ: gap -22.12% / slope_proxy -6.67%
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

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.69 | RSI14: 28.71 | ATR14%: 7.78%
- MA20/50/200 gap: -15.33% / -28.05% / -14.86%
- 5D return: -5.06% | 20D drawdown: -23.53% | vol_ratio: 0.18
- RS vs GDXJ: gap -14.18% / slope_proxy -13.52%
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
- close: 24.25 | RSI14: 33.05 | ATR14%: 5.16%
- MA20/50/200 gap: -6.30% / -10.59% / 16.59%
- 5D return: 1.63% | 20D drawdown: -11.85% | vol_ratio: 0.16
- RS vs SILJ: gap 6.66% / slope_proxy 1.66%
- FundamentalScore: 86 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **58.7**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.24 | RSI14: 38.31 | ATR14%: 5.16%
- MA20/50/200 gap: -2.59% / -12.68% / -13.72%
- 5D return: 1.72% | 20D drawdown: -10.11% | vol_ratio: 0.22
- RS vs SILJ: gap 4.24% / slope_proxy 2.20%
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.75 | RSI14: 35.39 | ATR14%: 4.96%
- MA20/50/200 gap: -5.18% / -17.57% / -20.73%
- 5D return: 1.31% | 20D drawdown: -10.61% | vol_ratio: 0.22
- RS vs SILJ: gap -2.42% / slope_proxy 2.46%
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.52 | RSI14: 29.62 | ATR14%: 4.91%
- MA20/50/200 gap: -6.74% / -18.67% / -22.34%
- 5D return: 2.94% | 20D drawdown: -15.55% | vol_ratio: 0.11
- RS vs SILJ: gap -2.57% / slope_proxy -3.99%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 7.20 | RSI14: 25.45 | ATR14%: 6.37%
- MA20/50/200 gap: -11.58% / -19.17% / -18.42%
- 5D return: 0.98% | 20D drawdown: -20.97% | vol_ratio: 0.15
- RS vs SILJ: gap -3.11% / slope_proxy -6.98%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **44.6**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 3.09 | RSI14: 17.72 | ATR14%: 7.04%
- MA20/50/200 gap: -18.14% / -32.32% / -45.99%
- 5D return: -3.29% | 20D drawdown: -30.98% | vol_ratio: 0.32
- RS vs SILJ: gap -20.07% / slope_proxy -20.64%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **41.9**
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

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 4.62 | RSI14: 29.87 | ATR14%: 5.80%
- MA20/50/200 gap: -10.19% / -24.14% / -32.93%
- 5D return: -3.14% | 20D drawdown: -17.20% | vol_ratio: 0.28
- RS vs SILJ: gap -11.11% / slope_proxy -5.36%
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
- close: 17.42 | RSI14: 39.66 | ATR14%: 6.46%
- MA20/50/200 gap: 0.11% / -14.52% / -42.20%
- 5D return: 10.53% | 20D drawdown: -9.22% | vol_ratio: 0.30
- RS vs SILJ: gap -2.10% / slope_proxy 5.86%
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
