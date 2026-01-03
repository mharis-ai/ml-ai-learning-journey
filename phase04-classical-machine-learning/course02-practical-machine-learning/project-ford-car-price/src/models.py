from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import joblib

def train_models(X_train, y_train, save_models_path=None):
    models = {
        "LinearRegression": {"model": LinearRegression(), "params": {}},
        "Ridge": {"model": Ridge(), "params": {"alpha":[0.01,0.1,1,10]}},
        "Lasso": {"model": Lasso(), "params": {"alpha":[0.01,0.1,1,10]}},
        "ElasticNet": {"model": ElasticNet(), "params": {"alpha":[0.01,0.1,1,10], "l1_ratio":[0.1,0.5,0.9]}},
        "RandomForest": {"model": RandomForestRegressor(random_state=42), "params":{"n_estimators":[50,100,200], "max_depth":[None,5,10]}},
        "GradientBoosting": {"model": GradientBoostingRegressor(random_state=42), "params":{"n_estimators":[50,100,200], "learning_rate":[0.01,0.1,0.2]}},
        "DecisionTree": {"model": DecisionTreeRegressor(random_state=42), "params":{"max_depth":[None,5,10,20]}},
        "KNeighbors": {"model": KNeighborsRegressor(), "params":{"n_neighbors":[3,5,7,9]}},
        "SVR": {"model": SVR(), "params":{"kernel":["linear","rbf"], "C":[0.1,1,10]}}
    }

    trained_models = {}

    for name, mp in models.items():
        print(f"Training and tuning {name}...")
        model, params = mp["model"], mp["params"]

        if params:
            grid = GridSearchCV(model, params, cv=5, scoring="r2", n_jobs=-1)
            grid.fit(X_train, y_train)
            best_model = grid.best_estimator_
            print(f"{name} best params: {grid.best_params_}")
        else:
            model.fit(X_train, y_train)
            best_model = model

        trained_models[name] = best_model

        if save_models_path:
            save_models_path.mkdir(exist_ok=True)
            joblib.dump(best_model, save_models_path / f"{name}.joblib")

    return trained_models
