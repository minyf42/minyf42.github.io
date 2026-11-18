#!/usr/bin/env python3
"""Point cv_pdf in _data/socials.yml at the newest dated CV.

Looks in assets/pdf/ for Minyue_Fan_CV_MMDD.pdf or Minyue_Fan_CV_YYYYMMDD.pdf
and rewrites the cv_pdf line. A four-digit date is month and day. It is read
as the latest occurrence that is not more than 45 days ahead of today, so a
January CV still wins after the year turns.
"""

import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "assets" / "pdf"
SOCIALS = ROOT / "_data" / "socials.yml"
NAME = re.compile(r"^Minyue_Fan_CV_(\d{4}|\d{8})\.pdf$")
AHEAD = timedelta(days=45)


def cv_date(token, today):
    if len(token) == 8:
        year, month, day = int(token[:4]), int(token[4:6]), int(token[6:8])
        return date(year, month, day)
    month, day = int(token[:2]), int(token[2:])
    candidates = []
    for year in (today.year - 1, today.year, today.year + 1):
        try:
            candidates.append(date(year, month, day))
        except ValueError:
            continue
    horizon = today + AHEAD
    eligible = [item for item in candidates if item <= horizon]
    if not eligible:
        raise ValueError(f"no usable date for {token}")
    return max(eligible)


def latest_cv(today=None):
    today = today or date.today()
    found = []
    for path in PDF_DIR.glob("Minyue_Fan_CV_*.pdf"):
        match = NAME.match(path.name)
        if not match:
            continue
        found.append((cv_date(match.group(1), today), path.name))
    if not found:
        raise SystemExit(f"No Minyue_Fan_CV_MMDD.pdf in {PDF_DIR}")
    found.sort()
    return found[-1][1]


def write_cv_pdf(filename):
    target = f"/assets/pdf/{filename}"
    text = SOCIALS.read_text()
    updated, count = re.subn(
        r"^cv_pdf:.*$",
        f"cv_pdf: {target}",
        text,
        count=1,
        flags=re.M,
    )
    if count != 1:
        raise SystemExit("cv_pdf is missing from _data/socials.yml")
    if updated != text:
        SOCIALS.write_text(updated)
        print(f"cv_pdf -> {target}")
    else:
        print(f"cv_pdf already {target}")
    return target


def main():
    filename = latest_cv()
    write_cv_pdf(filename)


if __name__ == "__main__":
    sys.exit(main())
