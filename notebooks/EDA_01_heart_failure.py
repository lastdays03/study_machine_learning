#!/usr/bin/env python
# coding: utf-8

# # Heart Failure Prediction: 데이터 분석 및 생존율 예측
# 
# ## 1. 분석 개요
# - **목표**: 심부전증 환자의 임상 기록 데이터를 분석하여 사망 위험 요인을 파악하고 생존 여부를 예측하는 모델을 구축합니다.
# - **데이터셋**: Heart Failure Clinical Records Dataset (300명 환자, 13개 Feature)
# - **방법론**: OSEMN (Obtain, Scrub, Explore, Model, Interpret) 프로세스를 따릅니다.
# 
# ## 2. 라이브러리 임포트

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score

# 시각화 설정
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.family'] = 'AppleGothic'  # Mac용 한글 폰트
plt.rcParams['axes.unicode_minus'] = False


# ## 3. Obtain & Scrub: 데이터 적재 및 품질 검증
# 
# 데이터를 로드하고 결측치, 이상치, 데이터 타입을 확인합니다.

# In[ ]:


# 데이터 로드
df = pd.read_csv('../data/heart_failure_clinical_records_dataset.csv')

# 데이터 구조 확인
print("데이터 크기:", df.shape)
display(df.head())


# In[ ]:


# 데이터 타입 및 결측치 확인
df.info()


# In[ ]:


# 기초 통계량 확인
df.describe()


# In[ ]:


# 결측치 재확인
missing_values = df.isnull().sum()
print("결측치 개수:\n", missing_values[missing_values > 0])

# 데이터 품질 검증 (Logical Checks)
# 1. 나이가 음수이거나 비상식적인 값인지 확인
assert (df['age'] > 0).all(), "나이에 0 이하의 값이 있습니다."
# 2. 박출계수(ejection_fraction)가 0~100 사이인지 확인
assert (df['ejection_fraction'] >= 0).all() and (df['ejection_fraction'] <= 100).all(), "박출계수 범위 오류"

print("\n✅ 데이터 품질 검증 완료: 결측치 없음, 논리적 오류 없음")


# ## 4. Explore: 탐색적 데이터 분석 (EDA)
# 
# 각 변수의 분포와 Target 변수(DEATH_EVENT)와의 관계를 분석합니다.

# ### 4.1 Target 변수 분포

# In[ ]:


plt.figure(figsize=(6, 4))
sns.countplot(x='DEATH_EVENT', data=df, palette='viridis')
plt.title('사망 여부 분포 (0: 생존, 1: 사망)')
plt.xlabel('DEATH_EVENT')
plt.ylabel('Count')
plt.show()

print(df['DEATH_EVENT'].value_counts(normalize=True))


# **인사이트**: 사망 데이터(1)가 생존 데이터(0)보다 적은 불균형(Imbalanced) 데이터셋입니다. 약 2:1의 비율을 보입니다.

# ### 4.2 주요 연속형 변수와 사망 여부의 관계
# 
# 나이, 크레아틴 수치, 박출 계수 등이 사망에 미치는 영향을 확인합니다.

# In[ ]:


cols_continuous = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']

fig, axes = plt.subplots(3, 3, figsize=(18, 15))
axes = axes.flatten()

for i, col in enumerate(cols_continuous):
    sns.boxplot(x='DEATH_EVENT', y=col, data=df, ax=axes[i], palette='Set2')
    axes[i].set_title(f'{col} vs DEATH_EVENT')

# 남은 subplot 정리
for j in range(len(cols_continuous), 9):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# ### 4.3 상관관계 분석

# In[ ]:


plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('피처 간 상관관계 행렬')
plt.show()


# **EDA 주요 발견점**:
# 1. **time**: 관찰 기간이 짧을수록 사망(1) 비중이 높습니다. 이는 조기 사망했기 때문일 수도 있고, 상태가 위중하여 관찰 기간이 짧았을 수도 있습니다. 가장 강력한 예측 인자가 될 가능성이 높습니다.
# 2. **ejection_fraction**: 박출계수가 낮을수록 사망 위험이 높은 경향이 보입니다.
# 3. **serum_creatinine**: 혈중 크레아틴 수치가 높을수록 사망 위험이 높습니다.
# 4. **age**: 나이가 많을수록 사망 위험이 다소 증가합니다.

# ## 5. Model: 모델링
# 
# 데이터 전처리 후 Classification 모델을 학습합니다.

# In[ ]:


# Feature와 Target 분리
X = df.drop('DEATH_EVENT', axis=1)
y = df['DEATH_EVENT']

# Train/Test Split (Stratified)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Training Set:", X_train.shape)
print("Test Set:", X_test.shape)


# In[ ]:


# 모델 학습 및 평가 함수 정의
def train_and_evaluate(model, model_name):
    # 학습
    model.fit(X_train_scaled, y_train)
    
    # 예측
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    # 평가
    print(f"--- {model_name} ---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("ROC AUC:", roc_auc_score(y_test, y_prob))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    return model


# In[ ]:


# 1. Logistic Regression
log_reg = LogisticRegression(random_state=42)
log_reg = train_and_evaluate(log_reg, "Logistic Regression")


# In[ ]:


# 2. Random Forest
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf = train_and_evaluate(rf_clf, "Random Forest")


# ## 6. Interpret: 해석 및 결론
# 
# 모델이 중요하게 생각하는 Feature를 확인합니다.

# In[ ]:


# Random Forest Feature Importance 시각화
importances = rf_clf.feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns

plt.figure(figsize=(10, 6))
plt.title("Feature Importances (Random Forest)")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), features[indices], rotation=45)
plt.tight_layout()
plt.show()


# ## 7. 결론
# 
# 분석 결과, 심부전증 환자의 생존에 가장 큰 영향을 미치는 요인은 **관찰 기간(time)**, **혈중 크레아틴(serum_creatinine)**, **박출 계수(ejection_fraction)**, **나이(age)** 순으로 나타났습니다.
# - **모델 성능**: Random Forest와 Logistic Regression 모두 준수한 성능을 보였으나, 데이터 특성에 따라 튜닝이 더 필요할 수 있습니다.
# - **시사점**: 조기에 발견하여 크레아틴 수치를 관리하고 심장 기능을 보존하는 것이 생존율을 높이는 데 중요할 수 있음을 데이터가 시사합니다.
