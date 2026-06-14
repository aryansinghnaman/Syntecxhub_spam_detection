# 🛡️ SmartShield AI

### Real-Time Email, SMS & Scam Detection Platform

SmartShield AI is an intelligent spam and scam detection platform built using Natural Language Processing (NLP) and Machine Learning. The system analyzes emails, SMS messages, promotional content, and suspicious text to identify potential threats and provide real-time security insights.

The platform leverages TF-IDF Vectorization and Logistic Regression to classify messages as safe or potentially harmful, while also providing confidence scores, threat analysis, and keyword-based risk indicators through an interactive Streamlit dashboard.

---

## 🚀 Features

* 📩 Email & SMS Spam Detection
* 🚨 Real-Time Threat Analysis
* 📊 Confidence Score Evaluation
* 🔍 Suspicious Keyword Detection
* 🛡️ Scam & Fraud Risk Identification
* 🎯 97%+ Prediction Accuracy
* 🌐 Interactive Streamlit Dashboard
* ⚡ Fast Real-Time Predictions
* 📈 Machine Learning Powered Analysis

---

## 🧠 Machine Learning Pipeline

### Data Preprocessing

* Text Cleaning
* Tokenization
* Feature Extraction

### Feature Engineering

* TF-IDF Vectorization
* Stopword Removal
* Text Normalization

### Model

* Logistic Regression Classifier

### Performance Metrics

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 97.04% |
| Precision | 100%   |
| Recall    | 77.85% |
| F1 Score  | 87.55% |

---

## 🖥️ Dashboard Preview

### Home Dashboard

![Dashboard](screenshots/dashboard.png)

### Threat Detection

![Threat Analysis](screenshots/prediction.png)

### Safe Message Analysis

![Analytics](screenshots/analytical.png)

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression

### Data Processing

* Pandas
* NumPy

### Frontend

* Streamlit

### Model Serialization

* Joblib

---

## 📂 Project Structure

```text
SmartShield-AI/

│
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── dashboard.png
│   ├── prediction.png
│   └── analytical.png
│
└── assets/
    └── logo.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/SmartShield-AI.git
```

Move to project directory:

```bash
cd SmartShield-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📊 Example Threat Detection

### Input

```text
Congratulations!

You have won ₹50,000.

Click the link below to claim your reward immediately.
```

### Output

```text
🚨 HIGH RISK MESSAGE DETECTED

Risk Score: 94/100

Threat Level: HIGH

Detection Type: Spam / Fraudulent Content
```

---

## 🔮 Future Enhancements

* Phishing URL Detection
* Email Header Analysis
* Deep Learning Models (LSTM/BERT)
* Multi-Language Spam Detection
* Advanced Threat Intelligence Dashboard
* API Integration for Real-Time Monitoring

---

## 💡 Key Learning Outcomes

* Natural Language Processing
* Text Classification
* Feature Engineering
* Machine Learning Model Development
* Streamlit Application Development
* Model Deployment Fundamentals
* Security-Oriented AI Solutions

---

## 👨‍💻 Author

### Aryan Singh

Machine Learning Intern @ Syntecshub

Python Developer | Machine Learning Enthusiast | AI Solutions Builder

Passionate about developing intelligent systems that combine Machine Learning, Automation, and Security to solve real-world problems.

---

## ⭐ Project Status

✅ Completed

Actively maintained and open for future improvements.
