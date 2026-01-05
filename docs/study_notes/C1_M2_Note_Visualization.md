# 2주차 Session 3: 데이터 시각화 (Visualization)

> **목표**: 숫자로만 보면 알 수 없는 데이터의 패턴과 인사이트를 **시각화(Graph)**를 통해 발견합니다.

## 1. Matplotlib vs Seaborn
*   **Matplotlib**: 파이썬 시각화의 조상. 자유도가 높지만 코드가 길어질 수 있습니다.
*   **Seaborn**: Matplotlib 기반의 고수준 라이브러리. 사용이 쉽고 스타일이 예쁩니다. 주로 통계적 그래프에 강점이 있습니다.

---

## 2. 주요 그래프 종류 (Chart Types)

### 1) 산점도 (Scatter Plot)
*   **용도**: 두 변수 간의 **상관관계**를 볼 때 사용합니다.
*   **예시**: 키와 몸무게의 관계, 공부 시간과 성적의 관계.
```python
sns.scatterplot(x='Age', y='Fare', data=df)
```

### 2) 히스토그램 (Histogram)
*   **용도**: 변수 하나의 **분포**를 볼 때 사용합니다.
*   **예시**: 승객들의 나이 분포 (어느 나이대가 가장 많은가?)
```python
sns.histplot(x='Age', data=df)
```

### 3) 막대 그래프 (Bar Chart)
*   **용도**: 범주형 데이터(Category)의 **크기 비교**를 할 때 사용합니다.
*   **예시**: 성별 생존율 비교, 선실 등급별 요금 평균.
```python
sns.barplot(x='Sex', y='Survived', data=df)
```

### 4) 박스 플롯 (Box Plot)
*   **용도**: 데이터의 **분포**와 **이상치(Outlier)**를 한눈에 볼 때 사용합니다.
*   **구조**: 박스 가운데 선은 중앙값, 위아래는 상위/하위 25% 구간, 점들은 이상치.

---

## 3. 실습: 시각화로 데이터 뜯어보기

`notebooks/05_visualization.ipynb`를 생성하고 아래 코드를 실행해 보세요.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 예제 데이터 로드 (Seaborn 내장 타이타닉 데이터)
df = sns.load_dataset('titanic')

# 한글 폰트 설정 (Mac의 경우 AppleGothic)
plt.rcParams['font.family'] = 'AppleGothic'
plt.figure(figsize=(10, 6))

# 2. 산점도: 나이와 요금의 관계, 그리고 생존 여부 색상 표시
plt.subplot(2, 2, 1)
sns.scatterplot(x='age', y='fare', hue='survived', data=df)
plt.title('Age vs Fare (Survival)')

# 3. 히스토그램: 나이 분포
plt.subplot(2, 2, 2)
sns.histplot(df['age'].dropna(), kde=True) # kde: 밀도 곡선 추가
plt.title('Age Distribution')

# 4. 막대 그래프: 선실 등급별 생존율
plt.subplot(2, 2, 3)
sns.barplot(x='class', y='survived', data=df)
plt.title('Survival Rate by Class')

# 5. 박스 플롯: 선실 등급별 요금 분포 (이상치 확인)
plt.subplot(2, 2, 4)
sns.boxplot(x='class', y='fare', data=df)
plt.title('Fare Distribution by Class')

plt.tight_layout()
plt.show()
```

---

## 📝 Practice Challenge
1.  **박스 플롯 해석**: 'First' Class(1등석)의 요금 분포에 이상치(점)가 많나요? 이것은 무엇을 의미할까요?
2.  **그래프 변경**: `scatterplot` 대신 `regplot`을 사용하면 무엇이 달라지나요?
3.  직접 다른 컬럼(`n_siblings` 등)을 사용하여 관계를 시각화해 보세요.
