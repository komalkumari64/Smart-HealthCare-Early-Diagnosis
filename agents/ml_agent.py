import joblib

model = joblib.load("models/rf_model.pkl")

symptom_map = {
    "fever": 0,
    "cough": 1
}

def predict_from_symptoms(symptoms):
    input_data = [0, 0]

    for s in symptoms:
        s = s.strip().lower()
        if s in symptom_map:
            input_data[symptom_map[s]] = 1

    prediction = model.predict([input_data])[0]
    proba = model.predict_proba([input_data])[0]

    confidence = max(proba) * 100

    return prediction, confidence