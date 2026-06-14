import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# =====================================
# LOAD DATASET
# =====================================

print("Loading dataset...")

df = pd.read_csv(
    "spam.csv",
    encoding="latin-1"
)

# Keep useful columns only

df = df[['v1', 'v2']]

df.columns = [
    'label',
    'message'
]

# =====================================
# BASIC INFO
# =====================================

print("\nDataset Shape:")
print(df.shape)

print("\nClass Distribution:")
print(df['label'].value_counts())

# =====================================
# FEATURES & TARGET
# =====================================

X = df['message']

y = df['label']

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =====================================
# TF-IDF VECTORIZATION
# =====================================

vectorizer = TfidfVectorizer(
    stop_words='english',
    lowercase=True,
    max_features=5000
)

X_train_vectorized = vectorizer.fit_transform(
    X_train
)

X_test_vectorized = vectorizer.transform(
    X_test
)

# =====================================
# MODEL TRAINING
# =====================================

print("\nTraining model...")

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train_vectorized,
    y_train
)

# =====================================
# PREDICTIONS
# =====================================

predictions = model.predict(
    X_test_vectorized
)

# =====================================
# EVALUATION
# =====================================

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    pos_label='spam'
)

recall = recall_score(
    y_test,
    predictions,
    pos_label='spam'
)

f1 = f1_score(
    y_test,
    predictions,
    pos_label='spam'
)

print("\n==========================")
print("MODEL PERFORMANCE")
print("==========================")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(
    model,
    "model.pkl"
)

joblib.dump(
    vectorizer,
    "vectorizer.pkl"
)

print("\nModel saved successfully!")

# =====================================
# SAMPLE TEST
# =====================================

sample_message = [
    "Congratulations! You have won a free iPhone. Click here now."
]

sample_vector = vectorizer.transform(
    sample_message
)

sample_prediction = model.predict(
    sample_vector
)

print("\nSample Prediction:")
print(sample_prediction[0])

print("\nProject Completed Successfully.")