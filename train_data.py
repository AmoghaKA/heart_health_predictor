import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib  

df = pd.read_csv("custom_heart.csv")
print("Dataset loaded with", len(df), "rows")


df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop(columns=["heart_health_percentage"])
y = df_encoded["heart_health_percentage"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestRegressor()
model.fit(X_train, y_train)

print("Model trained successfully!")
print("Test score (R^2):", model.score(X_test, y_test))


joblib.dump(model, "heart_health_model.pkl")
joblib.dump(list(X.columns), "X_columns.pkl") 
print("Model saved as heart_health_model.pkl")


sample = pd.DataFrame([{
    "age": 40,
    "gender": "male",
    "height": 170,
    "weight": 70,
    "systolic": 125,
    "diastolic": 82,
    "cholesterol": "normal",
    "smoking": "no",
    "exercise": "weekly",
    "family_history": "no"
}])


sample_encoded = pd.get_dummies(sample)
sample_encoded = sample_encoded.reindex(columns=X.columns, fill_value=0)

prediction = model.predict(sample_encoded)[0]
print("Predicted Heart Health %:", round(prediction, 2))
