# 분석 결과 보고서: Heart Failure Prediction

**Date**: 2026-01-05
**Analyst**: Antigravity
**Analysis File**: `docs/notebooks/EDA_01_heart_failure_prediction.ipynb`

## 1. 요약 (Executive Summary)
본 분석은 임상 기록 데이터를 활용하여 심부전증 환자의 사망 여부를 예측하는 모델을 개발하는 것을 목표로 하였습니다.
- **최고 성능 모델**: Random Forest Classifier
- **주요 지표**: Test F1-Score **0.706**, Recall **0.632**
- **결론**: Random Forest 모델이 가장 안정적인 성능을 보였으나, 전체적인 Recall(재현율)이 60%대로 다소 낮아 고위험군 환자 식별에 한계가 있음. 향후 Recall 향상을 위한 Threshold 조정이나 데이터 증강(SMOTE 등)이 필요함.

## 2. 데이터 품질 및 탐색 (Data Quality & EDA)
- **데이터셋**: 299명의 환자 데이터, 13개 Feature.
- **결측치**: 없음 (Clean Dataset).
- **Target Imbalance**: 사망(1)이 약 32%로 불균형 데이터임.
- **주요 상관관계**:
    - `age`와 사망률은 양의 상관관계.
    - `ejection_fraction`(박출계수)과 `serum_sodium`(혈중 나트륨)은 사망률과 음의 상관관계 (수치가 낮을수록 위험).
    - `serum_creatinine`(혈중 크레아틴)은 사망률과 양의 상관관계.

## 3. 모델링 결과 (Modeling Results)
Stratified K-Fold (k=5) 교차 검증 및 Test Set(20%) 평가 결과는 다음과 같습니다.

| Model                   | CV F1 Score (Mean) | Test F1 Score | Test Recall |
| :---------------------- | :----------------- | :------------ | :---------- |
| **Logistic Regression** | 0.7263             | 0.6667        | 0.5789      |
| **Random Forest**       | **0.7648**         | **0.7059**    | **0.6319**  |
| **XGBoost**             | 0.7439             | 0.6452        | 0.5263      |

- **Random Forest**가 교차 검증 및 테스트 셋 모두에서 가장 우수한 성능을 기록했습니다.
- **XGBoost**는 과적합 경향을 보였으며, 복잡한 모델보다 앙상블 트리 기반의 Random Forest가 소규모 데이터셋(N=299)에서 더 강건함을 확인했습니다.

## 4. 모델 해석 및 인사이트 (Interpretation)
Random Forest 모델의 **Feature Importance** 분석 결과, 사망 위험 예측에 가장 크게 기여한 변수는 다음과 같습니다:
1.  **time**: 관찰 기간 (가장 결정적 요인. 관찰 기간이 짧을수록 사망 이벤트 발생과 연관성이 높음, 다만 이는 생존 편향일 수 있어 해석 주의 요망)
2.  **serum_creatinine**: 신장 기능 지표
3.  **ejection_fraction**: 심박출률
4.  **age**: 고령일수록 위험

## 5. 제언 (Recommendations)
1.  **모델 개선**:
    - Recall을 높이기 위해 Classification Threshold를 낮추거나(예: 0.3), SMOTE와 같은 오버샘플링 기법 적용 권장.
2.  **임상적 활용**:
    - `serum_creatinine` 수치가 높고 `ejection_fraction`이 낮은 고령 환자를 **초고위험군**으로 분류하여 집중 모니터링 시스템 구축 제안.
