import optuna
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

def objective(trial, X_train, y_train):
    # Suggest hyperparameters for RandomForestRegressor
    min_samples_leaf = trial.suggest_int("min_samples_leaf", 1, 10)
    min_samples_split = trial.suggest_int("min_samples_split", 2, 20)
    min_weight_fraction_leaf = trial.suggest_float("min_weight_fraction_leaf", 0.0, 0.5)
    min_impurity_decrease = trial.suggest_float("min_impurity_decrease", 0.0, 0.1)
    n_estimators = trial.suggest_int("n_estimators", 50, 500, step=10)
    max_depth = trial.suggest_int("max_depth", 1, 50)
  

    # Create the RandomForestRegressor model with suggested hyperparameters
    rf = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        min_weight_fraction_leaf=min_weight_fraction_leaf,
        min_impurity_decrease=min_impurity_decrease,
        random_state=42,
        n_jobs=-1
    )

    # Evaluate the model using cross-validation and return the negative MAE score
    mae_scores = cross_val_score(rf, X_train, y_train, cv=3, scoring="neg_mean_absolute_error", n_jobs=-1)
    return mae_scores.mean()

def optimize_rf_hyperparameters(X_train, y_train, n_trials=100):
    # Create an Optuna study to maximize the objective
    study = optuna.create_study(direction="maximize")

    # Optimize the objective function
    study.optimize(lambda trial: objective(trial, X_train, y_train), n_trials=n_trials)

    # Print the best hyperparameters and the best score
    print("Best hyperparameters: ", study.best_params)
    print("Best MAE score: ", -study.best_value)  # Negate to get positive MAE

