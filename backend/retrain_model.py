import joblib
from xgboost import XGBClassifier
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\shari\Downloads\heart.csv") 
print(df.head()) # Replace with your actual dataset path
X = df.drop(columns=["target"])  # Replace "target" with the correct column name
y = df["target"]

# Train the model again
model = XGBClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "backend/xgboost_heart_model.pkl")
print("Model retrained and saved successfully!")

