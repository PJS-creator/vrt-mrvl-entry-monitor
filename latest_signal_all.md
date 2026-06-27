# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-27 15:01:25**
- 데이터 기준일(일봉): **2026-06-26**
- 데이터 기준일(주봉): **2026-06-22**
- VXN 기준일: **2026-06-25** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 706.52
- Weekly RSI14: **61.01**
- 52W MA: 617.44 / gap: **14.43%**
- 104W MA gap: **27.34%**
- 52W MA 13W slope: **8.48%**
- VXN: **30.91** / 5D change: 2.35

## Daily trigger: 실제 매수 타이밍

- QQQ close: 706.52
- Daily RSI14: **46.65**
- 20D gap: **-2.44%**
- 50D gap: **0.63%**
- 200D gap: **12.03%**
- MACD hist: -3.9828 / change: -0.6221
- ATR14%: **2.31%**
- 20D high drawdown: **-5.21%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **False**
- weekly_panic: **True**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **False**
- rebound_after_panic: **False**

## Why

- 공포/급락 구간은 QLD 몰빵보다 반등 확인이 우선
- VXN이 24 초과라 레버리지 비중 확대에는 불리

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-27 15:00:39**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.78 / 4주 변화 6.0 bp
- IG OAS (BAMLC0A0CM): 0.76 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.19 / 4주 변화 13.0 bp
- VIX (VIXCLS): 18.89
- NFCI: -0.516

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.32362
- MA60: 9.3001
- gap: 0.25%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.436177
- MA60: 0.356531
- gap: 22.34%
- MA60_slope_proxy: 0.072679
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-27 15:00:45**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **True**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 91.83 bp / 4주 변화 -15.76 bp
- CURVE_10s5s: 44.05 bp / 4주 변화 -1.94 bp

## NWG Price
- close: 656.4
- MA50: 597.1651 / gap50: 9.92%
- MA200: 595.8045 / gap200: 10.17%

## Relative Strength
- RS vs FTSE gap: 8.91% / slope_proxy: 0.001532
- RS vs Peers gap: 2.50% / slope_proxy: -0.015535

## Why not today?
- CurveGreen=FALSE
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-27 15:00:52**

## Commodity Regime

- WTI ref (CL=F): 69.23 / 5D -9.62%
- Brent ref (BZ=F): 71.99 / 5D -9.84%
- Brent Tier: **70-80**
- Brent-WTI spread: 2.76
- Gas ref (NG=F): 3.23 / 5D -0.06%

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

- close: 49.99
- MA20 / MA60 / MA200: 55.02 / 56.83 / 48.89
- gap20 / gap60: -9.14% / -12.04%
- 5D return: -3.53%
- 20D high/low: 59.37 / 49.99

### Relative Strength

- ratio: 0.928492
- ratio_MA60: 0.997913
- ratio_gap: -6.96%
- ratio_slope_proxy(20d): -0.008272

### Volume (if available)

- volume: 12773300.00
- volume_MA20: 10143360.00
- volume_ratio: 1.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.29
- MA20 / MA60 / MA200: 17.57 / 19.50 / 15.47
- gap20 / gap60: -7.30% / -16.48%
- 5D return: -2.75%
- 20D high/low: 18.72 / 16.29

### Relative Strength

- ratio: 0.469859
- ratio_MA60: 0.524775
- ratio_gap: -10.46%
- ratio_slope_proxy(20d): -0.002150

### Volume (if available)

- volume: 12178900.00
- volume_MA20: 14767435.00
- volume_ratio: 0.82

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

- close: 5.11
- MA20 / MA60 / MA200: 5.78 / 6.29 / 5.10
- gap20 / gap60: -11.56% / -18.79%
- 5D return: -3.77%
- 20D high/low: 6.25 / 5.04

### Relative Strength

- ratio: 0.013607
- ratio_MA60: 0.014948
- ratio_gap: -8.97%
- ratio_slope_proxy(20d): -0.000788

### Volume (if available)

- volume: 48990400.00
- volume_MA20: 31143655.00
- volume_ratio: 1.57

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **True**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 10.95
- MA20 / MA60 / MA200: 11.97 / 12.69 / 10.77
- gap20 / gap60: -8.53% / -13.71%
- 5D return: -0.64%
- 20D high/low: 13.27 / 10.51

### Relative Strength

- ratio: 0.045315
- ratio_MA60: 0.050990
- ratio_gap: -11.13%
- ratio_slope_proxy(20d): -0.000541

### Volume (if available)

- volume: 8511900.00
- volume_MA20: 14187740.00
- volume_ratio: 0.60

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-06-26**
- 실행시간(UTC): **2026-06-27 15:01:06**

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
- IG OAS 4주 변화: 3.0 bp / latest 0.76
- 10Y Real Yield 4주 변화: 13.0 bp / latest 2.19
- VIX: 18.89
- NFCI: -0.516

### Leadership ratios
- SILJ/SLV gap: 9.78% / slope_proxy: 0.005097
- GDXJ/GLD gap: -4.06% / slope_proxy: -0.001691

