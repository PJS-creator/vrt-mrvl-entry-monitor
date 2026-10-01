# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-10-01 03:01:09**
- 데이터 기준일(일봉): **2026-09-30**
- 데이터 기준일(주봉): **2026-09-28**
- VXN 기준일: **2026-09-29** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 739.77
- Weekly RSI14: **62.27**
- 52W MA: 655.65 / gap: **12.83%**
- 104W MA gap: **25.92%**
- 52W MA 13W slope: **5.77%**
- VXN: **22.07** / 5D change: 1.89

## Daily trigger: 실제 매수 타이밍

- QQQ close: 739.77
- Daily RSI14: **60.46**
- 20D gap: **2.16%**
- 50D gap: **3.56%**
- 200D gap: **11.10%**
- MACD hist: 1.8278 / change: -0.4035
- ATR14%: **1.26%**
- 20D high drawdown: **-1.03%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
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

- 데이터 기준일(주가): **2026-09-30**
- 실행시간(UTC): **2026-10-01 03:00:44**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.08 / 4주 변화 43.0 bp
- IG OAS (BAMLC0A0CM): 0.84 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.91 / 4주 변화 47.0 bp
- VIX (VIXCLS): 16.04
- NFCI: -0.548

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.517826
- MA60: 8.892649
- gap: -4.21%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.433842
- MA60: 0.389198
- gap: 11.47%
- MA60_slope_proxy: -0.010541
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-30**
- 실행시간(UTC): **2026-10-01 03:00:47**

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
- TERM_SPREAD_10Y_POLICY: 163.29 bp / 4주 변화 31.98 bp
- CURVE_10s5s: 41.33 bp / 4주 변화 -5.63 bp

## NWG Price
- close: 688.0
- MA50: 693.3563 / gap50: -0.77%
- MA200: 634.3417 / gap200: 8.46%

## Relative Strength
- RS vs FTSE gap: 0.89% / slope_proxy: 0.001081
- RS vs Peers gap: 2.81% / slope_proxy: 0.008321

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-10-01 03:00:54**

## Commodity Regime

- WTI ref (CL=F): 89.85 / 5D -2.51%
- Brent ref (BZ=F): 97.53 / 5D -5.38%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.68
- Gas ref (NG=F): 2.99 / 5D -1.06%

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

- close: 55.32
- MA20 / MA60 / MA200: 58.99 / 57.48 / 53.41
- gap20 / gap60: -6.22% / -3.75%
- 5D return: -3.56%
- 20D high/low: 63.52 / 54.94

### Relative Strength

- ratio: 0.899512
- ratio_MA60: 0.945980
- ratio_gap: -4.91%
- ratio_slope_proxy(20d): -0.009237

### Volume (if available)

- volume: 10167500.00
- volume_MA20: 9005955.00
- volume_ratio: 1.13

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 20.87
- MA20 / MA60 / MA200: 20.87 / 18.88 / 17.24
- gap20 / gap60: 0.02% / 10.51%
- 5D return: -1.28%
- 20D high/low: 21.77 / 20.12

### Relative Strength

- ratio: 0.560268
- ratio_MA60: 0.521870
- ratio_gap: 7.36%
- ratio_slope_proxy(20d): 0.024413

### Volume (if available)

- volume: 25287500.00
- volume_MA20: 21602965.00
- volume_ratio: 1.17

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.24
- MA20 / MA60 / MA200: 5.61 / 5.50 / 5.67
- gap20 / gap60: -6.58% / -4.79%
- 5D return: -4.20%
- 20D high/low: 6.22 / 5.21

### Relative Strength

- ratio: 0.013849
- ratio_MA60: 0.013760
- ratio_gap: 0.65%
- ratio_slope_proxy(20d): -0.000010

### Volume (if available)

- volume: 26621300.00
- volume_MA20: 44899455.00
- volume_ratio: 0.59

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

- close: 12.64
- MA20 / MA60 / MA200: 14.10 / 13.77 / 11.94
- gap20 / gap60: -10.37% / -8.22%
- 5D return: -4.75%
- 20D high/low: 15.76 / 12.54

### Relative Strength

- ratio: 0.046984
- ratio_MA60: 0.050991
- ratio_gap: -7.86%
- ratio_slope_proxy(20d): 0.000934

### Volume (if available)

- volume: 9239900.00
- volume_MA20: 14810340.00
- volume_ratio: 0.62

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **True**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-30**
- 실행시간(UTC): **2026-10-01 03:00:59**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 43.0 bp / latest 3.08
- IG OAS 4주 변화: 3.0 bp / latest 0.84
- 10Y Real Yield 4주 변화: 47.0 bp / latest 2.91
- VIX: 16.04
- NFCI: -0.548

### Leadership ratios
- SILJ/SLV gap: 0.26% / slope_proxy: 0.016124
- GDXJ/GLD gap: 2.79% / slope_proxy: 0.014092

## VZLA (Vizsla Silver)
- close: 3.79 | RSI14: 45.636075 | ATR14%: 5.25%
- MA20 gap: -4.70% | MA50 gap: 0.24% | MA200 gap: -5.07%
- vol_ratio(Volume/Vol20): 0.917025 | gap_open: 0.52%
- RS vs SILJ gap: 7.44% / slope_proxy: 0.002063
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
- close: 8.83 | RSI14: 47.225303 | ATR14%: 7.16%
- MA20 gap: -5.73% | MA50 gap: 1.52% | MA200 gap: -1.90%
- vol_ratio(Volume/Vol20): 0.456118 | gap_open: 0.84%
- SilverMarginGate: SI=61.165001 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 11.56% / slope_proxy: 0.019856
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

