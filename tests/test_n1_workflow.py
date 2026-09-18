import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def workflow_steps():
    workflow = yaml.load((ROOT / ".github/workflows/daily_signals.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    return workflow, {step["name"]: step for step in workflow["jobs"]["run-signals"]["steps"]}


def test_daily_workflow_retains_schedule_and_requires_explicit_repair():
    workflow, steps = workflow_steps()
    assert workflow["on"]["schedule"] == [{"cron": "37 22 * * *"}]
    assert workflow["on"]["workflow_dispatch"]["inputs"]["n1_repair_from"]["default"] == ""
    command = steps["Generate validated N1 signal"]["run"]
    assert '--repair-from "$N1_REPAIR_FROM"' in command
    assert steps["Validate N1 output contract"]["run"].strip() == "python n1_validate_outputs.py"
    assert steps["Fail visibly when N1 was not validated"]["if"].startswith("always()")
    assert "exit 1" in steps["Fail visibly when N1 was not validated"]["run"]
    assert "OUTPUT_CONTRACT_REJECTED" in steps["Mark rejected N1 output"]["run"]


def test_commit_does_not_publish_failed_n1_or_rebase_stale_state():
    _, steps = workflow_steps()
    command = steps["Commit and push if changed"]["run"]
    assert 'if [ "$N1_VALID" = "true" ]; then' in command
    assert "FILES+=(n1_latest_signal.json" in command
    assert "pull --rebase" not in command
    assert 'git push origin "HEAD:${BRANCH}"' in command


@pytest.mark.parametrize("valid", [False, True])
def test_issue_summary_distinguishes_failed_and_valid_signal(valid):
    node = os.environ.get("N1_TEST_NODE") or shutil.which("node")
    if not node:
        pytest.skip("Node is required to execute the GitHub Issue rendering test")
    _, steps = workflow_steps()
    script = steps["Create Issue for today's report (always)"]["with"]["script"]
    payload = {
        "script": script, "valid": valid,
        "files": {
            "n1_latest_signal.json": '{"execution_target":"QQQ"}' if valid else '{"qqq_adjusted_close":NaN}',
            "n1_latest_signal.md": "CURRENT_VALID_REPORT" if valid else "OLD_STALE_NAN_REPORT",
            "n1_run_status.json": json.dumps({"status": "VALIDATED" if valid else "BLOCKED",
                                               "reason": "INVALID_OHLC:QQQ", "previous_signal_date": "2026-09-01"}),
            "latest_signal_all.md": "Other monitor reports",
        },
    }
    result = subprocess.run([node, str(ROOT / "tests/issue_render_harness.cjs")],
                            input=json.dumps(payload), text=True, encoding="utf-8", capture_output=True, check=True)
    body = json.loads(result.stdout)["body"]
    if valid:
        assert "N1 QQQ Meta shadow: **QQQ**" in body
        assert "CURRENT_VALID_REPORT" in body
    else:
        assert "갱신 실패 · 신규 판정 중단" in body
        assert "Workflow status: **failure**" in body
        assert "INVALID_OHLC:QQQ" in body
        assert "OLD_STALE_NAN_REPORT" not in body
        assert "N1 QQQ Meta shadow: **QQQ**" not in body


def test_test_workflow_uses_dev_dependencies():
    config = yaml.load((ROOT / ".github/workflows/n1-tests.yml").read_text(), Loader=yaml.BaseLoader)
    commands = [step.get("run", "") for step in config["jobs"]["test"]["steps"]]
    assert "python -m pip install -r requirements-dev.txt" in commands
    assert "python -m pytest -q tests" in commands
