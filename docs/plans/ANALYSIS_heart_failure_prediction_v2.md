# 분석 계획서 (Analysis Plan): Heart Failure Prediction V2

**Date**: 2026-01-05
**Analyst**: Antigravity
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)
- **Question**: V1 분석에서 확인된 낮은 Recall(약 0.63)을 극복하고, 실제 사망 위험이 있는 환자를 더 잘 찾아낼 수 있는가?
- **Utility**: 의료 현장에서 '위험 환자'를 놓치는 비용(Type II Error)이 오진 비용(Type I Error)보다 훨씬 큼. 따라서 **Recall(재현율) 극대화**가 필수적임.
- **Success Metrics (KPI)** v2:
    - [ ] **Recall (Sensitivity)**: **0.75 이상** (V1 대비 12%p 향상 목표)
    - [ ] **F1-Score**: 0.75 이상 (Precision의 급격한 하락 방지)

---

## 2. 방법론 (Methodology) - Advanced

### Data Processing Strategy
- **Imbalanced Handling**:
    - **SMOTE (Synthetic Minority Over-sampling Technique)**: 소수 클래스(사망) 데이터를 합성하여 학습 데이터 균형 맞춤.
    - **Class Weight Adjustment**: 모델 학습 시 소수 클래스에 더 높은 가중치 부여.
- **Feature Engineering**:
    - **Binning**: `age`, `platelets` 등 연속형 변수의 구간화(Binning)를 통해 비선형성 포착.
    - **Interaction Features**: `age` * `serum_creatinine` 등 주요 변수 간 곱셉항 추가.

### Model Candidates (Methodology Screening Results)
`SKILL.md` 및 V1 교훈을 반영하여 선정.

1.  **Random Forest (Weighted)**: `class_weight='balanced'` 옵션 적용.
2.  **XGBoost (Tuned)**: `scale_pos_weight` 파라미터 조정으로 불균형 대응.
3.  **LightGBM**: 대용량은 아니지만, Leaf-wise growth 특성상 복잡한 패턴 포착에 유리할 수 있음. (설치된 라이브러리 활용)

### Validation Strategy
- **Stratified K-Fold (k=5)**
- **Threshold Tuning**: 기본 0.5가 아닌, Precision-Recall Curve를 분석하여 최적의 Threshold(`Probability > 0.3` 등) 탐색.

---

## 3. 검증 가설 (Hypothesis to Validate)

1.  **H1 (Re-verify)**: `time` 변수는 생존 편향(Survival Bias) 가능성이 있으므로, 이를 제외한 모델에서도 유의미한 성능이 나오는지 확인 필요하다. (V2에서는 `time` 제외 모델 별도 테스트 고려)
2.  **H2**: SMOTE를 적용하면 Recall은 오르지만 Precision은 다소 떨어질 것이다. 그 Trade-off가 수용 가능한 수준인지 검증한다.

---

## 4. 예상 산출물 (Expected Deliverables)
- [ ] **Notebook**: `docs/notebooks/EDA_02_heart_failure_prediction.ipynb`
- [ ] **Comparative Report**: V1 vs V2 성능 비교 및 최종 제언.
