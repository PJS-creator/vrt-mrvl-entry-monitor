# Daily Signals (All-in-One)

## Quick Summary

- QQQ/QLD Timing: **⏸ QLD/TIGER 레버리지 대기**
- Core (VRT/MRVL): **✅ Entry condition met: BOTH**
- NatWest (NWG): **⏸ No entry today**
- Energy (OXY/PBR/RIG/VG): **⏸ No entry today**
- Silver (VZLA/SCZM/HYMC): **⏸ No entry today**
- Precious Miners (Gold/Silver): **🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, HL, USAS, ASM**

---

## QQQ/QLD timing report

# QQQ / QLD Timing Monitor

- 실행시간(UTC): **2026-06-02 15:02:14**
- 데이터 기준일(일봉): **2026-06-02**
- 데이터 기준일(주봉): **2026-06-01**
- VXN 기준일: **2026-06-01** / source: `FRED: VXNCLS`

## Verdict

**⏸ QLD/TIGER 레버리지 대기**
- Regime: **F: 과열권, QLD 대기**

## Recommended monthly buy amount

- 월 적립 예산: **2,000,000원**
- TIGER 미국나스닥100 (133690) / QQQ 역할: **1,000,000원** (50%)
- TIGER 미국나스닥100레버리지(합성) (418660) / QLD 역할: **0원** (0%)
- 대기자금: **1,000,000원** (50%)

## Weekly gate: 큰 환경

- QQQ close: 744.40
- Weekly RSI14: **78.07**
- 52W MA: 607.81 / gap: **22.47%**
- 104W MA gap: **35.69%**
- 52W MA 13W slope: **7.82%**
- VXN: **23.18** / 5D change: 0.36

## Daily trigger: 실제 매수 타이밍

- QQQ close: 744.40
- Daily RSI14: **78.90**
- 20D gap: **3.96%**
- 50D gap: **12.93%**
- 200D gap: **20.36%**
- MACD hist: 0.2657 / change: 0.0302
- ATR14%: **1.34%**
- 20D high drawdown: **0.00%**

## Checks

- weekly_good: **False**
- weekly_small: **False**
- weekly_overheated: **True**
- weekly_panic: **False**
- daily_a: **False**
- daily_b: **False**
- daily_overheated: **True**
- rebound_after_panic: **False**

## Why

- 주봉 RSI 또는 52주선 이격도가 과열권이라 QLD 신규 본격 매수는 제한
- 일봉도 단기 과열 또는 고점 근처라 QLD 추격매수 부적합

## Rule note

- 이 알림은 월 신규 적립금 배분 판단용입니다. 기존 보유분을 자동 매도하라는 뜻이 아닙니다.
- QLD 및 국내 레버리지 ETF는 일간 2배 구조라 장기 누적성과가 단순 2배와 다를 수 있습니다.
- 한국 상장 레버리지 ETF는 한국장/미국장 시차 때문에 장중 괴리가 생길 수 있으므로 시장가보다 지정가가 안전합니다.

---

## Core report

# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-02**
- 실행시간(UTC): **2026-06-02 15:00:55**

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 -6.0 bp
- IG OAS (BAMLC0A0CM): 0.73 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.07 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.819127
- MA60: 8.987015
- gap: 9.26%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.437641
- MA60: 0.292498
- gap: 49.62%
- MA60_slope_proxy: 0.043917
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH

---

## NatWest report

# NatWest Daily Entry Monitor

- 데이터 기준일(주가): **2026-06-02**
- 실행시간(UTC): **2026-06-02 15:00:57**

## Verdict
⏸ No entry today

## Checks
- RiskGreen: **True**
- CurveGreen: **True**
- DemandGreen(monthly): **True**
- MacroGreen: **True**
- PriceConfirm: **False**
- ENTRY_STRICT: **False**
- ENTRY_LOOSE: **False**

## Derived (UK rates/curve)
- TERM_SPREAD_10Y_POLICY: 102.6 bp / 4주 변화 -14.81 bp
- CURVE_10s5s: 46.77 bp / 4주 변화 0.83 bp

## NWG Price
- close: 599.8
- MA50: 578.0251 / gap50: 3.77%
- MA200: 587.6505 / gap200: 2.07%

## Relative Strength
- RS vs FTSE gap: 3.47% / slope_proxy: -0.000705
- RS vs Peers gap: -4.58% / slope_proxy: -0.023688

## Why not today?
- RelativeTurn=FALSE

---

## Energy report

# Energy Daily Signal Monitor

- 실행시간(UTC): **2026-06-02 15:01:05**

## ⚠️ DATA WARNING

