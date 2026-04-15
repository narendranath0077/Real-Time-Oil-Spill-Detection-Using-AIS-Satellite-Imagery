"""Filter AIS vessel records around known oil-spill coordinates.

The raw AIS exports are large, so this script reads them in chunks and writes a
deduplicated, sorted output CSV.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


DEFAULT_SPILL_LOCATIONS = (
    (25.78166, -80.15023),
    (27.78969, -97.39082),
    (32.02417, -81.04617),
    (26.09262, -80.11391),
    (48.68902, -123.40947),
)


def filter_ais_data(
    input_csv: Path,
    output_csv: Path,
    spill_locations: tuple[tuple[float, float], ...] = DEFAULT_SPILL_LOCATIONS,
    chunksize: int = 100_000,
) -> None:
    """Filter AIS rows whose latitude and longitude match target locations."""
    matches: list[pd.DataFrame] = []
    location_index = set(spill_locations)

    for chunk in pd.read_csv(input_csv, chunksize=chunksize):
        coordinate_pairs = list(zip(chunk["LAT"], chunk["LON"]))
        filtered_chunk = chunk[[pair in location_index for pair in coordinate_pairs]]
        if not filtered_chunk.empty:
            matches.append(filtered_chunk)

    if matches:
        filtered_df = (
            pd.concat(matches)
            .drop_duplicates(subset=["LAT", "LON", "BaseDateTime"])
            .sort_values(by=["LON", "LAT"])
        )
    else:
        filtered_df = pd.DataFrame(columns=["LAT", "LON", "BaseDateTime"])

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    filtered_df.to_csv(output_csv, index=False)
    print(f"Filtering complete. Saved {len(filtered_df)} rows to {output_csv}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Filter large AIS CSV exports.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/ais/raw/AIS_2024_01_01.csv"),
        help="Path to a raw AIS CSV file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/ais/processed/filtered_ais_data.csv"),
        help="Path where the filtered CSV should be written.",
    )
    parser.add_argument(
        "--chunksize",
        type=int,
        default=100_000,
        help="Rows to read per pandas chunk.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    filter_ais_data(args.input, args.output, chunksize=args.chunksize)


if __name__ == "__main__":
    main()
