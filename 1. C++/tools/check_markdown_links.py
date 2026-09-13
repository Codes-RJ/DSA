#!/usr/bin/env python3
"""Fail when a local Markdown link points to a missing file or directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?P<target>[^)]+)\)")
CODE_SPAN = re.compile(r"`[^`]*`")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "ftp"}


def local_target(raw_target: str) -> str | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith("#"):
        return None
    parsed = urlsplit(target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES:
        return None
    return unquote(parsed.path)


def broken_links(root: Path) -> list[tuple[Path, int, str]]:
    failures: list[tuple[Path, int, str]] = []
    for document in sorted(root.rglob("*.md")):
        in_fence = False
        text = document.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            prose = CODE_SPAN.sub("", line)
            for match in LINK.finditer(prose):
                raw = match.group("target")
                target = local_target(raw)
                if target is None:
                    continue
                candidate = (document.parent / target).resolve()
                if not candidate.exists():
                    failures.append((document, line_number, raw))
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    failures = broken_links(root)
    for document, line_number, target in failures:
        relative = document.relative_to(root)
        print(f"{relative}:{line_number}: missing local target: {target}")
    print(f"Checked Markdown links under {root}: {len(failures)} broken")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
