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
