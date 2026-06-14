import streamlit as st
import joblib

st.set_page_config(
    page_title="SmartShield AI",
    page_icon="🛡️",
    layout="wide"
)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#111827);
}

.hero{
    padding:35px;
    border-radius:25px;
    background:rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border:1px solid rgba(255,255,255,0.15);
    margin-bottom:25px;
}

.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    font-size:18px;
    font-weight:600;
    color:white;
    background:linear-gradient(90deg,#3b82f6,#06b6d4);
}

.stButton > button:hover{
    transform:scale(1.02);
}

.metric-card{
    background:rgba(255,255,255,0.06);
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1 style="color:white;">
🛡️ SmartShield AI
</h1>

<p style="color:#cbd5e1;font-size:18px;">
Real-Time Email, SMS & Scam Detection Platform
</p>

<p style="color:#94a3b8;">
Powered by Natural Language Processing and Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.success("✓ Spam Detection")

with c2:
    st.info("✓ Scam Detection")

with c3:
    st.warning("✓ Risk Analysis")

with c4:
    st.success("✓ Confidence Scoring")

st.info(
    "🎯 Model Accuracy: 97.04% | TF-IDF + Logistic Regression"
)

message = st.text_area(
    "📩 Paste an Email, SMS, Promotional Message or Suspicious Text",
    height=220,
    placeholder="Congratulations! You won ₹50,000. Click here to claim your reward."
)

spam_keywords = [
    "free",
    "winner",
    "won",
    "prize",
    "claim",
    "click",
    "offer",
    "urgent",
    "cash",
    "money",
    "reward"
]

if st.button("Analyze Message", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message.")
        st.stop()

    vec = vectorizer.transform([message])

    prediction = model.predict(vec)[0]

    probs = model.predict_proba(vec)[0]

    idx = list(model.classes_).index(prediction)

    confidence = probs[idx] * 100

    m1,m2,m3 = st.columns(3)

    with m1:
        st.metric(
            "Model Accuracy",
            "97.04%"
        )

    with m2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with m3:
        st.metric(
            "Words",
            len(message.split())
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction == "spam":

        st.error(
            "🚨 HIGH RISK MESSAGE DETECTED"
        )

        st.markdown(f"""
        <div style="
        background:rgba(239,68,68,0.15);
        padding:25px;
        border-radius:15px;
        border-left:6px solid #ef4444;
        ">

        <h2 style="color:white;">
        🚨 Threat Analysis
        </h2>

        <p style="color:white;font-size:18px;">
        <b>Risk Score:</b> {int(confidence)}/100
        </p>

        <p style="color:white;font-size:18px;">
        <b>Threat Level:</b> HIGH
        </p>

        <p style="color:white;font-size:18px;">
        <b>Detection Type:</b> Spam / Fraudulent Content
        </p>

        <p style="color:white;font-size:18px;">
        <b>Confidence:</b> {confidence:.2f}%
        </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.success(
            "🟢 SAFE MESSAGE"
        )

        st.markdown(f"""
        <div style="
        background:rgba(34,197,94,0.15);
        padding:25px;
        border-radius:15px;
        border-left:6px solid #22c55e;
        ">

        <h2 style="color:white;">
        🛡️ Safety Analysis
        </h2>

        <p style="color:white;font-size:18px;">
        <b>Risk Score:</b> {100-int(confidence)}/100
        </p>

        <p style="color:white;font-size:18px;">
        <b>Threat Level:</b> LOW
        </p>

        <p style="color:white;font-size:18px;">
        <b>Detection Type:</b> Normal Communication
        </p>

        <p style="color:white;font-size:18px;">
        <b>Confidence:</b> {confidence:.2f}%
        </p>

        </div>
        """, unsafe_allow_html=True)

    detected = [
        word
        for word in spam_keywords
        if word in message.lower()
    ]

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader(
        "🔎 Potential Risk Indicators"
    )

    if detected:

        for word in detected:
            st.warning(
                f"⚠️ Suspicious Keyword Detected: {word}"
            )

    else:

        st.success(
            "✅ No suspicious keywords detected"
        )

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;'>

SmartShield AI • NLP Security Project

Built with Python, Streamlit & Scikit-Learn

</div>
""",
unsafe_allow_html=True
)

