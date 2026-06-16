import random

def cnn_predict(image):

    predictions = [

        ("Pneumonia", 94),

        ("Brain Tumor", 92),

        ("Skin Cancer", 90),

        ("Normal", 96)

    ]

    return random.choice(predictions)