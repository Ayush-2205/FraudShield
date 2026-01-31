import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/insurance_claims.csv")

# Select only the 4 features you use in UI
X = df[[
    "policy_annual_premium",
    "total_claim_amount",
    "age",
    "vehicle_claim"
]]

y = df["fraud_reported"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "fraud_model.pkl")
print("Model saved successfully")
