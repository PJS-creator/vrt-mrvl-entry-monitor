# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **⏸ No confirmed entry; watchlist only**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-08-20 15:01:29**
- 데이터 기준일(일봉): **2026-08-20**
- 데이터 기준일(주봉): **2026-08-17**
- VXN 기준일: **2026-08-19** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 713.68
- Weekly RSI14: **57.62**
- 52W MA: 640.16 / gap: **11.49%**
- 104W MA gap: **24.46%**
- 52W MA 13W slope: **6.91%**
- VXN: **22.04** / 5D change: 1.07

## Daily trigger: 실제 매수 타이밍

- QQQ close: 713.64
- Daily RSI14: **50.18**
- 20D gap: **0.82%**
- 50D gap: **0.09%**
- 200D gap: **9.57%**
- MACD hist: 0.7314 / change: -0.9311
- ATR14%: **1.61%**
- 20D high drawdown: **-2.52%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
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

- 데이터 기준일(주가): **2026-08-20**
- 실행시간(UTC): **2026-08-20 15:00:49**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.73 / 4주 변화 5.0 bp
- IG OAS (BAMLC0A0CM): 0.81 / 4주 변화 3.0 bp
- 10Y Real Yield (DFII10): 2.41 / 4주 변화 4.0 bp
- VIX (VIXCLS): 14.89
- NFCI: -0.559

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.185797
- MA60: 9.253966
- gap: -11.54%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.433887
- MA60: 0.399239
- gap: 8.68%
- MA60_slope_proxy: 0.017079
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-08-20**
- 실행시간(UTC): **2026-08-20 15:00:54**

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
- TERM_SPREAD_10Y_POLICY: 131.76 bp / 4주 변화 4.66 bp
- CURVE_10s5s: 49.46 bp / 4주 변화 1.89 bp

## NWG Price
- close: 679.8
- MA50: 674.5088 / gap50: 0.78%
- MA200: 623.2963 / gap200: 9.07%

## Relative Strength
- RS vs FTSE gap: 2.12% / slope_proxy: 0.003007
- RS vs Peers gap: 1.38% / slope_proxy: 0.015879

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-08-20 15:01:02**

## Commodity Regime

- WTI ref (CL=F): 86.19 / 5D 6.08%
- Brent ref (BZ=F): 93.32 / 5D 7.18%
- Brent Tier: **>=90**
- Brent-WTI spread: 7.13
- Gas ref (NG=F): 2.73 / 5D -0.04%

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

- close: 61.79
- MA20 / MA60 / MA200: 57.23 / 55.18 / 51.09
- gap20 / gap60: 7.97% / 11.98%
- 5D return: 7.09%
- 20D high/low: 61.79 / 53.81

### Relative Strength

- ratio: 0.958653
- ratio_MA60: 0.962330
- ratio_gap: -0.38%
- ratio_slope_proxy(20d): -0.013373

### Volume (if available)

- volume: 2951693.00
- volume_MA20: 8143799.65
- volume_ratio: 0.36

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 19.16
- MA20 / MA60 / MA200: 18.42 / 17.84 / 16.57
- gap20 / gap60: 3.98% / 7.41%
- 5D return: 7.09%
- 20D high/low: 19.40 / 17.76

### Relative Strength

- ratio: 0.556197
- ratio_MA60: 0.510927
- ratio_gap: 8.86%
- ratio_slope_proxy(20d): -0.006663

### Volume (if available)

- volume: 6714171.00
- volume_MA20: 14934778.55
- volume_ratio: 0.45

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

- close: 6.01
- MA20 / MA60 / MA200: 5.46 / 5.49 / 5.46
- gap20 / gap60: 10.21% / 9.52%
- 5D return: 5.16%
- 20D high/low: 6.01 / 4.95

### Relative Strength

- ratio: 0.014290
- ratio_MA60: 0.013918
- ratio_gap: 2.67%
- ratio_slope_proxy(20d): -0.000525

### Volume (if available)

- volume: 11658515.00
- volume_MA20: 45187955.75
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- OIL_TREND_UP: **True**
- OIH_TREND_UP: **False**
- RIG_BREAKOUT: **True**
- RIG_VOLUME_CONFIRM: **False**
- RIG_RELATIVE_OK: **False**

