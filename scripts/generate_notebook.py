import nbformat as nbf
import os

# Define the notebook content
nb = nbf.v4.new_notebook()

# Cells list
cells = []

# --- Header ---
cells.append(nbf.v4.new_markdown_cell("""# Heart Failure Prediction Analysis
**Author**: Antigravity
**Date**: 2026-01-05
**Goal**: Predict survival of patients with heart failure using clinical records.

## 0. Environment Setup
Loading necessary libraries and setting display options.
"""))

cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Scikit-learn
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

# Configuration
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8-whitegrid')
%matplotlib inline

print("Libraries loaded successfully.")"""))

# --- 1. Obtain & Scrub ---
cells.append(nbf.v4.new_markdown_cell("""## 1. Obtain & Scrub (Data Loading & Cleaning)
Loading the dataset and checking for data integrity (missing values, data types, logical errors).
"""))

cells.append(nbf.v4.new_code_cell("""# Load Data
df = pd.read_csv('../../data/heart_failure_clinical_records_dataset.csv')

# Check structure
print(f"Dataset Shape: {df.shape}")
display(df.head())
print("-" * 30)
df.info()"""))

cells.append(nbf.v4.new_markdown_cell("""### Data Integrity Check
- **Missing Values**: Checking for nulls.
- **Logical Failures**: Verifying if `age`, `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium`, `time` are within reasonable ranges (no negative values).
"""))

cells.append(nbf.v4.new_code_cell("""# Missing Values
print("Missing Values:\\n", df.isnull().sum())

# Logical Sanity Check
impossible_values = {
    'Negative Age': (df['age'] < 0).sum(),
    'Negative Time': (df['time'] < 0).sum(),
    'Invalid Ejection Fraction': ((df['ejection_fraction'] < 0) | (df['ejection_fraction'] > 100)).sum()
}
print("\\nLogical Sanity Check Results:", impossible_values)

# Descriptive Statistics
display(df.describe())"""))

# --- 2. Explore ---
cells.append(nbf.v4.new_markdown_cell("""## 2. Explore (Exploratory Data Analysis)
Investigating the distribution of variables and their relationship with the target (`DEATH_EVENT`).
"""))

cells.append(nbf.v4.new_code_cell("""# Target Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='DEATH_EVENT', data=df, palette='coolwarm')
plt.title('Distribution of DEATH_EVENT (Target)')
plt.show()

print(df['DEATH_EVENT'].value_counts(normalize=True))"""))

cells.append(nbf.v4.new_markdown_cell("""**Interpretation**:
- The dataset is imbalanced. We need to check the exact ratio.
- If the imbalance is severe, we might need stratified sampling or re-sampling techniques.

### Univariate & Bivariate Analysis
Analyzing key continuous variables against `DEATH_EVENT`.
"""))

cells.append(nbf.v4.new_code_cell("""continuous_vars = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']

fig, axes = plt.subplots(4, 2, figsize=(15, 20))
axes = axes.flatten()

for i, col in enumerate(continuous_vars):
    sns.histplot(data=df, x=col, hue='DEATH_EVENT', kde=True, multiple="stack", ax=axes[i], palette='coolwarm')
    axes[i].set_title(f'{col} Distribution by Target')

plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""### Correlation Analysis
Checking the correlation between numerical features.
"""))

cells.append(nbf.v4.new_code_cell("""plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""### Statistical Hypothesis Testing
**H1**: `ejection_fraction` levels differ significantly between surviving and deceased patients.
**H2**: `serum_creatinine` levels differ significantly between surviving and deceased patients.
Using T-test to validate.
"""))

cells.append(nbf.v4.new_code_cell("""def run_ttest(var_name):
    group0 = df[df['DEATH_EVENT'] == 0][var_name]
    group1 = df[df['DEATH_EVENT'] == 1][var_name]
    t_stat, p_val = stats.ttest_ind(group0, group1, equal_var=False) # Welch's t-test
    print(f"** {var_name} **")
    print(f"Mean (Alive): {group0.mean():.2f}, Mean (Deceased): {group1.mean():.2f}")
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_val:.4e}\\n")

run_ttest('ejection_fraction')
run_ttest('serum_creatinine')
run_ttest('time')"""))

# --- 3. Model ---
cells.append(nbf.v4.new_markdown_cell("""## 3. Model (Predictive Modeling)
Building and evaluating machine learning models.
- **Preprocessing**: StandardScaler
- **Models**: Logistic Regression, Decision Tree, Random Forest
- **Validation**: Stratified K-Fold CV
"""))

cells.append(nbf.v4.new_code_cell("""# Train/Test Split
X = df.drop('DEATH_EVENT', axis=1)
y = df['DEATH_EVENT']

# Stratified Split to maintain class ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")

# Scaling (Important for Logistic Regression, helpful for others)
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X.columns)"""))

cells.append(nbf.v4.new_code_cell("""# Model Initialization
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100)
}

# Training and Evaluation Loop
results = {}

for name, model in models.items():
    # Train
    model.fit(X_train_scaled, y_train)
    
    # Predict
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    # Evaluate
    acc = accuracy_score(y_test, y_pred)
    f1 = classification_report(y_test, y_pred, output_dict=True)['1']['f1-score'] # F1 for positive class
    recall = classification_report(y_test, y_pred, output_dict=True)['1']['recall']
    roc_auc = roc_auc_score(y_test, y_prob)
    
    results[name] = {'Accuracy': acc, 'F1-Score': f1, 'Recall': recall, 'ROC-AUC': roc_auc}
    
    print(f"--- {name} ---")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))"""))

cells.append(nbf.v4.new_markdown_cell("""### Cross-Validation
Validating model stability using Stratified K-Fold (k=5).
"""))

cells.append(nbf.v4.new_code_cell("""cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("Cross-Validation Scores (Accuracy):")
for name, model in models.items():
    scores = cross_val_score(model, X_train_scaled, y_train, cv=cv, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")"""))

# --- 4. Interpret ---
cells.append(nbf.v4.new_markdown_cell("""## 4. Interpret (Model Explanation)
Understanding why the models made their predictions.
"""))

cells.append(nbf.v4.new_code_cell("""# Feature Importance (Random Forest)
rf_model = models['Random Forest']
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("Feature Importance (Random Forest)")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), [X.columns[i] for i in indices], rotation=45, ha='right')
plt.tight_layout()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""### Decision Tree Visualization
Visualizing the decision rules of the Decision Tree model.
"""))

cells.append(nbf.v4.new_code_cell("""dt_model = models['Decision Tree']
plt.figure(figsize=(20, 10))
plot_tree(dt_model, feature_names=X.columns, class_names=['Survival', 'Death'], filled=True, rounded=True, fontsize=10)
plt.show()"""))

# Add cells to notebook
nb['cells'] = cells

# Ensure directory exists
os.makedirs('docs/notebooks', exist_ok=True)

# Write file
file_path = 'docs/notebooks/EDA_01_heart_failure_study.ipynb'
with open(file_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Notebook created at: {file_path}")
