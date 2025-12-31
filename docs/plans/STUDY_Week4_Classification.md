# STUDY: 4주차 - 지도 학습 (분류)

> **Topic**: 데이터를 범주형 클래스(Class)로 나누는 **분류(Classification)** 알고리즘과 평가 지표 학습
> **Date**: 2025-01-06 ~ (예정)
> **Status**: Planning

## 🎯 Goal
1.  **분류(Classification)**와 회귀(Regression)의 차이를 명확히 이해한다.
2.  대표적인 분류 알고리즘(**로지스틱 회귀, 의사결정나무, 랜덤 포레스트**)의 원리를 파악한다.
3.  단순 정확도(Accuracy)의 함정을 이해하고, **정밀도(Precision), 재현율(Recall), F1-Score** 등 다양한 평가 지표를 활용할 수 있다.

## 📚 Curriculum

### Session 1: 로지스틱 회귀 (Logistic Regression)
*   **Key Concepts**:
    *   Regression인데 왜 분류인가? (Sigmoid 함수의 마법).
    *   임계값(Threshold)에 따른 클래스 결정 (0/1).
    *   이진 분류(Binary) vs 다중 분류(Multi-class).
*   **Activity**:
    *   타이타닉 생존자 예측 맛보기 (간단한 버전).

### Session 1.5: 데이터 전처리 심화 (Preprocessing Deep Dive)
*   **Key Concepts**:
    *   **인코딩(Encoding)**: 문자를 숫자로 (Label Encoding vs One-Hot Encoding).
    *   **스케일링(Scaling)**: 데이터의 단위를 맞추기 (StandardScaler vs MinMaxScaler).
*   **Activity**:
    *   `10_logistic_regression.ipynb`에 스케일링/인코딩 적용하여 성능 변화 확인.

### Session 2: 트리와 앙상블 (Decision Tree & Random Forest)
*   **Key Concepts**:
    *   스무고개와 비슷한 의사결정나무(Decision Tree)의 원리 (Entropy, Gini Index).
    *   과적합(Overfitting) 문제와 가지치기(Pruning).
    *   "집단 지성" 앙상블의 기초: 랜덤 포레스트(Random Forest).
*   **Activity**:
    *   붓꽃(Iris) 데이터 다시보기: 트리 구조 시각화 (`plot_tree`).

### Session 3: 모델 성능 평가 (Evaluation Metrics)
*   **Key Concepts**:
    *   오차 행렬 (Confusion Matrix): TP, TN, FP, FN.
    *   정확도(Accuracy)가 위험한 경우 (불균형 데이터).
    *   정밀도(Precision) vs 재현율(Recall) 트레이드오프.
    *   ROC 곡선과 AUC 점수.
*   **Activity**:
    *   암 환자 예측 가상 시나리오로 지표 해석해보기.

## 🧪 Quiz / Challenge
1.  **Quiz**: 스팸 메일 필터링 시스템에서는 '정밀도'와 '재현율' 중 무엇이 더 중요할까요? (정상 메일을 스팸으로 분류하면 안 됨)
2.  **Challenge**:
    *   **와인 품질(Wine Quality) 데이터셋** (또는 유방암 데이터셋) 로드.
    *   로지스틱 회귀 vs 의사결정나무 모델 성능 비교.
    *   오차 행렬(Confusion Matrix) 출력 및 F1-Score 비교.
