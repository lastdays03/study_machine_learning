# 분석 계획서 (Analysis Plan): Sonar Mineral Prediction

**Date**: 2026-01-09
**Analyst**: AI Assistant
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 음파 탐지 데이터(Sonar)의 60개 주파수 에너지를 분석하여, 해당 물체가 기뢰(Mine)인지 바위(Rock)인지 정확하게 판별할 수 있는가?
- **Utility**:
  - 딥러닝 모델을 활용한 고성능 분류 모델 확보
  - 기뢰 탐지 자동화 및 오탐지 감소

### Success Metrics (KPI)
- [ ] **성능 지표**: Accuracy ≥ 0.85, ROC-AUC ≥ 0.90
- [ ] **해석 지표**: Loss 수렴 그래프 확인 (Overfitting 여부 판단)
- [ ] **재현성**: 전체 파이프라인(전처리-학습-검증)의 자동화 및 에러 없는 실행
- [ ] **완료 조건**: MLP(Deep Learning) 모델 구현 및 K-Fold Cross Validation을 통한 성능 검증 완료

---

## 2. 방법론 스크리닝 (Methodology Screening)
**"The Right Tool for the Job"** (Select from `SKILL.md`)

*   **Metric Selection**:
    *   **Primary Metric**: `Accuracy` (바위 vs 기뢰 분류의 정확성이 중요)
    *   **Auxiliary Metric**: `Binary Crossentropy Loss` (학습 안정성 확인)
*   **Preprocessing Strategy**:
    *   **Scaling**: `StandardScaler` or `MinMaxScaler` (딥러닝 학습 수렴을 위해 필수, 0~1 또는 표준정규분포로 변환)
    *   **Encoding**: `LabelEncoder` (Target 변수: R/M -> 0/1 변환 필요 시)
    *   **Imbalance Handling**: 데이터 분포 확인 후 결정 (Stratified Split 기본 적용)
*   **Modeling Strategy**:
    *   **Baseline**: `Logistic Regression` (선형 분리 가능성 확인을 위한 기준점)
    *   **Advanced Candidates**: `MLP (Multi-Layer Perceptron)` (사용자 요청: 딥러닝 적용. Keras/TensorFlow 활용)
*   **Validation Strategy**:
    *   **CV Type**: `Stratified K-Fold (k=5)` (소규모 데이터셋의 과적합 방지 및 일반화 성능 평가)
    *   **Hyperparameter Tuning**: 은닉층 노드 수, Epoch, Batch Size 조정

---

## 3. 검증 가설 (Hypothesis to Validate)

### 도메인/비즈니스 가설
1. **H1**: 특정 주파수 대역(Feature)의 에너지 값이 기뢰와 바위를 구분하는 결정적 요인일 것이다.
2. **H2**: 단순 선형 모델보다 비선형 패턴을 학습하는 딥러닝 모델의 성능이 더 우수할 것이다.

### 데이터 품질 가설
- **H_Data1**: 60개 변수 모두 연속형 수치 데이터일 것이며, 결측치는 없을 것이다.
- **H_Data2**: 각 변수의 스케일은 0.0 ~ 1.0 사이로 분포할 가능성이 높다 (Sonar 데이터 특성).

---

## 4. 예상 산출물 (Expected Deliverables)

- [ ] **Notebook**: `docs/notebooks/EDA_01_Sonar.ipynb`
  - 데이터 로딩 (Header 처리 주의)
  - 기초 통계 및 결측치 확인
  - 시각화: Target 분포, 주요 Feature 분포
  - 전처리: 스케일링, Train/Test Split
  - 모델링: Keras Sequential API를 이용한 모델 설계
  - 학습: `model.fit()` 및 History 시각화
  - 평가: Test Set Accuracy 및 K-Fold 검증 평균 점수

- [ ] **Insight Report**: 모델 성능 요약 및 개선 방향 제언 (Walkthrough에 포함)

---

## 5. 데이터 개요

- **Source**: `data/sonar3.csv`
- **Features**:
  - **연속형**: 0번 ~ 59번 컬럼 (60개 주파수 에너지 값)
  - **Target**: 60번 컬럼 (Class Label)

---

## 6. 분석 단계 (OSEMN Framework)

### Phase 1: Obtain & Scrub
- `pandas` read_csv (header=None)
- `pd.to_numeric` (필요 시)
- 결측치(`isnull().sum()`) 확인

### Phase 2: Explore
- Target Class Balance 확인 (`value_counts()`)
- Feature들의 상관관계 (`heatmap` - 60개라 복잡할 수 있음, 요약 통계 위주)

### Phase 3: Model (Deep Learning)
- **Architecture**:
  - Input Layer (60 nodes)
  - Hidden Layers (e.g., Dense 24, Dense 10, Relu activation)
  - Output Layer (1 node, Sigmoid activation)
- **Compilation**:
  - Optimizer: Adam
  - Loss: Binary Crossentropy
  - Metrics: Accuracy
- **Training**:
  - Early Stopping 적용 고려 (Epoch 과다 시)

### Phase 4: Interpret
- 학습 곡선(Loss/Accuracy Curve) 시각화
- 최종 Test Accuracy 보고

---

## 7. 타임라인

| 단계                     | 예상 소요 시간 |
| :----------------------- | :------------- |
| 데이터 로딩 및 품질 검증 | 5 mins         |
| EDA 및 시각화            | 10 mins        |
| 모델링 (Baseline + MLP)  | 20 mins        |
| 검증 및 해석             | 10 mins        |
| **Total**                | **45 mins**    |
