#!/usr/bin/env python3
"""Sanitize Agent runtime logs before sharing them publicly."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = [
    (re.compile(r"linkSecret=[^\s)]+"), "linkSecret=***REDACTED***"),
    (re.compile(r"linkCode=\d+"), "linkCode=***REDACTED***"),
    (re.compile(r"account=[A-Za-z0-9_\-]+"), "account=***REDACTED***"),
    (re.compile(r"open_id resolved: \S+"), "open_id resolved: ***REDACTED***"),
    (re.compile(r"ou_[A-Za-z0-9_\-]+"), "ou_***REDACTED***"),
    (re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I), "***UUID***"),
    (re.compile(r"(token|secret|key|password)([\"=: ][^\s,}\n]+)", re.I), r"\1***REDACTED***"),
]


def sanitize(text: str) -> str:
    for pattern, replacement in PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: sanitize_logs.py INPUT OUTPUT", file=sys.stderr)
        return 2

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    target.write_text(sanitize(source.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