## HYMC (Hycroft Mining)
- close: 19.040001 | RSI14: 38.03758 | ATR14%: 8.12%
- MA20 gap: -10.74% | MA50 gap: -16.91% | MA200 gap: -38.08%
- vol_ratio(Volume/Vol20): 1.124749 | gap_open: 1.29%
- RS vs SILJ gap: -12.08% / slope_proxy: -0.06663
- RS vs GDXJ gap: -15.52% / slope_proxy: -0.021252
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

- 실행시간(UTC): **2026-10-01 03:01:08**
- 데이터 기준일(주가): **2026-09-30**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **True**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **False**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **False**

### Macro (FRED, if available)

- HY OAS: 3.08 / 4주 변화 0.43 bp-ish / 2026-09-29
- IG OAS: 0.84 / 4주 변화 0.03 bp-ish / 2026-09-29
- 10Y Real Yield: 2.91 / 4주 변화 0.47 bp-ish / 2026-09-29
- VIX: 16.04 / 4주 변화 -0.30 / 2026-09-29
- NFCI: -0.55 / 4주 변화 -0.04 / 2026-09-25

### Leadership ratios

- GDX/GLD: gap 2.93% / slope_proxy -4.89%
- GDXJ/GLD: gap 2.79% / slope_proxy -5.88%
- SILJ/SLV: gap 0.26% / slope_proxy -6.57%
- Gold breadth proxy: above50 7.69%, above200 30.77%, count 13
- Silver breadth proxy: above50 30.77%, above200 15.38%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 9.39 | RSI14: 42.71 | ATR14%: 4.86%
- MA20/50/200 gap: -6.58% / -0.92% / 20.36%
- 5D return: -6.75% | 20D drawdown: -10.91% | vol_ratio: 0.50
- RS vs GDXJ: gap 3.97% / slope_proxy 6.69%
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
- close: 7.06 | RSI14: 32.68 | ATR14%: 5.06%
- MA20/50/200 gap: -8.52% / -0.16% / -0.36%
- 5D return: -8.31% | 20D drawdown: -15.35% | vol_ratio: 0.46
- RS vs GDXJ: gap 5.92% / slope_proxy 3.30%
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.06 | RSI14: 24.69 | ATR14%: 8.76%
- MA20/50/200 gap: -23.58% / -23.85% / -28.72%
- 5D return: -17.19% | 20D drawdown: -33.75% | vol_ratio: 1.06
- RS vs GDXJ: gap -20.73% / slope_proxy -22.15%
- FundamentalScore: 70 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **48.0**
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
- close: 2.27 | RSI14: 34.04 | ATR14%: 6.17%
- MA20/50/200 gap: -11.88% / -3.58% / 14.02%
- 5D return: -13.36% | 20D drawdown: -18.64% | vol_ratio: 1.18
- RS vs GDXJ: gap 0.61% / slope_proxy -8.57%
- FundamentalScore: 55 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **41.2**
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
- close: 26.90 | RSI14: 43.60 | ATR14%: 6.02%
- MA20/50/200 gap: -4.67% / 2.85% / 36.94%
- 5D return: -4.58% | 20D drawdown: -11.45% | vol_ratio: 0.67
- RS vs SILJ: gap 12.50% / slope_proxy 10.05%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.83 | RSI14: 42.24 | ATR14%: 7.50%
- MA20/50/200 gap: -5.73% / 1.52% / -1.90%
- 5D return: -0.56% | 20D drawdown: -15.34% | vol_ratio: 0.46
- RS vs SILJ: gap 11.56% / slope_proxy 0.60%
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
- close: 3.79 | RSI14: 43.05 | ATR14%: 5.47%
- MA20/50/200 gap: -4.70% / 0.24% / -5.07%
- 5D return: -6.19% | 20D drawdown: -11.86% | vol_ratio: 0.92
- RS vs SILJ: gap 7.44% / slope_proxy 5.92%
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

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.03 | RSI14: 28.85 | ATR14%: 5.55%
- MA20/50/200 gap: -10.39% / -6.37% / -11.31%
- 5D return: -6.79% | 20D drawdown: -19.71% | vol_ratio: 1.01
- RS vs SILJ: gap 0.55% / slope_proxy -4.90%
- FundamentalScore: 78 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **51.6**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.58 | RSI14: 28.54 | ATR14%: 6.66%
- MA20/50/200 gap: -14.50% / -11.95% / -13.75%
- 5D return: -7.34% | 20D drawdown: -25.20% | vol_ratio: 0.91
- RS vs SILJ: gap -4.91% / slope_proxy -10.59%
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

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 4.36 | RSI14: 36.53 | ATR14%: 7.01%
- MA20/50/200 gap: -12.20% / -10.63% / -26.09%
- 5D return: -10.10% | 20D drawdown: -21.30% | vol_ratio: 0.87
- RS vs SILJ: gap -4.08% / slope_proxy -6.87%
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
- close: 5.55 | RSI14: 24.76 | ATR14%: 6.46%
- MA20/50/200 gap: -14.05% / -15.79% / -20.88%
- 5D return: -8.11% | 20D drawdown: -27.83% | vol_ratio: 0.55
- RS vs SILJ: gap -10.56% / slope_proxy -14.17%
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
- close: 19.04 | RSI14: 39.39 | ATR14%: 7.59%
- MA20/50/200 gap: -10.74% / -16.91% / -38.08%
- 5D return: -10.44% | 20D drawdown: -18.28% | vol_ratio: 1.12
- RS vs SILJ: gap -12.08% / slope_proxy -4.86%
- FundamentalScore: 42 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **35.4**
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
