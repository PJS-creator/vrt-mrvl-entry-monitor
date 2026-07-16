# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, AYA, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-16 15:01:25**
- 데이터 기준일(일봉): **2026-07-16**
- 데이터 기준일(주봉): **2026-07-13**
- VXN 기준일: **2026-07-15** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 711.42
- Weekly RSI14: **60.18**
- 52W MA: 626.82 / gap: **13.50%**
- 104W MA gap: **26.68%**
- 52W MA 13W slope: **8.18%**
- VXN: **25.65** / 5D change: -2.21

## Daily trigger: 실제 매수 타이밍

- QQQ close: 711.42
- Daily RSI14: **47.58**
- 20D gap: **-1.18%**
- 50D gap: **-0.96%**
- 200D gap: **11.32%**
- MACD hist: -1.4664 / change: -0.2909
- ATR14%: **2.06%**
- 20D high drawdown: **-3.84%**

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

- 데이터 기준일(주가): **2026-07-16**
- 실행시간(UTC): **2026-07-16 15:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 8.0 bp
- IG OAS (BAMLC0A0CM): 0.79 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.33 / 4주 변화 19.0 bp
- VIX (VIXCLS): 15.67
- NFCI: -0.538

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.759895
- MA60: 9.606281
- gap: 1.60%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.335136
- MA60: 0.380088
- gap: -11.83%
- MA60_slope_proxy: 0.047764
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-16**
- 실행시간(UTC): **2026-07-16 15:00:46**

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
- TERM_SPREAD_10Y_POLICY: 118.86 bp / 4주 변화 15.92 bp
- CURVE_10s5s: 46.96 bp / 4주 변화 0.63 bp

## NWG Price
- close: 658.8
- MA50: 619.8211 / gap50: 6.29%
- MA200: 606.0259 / gap200: 8.71%

## Relative Strength
- RS vs FTSE gap: 6.58% / slope_proxy: 0.002284
- RS vs Peers gap: -0.58% / slope_proxy: -0.004683

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-16 15:00:57**

## Commodity Regime

- WTI ref (CL=F): 79.73 / 5D 10.61%
- Brent ref (BZ=F): 85.03 / 5D 11.44%
- Brent Tier: **80-90**
- Brent-WTI spread: 5.30
- Gas ref (NG=F): 2.86 / 5D -5.18%

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

- close: 53.74
- MA20 / MA60 / MA200: 51.60 / 55.37 / 49.26
- gap20 / gap60: 4.15% / -2.94%
- 5D return: 2.76%
- 20D high/low: 54.81 / 47.94

### Relative Strength

- ratio: 0.941656
- ratio_MA60: 0.979843
- ratio_gap: -3.90%
- ratio_slope_proxy(20d): -0.027748

### Volume (if available)

- volume: 1655340.00
- volume_MA20: 9731397.00
- volume_ratio: 0.17

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 17.70
- MA20 / MA60 / MA200: 16.86 / 18.73 / 15.75
- gap20 / gap60: 4.99% / -5.46%
- 5D return: 3.96%
- 20D high/low: 17.92 / 15.99

### Relative Strength

- ratio: 0.498592
- ratio_MA60: 0.518060
- ratio_gap: -3.76%
- ratio_slope_proxy(20d): -0.012998

### Volume (if available)

- volume: 3130945.00
- volume_MA20: 14299667.25
- volume_ratio: 0.22

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

- close: 5.17
- MA20 / MA60 / MA200: 5.17 / 6.01 / 5.21
- gap20 / gap60: 0.11% / -13.91%
- 5D return: 0.68%
- 20D high/low: 5.58 / 4.87

### Relative Strength

- ratio: 0.013666
- ratio_MA60: 0.014484
- ratio_gap: -5.65%
- ratio_slope_proxy(20d): -0.000779

### Volume (if available)

- volume: 4864159.00
- volume_MA20: 37937197.95
- volume_ratio: 0.13

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

- close: 12.96
- MA20 / MA60 / MA200: 11.67 / 12.39 / 10.65
- gap20 / gap60: 11.09% / 4.59%
- 5D return: 3.43%
- 20D high/low: 13.36 / 10.51

### Relative Strength

- ratio: 0.049927
- ratio_MA60: 0.050389
- ratio_gap: -0.92%
- ratio_slope_proxy(20d): -0.001775

### Volume (if available)

- volume: 3265018.00
- volume_MA20: 12745220.90
- volume_ratio: 0.26

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

- 데이터 기준일(주가): **2026-07-16**
- 실행시간(UTC): **2026-07-16 15:01:07**

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
- 10Y Real Yield 4주 변화: 19.0 bp / latest 2.33
- VIX: 15.67
- NFCI: -0.538

### Leadership ratios
- SILJ/SLV gap: 5.09% / slope_proxy: 0.008917
- GDXJ/GLD gap: -7.22% / slope_proxy: -0.006159

