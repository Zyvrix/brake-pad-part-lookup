"""Export brake pad part rows from the Excel workbook to parts.json."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
WORKBOOK = ROOT / "brake_pads_parts.xlsx"
OUTPUT = ROOT / "parts.json"


def main():
    parts = pd.read_excel(WORKBOOK)
    if "Part No" not in parts.columns:
        raise ValueError("The Excel sheet must have a 'Part No' column.")

    # Keep part records only; blank rows and the explanatory note are not parts.
    parts = parts[parts["Part No"].astype("string").str.match(r"^BP-\d+$", case=False, na=False)]
    parts = parts.where(pd.notna(parts), None)
    OUTPUT.write_text(
        json.dumps(parts.to_dict(orient="records"), indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )
    print("Wrote {} parts to {}".format(len(parts), OUTPUT))


if __name__ == "__main__":
    main()
