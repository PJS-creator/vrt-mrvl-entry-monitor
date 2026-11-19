# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-19 15:01:17**
- 데이터 기준일(일봉): **2026-11-19**
- 데이터 기준일(주봉): **2026-11-16**
- VXN 기준일: **2026-11-18** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **E: 급락 진행/공포, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 671.62
- Weekly RSI14: **44.18**
- 52W MA: 668.05 / gap: **0.53%**
- 104W MA gap: **11.72%**
- 52W MA 13W slope: **4.47%**
- VXN: **33.12** / 5D change: 6.38

## Daily trigger: 실제 매수 타이밍

- QQQ close: 671.62
- Daily RSI14: **43.03**
- 20D gap: **-1.90%**
- 50D gap: **-5.87%**
- 200D gap: **-1.54%**
- MACD hist: -0.5301 / change: 0.9616
- ATR14%: **2.39%**
- 20D high drawdown: **-7.44%**

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

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-19 15:00:57**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.43 / 4주 변화 10.0 bp
- IG OAS (BAMLC0A0CM): 0.92 / 4주 변화 5.0 bp
- 10Y Real Yield (DFII10): 2.89 / 4주 변화 12.0 bp
- VIX (VIXCLS): 24.56
- NFCI: -0.478

## VRT 신규진입 룰
- ratio (VRT/SRVR): 7.270429
- MA60: 8.022816
- gap: -9.38%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.319352
- MA60: 0.398674
- gap: -19.90%
- MA60_slope_proxy: -0.012746
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-19 15:00:59**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **False**
- DemandGreen(monthly): **False**
- MacroGreen: **False**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 135.2 bp / 4주 변화 -24.96 bp
- CURVE_10s5s: 35.2 bp / 4주 변화 -3.78 bp

## NWG Price
- close: 595.6
- MA50: 645.6 / gap50: -7.74%
- MA200: 630.4396 / gap200: -5.53%

## Relative Strength
- RS vs FTSE gap: -7.12% / slope_proxy: -0.002828
- RS vs Peers gap: -0.42% / slope_proxy: 0.003549

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-19 15:01:05**

## Commodity Regime

- WTI ref (CL=F): 83.80 / 5D -5.57%
- Brent ref (BZ=F): 90.62 / 5D -5.43%
- Brent Tier: **>=90**
- Brent-WTI spread: 6.82
- Gas ref (NG=F): 3.37 / 5D 0.87%

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

- close: 54.22
- MA20 / MA60 / MA200: 59.05 / 59.47 / 56.65
- gap20 / gap60: -8.18% / -8.83%
- 5D return: -7.16%
- 20D high/low: 64.17 / 53.76

### Relative Strength

- ratio: 0.883710
- ratio_MA60: 0.920430
- ratio_gap: -3.99%
- ratio_slope_proxy(20d): -0.015540

### Volume (if available)

- volume: 908590.00
- volume_MA20: 10612854.50
- volume_ratio: 0.09

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 16.70
- MA20 / MA60 / MA200: 19.76 / 21.40 / 18.98
- gap20 / gap60: -15.47% / -21.97%
- 5D return: -7.73%
- 20D high/low: 26.16 / 16.70

### Relative Strength

- ratio: 0.557789
- ratio_MA60: 0.578323
- ratio_gap: -3.55%
- ratio_slope_proxy(20d): 0.030712

### Volume (if available)

- volume: 2271105.00
- volume_MA20: 27489470.25
- volume_ratio: 0.08

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.04
- MA20 / MA60 / MA200: 5.73 / 5.66 / 5.90
- gap20 / gap60: -11.97% / -10.93%
- 5D return: -5.26%
- 20D high/low: 6.94 / 5.03

### Relative Strength

- ratio: 0.014176
- ratio_MA60: 0.014439
- ratio_gap: -1.82%
- ratio_slope_proxy(20d): 0.000451

### Volume (if available)

- volume: 2903821.00
- volume_MA20: 39443676.05
- volume_ratio: 0.07

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **False**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **False**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **True**

## VG

- **ENTRY**: **False**

### Trend

- close: 12.27
- MA20 / MA60 / MA200: 12.93 / 13.46 / 12.89
- gap20 / gap60: -5.08% / -8.86%
- 5D return: -7.47%
- 20D high/low: 14.79 / 11.52

### Relative Strength

- ratio: 0.041303
- ratio_MA60: 0.047282
- ratio_gap: -12.64%
- ratio_slope_proxy(20d): -0.002673

### Volume (if available)

- volume: 932024.00
- volume_MA20: 14700546.20
- volume_ratio: 0.06

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

- 데이터 기준일(주가): **2026-11-19**
- 실행시간(UTC): **2026-11-19 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 10.0 bp / latest 3.43
- IG OAS 4주 변화: 5.0 bp / latest 0.92
- 10Y Real Yield 4주 변화: 12.0 bp / latest 2.89
- VIX: 24.56
- NFCI: -0.478

### Leadership ratios
- SILJ/SLV gap: -0.82% / slope_proxy: 0.002616
- GDXJ/GLD gap: -10.47% / slope_proxy: -0.005405

## VZLA (Vizsla Silver)
- close: 2.865 | RSI14: 36.686897 | ATR14%: 6.98%
- MA20 gap: -8.88% | MA50 gap: -16.90% | MA200 gap: -19.21%
- vol_ratio(Volume/Vol20): 0.714703 | gap_open: 6.71%
- RS vs SILJ gap: 4.89% / slope_proxy: 0.002762
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
- close: 6.945 | RSI14: 44.677402 | ATR14%: 8.03%
- MA20 gap: -3.36% | MA50 gap: -14.43% | MA200 gap: -17.04%
- vol_ratio(Volume/Vol20): 0.106891 | gap_open: 0.00%
- SilverMarginGate: SI=45.334999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 7.47% / slope_proxy: 0.005511
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

