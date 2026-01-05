import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
import os

# Create a new notebook
nb = nbf.v4.new_notebook()

# Define the content of the notebook cells
cells = []

# 1. Imports
cells.append(nbf.v4.new_markdown_cell("# Heart Failure Prediction Analysis V2\n\n## 1. Environment & Advanced Setup"))
cells.append(nbf.v4.new_code_cell("""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score, recall_score, precision_recall_curve, precision_score
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

from IPython.display import display
import warnings

warnings.filterwarnings('ignore')
%matplotlib inline

# Set aesthetic style
sns.set_style("ticks")
sns.set_context("notebook")
plt.rcParams['figure.figsize'] = (12, 8)
print("Libraries imported successfully.")
"""))

# 2. Data Loading & Profiling
cells.append(nbf.v4.new_markdown_cell("## 2. Data Loading & Deep Quality Check"))
cells.append(nbf.v4.new_code_cell("""
# Load dataset
df = pd.read_csv('../../data/heart_failure_clinical_records_dataset.csv')
print(f"Dataset Shape: {df.shape}")

# Imbalance Check
target_counts = df['DEATH_EVENT'].value_counts(normalize=True)
print("\\nTarget Variable Distribution:")
print(target_counts)

plt.figure(figsize=(6, 4))
sns.barplot(x=target_counts.index, y=target_counts.values, palette='viridis')
plt.title("Imbalance in DEATH_EVENT")
plt.show()
"""))

# 3. Hypothesis Driven EDA (Deep)
cells.append(nbf.v4.new_markdown_cell("## 3. Advanced EDA"))
cells.append(nbf.v4.new_code_cell("""
# 1. Violin Plots for Distribution Comparison
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.violinplot(x='DEATH_EVENT', y='age', data=df, ax=axes[0], palette='muted')
sns.violinplot(x='DEATH_EVENT', y='ejection_fraction', data=df, ax=axes[1], palette='muted')
sns.violinplot(x='DEATH_EVENT', y='serum_creatinine', data=df, ax=axes[2], palette='muted')
plt.suptitle("Distribution of Key Features by Death Event", fontsize=16)
plt.show()

# 2. Interaction Effect: Age vs Creatinine
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='serum_creatinine', hue='DEATH_EVENT', data=df, palette='coolwarm', alpha=0.7)
plt.title("Interaction: Age vs Serum Creatinine")
plt.show()
"""))

# 4. Advanced Modeling
cells.append(nbf.v4.new_markdown_cell("## 4. Modeling (Recall Focused)"))
cells.append(nbf.v4.new_code_cell("""
# Feature Engineering (Interaction)
df['age_creatinine'] = df['age'] * df['serum_creatinine']

X = df.drop('DEATH_EVENT', axis=1)
y = df['DEATH_EVENT']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Split Done.")

# Models with Class Weight or SMOTE
models = {
    'RF (Balanced)': RandomForestClassifier(random_state=42, class_weight='balanced'),
    'XGBoost (ScalePosWeight)': XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss', scale_pos_weight=2), # approx 2:1 ratio
    'LightGBM': LGBMClassifier(random_state=42, class_weight='balanced', verbosity=-1)
}

results = {}

for name, model in models.items():
    print(f"Training {name} with SMOTE...")
    
    # Pipeline: Scaler -> SMOTE -> Classifier
    pipeline = ImbPipeline([
        ('scaler', RobustScaler()), # Robust to outliers
        ('smote', SMOTE(random_state=42)),
        ('classifier', model)
    ])
    
    # CV
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores_recall = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='recall')
    scores_f1 = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='f1')
    
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]
    
    results[name] = {
        'CV Recall': scores_recall.mean(),
        'CV F1': scores_f1.mean(),
        'Test Recall': recall_score(y_test, y_pred),
        'Test F1': f1_score(y_test, y_pred),
        'Test Precision': precision_score(y_test, y_pred),
        'Model': pipeline
    }
    
    print(f"{name} -> CV Recall: {scores_recall.mean():.4f}, Test Recall: {recall_score(y_test, y_pred):.4f}")

"""))

# 5. Threshold Tuning
cells.append(nbf.v4.new_markdown_cell("## 5. Threshold Tuning for Maximum Recall"))
cells.append(nbf.v4.new_code_cell("""
# Using Random Forest (Balanced) as example
best_model = results['RF (Balanced)']['Model']
y_prob = best_model.predict_proba(X_test)[:, 1]

precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)

plt.figure(figsize=(10, 6))
plt.plot(thresholds, precisions[:-1], 'b--', label='Precision')
plt.plot(thresholds, recalls[:-1], 'g-', label='Recall')
plt.xlabel('Threshold')
plt.legend(loc='center left')
plt.ylim([0, 1])
plt.title("Precision-Recall vs Threshold")
plt.show()

# Find threshold where Recall >= 0.8
optimal_idx = np.where(recalls >= 0.80)[0][-1]
optimal_threshold = thresholds[optimal_idx]
print(f"Optimal Threshold for Recall >= 0.80: {optimal_threshold:.4f}")

y_pred_tuned = (y_prob >= optimal_threshold).astype(int)
print("\\nFinal Performance with Tuned Threshold:")
print(classification_report(y_test, y_pred_tuned))
"""))

# 6. Result Summary
cells.append(nbf.v4.new_markdown_cell("## 6. Comparison V1 vs V2"))
cells.append(nbf.v4.new_code_cell("""
res_df = pd.DataFrame(results).T[['CV Recall', 'Test Recall', 'Test F1']]
print("V2 Result Summary:")
display(res_df)
"""))

nb.cells = cells

# Save and Execute
notebook_path = 'docs/notebooks/EDA_02_heart_failure_prediction.ipynb'
with open(notebook_path, 'w') as f:
    nbf.write(nb, f)

print(f"Notebook generated at {notebook_path}. Executing...")

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

# Set path for execution
try:
    ep.preprocess(nb, {'metadata': {'path': 'docs/notebooks/'}})
    print("Execution successful.")
except Exception as e:
    print(f"Execution failed: {e}")
    # Still save the notebook to show partial output or errors
    with open(notebook_path, 'w') as f:
        nbf.write(nb, f)
    raise e

# Save executed notebook
with open(notebook_path, 'w') as f:
    nbf.write(nb, f)
