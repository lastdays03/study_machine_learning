# Study Note: Recommender System Basic

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M1_Plan_Advanced_ML.md](../plans/C2_M1_Plan_Advanced_ML.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 추천 시스템의 두 줄기
1.  **Content-based Filtering (콘텐츠 기반)**:
    *   "아이언맨을 본 사용자에게, 비슷한 장르/배우가 나오는 어벤져스를 추천."
    *   아이템의 속성(Attribute) 분석이 중요.
2.  **Collaborative Filtering (협업 필터링)**:
    *   "아이언맨을 본 다른 사용자들이 스파이더맨도 많이 봤으니, 당신에게도 추천."
    *   **집단 지성** 활용. 아이템 속성을 몰라도 됨.

### 1.2 Matrix Factorization (행렬 분해)
*   **개념**: 사용자-아이템 평점 행렬(R)을 두 개의 저차원 행렬(P, Q)의 곱으로 근사(Approximation)하는 기법입니다.
    *   $R pprox P 	imes Q^T$
*   **Latent Factor (잠재 요인)**:
    *   행렬 분해를 통해 찾아낸 P와 Q의 차원들은 명시적인 의미(장르 등)는 없지만, 데이터가 내포한 **취향의 잠재적 특성**을 나타냅니다.
*   **학습 원리**: 실제 평점과 예측 평점($p_u \cdot q_i$)의 오차(RMSE)를 최소화하도록 경사하강법으로 P, Q를 업데이트합니다.

## 2. 🧪 Experiment & Insight
*   **Notebook**: `C2_M1_Exp_Recommender.ipynb`
*   **Insight**:
    *   Sparsity(희소성): 전체 행렬 중 평점이 채워진 건 1%도 안 되는 경우가 많다. 이 희소한 정보만으로 나머지를 추론해야 하는 것이 난제.
    *   Implicit Feedback: 별점(1~5점)보다, 클릭/구매/시청시간 같은 암묵적 피드백이 더 풍부하고 중요하다.

## 3. 🔨 Break & Fix Log
*   **Break**: 모든 유저가 똑같이 5점을 준 아이템 추가.
*   **Result**: 개인화 추천이 안 되고 모두에게 추천됨 (Popluarity bias).
