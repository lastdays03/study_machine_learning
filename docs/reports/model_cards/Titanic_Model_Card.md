# Model Card: Titanic Survival Predictor

## Model Details
- **Name**: Titanic Survival Predictor
- **Version**: 1.0 (2026-01-05)
- **Type**: Random Forest Classifier
- **Dev**: [User Name]
- **Framework**: Scikit-Learn

## Intended Use
- **Primary Use**: 머신러닝 입문 교육용 실습 모델. 1912년 타이타닉 호 승객 데이터를 기반으로 생존 확률을 예측.
- **Out of Scope**: 실제 해상 사고의 생존자 예측 시스템으로 사용 불가.

## Factors & Metrics
- **Factors (Features)**:
    - `Sex` (성별): 가장 강력한 예측 변수.
    - `Pclass` (객실 등급): 사회경제적 지위 반영.
    - `Age` (나이): 어린이/노약자 구분.
- **Metrics**:
    - Accuracy: 0.86 (Test Set)
    - ROC-AUC: 0.89
    - Recall: ~0.76 (생존자 식별 능력)

## Ethical Considerations (Bias & Fairness)
1.  **Historical Bias (역사적 편향)**:
    - 모델은 "여성과 어린이를 먼저(Women and children first)"라는 당시의 구조 프로토콜을 그대로 학습했습니다. 결과적으로 `Sex=Female`일 때 생존 확률이 비약적으로 상승합니다. 이는 데이터가 그 당시 사회상을 정확히 반영한 것이지만, 현대의 관점에서는 '성별에 따른 차별'로 보일 수 있습니다.
2.  **Socio-economic Bias (사회경제적 편향)**:
    - 1등석(`Pclass=1`) 승객의 생존율이 3등석보다 훨씬 높습니다. 이 모델은 부유한 승객을 더 생존 가능성이 높은 그룹으로 분류합니다.

## Quantitative Analysis
- **Group Fairness**:
    - Female Accuracy > Male Accuracy 경향이 있음.
    - False Negative Rate는 남성 그룹에서 더 높게 나타날 가능성 있음 (남성이나 구조받지 못한 케이스).
