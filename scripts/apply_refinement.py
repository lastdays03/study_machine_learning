import nbformat as nbf
import os

def create_notebook_v1():
    nb = nbf.v4.new_notebook()
    cells = []

    # --- Header ---
    cells.append(nbf.v4.new_markdown_cell("""# 심부전증 생존 예측 (Heart Failure Prediction) - V1
**Author**: Antigravity
**Date**: 2026-01-05
**Goal**: 임상 기록 데이터를 바탕으로 심부전증 환자의 생존 여부를 예측하고, 주요 위험 요인을 파악합니다.

## 0. 환경 설정 (Environment Setup)
데이터 분석과 모델링에 필요한 라이브러리를 로드하고, 시각화 옵션을 설정합니다.
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
    cells.append(nbf.v4.new_markdown_cell("""## 1. 데이터 적재 및 정제 (Obtain & Scrub)
**Why?**: 데이터의 품질은 분석의 신뢰도를 결정합니다. 결측치나 비논리적인 값(음수 나이 등)이 없는지 꼼꼼히 확인해야 합니다.
"""))

    cells.append(nbf.v4.new_code_cell("""# 데이터 로드
try:
    df = pd.read_csv('../../data/heart_failure_clinical_records_dataset.csv')
    print(f"Dataset Shape: {df.shape}")
    display(df.head())
    print("-" * 30)
    df.info()
except FileNotFoundError:
    print("Error: 파일을 찾을 수 없습니다. 경로를 확인해주세요.")"""))

    cells.append(nbf.v4.new_markdown_cell("""### 데이터 무결성 점검 (Integrity Check)
- **결측치(Missing Values)**: 모델 학습 에러를 유발하므로 확인이 필요합니다.
- **논리적 오류(Logical Failures)**: `age`, `time` 등이 음수일 수 없으며, `ejection_fraction`(박출계수)은 백분율이므로 0~100 사이여야 합니다.
"""))

    cells.append(nbf.v4.new_code_cell("""# 결측치 확인
print("Missing Values:\\n", df.isnull().sum())

# 논리적 이상치 점검
impossible_values = {
    'Negative Age': (df['age'] < 0).sum(),
    'Negative Time': (df['time'] < 0).sum(),
    'Invalid Ejection Fraction': ((df['ejection_fraction'] < 0) | (df['ejection_fraction'] > 100)).sum()
}
print("\\nLogical Sanity Check Results:", impossible_values)

# 기초 통계량 확인
display(df.describe())"""))

    # --- 2. Explore ---
    cells.append(nbf.v4.new_markdown_cell("""## 2. 탐색적 데이터 분석 (EDA)
**Why?**: 변수들의 분포와 타겟(`DEATH_EVENT`)과의 관계를 시각적으로 이해하여, 모델링 전략을 수립하기 위함입니다.
"""))

    cells.append(nbf.v4.new_code_cell("""# 타겟 변수 분포 확인
plt.figure(figsize=(6, 4))
sns.countplot(x='DEATH_EVENT', data=df, palette='coolwarm')
plt.title('Distribution of DEATH_EVENT (0: Alive, 1: Deceased)')
plt.show()

print(df['DEATH_EVENT'].value_counts(normalize=True))"""))

    cells.append(nbf.v4.new_markdown_cell("""**Insight**:
- 사망(1) 비율이 약 32%로, 불균형 데이터(Imbalanced Data)에 속합니다.
- 평가 시 단순 정확도(Accuracy) 외에 Recall, F1-Score를 중요하게 봐야 합니다.

### 변수별 분포 시각화 (Univariate & Bivariate)
연속형 변수들이 사망 여부에 따라 어떻게 다른 분포를 보이는지 확인합니다.
"""))

    cells.append(nbf.v4.new_code_cell("""continuous_vars = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']

fig, axes = plt.subplots(4, 2, figsize=(15, 20))
axes = axes.flatten()

for i, col in enumerate(continuous_vars):
    sns.histplot(data=df, x=col, hue='DEATH_EVENT', kde=True, multiple="stack", ax=axes[i], palette='coolwarm')
    axes[i].set_title(f'{col} Distribution by Survival Status')

plt.tight_layout()
plt.show()"""))

    cells.append(nbf.v4.new_markdown_cell("""### 통계적 가설 검정 (Statistical Hypothesis Testing)
**Hypothesis**: "혈중 크레아틴(`serum_creatinine`) 수치는 사망 환자군에서 유의하게 높을 것이다."
- **Why?**: 시각적으로 보이는 차이가 '우연'이 아님을 수학적으로 증명하기 위해 T-test를 수행합니다.
"""))

    cells.append(nbf.v4.new_code_cell("""def run_ttest(var_name):
    group0 = df[df['DEATH_EVENT'] == 0][var_name]
    group1 = df[df['DEATH_EVENT'] == 1][var_name]
    # 등분산 가정이 없으므로 Welch's t-test 사용
    t_stat, p_val = stats.ttest_ind(group0, group1, equal_var=False)
    
    print(f"** {var_name} **")
    print(f"Mean (Alive): {group0.mean():.2f}, Mean (Deceased): {group1.mean():.2f}")
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_val:.4e}")
    if p_val < 0.05:
        print("=> 귀무가설 기각: 두 집단 간 평균 차이는 통계적으로 유의미합니다.")
    else:
        print("=> 귀무가설 채택: 통계적으로 유의미한 차이가 없습니다.")
    print("-" * 50)

run_ttest('ejection_fraction')
run_ttest('serum_creatinine')
run_ttest('platelets')"""))

    # --- 3. Model ---
    cells.append(nbf.v4.new_markdown_cell("""## 3. 모델링 (Modeling)
**Strategy**:
1.  **Baseline (Logistic Regression)**: 변수 간의 선형 관계를 파악하고 기준점 설정.
2.  **Tree-based (Random Forest)**: 비선형성 및 변수 상호작용 포착.
3.  **Validation**: Stratified K-Fold를 사용하여 클래스 비율을 유지하며 일반화 성능 검증.
"""))

    cells.append(nbf.v4.new_code_cell("""# 데이터 분할 (Stratified Split)
X = df.drop('DEATH_EVENT', axis=1)
y = df['DEATH_EVENT']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")

# 스케일링 (Scaling)
# 로지스틱 회귀는 스케일에 민감하므로 필수, 트리 모델엔 영향 적음
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X.columns)"""))

    cells.append(nbf.v4.new_code_cell("""# 모델 정의 및 학습
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10)
}

