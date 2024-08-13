from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score
from sklearn.metrics import r2_score
import pandas as pd
import os

file_path = os.listdir("../data/processed/market data/")
data = pd.read_csv(f"../data/processed/market data/{file_path[0]}")
data.head()

data = data.drop(columns=['Unnamed: 0'])

# Prepare features and target variable
data.dropna(inplace=True)
X = data[['Open', 'High', 'Low', 'Volume', 'MA_30', 'MA_100', 'Volatility 30', 'Volatility 100', 'Rolling Std']]
y = data['Close'].shift(-1).dropna()
X = X.iloc[:-1]  # Align X with y
# Train Linear Regression and Random Forest models
model = LinearRegression()
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

# Evaluate models
mse = mean_squared_error(y_test, y_pred)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2 = r2_score(y_test, y_pred)
r2_rf = r2_score(y_test, y_pred_rf)
mae = mean_absolute_error(y_test, y_pred)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
evs = explained_variance_score(y_test, y_pred)
evs_rf = explained_variance_score(y_test, y_pred_rf)

print("Linear Regression Results:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
print(f"Mean Absolute Error: {mae}")
print(f"Explained Variance Score: {evs}\n")

print("Random Forest Results:")
print(f"Mean Squared Error: {mse_rf}")
print(f"R-squared: {r2_rf}")
print(f"Mean Absolute Error: {mae_rf}")
print(f"Explained Variance Score: {evs_rf}")

cv_scores = -cross_val_score(model, X, y, cv=10, scoring='neg_mean_squared_error')
cv_scores_rf = -cross_val_score(rf_model, X, y, cv=10, scoring='neg_mean_squared_error')

print("Cross-Validated MSE Scores Linear Regression:", cv_scores)
print("Cross-Validated MSE Scores Random Forest:", cv_scores_rf)
