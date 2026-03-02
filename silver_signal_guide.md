# Silver Miners Signal Guide (VZLA / SCZM / HYMC)

이 문서는 `silver_signal_monitor.py`에서 매일 산출되는 **신규 진입(Entry) 모니터링 지표**의 의미와, 각 **임계값(Threshold)** 을 왜 그렇게 두었는지/어떻게 해석하는지 정리한 자료입니다.

> ⚠️ 전제
>
> - VZLA, SCZM, HYMC는 모두 **변동성이 큰 광산/주니어/개발사 성격**이 강합니다.
> - 따라서 “정확한 타점”이 아니라 **나쁜 구간을 피하고(레짐 게이트), 좋은 구간에서만(추세·리더십), 들어갈 만한 자리를 기다리는(트리거)** 구조로 설계했습니다.
> - 뉴스/치안/정책 등으로 **갭이 발생**하면 기술적 손절이 무력화될 수 있습니다.

---

## 1) 전체 구조: 3단 게이트 + 2단 신호

### (A) 공통 레짐(환경) 게이트
1) **RiskGreen (거시/리스크)**
2) **SilverUptrend (은 가격 추세)**
3) **MinersLeadership (은광주가 은 현물/ETF를 이기는지)**

→ 이 3개가 맞을 때 “주니어 은광주가 잘 가는 장”일 확률이 올라갑니다.

### (B) 종목 전용 게이트
- **Trend (MA 기반 추세)**
- **Relative Strength (섹터 대비 강도)**
- **Risk Filter (ATR/갭/쇼크 캔들 필터)**

### (C) 트리거 (Trigger)
- **Pullback**: 추세 유지 중 눌림에서 재상승 시도
- **Breakout**: N일 고점 돌파 + 거래량 확인

### (D) 신호 단계
- `ENTRY_CANDIDATE`: 오늘 “진입 검토”가 가능한 상태
- `ENTRY_CONFIRMED`: 전일도 candidate였고 오늘도 candidate (2일 연속 확인)

> 실전에서는 Breakout 계열은 `ENTRY_CONFIRMED`가 훨씬 덜 흔들립니다.

---

## 2) 데이터 소스/특징

### 가격/차트 데이터
- yfinance 일봉 OHLCV 사용
- `auto_adjust=True`로 **스플릿(액면분할/병합) 왜곡을 줄인 OHLC**를 사용합니다.

### 매크로(리스크) 데이터
- FRED CSV API 사용
  - `BAMLH0A0HYM2` (HY OAS)
  - `BAMLC0A0CM` (IG OAS)
  - `DFII10` (10Y Real Yield)
  - `VIXCLS` (VIX)
  - `NFCI` (NFCI)

> 이 값이 수집 실패하면, 전날 JSON에 저장된 캐시 값을 사용합니다.

---

## 3) 공통 지표 정의

### 3.1 이동평균(MA) & 괴리율(Gap)
- `MA20`, `MA50`, `MA120`, `MA200`: 종가 기준 단순이동평균
- `gap20 = Close/MA20 - 1`
- `gap50 = Close/MA50 - 1`
- `gap200 = Close/MA200 - 1`

**해석**
- gap이 +이면 이동평균 위(추세 우호)
- gap이 너무 크면(예: +20% 이상) “과열 추격” 가능성이 커져서 Breakout 필터로 제한합니다.

### 3.2 RSI(14)
`RSI14`: Wilder smoothing 방식

**해석(대략)**
- 40~60: 추세 속 눌림/중립 구간
- 60 이상: 모멘텀 강화(돌파 확인에 유리)

### 3.3 ATR(14) & ATR% (변동성)
- `ATR14`: 평균 진폭
- `ATR14_pct = ATR14 / Close`

**해석**
- ATR%가 높을수록 하루 변동폭이 커서 **타점 정확도/손절 효율이 급감**합니다.
- 그래서 VZLA/SCZM/HYMC별로 상한을 다르게 둡니다.

### 3.4 거래량 비율
- `vol_ratio = Volume / Vol20(20일 평균 거래량)`

**해석**
- Breakout 신뢰도를 높이기 위한 핵심 지표
- 다만 HYMC는 “밈성 급등”을 걸러내기 위해 `vol_ratio` 상한도 둡니다.

### 3.5 갭(갭 리스크)
- `gap_open = |Open - PrevClose| / PrevClose`

**해석**
- 갭이 큰 날은 이벤트성 변동일 수 있어 신규 진입을 피하는 편이 안전합니다.

### 3.6 쇼크 캔들 필터(급락/급등)
하루 수익률(`ret1d`)과 거래량 비율을 같이 사용합니다.

- `shock_down`: 큰 음봉 + 거래량 폭증
- `shock_up`: 큰 양봉 + 거래량 폭증 (특히 HYMC)

**해석**
- shock_down은 “패닉/악재”일 수 있어 진입 금지
- shock_up은 “펌프/과열” 가능성이 있어(특히 HYMC) 진입 금지

---

## 4) 레짐(환경) 게이트 상세

### 4.1 RiskGreen (FRED 기반)
아래 조건을 모두 만족하면 `risk_green=True`.

- `VIX < 30`
- `HY OAS 4주 변화 < +150bp`
- `IG OAS 4주 변화 < +80bp`
- `10Y Real Yield 4주 변화 < +50bp`
- `NFCI <= 0.5`

**왜 이렇게 두나?**
- 주니어/개발사는 “위험회피(credit widening, volatility spike)”에 먼저 무너지는 경우가 많아
  **아예 신규진입을 차단**하는 구간을 만들었습니다.

