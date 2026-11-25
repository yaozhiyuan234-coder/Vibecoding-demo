from pathlib import Path

import pandas as pd
import yfinance as yf

TICKER = "AAPL"
OUTPUT = Path("data") / "aapl.csv"


def main() -> None:
    df = yf.download(TICKER, period="2y", auto_adjust=False, progress=False)
    if df.empty:
        raise RuntimeError(f"No data returned for {TICKER}")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.index.name = "Date"
    df = df.reset_index()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT}")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumns:")
    print(list(df.columns))


if __name__ == "__main__":
    main()
