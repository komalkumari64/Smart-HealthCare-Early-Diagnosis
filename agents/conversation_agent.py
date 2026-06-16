from backend.logger import log_chat

def chat_response(query):

    log_chat(query)

    return f"""
👨‍⚕️ AI Assistant

You said:
{query}

👉 Please consult a doctor for proper diagnosis.
"""