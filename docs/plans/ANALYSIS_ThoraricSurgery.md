# 분석 계획서 (Analysis Plan): Thoracic Surgery Risk Prediction

**Date**: 2026-01-07
**Analyst**: @Antigravity
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 흉부 수술 환자의 임상 지표(폐기능, 병력, 연령 등)를 바탕으로 수술 후 1년 내 사망 위험(Risk1Y)을 정확히 예측할 수 있는가?
- **Utility**:
  - 수술 전 고위험군 환자를 조기에 선별하여 집중 모니터링 및 치료 계획 수립 지원
  - 환자별 맞춤형 리스크 프로필 제공을 통한 의료진의 의사결정 보조

### Success Metrics (KPI)
- [ ] **성능 지표**: 
    - **Primary**: Mean Absolute Error (MAE) 또는 Accuracy (Target 값이 0/1일 경우 F1-Score 확인 필요)
    - *데이터 확인 결과 Target이 0/1 이진 분류로 추정되므로 F1-Score 및 ROC-AUC를 주요 지표로 설정*
- [ ] **해석 지표**: 수술 후 사망 위험에 영향을 미치는 주요 요인(Top 5) 식별 (예: FVC, Age 등)
- [ ] **재현성**: Notebook이 처음부터 끝까지 에러 없이 실행 가능하고, 논리적 비약이 없음
- [ ] **완료 조건**: EDA → Feature Engineering → Model Training → Evaluation 전 과정 구현

---

## 2. 방법론 스크리닝 (Methodology Screening)
**"The Right Tool for the Job"** (Select from `SKILL.md`)

*   **Metric Selection**:
    *   **Primary Metric**: `F1-Score` (Reason: 의료 데이터 특성상 사망(양성) 클래스가 소수일 가능성이 높음. Imbalanced Data 대비)
    *   **Auxiliary Metric**: `ROC-AUC`, `Recall` (실제 고위험군을 놓치지 않는 것이 중요)
*   **Preprocessing Strategy**:
    *   **Scaling**: `StandardScaler` (Reason: 딥러닝은 스케일에 매우 민감하므로 필수)
    *   **Imbalance Handling**: `Class Weights` in loss function (Reason: 데이터가 적어 SMOTE보다 Class Weight 조정이 오버피팅 위험이 적음)
*   **Modeling Strategy**:
    *   **Baseline**: `Logistic Regression` (Linear relationship check)
    *   **Key Model (User Request)**: `Deep Learning (MLP)`
        - **Architecture**: Input Layer -> Hidden Layers (ReLU, Dropout for regularization) -> Output Layer (Sigmoid)
        - **Optimization**: Adam optimizer, Binary Crossentropy Loss
    *   **Comparison**: `Random Forest` or `XGBoost` (Tabular data SOTA comparison)
*   **Validation Strategy**:
    *   **CV Type**: `Stratified K-Fold`
    *   **Prevent Overfitting**: `Early Stopping`, `Dropout`, `L2 Regularization` (데이터셋이 470건으로 매우 작아 딥러닝 적용 시 과적합 방지가 핵심)

---

## 3. 검증 가설 (Hypothesis to Validate)

### 도메인/비즈니스 가설
1. **H1**: 폐활량 관련 지표(FVC, FEV1)가 낮을수록 수술 후 사망 위험이 높을 것이다.
2. **H2**: 고령(Age)일수록, 그리고 흡연(Smoking) 여부가 양성일수록 위험도가 증가할 것이다.
3. **H3**: 딥러닝 모델이 비선형적 관계를 학습하여 기존 선형 모델보다 높은 예측 성능을 보일 것이다.

### 데이터 품질 가설
- **H_Data1**: 데이터에 헤더가 없으므로 첫 행부터 데이터로 간주하고 적절한 컬럼명(UCI 기준)을 부여해야 한다.
- **H_Data2**: 연속형 변수에 이상치(예: 측정 오류로 인한 극단값)가 존재할 수 있다.

---

## 4. 예상 산출물 (Expected Deliverables)

- [ ] **Notebook**: `docs/notebooks/EDA_01_ThoraricSurgery.ipynb`
  - 데이터 로딩 (Header=None 처리, 컬럼명 부여) 및 품질 검증
  - 단변량/이변량 분석
  - Feature Engineering (Scaling 필수)
  - **Deep Learning Modeling**:
    - Build MLP Model (Keras/TensorFlow)
    - Plot Training History (Loss/Accuracy curves)
  - Model Comparison (DL vs Logistic vs Tree-based)
  - Stratified K-Fold CV
  - Feature Importance (Permutation Importance for DL)

- [ ] **Insight Report**: 주요 발견점 및 시사점 정리 (Markdown)
  - 딥러닝 모델의 효용성 평가 (적은 데이터셋에서의 한계 vs 성능)
  - 주요 위험 요인 Top 5

---

## 5. 데이터 개요

- **Source**: Local (`data/ThoraricSurgery3.csv`) - likely Thoracic Surgery Data Set
- **Size**: Approx 470 rows, 17 columns
- **Features (Estimated based on UCI)**:
  - **연속형**: FVC, FEV1, Age, Size of original tumour
  - **범주형**: Diagnosis, Performance status, Pain, Haemoptysis, Dyspnoea, Cough, Weakness, Type 2 DM, MI, PAD, Smoking, Asthma
  - **Target**: Risk1Y (1 year survival period) - Binary (0/1)

---

## 6. 분석 단계 (OSEMN Framework)

### Phase 1: Obtain & Scrub
- `read_csv` (header=None)
- 컬럼명 매핑
- 결측치 및 데이터 타입 확인

### Phase 2: Explore
- Target 분포 확인
- Scaling 전후 분포 확인 (딥러닝 입력용)

### Phase 3: Model
- Stratified Train/Test Split
- Scaling (StandardScaler)
- **Deep Learning Setup**:
  - Define Architecture (Dense -> Dropout -> Dense -> Output)
  - Compile (Adam, Binary Crossentropy)
  - Train with Early Stopping
- Baseline Comparison

### Phase 4: Interpret
- Confusion Matrix, F1-Score, ROC-AUC
- Loss Curve Visualization (Overfitting check)
