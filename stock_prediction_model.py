import pandas as pd
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

# Load processed data
df = pd.read_csv('apple_stock_processed.csv')

# Define features and target variable
X = df[['SMA_50', 'SMA_200', 'Price_Change', 'Volatility']]
y = df['Close']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future prices
y_pred = model.predict(X_test)

# Save the model
import pickle
with open('stock_prediction_model.pkl', 'wb') as f:
    pickle.dump(model, f)
