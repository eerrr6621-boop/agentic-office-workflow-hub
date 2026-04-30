#!/usr/bin/env python3
"""Small pre-publish check for obvious secret leaks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mov", ".mp4", ".pdf"}
PATTERNS = {
    "api_key_assignment": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    "github_pat": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "openai_like": re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    "google_api_key": re.compile(r"AIza[0-9A-Za-z_\-]{20,}"),
}


def iter_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and path.suffix.lower() not in SKIP_SUFFIXES
    ]


def main() -> int:
    findings: list[str] = []
    for path in iter_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{name}: {path.relative_to(ROOT)}")

    if findings:
        print("Potential secrets found:")
        print("\n".join(findings))
        return 1

    print("No obvious secrets detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

