import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
import os

# Create a new notebook
nb = nbf.v4.new_notebook()

# Define the content of the notebook cells
cells = []

# 1. Imports
cells.append(nbf.v4.new_markdown_cell("# Heart Failure Prediction Analysis\n\n## 1. Environment Setup"))
cells.append(nbf.v4.new_code_cell("""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score, recall_score
from IPython.display import display
import warnings

warnings.filterwarnings('ignore')
%matplotlib inline

# Set aesthetic style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
"""))

# 2. Data Loading & Profiling
cells.append(nbf.v4.new_markdown_cell("## 2. Data Loading & Quality Check"))
cells.append(nbf.v4.new_code_cell("""
# Load dataset
try:
    df = pd.read_csv('../../data/heart_failure_clinical_records_dataset.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found.")
    df = None

if df is not None:
    # Basic Info
    print("Dataset Shape:", df.shape)
    print("\\nInfo:")
    df.info()

    print("\\nMissing Values:")
    print(df.isnull().sum())

    print("\\nHead:")
    display(df.head())

    print("\\nDescription:")
    display(df.describe())
"""))

# 3. EDA
cells.append(nbf.v4.new_markdown_cell("## 3. Exploratory Data Analysis (EDA)"))
cells.append(nbf.v4.new_code_cell("""
if df is not None:
    # Target Distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x='DEATH_EVENT', data=df)
    plt.title('Distribution of Target Variable (DEATH_EVENT)')
    plt.show()

    print("Death Event Ratio:")
    print(df['DEATH_EVENT'].value_counts(normalize=True))
    
    # Correlation Matrix
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

    # Age vs Death Event
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='age', hue='DEATH_EVENT', kde=True, element="step")
    plt.title('Age Distribution by Death Event')
    plt.show()
    
    # Pairplot for selected features
    selected_features = ['age', 'ejection_fraction', 'serum_creatinine', 'serum_sodium', 'DEATH_EVENT']
    sns.pairplot(df[selected_features], hue='DEATH_EVENT')
    plt.show()
"""))

# 4. Modeling
cells.append(nbf.v4.new_markdown_cell("## 4. Modeling & Evaluation"))
cells.append(nbf.v4.new_code_cell("""
if df is not None:
    # Feature Selection & Split
    X = df.drop('DEATH_EVENT', axis=1)
    y = df['DEATH_EVENT']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")

    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'Random Forest': RandomForestClassifier(random_state=42),
        'XGBoost': XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
    }

    results = {}

    for name, model in models.items():
        print(f"Training {name}...")
        # Pipeline for scaling
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', model)
        ])
        
        # Stratified K-Fold CV
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='f1')
        
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        
        results[name] = {
            'CV F1 Mean': scores.mean(),
            'Test F1': f1_score(y_test, y_pred),
            'Test Recall': recall_score(y_test, y_pred),
            'Model': pipeline
        }
        
        print(f"{name} CV F1: {scores.mean():.4f}")
        print(f"{name} Test F1: {f1_score(y_test, y_pred):.4f}")
        print("-" * 30)
"""))

# 5. Result Summary
cells.append(nbf.v4.new_markdown_cell("## 5. Result Summary"))
cells.append(nbf.v4.new_code_cell("""
if df is not None:
    res_df = pd.DataFrame(results).T[['CV F1 Mean', 'Test F1', 'Test Recall']]
    display(res_df)

    # Feature Importance (Random Forest)
    # Access the classifier step from the pipeline
    rf_model = results['Random Forest']['Model'].named_steps['classifier']
    importances = rf_model.feature_importances_
    indices = np.argsort(importances)[::-1]
    features = X.columns
    
    plt.figure(figsize=(10, 6))
    plt.title("Feature Importances (Random Forest)")
    plt.bar(range(X.shape[1]), importances[indices], align="center")
    plt.xticks(range(X.shape[1]), features[indices], rotation=90)
    plt.xlim([-1, X.shape[1]])
    plt.tight_layout()
    plt.show()
"""))

nb.cells = cells

# Save and Execute
notebook_path = 'docs/notebooks/EDA_01_heart_failure_prediction.ipynb'
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
