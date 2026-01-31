import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE

def preprocess_data(path):
    df = pd.read_csv(path)

    # Drop highly correlated columns
    df.drop(['months_as_customer', 'total_claim_amount'], axis=1, inplace=True)

    # Encode categorical columns
    encoder = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = encoder.fit_transform(df[col])

    X = df.drop('fraud_reported', axis=1)
    y = df['fraud_reported']

    # Handle imbalance
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_resampled)

    return X_scaled, y_resampled

