
def get_features(X, y, runs, selector):

    important_features = [[] for i in range(runs)]

    for i in range(runs):
        model = selector.fit(X, y)
        importances = model.feature_importances_

        for j in range(len(importances)):
            important_features[i].append(list(importances).index(importances[j])) if importances[j] > 1 else 0

    print(important_features)

    for i in range(len(important_features) - 1):
        if i != 0:
            importances = set.intersection(*map(set, important_features))

    importances = list(importances)
    X = X[..., importances]
    return X