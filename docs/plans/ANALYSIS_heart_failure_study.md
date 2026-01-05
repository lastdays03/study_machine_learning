# 분석 계획서 (Analysis Plan): Heart Failure Study

**Date**: 2026-01-05
**Analyst**: Antigravity
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 심부전증 환자의 사망 위험 요인은 무엇이며, 생존율 예측에 가장 중요한 임상 지표는 무엇인가?
- **Utility**:
  - 임상 데이터(`ejection_fraction`, `serum_creatinine` 등)를 통해 조기 경보 시스템 구축 가능성 타진.
  - 의료진이 집중 관리해야 할 고위험군 환자 식별 기준 마련.

### Success Metrics (KPI)
- [ ] **성능 지표**: Recall (Sensitivity) ≥ 0.75 (생존보다 사망 예측이 중요 - Type II Error 최소화), ROC-AUC ≥ 0.80
- [ ] **해석 지표**: 주요 위험 요인 Top 3 식별 및 시각화 (SHAP/Feature Importance)
- [ ] **재현성**: Notebook이 처음부터 끝까지 에러 없이 실행 가능하고, 논리적 비약이 없음
- [ ] **완료 조건**: EDA → Feature Engineering → Model Training (3종) → Evaluation 전 과정 구현

---

## 2. 방법론 (Methodology)

- **Type**: Detective & Predictive Modeling (Binary Classification)
- **Tools**:
  - **Data Processing**: Pandas, NumPy
  - **Visualization**: Matplotlib, Seaborn
  - **Statistical Testing**: SciPy (T-test, Chi-square for independence)
  - **Modeling**: Scikit-learn (LogisticRegression, DecisionTree, RandomForest)
  - **Interpretation**: Permutation Importance, Feature Importance (Tree-based)
- **Target Variable**: `DEATH_EVENT` (0: 생존, 1: 사망)

---

## 3. 검증 가설 (Hypothesis to Validate)

### 도메인/비즈니스 가설
1. **H1**: `ejection_fraction`(박출계수)이 낮을수록 `DEATH_EVENT` 발생 확률이 급격히 증가할 것이다.
2. **H2**: `age`(나이)와 `serum_creatinine`(혈중 크레아틴)은 상호작용하여 고령이면서 신장 기능이 저하된 경우 사망률이 매우 높을 것이다.
3. **H3**: `time`(관찰 기간)은 생존 편향(Survival Bias)이 있을 수 있으므로, 해석 시 주의가 필요하다.

### 데이터 품질 가설
- **H_Data1**: `platelets` 등 일부 변수에 극단적인 이상치(Outlier)가 존재할 것이다.
- **H_Data2**: `sex`, `smoking`, `diabetes` 등 범주형 변수의 클래스 불균형이 모델 성능에 영향을 줄 수 있다.

---

## 4. 예상 산출물 (Expected Deliverables)

- [ ] **Notebook**: `docs/notebooks/EDA_01_heart_failure_study.ipynb`
  - 데이터 로딩 및 품질 검증 (Clean Code)
  - 단변량/이변량 분석 및 시각화
  - 통계적 검정 (t-test, chi-square)
  - Feature Engineering (StandardScaler, Binning)
  - Baseline (Logistic) 및 Advanced (RF, DT) 모델 구축
  - Stratified K-Fold Cross-Validation (k=5)
  - Feature Importance 분석

- [ ] **Insight Report**: 주요 발견점 및 시사점 정리 (Markdown)
  - 주요 영향 요인(Feature) Top 3
  - 모델 성능 비교 (Accuracy vs Recall)
  - 모델의 의사결정 기준 (Tree Visualization)

---

## 5. 데이터 개요

- **Source**: Kaggle Heart Failure Clinical Records
- **File**: `data/heart_failure_clinical_records_dataset.csv`
- **Features**:
  - **연속형**: `age`, `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium`, `time`
  - **범주형**: `anaemia`, `diabetes`, `high_blood_pressure`, `sex`, `smoking`
  - **Target**: `DEATH_EVENT`

---

## 6. 분석 단계 (OSEMN Framework)

### Phase 1: Obtain & Scrub (데이터 적재 및 정제)
- 파일 로드 (encoding, delimiter 자동 감지)
- 기초 통계량(`describe`) 및 데이터 타입(`dtypes`) 검증
- **Deep Sanity Check**: `age` < 0, `ejection_fraction` > 100 등 논리적 오류 확인

### Phase 2: Explore (탐색적 데이터 분석)
- **Univariate**: 히스토그램 및 박스플롯으로 이상치 식별
- **Bivariate**: 상관관계 행렬(Heatmap) 및 산점도(Scatter) 분석
- **Hypothesis Testing**: 생존/사망 그룹 간 평균 차이 검정 (T-test)
- **Insight Logging**: 변수별 특이사항 즉시 기록

### Phase 3: Model (모델링)
- **Data Split**: Stratified Train/Test Split (80:20)
- **Preprocessing**: `StandardScaler` (트리 모델은 제외 가능하나 로지스틱 비교 위해 적용)
- **Model Training**:
    1.  **Logistic Regression** (Baseline)
    2.  **Decision Tree** (Interpretability)
    3.  **Random Forest** (Performance)
- **Validation**: Stratified K-Fold (k=5)로 일반화 성능 검증

### Phase 4: Interpret (해석)
- Confusion Matrix, Classification Report (Precision, Recall, F1)
- **Interpretation**: Feature Importance 플롯, Decision Tree 시각화
- **Error Analysis**: FP(False Positive)와 FN(False Negative) 사례 분석

---

## 7. 리스크 및 제약사항

- **데이터**: 299개의 소규모 데이터셋으로, 과적합(Overfitting) 위험이 큼.
- **도메인**: `time` 변수의 인과성 문제 (오래 살아서 관찰 기간이 긴 것인지, 관찰 기간이 길어서 생존한 것으로 기록된 것인지) 주의.

---

## 8. 타임라인

| 단계                     | 예상 소요 시간 |
| :----------------------- | :------------- |
| 데이터 로딩 및 품질 검증 | 10 mins        |
| EDA 및 시각화            | 30 mins        |
| Feature Engineering      | 15 mins        |
| 모델링 및 평가           | 20 mins        |
| 해석 및 리포팅           | 15 mins        |
| **Total**                | **90 mins**    |