- FRED DCOILBRENTEU failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## Commodity Regime

- WTI ref (CL=F): 91.95 / 5D -2.07%
- Brent ref (BZ=F): 94.94 / 5D -4.66%
- Brent Tier: **>=90**
- Brent-WTI spread: 2.99
- Gas ref (NG=F): 3.15 / 5D 8.85%

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

- close: 58.81
- MA20 / MA60 / MA200: 57.42 / 58.54 / 48.30
- gap20 / gap60: 2.42% / 0.46%
- 5D return: 2.35%
- 20D high/low: 60.70 / 53.03

### Relative Strength

- ratio: 1.021379
- ratio_MA60: 1.006861
- ratio_gap: 1.44%
- ratio_slope_proxy(20d): 0.025651

### Volume (if available)

- volume: 3139667.00
- volume_MA20: 12009568.35
- volume_ratio: 0.26

### Checks

- RISK_OK_STRICT: **True**
- WTI_TREND_UP: **False**
- OXY_TREND_UP: **False**
- OXY_PULLBACK_OK: **False**
- OXY_RELATIVE_OK: **True**

## PBR

- **ENTRY**: **False**

### Trend

- close: 18.73
- MA20 / MA60 / MA200: 19.92 / 20.18 / 15.13
- gap20 / gap60: -5.96% / -7.18%
- 5D return: -3.45%
- 20D high/low: 21.77 / 18.73

### Relative Strength

- ratio: 0.522525
- ratio_MA60: 0.529132
- ratio_gap: -1.25%
- ratio_slope_proxy(20d): 0.039187

### Volume (if available)

- volume: 3919431.00
- volume_MA20: 17414281.55
- volume_ratio: 0.23

### Checks

- RISK_OK_SOFT: **True**
- BRENT_TREND_UP: **False**
- BRAZIL_RISK_OK: **True**
- PBR_TREND_OK: **False**
- PBR_PULLBACK_OK: **False**
- PBR_RELATIVE_OK: **True**

## RIG

- **ENTRY**: **False**

### Trend

- close: 6.36
- MA20 / MA60 / MA200: 6.62 / 6.51 / 4.87
- gap20 / gap60: -3.99% / -2.41%
- 5D return: -1.93%
- 20D high/low: 7.58 / 6.17

### Relative Strength

- ratio: 0.014772
- ratio_MA60: 0.015665
- ratio_gap: -5.70%
- ratio_slope_proxy(20d): -0.000279

### Volume (if available)

- volume: 7338250.00
- volume_MA20: 34067757.50
- volume_ratio: 0.22

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

- close: 12.58
- MA20 / MA60 / MA200: 12.94 / 13.46 / 10.86
- gap20 / gap60: -2.77% / -6.52%
- 5D return: -2.40%
- 20D high/low: 14.78 / 11.45

### Relative Strength

- ratio: 0.053212
- ratio_MA60: 0.051923
- ratio_gap: 2.48%
- ratio_slope_proxy(20d): 0.003167

### Volume (if available)

- volume: 2409632.00
- volume_MA20: 18371071.60
- volume_ratio: 0.13

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

- 데이터 기준일(주가): **2026-06-02**
- 실행시간(UTC): **2026-06-02 15:01:56**

## Verdict
⏸ No entry today

## Regime (공통 게이트)
- RiskGreen: **True**
- SilverUptrend(SI=F): **False**
- GoldUptrend(GC=F): **False**
- MinersLeadership(SILJ/SLV): **False**
- JuniorGoldLeadership(GDXJ/GLD): **False**

### Macro (FRED)
- HY OAS 4주 변화: -6.0 bp / latest 2.72
- IG OAS 4주 변화: -7.0 bp / latest 0.73
- 10Y Real Yield 4주 변화: 16.0 bp / latest 2.07
- VIX: 16.05
- NFCI: -0.51

### Leadership ratios
- SILJ/SLV gap: 2.56% / slope_proxy: -0.012991
- GDXJ/GLD gap: -0.93% / slope_proxy: -0.006305

