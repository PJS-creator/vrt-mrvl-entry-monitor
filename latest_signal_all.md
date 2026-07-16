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

- 실행시간(UTC): **2026-07-16 03:01:30**
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

- QQQ close: 717.74
- Weekly RSI14: **61.94**
- 52W MA: 626.94 / gap: **14.48%**
- 104W MA gap: **27.80%**
- 52W MA 13W slope: **8.20%**
- VXN: **26.28** / 5D change: -1.64

## Daily trigger: 실제 매수 타이밍

- QQQ close: 717.74
- Daily RSI14: **50.04**
- 20D gap: **-0.42%**
- 50D gap: **0.03%**
- 200D gap: **12.42%**
- MACD hist: -1.1755 / change: 0.1112
- ATR14%: **2.09%**
- 20D high drawdown: **-2.98%**

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
- 실행시간(UTC): **2026-07-16 03:00:52**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 1.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 4.0 bp
- 10Y Real Yield (DFII10): 2.33 / 4주 변화 19.0 bp
- VIX (VIXCLS): 16.5
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.866213
- MA60: 9.592697
- gap: 2.85%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.349138
- MA60: 0.379812
- gap: -8.08%
- MA60_slope_proxy: 0.05122
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-15**
- 실행시간(UTC): **2026-07-16 03:00:56**

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
- close: 649.8
- MA50: 615.7971 / gap50: 5.52%
- MA200: 604.6159 / gap200: 7.47%

## Relative Strength
- RS vs FTSE gap: 5.35% / slope_proxy: 0.002381
- RS vs Peers gap: -2.02% / slope_proxy: -0.005947

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-16 03:01:04**

## Commodity Regime

- WTI ref (CL=F): 80.12 / 5D 8.98%
- Brent ref (BZ=F): 85.30 / 5D 9.33%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.18
- Gas ref (NG=F): 2.90 / 5D -9.84%

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

- close: 53.77
- MA20 / MA60 / MA200: 51.60 / 55.38 / 49.23
- gap20 / gap60: 4.21% / -2.91%
- 5D return: 0.34%
- 20D high/low: 54.81 / 47.94

### Relative Strength

- ratio: 0.951681
- ratio_MA60: 0.980679
- ratio_gap: -2.96%
- ratio_slope_proxy(20d): -0.027853

### Volume (if available)

- volume: 8675648.00
- volume_MA20: 10131097.40
- volume_ratio: 0.86

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.86
- MA20 / MA60 / MA200: 16.83 / 18.77 / 15.72
- gap20 / gap60: 6.12% / -4.87%
- 5D return: 3.60%
- 20D high/low: 17.92 / 15.99

### Relative Strength

- ratio: 0.497770
- ratio_MA60: 0.518095
- ratio_gap: -3.92%
- ratio_slope_proxy(20d): -0.013607

### Volume (if available)

- volume: 10504776.00
- volume_MA20: 15281898.80
- volume_ratio: 0.69

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

- close: 5.20
- MA20 / MA60 / MA200: 5.19 / 6.02 / 5.20
- gap20 / gap60: 0.19% / -13.67%
- 5D return: -0.57%
- 20D high/low: 5.59 / 4.87

### Relative Strength

- ratio: 0.013610
- ratio_MA60: 0.014502
- ratio_gap: -6.15%
- ratio_slope_proxy(20d): -0.000800

### Volume (if available)

- volume: 28080926.00
- volume_MA20: 39042296.30
- volume_ratio: 0.72

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

- close: 12.91
- MA20 / MA60 / MA200: 11.57 / 12.37 / 10.65
- gap20 / gap60: 11.56% / 4.40%
- 5D return: 4.28%
- 20D high/low: 13.36 / 10.51

### Relative Strength

- ratio: 0.050463
- ratio_MA60: 0.050314
- ratio_gap: 0.30%
- ratio_slope_proxy(20d): -0.001989

### Volume (if available)

- volume: 11589953.00
- volume_MA20: 13564662.65
- volume_ratio: 0.85

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
- 실행시간(UTC): **2026-07-16 03:01:13**

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
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.33
- VIX: 16.5
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 6.68% / slope_proxy: 0.009248
- GDXJ/GLD gap: -5.46% / slope_proxy: -0.004857

## VZLA (Vizsla Silver)
- close: 3.2 | RSI14: 46.42815 | ATR14%: 6.34%
- MA20 gap: -2.16% | MA50 gap: -7.45% | MA200 gap: -23.76%
- vol_ratio(Volume/Vol20): 0.675999 | gap_open: 0.00%
- RS vs SILJ gap: 5.25% / slope_proxy: 0.005337
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
- close: 6.35 | RSI14: 42.235487 | ATR14%: 7.25%
- MA20 gap: -5.05% | MA50 gap: -15.36% | MA200 gap: -25.28%
- vol_ratio(Volume/Vol20): 0.84819 | gap_open: 0.31%
- SilverMarginGate: SI=57.334999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.08% / slope_proxy: -0.005319
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
- close: 20.889999 | RSI14: 37.044797 | ATR14%: 9.56%
- MA20 gap: -9.07% | MA50 gap: -28.64% | MA200 gap: -22.57%
- vol_ratio(Volume/Vol20): 0.691257 | gap_open: 1.01%
- RS vs SILJ gap: -21.82% / slope_proxy: -0.108913
- RS vs GDXJ gap: -21.16% / slope_proxy: -0.02384
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

