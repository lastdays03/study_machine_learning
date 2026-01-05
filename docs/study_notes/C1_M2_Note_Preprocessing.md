# 2주차 Session 2: 데이터 전처리 (Data Preprocessing)

> **목표**: 지저분한 현실 데이터(Dirty Data)를 분석 가능한 깨끗한 형태(Clean Data)로 만드는 방법을 익힙니다. **"Garbage In, Garbage Out"**을 기억하세요.

## 1. 결측치 (Missing Values) 처리
데이터에 값이 비어있는 경우입니다. Python에서는 `NaN` (Not a Number) 또는 `None`으로 표시됩니다.

### 1) 확인하기
```python
import pandas as pd
import numpy as np

# 결측치 확인
print(df.isnull().sum())  # 각 컬럼별 결측치 개수 출력
```

### 2) 처리 방법
상황에 따라 전략이 다릅니다.
*   **삭제 (Dropping)**: 데이터가 충분히 많거나, 결측치가 너무 많은 행/열일 때.
    ```python
    df.dropna()          # 결측치가 하나라도 있는 행 제거
    df.dropna(axis=1)    # 결측치가 있는 열 제거
    ```
*   **채우기 (Imputation)**: 데이터를 버리기 아까울 때. (평균, 중앙값, 최빈값, 혹은 0으로 대체)
    ```python
    df.fillna(0)                    # 0으로 채우기
    df['Age'].fillna(df['Age'].mean()) # 'Age' 평균값으로 채우기
    ```

---

## 2. 데이터 필터링 (Conditioning)
원하는 데이터만 쏙쏙 뽑아내는 기술입니다.

### 1) Boolean Indexing
```python
# 'Age'가 30 이상인 데이터만 추출
over_30 = df[df['Age'] >= 30]

# 조건이 여러 개일 때: 'Age'가 30 이상이면서(&) 'Sex'가 'male'인 경우
target = df[(df['Age'] >= 30) & (df['Sex'] == 'male')]
```

### 2) 이상치 (Outlier) 제거
말도 안 되게 크거나 작은 값은 분석을 방해하므로 제거해야 합니다. (예: 나이가 200살)
```python
# 나이가 100살 이하인 데이터만 남기기
df = df[df['Age'] <= 100]
```

---

## 3. 실습: 타이타닉 생존자 데이터 맛보기

`notebooks/04_data_preprocessing.ipynb`를 생성하고 아래 예제를 실습해보세요.

```python
import pandas as pd
import numpy as np

# 가상의 타이타닉 데이터 생성
data = {
    'Name': ['Jack', 'Rose', 'John', 'Doe'],
    'Age': [20, 17, np.nan, 150],  # 결측치(NaN)와 이상치(150) 존재
    'Fare': [7.25, 71.28, 8.05, np.nan] # 결측치 존재
}
df = pd.DataFrame(data)

print("--- 원본 데이터 ---")
print(df)

# 1. 결측치 처리: 'Age'는 평균으로, 'Fare'는 0으로
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Fare'] = df['Fare'].fillna(0)

# 2. 이상치 처리: 나이가 100살 넘는 사람은 제외
df = df[df['Age'] <= 100]

print("\n--- 전처리 후 데이터 ---")
print(df)
```

---

## 📝 Practice Challenge
위 코드를 실행해보고 결과를 확인하세요.
1.  `John`의 나이가 몇 살로 채워졌나요? (평균값 계산 원리 확인)
2.  `Doe` 데이터가 사라졌나요?
3.  만약 `dropna()`를 썼다면 어떤 결과가 나왔을지 코드를 바꿔서 실행해보세요.