### 4.2 SilverUptrend (SI=F)
아래 조건을 모두 만족하면 은 추세가 살아있다고 봅니다.

- `Close > MA200`
- `MA50 > MA200`
- `MA50_slope20 > 0` (20거래일 동안 MA50이 상승)

### 4.3 MinersLeadership (SILJ/SLV)
`SILJ/SLV` 비율이 **60일 평균 대비 강하고**, 그 평균의 기울기가 양(+)이면 리더십이 있다고 봅니다.

- `gap >= 0` AND `slope_proxy > 0`

**해석**
- 은 가격이 오르더라도 광산주가 못 가는 구간이 있습니다.
  이걸 걸러내는 용도입니다.

---

## 5) 종목별 전용 룰(핵심)

### 5.1 VZLA (가장 공격적 / 리스크 필터 가장 강함)
**핵심 컨셉**: “리더십 + 추세 + 눌림/돌파”를 보되, **갭/쇼크/변동성 상한**을 엄격히 적용.

#### (1) Risk Filter
- `ATR14_pct <= 0.15`
- `gap_open <= 0.08`
- `shock_down`/`shock_up`이면 진입 금지

#### (2) Trend
- `Close > MA200` AND `MA50 > MA200`

#### (3) Relative Strength (vs SILJ)
- RS gap ≥ 0 AND RS slope_proxy > 0

#### (4) Trigger
- Pullback: `gap20 ∈ [-2%, +5%]` AND `RSI ∈ [40,60]` AND `Close > MA20`
- Breakout: `Close > 60일 고점 * 1.01` AND `vol_ratio ≥ 2.0` AND `RSI ≥ 60`
  - 단, `gap20`이 너무 크면(>15%) 과열로 간주하여 제외

---

### 5.2 SCZM (레버리지/은 가격 의존이 큰 편 → Silver Margin Gate 추가)
**핵심 컨셉**: SCZM이 “은 가격 레버리지”가 크다는 가정 하에, **은 가격 자체가 충분히 높아야** 진입을 허용.

#### (1) Silver Margin Gate
- watch: `SI >= 32`
- entry: `SI >= 35` (이 조건을 만족해야 `ENTRY_CANDIDATE` 가능)

#### (2) Trend
- 히스토리가 충분하면 MA200, 부족하면 MA120을 사용
- `Close > MA_long` AND `MA50 > MA_long` AND `MA50_slope20 > 0`

#### (3) Risk Filter
- `ATR14_pct <= 0.20`
- `gap_open <= 0.10`
- `shock_down`이면 진입 금지

#### (4) Trigger
- Pullback: `gap20 ∈ [-2%, +7%]` AND `RSI ∈ [35,60]` AND `Close > MA20` AND `vol_ratio >= 1.2`
- Breakout: `Close > 40일 고점 * 1.01` AND `vol_ratio ≥ 1.5` AND `RSI ≥ 55`
  - 과열 방지: gap20 > 18%면 제외

---

### 5.3 HYMC (개발사/수급 이벤트 큼 → Metals 동시 추세 + 과열 필터)
**핵심 컨셉**: HYMC는 “은광주라기보다 금/은 옵션성 + 수급”이라,
**(1) 금·은 동시 추세**, **(2) 섹터 리더십**, **(3) 펌프/과열 제외**를 강하게 적용.

#### (1) MetalsUptrend
- `SilverUptrend == True` AND `GoldUptrend == True`

#### (2) SectorLeadership
- `SILJ/SLV` 또는 `GDXJ/GLD` 중 하나라도 리더십이 있으면 통과

#### (3) Relative Strength
- `HYMC/GDXJ` 또는 `HYMC/SILJ` 중 하나라도 RS가 양호하면 통과

#### (4) Risk Filter
- `ATR14_pct <= 0.25`
- `gap_open <= 0.12`
- `shock_up`/`shock_down`이면 진입 금지

#### (5) Trigger
- Breakout(Base breakout): `Close > 120일 고점 * 1.01` AND `2.0 <= vol_ratio <= 8.0` AND `RSI >= 55`
  - 거래량이 “너무 과도”하면(>8배) 밈/펌프 가능성으로 제외
- Retest: `Close > MA200` AND `|Close/MA50-1| <= 5%` AND `RSI >= 50`

---

## 6) 결과(JSON/MD) 해석 방법

### 6.1 JSON 핵심 키
- `verdict`: 오늘의 요약 결론
- `regime`: 공통 게이트 상태(리스크/추세/리더십)
- `signals.<TICKER>`
  - `ta`: 기술지표 값
  - `checks`: 각 게이트/트리거 boolean
  - `entry_candidate`, `entry_confirmed`
  - `fails`: 왜 오늘은 아닌지(디버깅용)

### 6.2 MD 리포트에서 보는 순서
1) Regime이 좋은가?
2) 각 종목의 `trend_ok`, `rs_ok`, `risk_ok`가 True인가?
3) `trigger`가 무엇으로 켜졌는지(pullback vs breakout vs retest)
4) 가능하면 다음날 `ENTRY_CONFIRMED`까지 확인

---

## 7) 자주 조정하는 튜닝 포인트(권장)

1) `VIX_MAX` (30 → 25로 내리면 신호가 줄고 더 보수적)
2) `SILVER_ENTRY` (35가 너무 빡세면 33~34로)
3) `ATR14_PCT_MAX` (주니어는 이 값이 체감 난이도에 가장 큰 영향)
4) Breakout 기간(60/40/120) 조정
5) Confirm 룰(2일 확인을 1일로 줄이거나, Breakout만 확인 적용 등)
