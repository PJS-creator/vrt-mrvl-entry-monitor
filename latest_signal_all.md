# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **🟡 QLD/TIGER 레버리지 소액만 허용**
- Core (VRT/MRVL): **✅ Entry condition met: VRT**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM, HL**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-09-11 15:01:09**
- 데이터 기준일(일봉): **2026-09-11**
- 데이터 기준일(주봉): **2026-09-07**
- VXN 기준일: **2026-09-10** / source: `FRED: VXNCLS`

## Verdict

**🟡 QLD/TIGER 레버리지 소액만 허용**
- Regime: **C: QLD 소액 테스트만 허용**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,500,000원** (75%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **200,000원** (10%)
- 대기자금: **300,000원** (15%)

## Weekly gate: 큰 환경

- QQQ close: 714.79
- Weekly RSI14: **57.40**
- 52W MA: 648.33 / gap: **10.25%**
- 104W MA gap: **23.08%**
- 52W MA 13W slope: **6.24%**
- VXN: **23.33** / 5D change: 2.26

## Daily trigger: 실제 매수 타이밍

- QQQ close: 714.79
- Daily RSI14: **50.72**
- 20D gap: **-0.12%**
- 50D gap: **0.62%**
- 200D gap: **8.42%**
- MACD hist: -0.4942 / change: 0.0948
- ATR14%: **1.25%**
- 20D high drawdown: **-2.23%**

## Checks

- weekly_good: **False**
- weekly_small: **True**
- weekly_overheated: **False**
- weekly_panic: **False**
- daily_a: **True**
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

- 데이터 기준일(주가): **2026-09-11**
- 실행시간(UTC): **2026-09-11 15:00:45**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.7 / 4주 변화 -1.0 bp
- IG OAS (BAMLC0A0CM): 0.8 / 4주 변화 1.0 bp
- 10Y Real Yield (DFII10): 2.46 / 4주 변화 4.0 bp
- VIX (VIXCLS): 17.84
- NFCI: -0.564

## VRT 신규진입 룰
- ratio (VRT/SRVR): 8.484349
- MA60: 9.262186
- gap: -8.40%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.412604
- MA60: 0.39223
- gap: 5.19%
- MA60_slope_proxy: -0.001486
- **MRVL_ENTRY**: **False**

## Verdict
✅ Entry condition met: VRT

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-09-11**
- 실행시간(UTC): **2026-09-11 15:00:47**

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
- TERM_SPREAD_10Y_POLICY: 144.22 bp / 4주 변화 23.29 bp
- CURVE_10s5s: 45.72 bp / 4주 변화 -2.06 bp

## NWG Price
- close: 693.0
- MA50: 686.4655 / gap50: 0.95%
- MA200: 630.1486 / gap200: 9.97%

## Relative Strength
- RS vs FTSE gap: 2.05% / slope_proxy: 0.002084
- RS vs Peers gap: 0.81% / slope_proxy: 0.012544

## Why not today?
- DemandGreen=FALSE (monthly)
- PullbackZone=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-09-11 15:00:52**

## Commodity Regime

- WTI ref (CL=F): 99.10 / 5D 8.54%
- Brent ref (BZ=F): 104.47 / 5D 9.37%
- Brent Tier: **>=90**
- Brent-WTI spread: 5.37
- Gas ref (NG=F): 2.82 / 5D -3.30%

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

- close: 60.88
- MA20 / MA60 / MA200: 59.86 / 55.78 / 52.31
- gap20 / gap60: 1.71% / 9.16%
- 5D return: 0.91%
- 20D high/low: 61.24 / 58.09

### Relative Strength

- ratio: 0.936620
- ratio_MA60: 0.944234
- ratio_gap: -0.81%
- ratio_slope_proxy(20d): -0.017607

### Volume (if available)

- volume: 1885476.00
- volume_MA20: 6780638.80
- volume_ratio: 0.28

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **True**
- OXY_TREND_UP: **True**
- OXY_PULLBACK_OK: **True**
- OXY_RELATIVE_OK: **False**

## PBR

- **ENTRY**: **False**

### Trend

- close: 21.14
- MA20 / MA60 / MA200: 19.19 / 17.83 / 16.66
- gap20 / gap60: 10.15% / 18.54%
- 5D return: 3.05%
- 20D high/low: 21.38 / 17.37

### Relative Strength

- ratio: 0.551036
- ratio_MA60: 0.501771
- ratio_gap: 9.82%
- ratio_slope_proxy(20d): 0.005077

### Volume (if available)

- volume: 4542439.00
- volume_MA20: 22174021.95
- volume_ratio: 0.20

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **True**
- BRAZIL_RISK_OK: **False**
- PBR_TREND_OK: **True**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 5.73
- MA20 / MA60 / MA200: 5.83 / 5.43 / 5.59
- gap20 / gap60: -1.78% / 5.50%
- 5D return: -4.82%
- 20D high/low: 6.22 / 5.60

### Relative Strength

- ratio: 0.013714
- ratio_MA60: 0.013729
- ratio_gap: -0.10%
- ratio_slope_proxy(20d): -0.000263

### Volume (if available)

- volume: 9298176.00
- volume_MA20: 37813978.80
- volume_ratio: 0.25

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

- close: 15.63
- MA20 / MA60 / MA200: 14.51 / 13.24 / 11.52
- gap20 / gap60: 7.73% / 18.08%
- 5D return: 7.94%
- 20D high/low: 15.63 / 13.75

### Relative Strength

- ratio: 0.056517
- ratio_MA60: 0.050243
- ratio_gap: 12.49%
- ratio_slope_proxy(20d): -0.000865

### Volume (if available)

- volume: 8325671.00
- volume_MA20: 13008188.55
- volume_ratio: 0.64

### Checks

- RISK_OK_STRICT: **True**
- LNG_PEER_TREND_UP: **False**
- VG_TREND_UP: **True**
- VG_RELATIVE_TURN_UP: **False**
- VG_NOT_EXTENDED: **False**

## Verdict

⏸ No entry today


---

## Silver report

# Silver Miners Daily Entry Monitor (VZLA / SCZM / HYMC)

- 데이터 기준일(주가): **2026-09-11**
- 실행시간(UTC): **2026-09-11 15:00:58**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **True**
- JuniorGoldLeadership(GDXJ/GLD): **True**

### Macro (FRED)
- HY OAS 4주 변화: -1.0 bp / latest 2.7
- IG OAS 4주 변화: 1.0 bp / latest 0.8
- 10Y Real Yield 4주 변화: 4.0 bp / latest 2.46
- VIX: 17.84
- NFCI: -0.564

### Leadership ratios
- SILJ/SLV gap: 7.20% / slope_proxy: 0.02789
- GDXJ/GLD gap: 11.45% / slope_proxy: 0.013575

## VZLA (Vizsla Silver)
- close: 3.995 | RSI14: 54.684923 | ATR14%: 4.89%
- MA20 gap: 0.83% | MA50 gap: 11.63% | MA200 gap: -1.57%
- vol_ratio(Volume/Vol20): 0.175479 | gap_open: 1.75%
- RS vs SILJ gap: 1.88% / slope_proxy: 0.000107
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
- close: 9.76 | RSI14: 56.260614 | ATR14%: 6.09%
- MA20 gap: 1.45% | MA50 gap: 21.71% | MA200 gap: 9.24%
- vol_ratio(Volume/Vol20): 0.240381 | gap_open: 2.17%
- SilverMarginGate: SI=65.375 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: 13.86% / slope_proxy: 0.014657
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
- close: 21.540001 | RSI14: 41.061919 | ATR14%: 7.99%
- MA20 gap: -11.85% | MA50 gap: -6.35% | MA200 gap: -28.53%
- vol_ratio(Volume/Vol20): 0.34353 | gap_open: 2.81%
- RS vs SILJ gap: -16.09% / slope_proxy: -0.088565
- RS vs GDXJ gap: -19.17% / slope_proxy: -0.027029
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

- 실행시간(UTC): **2026-09-11 15:01:08**
- 데이터 기준일(주가): **2026-09-11**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, SCZM, HL**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **False**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **True**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **True**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.70 / 4주 변화 -0.01 bp-ish / 2026-09-10
- IG OAS: 0.80 / 4주 변화 0.01 bp-ish / 2026-09-10
- 10Y Real Yield: 2.46 / 4주 변화 0.03 bp-ish / 2026-09-09
- VIX: 17.84 / 4주 변화 3.21 / 2026-09-10
- NFCI: -0.56 / 4주 변화 -0.08 / 2026-09-04

### Leadership ratios

- GDX/GLD: gap 11.91% / slope_proxy 8.58%
- GDXJ/GLD: gap 11.46% / slope_proxy 7.24%
- SILJ/SLV: gap 7.20% / slope_proxy 3.60%
- Gold breadth proxy: above50 100.00%, above200 76.92%, count 13
- Silver breadth proxy: above50 92.31%, above200 53.85%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 10.00 | RSI14: 42.82 | ATR14%: 4.54%
- MA20/50/200 gap: -2.64% / 13.81% / 33.22%
- 5D return: -3.38% | 20D drawdown: -9.67% | vol_ratio: 0.30
- RS vs GDXJ: gap 1.99% / slope_proxy -7.71%
- FundamentalScore: 88 | TechnicalScore: 60 | RegimeScore: 75 | OverallScore: **75.6**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, RelativeStrength(vs GDXJ)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 8.01 | RSI14: 52.11 | ATR14%: 4.71%
- MA20/50/200 gap: 3.85% / 24.06% / 13.63%
- 5D return: -1.17% | 20D drawdown: -4.02% | vol_ratio: 0.07
- RS vs GDXJ: gap 12.49% / slope_proxy 6.65%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **74.7**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 2.62 | RSI14: 56.31 | ATR14%: 6.92%
- MA20/50/200 gap: 1.39% / 20.54% / 34.87%
- 5D return: -3.68% | 20D drawdown: -6.09% | vol_ratio: 0.08
- RS vs GDXJ: gap 11.36% / slope_proxy 5.02%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **69.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **False**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: 금/구리 고가격에서 FCF 가능. 하지만 고비용 + Bolivia 물류/정치 리스크.
- Watch: Don Mario 물류 정상화, AISC 하향, Bolivia 리스크.
- Why not today: GoldUptrend=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.49 | RSI14: 35.92 | ATR14%: 4.64%
- MA20/50/200 gap: -5.04% / 10.04% / -0.65%
- 5D return: -7.19% | 20D drawdown: -10.00% | vol_ratio: 0.14
- RS vs GDXJ: gap -2.18% / slope_proxy -9.35%
- FundamentalScore: 70 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **51.8**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs GDXJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 20.09 | RSI14: 46.21 | ATR14%: 4.96%
- MA20/50/200 gap: -0.55% / 15.08% / 5.16%
- 5D return: -5.26% | 20D drawdown: -6.23% | vol_ratio: 0.12
- RS vs SILJ: gap 6.21% / slope_proxy 5.98%
- FundamentalScore: 78 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **79.8**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: SilverUptrend=FALSE

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 9.76 | RSI14: 50.91 | ATR14%: 6.23%
- MA20/50/200 gap: 1.45% / 21.71% / 9.24%
- 5D return: -6.33% | 20D drawdown: -6.42% | vol_ratio: 0.24
- RS vs SILJ: gap 13.86% / slope_proxy 6.85%
- FundamentalScore: 74 | TechnicalScore: 85 | RegimeScore: 75 | OverallScore: **78.0**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **True**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 볼리비아/멕시코 생산 + 은/아연/납 복합 레버리지. 변동성 큼.
- Watch: Bolivar 회복, Zimapan 문제, Bolivia 사회/정치 리스크.
- Why not today: SilverUptrend=FALSE

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 29.10 | RSI14: 59.29 | ATR14%: 5.91%
- MA20/50/200 gap: 4.74% / 21.38% / 55.74%
- 5D return: -2.41% | 20D drawdown: -2.64% | vol_ratio: 0.25
- RS vs SILJ: gap 14.22% / slope_proxy 8.77%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 75 | OverallScore: **76.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 3.99 | RSI14: 51.28 | ATR14%: 5.08%
- MA20/50/200 gap: 0.83% / 11.63% / -1.57%
- 5D return: -4.20% | 20D drawdown: -4.20% | vol_ratio: 0.18
- RS vs SILJ: gap 1.88% / slope_proxy 2.94%
- FundamentalScore: 72 | TechnicalScore: 40 | RegimeScore: 75 | OverallScore: **61.4**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 10.45 | RSI14: 48.14 | ATR14%: 5.60%
- MA20/50/200 gap: -3.09% / 11.91% / 5.58%
- 5D return: -8.85% | 20D drawdown: -8.85% | vol_ratio: 0.34
- RS vs SILJ: gap 3.37% / slope_proxy -4.98%
- FundamentalScore: 82 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **57.1**
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
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 5.18 | RSI14: 45.79 | ATR14%: 5.92%
- MA20/50/200 gap: -2.81% / 9.59% / -11.94%
- 5D return: -6.41% | 20D drawdown: -9.67% | vol_ratio: 0.20
- RS vs SILJ: gap -1.77% / slope_proxy -4.13%
- FundamentalScore: 68 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **50.9**
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
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 6.80 | RSI14: 39.36 | ATR14%: 5.60%
- MA20/50/200 gap: -7.27% / 3.37% / -2.58%
- 5D return: -11.57% | 20D drawdown: -12.03% | vol_ratio: 0.52
- RS vs SILJ: gap -5.80% / slope_proxy -6.15%
- FundamentalScore: 60 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **47.2**
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
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 21.54 | RSI14: 25.72 | ATR14%: 7.74%
- MA20/50/200 gap: -11.85% / -6.35% / -28.53%
- 5D return: -7.55% | 20D drawdown: -22.80% | vol_ratio: 0.34
- RS vs SILJ: gap -16.09% / slope_proxy -22.91%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 75 | OverallScore: **39.2**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **True**
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
- Why not today: SilverUptrend=FALSE, PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
