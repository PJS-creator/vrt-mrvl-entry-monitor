# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA, EXK, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-07-23 15:01:32**
- 데이터 기준일(일봉): **2026-07-23**
- 데이터 기준일(주봉): **2026-07-20**
- VXN 기준일: **2026-07-22** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 691.06
- Weekly RSI14: **55.06**
- 52W MA: 628.96 / gap: **9.87%**
- 104W MA gap: **22.60%**
- 52W MA 13W slope: **7.86%**
- VXN: **26.74** / 5D change: 1.09

## Daily trigger: 실제 매수 타이밍

- QQQ close: 691.06
- Daily RSI14: **41.58**
- 20D gap: **-3.11%**
- 50D gap: **-3.79%**
- 200D gap: **7.72%**
- MACD hist: -2.7438 / change: -0.5643
- ATR14%: **2.06%**
- 20D high drawdown: **-6.16%**

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

- 데이터 기준일(주가): **2026-07-23**
- 실행시간(UTC): **2026-07-23 15:00:50**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.68 / 4주 변화 -8.0 bp
- IG OAS (BAMLC0A0CM): 0.78 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.37 / 4주 변화 8.0 bp
- VIX (VIXCLS): 16.64
- NFCI: -0.552

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.806145
- MA60: 9.657942
- gap: 1.53%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.359761
- MA60: 0.382143
- gap: -5.86%
- MA60_slope_proxy: 0.03199
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-07-23**
- 실행시간(UTC): **2026-07-23 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 127.1 bp / 4주 변화 28.88 bp
- CURVE_10s5s: 47.57 bp / 4주 변화 2.38 bp

## NWG Price
- close: 673.8
- MA50: 630.176 / gap50: 6.92%
- MA200: 609.4852 / gap200: 10.55%

## Relative Strength
- RS vs FTSE gap: 6.60% / slope_proxy: 0.002187
- RS vs Peers gap: -0.11% / slope_proxy: -0.003253

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-07-23 15:01:03**

## Commodity Regime

- WTI ref (CL=F): 92.01 / 5D 16.54%
- Brent ref (BZ=F): 87.06 / 5D 3.36%
- Brent Tier: **80-90**
- Brent-WTI spread: -4.95
- Gas ref (NG=F): 2.94 / 5D 3.01%

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

- close: 58.50
- MA20 / MA60 / MA200: 52.72 / 55.34 / 49.53
- gap20 / gap60: 10.97% / 5.70%
- 5D return: 9.04%
- 20D high/low: 58.50 / 47.94

### Relative Strength

- ratio: 0.972003
- ratio_MA60: 0.975736
- ratio_gap: -0.38%
- ratio_slope_proxy(20d): -0.026517

### Volume (if available)

- volume: 2332451.00
- volume_MA20: 9184267.55
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

- close: 19.25
- MA20 / MA60 / MA200: 17.29 / 18.53 / 15.90
- gap20 / gap60: 11.33% / 3.86%
- 5D return: 10.19%
- 20D high/low: 19.25 / 15.99

### Relative Strength

- ratio: 0.528991
- ratio_MA60: 0.517553
- ratio_gap: 2.21%
- ratio_slope_proxy(20d): -0.009702

### Volume (if available)

- volume: 2244405.00
- volume_MA20: 14121970.25
- volume_ratio: 0.16

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **False**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.38
- MA20 / MA60 / MA200: 5.14 / 5.93 / 5.26
- gap20 / gap60: 4.60% / -9.38%
- 5D return: 4.98%
- 20D high/low: 5.38 / 4.87

### Relative Strength

- ratio: 0.013735
- ratio_MA60: 0.014410
- ratio_gap: -4.69%
- ratio_slope_proxy(20d): -0.000632

### Volume (if available)

- volume: 11005500.00
- volume_MA20: 37634125.00
- volume_ratio: 0.29

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 15.31
- MA20 / MA60 / MA200: 12.51 / 12.57 / 10.65
- gap20 / gap60: 22.35% / 21.82%
- 5D return: 20.84%
- 20D high/low: 15.31 / 10.83

### Relative Strength

- ratio: 0.056176
- ratio_MA60: 0.050922
- ratio_gap: 10.32%
- ratio_slope_proxy(20d): -0.000431

### Volume (if available)

- volume: 7789834.00
- volume_MA20: 13908661.70
- volume_ratio: 0.56

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

- 데이터 기준일(주가): **2026-07-23**
- 실행시간(UTC): **2026-07-23 15:01:11**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -8.0 bp / latest 2.68
- IG OAS 4주 변화: 3.0 bp / latest 0.78
- 10Y Real Yield 4주 변화: 8.0 bp / latest 2.37
- VIX: 16.64
- NFCI: -0.552

### Leadership ratios
- SILJ/SLV gap: 4.44% / slope_proxy: 0.008225
- GDXJ/GLD gap: -3.77% / slope_proxy: -0.008787

## VZLA (Vizsla Silver)
- close: 3.255 | RSI14: 49.43917 | ATR14%: 6.01%
- MA20 gap: 1.93% | MA50 gap: -5.03% | MA200 gap: -21.80%
- vol_ratio(Volume/Vol20): 0.351376 | gap_open: 3.51%
- RS vs SILJ gap: 6.90% / slope_proxy: 0.006192
- Checks:
  - trend_ok: **False**
  - rs_ok: **True**
  - risk_ok: **True**
  - triggers: pullback=True, breakout=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- SilverUptrend=FALSE
- Trend(MA200/MA50)=FALSE

