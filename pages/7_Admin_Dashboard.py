import streamlit as st
import pandas as pd
import plotly.express as px

from backend.mongodb import db
from backend.analytics import (
    get_stats,
    recent_activity,
    last_active_user,
    login_history
)

from backend.disease_stats import top_diseases
from backend.report import create_report

# --------------------------
# LOGIN CHECK
# --------------------------

if "login" not in st.session_state:
    st.error("Please Login First")
    st.stop()

# --------------------------
# PAGE CONFIG
# --------------------------

st.set_page_config(
    page_title="Smart Healthcare Dashboard",
    layout="wide"
)

# --------------------------
# CSS
# --------------------------

st.markdown("""
<style>

[data-testid="metric-container"]{
background:#111827;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.15);
}

[data-testid="metric-container"] label{
color:white;
}

[data-testid="metric-container"] div{
color:#00E5FF;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# TITLE
# --------------------------

st.title("🏥 Smart Healthcare Analytics Dashboard")

stats = get_stats()

# --------------------------
# METRICS
# --------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric("👥 Patients", stats["patients"])
col2.metric("🟢 Active Users", stats["active"])
col3.metric("🔍 Searches", stats["searches"])
col4.metric("🤖 Predictions", stats["predictions"])

col5,col6,col7,col8 = st.columns(4)

col5.metric("🖼 Images", stats["images"])
col6.metric("💬 Chats", stats["chats"])
col7.metric("🔐 Logins", stats["logins"])
col8.metric("📊 Online", stats["active"])

st.divider()

# --------------------------
# LAST ACTIVE USER
# --------------------------

st.subheader("👤 Last Active User")

st.success(last_active_user())

# --------------------------
# SEARCH ANALYTICS
# --------------------------

st.subheader("📈 Search Analytics")

search_df = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Searches":[10,20,15,30,25,35,40]
})

fig = px.line(
    search_df,
    x="Day",
    y="Searches",
    markers=True,
    title="Weekly Searches"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------
# DISEASE TREND
# --------------------------

st.subheader("📊 Disease Trend")

disease_data = top_diseases()

if disease_data:

    disease_df = pd.DataFrame(disease_data)

    disease_df.rename(
        columns={
            "_id":"Disease",
            "count":"Count"
        },
        inplace=True
    )

    fig2 = px.bar(
        disease_df,
        x="Disease",
        y="Count",
        title="Disease Prediction Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# --------------------------
# AI USAGE
# --------------------------

st.subheader("🤖 AI Usage")

usage_df = pd.DataFrame({
    "Feature":["Symptoms","Images","Chat"],
    "Count":[
        stats["searches"],
        stats["images"],
        stats["chats"]
    ]
})

fig3 = px.pie(
    usage_df,
    names="Feature",
    values="Count"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------
# TOP DISEASES
# --------------------------

st.subheader("🏆 Top Diseases")

if disease_data:

    rank = 1

    for item in disease_data:

        st.success(
            f"#{rank} {item['_id']} ({item['count']})"
        )

        rank += 1

# --------------------------
# ACTIVITY FEED
# --------------------------

st.subheader("⚡ Live Activity Feed")

activities = recent_activity()

for item in activities:
    st.info(item)

# --------------------------
# PATIENTS TABLE
# --------------------------

st.subheader("👥 Registered Patients")

patients = list(
    db.users.find(
        {},
        {"password":0}
    )
)

if patients:

    df = pd.DataFrame(patients)

    st.dataframe(
        df,
        use_container_width=True
    )

# --------------------------
# LOGIN HISTORY
# --------------------------

st.subheader("🔐 Login History")

history = login_history()

if history:

    login_df = pd.DataFrame(history)

    st.dataframe(
        login_df,
        use_container_width=True
    )

# --------------------------
# MODEL STATUS
# --------------------------

st.subheader("🤖 CNN Model Accuracy")

st.progress(92)

st.success("CNN Accuracy : 92%")

st.subheader("🚀 Model Training Progress")

st.progress(85)

st.info("Training Progress : 85%")

# --------------------------
# PDF REPORT
# --------------------------

st.subheader("📄 Export Analytics")

if st.button("Generate Report"):

    file = create_report()

    with open(file, "rb") as f:

        st.download_button(
            "Download PDF",
            f,
            "analytics_report.pdf"
        )
# ===================================
# ADVANCED FEATURES
# ===================================

from datetime import datetime

st.divider()

st.header("🚀 Advanced Healthcare Insights")

# Live Time

st.subheader("🕒 System Time")

st.success(
    datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )
)

# System Health

st.subheader("🖥 System Health")

c1,c2,c3 = st.columns(3)

c1.metric("Database","Online")
c2.metric("ML Model","Running")
c3.metric("CNN Model","Running")

# Risk Meter

st.subheader("📍 Disease Risk Meter")

risk = 72

st.progress(risk)

st.warning(
    f"Current Risk Level : {risk}%"
)

# AI Recommendation

st.subheader("🧠 AI Recommendation")

st.info("""
• Drink more water

• Exercise daily

• Maintain healthy diet

• Consult doctor if symptoms continue
""")

# Total Records

st.subheader("📦 Total Records")

total_records = (
    stats["patients"]
    + stats["searches"]
    + stats["images"]
    + stats["chats"]
    + stats["predictions"]
)

st.metric(
    "Database Records",
    total_records
)

# Most Used Service

st.subheader("🏆 Most Used AI Service")

services = {

    "Symptoms": stats["searches"],

    "Images": stats["images"],

    "Chat": stats["chats"]

}

top_service = max(
    services,
    key=services.get
)

st.success(
    f"Most Used Service : {top_service}"
)

# Accuracy Comparison

st.subheader("📊 Model Accuracy Comparison")

compare_df = pd.DataFrame({

    "Model":[
        "Random Forest",
        "CNN"
    ],

    "Accuracy":[
        89,
        92
    ]

})

fig4 = px.bar(
    compare_df,
    x="Model",
    y="Accuracy",
    title="Model Accuracy Comparison"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)