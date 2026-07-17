# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-17 15:01:16**
- 데이터 기준일(일봉): **2026-07-17**
- 데이터 기준일(주봉): **2026-07-13**
- VXN 기준일: **2026-07-16** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 694.01
- Weekly RSI14: **55.81**
- 52W MA: 626.49 / gap: **10.78%**
- 104W MA gap: **23.62%**
- 52W MA 13W slope: **8.12%**
- VXN: **27.34** / 5D change: 0.43

## Daily trigger: 실제 매수 타이밍

- QQQ close: 693.97
- Daily RSI14: **41.65**
- 20D gap: **-3.38%**
- 50D gap: **-3.41%**
- 200D gap: **8.51%**
- MACD hist: -2.9011 / change: -1.0850
- ATR14%: **2.20%**
- 20D high drawdown: **-6.20%**

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

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-17 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 8.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.32 / 4주 변화 9.0 bp
- VIX (VIXCLS): 16.73
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.390989
- MA60: 9.610124
- gap: -2.28%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.334523
- MA60: 0.380168
- gap: -12.01%
- MA60_slope_proxy: 0.043949
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-17 15:00:48**

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
- TERM_SPREAD_10Y_POLICY: 118.99 bp / 4주 변화 20.05 bp
- CURVE_10s5s: 47.2 bp / 4주 변화 0.42 bp

## NWG Price
- close: 661.2
- MA50: 621.716 / gap50: 6.35%
- MA200: 606.728 / gap200: 8.98%

## Relative Strength
- RS vs FTSE gap: 6.27% / slope_proxy: 0.002256
- RS vs Peers gap: 0.40% / slope_proxy: -0.004257

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-17 15:00:55**

## Commodity Regime

- WTI ref (CL=F): 80.61 / 5D 12.88%
- Brent ref (BZ=F): 86.64 / 5D 13.98%
- Brent Tier: **80-90**
- Brent-WTI spread: 6.03
- Gas ref (NG=F): 2.89 / 5D -1.60%

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

- close: 54.28
- MA20 / MA60 / MA200: 51.66 / 55.34 / 49.30
- gap20 / gap60: 5.06% / -1.93%
- 5D return: 2.62%
- 20D high/low: 54.81 / 47.94

### Relative Strength

- ratio: 0.944406
- ratio_MA60: 0.978723
- ratio_gap: -3.51%
- ratio_slope_proxy(20d): -0.028254

### Volume (if available)

- volume: 2423594.00
- volume_MA20: 9684484.70
- volume_ratio: 0.25

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.80
- MA20 / MA60 / MA200: 16.90 / 18.67 / 15.77
- gap20 / gap60: 5.29% / -4.70%
- 5D return: 2.74%
- 20D high/low: 17.92 / 15.99

### Relative Strength

- ratio: 0.505109
- ratio_MA60: 0.517803
- ratio_gap: -2.45%
- ratio_slope_proxy(20d): -0.012779

### Volume (if available)

- volume: 5134053.00
- volume_MA20: 14424657.65
- volume_ratio: 0.36

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **True**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.08
- MA20 / MA60 / MA200: 5.14 / 5.99 / 5.22
- gap20 / gap60: -1.20% / -15.25%
- 5D return: -2.31%
- 20D high/low: 5.41 / 4.87

### Relative Strength

- ratio: 0.013541
- ratio_MA60: 0.014462
- ratio_gap: -6.37%
- ratio_slope_proxy(20d): -0.000766

### Volume (if available)

- volume: 6214360.00
- volume_MA20: 38273028.00
- volume_ratio: 0.16

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

- close: 13.18
- MA20 / MA60 / MA200: 11.76 / 12.40 / 10.64
- gap20 / gap60: 12.05% / 6.21%
- 5D return: 7.64%
- 20D high/low: 13.36 / 10.51

### Relative Strength

- ratio: 0.050654
- ratio_MA60: 0.050434
- ratio_gap: 0.43%
- ratio_slope_proxy(20d): -0.001608

### Volume (if available)

- volume: 5283648.00
- volume_MA20: 12518177.40
- volume_ratio: 0.42

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

- 데이터 기준일(주가): **2026-07-17**
- 실행시간(UTC): **2026-07-17 15:01:03**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 8.0 bp / latest 2.71
- IG OAS 4주 변화: 5.0 bp / latest 0.79
- 10Y Real Yield 4주 변화: 9.0 bp / latest 2.32
- VIX: 16.73
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 3.19% / slope_proxy: 0.008694
- GDXJ/GLD gap: -8.64% / slope_proxy: -0.006924

## VZLA (Vizsla Silver)
- close: 3.01 | RSI14: 40.658646 | ATR14%: 6.55%
- MA20 gap: -6.26% | MA50 gap: -12.69% | MA200 gap: -28.07%
- vol_ratio(Volume/Vol20): 0.324032 | gap_open: 1.63%
- RS vs SILJ gap: 5.42% / slope_proxy: 0.005636
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
- close: 5.7526 | RSI14: 35.174298 | ATR14%: 7.87%
- MA20 gap: -11.51% | MA50 gap: -22.51% | MA200 gap: -32.15%
- vol_ratio(Volume/Vol20): 0.442041 | gap_open: 2.68%
- SilverMarginGate: SI=55.919998 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -7.58% / slope_proxy: -0.00603
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
- close: 18.385 | RSI14: 31.299217 | ATR14%: 10.69%
- MA20 gap: -17.22% | MA50 gap: -35.67% | MA200 gap: -32.16%
- vol_ratio(Volume/Vol20): 0.274684 | gap_open: 1.27%
- RS vs SILJ gap: -25.06% / slope_proxy: -0.118166
- RS vs GDXJ gap: -25.61% / slope_proxy: -0.026213
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

