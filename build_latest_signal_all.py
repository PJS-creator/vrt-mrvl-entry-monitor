from __future__ import annotations

import json
from pathlib import Path


CORE_JSON = Path("latest_signal.json")
CORE_MD = Path("latest_signal.md")

NWG_JSON = Path("nwg_latest_signal.json")
NWG_MD = Path("nwg_latest_signal.md")

ENERGY_JSON = Path("latest_energy_signal.json")
ENERGY_MD = Path("latest_energy_signal.md")

SILVER_JSON = Path("latest_silver_signal.json")
SILVER_MD = Path("latest_silver_signal.md")

PRECIOUS_JSON = Path("latest_precious_miners_signal.json")
PRECIOUS_MD = Path("latest_precious_miners_signal.md")

QQQ_QLD_JSON = Path("qqq_qld_timing_signal.json")
QQQ_QLD_MD = Path("qqq_qld_timing_signal.md")

OUT_MD = Path("latest_signal_all.md")


def read_text(path: Path) -> str:
    if not path.exists():
        return f"_(missing: {path.name})_"
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return path.read_text(encoding="utf-8", errors="replace").strip()


def load_verdict(path: Path) -> str:
    if not path.exists():
        return "N/A"
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        v = obj.get("verdict")
        return str(v) if v is not None else "N/A"
    except Exception:
        return "N/A"


def main() -> None:
    core_verdict = load_verdict(CORE_JSON)
    nwg_verdict = load_verdict(NWG_JSON)
    energy_verdict = load_verdict(ENERGY_JSON)
    silver_verdict = load_verdict(SILVER_JSON)
    precious_verdict = load_verdict(PRECIOUS_JSON)
    qqq_qld_verdict = load_verdict(QQQ_QLD_JSON)

    core_md = read_text(CORE_MD)
    nwg_md = read_text(NWG_MD)
    energy_md = read_text(ENERGY_MD)
    silver_md = read_text(SILVER_MD)
    precious_md = read_text(PRECIOUS_MD)
    qqq_qld_md = read_text(QQQ_QLD_MD)

    lines: list[str] = []
    lines += ["# Daily Signals (All-in-One)", ""]
    lines += ["## Quick Summary", ""]
    lines += [f"- QQQ/QLD Timing: **{qqq_qld_verdict}**"]
    lines += [f"- Core (VRT/MRVL): **{core_verdict}**"]
    lines += [f"- NatWest (NWG): **{nwg_verdict}**"]
    lines += [f"- Energy (OXY/PBR/RIG/VG): **{energy_verdict}**"]
    lines += [f"- Silver (VZLA/SCZM/HYMC): **{silver_verdict}**"]
    lines += [f"- Precious Miners (Gold/Silver): **{precious_verdict}**"]
    lines += ["", "---", ""]

    lines += ["## QQQ/QLD timing report", "", qqq_qld_md, "", "---", ""]
    lines += ["## Core report", "", core_md, "", "---", ""]
    lines += ["## NatWest report", "", nwg_md, "", "---", ""]
    lines += ["## Energy report", "", energy_md, ""]
    lines += ["", "---", "", "## Silver report", "", silver_md, ""]
    lines += ["", "---", "", "## Precious miners report", "", precious_md, ""]

    OUT_MD.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
