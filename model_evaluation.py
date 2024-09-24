import pandas as pd
from sklearn.metrics import mean_squared_error

from stock_prediction_model import X_test
from stock_prediction_model import y_pred

mse = mean_squared_error(X_test, y_pred) 
print(f'Model Mean Squared Error: {mse}')
