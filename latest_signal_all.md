# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: AYA**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-11-03 03:01:09**
- 데이터 기준일(일봉): **2026-11-02**
- 데이터 기준일(주봉): **2026-11-02**
- VXN 기준일: **2026-10-30** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **G: 중립, QQQ 중심**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **500,000원** (25%)

## Weekly gate: 큰 환경

- QQQ close: 681.09
- Weekly RSI14: **44.69**
- 52W MA: 665.49 / gap: **2.34%**
- 104W MA gap: **13.90%**
- 52W MA 13W slope: **5.02%**
- VXN: **28.50** / 5D change: 0.20

## Daily trigger: 실제 매수 타이밍

- QQQ close: 681.09
- Daily RSI14: **32.13**
- 20D gap: **-5.98%**
- 50D gap: **-5.94%**
- 200D gap: **0.35%**
- MACD hist: -4.3427 / change: -1.2268
- ATR14%: **1.93%**
- 20D high drawdown: **-10.34%**

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

- 데이터 기준일(주가): **2026-11-02**
- 실행시간(UTC): **2026-11-03 03:00:43**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 3.44 / 4주 변화 34.0 bp
- IG OAS (BAMLC0A0CM): 0.94 / 4주 변화 9.0 bp
- 10Y Real Yield (DFII10): 2.6 / 4주 변화 -32.0 bp
- VIX (VIXCLS): 19.42
- NFCI: -0.487

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.074901
- MA60: 8.380596
- gap: -3.65%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.337215
- MA60: 0.416604
- gap: -19.06%
- MA60_slope_proxy: 0.025543
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-11-02**
- 실행시간(UTC): **2026-11-03 03:00:45**

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
- TERM_SPREAD_10Y_POLICY: 150.89 bp / 4주 변화 -10.76 bp
- CURVE_10s5s: 35.27 bp / 4주 변화 -10.06 bp

## NWG Price
- close: 579.6
- MA50: 672.144 / gap50: -13.77%
- MA200: 635.1245 / gap200: -8.74%

## Relative Strength
- RS vs FTSE gap: -14.49% / slope_proxy: -0.000971
- RS vs Peers gap: -1.78% / slope_proxy: 0.022785

## Why not today?
- CurveGreen=FALSE
- DemandGreen=FALSE (monthly)
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-11-03 03:00:53**

## Commodity Regime

- WTI ref (CL=F): 96.59 / 5D -5.08%
- Brent ref (BZ=F): 104.73 / 5D -9.57%
- Brent Tier: **>=90**
- Brent-WTI spread: 8.14
- Gas ref (NG=F): 2.88 / 5D 10.80%

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

- close: 60.72
- MA20 / MA60 / MA200: 61.83 / 59.94 / 55.79
- gap20 / gap60: -1.79% / 1.30%
- 5D return: -5.23%
- 20D high/low: 64.17 / 58.21

### Relative Strength

- ratio: 0.902900
- ratio_MA60: 0.931662
- ratio_gap: -3.09%
- ratio_slope_proxy(20d): -0.012385

### Volume (if available)

- volume: 12661800.00
- volume_MA20: 8610870.00
- volume_ratio: 1.47

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.16
- MA20 / MA60 / MA200: 24.33 / 21.31 / 18.69
- gap20 / gap60: -13.03% / -0.70%
- 5D return: -5.96%
- 20D high/low: 26.16 / 21.16

### Relative Strength

- ratio: 0.657960
- ratio_MA60: 0.565133
- ratio_gap: 16.43%
- ratio_slope_proxy(20d): 0.038843

### Volume (if available)

- volume: 26112900.00
- volume_MA20: 27996035.00
- volume_ratio: 0.93

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

- close: 6.23
- MA20 / MA60 / MA200: 5.98 / 5.77 / 5.87
- gap20 / gap60: 4.18% / 7.95%
- 5D return: -4.59%
- 20D high/low: 6.94 / 5.39

