import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Load Kaggle dataset
df = pd.read_csv("data/phishing_data.csv")

# Print original label counts
print("Original labels:")
print(df["class"].value_counts())  # Expect: 1 = legit, -1 = phishing

# Replace: 1 → 0 (Legit), -1 → 1 (Phishing)
df["label"] = df["class"].replace({1: 0, -1: 1})
y = df["label"].values
X = df.drop(["Index", "class", "label"], axis=1)

# Check label distribution
print("\n✅ After Mapping:")
print(pd.Series(y).value_counts())

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"🎯 Accuracy: {acc:.4f}")

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/phishing_model.pkl")
print("✅ Model saved to model/phishing_model.pkl")
