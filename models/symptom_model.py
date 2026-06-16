from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Dummy trained model (demo purpose)
def load_symptom_model():
    model = RandomForestClassifier()
    
    # Dummy training data
    X = np.array([
        [1, 0, 1],  # fever, cough, headache
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 0]
    ])
    
    y = ["Flu", "Covid", "Cold", "Flu"]
    
    model.fit(X, y)
    return model