### Relative Strength

- ratio: 0.016014
- ratio_MA60: 0.014316
- ratio_gap: 11.86%
- ratio_slope_proxy(20d): 0.000557

### Volume (if available)

- volume: 45633600.00
- volume_MA20: 42382775.00
- volume_ratio: 1.08

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

- close: 12.87
- MA20 / MA60 / MA200: 13.39 / 13.81 / 12.69
- gap20 / gap60: -3.92% / -6.83%
- 5D return: -6.47%
- 20D high/low: 14.79 / 12.50

### Relative Strength

- ratio: 0.041294
- ratio_MA60: 0.049261
- ratio_gap: -16.17%
- ratio_slope_proxy(20d): -0.001760

### Volume (if available)

- volume: 34655100.00
- volume_MA20: 16034540.00
- volume_ratio: 2.16

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **True**
- VG_TREND_UP: **False**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **True**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-11-02**
- 실행시간(UTC): **2026-11-03 03:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: 34.0 bp / latest 3.44
- IG OAS 4주 변화: 9.0 bp / latest 0.94
- 10Y Real Yield 4주 변화: -32.0 bp / latest 2.6
- VIX: 19.42
- NFCI: -0.487

### Leadership ratios
- SILJ/SLV gap: -1.24% / slope_proxy: 0.005769
- GDXJ/GLD gap: -10.19% / slope_proxy: 0.00623

## VZLA (Vizsla Silver)
- close: 3.05 | RSI14: 36.619313 | ATR14%: 6.12%
- MA20 gap: -7.10% | MA50 gap: -17.18% | MA200 gap: -18.28%
- vol_ratio(Volume/Vol20): 0.656512 | gap_open: 3.27%
- RS vs SILJ gap: 2.80% / slope_proxy: 0.000384
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
- close: 6.95 | RSI14: 36.250331 | ATR14%: 7.26%
- MA20 gap: -12.51% | MA50 gap: -20.97% | MA200 gap: -20.86%
- vol_ratio(Volume/Vol20): 1.331505 | gap_open: 3.69%
- SilverMarginGate: SI=50.279999 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -1.83% / slope_proxy: 0.017271
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
- close: 16.33 | RSI14: 40.345561 | ATR14%: 7.47%
- MA20 gap: -4.81% | MA50 gap: -18.21% | MA200 gap: -45.49%
- vol_ratio(Volume/Vol20): 0.984448 | gap_open: 3.41%
- RS vs SILJ gap: -2.78% / slope_proxy: -0.048724
- RS vs GDXJ gap: -5.93% / slope_proxy: -0.016545
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

- 실행시간(UTC): **2026-11-03 03:01:08**
- 데이터 기준일(주가): **2026-11-02**

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

- HY OAS: 3.44 / 4주 변화 0.34 bp-ish / 2026-10-30
- IG OAS: 0.94 / 4주 변화 0.09 bp-ish / 2026-10-30
- 10Y Real Yield: 2.60 / 4주 변화 -0.28 bp-ish / 2026-10-30
- VIX: 19.42 / 4주 변화 4.11 / 2026-10-30
- NFCI: -0.49 / 4주 변화 0.02 / 2026-10-23

### Leadership ratios

