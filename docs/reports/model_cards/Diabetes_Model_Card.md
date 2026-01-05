# Model Card: Diabetes Risk Assessment Model

## Model Details
- **Developed by**: Study Machine Learning Project Team
- **Model Type**: Random Forest Classifier (Scikit-learn)
- **Version**: 1.0
- **License**: Apache 2.0 (Assumption)
- **Algorithm**: Ensemble Learning (Bagging) based on Decision Trees.
- **Parameters**: `n_estimators=100`, `max_depth=8`, `min_samples_leaf=12` (Optimized via GridSearchCV).

## Intended Use
- **Primary Use**: Pima Indians Diabetes 데이터셋을 기반으로 환자의 당뇨병 발병 여부(Outcome)를 예측.
- **Goal**: 조기 진단을 위한 보조 도구로써, 발병 위험인자를 식별하고 의료 전문가의 판단을 지원.
- **Target Users**: 의료 연구자, 데이터 분석가, 1차 진료 의사.
- **Out of Scope**: 이 모델 하나만으로 임상적 확진을 내리는 것은 불가능하며, 반드시 의사의 진단이 필요함.

## Factors (Risk Drivers)
이 모델은 다음 변수들에 의해 주로 영향을 받습니다 (Feature Importance 순):
1.  **Glucose**: 혈당 수치 (가장 강력한 예측 인자).
2.  **BMI**: 체질량 지수 (비만도).
3.  **Age**: 연령.
4.  **Pregnancies**: 임신 횟수.

## Metrics (Performance)
- **Evaluation Data**: 20% Hold-out Test Set (Stratified Split)
- **Accuracy**: 0.7727 (77.3%)
- **Recall (Sensitivity)**: 0.6111 (61.1%) - *실제 환자를 찾는 비율이 다소 낮아 개선 필요.*
- **ROC-AUC**: 0.8593 - *전반적인 모델의 변별력은 우수함.*

> **Analysis**: ROC-AUC가 0.86으로 준수하지만, 의료 도구로 쓰기엔 Recall(0.61)이 낮습니다. 실제 환자를 놓칠 위험(False Negative)을 줄이기 위해 Threshold 조정이 필요합니다.

## Ethical Considerations [User Review Required]
- **Dataset Bias**: Pima Indians 여성만을 대상으로 한 데이터셋이므로, 남성이나 다른 인종에게는 일반화하기 어렵습니다.
- **Privacy**: 의료 데이터 특성상 개인 식별 정보(PII)가 포함되지 않도록 주의해야 합니다. (본 데이터셋은 익명화됨)
- **Automation Bias**: 모델의 예측 결과를 맹신하여 실제 증상을 간과하는 오류를 범해선 안 됩니다.

## Caveats & Recommendations
- **Recall Optimization**: Recall을 0.75 이상으로 높이기 위해 Classification Threshold를 낮추는 후처리(Post-processing)를 권장합니다.
- **Data Augmentation**: 더 다양한 연령대와 인종의 데이터를 확보하여 모델의 포용성을 높여야 합니다.