- 실행시간(UTC): **2026-07-16 03:01:29**
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
- 10Y Real Yield: 2.33 / 4주 변화 0.16 bp-ish / 2026-07-14
- VIX: 16.50 / 4주 변화 0.09 / 2026-07-14
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -4.89% / slope_proxy -9.42%
- GDXJ/GLD: gap -5.46% / slope_proxy -9.90%
- SILJ/SLV: gap 6.68% / slope_proxy 2.64%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.24 | RSI14: 49.19 | ATR14%: 5.43%
- MA20/50/200 gap: -5.21% / -7.97% / 6.70%
- 5D return: -3.08% | 20D drawdown: -13.71% | vol_ratio: 0.67
- RS vs GDXJ: gap 5.45% / slope_proxy 2.28%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 4.96 | RSI14: 50.00 | ATR14%: 5.06%
- MA20/50/200 gap: -6.55% / -16.58% / -28.20%
- 5D return: -3.88% | 20D drawdown: -15.93% | vol_ratio: 1.09
- RS vs GDXJ: gap -6.83% / slope_proxy -3.08%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.90 | RSI14: 74.42 | ATR14%: 7.18%
- MA20/50/200 gap: 12.06% / 3.96% / 8.26%
- 5D return: 7.34% | 20D drawdown: -7.77% | vol_ratio: 0.80
- RS vs GDXJ: gap 20.56% / slope_proxy 30.28%
- FundamentalScore: 55 | TechnicalScore: 50 | RegimeScore: 30 | OverallScore: **48.2**
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.10 | RSI14: 44.23 | ATR14%: 7.27%
- MA20/50/200 gap: -8.49% / -15.18% / -26.94%
- 5D return: -2.65% | 20D drawdown: -21.43% | vol_ratio: 0.62
- RS vs GDXJ: gap -3.13% / slope_proxy -6.96%
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
- close: 19.75 | RSI14: 63.14 | ATR14%: 6.79%
- MA20/50/200 gap: 1.90% / 3.74% / 24.68%
- 5D return: 3.29% | 20D drawdown: -6.18% | vol_ratio: 0.67
- RS vs SILJ: gap 19.02% / slope_proxy 10.98%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.46 | RSI14: 59.07 | ATR14%: 5.40%
- MA20/50/200 gap: -1.11% / -6.92% / -14.87%
- 5D return: 2.45% | 20D drawdown: -7.54% | vol_ratio: 1.12
- RS vs SILJ: gap 4.13% / slope_proxy 9.37%
- FundamentalScore: 78 | TechnicalScore: 55 | RegimeScore: 55 | OverallScore: **65.3**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.96 | RSI14: 53.94 | ATR14%: 6.18%
- MA20/50/200 gap: -3.67% / -11.02% / -16.83%
- 5D return: 3.11% | 20D drawdown: -14.41% | vol_ratio: 0.85
- RS vs SILJ: gap 0.43% / slope_proxy 1.24%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.20 | RSI14: 53.66 | ATR14%: 5.76%
- MA20/50/200 gap: -2.16% / -7.45% / -23.76%
- 5D return: 8.11% | 20D drawdown: -13.28% | vol_ratio: 0.68
- RS vs SILJ: gap 5.25% / slope_proxy 2.58%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.03 | RSI14: 38.22 | ATR14%: 8.06%
- MA20/50/200 gap: -15.10% / -26.21% / -29.69%
- 5D return: -4.28% | 20D drawdown: -31.46% | vol_ratio: 1.11
- RS vs SILJ: gap -16.73% / slope_proxy -18.93%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **52.1**
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
- close: 5.93 | RSI14: 54.98 | ATR14%: 6.73%
- MA20/50/200 gap: -4.39% / -9.42% / -10.65%
- 5D return: 3.49% | 20D drawdown: -14.68% | vol_ratio: 0.57
- RS vs SILJ: gap 2.33% / slope_proxy 0.93%
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
- close: 6.35 | RSI14: 50.43 | ATR14%: 6.09%
- MA20/50/200 gap: -5.05% / -15.36% / -25.28%
- 5D return: 1.76% | 20D drawdown: -20.33% | vol_ratio: 0.85
- RS vs SILJ: gap -5.08% / slope_proxy -5.76%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 20.89 | RSI14: 46.29 | ATR14%: 8.17%
- MA20/50/200 gap: -9.07% / -28.64% / -22.57%
- 5D return: 0.48% | 20D drawdown: -21.38% | vol_ratio: 0.69
- RS vs SILJ: gap -21.82% / slope_proxy -7.00%
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
