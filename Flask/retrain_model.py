import pandas as pd
import xgboost as xgb
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("../Dataset/garments_worker_productivity.csv")

print(f"Original dataset: {df.shape}")


# ==========================================
# 2. CLEAN DATA
# ==========================================

# Remove accidental whitespace from categorical values
df["department"] = df["department"].astype(str).str.strip()

# Create month from the original date column
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

# The original notebook uses these three categorical features
categorical_columns = [
    "quarter",
    "department",
    "day"
]


# ==========================================
# 3. ENCODE CATEGORICAL FEATURES
# ==========================================

encoders = {}

for column in categorical_columns:
    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(
        df[column].astype(str)
    )

    encoders[column] = encoder

    print(f"\n{column}:")
    for label, value in zip(
        encoder.classes_,
        encoder.transform(encoder.classes_)
    ):
        print(f"  {label} -> {value}")


# ==========================================
# 4. SELECT FEATURES
# ==========================================

features = [
    "quarter",
    "department",
    "day",
    "team",
    "targeted_productivity",
    "smv",
    "over_time",
    "incentive",
    "idle_time",
    "idle_men",
    "no_of_style_change",
    "no_of_workers",
    "month"
]

X = df[features]
y = df["actual_productivity"]


print("\nFeatures:")
print(features)

print("\nX shape:", X.shape)
print("y shape:", y.shape)


# ==========================================
# 5. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=0
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 6. TRAIN XGBOOST
# ==========================================

model = xgb.XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    objective="reg:squarederror"
)

model.fit(X_train, y_train)


# ==========================================
# 7. EVALUATE
# ==========================================

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)

print("\n==========================================")
print("MODEL PERFORMANCE")
print("==========================================")

print(f"MAE  : {mae:.4f}")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")


# ==========================================
# 8. SAVE MODEL
# ==========================================

model.save_model("productivity_model.json")

# Save encoders separately
with open("productivity_encoders.pkl", "wb") as file:
    pickle.dump(encoders, file)


print("\n==========================================")
print("FILES SAVED")
print("==========================================")

print("productivity_model.json")
print("productivity_encoders.pkl")