from sklearn.feature_selection import SelectKBest, f_regression

def select_features(X_train, y_train, X_test, k='all'):
    """
    Perform univariate feature selection using f_regression
    k: number of top features to select, 'all' selects all
    """
    selector = SelectKBest(score_func=f_regression, k=k)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    selected_features = selector.get_support(indices=True)
    return X_train_selected, X_test_selected, selected_features