## VZLA (Vizsla Silver)
- close: 3.075 | RSI14: 42.550055 | ATR14%: 6.46%
- MA20 gap: -5.09% | MA50 gap: -10.92% | MA200 gap: -26.64%
- vol_ratio(Volume/Vol20): 0.290211 | gap_open: 0.94%
- RS vs SILJ gap: 5.26% / slope_proxy: 0.005502
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
- close: 5.9988 | RSI14: 37.890948 | ATR14%: 7.57%
- MA20 gap: -8.96% | MA50 gap: -19.63% | MA200 gap: -29.34%
- vol_ratio(Volume/Vol20): 0.316884 | gap_open: 1.73%
- SilverMarginGate: SI=56.369999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -6.25% / slope_proxy: -0.005753
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
- close: 19.145 | RSI14: 32.850461 | ATR14%: 10.36%
- MA20 gap: -15.30% | MA50 gap: -33.83% | MA200 gap: -29.21%
- vol_ratio(Volume/Vol20): 0.288907 | gap_open: 3.02%
- RS vs SILJ gap: -24.58% / slope_proxy: -0.113975
- RS vs GDXJ gap: -24.44% / slope_proxy: -0.025079
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

- 실행시간(UTC): **2026-07-16 15:01:23**
- 데이터 기준일(주가): **2026-07-16**

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

- HY OAS: 2.71 / 4주 변화 0.08 bp-ish / 2026-07-15
- IG OAS: 0.79 / 4주 변화 0.05 bp-ish / 2026-07-15
- 10Y Real Yield: 2.33 / 4주 변화 0.16 bp-ish / 2026-07-14
- VIX: 15.67 / 4주 변화 -2.77 / 2026-07-15
- NFCI: -0.54 / 4주 변화 -0.02 / 2026-07-10

### Leadership ratios

- GDX/GLD: gap -6.12% / slope_proxy -9.84%
- GDXJ/GLD: gap -7.26% / slope_proxy -10.21%
- SILJ/SLV: gap 5.11% / slope_proxy 0.49%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.05 | RSI14: 44.95 | ATR14%: 5.46%
- MA20/50/200 gap: -6.94% / -10.34% / 3.69%
- 5D return: -9.21% | 20D drawdown: -13.35% | vol_ratio: 0.35
- RS vs GDXJ: gap 6.18% / slope_proxy 2.28%
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
- close: 1.87 | RSI14: 75.29 | ATR14%: 7.26%
- MA20/50/200 gap: 9.58% / 2.03% / 6.18%
- 5D return: 3.31% | 20D drawdown: -9.22% | vol_ratio: 0.21
- RS vs GDXJ: gap 22.50% / slope_proxy 31.47%
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

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 4.80 | RSI14: 46.12 | ATR14%: 5.28%
- MA20/50/200 gap: -8.61% / -18.84% / -30.47%
- 5D return: -9.26% | 20D drawdown: -16.52% | vol_ratio: 0.36
- RS vs GDXJ: gap -6.25% / slope_proxy -3.97%
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
- close: 1.06 | RSI14: 42.59 | ATR14%: 7.08%
- MA20/50/200 gap: -10.55% / -17.94% / -29.52%
- 5D return: -10.17% | 20D drawdown: -20.30% | vol_ratio: 0.20
- RS vs GDXJ: gap -3.13% / slope_proxy -11.28%
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
- close: 19.11 | RSI14: 54.37 | ATR14%: 6.75%
- MA20/50/200 gap: -0.91% / 0.27% / 20.31%
- 5D return: -3.82% | 20D drawdown: -5.91% | vol_ratio: 0.29
- RS vs SILJ: gap 19.47% / slope_proxy 12.46%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 14.69 | RSI14: 45.72 | ATR14%: 5.68%
- MA20/50/200 gap: -5.39% / -11.22% / -19.15%
- 5D return: -6.93% | 20D drawdown: -10.72% | vol_ratio: 0.09
- RS vs SILJ: gap 3.24% / slope_proxy 8.77%
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
- close: 3.08 | RSI14: 47.94 | ATR14%: 6.04%
- MA20/50/200 gap: -5.09% / -10.92% / -26.64%
- 5D return: -2.69% | 20D drawdown: -14.11% | vol_ratio: 0.29
- RS vs SILJ: gap 5.26% / slope_proxy 2.11%
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
- close: 7.55 | RSI14: 42.40 | ATR14%: 6.44%
- MA20/50/200 gap: -7.71% / -15.37% / -21.15%
- 5D return: -8.43% | 20D drawdown: -14.84% | vol_ratio: 0.29
- RS vs SILJ: gap -0.67% / slope_proxy 1.23%
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
- close: 6.00 | RSI14: 41.45 | ATR14%: 6.47%
- MA20/50/200 gap: -8.96% / -19.63% / -29.34%
- 5D return: -10.06% | 20D drawdown: -19.91% | vol_ratio: 0.32
- RS vs SILJ: gap -6.25% / slope_proxy -4.79%
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
- close: 3.74 | RSI14: 27.27 | ATR14%: 8.57%
- MA20/50/200 gap: -19.39% / -30.99% / -34.76%
- 5D return: -16.14% | 20D drawdown: -35.07% | vol_ratio: 0.34
- RS vs SILJ: gap -19.04% / slope_proxy -22.81%
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
- close: 5.65 | RSI14: 46.46 | ATR14%: 6.98%
- MA20/50/200 gap: -7.94% / -13.51% / -14.91%
- 5D return: -8.13% | 20D drawdown: -17.28% | vol_ratio: 0.28
- RS vs SILJ: gap 1.73% / slope_proxy -1.66%
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
- close: 19.15 | RSI14: 38.99 | ATR14%: 9.18%
- MA20/50/200 gap: -15.30% / -33.83% / -29.21%
- 5D return: -12.18% | 20D drawdown: -26.39% | vol_ratio: 0.29
- RS vs SILJ: gap -24.58% / slope_proxy -10.99%
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
