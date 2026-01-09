# 분석 계획서 (Analysis Plan): Wine Quality Prediction

**Date**: 2026-01-09
**Analyst**: AI Assistant
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 와인의 화학적 특성(12개 변수)을 기반으로 와인의 품질(또는 종류)을 딥러닝 모델로 예측하고, **모델 검증(Callback 등)을 통해 성능을 극대화**할 수 있는가?
- **Utility**:
  - 와인 품질 자동 판별 시스템 구축
  - Overfitting 방지 및 최적 모델 자동 저장을 통한 신뢰성 확보

### Success Metrics (KPI)
- [ ] **성능 지표**: Accuracy 향상 (Baseline 대비 +5% 이상 또는 절대 수치 0.85 이상)
- [ ] **최적화 지표**: Validation Loss의 최저점 도달 (Early Stopping Trigger)
- [ ] **완료 조건**: `ModelCheckpoint`와 `EarlyStopping`이 적용된 딥러닝 파이프라인 구현

---

## 2. 방법론 스크리닝 (Methodology Screening)

*   **Data Characteristics**:
    - 파일: `data/wine.csv`
    - 특징: 12개 컬럼. 마지막 컬럼이 클래스(0/1)로 추정됨 (Red/White 구분 또는 품질 이진 분류).
    - *Note*: `head` 출력 결과 `1`과 `0`이 섞여있어 이진 분류(Binary Classification) 문제로 판단됨.
*   **Preprocessing**:
    - **Scaling**: `StandardScaler` (필수)
    - **Split**: `Stratified Train/Test Split` (8:2)
*   **Modeling Strategy**:
    - **Baseline**: Logistic Regression (Linear)
    - **Deep Learning**: MLP (Dense Layers)
        - **Structure**: Input(12) -> Dense(30, Relu) -> Dense(12, Relu) -> Dense(8, Relu) -> Output(1, Sigmoid)
        - **Optimization**: Adam, Binary Crossentropy
*   **Performance Improvement (Crucial)**:
    - **Callacks**:
        - `ModelCheckpoint`: 검증 손실(`val_loss`)이 가장 낮은 최고의 가중치를 `best_model.h5`로 저장.
        - `EarlyStopping`: `val_loss`가 더 이상 개선되지 않으면(patience=20) 학습 조기 종료.

---

## 3. 예상 산출물 (Expected Deliverables)

- [ ] **Notebook**: `docs/notebooks/EDA_01_Wine.ipynb`
  - 데이터 로딩 및 EDA (Target 분포 확인)
  - 전처리 (StandardScaler)
  - 딥러닝 모델링 (Callback 적용 포함)
  - **결과 비교**: 학습 종료 후 `Best Model` 로드하여 평가

- [ ] **Insight Report**: 성능 개선 효과 확인 (학습 곡선 시각화 포함)

---

## 4. 타임라인

| 단계                            | 예상 소요 시간 |
| :------------------------------ | :------------- |
| 데이터 로딩 및 EDA              | 5 mins         |
| 전처리 및 Baseline              | 5 mins         |
| **Deep Learning (w/ Callback)** | 10 mins        |
| 검증 및 해석                    | 5 mins         |
| **Total**                       | **25 mins**    |
