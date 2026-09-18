# N1 결측 차단 및 복구

## 변경 범위

N1 v2.3 shadow runner의 데이터 수집, 검증, 저장 및 알림만 보완합니다.
전략 YAML, 다른 모니터, Streamlit/Supabase는 변경하지 않습니다. 실제 주문은 제출하지 않습니다.

- 완료된 미국 정규 거래일은 거래소 캘린더의 실제 폐장 시각 + 15분으로 결정합니다.
  휴장일과 조기 폐장을 반영하고, 최신 가격 행의 날짜만 보고 완료 여부를 추정하지 않습니다.
- Tiingo 우선, Yahoo bulk 대체 조회, Yahoo 단일 종목 history 재조회 순서입니다.
  소스 간 종가를 혼합하거나, NaN을 0/전일 종가로 채우거나, 자동 price repair로 추정하지 않습니다.
- 최근 260거래일의 OHLC 및 세션 누락을 확인합니다. Wilder RSI에 영향을 주는 전체 Close의 결측도 거부합니다.
- SMA20/50/200, 현재·직전 RSI, 적용 P를 계산 후 다시 검증합니다.
- 필요한 Router 입력이 없으면 XLV로 임의 판정하지 않고 중단합니다.
- JSON의 NaN, Infinity, 숫자 대신 문자열/boolean, 해시 및 상태 불일치를 거부합니다.
- 모든 세션을 메모리에서 계산·검증한 후 최신 파일을 저장합니다.
  파일을 미리 준비한 뒤 교체하며 일반 쓰기 실패는 되돌립니다. 여러 파일의 교체는 단일 파일시스템 트랜잭션이 아니므로
  강제 종료에 따른 부분 저장은 다음 실행의 signal/state/status 해시 검사로 차단합니다.

## 읽어야 할 파일

1. `n1_run_status.json`: 최신 실행 상태. `VALIDATED` 또는 `BLOCKED`.
2. `n1_latest_signal.json`: 마지막으로 저장된 정상 판정. 기준일을 반드시 함께 확인합니다.
3. `n1_latest_state_snapshot.json`: 같은 판정의 상태. signal의 `state_sha256`과 일치해야 합니다.
4. `n1_liquidity_p_lineage.csv`: 적용 주간과 P의 계보.

`BLOCKED`에서는 새로운 `execution_target`을 내지 않습니다. 마지막 정상 체크포인트는 그대로 보존하며,
GitHub Issue에는 **갱신 실패 · 신규 판정 중단**과 안전한 오류 코드가 표시됩니다.
과거부터 손상된 체크포인트는 정상이라고 재사용하지 않습니다. 아래 복구를 수행해야 합니다.
기존 최신 파일만 읽던 외부 소비자도 `n1_run_status.json`을 먼저 확인해야 합니다.

CSV의 초기 26/38/260/261행 빈 값은 성장률·평활·순위·shift 계산에 따른 누적 기간입니다.
JSON의 필수 값 결측과 다릅니다. 이 변경은 유동성 전략의 산식이나 주간 적용 규칙을 변경하지 않습니다.
CSV의 미래 주간 라벨은 현재 적용값이 아니며 signal에 기록된 적용 주간을 사용합니다.

## 이번 손상 기간

2026-09-18 점검 기준, 9월 2일~17일의 11개 거래일 신호에서 QQQ Close 및 SMA 세 값이 NaN이었습니다.
당시 Yahoo 대체 조회를 사용했으며 NaN 비교로 YELLOW가 선택되고 상태가 진행됐습니다.

9월 1일 신호를 포함하는 복구 후보 커밋:

`c0368528a2e82ad8007a4f3ad4006dfab03a049e`

이 후보의 필수 숫자, 규칙 해시, 입력 해시 및 signal/state 일치 검사는 통과했습니다.
이는 모든 과거 전략 판단을 독립적으로 검증했다는 뜻은 아닙니다.

## 운영 복구 순서

1. **이 저장소**의 Settings → Secrets and variables → Actions → New repository secret에
   `TIINGO_API_TOKEN`을 등록합니다. 다른 저장소의 Secret은 자동 공유되지 않습니다.
   토큰 값은 코드, Issue, 로그, 채팅에 남기지 않습니다. 점검 시 이 저장소의 Repository Secrets 목록은 비어 있었습니다.
2. 수정 코드를 운영 브랜치 `tqg651`에 반영합니다.
3. Actions → Daily Signals → Run workflow에서 운영 브랜치를 선택합니다.
4. `n1_repair_from`에 위 40자리 커밋 SHA를 입력해 한 번 실행합니다.
5. 출력 계약 검증 통과, 새 기준일, 유한한 가격/SMA/RSI/P, Issue의 정상 결과를 확인합니다.
6. 이후 정기 실행에서는 `n1_repair_from`을 비워 둡니다.

로컬에서는 다음과 같이 먼저 시험할 수 있습니다. 원본 저장소의 전체 Git 이력이 필요합니다.

```powershell
python n1_meta_signal.py --repair-from c0368528a2e82ad8007a4f3ad4006dfab03a049e --dry-run
python n1_meta_signal.py --repair-from c0368528a2e82ad8007a4f3ad4006dfab03a049e
python n1_validate_outputs.py
```

`--dry-run`은 최신 신호/상태/계보/실행상태를 바꾸지 않고 `n1_audit/`에만 성공한 계산 근거를 남깁니다.
일반 실행 실패는 `n1_run_status.json`에 기록됩니다. CI는 실패 Issue를 작성하고 최종 실패로 종료합니다.
다른 모니터의 성공 결과는 유지하되, 검증되지 않은 N1 결과는 커밋 대상에서 제외합니다.

## 복구의 한계

- 최대 120개 거래일을 순서대로 재계산합니다. 중간 날짜의 입력 검증 실패 시 일부 상태만 반영하지 않습니다.
- 유동성은 해당 날짜에 처음 커밋된 계보를 사용합니다. 과거 계보가 없는 중간 날짜는 현재 FRED 값으로 대체하지 않습니다.
- 가격은 현재 공급자가 제공하는 수정주가 이력입니다. 과거 당시의 가격 빈티지와 완전히 같다고 보장할 수 없어
  `RECOVERY_CURRENT_PRICE_VINTAGE` 경고와 복구 이력을 남깁니다.
- 재생 중 Router 신규 진입이 필요하면 당시 거시 입력 빈티지가 없으므로 중단합니다.
  `RECOVERY_ROUTER_MACRO_VINTAGE_UNAVAILABLE`은 별도 과거 원자료 확보가 필요한 경우입니다.
- 정상 가격을 공급자가 반환하지 않는다면 복구를 성공 처리하지 않습니다. Secret을 추가해도 API 응답 검증 통과가 필요합니다.
- 같은 거래일 재실행은 검증된 상태만 유지합니다. 손상된 JSON은 그대로 재발행하지 않습니다.

## 검증

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
```

자동 테스트는 네트워크를 금지한 합성 입력으로 결측/Infinity, 오래된 가격, 중간 거래일 누락, 휴일,
조기 폐장, JSON 및 해시 계약, 저장 실패 복구, 11거래일 재생, 같은 날 중복 실행, provider 대체 조회를 확인합니다.
실데이터 복구 결과는 `n1-audit-<run_id>-<attempt>` artifact에서 원가격과 세션별 계산을 확인합니다.
artifact는 14일 보관하며 Secret 값은 포함하지 않습니다.