## SCZM (Santacruz Silver)
- close: 6.32 | RSI14: 45.25345 | ATR14%: 6.99%
- MA20 gap: -1.79% | MA50 gap: -12.46% | MA200 gap: -25.24%
- vol_ratio(Volume/Vol20): 0.316632 | gap_open: 2.37%
- SilverMarginGate: SI=58.185001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.16% / slope_proxy: -0.005749
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
- close: 20.110001 | RSI14: 40.928826 | ATR14%: 9.37%
- MA20 gap: -6.51% | MA50 gap: -25.53% | MA200 gap: -26.57%
- vol_ratio(Volume/Vol20): 0.210517 | gap_open: 5.62%
- RS vs SILJ gap: -20.04% / slope_proxy: -0.127416
- RS vs GDXJ gap: -21.39% / slope_proxy: -0.028579
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

- 실행시간(UTC): **2026-07-23 15:01:29**
- 데이터 기준일(주가): **2026-07-23**

## Verdict
**🟡 Precious miners watch/add-on candidates: AYA, EXK, HL**

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

- HY OAS: 2.68 / 4주 변화 -0.08 bp-ish / 2026-07-22
- IG OAS: 0.78 / 4주 변화 0.03 bp-ish / 2026-07-22
- 10Y Real Yield: 2.37 / 4주 변화 0.09 bp-ish / 2026-07-21
- VIX: 16.64 / 4주 변화 -1.99 / 2026-07-22
- NFCI: -0.55 / 4주 변화 -0.05 / 2026-07-17

### Leadership ratios

- GDX/GLD: gap -2.98% / slope_proxy -1.99%
- GDXJ/GLD: gap -3.78% / slope_proxy -1.52%
- SILJ/SLV: gap 4.45% / slope_proxy -3.05%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 7.69%, above200 7.69%, count 13

---

## Gold miners

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.94 | RSI14: 61.62 | ATR14%: 7.62%
- MA20/50/200 gap: 9.08% / 5.93% / 8.40%
- 5D return: 6.59% | 20D drawdown: -5.83% | vol_ratio: 0.57
- RS vs GDXJ: gap 18.65% / slope_proxy 29.65%
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

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.03 | RSI14: 39.23 | ATR14%: 5.28%
- MA20/50/200 gap: -4.37% / -9.41% / 3.05%
- 5D return: 1.37% | 20D drawdown: -11.06% | vol_ratio: 0.17
- RS vs GDXJ: gap 0.32% / slope_proxy -3.01%
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
- close: 5.24 | RSI14: 36.55 | ATR14%: 4.86%
- MA20/50/200 gap: 0.88% / -8.60% / -23.94%
- 5D return: 8.39% | 20D drawdown: -8.96% | vol_ratio: 0.37
- RS vs GDXJ: gap -1.44% / slope_proxy 4.39%
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
- close: 1.11 | RSI14: 29.47 | ATR14%: 6.11%
- MA20/50/200 gap: -3.22% / -11.87% / -26.00%
- 5D return: 5.24% | 20D drawdown: -15.00% | vol_ratio: 0.12
- RS vs GDXJ: gap -3.61% / slope_proxy -5.78%
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
- close: 19.50 | RSI14: 49.43 | ATR14%: 6.68%
- MA20/50/200 gap: 0.76% / 1.94% / 21.34%
- 5D return: 4.00% | 20D drawdown: -6.70% | vol_ratio: 0.58
- RS vs SILJ: gap 15.47% / slope_proxy 10.34%
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
- close: 7.89 | RSI14: 41.68 | ATR14%: 5.99%
- MA20/50/200 gap: -2.08% / -9.50% / -17.62%
- 5D return: 5.27% | 20D drawdown: -7.89% | vol_ratio: 0.35
- RS vs SILJ: gap 0.83% / slope_proxy 1.45%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **56.9**
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
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 15.15 | RSI14: 40.45 | ATR14%: 5.43%
- MA20/50/200 gap: -1.54% / -6.47% / -17.00%
- 5D return: 4.30% | 20D drawdown: -7.99% | vol_ratio: 0.11
- RS vs SILJ: gap 3.54% / slope_proxy 3.41%
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
- close: 3.26 | RSI14: 47.25 | ATR14%: 5.71%
- MA20/50/200 gap: 1.93% / -5.03% / -21.80%
- 5D return: 6.03% | 20D drawdown: -4.82% | vol_ratio: 0.35
- RS vs SILJ: gap 6.90% / slope_proxy 7.57%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.32 | RSI14: 44.57 | ATR14%: 6.43%
- MA20/50/200 gap: -1.79% / -12.46% / -25.24%
- 5D return: 5.69% | 20D drawdown: -7.20% | vol_ratio: 0.32
- RS vs SILJ: gap -3.16% / slope_proxy 1.51%
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
- close: 4.02 | RSI14: 33.33 | ATR14%: 7.68%
- MA20/50/200 gap: -7.32% / -22.29% / -29.93%
- 5D return: 7.49% | 20D drawdown: -17.79% | vol_ratio: 0.69
- RS vs SILJ: gap -14.07% / slope_proxy -13.19%
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
- close: 5.70 | RSI14: 38.29 | ATR14%: 7.15%
- MA20/50/200 gap: -5.37% / -11.37% / -14.38%
- 5D return: 3.36% | 20D drawdown: -13.45% | vol_ratio: 0.50
- RS vs SILJ: gap -0.46% / slope_proxy 0.53%
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
- close: 20.11 | RSI14: 38.68 | ATR14%: 8.47%
- MA20/50/200 gap: -6.51% / -25.53% / -26.57%
- 5D return: 9.09% | 20D drawdown: -15.29% | vol_ratio: 0.21
- RS vs SILJ: gap -20.04% / slope_proxy -4.97%
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
