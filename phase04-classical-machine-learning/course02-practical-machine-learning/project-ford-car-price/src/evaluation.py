import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="whitegrid", palette="muted", font_scale=1.2)

def evaluate_models(models, X_train, y_train, X_test, y_test, save_plots_path=None, feature_names=None):
    """
    Evaluate models with train/test metrics, overfitting check, and generate clean plots.
    
    Args:
        models (dict): dictionary of trained models {name: model}
        X_train, y_train, X_test, y_test: data
        save_plots_path (str/Path): path to save plots
        feature_names (list): list of feature names for feature importance plots
    Returns:
        pd.DataFrame: metrics for each model with overfitting flag
    """
    results = []
    save_plots_path = Path(save_plots_path) if save_plots_path else None
    if save_plots_path:
        save_plots_path.mkdir(parents=True, exist_ok=True)

    for name, model in models.items():
        # Predictions
        preds_train = model.predict(X_train)
        preds_test = model.predict(X_test)

        # Metrics
        r2_train = r2_score(y_train, preds_train)
        r2_test = r2_score(y_test, preds_test)
        rmse_train = np.sqrt(mean_squared_error(y_train, preds_train))
        rmse_test = np.sqrt(mean_squared_error(y_test, preds_test))

        # Overfitting check
        overfit_flag = "Yes" if r2_train - r2_test > 0.1 else "No"
        color = "red" if overfit_flag == "Yes" else "green"

        results.append({
            "Model": name,
            "R2_train": r2_train,
            "R2_test": r2_test,
            "RMSE_train": rmse_train,
            "RMSE_test": rmse_test,
            "Overfit": overfit_flag
        })

        if save_plots_path:
            # ---- Predicted vs Actual ----
            plt.figure(figsize=(10,6))
            plt.scatter(y_test, preds_test, alpha=0.6, edgecolor='k', color=color)
            plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
            plt.xlabel("Actual")
            plt.ylabel("Predicted")
            plt.title(f"{name}: Predicted vs Actual ({'Overfit' if color=='red' else 'Good'})")
            plt.tight_layout()
            plt.savefig(save_plots_path / f"{name}_pred_vs_actual.png", dpi=150)
            plt.close()

            # ---- Residuals ----
            residuals = y_test - preds_test
            plt.figure(figsize=(8,4))
            sns.histplot(residuals, kde=True, color=color, edgecolor="black")
            plt.xlabel("Residuals")
            plt.title(f"{name}: Residuals ({'Overfit' if color=='red' else 'Good'})")
            plt.tight_layout()
            plt.savefig(save_plots_path / f"{name}_residuals.png", dpi=150)
            plt.close()

            # ---- Train vs Test ----
            plt.figure(figsize=(10,6))
            plt.scatter(y_train, preds_train, alpha=0.5, label='Train', edgecolor='k', color='blue')
            plt.scatter(y_test, preds_test, alpha=0.5, label='Test', edgecolor='k', color=color)
            plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
            plt.xlabel("Actual")
            plt.ylabel("Predicted")
            plt.title(f"{name}: Train vs Test ({'Overfit' if color=='red' else 'Good'})")
            plt.legend()
            plt.tight_layout()
            plt.savefig(save_plots_path / f"{name}_train_test_comparison.png", dpi=150)
            plt.close()

            # ---- Feature Importance for tree-based models ----
            if hasattr(model, "feature_importances_") and feature_names is not None:
                importance = model.feature_importances_
                plt.figure(figsize=(8,4))
                # Plot bars manually to avoid Seaborn palette warning
                colors = sns.color_palette("viridis", len(feature_names))
                for i, (val, feat) in enumerate(zip(importance, feature_names)):
                    plt.barh(feat, val, color=colors[i])
                plt.xlabel("Importance")
                plt.ylabel("Feature")
                plt.title(f"{name}: Feature Importance")
                plt.tight_layout()
                plt.savefig(save_plots_path / f"{name}_feature_importance.png", dpi=150)
                plt.close()

    return pd.DataFrame(results).sort_values(by="R2_test", ascending=False)