## VZLA (Vizsla Silver)
- close: 3.28 | RSI14: 43.73333 | ATR14%: 6.86%
- MA20 gap: -7.62% | MA50 gap: -6.69% | MA200 gap: -22.65%
- vol_ratio(Volume/Vol20): 0.63506 | gap_open: 1.28%
- RS vs SILJ gap: 6.91% / slope_proxy: 0.004446
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
- close: 6.61 | RSI14: 41.549482 | ATR14%: 8.50%
- MA20 gap: -6.52% | MA50 gap: -17.17% | MA200 gap: -22.39%
- vol_ratio(Volume/Vol20): 0.632543 | gap_open: 3.26%
- SilverMarginGate: SI=59.216999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -5.91% / slope_proxy: -0.00963
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
- close: 23.74 | RSI14: 38.163472 | ATR14%: 10.10%
- MA20 gap: -11.29% | MA50 gap: -28.74% | MA200 gap: -8.77%
- vol_ratio(Volume/Vol20): 3.92136 | gap_open: 1.32%
- RS vs SILJ gap: -20.04% / slope_proxy: -0.078992
- RS vs GDXJ gap: -18.41% / slope_proxy: -0.016894
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

- 실행시간(UTC): **2026-06-27 15:01:21**
- 데이터 기준일(주가): **2026-06-26**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

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

- HY OAS: 2.78 / 4주 변화 0.06 bp-ish / 2026-06-25
- IG OAS: 0.76 / 4주 변화 0.03 bp-ish / 2026-06-25
- 10Y Real Yield: 2.19 / 4주 변화 0.10 bp-ish / 2026-06-25
- VIX: 18.89 / 4주 변화 3.15 / 2026-06-25
- NFCI: -0.52 / 4주 변화 0.05 / 2026-06-19

### Leadership ratios

- GDX/GLD: gap -3.34% / slope_proxy -3.94%
- GDXJ/GLD: gap -4.06% / slope_proxy -6.14%
- SILJ/SLV: gap 9.78% / slope_proxy 8.37%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.47 | RSI14: 51.71 | ATR14%: 6.38%
- MA20/50/200 gap: -4.45% / -5.73% / 12.65%
- 5D return: -7.89% | 20D drawdown: -14.14% | vol_ratio: 0.44
- RS vs GDXJ: gap 11.22% / slope_proxy 2.13%
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
- close: 5.15 | RSI14: 40.33 | ATR14%: 6.91%
- MA20/50/200 gap: -10.24% / -18.89% / -25.76%
- 5D return: -8.04% | 20D drawdown: -26.95% | vol_ratio: 0.64
- RS vs GDXJ: gap -8.09% / slope_proxy -12.24%
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
- close: 1.17 | RSI14: 46.91 | ATR14%: 8.33%
- MA20/50/200 gap: -8.34% / -12.91% / -22.17%
- 5D return: -8.59% | 20D drawdown: -20.41% | vol_ratio: 0.93
- RS vs GDXJ: gap -1.10% / slope_proxy 0.12%
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
- close: 1.52 | RSI14: 40.74 | ATR14%: 6.53%
- MA20/50/200 gap: -8.74% / -16.60% / -9.68%
- 5D return: -6.17% | 20D drawdown: -22.84% | vol_ratio: 0.33
- RS vs GDXJ: gap -3.10% / slope_proxy -6.32%
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
- close: 19.81 | RSI14: 59.97 | ATR14%: 7.45%
- MA20/50/200 gap: 4.04% / 6.63% / 29.04%
- 5D return: -0.35% | 20D drawdown: -7.82% | vol_ratio: 0.90
- RS vs SILJ: gap 23.04% / slope_proxy 11.63%
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
- close: 15.54 | RSI14: 55.52 | ATR14%: 5.96%
- MA20/50/200 gap: -1.89% / -10.18% / -13.15%
- 5D return: -2.63% | 20D drawdown: -12.70% | vol_ratio: 3.73
- RS vs SILJ: gap 0.49% / slope_proxy 3.49%
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

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.28 | RSI14: 47.44 | ATR14%: 6.61%
- MA20/50/200 gap: -7.62% / -6.69% / -22.65%
- 5D return: -7.61% | 20D drawdown: -20.58% | vol_ratio: 0.64
- RS vs SILJ: gap 6.91% / slope_proxy 0.04%
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
- close: 8.33 | RSI14: 53.47 | ATR14%: 6.83%
- MA20/50/200 gap: -3.43% / -10.21% / -12.18%
- 5D return: -3.25% | 20D drawdown: -16.45% | vol_ratio: 0.63
- RS vs SILJ: gap 1.67% / slope_proxy -1.13%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.61 | RSI14: 52.48 | ATR14%: 8.21%
- MA20/50/200 gap: -6.52% / -17.17% / -22.39%
- 5D return: -7.55% | 20D drawdown: -20.65% | vol_ratio: 0.63
- RS vs SILJ: gap -5.91% / slope_proxy -4.02%
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
- close: 4.81 | RSI14: 48.34 | ATR14%: 8.57%
- MA20/50/200 gap: -10.20% / -17.56% / -14.74%
- 5D return: -10.26% | 20D drawdown: -25.19% | vol_ratio: 0.80
- RS vs SILJ: gap -5.49% / slope_proxy -7.60%
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
- close: 6.15 | RSI14: 53.94 | ATR14%: 7.55%
- MA20/50/200 gap: -4.05% / -8.69% / -5.93%
- 5D return: -5.96% | 20D drawdown: -17.12% | vol_ratio: 0.87
- RS vs SILJ: gap 3.61% / slope_proxy -0.58%
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
- close: 23.74 | RSI14: 42.26 | ATR14%: 9.01%
- MA20/50/200 gap: -11.29% / -28.74% / -8.77%
- 5D return: -8.73% | 20D drawdown: -29.80% | vol_ratio: 3.92
- RS vs SILJ: gap -20.04% / slope_proxy -15.00%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 55 | OverallScore: **40.4**
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
