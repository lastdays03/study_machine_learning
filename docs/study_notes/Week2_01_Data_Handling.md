# 2주차 Session 1: 데이터 핸들링 기초 (Numpy & Pandas)

> **목표**: Python 데이터 분석의 핵심인 **Numpy**의 배열 구조와 **Pandas**의 DataFrame을 이해하고, 데이터를 자유자재로 다루는 기초 체력을 기릅니다.

## 1. Numpy (Numerical Python)
수치 계산을 효율적으로 하기 위한 라이브러리입니다. 핵심은 **ndarray** (N-dimensional Array)입니다.

### 1) 왜 리스트(List) 대신 Numpy를 쓰나요?
*   **속도**: C언어로 구현되어 있어 파이썬 리스트보다 훨씬 빠릅니다.
*   **메모리**: 적은 메모리를 사용합니다.
*   **편의성**: 행렬 연산, 브로드캐스팅 등 수학적 계산이 쉽습니다.

### 2) 핵심 실습
```python
import numpy as np

# 리스트를 배열로 변환
arr = np.array([1, 2, 3, 4, 5])

# 벡터 연산 (반복문 없이 한 번에 계산)
print(arr * 2)  # [2, 4, 6, 8, 10]

# 2차원 배열 (행렬)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)  # (2, 3) -> 2행 3열
```

---

## 2. Pandas (Python Data Analysis)
엑셀(Excel)과 유사한 **표(Table)** 형태의 데이터를 다루는 도구입니다.

### 1) 핵심 구조
*   **DataFrame (데이터프레임)**: 2차원 표 데이터 (엑셀 시트 전체). 행(Index)과 열(Columns)로 구성됨.
*   **Series (시리즈)**: 1차원 데이터 (엑셀의 한 열).

### 2) 데이터 로드 및 확인
가장 많이 쓰는 기능입니다.

```python
import pandas as pd

# CSV 파일 읽기 (없으면 에러나므로 실습 시 파일 경로 주의)
# df = pd.read_csv('data.csv')

# 데이터 직접 생성 (실습용)
data = {
    'Name': ['Iron Man', 'Captain', 'Thor', 'Hulk'],
    'Age': [48, 100, 1500, 49],
    'Team': ['Tech', 'Leader', 'God', 'Power']
}
df = pd.DataFrame(data)

# 데이터 확인
print(df.head(2))        # 상위 2개 행 출력
print(df.info())         # 데이터 타입 및 결측치 확인
print(df.describe())     # 수치형 데이터 통계 요약 (평균, 최소, 최대 등)
```

### 3) 데이터 선택 (Indexing & Slicing)
*   **열 선택**: `df['Name']`
*   **행 선택 (조건)**: `df[df['Age'] > 50]` (50세 이상만 필터링)
*   **위치 기반 선택**: `df.iloc[0]` (첫 번째 행)

---

## 📝 Practice Code
`notebooks/03_data_handling_basics.ipynb`를 생성하여 다음 미션을 수행하세요.

1.  **Numpy**: 1부터 10까지의 숫자가 들어있는 배열을 만들고, 모든 숫자에 10을 더해서 출력하세요.
2.  **Pandas**:
    *   위의 '어벤져스' 데이터를 DataFrame으로 만드세요.
    *   'Age'가 100살 이상인 영웅만 뽑아서 출력하세요.
    *   'Power'라는 새로운 열(Column)을 추가하고, 모든 값을 100으로 설정하세요.