- 실행시간(UTC): **2026-07-17 15:01:14**
- 데이터 기준일(주가): **2026-07-17**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA, HL**

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

- HY OAS: 2.71 / 4주 변화 0.08 bp-ish / 2026-07-15
- IG OAS: 0.79 / 4주 변화 0.05 bp-ish / 2026-07-15
- 10Y Real Yield: 2.32 / 4주 변화 0.17 bp-ish / 2026-07-15
- VIX: 16.73 / 4주 변화 0.33 / 2026-07-16
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -7.38% / slope_proxy -9.58%
- GDXJ/GLD: gap -8.64% / slope_proxy -9.97%
- SILJ/SLV: gap 3.19% / slope_proxy -0.74%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.70 | RSI14: 36.30 | ATR14%: 5.91%
- MA20/50/200 gap: -10.60% / -14.53% / -1.48%
- 5D return: -13.10% | 20D drawdown: -17.49% | vol_ratio: 0.47
- RS vs GDXJ: gap 2.45% / slope_proxy -3.17%
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
- close: 4.86 | RSI14: 42.25 | ATR14%: 5.07%
- MA20/50/200 gap: -6.72% / -17.28% / -29.56%
- 5D return: -6.18% | 20D drawdown: -15.48% | vol_ratio: 0.32
- RS vs GDXJ: gap -3.40% / slope_proxy -1.13%
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
- close: 1.72 | RSI14: 60.87 | ATR14%: 8.22%
- MA20/50/200 gap: 0.70% / -6.11% / -2.63%
- 5D return: -16.50% | 20D drawdown: -16.50% | vol_ratio: 0.72
- RS vs GDXJ: gap 14.14% / slope_proxy 25.11%
- FundamentalScore: 55 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **44.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.03 | RSI14: 37.04 | ATR14%: 7.18%
- MA20/50/200 gap: -11.93% / -19.81% / -31.42%
- 5D return: -10.43% | 20D drawdown: -21.37% | vol_ratio: 0.73
- RS vs GDXJ: gap -4.30% / slope_proxy -11.70%
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
- close: 18.51 | RSI14: 42.43 | ATR14%: 6.78%
- MA20/50/200 gap: -3.48% / -2.96% / 16.31%
- 5D return: -8.84% | 20D drawdown: -8.84% | vol_ratio: 0.29
- RS vs SILJ: gap 18.11% / slope_proxy 10.93%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.16 | RSI14: 37.34 | ATR14%: 5.82%
- MA20/50/200 gap: -8.25% / -14.16% / -22.16%
- 5D return: -10.52% | 20D drawdown: -14.00% | vol_ratio: 0.16
- RS vs SILJ: gap 2.02% / slope_proxy 5.65%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **55.1**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.01 | RSI14: 39.20 | ATR14%: 6.07%
- MA20/50/200 gap: -6.26% / -12.69% / -28.07%
- 5D return: -3.83% | 20D drawdown: -15.21% | vol_ratio: 0.32
- RS vs SILJ: gap 5.42% / slope_proxy 0.99%
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
- close: 7.33 | RSI14: 34.26 | ATR14%: 6.56%
- MA20/50/200 gap: -9.48% / -17.55% / -23.39%
- 5D return: -9.30% | 20D drawdown: -14.88% | vol_ratio: 0.36
- RS vs SILJ: gap -1.04% / slope_proxy 1.39%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 5.76 | RSI14: 33.93 | ATR14%: 6.80%
- MA20/50/200 gap: -11.45% / -22.45% / -32.09%
- 5D return: -11.56% | 20D drawdown: -19.48% | vol_ratio: 0.44
- RS vs SILJ: gap -7.50% / slope_proxy -4.09%
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
- close: 3.61 | RSI14: 25.15 | ATR14%: 8.88%
- MA20/50/200 gap: -20.45% / -33.00% / -37.11%
- 5D return: -16.16% | 20D drawdown: -32.74% | vol_ratio: 0.33
- RS vs SILJ: gap -19.65% / slope_proxy -19.89%
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
- close: 5.39 | RSI14: 37.07 | ATR14%: 7.28%
- MA20/50/200 gap: -11.03% / -17.25% / -18.82%
- 5D return: -10.91% | 20D drawdown: -18.09% | vol_ratio: 0.44
- RS vs SILJ: gap -0.40% / slope_proxy -1.83%
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
- close: 18.39 | RSI14: 26.46 | ATR14%: 9.37%
- MA20/50/200 gap: -17.22% / -35.67% / -32.16%
- 5D return: -14.01% | 20D drawdown: -29.32% | vol_ratio: 0.27
- RS vs SILJ: gap -25.06% / slope_proxy -15.81%
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
