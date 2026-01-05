# STUDY: 3주차 - 지도 학습 기초 (회귀)

> **Topic**: 데이터의 **관계**를 찾고 **미래의 값**을 예측하는 회귀(Regression) 모델링 기초
> **Date**: 2025-12-30 ~
> **Status**: Planning

## 🎯 Goal
1.  **선형 회귀(Linear Regression)**의 개념(독립변수, 종속변수, 가중치, 편향)을 이해한다.
2.  머신러닝 학습의 핵심 원리인 **손실 함수(Loss Function)**와 **경사하강법(Gradient Descent)**을 시각적으로 이해한다.
3.  **Scikit-learn** 라이브러리를 사용하여 실제로 회귀 모델을 만들고 예측해 본다.

## 📚 Curriculum

### Session 1: 선형 회귀의 원리 (Theory)
*   **Key Concepts**:
    *   **가설(Hypothesis)**: $H(x) = Wx + b$ (직선을 긋는 것).
    *   **비용(Cost/Loss)**: 예측값과 실제값의 차이(MSE).
    *   **경사하강법(Gradient Descent)**: 오차를 줄이기 위해 산을 내려가는 방법.
*   **Activity**:
    *   공부 시간($x$)과 성적($y$) 데이터를 보고 가장 적절한 직선 그려보기.

### Session 2: 사이킷런으로 모델 만들기 (Practice)
*   **Library**: `scikit-learn` (파이썬 머신러닝의 표준).
*   **Actions**:
    *   데이터 분리: `train_test_split` (훈련 데이터와 시험 데이터 나누기).
    *   모델 학습: `model.fit(X_train, y_train)`.
    *   예측 및 평가: `model.predict(X_test)` 및 `mean_squared_error`.

### Session 3: 경사하강법 시각화 (Deep Dive)
*   **Key Concepts**:
    *   Learning Rate(학습률)의 중요성. (너무 크면 발산, 너무 작으면 느림)
*   **Actions**:
    *   간단한 코드로 경사하강법을 직접 구현해보고, $W$(웨이트)값이 변해가는 과정을 그래프로 확인.

## 🧪 Quiz / Challenge
1.  **Quiz**: 선형 회귀에서 학습(Training)이란 결국 $W$(기울기)와 $b$(절편)를 어떻게 만드는 과정인가요?
2.  **Challenge**:
    *   Scikit-learn에서 제공하는 당뇨병(diabetes) 또는 보스턴 집값(california housing) 데이터를 로드합니다.
    *   데이터를 8:2로 나눕니다.
    *   선형 회귀 모델을 학습시키고, 테스트 데이터에 대한 $R^2$ 점수(결정 계수)를 출력하세요.
