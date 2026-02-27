# PR 충돌 해결 가이드

현재 PR에서 충돌이 난 파일:
- `.github/workflows/daily_signals.yml`
- `monitor_signals.py`
- `latest_signal.json`
- `latest_signal.md`

## 왜 자주 충돌하나요?
- `latest_signal.json` / `latest_signal.md`는 GitHub Actions가 매일 갱신하는 **자동 생성 파일**이라, 메인 브랜치와 PR 브랜치가 동시에 바뀌기 쉽습니다.
- 워크플로우/스크립트 파일도 같은 기간에 수정되면 충돌이 발생합니다.

## 가장 안전한 해결 절차 (명령줄)

```bash
git checkout <your-pr-branch>
git fetch origin
git rebase origin/main
```

충돌이 나면 파일별로 다음처럼 처리하세요.

### 1) 자동 생성 파일은 "현재 브랜치 버전" 유지 권장

```bash
git checkout --ours latest_signal.json latest_signal.md
git add latest_signal.json latest_signal.md
```

> 이후 머지/리베이스가 끝나면 Actions가 다시 최신 값으로 덮어씁니다.

### 2) 코드 파일은 수동 병합

- `.github/workflows/daily_signals.yml`
- `monitor_signals.py`

충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)를 정리하고 저장한 뒤:

```bash
git add .github/workflows/daily_signals.yml monitor_signals.py
git rebase --continue
```

모든 충돌 해결 후:

```bash
git push --force-with-lease
```

## GitHub 웹에서 해결하는 경우

1. PR의 **Resolve conflicts** 클릭
2. `latest_signal.json`, `latest_signal.md`는 PR 브랜치(ours) 쪽 유지
3. `daily_signals.yml`, `monitor_signals.py`는 두 변경을 합쳐 저장
4. Mark as resolved → Commit merge

## 재발 줄이기

이 저장소에는 `.gitattributes`로 아래 정책이 추가되어 있습니다.

- `latest_signal.json merge=ours`
- `latest_signal.md merge=ours`

즉, 추후 머지 충돌 시 자동 생성 산출물은 현재 브랜치 버전을 우선하도록 유도합니다.

---

## 완전 초보용: GitHub 웹에서 `monitor_signals.py` 다시 고치는 순서

아래 순서대로 **클릭만** 하세요.

1. GitHub 저장소 메인 화면으로 이동합니다.
2. 상단에서 **브랜치 선택 드롭다운**(보통 `main`이라고 표시) 클릭 후, 충돌 난 PR 브랜치로 바꿉니다.
3. 파일 목록에서 `monitor_signals.py` 클릭.
4. 우측 상단 **연필 아이콘(Edit this file)** 클릭.
5. 키보드에서 `Ctrl + F`(맥은 `Cmd + F`)를 눌러 아래 함수 이름 검색:
   - `def fetch_yfinance_close(ticker: str) -> pd.Series:`
6. 그 함수 시작 줄부터 함수 끝(`return series.sort_index()`)까지 전부 지우고, 아래 코드로 교체합니다.

```python
def fetch_yfinance_close(ticker: str) -> pd.Series:
    data = yf.download(
        ticker,
        period="2y",
        interval="1d",
        auto_adjust=False,
        progress=False,
        threads=False,
    )
    if data.empty:
        return pd.Series(dtype=float)

    frame = data.copy()

    # yfinance can return MultiIndex columns depending on version/options.
    # Normalize to a single-ticker 2D frame with OHLCV-like columns.
    if isinstance(frame.columns, pd.MultiIndex):
        # Common shape: (field, ticker) e.g. ('Close', 'VRT')
        if ticker in frame.columns.get_level_values(-1):
            frame = frame.xs(ticker, axis=1, level=-1)
        # Alternative shape: (ticker, field)
        elif ticker in frame.columns.get_level_values(0):
            frame = frame.xs(ticker, axis=1, level=0)

    # After normalization, select Adj Close first, else Close.
    if "Adj Close" in frame.columns:
        close_like = frame["Adj Close"]
    elif "Close" in frame.columns:
        close_like = frame["Close"]
    else:
        return pd.Series(dtype=float)

    if isinstance(close_like, pd.DataFrame):
        # Defensive fallback in case duplicate columns remain.
        close_like = close_like.iloc[:, 0]

    series = pd.to_numeric(close_like, errors="coerce").dropna()
    series.index = pd.to_datetime(series.index)
    return series.sort_index()
```

7. 페이지 맨 아래 **Commit changes...** 클릭.
8. 커밋 메시지 예시:
   - `Fix yfinance MultiIndex handling in fetch_yfinance_close`
9. **Commit directly to <브랜치명>** 선택 후 다시 **Commit changes** 클릭.

### 그 다음(중요)
10. PR 페이지로 돌아가서 충돌 해결 화면이 있으면:
    - `latest_signal.json`, `latest_signal.md`는 **현재 PR 브랜치 버전 유지**
    - `monitor_signals.py`는 방금 수정한 버전 유지
11. PR 머지 후, 저장소 탭에서 **Actions → Daily Signals → Run workflow** 수동 1회 실행.
12. 실행 성공 후 `latest_signal.md`에서 아래 경고가 사라졌는지 확인:
    - `arg must be a list, tuple, 1-d array, or Series`


## 같은 에러가 계속 보일 때(중요)

로그가 아래처럼 **한 번 push 시도 후 바로 종료**되면,

- `git push ...`
- `! [rejected] main -> main (fetch first)`
- 즉시 `Error: Process completed with exit code 1`

대부분은 **새 워크플로우가 아직 main에 반영되지 않은 상태**입니다.
(새 워크플로우는 `Push rejected (attempt x/5)...` 같은 재시도 로그가 보여야 정상입니다.)

해결:
1. 워크플로우 수정 PR을 먼저 main에 머지
2. `Actions > Daily Signals > Run workflow` 수동 실행
3. 새 로그에 `Push rejected (attempt ... )` 또는 `Push succeeded`가 보이는지 확인