- GDX/GLD: gap -6.06% / slope_proxy -5.17%
- GDXJ/GLD: gap -10.19% / slope_proxy -9.56%
- SILJ/SLV: gap -1.24% / slope_proxy 1.39%
- Gold breadth proxy: above50 0.00%, above200 0.00%, count 13
- Silver breadth proxy: above50 0.00%, above200 7.69%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 7.49 | RSI14: 24.83 | ATR14%: 5.10%
- MA20/50/200 gap: -12.06% / -20.77% / -7.49%
- 5D return: -5.43% | 20D drawdown: -19.98% | vol_ratio: 1.52
- RS vs GDXJ: gap -5.11% / slope_proxy -3.70%
- FundamentalScore: 88 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **56.1**
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
- close: 5.25 | RSI14: 24.20 | ATR14%: 6.64%
- MA20/50/200 gap: -15.36% / -25.98% / -24.35%
- 5D return: -5.75% | 20D drawdown: -25.43% | vol_ratio: 1.55
- RS vs GDXJ: gap -10.08% / slope_proxy -11.66%
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

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 0.78 | RSI14: 25.64 | ATR14%: 8.06%
- MA20/50/200 gap: -14.52% / -35.66% / -44.99%
- 5D return: -6.02% | 20D drawdown: -23.53% | vol_ratio: 1.09
- RS vs GDXJ: gap -24.43% / slope_proxy -7.59%
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
- close: 1.58 | RSI14: 25.00 | ATR14%: 8.50%
- MA20/50/200 gap: -18.22% / -31.65% / -20.25%
- 5D return: -4.24% | 20D drawdown: -28.51% | vol_ratio: 0.57
- RS vs GDXJ: gap -16.51% / slope_proxy -16.61%
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
- close: 23.61 | RSI14: 37.02 | ATR14%: 5.83%
- MA20/50/200 gap: -7.46% / -12.51% / 13.16%
- 5D return: -0.92% | 20D drawdown: -14.18% | vol_ratio: 0.85
- RS vs SILJ: gap 8.75% / slope_proxy 3.00%
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
- close: 3.05 | RSI14: 38.69 | ATR14%: 6.07%
- MA20/50/200 gap: -7.10% / -17.18% / -18.28%
- 5D return: -0.65% | 20D drawdown: -14.08% | vol_ratio: 0.66
- RS vs SILJ: gap 2.80% / slope_proxy 3.70%
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
- close: 13.54 | RSI14: 29.25 | ATR14%: 5.66%
- MA20/50/200 gap: -11.00% / -22.93% / -27.18%
- 5D return: -3.15% | 20D drawdown: -20.82% | vol_ratio: 1.10
- RS vs SILJ: gap -4.61% / slope_proxy -4.97%
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

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 6.95 | RSI14: 30.31 | ATR14%: 7.03%
- MA20/50/200 gap: -12.51% / -20.97% / -20.86%
- 5D return: -1.28% | 20D drawdown: -23.71% | vol_ratio: 1.33
- RS vs SILJ: gap -1.83% / slope_proxy -6.91%
- FundamentalScore: 74 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **49.8**
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

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.23 | RSI14: 34.37 | ATR14%: 5.82%
- MA20/50/200 gap: -10.03% / -21.91% / -25.74%
- 5D return: -3.47% | 20D drawdown: -16.61% | vol_ratio: 1.00
- RS vs SILJ: gap -4.25% / slope_proxy 0.08%
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
- close: 2.88 | RSI14: 19.35 | ATR14%: 7.84%
- MA20/50/200 gap: -20.29% / -35.43% / -49.28%
- 5D return: -4.32% | 20D drawdown: -35.57% | vol_ratio: 1.06
- RS vs SILJ: gap -20.83% / slope_proxy -22.67%
- FundamentalScore: 68 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **47.1**
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
- close: 4.38 | RSI14: 32.02 | ATR14%: 6.39%
- MA20/50/200 gap: -12.80% / -26.56% / -36.19%
- 5D return: -4.78% | 20D drawdown: -21.36% | vol_ratio: 1.13
- RS vs SILJ: gap -10.83% / slope_proxy -5.62%
- FundamentalScore: 60 | TechnicalScore: 30 | RegimeScore: 30 | OverallScore: **43.5**
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
- close: 16.33 | RSI14: 42.28 | ATR14%: 7.33%
- MA20/50/200 gap: -4.81% / -18.21% / -45.49%
- 5D return: 6.11% | 20D drawdown: -14.90% | vol_ratio: 0.98
- RS vs SILJ: gap -2.78% / slope_proxy 2.67%
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
