# Study Note: Unsupervised Learning (Clustering & PCA)

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M1_Plan_Advanced_ML.md](../plans/C2_M1_Plan_Advanced_ML.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 비지도 학습 (Unsupervised Learning)의 본질
**정의**: 정답(Label)이 주어지지 않은 상태에서 데이터가 가진 내재적인 구조(Structure)와 패턴(Pattern)을 찾아내는 학습 방법론입니다.

*   **Clustering (군집화)**: 비슷한 개체끼리 그룹핑. (예: 고객 세그먼테이션)
*   **Dimensionality Reduction (차원 축소)**: 데이터의 복잡성을 줄이면서 정보 손실을 최소화. (예: 시각화, 노이즈 제거)

### 1.2 K-Means Clustering
*   **알고리즘 메커니즘**:
    1.  **초기화**: K개의 중심점(Centroid)을 임의로 선정합니다.
    2.  **할당 (Assignment)**: 모든 데이터를 가장 가까운 중심점에 소속시킵니다. (거리 측정: 유클리디안 거리 등)
    3.  **업데이트 (Update)**: 각 그룹의 평균 좌표로 중심점을 이동시킵니다.
    4.  **반복**: 중심점이 더 이상 움직이지 않을 때까지 2~3 과정을 반복합니다.
*   **한계점**:
    *   **구형 군집 가정**: 데이터가 원형으로 퍼져있을 때만 잘 작동합니다. (달모양, 길게 늘어진 모양 등에는 부적합 -> DBSCAN 사용)
    *   **K값 결정**: 몇 개의 그룹으로 나눌지 미리 정해야 합니다. (Elbow Method 사용)

### 1.3 PCA (Principal Component Analysis)
*   **수학적 직관**: 데이터의 **분산(Variance)**을 가장 잘 보존하는 새로운 축(Axis)을 찾는 과정입니다.
    *   분산이 크다는 것은 정보량이 많다는 뜻입니다. (모든 데이터가 한 점에 모여있으면 분산=0, 정보=0)
*   **Eigenvector (고유벡터)**: 데이터가 퍼져있는 방향.
*   **Eigenvalue (고유값)**: 그 방향으로의 분산 크기 (설명력).

## 2. 🧪 Experiment & Insight
*   **Notebook**: `C2_M1_Exp_Unsupervised.ipynb`
*   **Insight**:
    *   PCA로 2차원으로 축소하여 시각화했을 때, 군집들이 서로 겹치지 않고 잘 분리되어 보여야 좋은 군집화입니다.
    *   StandardScaler로 스케일링을 하지 않으면, 값의 단위가 큰 Feature(예: 연봉)가 결과를 지배해버립니다.

## 3. 🔨 Break & Fix Log
*   **Break**: 이상치(Outlier)를 하나 추가하고 K-Means 돌리기.
*   **Result**: 중심점 하나가 이상치 쪽으로 확 끌려감.
*   **Insight**: K-Means는 평균을 사용하므로 이상치에 매우 민감하다. 전처리 단계에서 이상치 제거가 필수적이다.