## VG

- **ENTRY**: **False**

### Trend

- close: 14.35
- MA20 / MA60 / MA200: 13.45 / 12.69 / 11.01
- gap20 / gap60: 6.66% / 13.01%
- 5D return: 5.95%
- 20D high/low: 14.35 / 12.17

### Relative Strength

- ratio: 0.051686
- ratio_MA60: 0.050636
- ratio_gap: 2.07%
- ratio_slope_proxy(20d): -0.000280

### Volume (if available)

- volume: 4950405.00
- volume_MA20: 13767680.25
- volume_ratio: 0.36

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-08-20**
- 실행시간(UTC): **2026-08-20 15:01:09**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: 5.0 bp / latest 2.73
- IG OAS 4주 변화: 3.0 bp / latest 0.81
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.41
- VIX: 14.89
- NFCI: -0.559

### Leadership ratios
- SILJ/SLV gap: 9.16% / slope_proxy: 0.019778
- GDXJ/GLD gap: 14.68% / slope_proxy: 0.00049

## VZLA (Vizsla Silver)
- close: 3.955 | RSI14: 64.168678 | ATR14%: 4.72%
- MA20 gap: 11.56% | MA50 gap: 16.69% | MA200 gap: -2.95%
- vol_ratio(Volume/Vol20): 0.273738 | gap_open: 1.54%
- RS vs SILJ gap: -2.83% / slope_proxy: 0.004415
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

## SCZM (Santacruz Silver)
- close: 9.93 | RSI14: 73.573685 | ATR14%: 5.40%
- MA20 gap: 25.74% | MA50 gap: 39.62% | MA200 gap: 15.61%
- vol_ratio(Volume/Vol20): 0.570788 | gap_open: 0.94%
- SilverMarginGate: SI=68.010002 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 17.37% / slope_proxy: 0.000766
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
- close: 27.5 | RSI14: 59.784001 | ATR14%: 6.88%
- MA20 gap: 14.79% | MA50 gap: 18.58% | MA200 gap: -5.25%
- vol_ratio(Volume/Vol20): 0.358094 | gap_open: 2.33%
- RS vs SILJ gap: -4.09% / slope_proxy: -0.118983
- RS vs GDXJ gap: -7.94% / slope_proxy: -0.031983
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

- 실행시간(UTC): **2026-08-20 15:01:26**
- 데이터 기준일(주가): **2026-08-20**

## Verdict
**⏸ No confirmed entry; watchlist only**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **True**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.73 / 4주 변화 0.05 bp-ish / 2026-08-19
- IG OAS: 0.81 / 4주 변화 0.03 bp-ish / 2026-08-19
- 10Y Real Yield: 2.41 / 4주 변화 0.04 bp-ish / 2026-08-18
- VIX: 14.89 / 4주 변화 -1.75 / 2026-08-19
- NFCI: -0.56 / 4주 변화 -0.10 / 2026-08-14

### Leadership ratios

