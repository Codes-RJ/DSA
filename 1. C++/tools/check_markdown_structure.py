#!/usr/bin/env python3
"""Check Markdown fence balance and prevent unlabeled-fence regressions."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


FENCE = re.compile(r"^\s*(?P<marker>`{3,}|~{3,})(?P<info>.*)$")


@dataclass(frozen=True)
class OpenFence:
    document: Path
    line_number: int
    marker: str


def inspect(root: Path) -> tuple[list[OpenFence], list[OpenFence]]:
    unclosed: list[OpenFence] = []
    unlabeled: list[OpenFence] = []

    for document in sorted(root.rglob("*.md")):
        current: OpenFence | None = None
        for line_number, line in enumerate(
            document.read_text(encoding="utf-8").splitlines(), start=1
        ):
            match = FENCE.match(line)
            if match is None:
                continue

            marker = match.group("marker")
            info = match.group("info").strip()
            if current is None:
                current = OpenFence(document, line_number, marker)
                if not info:
                    unlabeled.append(current)
                continue

            same_character = marker[0] == current.marker[0]
            long_enough = len(marker) >= len(current.marker)
            if same_character and long_enough and not info:
                current = None

        if current is not None:
            unclosed.append(current)

    return unclosed, unlabeled


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument(
        "--max-unlabeled",
        type=int,
        help="fail when the number of unlabeled opening fences exceeds this baseline",
    )
    parser.add_argument(
        "--require-labels",
        action="store_true",
        help="fail on every unlabeled opening fence",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    unclosed, unlabeled = inspect(root)

    for fence in unclosed:
        relative = fence.document.relative_to(root)
        print(f"{relative}:{fence.line_number}: unclosed {fence.marker!r} fence")

    allowed_unlabeled = 0 if args.require_labels else args.max_unlabeled
    too_many_unlabeled = (
        allowed_unlabeled is not None and len(unlabeled) > allowed_unlabeled
    )
    if too_many_unlabeled:
        for fence in unlabeled[:25]:
            relative = fence.document.relative_to(root)
            print(f"{relative}:{fence.line_number}: unlabeled fence")
        if len(unlabeled) > 25:
            print(f"... and {len(unlabeled) - 25} more unlabeled fences")

    print(
        f"Checked Markdown structure under {root}: "
        f"{len(unclosed)} unclosed, {len(unlabeled)} unlabeled fences"
    )
    return 1 if unclosed or too_many_unlabeled else 0


if __name__ == "__main__":
    sys.exit(main())
