import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example dummy data (replace with real dataset)
data = {
    "fever": [1,0,1,0],
    "cough": [1,1,0,0],
    "disease": ["Flu","Cold","Malaria","Healthy"]
}

df = pd.DataFrame(data)

X = df[["fever","cough"]]
y = df["disease"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/rf_model.pkl")

print("Model saved!")