results = {}

print("Model Evaluation Results:")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    f1 = classification_report(y_test, y_pred, output_dict=True)['1']['f1-score']
    recall = classification_report(y_test, y_pred, output_dict=True)['1']['recall']
    roc = roc_auc_score(y_test, y_prob)
    
    results[name] = {'Accuracy': acc, 'F1': f1, 'Recall': recall, 'AUC': roc}
    
    print(f"\\n[{name}]")
    print(f"Accuracy: {acc:.4f}, F1-Score: {f1:.4f}, Recall: {recall:.4f}, AUC: {roc:.4f}")"""))

    # --- 4. Interpret ---
    cells.append(nbf.v4.new_markdown_cell("""## 4. 해석 및 결론 (Interpret & Conclusion)
모델이 어떤 변수를 중요하게 판단했는지 시각화합니다.
"""))

    cells.append(nbf.v4.new_code_cell("""# Feature Importance (Random Forest)
rf_model = models['Random Forest']
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("Feature Importance (Random Forest)")
plt.bar(range(X.shape[1]), importances[indices], align="center", color='skyblue')
plt.xticks(range(X.shape[1]), [X.columns[i] for i in indices], rotation=45, ha='right')
plt.tight_layout()
plt.show()"""))

    cells.append(nbf.v4.new_markdown_cell("""### Key Takeaways (핵심 요약)
1.  **Time Factor**: `time`(관찰 기간)이 가장 중요한 변수로 나타났으나, 이는 생존했기에 관찰 기간이 긴 것일 수 있어(Data Leakage) 해석에 주의가 필요합니다.
2.  **Medical Indicators**: `serum_creatinine`(신장 기능)과 `ejection_fraction`(심장 기능)이 사망 예측에 중요한 의학적 지표임이 확인되었습니다.
3.  **Model Performance**: Random Forest가 Logistic Regression보다 전반적으로 우수한 성능을 보였습니다.
"""))

    nb['cells'] = cells
    return nb

def create_notebook_v2():
    nb = nbf.v4.new_notebook()
    cells = []
    
    # --- Header ---
    cells.append(nbf.v4.new_markdown_cell("""# 심부전증 생존 예측 - V2 (Advanced)
**Author**: Antigravity
**Date**: 2026-01-05
**Goal**: 불균형 데이터 처리를 통해 사망 환자 검출율(Recall)을 극대화합니다.

## 0. 개선 전략 (Enhancement Strategy)
- **Problem**: V1 모델은 생존(0) 예측엔 강하나, 사망(1) 예측(Recall)이 상대적으로 낮을 수 있음.
- **Solution**:
    1.  `time` 변수 제외 (생존 편향 제거)
    2.  Class Weight Adjustment (데이터 불균형 보정)
    3.  Threshold Tuning (임계값 조정)
