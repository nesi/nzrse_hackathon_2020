#!/usr/bin/env python3

"""
Create a conda virtual environment and install dependencies listed in the
requirement.txt file before running this script.
"""

import numpy as np
import pandas as pd

from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer


def quantile_loss(y_actual, y_predict):
    """
    Cost function to minimise
    - y_actual: the actual number of core hours consumed by the simulation (array-like)
    - y_predict: the model's prediction (array-like of same length as above)
    - returns positive number, the lower the better
    """
    quantile = 0.9
    errors = np.maximum(
        (y_actual - y_predict) * quantile, (y_predict - y_actual) * (1.0 - quantile)
    )
    return np.mean(errors)


X_train = pd.read_csv("data/emod3d_train_x.csv")
y_train = pd.read_csv("data/emod3d_train_y.csv")
X_test = pd.read_csv("data/emod3d_test_x.csv")

model = make_pipeline(
    StandardScaler(),
    GridSearchCV(
        ElasticNet(),
        {"alpha": [1e-3, 1e-2, 1e-1, 1, 10, 100]},
        scoring=make_scorer(quantile_loss, greater_is_better=False),
    ),
)
model.fit(X_train.values, y_train.values)

print("Best found model is:", model.steps[1][1].best_estimator_)

y_test = model.predict(X_test)

pd.DataFrame({"core_hours": y_test}).to_csv("emod3d_test_y.csv", index=False)
