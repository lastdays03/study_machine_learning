# 분석 계획서 (Analysis Plan): Heart Failure Revisit (V3)

**Date**: 2026-01-06
**Analyst**: Antigravity
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 최신 방법론(KNN, XGBoost)과 엄격한 재현(Recall) 중심의 평가를 통해 V1/V2 대비 성능을 얼마나 더 끌어올릴 수 있는가?
- **Utility**:
  - 다양한 알고리즘 비교를 통해 데이터셋에 최적화된 모델 선정.
  - "Top 10 Worst Errors" 분석을 통해 모델이 실패하는 케이스의 패턴 규명.

### Success Metrics (KPI)
*`SKILL.md` Evaluation Metrics Guide 참조*
- [ ] **Primary Metric**: **Recall** (Sensitivity) - 생존 예측(False Negative 방지)에 집중.
- [ ] **Secondary Metrics**: 
    - **F1-Score**: Precision과 Recall의 조화.
    - **ROC-AUC**: Threshold 변화에 따른 성능 안정성.
    - **Precision**: 불필요한 치료 방지(FP 최소화).
    - **Accuracy**: 전체 정확도 (참고용).
    - *Note*: `SKILL.md` 가이드의 모든 분류 지표를 산출하여 모델 간 Trade-off를 분석함.

---

## 2. 방법론 (Methodology Screening)

`SKILL.md` Update 반영 (New Candidates Identified)

| Process        | Candidates                    | Reason                                                                          |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------ |
| **Imputation** | Median                        | Outlier 강건성 유지.                                                            |
| **Scaling**    | **Standard Scaler**           | **KNN**은 거리 기반 알고리즘이므로 스케일링이 필수적임.                         |
| **Model 1**    | **XGBoost**                   | (New) 강력한 Gradient Boosting 성능 확인.                                       |
| **Model 2**    | **K-Nearest Neighbors (KNN)** | (New) 데이터 크기(299건)가 작으므로 Instance-based Learning이 효과적일 수 있음. |
| **Validation** | Stratified K-Fold             | 클래스 불균형 유지.                                                             |

---

## 3. 검증 가설 (Hypothesis)
1.  **H1 (Model)**: 데이터가 소규모이므로 복잡한 XGBoost보다 단순한 KNN이나 Random Forest가 더 안정적인 성능을 보일 수 있다.
2.  **H2 (Feature)**: `time` 변수가 오해의 소지가 있어 **제외하되**, KNN은 다차원 공간에서의 "유사한 환자"를 찾으므로 `age`, `ejection_fraction`의 조합이 중요할 것이다.
3.  **H3 (Error)**: 모델이 틀리는 케이스는 `ejection_fraction`은 정상인데 사망했거나, 그 반대의 경우일 것이다.

---

## 4. 예상 산출물 (Deliverables)
- [ ] **Notebook**: `docs/notebooks/EDA_03_heart_failure_revisit.ipynb`
    - KNN (k-Finding), XGBoost (Tuning) 구현.
    - Error Analysis (Top 10 Worst Cases).
- [ ] **Comparative Report**: V1(Logistic/RF) vs V2(Tuned RF) vs V3(KNN/XGB)

---

## 5. 데이터 개요
- **File**: `data/heart_failure_clinical_records_dataset.csv`
- **Target**: `DEATH_EVENT`
