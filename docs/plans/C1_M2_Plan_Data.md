# STUDY: 2주차 - 데이터 핸들링 및 시각화

> **Topic**: Python 데이터 분석 필수 라이브러리(Pandas, Numpy)와 시각화 도구(Matplotlib, Seaborn) 마스터
> **Date**: 2025-12-30 ~ 
> **Status**: Planning

## 🎯 Goal
1.  **Numpy**와 **Pandas**를 사용하여 정형 데이터를 능숙하게 로드하고 조작할 수 있다.
2.  결측치 처리, 데이터 필터링 등 머신러닝 학습 전단계인 **전처리(Pre-processing)** 과정을 실습한다.
3.  **Matplotlib**과 **Seaborn**을 활용하여 데이터의 분포와 상관관계를 시각적으로 분석(EDA)할 수 있다.

## 📚 Curriculum

### Session 1: 데이터 핸들링 기초 (Numpy & Pandas) (Theory & Practice)
*   **Key Concepts**:
    *   **Numpy**: Array(배열)의 이해, 차원(Dimension), 브로드캐스팅.
    *   **Pandas**: DataFrame과 Series 구조, CSV 파일 읽기/쓰기(`read_csv`).
*   **Actions**:
    *   `dataset`을 로드하여 상위 5개 행(`head()`), 통계 정보(`describe()`) 확인하기.
    *   특정 열(Column) 또는 행(Row) 선택 및 슬라이싱 실습.

### Session 2: 데이터 전처리 (Pre-processing) (Practice)
*   **Key Concepts**:
    *   **결측치(Missing Value)**: `NaN` 확인(`isnull`) 및 처리(삭제 `dropna` vs 채우기 `fillna`).
    *   **이상치(Outlier)**: 통계적 범위를 벗어난 값 식별.
    *   **데이터 필터링**: 조건에 맞는 데이터만 추출하기 (예: `age > 30`).
*   **Actions**:
    *   타이타닉 데이터셋 등을 활용하여 결측치를 찾고 평균값으로 채우는 실습.

### Session 3: 데이터 시각화 (Visualization) (Practice)
*   **Key Concepts**:
    *   **Matplotlib**: 기본 그래프(Line, Scatter, Bar) 그리기, 축/제목 설정.
    *   **Seaborn**: 통계적 시각화(Boxplot, Heatmap, Pairplot) 및 스타일링.
*   **Actions**:
    *   두 변수 간의 관계(상관관계)를 산점도(Scatter Plot)로 그리기.
    *   데이터의 분포를 히스토그램(Histogram)과 박스 플롯(Boxplot)으로 시각화하여 이상치 눈으로 확인하기.

## 🧪 Quiz / Challenge
1.  **Quiz**: Pandas DataFrame에서 결측치가 있는 행을 모두 제거하는 함수는 무엇인가요?
2.  **Challenge**:
    *   임의의 CSV 파일을 생성(또는 로드)합니다.
    *   'Age' 컬럼의 결측치를 평균 나이로 채웁니다.
    *   'Gender'별 평균 'Income'을 막대 그래프(Bar Chart)로 시각화하는 코드를 작성하고 결과를 보여주세요.
