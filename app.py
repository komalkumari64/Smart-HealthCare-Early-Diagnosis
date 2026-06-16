import streamlit as st
from backend.router import route
from PIL import Image
import matplotlib.pyplot as plt
import speech_recognition as sr
import time

st.set_page_config(page_title="Smart Healthcare AI", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp { background:#f5f7fb; }

/* Title */
.title {
    font-size:36px;
    font-weight:600;
    text-align:center;
    color:#111827;
}
.subtitle {
    text-align:center;
    color:#6b7280;
    margin-bottom:20px;
}

/* Card */
.card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.05);
}

/* Chat container */
.chat-container {
    max-height:400px;
    overflow-y:auto;
    padding-right:10px;
}

/* User bubble */
.user-msg {
    background:#0f172a;
    color:white;
    padding:10px 14px;
    border-radius:15px;
    max-width:45%;
    margin-left:auto;
    margin-bottom:8px;
    font-size:14px;
}

/* Bot bubble */
.bot-msg {
    background:#f1f5f9;
    color:#111;
    padding:10px 14px;
    border-radius:15px;
    max-width:45%;
    margin-bottom:8px;
    font-size:14px;
}

/* Input */
.stTextInput input {
    border-radius:30px !important;
    padding:12px;
    border:1px solid #ddd;
}

/* Buttons */
.stButton>button {
    background:#111827;
    color:white;
    border-radius:10px;
    padding:8px 14px;
}

/* Warning */
.warning-box {
    background:#fef3c7;
    padding:12px;
    border-radius:10px;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">Smart Healthcare AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered diagnosis using ML & DL</div>', unsafe_allow_html=True)

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(["💬 Chat", "🧠 Symptoms", "🖼 Image"])

# ---------- CHAT ----------
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for sender, msg in st.session_state.messages:
        if sender == "user":
            st.markdown(f'<div class="user-msg">👤 {msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">🤖 {msg}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns([8,1,1])

    with col1:
        user_input = st.text_input("", placeholder="Type your message...", label_visibility="collapsed")

    with col2:
        send = st.button("➤")

    with col3:
        mic = st.button("🎙️")

    # SEND
    if send:
        if user_input:
            st.session_state.messages.append(("user", user_input))

            with st.spinner("Thinking..."):
                time.sleep(1)
                response = route("chat", user_input)

            st.session_state.messages.append(("bot", response))
            st.rerun()

    # MIC
    if mic:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                st.info("Listening...")
                audio = r.listen(source)
                text = r.recognize_google(audio)

                st.session_state.messages.append(("user", text))
                response = route("chat", text)
                st.session_state.messages.append(("bot", response))
                st.rerun()
        except:
            st.error("Mic error")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SYMPTOMS ----------
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    symptoms = st.text_input("Enter symptoms (e.g., fever, cough)")

    if st.button("Predict"):
        symptoms_list = symptoms.split(",")

        with st.spinner("Analyzing..."):
            result, confidence = route("symptom", symptoms_list)

        st.success(f"🩺 Prediction: {result}")
        st.progress(int(confidence))
        st.write(f"Confidence: {confidence:.2f}%")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- IMAGE ----------
with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    file = st.file_uploader("Upload Image")

    if file:
        img = Image.open(file)
        st.image(img)

        if st.button("Analyze"):
            result = route("image", img)
            st.success(result)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown('<div class="warning-box">⚠️ This is not a medical diagnosis. Consult a doctor.</div>', unsafe_allow_html=True)