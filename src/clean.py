import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_and_standardize(path: Path, year: int) -> pd.DataFrame:
    df = pd.read_csv(path)

    df.columns = df.columns.str.strip().str.lower()

    if "source_system" not in df.columns:
        df["source_system"] = "unknown"
    if "department" not in df.columns:
        df["department"] = "unknown"
    if "priority" not in df.columns:
        df["priority"] = "unknown"

    df["year"] = year
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["record_id"])
    df = df.dropna(subset=["record_id", "date", "value"])
    df = df[df["value"] >= 0]

    df["category"] = (
        df["category"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    return df


def main():
    df_2022 = load_and_standardize(RAW_DIR / "records_2022.csv", 2022)
    df_2023 = load_and_standardize(RAW_DIR / "records_2023.csv", 2023)

    df_all = pd.concat([df_2022, df_2023], ignore_index=True)
    df_clean = clean_data(df_all)

    csv_out = OUT_DIR / "cleaned_records.csv"
    parquet_out = OUT_DIR / "cleaned_records.parquet"

    df_clean.to_csv(csv_out, index=False)
    df_clean.to_parquet(parquet_out)


if __name__ == "__main__":
    main()

