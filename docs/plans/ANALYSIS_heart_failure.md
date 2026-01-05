# 분석 계획서 (Analysis Plan): Heart Failure Prediction

**Date**: 2026-01-05  
**Analyst**: bagjongman  
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 심부전증 환자의 사망 위험 요인은 무엇이며, 어떤 임상 지표가 생존율 예측에 가장 중요한가?
- **Utility**: 
  - 의료 데이터 분석 및 시각화 기법 습득
  - Scikit-learn 기반 Classification 모델 학습 방법 이해
  - 임상 데이터에서 실질적인 인사이트를 도출하는 능력 배양
  
### Success Metrics (KPI)
- [ ] **모델 성능**: ROC-AUC ≥ 0.75 (생존/사망 분류)
- [ ] **해석 가능성**: 주요 위험 요인 Top 5 식별 및 통계적 검증
- [ ] **재현성**: Notebook이 처음부터 끝까지 에러 없이 실행 가능
- [ ] **학습 목표 달성**: EDA → Feature Engineering → Model Training → Evaluation 전 과정 구현

---

## 2. 방법론 (Methodology)

- **Type**: Predictive Modeling (Binary Classification)
- **Tools**: 
  - **Data Processing**: Pandas, NumPy
  - **Visualization**: Matplotlib, Seaborn
  - **Statistical Testing**: SciPy (t-test, chi-square)
  - **Modeling**: Scikit-learn (Logistic Regression, Random Forest, XGBoost)
  - **Interpretation**: SHAP, Feature Importance
- **Target Variable**: `DEATH_EVENT` (0: 생존, 1: 사망)

---

## 3. 검증 가설 (Hypothesis to Validate)

### 임상적 가설
1. **H1**: 나이(age)가 높을수록 사망률이 증가할 것이다.
2. **H2**: 박출계수(ejection_fraction)가 낮을수록 사망 위험이 높을 것이다.
3. **H3**: 혈중 크레아틴(serum_creatinine) 수치가 높을수록 사망률이 증가할 것이다.
4. **H4**: 빈혈(anaemia), 당뇨(diabetes), 고혈압(high_blood_pressure) 등 기저질환이 있는 환자의 사망률이 더 높을 것이다.
5. **H5**: 관찰 기간(time)이 짧은 환자일수록 조기 사망 가능성이 높을 것이다.

### 데이터 품질 가설
- **H6**: 결측치가 없거나 최소한일 것이다. (의료 데이터 특성상)
- **H7**: 연속형 변수(age, creatinine_phosphokinase 등)에 이상치가 존재할 수 있다.

---

## 4. 예상 산출물 (Expected Deliverables)

- [ ] **Notebook**: `notebooks/EDA_01_heart_failure.ipynb` (전체 분석 과정)
  - 데이터 로딩 및 품질 검증
  - 단변량/이변량 분석 및 시각화
  - 통계적 검정 (t-test, chi-square)
  - Feature Engineering 및 전처리
  - Baseline 모델 구축
  - Advanced 모델 학습 (Logistic Regression, Random Forest, XGBoost)
  - Cross-Validation 및 성능 평가
  - Feature Importance 분석
  
- [ ] **Insight Report**: 주요 발견점 및 임상적 시사점 정리
  - 사망 위험 요인 Top 5
  - 모델 성능 비교 및 최적 모델 선정
  - 실무 적용 가능성 제안

- [ ] **Model Artifact**: (Optional) 최종 모델 저장 (`models/heart_failure_classifier.pkl`)

---

## 5. 데이터 개요

- **Source**: [Kaggle - Heart Failure Clinical Data](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)
- **File**: `data/heart_failure_clinical_records_dataset.csv`
- **Features** (13개):
  - **연속형 변수** (5개): age, creatinine_phosphokinase, ejection_fraction, platelets, serum_creatinine, serum_sodium, time
  - **범주형 변수** (5개): anaemia, diabetes, high_blood_pressure, sex, smoking
  - **Target**: DEATH_EVENT (Binary)

---

## 6. 분석 단계 (OSEMN Framework)

### Phase 1: Obtain & Scrub (데이터 적재 및 정제)
- CSV 파일 로드 (encoding, delimiter 확인)
- 기초 통계량 확인 (`df.info()`, `df.describe()`)
- 결측치, 중복값, 논리적 오류 검증
- 데이터 타입 검증 (numeric vs categorical)

### Phase 2: Explore (탐색적 데이터 분석)
- **Univariate Analysis**: 각 변수의 분포 확인 (Histogram, Boxplot)
- **Bivariate Analysis**: Target과의 관계 분석 (Correlation, Group Comparison)
- **Statistical Testing**: 가설 검증 (t-test for continuous, chi-square for categorical)
- **Insight Logging**: 발견된 패턴 즉시 기록

### Phase 3: Model (모델링)
- Train/Test Split (Stratified)
- Baseline Model (Dummy Classifier)
- Feature Scaling (StandardScaler)
- Model Training:
  - Logistic Regression
  - Random Forest
  - XGBoost (Optional)
- Cross-Validation (Stratified K-Fold)

### Phase 4: Interpret (해석)
- Confusion Matrix, ROC Curve, Precision-Recall Curve
- Feature Importance (Tree-based models)
- SHAP Values (Optional)
- Error Analysis (False Positives/Negatives)

---

## 7. 리스크 및 제약사항

- **데이터 크기**: 소규모 데이터셋일 가능성 (Overfitting 주의)
- **클래스 불균형**: 사망 환자 비율이 낮을 수 있음 (SMOTE 고려)
- **도메인 지식**: 의료 전문 지식 부족 (문헌 조사 필요)
- **해석 가능성**: 복잡한 모델(XGBoost)보다 Logistic Regression이 더 해석 가능

---

## 8. 타임라인

| 단계                     | 예상 소요 시간 |
| ------------------------ | -------------- |
| 데이터 로딩 및 품질 검증 | 30분           |
| EDA 및 시각화            | 1시간          |
| Feature Engineering      | 30분           |
| 모델링 및 평가           | 1시간          |
| 해석 및 리포팅           | 30분           |
| **Total**                | **3.5시간**    |