## HYMC (Hycroft Mining)
- close: 15.3616 | RSI14: 41.076829 | ATR14%: 9.21%
- MA20 gap: -9.07% | MA50 gap: -15.83% | MA200 gap: -45.57%
- vol_ratio(Volume/Vol20): 0.214928 | gap_open: 0.33%
- RS vs SILJ gap: 4.97% / slope_proxy: -0.045266
- RS vs GDXJ gap: 1.50% / slope_proxy: -0.015297
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

- 실행시간(UTC): **2026-11-19 15:01:16**
- 데이터 기준일(주가): **2026-11-19**

## Verdict
**⏸ No confirmed entry; watchlist only**

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

- HY OAS: 3.43 / 4주 변화 0.10 bp-ish / 2026-11-17
- IG OAS: 0.92 / 4주 변화 0.05 bp-ish / 2026-11-17
- 10Y Real Yield: 2.89 / 4주 변화 0.09 bp-ish / 2026-11-17
- VIX: 24.56 / 4주 변화 7.88 / 2026-11-18
- NFCI: -0.48 / 4주 변화 0.03 / 2026-11-13

### Leadership ratios

- GDX/GLD: gap -5.70% / slope_proxy 0.01%
- GDXJ/GLD: gap -10.47% / slope_proxy -2.93%
- SILJ/SLV: gap -0.80% / slope_proxy 5.95%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 0.00%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 6.51 | RSI14: 36.24 | ATR14%: 6.74%
- MA20/50/200 gap: -14.54% / -25.30% / -19.73%
- 5D return: -14.34% | 20D drawdown: -22.50% | vol_ratio: 0.25
- RS vs GDXJ: gap -8.47% / slope_proxy -9.27%
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
- close: 3.63 | RSI14: 28.14 | ATR14%: 11.00%
- MA20/50/200 gap: -28.83% / -42.44% / -45.82%
- 5D return: -28.68% | 20D drawdown: -38.37% | vol_ratio: 0.20
- RS vs GDXJ: gap -29.83% / slope_proxy -26.69%
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
- close: 0.58 | RSI14: 28.26 | ATR14%: 11.45%
- MA20/50/200 gap: -25.83% / -42.02% / -56.62%
- 5D return: -26.58% | 20D drawdown: -35.56% | vol_ratio: 0.34
- RS vs GDXJ: gap -31.92% / slope_proxy -23.30%
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
- close: 1.30 | RSI14: 38.38 | ATR14%: 9.78%
- MA20/50/200 gap: -19.08% / -35.87% / -33.11%
- 5D return: -17.20% | 20D drawdown: -27.78% | vol_ratio: 0.33
- RS vs GDXJ: gap -22.58% / slope_proxy -17.48%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.95 | RSI14: 51.50 | ATR14%: 8.44%
- MA20/50/200 gap: -3.36% / -14.43% / -17.04%
- 5D return: -1.49% | 20D drawdown: -14.15% | vol_ratio: 0.11
- RS vs SILJ: gap 7.45% / slope_proxy 12.16%
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
- close: 2.87 | RSI14: 43.21 | ATR14%: 7.23%
- MA20/50/200 gap: -8.88% / -16.90% / -19.21%
- 5D return: -8.17% | 20D drawdown: -18.14% | vol_ratio: 0.71
- RS vs SILJ: gap 4.86% / slope_proxy 4.07%
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

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 19.92 | RSI14: 39.35 | ATR14%: 7.94%
- MA20/50/200 gap: -15.71% / -22.49% / -6.09%
- 5D return: -12.86% | 20D drawdown: -25.59% | vol_ratio: 0.15
- RS vs SILJ: gap -1.46% / slope_proxy -5.94%
- FundamentalScore: 86 | TechnicalScore: 15 | RegimeScore: 30 | OverallScore: **50.0**
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
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 6.42 | RSI14: 40.20 | ATR14%: 7.74%
- MA20/50/200 gap: -14.70% / -23.25% / -31.73%
- 5D return: -18.01% | 20D drawdown: -23.02% | vol_ratio: 0.13
- RS vs SILJ: gap -4.78% / slope_proxy -3.54%
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
- close: 11.57 | RSI14: 37.66 | ATR14%: 7.49%
- MA20/50/200 gap: -15.69% / -26.51% / -34.73%
- 5D return: -13.33% | 20D drawdown: -24.92% | vol_ratio: 0.07
- RS vs SILJ: gap -8.55% / slope_proxy -6.24%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 2.15 | RSI14: 33.33 | ATR14%: 11.26%
- MA20/50/200 gap: -23.96% / -42.87% / -59.70%
- 5D return: -22.95% | 20D drawdown: -34.66% | vol_ratio: 0.10
- RS vs SILJ: gap -29.46% / slope_proxy -21.40%
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

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 15.37 | RSI14: 46.06 | ATR14%: 10.60%
- MA20/50/200 gap: -9.02% / -15.78% / -45.54%
- 5D return: -9.59% | 20D drawdown: -27.74% | vol_ratio: 0.21
- RS vs SILJ: gap 5.00% / slope_proxy 11.73%
- FundamentalScore: 42 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **38.9**
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
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, SilverMinerLeadership(SILJ/SLV)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 3.79 | RSI14: 38.30 | ATR14%: 7.43%
- MA20/50/200 gap: -14.85% / -26.77% / -42.14%
- 5D return: -13.86% | 20D drawdown: -22.81% | vol_ratio: 0.10
- RS vs SILJ: gap -10.36% / slope_proxy -8.32%
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

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