## VZLA (Vizsla Silver)
- close: 4.115 | RSI14: 66.257099 | ATR14%: 5.52%
- MA20 gap: 13.74% | MA50 gap: 19.60% | MA200 gap: -3.13%
- vol_ratio(Volume/Vol20): 0.335558 | gap_open: 2.22%
- RS vs SILJ gap: 16.84% / slope_proxy: 0.001595
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
- close: 8.27 | RSI14: 47.154535 | ATR14%: 6.99%
- MA20 gap: -3.99% | MA50 gap: -1.40% | MA200 gap: -0.93%
- vol_ratio(Volume/Vol20): 0.211193 | gap_open: 1.35%
- SilverMarginGate: SI=76.074997 / watch>=32.0:True / entry>=35.0:True
- RS vs SILJ gap: -3.75% / slope_proxy: -0.009936
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
- close: 34.047501 | RSI14: 45.47823 | ATR14%: 8.43%
- MA20 gap: -6.27% | MA50 gap: -7.42% | MA200 gap: 40.50%
- vol_ratio(Volume/Vol20): 0.266399 | gap_open: 1.63%
- RS vs SILJ gap: -9.09% / slope_proxy: 0.001092
- RS vs GDXJ gap: -3.26% / slope_proxy: 0.002653
- Checks:
  - trend_ok: **True**
  - rs_ok: **False**
  - risk_ok: **True**
  - triggers: breakout=False, retest=False
- **ENTRY_CANDIDATE**: **False**
- **ENTRY_CONFIRMED**: **False**

### Why not today?
- MetalsUptrend(SI&GC)=FALSE
- SectorLeadership(SILJ/SLV or GDXJ/GLD)=FALSE
- RelativeStrength(vs GDXJ/SILJ)=FALSE
- Trigger(Breakout/Retest)=FALSE


---

## Precious miners report

# Precious Miners Daily Entry Monitor (Gold / Silver)

- 실행시간(UTC): **2026-06-02 15:02:09**
- 데이터 기준일(주가): **2026-06-02**

## Verdict
**🟡 Precious miners watch/add-on candidates: MAKO, JAG.TO, AYA, EXK, HL, USAS, ASM**

## Regime / 공통 게이트

- RiskGreen: **True**
- RealYieldHeadwind: **False**
- GoldUptrend(GC=F/GLD): **False**
- SilverUptrend(SI=F/SLV): **True**
- GoldMinerLeadership(GDX/GLD or GDXJ/GLD): **False**
- SilverMinerLeadership(SILJ/SLV): **True**
- GoldBreadthProxy >=45% above MA50: **False**
- SilverBreadthProxy >=45% above MA50: **True**

### Macro (FRED, if available)

- HY OAS: 2.72 / 4주 변화 -0.05 bp-ish / 2026-06-01
- IG OAS: 0.73 / 4주 변화 -0.06 bp-ish / 2026-06-01
- 10Y Real Yield: 2.07 / 4주 변화 0.13 bp-ish / 2026-05-29
- VIX: 16.05 / 4주 변화 -2.24 / 2026-06-01
- NFCI: -0.51 / 4주 변화 0.04 / 2026-05-22

### Leadership ratios

- GDX/GLD: gap -0.98% / slope_proxy 2.83%
- GDXJ/GLD: gap -0.91% / slope_proxy 2.86%
- SILJ/SLV: gap 2.56% / slope_proxy 4.54%
- Gold breadth proxy: above50 7.69%, above200 61.54%, count 13
- Silver breadth proxy: above50 53.85%, above200 84.62%, count 13

---

## Gold miners

### MAKO (Mako Mining)
- Style: **생산+성장 핵심 알파** | Static rank: 1 | Risk: Medium-High | Max signal: ENTRY
- close: 8.49 | RSI14: 53.32 | ATR14%: 6.55%
- MA20/50/200 gap: 3.02% / 12.74% / 33.57%
- 5D return: -1.45% | 20D drawdown: -2.36% | vol_ratio: 0.20
- RS vs GDXJ: gap 20.00% / slope_proxy 11.28%
- FundamentalScore: 88 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **68.3**
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
- Thesis: San Albino 현금흐름 + Moss 램프업 + Mt. Hamilton/Eagle Mountain 성장 옵션.
- Watch: Moss AISC 하락, Mt. Hamilton 일정, 니카라과 리스크.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### JAG.TO (Jaguar Mining)
- Style: **저평가 FCF/램프업 후보** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 7.11 | RSI14: 47.40 | ATR14%: 5.33%
- MA20/50/200 gap: 6.36% / 3.50% / 3.54%
- 5D return: 10.92% | 20D drawdown: -3.40% | vol_ratio: 0.24
- RS vs GDXJ: gap 6.12% / slope_proxy 8.37%
- FundamentalScore: 82 | TechnicalScore: 65 | RegimeScore: 30 | OverallScore: **65.7**
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
- Thesis: Pilar 현금흐름 + MTL/Turmalina 재가동 + Santa Isabel 옵션.
- Watch: Q2~Q3 생산량 13~15koz/분기 이상, Satinoco 비용 정상화.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, Trigger(Pullback/Breakout)=FALSE

