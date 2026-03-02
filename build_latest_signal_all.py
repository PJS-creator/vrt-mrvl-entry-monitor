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

    core_md = read_text(CORE_MD)
    nwg_md = read_text(NWG_MD)
    energy_md = read_text(ENERGY_MD)
    silver_md = read_text(SILVER_MD)

    lines: list[str] = []
    lines += ["# Daily Signals (All-in-One)", ""]
    lines += ["## Quick Summary", ""]
    lines += [f"- Core (VRT/MRVL): **{core_verdict}**"]
    lines += [f"- NatWest (NWG): **{nwg_verdict}**"]
    lines += [f"- Energy (OXY/PBR/RIG/VG): **{energy_verdict}**"]
    lines += [f"- Silver (VZLA/SCZM/HYMC): **{silver_verdict}**"]
    lines += ["", "---", ""]

    lines += ["## Core report", "", core_md, "", "---", ""]
    lines += ["## NatWest report", "", nwg_md, "", "---", ""]
    lines += ["## Energy report", "", energy_md, ""]
    lines += ["", "---", "", "## Silver report", "", silver_md, ""]

    OUT_MD.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
