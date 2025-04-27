# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, RocCurveDisplay
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

# Load the dataset
df = pd.read_csv("data/Marketing_AB_Testing.csv")
df.columns = df.columns.str.strip()

# Preprocessing
df['test group'] = df['test group'].map({'psa': 0, 'ad': 1})
df['converted'] = df['converted'].astype(int)
df.dropna(subset=['test group', 'converted', 'total ads', 'most ads hour'], inplace=True)

# Features and Target
features = ['test group', 'total ads', 'most ads hour'] + [col for col in df.columns if col.startswith('most ads day_')]
X = df[features]
y = df['converted']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42))
])

# Train model
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:,1]

# Create 'images' folder if not exists
if not os.path.exists('images'):
    os.makedirs('images')

# Save Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Logistic Regression - Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig('images/LogisticReg_confusion_matrix.png')
plt.close()

# Save ROC Curve
plt.figure(figsize=(6, 4))
RocCurveDisplay.from_estimator(pipeline, X_test, y_test)
plt.title('Logistic Regression - ROC Curve')
plt.tight_layout()
plt.savefig('images/LogisticReg_roc_curve.png')
plt.close()

# Save Model
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

# Save input columns
with open("input_columns.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)

# Print Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))