### ORV.TO (Orvana Minerals)
- Style: **고위험 턴어라운드** | Static rank: 4 | Risk: High | Max signal: WATCH
- close: 1.95 | RSI14: 44.52 | ATR14%: 8.94%
- MA20/50/200 gap: -3.75% / 5.23% / 22.98%
- 5D return: 5.98% | 20D drawdown: -21.69% | vol_ratio: 0.11
- RS vs GDXJ: gap 12.12% / slope_proxy 16.19%
- FundamentalScore: 55 | TechnicalScore: 85 | RegimeScore: 30 | OverallScore: **60.5**
- Checks:
  - sector_ok: **False**
  - breadth_ok: **False**
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
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, StaticRiskPolicy=WATCH_ONLY

### TSK.TO (Talisker Resources)
- Style: **BC 고품위 M&A 콜옵션** | Static rank: 3 | Risk: Medium | Max signal: WATCH
- close: 1.38 | RSI14: 35.14 | ATR14%: 5.30%
- MA20/50/200 gap: -1.91% / -2.24% / -5.56%
- 5D return: -0.36% | 20D drawdown: -10.71% | vol_ratio: 0.12
- RS vs GDXJ: gap 1.44% / slope_proxy 1.64%
- FundamentalScore: 70 | TechnicalScore: 40 | RegimeScore: 30 | OverallScore: **51.5**
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
- Thesis: Bralorne 고품위/캐나다 관할권. 다만 PEA, AISC, 반복 생산 미검증.
- Watch: PEA economics, AISC 공개, inferred→indicated 전환.
- Why not today: GoldUptrend=FALSE, GoldMinerLeadership(GDX/GLD or GDXJ/GLD)=FALSE, SectorBreadthProxy=FALSE, PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Silver miners

### AYA (Aya Gold & Silver)
- Style: **품질형 은광 코어** | Static rank: 1 | Risk: Medium | Max signal: ENTRY
- close: 21.35 | RSI14: 50.82 | ATR14%: 6.53%
- MA20/50/200 gap: 11.61% / 22.32% / 46.45%
- 5D return: 14.01% | 20D drawdown: -0.30% | vol_ratio: 0.29
- RS vs SILJ: gap 22.97% / slope_proxy 14.77%
- FundamentalScore: 86 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **81.5**
- Checks:
  - sector_ok: **True**
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
- Why not today: Trigger(Pullback/Breakout)=FALSE

### USAS (Americas Gold and Silver)
- Style: **고품위 북미/antimony 옵션** | Static rank: 5 | Risk: Medium-High | Max signal: ENTRY
- close: 6.42 | RSI14: 31.60 | ATR14%: 7.08%
- MA20/50/200 gap: 2.40% / 7.57% / 18.55%
- 5D return: 9.56% | 20D drawdown: -13.36% | vol_ratio: 0.27
- RS vs SILJ: gap 2.57% / slope_proxy 6.62%
- FundamentalScore: 68 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **73.3**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: Galena/Crescent 고품위 + 미국 전략광물 프리미엄. 5Moz 규모는 아직 미달.
- Watch: AISC $30~35, capex, Idaho 생산 확대.
- Why not today: Trigger(Pullback/Breakout)=FALSE

### EXK (Endeavour Silver)
- Style: **밸류/베타 균형형 은광** | Static rank: 2 | Risk: Medium | Max signal: ENTRY
- close: 9.77 | RSI14: 30.89 | ATR14%: 6.06%
- MA20/50/200 gap: -1.03% / 1.79% / 5.35%
- 5D return: 1.72% | 20D drawdown: -14.79% | vol_ratio: 0.20
- RS vs SILJ: gap -0.43% / slope_proxy 4.60%
- FundamentalScore: 82 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **70.9**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 8Moz+ 생산 가이던스, Terronera/Kolpa 성장, Pitarrilla 장기 옵션.
- Watch: Terronera 램프업, AISC, 멕시코/페루 운영 리스크.
- Why not today: RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### ASM (Avino Silver & Gold)
- Style: **재무 안정형 소형 은광** | Static rank: 6 | Risk: Medium | Max signal: ENTRY
- close: 7.36 | RSI14: 41.04 | ATR14%: 6.35%
- MA20/50/200 gap: 4.46% / 7.97% / 15.77%
- 5D return: 6.74% | 20D drawdown: -7.59% | vol_ratio: 0.33
- RS vs SILJ: gap 6.46% / slope_proxy 8.95%
- FundamentalScore: 60 | TechnicalScore: 65 | RegimeScore: 100 | OverallScore: **69.8**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 재무 안정성은 좋지만 2026 생산 가이던스가 낮음. La Preciosa 전환 전까지 베타 제한.
- Watch: La Preciosa 개발 속도, 생산량 회복.
- Why not today: Trigger(Pullback/Breakout)=FALSE

