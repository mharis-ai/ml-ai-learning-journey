import pandas as pd
from pathlib import Path

def load_data(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_csv(path)
    print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df
