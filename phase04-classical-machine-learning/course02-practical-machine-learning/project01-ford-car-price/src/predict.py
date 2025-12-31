import joblib
from pathlib import Path

def predict_new(model_path, df_new, scaler=None):
    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")

    model = joblib.load(model_path)

    if scaler:
        df_scaled = scaler.transform(df_new)
    else:
        df_scaled = df_new

    preds = model.predict(df_scaled)
    return preds
