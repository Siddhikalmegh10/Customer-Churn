import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# Dummy training data
X = np.array([
    [25, 2000, 1],
    [45, 5000, 5],
    [30, 3000, 2],
    [50, 7000, 8],
    [23, 1500, 1],
    [60, 9000, 10]
])

y = np.array([1, 0, 1, 0, 1, 0])  # 1 = Leave, 0 = Stay

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "churn_model.pkl")

print("✅ Model trained & saved successfully")
