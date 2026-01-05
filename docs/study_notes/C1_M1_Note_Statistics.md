# 1주차 Session 3: 기초 수학 리터러시 (통계와 확률)

> **목표**: 머신러닝 데이터 분석의 기초가 되는 **기술 통계**와 **확률 분포**의 개념을 확실히 잡습니다.

## 1. 기술 통계 (Descriptive Statistics)
데이터를 요약하고 설명하는 숫자들입니다.

### 1) 대표값 (Central Tendency)
데이터의 **중심**이 어디인지 나타냅니다.
*   **평균 (Mean, $\mu$)**: 모든 값을 더해서 개수로 나눈 값. (이상치에 민감함)
*   **중앙값 (Median)**: 데이터를 크기순으로 줄 세웠을 때 정중앙에 있는 값. (이상치에 덜 민감함)

### 2) 산포도 (Dispersion)
데이터가 **얼마나 퍼져 있는지** 나타냅니다.
*   **분산 (Variance, $\sigma^2$)**: 편차(데이터 - 평균)의 제곱의 평균.
*   **표준편차 (Standard Deviation, $\sigma$)**: 분산에 루트를 씌운 값. 원래 데이터와 단위가 같아서 직관적입니다.
    *   *표준편차가 크다 = 데이터가 넓게 퍼져 있다.*
    *   *표준편차가 작다 = 데이터가 평균 근처에 모여 있다.*

---

## 2. 확률 분포 (Probability Distribution)

### 1) 정규 분포 (Normal Distribution / Gaussian Distribution)
*   **형태**: 종 모양(Bell Curve)의 대칭 분포입니다.
*   **특징**: 자연계의 많은 현상(키, 시험 점수, 오차 등)이 이 분포를 따릅니다.
*   **중요성**: 많은 머신러닝 알고리즘이 데이터가 정규 분포를 따른다고 가정하고 설계되었습니다.
*   **표준 정규 분포**: 평균이 0이고 표준편차가 1인 정규 분포입니다.

### 2) 확률 (Probability) vs 가능도 (Likelihood)
(심화 개념이지만 간단히만 알아둡시다)
*   **확률**: 분포가 고정되어 있을 때, 특정 데이터가 나올 가능성. (미래 예측)
*   **가능도**: 데이터가 관측되었을 때, 이 데이터가 어떤 분포에서 왔을지 추정하는 것. (원인 추론 - 머신러닝 학습의 핵심 원리)

---

## 3. Python 실습 (Numpy & Matplotlib)

아래 코드를 `notebooks` 폴더에 새 노트북(`02_statistics_basics.ipynb`)을 만들어 직접 작성하고 실행해 보세요.

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터 생성 (평균 0, 표준편차 1인 난수 1000개)
data = np.random.normal(loc=0, scale=1, size=1000)

# 2. 통계량 계산
print(f"평균(Mean): {np.mean(data):.4f}")
print(f"표준편차(Std): {np.std(data):.4f}")
print(f"중앙값(Median): {np.median(data):.4f}")

# 3. 시각화 (히스토그램)
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title("Normal Distribution (Mean=0, Std=1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

---

## 📝 Practice Challenge
위 실습 코드를 실행했을 때,
1.  평균은 정확히 0이 나오나요? 아니라면 왜 그럴까요?
2.  데이터 개수(`size`)를 1000개에서 10개로 줄이면 그래프 모양과 통계량이 어떻게 변하나요?
3.  직접 실험해보고 결과를 노트북에 Markdown으로 적어보세요.
