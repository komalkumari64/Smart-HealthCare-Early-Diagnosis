import random

def cnn_predict(image):
    diseases = ["Pneumonia", "Normal", "Covid"]
    prediction = random.choice(diseases)
    confidence = random.randint(85, 95)
    return prediction, confidence
