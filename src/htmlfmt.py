from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from bs4 import BeautifulSoup as bs  # noqa: N813
from bs4.formatter import HTMLFormatter


def fix_file(fname: Path, indent: int = 2) -> bool:
    """Fix a file, returning whether it was modified or not."""
    original = fname.read_text()
    soup = bs(original, features="html5lib")
    formatter = HTMLFormatter(indent=indent)
    pretty = soup.prettify(formatter=formatter)
    if pretty != original:
        fname.write_text(pretty)
        return True
    return False


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    parser.add_argument(
        "--indent", action="store", type=int, default=2, help="The html indentation level per tag"
    )

    args = parser.parse_args()
    return_code = 0
    for filename in args.filenames:
        if fix_file(Path(filename), indent=args.indent):
            print(f"Fixed {filename}")
            return_code = 1

    return return_code


if __name__ == "__main__":
    sys.exit(main())
