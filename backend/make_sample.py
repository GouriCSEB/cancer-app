from pathlib import Path

import pandas as pd


BACKEND_DIR = Path(__file__).resolve().parent
DATA_PATH = BACKEND_DIR / "data" / "data.csv"
OUTPUT_PATH = BACKEND_DIR.parent / "frontend" / "public" / "sample.csv"


def main() -> None:
    if not DATA_PATH.is_file():
        raise SystemExit(
            f"Dataset file not found: {DATA_PATH}\n"
            "Add backend/data/data.csv before generating the sample."
        )

    features = pd.read_csv(DATA_PATH)
    if features.empty or features.shape[1] == 0:
        raise SystemExit(f"No feature rows or columns found in {DATA_PATH}.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    features.head(1).to_csv(OUTPUT_PATH, index=False)
    print(f"Sample feature row saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
