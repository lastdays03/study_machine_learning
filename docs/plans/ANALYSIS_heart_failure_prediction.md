# 분석 계획서 (Analysis Plan): Heart Failure Prediction

**Date**: 2026-01-05
**Analyst**: Antigravity
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)
- **Question**: 임상 기록 데이터를 바탕으로 심부전증 환자의 사망 여부(DEATH_EVENT)를 조기에 정확하게 예측할 수 있는가? 어떤 임상 지표가 사망 위험에 가장 큰 영향을 미치는가?
- **Utility**: 고위험군 환자를 조기에 식별하여 집중 치료 및 모니터링을 통한 생존율 향상.
- **Success Metrics (KPI)**:
    - [ ] **F1-Score**: 0.85 이상 (Imbalanced Class 고려)
    - [ ] **Recall (Sensitivity)**: 0.90 이상 (사망 위험 환자를 놓치지 않는 것이 중요)

---

## 2. 방법론 (Methodology)

### Data Processing Strategy
- **Imputation**: 결측치가 확인될 경우 `Simple Imputer` (Median) 혹은 `KNN Imputer` 사용. (Basic sanity check에서 결측이 없어도 방어적 코딩)
- **Scaling**: `StandardScaler` (나이, 혈소판 수 등 수치형 변수의 스케일 차이 보정)
- **Encoding**: 이미 수치형으로 인코딩된 범주형 변수(성별, 흡연 등)는 그대로 사용하거나 필요시 `OneHot` 변환 검토.

### Model Candidates (Methodology Screening Results)
`SKILL.md` 기준, Tabular Classification에 적합한 다음 모델을 선정함.

1.  **Logistic Regression**: Baseline 모델. 변수의 선형적 영향력 파악 용이.
2.  **Random Forest**: 비선형 관계 포착 및 Feature Importance 확인에 유리. Overfitting에 강함.
3.  **XGBoost**: 고성능 분류 모델. 결측치 처리가 내장되어 있으며 높은 예측 성능 기대.

### Validation Strategy
- **Stratified K-Fold (k=5)**: 사망(1)과 생존(0)의 비율을 유지하며 검증.

---

## 3. 검증 가설 (Hypothesis to Validate)

1.  **H1**: `ejection_fraction` (박출계수)이 낮을수록 사망 위험이 크게 증가할 것이다.
2.  **H2**: `serum_creatinine` (혈중 크레아틴) 수치가 높을수록 신장 기능 저하와 연관되어 사망률이 높을 것이다.
3.  **H3**: `age` (나이)는 다른 모든 변수와 독립적으로 사망 위험을 높이는 주요 요인일 것이다.

---

## 4. 예상 산출물 (Expected Deliverables)
- [ ] **Notebook**: `docs/notebooks/EDA_01_heart_failure_prediction.ipynb` (데이터 분포, 상관관계, 모델 학습 및 해석 포함)
- [ ] **Insight Report**: `docs/reports/REPORT_heart_failure_prediction.md` (임상적 인사이트 및 모델 결과 요약)
