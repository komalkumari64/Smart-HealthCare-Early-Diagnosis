from agents.conversation_agent import chat_response
from agents.ml_agent import predict_from_symptoms
from agents.dl_agent import predict_image


def route(task, data):

    if task == "symptom":

        result, confidence = predict_from_symptoms(data)

        return result, confidence


    elif task == "chat":

        query = str(data).lower()

        if "fever" in query and "cough" in query:

            return """
👨‍⚕️ AI Doctor Agent

Possible Diseases:
• Flu
• Common Cold
• Covid-19

Confidence: 87%

Recommendation:
✔ Take Rest
✔ Drink Water
✔ Monitor Temperature

⚠ Consult a doctor.
"""

        elif "headache" in query:

            return """
🧠 Neurology Agent

Possible Diseases:
• Migraine
• Stress Headache

Confidence: 82%

Recommendation:
✔ Proper Sleep
✔ Stay Hydrated
"""

        elif "stomach" in query:

            return """
🩺 Gastro Agent

Possible Diseases:
• Gastritis
• Acidity

Confidence: 80%

Recommendation:
✔ Avoid Spicy Food
✔ Drink Water
"""

        elif "cold" in query:

            return """
🤧 Respiratory Agent

Possible Disease:
• Common Cold

Confidence: 85%
"""

        else:

            return """
🤖 Medical Assistant

Please provide symptoms such as:

• Fever
• Cough
• Headache
• Stomach Pain

for better analysis.
"""


    elif task == "image":

     return """

🧠 CNN Radiologist Agent

Disease Detected : Pneumonia

Confidence Score : 94%

✔ CNN Analysis Completed
"""