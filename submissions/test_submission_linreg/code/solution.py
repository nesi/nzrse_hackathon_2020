import pandas as pd
from sklearn.linear_model import LinearRegression

x = pd.read_csv('emod3d_train_x.csv')
y = pd.read_csv('emod3d_train_y.csv')

reg = LinearRegression().fit(x, y)
x_test = pd.read_csv('emod3d_test_x.csv')
y_test = reg.predict(x_test)

# compute the score
import numpy as np
def quantile_loss(y_actual, y_predict):
    """
    Cost function to minimise
    - y_actual: the actual number of core hours consumed by the simulation (array-like)
    - y_predict: the model's prediction (array-like of same length as above)
    - returns positive number, the lower the better
    """
    quantile = 0.9
    errors = np.maximum((y_actual - y_predict) * quantile, (y_predict - y_actual) * (1.0 - quantile))
    return np.mean(errors)

y_actual = pd.read_csv('emod3d_test_y.csv')
loss = quantile_loss(y_actual, y_test)
print(f'loss: {loss["core_hours"]:.7g}')

np.savetxt('emod3d_test_y_mine.csv', y_test, header='core_hours')