### HL (Hecla Mining)
- Style: **방어형 은광 코어** | Static rank: 4 | Risk: Low-Medium | Max signal: ENTRY
- close: 17.64 | RSI14: 33.41 | ATR14%: 5.95%
- MA20/50/200 gap: -2.38% / -4.08% / 2.04%
- 5D return: 0.34% | 20D drawdown: -16.20% | vol_ratio: 0.27
- RS vs SILJ: gap -6.48% / slope_proxy -4.81%
- FundamentalScore: 78 | TechnicalScore: 40 | RegimeScore: 100 | OverallScore: **69.1**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **True**
  - rs_ok: **False**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **True**
  - entry_candidate: **True**
  - entry_confirmed: **False**
- Thesis: 북미 저비용 대형 은광. 다만 중형 고성장 베타는 낮음.
- Watch: 은 가격 대비 상대강도, 비용 인플레이션.
- Why not today: RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### VZLA (Vizsla Silver)
- Style: **최고 명목 업사이드 / 보안 리스크** | Static rank: 7 | Risk: Very High | Max signal: WATCH
- close: 4.11 | RSI14: 57.86 | ATR14%: 5.66%
- MA20/50/200 gap: 13.74% / 19.60% / -3.13%
- 5D return: 10.62% | 20D drawdown: 0.00% | vol_ratio: 0.34
- RS vs SILJ: gap 16.84% / slope_proxy 17.22%
- FundamentalScore: 72 | TechnicalScore: 25 | RegimeScore: 100 | OverallScore: **61.1**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
  - strategic_ok: **True**
  - trend_ok: **False**
  - rs_ok: **True**
  - pullback: **False**
  - breakout: **False**
  - not_extended: **False**
  - entry_candidate: **False**
  - entry_confirmed: **False**
- Thesis: Panuco 광상 품질은 최상급. 하지만 Sinaloa 보안/허가/financing 리스크 큼.
- Watch: MIA 허가, 보안계획, 현장 정상화, financing.
- Why not today: PriceTrend=FALSE, Trigger(Pullback/Breakout)=FALSE, Overextended=TRUE, StaticRiskPolicy=WATCH_ONLY

### SCZM (Santacruz Silver)
- Style: **공격형 은 가격 레버리지** | Static rank: 3 | Risk: High | Max signal: ENTRY
- close: 8.27 | RSI14: 20.63 | ATR14%: 6.62%
- MA20/50/200 gap: -3.99% / -1.40% / -0.93%
- 5D return: 2.73% | 20D drawdown: -18.52% | vol_ratio: 0.21
- RS vs SILJ: gap -3.75% / slope_proxy -2.20%
- FundamentalScore: 74 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **58.6**
- Checks:
  - sector_ok: **True**
  - breadth_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE

### HYMC (Hycroft Mining)
- Style: **네바다 대형 자원 옵션** | Static rank: 8 | Risk: Very High | Max signal: WATCH
- close: 34.03 | RSI14: 21.39 | ATR14%: 7.46%
- MA20/50/200 gap: -6.31% / -7.47% / 40.43%
- 5D return: 2.44% | 20D drawdown: -24.65% | vol_ratio: 0.27
- RS vs SILJ: gap -9.14% / slope_proxy -11.48%
- FundamentalScore: 42 | TechnicalScore: 15 | RegimeScore: 100 | OverallScore: **44.2**
- Checks:
  - sector_ok: **True**
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
- Why not today: PriceTrend=FALSE, RelativeStrength(vs SILJ)=FALSE, Trigger(Pullback/Breakout)=FALSE, StaticRiskPolicy=WATCH_ONLY

---

## Rule notes

- 이 보고서는 신규 매수/추가매수 후보를 거르는 체크리스트입니다. 기존 보유분 자동 매도 신호가 아닙니다.
- BPGDM은 직접 조회 대신 금광/은광 후보군의 MA50/MA200 breadth proxy로 대체했습니다.
- VZLA, TSK, ORV, HYMC처럼 허가/보안/공정/관할권 리스크가 큰 종목은 기술적 신호가 좋아도 WATCH_ONLY로 제한했습니다.
- 개별 회사의 실적/허가/보안 이벤트는 가격 데이터만으로 완전히 포착되지 않으므로 분기 실적과 보도자료 확인이 필요합니다.
