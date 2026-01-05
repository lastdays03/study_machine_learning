# 3주차 Session 2: 사이킷런으로 모델 만들기 (Practice)

> **목표**: 파이썬 머신러닝의 표준 라이브러리인 **Scikit-learn**을 사용하여 실제로 데이터를 학습시키고 예측하는 전체 파이프라인(Pipeline)을 경험합니다.

## 1. Scikit-learn 워크플로우
머신러닝 코드는 대부분 아래의 4단계 정형화된 패턴을 따릅니다.

1.  **데이터 준비 (Data split)**: 공부할 데이터(Train)와 시험 칠 데이터(Test) 나누기.
2.  **모델 생성 (Create model)**: 어떤 알고리즘을 쓸지 정하기 (여기선 Linear Regression).
3.  **학습 (Fit)**: `model.fit(문제, 정답)` 실행.
4.  **평가/예측 (Predict/Score)**: `model.predict(새로운문제)` 로 값 예측하기.

---

## 2. 핵심 함수 (API)
### 1) 데이터 나누기
```python
from sklearn.model_selection import train_test_split

# 독립변수(X)와 종속변수(y)를 8:2 비율로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
*   `random_state`: 랜덤 시드값. 이 값을 고정해야 매번 똑같은 결과가 나옵니다.

### 2) 모델 학습 및 예측
```python
from sklearn.linear_model import LinearRegression

# 모델 생성
model = LinearRegression()

# 학습 (Training)
model.fit(X_train, y_train)

# 예측 (Prediction)
predictions = model.predict(X_test)
```

### 3) 학습 결과 확인
선형 회귀 모델이 찾은 **직선의 방정식 ($H(x) = Wx + b$)**을 확인해 봅니다.
```python
print(model.coef_)      # 기울기(W, Weight)
print(model.intercept_) # 절편(b, Bias)
```

---

## 3. 실습: 당뇨병 데이터로 수치 예측하기

`notebooks/06_regression_concept.ipynb` (이전에 안 만들었다면 생성) 또는 `07_sklearn_basics.ipynb`를 생성하여 아래 코드를 실행해 보세요.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 로드 (사이킷런 내장 데이터)
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 2. 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 4. 예측 및 평가
y_pred = model.predict(X_test)

# 평가 지표: MSE(오차 제곱 평균)와 R2 Score(설명력, 1에 가까울수록 좋음)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 5. 시각화 (실제값 vs 예측값)
plt.scatter(y_test, y_pred)
plt.plot([0, 350], [0, 350], 'r--') # 정답 직선
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
```

---

## 📝 Practice Challenge
1.  **시각화 해석**: 위 그래프에서 점들이 붉은 점선(정답) 위에 정확히 찍히면 완벽한 예측입니다. 현재 모델의 성능은 어떤가요? 많이 퍼져 있나요?
2.  **데이터 변경**: `diabetes` 대신 `load_linnerud()` 데이터를 사용하여 멀티 아웃풋 회귀도 가능한지 실험해 보거나, 인터넷에서 csv를 받아 실습해 보세요.
