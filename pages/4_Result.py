import streamlit as st

st.header("📊 Diagnosis Result Summary")

st.write("""
### Final Diagnosis
- Disease: **Pneumonia**
- Confidence: **92%**
- Model Used: CNN + ML Ensemble
""")

st.warning("⚠ AI-assisted diagnosis. Consult a medical professional.")
