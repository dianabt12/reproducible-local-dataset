import pandas as pd
from pathlib import Path

IN_PATH = Path("data/processed/cleaned_records.csv")
OUT_PATH = Path("reports/summary.md")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(IN_PATH)

with open(OUT_PATH, "w") as f:
    f.write("# Data Cleaning Summary\n\n")
    f.write(f"- Total records after cleaning: {len(df)}\n")
    f.write(f"- Unique categories: {df['category'].nunique()}\n")
    f.write(f"- Year coverage: {df['year'].min()}–{df['year'].max()}\n")

