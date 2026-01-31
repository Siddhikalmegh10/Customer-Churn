import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


# Sample dataset
data = {
'Age': [25, 45, 35, 50, 23, 40],
'MonthlyCharges': [200, 500, 300, 700, 150, 450],
'Tenure': [1, 5, 3, 7, 1, 4],
'Churn': [1, 0, 0, 0, 1, 0]
}