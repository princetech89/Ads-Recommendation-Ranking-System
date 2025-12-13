from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from src.feature_engineering import prepare_features
from src.data_preprocessing import load_data
import joblib

print("📌 Loading data...")
df = load_data()

print("📌 Preparing features...")
X, y, pipeline = prepare_features(df)

# Save preprocessing pipeline
joblib.dump(pipeline, "feature_pipeline.pkl")
print("✔ Feature pipeline saved as feature_pipeline.pkl")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ------------------------ TRAIN LOGISTIC REGRESSION ONLY ------------------------
print("📌 Training Logistic Regression model...")
lr_model = LogisticRegression(max_iter=500)
lr_model.fit(X_train, y_train)

# Save model
joblib.dump(lr_model, "lr_model.pkl")
print("✔ Logistic Regression model saved as lr_model.pkl")

print("🎉 Training completed successfully!")
