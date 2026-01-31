import joblib
from sklearn.metrics import classification_report, confusion_matrix
from src.data_preprocessing import preprocess_data
from sklearn.model_selection import train_test_split

model = joblib.load("model/fraud_model.pkl")
X, y = preprocess_data("data/insurance_claims.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

