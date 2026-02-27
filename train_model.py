import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Generate synthetic dataset using NumPy
np.random.seed(42)

transaction_amount = np.random.randint(100, 50000, 1000)
transaction_time = np.random.randint(0, 24, 1000)
customer_age = np.random.randint(18, 70, 1000)
location_score = np.random.randint(1, 10, 1000)
previous_fraud_count = np.random.randint(0, 5, 1000)

# Fraud logic (simple artificial rule)
fraud = (
    (transaction_amount > 30000) &
    (location_score > 7)
).astype(int)

# Combine features
X = np.column_stack((
    transaction_amount,
    transaction_time,
    customer_age,
    location_score,
    previous_fraud_count
))

y = fraud

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "fraud_model.pkl")

print("Model trained and saved successfully!")
