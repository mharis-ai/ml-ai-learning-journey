from pathlib import Path
import pandas as pd

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_selection import select_features
from src.models import train_models
from src.evaluation import evaluate_models
from src.report import PDFReport

def main():
    # --------------------- Paths ---------------------
    ROOT = Path(__file__).resolve().parent
    RAW_DATA_PATH = ROOT / "data" / "raw" / "ford-cars.csv"
    PROCESSED_DATA_PATH = ROOT / "data" / "processed" / "ford-cars-clean.csv"
    RESULTS_PATH = ROOT / "results"
    MODELS_PATH = ROOT / "models"
    PLOTS_PATH = RESULTS_PATH / "plots"
    REPORT_PATH = RESULTS_PATH / "ford-project-report.pdf"

    # --------------------- Load Data ---------------------
    df = load_data(RAW_DATA_PATH)

    # --------------------- Preprocessing ---------------------
    TARGET_COLUMN = "price"
    X_train, X_test, y_train, y_test = preprocess_data(df, TARGET_COLUMN)

    # Feature columns before selection
    feature_columns = [col for col in df.columns if col != TARGET_COLUMN]

    # --------------------- Feature Selection ---------------------
    X_train_sel, X_test_sel, selected_features = select_features(X_train, y_train, X_test, k='all')
    selected_feature_names = [feature_columns[i] for i in selected_features]

    # Save cleaned data
    df_clean = pd.DataFrame(X_train_sel, columns=selected_feature_names)
    df_clean[TARGET_COLUMN] = y_train.reset_index(drop=True)
    PROCESSED_DATA_PATH.parent.mkdir(exist_ok=True)
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)

    # --------------------- Train Models ---------------------
    models = train_models(X_train_sel, y_train, save_models_path=MODELS_PATH)

    # --------------------- Evaluate Models ---------------------
    results = evaluate_models(
        models,
        X_train_sel, y_train,
        X_test_sel, y_test,
        save_plots_path=PLOTS_PATH,
        feature_names=selected_feature_names
    )
    results.to_csv(RESULTS_PATH / "evaluation-results.csv", index=False)

    # --------------------- Generate PDF Report ---------------------
    pdf = PDFReport("Ford Car Price Project Report with Overfitting Badge")
    pdf.add_title()

    for _, row in results.iterrows():
        model_name = row["Model"]
        overfit = row["Overfit"]
        badge_text = "Overfit" if overfit == "Yes" else "Good"
        badge_color = "red" if overfit == "Yes" else "green"

        # Add section header with badge
        pdf.add_section(f"{model_name} ({badge_text})")

        # Add metrics
        metrics_text = (
            f"R2_train: {row['R2_train']:.3f}, R2_test: {row['R2_test']:.3f}\n"
            f"RMSE_train: {row['RMSE_train']:.3f}, RMSE_test: {row['RMSE_test']:.3f}\n"
            f"Overfitting: {overfit}"
        )
        pdf.add_text(metrics_text)

        # Add plots for this model
        for plot_file in sorted(PLOTS_PATH.glob(f"{model_name}_*.png")):
            pdf.add_image(plot_file, w=160)

    pdf.save(REPORT_PATH)

    # --------------------- Completion Messages ---------------------
    print("Pipeline complete!")
    print(f"Cleaned data saved: {PROCESSED_DATA_PATH}")
    print(f"Models saved: {MODELS_PATH}")
    print(f"Evaluation results: {RESULTS_PATH / 'evaluation-results.csv'}")
    print(f"Plots saved: {PLOTS_PATH}")
    print(f"PDF report generated: {REPORT_PATH}")


if __name__ == "__main__":
    main()