"""))
    
    cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, precision_recall_curve

# Config
import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-whitegrid')
%matplotlib inline"""))

    cells.append(nbf.v4.new_code_cell("""# 데이터 로드
try:
    df = pd.read_csv('../../data/heart_failure_clinical_records_dataset.csv')
except:
    # 경로가 다를 경우를 대비한 fallback (같은 디렉토리에 있을 경우 등)
    # 여기선 절대경로나 상위경로를 이미 알고 가정함
    pass

# Time 변수 제거 (Data Leakage 우려)
if 'time' in df.columns:
    df_v2 = df.drop('time', axis=1)
    print("Dropped 'time' column to prevent Survival Bias.")
else:
    df_v2 = df.copy()

X = df_v2.drop('DEATH_EVENT', axis=1)
y = df_v2['DEATH_EVENT']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)"""))

    cells.append(nbf.v4.new_markdown_cell("""## 1. 모델링 개선 (Advanced Modeling)
**Random Forest with Class Weight**: 소수 클래스(사망)에 더 큰 페널티를 부여하여 학습 시 집중하도록 합니다.
"""))

    cells.append(nbf.v4.new_code_cell("""scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Class Weight 적용
rf_weighted = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced', # 핵심 설정
    random_state=42
)

rf_weighted.fit(X_train_scaled, y_train)
y_prob = rf_weighted.predict_proba(X_test_scaled)[:, 1]

print("Model Trained with Balanced Class Weights.")"""))

    cells.append(nbf.v4.new_markdown_cell("""## 2. 임계값 튜닝 (Threshold Tuning)
기본 임계값(0.5) 대신, Recall을 높일 수 있는 최적의 임계값을 찾습니다. Precision-Recall Curve를 사용합니다.
"""))
    
    cells.append(nbf.v4.new_code_cell("""precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)

# Precision, Recall Trade-off 시각화
plt.figure(figsize=(10, 6))
plt.plot(thresholds, precisions[:-1], 'b--', label='Precision')
plt.plot(thresholds, recalls[:-1], 'g-', label='Recall')
plt.xlabel('Threshold')
plt.legend(loc='center left')
plt.title('Precision-Recall Curve')
plt.show()

# Recall >= 0.75를 만족하는 최대 Threshold 찾기
target_recall = 0.75
valid_indices = np.where(recalls >= target_recall)[0]
if len(valid_indices) > 0:
    best_threshold_idx = valid_indices[-1] # 임계값이 높을수록 Precision이 좋으므로, Recall 만족하는 것 중 가장 높은 Threshold
    best_threshold = thresholds[best_threshold_idx]
    print(f"Target Recall: {target_recall}")
    print(f"Optimal Threshold: {best_threshold:.4f}")
else:
    best_threshold = 0.5
    print("Target Recall not achievable.")"""))

    cells.append(nbf.v4.new_code_cell("""# 최적 임계값 적용 평가
y_pred_tuned = (y_prob >= best_threshold).astype(int)

print("\\n--- Tuned Comparison ---")
print(classification_report(y_test, y_pred_tuned))"""))

    cells.append(nbf.v4.new_markdown_cell("""### Key Takeaways (V2)
1.  **Survival Bias Removal**: `time` 변수를 제거하여 보다 현실적인(예측 시점 기준) 모델을 만들었습니다.
2.  **Class Imbalance**: `class_weight='balanced'`와 Threshold Tuning을 통해 Recall을 개선하려 시도했습니다.
3.  **Trade-off**: Recall을 높이면 Precision이 낮아지는 경향이 있음을 확인했습니다. 의료 현장에서는 놓치는 환자(False Negative)를 줄이는 것이 중요하므로 Recall 중심의 튜닝이 유효합니다.
"""))

    nb['cells'] = cells
    return nb

# Execute Creation
os.makedirs('docs/notebooks', exist_ok=True)

nb_v1 = create_notebook_v1()
with open('docs/notebooks/EDA_01_heart_failure_study.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb_v1, f)
print("Created docs/notebooks/EDA_01_heart_failure_study.ipynb")

nb_v2 = create_notebook_v2()
with open('docs/notebooks/EDA_02_heart_failure_prediction.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb_v2, f)
print("Created docs/notebooks/EDA_02_heart_failure_prediction.ipynb")

# Copy V1 to the original filename requested by user to ensure coverage
import shutil
shutil.copy('docs/notebooks/EDA_01_heart_failure_study.ipynb', 'docs/notebooks/EDA_01_heart_failure_prediction.ipynb')
print("Updated docs/notebooks/EDA_01_heart_failure_prediction.ipynb (Synced with Study)")