- GDX/GLD: gap 15.27% / slope_proxy 18.74%
- GDXJ/GLD: gap 14.76% / slope_proxy 18.58%
- SILJ/SLV: gap 9.18% / slope_proxy 9.59%
- Gold breadth proxy: above50 100.00%, above200 84.62%, count 13
- Silver breadth proxy: above50 100.00%, above200 69.23%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.35 | RSI14: 80.85 | ATR14%: 5.72%
- MA20/50/200 gap: 18.97% / 29.69% / 45.84%
- 5D return: 6.21% | 20D drawdown: -0.43% | vol_ratio: 0.16
- RS vs GDXJ: gap 5.50% / slope_proxy 9.58%
- FundamentalScore: 88 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **77.1**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.49 | RSI14: 89.65 | ATR14%: 4.52%
- MA20/50/200 gap: 19.27% / 30.69% / 8.72%
- 5D return: 7.07% | 20D drawdown: 0.00% | vol_ratio: 0.90
- RS vs GDXJ: gap 5.36% / slope_proxy 7.44%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **74.4**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.65 | RSI14: 87.14 | ATR14%: 5.26%
- MA20/50/200 gap: 22.45% / 30.56% / 11.14%
- 5D return: 15.38% | 20D drawdown: 0.00% | vol_ratio: 0.54
- RS vs GDXJ: gap 6.34% / slope_proxy 11.51%
- FundamentalScore: 70 | TechnicalScore: 50 | RegimeScore: 100 | OverallScore: **69.0**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.42 | RSI14: 73.45 | ATR14%: 5.95%
- MA20/50/200 gap: 17.99% / 32.15% / 31.02%
- 5D return: 14.93% | 20D drawdown: -1.42% | vol_ratio: 0.29
- RS vs GDXJ: gap 6.74% / slope_proxy -3.33%
- FundamentalScore: 55 | TechnicalScore: 25 | RegimeScore: 100 | OverallScore: **53.5**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 27.52 | RSI14: 73.29 | ATR14%: 6.13%
- MA20/50/200 gap: 13.92% / 30.46% / 59.48%
- 5D return: 2.15% | 20D drawdown: -1.85% | vol_ratio: 0.40
- RS vs SILJ: gap 12.75% / slope_proxy 7.45%
- FundamentalScore: 86 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **71.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Zgounder 생산/현금흐름, 5Moz+ 규모, 모로코 관할권. 프리미엄 밸류 주의.
- Watch: Zgounder cash cost, Boumadine PEA/FS, 밸류에이션 과열.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 11.28 | RSI14: 78.40 | ATR14%: 5.78%
- MA20/50/200 gap: 22.46% / 31.29% / 16.80%
- 5D return: 9.41% | 20D drawdown: 0.00% | vol_ratio: 0.54
- RS vs SILJ: gap 10.35% / slope_proxy 12.08%
- FundamentalScore: 82 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **69.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.97 | RSI14: 82.03 | ATR14%: 5.05%
- MA20/50/200 gap: 25.19% / 31.35% / 12.66%
- 5D return: 18.25% | 20D drawdown: 0.00% | vol_ratio: 0.16
- RS vs SILJ: gap 10.57% / slope_proxy 7.59%
- FundamentalScore: 78 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **67.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.93 | RSI14: 83.95 | ATR14%: 5.85%
- MA20/50/200 gap: 25.74% / 39.27% / 15.50%
- 5D return: 13.88% | 20D drawdown: 0.00% | vol_ratio: 0.57
- RS vs SILJ: gap 17.54% / slope_proxy 22.66%
- FundamentalScore: 74 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **65.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.79 | RSI14: 78.34 | ATR14%: 5.65%
- MA20/50/200 gap: 20.51% / 24.61% / 15.11%
- 5D return: 12.73% | 20D drawdown: 0.00% | vol_ratio: 0.55
- RS vs SILJ: gap 4.39% / slope_proxy 7.51%
- FundamentalScore: 60 | TechnicalScore: 50 | RegimeScore: 75 | OverallScore: **59.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.96 | RSI14: 73.99 | ATR14%: 4.76%
- MA20/50/200 gap: 11.52% / 16.68% / -3.04%
- 5D return: 5.87% | 20D drawdown: 0.00% | vol_ratio: 0.27
- RS vs SILJ: gap -2.44% / slope_proxy -4.86%
- FundamentalScore: 72 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **52.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.34 | RSI14: 77.63 | ATR14%: 5.77%
- MA20/50/200 gap: 15.03% / 15.12% / -7.49%
- 5D return: 5.81% | 20D drawdown: -0.86% | vol_ratio: 0.43
- RS vs SILJ: gap -5.72% / slope_proxy 4.58%
- FundamentalScore: 68 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **45.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 27.50 | RSI14: 72.38 | ATR14%: 7.25%
- MA20/50/200 gap: 14.79% / 18.58% / -5.25%
- 5D return: 3.50% | 20D drawdown: -1.43% | vol_ratio: 0.36
- RS vs SILJ: gap -4.09% / slope_proxy 5.67%
- FundamentalScore: 42 | TechnicalScore: 0 | RegimeScore: 75 | OverallScore: **33.9**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **False**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 생산주가 아니라 PEA/공정 선택 전 개발 옵션.
- Watch: PEA, 공정 선택, capex, 회수율.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
