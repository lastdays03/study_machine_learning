import nbformat as nbf
import os

nb = nbf.v4.new_notebook()
cells = []

# --- Header ---
cells.append(nbf.v4.new_markdown_cell("""# Heart Failure Prediction V3: Revisit with New Methods
**Author**: Antigravity
**Date**: 2026-01-06
**Goal**: 업데이트된 워크플로우(`SKILL.md`)를 반영하여 심부전증 생존 예측 모델을 고도화합니다.
**Key Changes**:
1.  **New Models**: KNN (Distance-based), XGBoost (Gradient Boosting) 도입.
2.  **Metric Focus**: **Recall** (사망자 예측)을 최우선으로 하되, 5대 분류 지표를 모두 평가.
3.  **Deep Dive**: 모델이 틀린 케이스(Top 10 Worst Errors)를 심층 분석.

## 0. 환경 설정 (Environment Setup)
"""))

cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# Metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report

# Config
import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-whitegrid')
%matplotlib inline

print("Result: Libraries loaded.")"""))

# --- 1. Obtain & Scrub ---
cells.append(nbf.v4.new_markdown_cell("""## 1. 데이터 로드 및 전처리 (Obtain & Scrub)
KNN은 거리 기반 알고리즘이므로 **Standard Scaler** 적용이 필수적입니다.
"""))

cells.append(nbf.v4.new_code_cell("""df = pd.read_csv('../../data/heart_failure_clinical_records_dataset.csv')

# Feature Selection (Based on V2 findings, we keep most but 'time' is controversial. 
# V3 Hypothesis: Let's test WITHOUT 'time' strictly to avoid leakage, as requested in V2/V3 transition logic often.)
# However, for metric comparison with V1, we should be careful. 
# Let's drop 'time' for a realistic prediction scenario.

X = df.drop(['DEATH_EVENT', 'time'], axis=1)
y = df['DEATH_EVENT']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scaling (Essential for KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")"""))

# --- 2. Modeling (V3) ---
cells.append(nbf.v4.new_markdown_cell("""## 2. 모델링 (Modeling V3)
**Candidates**:
1.  **LogReg**: Baseline.
2.  **KNN**: 유클리드 거리 기반 유사 환자 탐색.
3.  **Random Forest**: V2의 베스트 모델 (비교용).
4.  **XGBoost**: 강력한 부스팅 알고리즘.
"""))

cells.append(nbf.v4.new_code_cell("""models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Random Forest': RandomForestClassifier(random_state=42, class_weight='balanced'),
    'XGBoost': XGBClassifier(random_state=42, eval_metric='logloss', scale_pos_weight=2) # scale_pos_weight for imbalance
}

results = {}

for name, model in models.items():
    # KNN and LogReg use Scaled Data. Trees can use either but Scaled is fine.
    model.fit(X_train_scaled, y_train)
    
    # Predict defaults
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    # Metrics
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred),
        'ROC-AUC': roc_auc_score(y_test, y_prob)
    }
    
    results[name] = metrics
    
    print(f"--- {name} ---")
    print(f"Recall: {metrics['Recall']:.4f} | AUC: {metrics['ROC-AUC']:.4f}")

# Visualization of Results
res_df = pd.DataFrame(results).T
display(res_df)

# Plot
res_df[['Recall', 'ROC-AUC', 'F1-Score']].plot(kind='bar', figsize=(10, 6))
plt.title("Model Performance Comparison (V3)")
plt.ylim(0.5, 1.0)
plt.axhline(0.75, color='r', linestyle='--', label='Target Recall (0.75)')
plt.legend()
plt.show()"""))

cells.append(nbf.v4.new_markdown_cell("""## 3. 심층 분석 (Interpretation)
**Top 10 Worst Errors**: XGBoost 모델이 가장 확신을 가지고 틀린 케이스(High Confidence Error)를 분석합니다.
"""))

cells.append(nbf.v4.new_code_cell("""# Error Analysis with XGBoost
best_model = models['XGBoost']
y_prob_xgb = best_model.predict_proba(X_test_scaled)[:, 1]

# Create Error DataFrame
error_df = X_test.copy()
error_df['Actual'] = y_test
error_df['Predicted_Prob'] = y_prob_xgb
error_df['Error'] = np.abs(error_df['Actual'] - error_df['Predicted_Prob'])

# Top 10 Worst Errors (Largest difference between Prob and Actual)
top_errors = error_df.sort_values('Error', ascending=False).head(10)
display(top_errors)

# Heatmap of Errors features (Standardized to see deviations)
plt.figure(figsize=(12, 6))
sns.heatmap(scaler.transform(top_errors.drop(['Actual', 'Predicted_Prob', 'Error'], axis=1)), 
            annot=True, cmap='RdBu', center=0,
            xticklabels=X.columns)
plt.title("Feature Patterns of Top 10 Prediction Errors (Z-Score)")
plt.show()
"""))

cells.append(nbf.v4.new_markdown_cell("""**Insight Derived**:
- **False Negatives (실제 사망인데 생존으로 예측)**: `Error`가 높은 상위 케이스 중 Actual=1인 경우를 봅니다.
- **공통 패턴**: 예를 들어 박출계수(`ejection_fraction`)가 정상 범위(>50)이거나 나이가 상대적으로 젊은 경우, 모델이 '생존'으로 과신했을 가능성이 있습니다.
- 이는 모델이 특정 수치(정상 범위)에 과도하게 의존함을 시사하며, 복합적인 상호작용을 더 학습해야 함을 의미합니다.
"""))

nb['cells'] = cells

# Save
os.makedirs('docs/notebooks', exist_ok=True)
with open('docs/notebooks/EDA_03_heart_failure_revisit.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook Created: docs/notebooks/EDA_03_heart_failure_revisit.ipynb")
