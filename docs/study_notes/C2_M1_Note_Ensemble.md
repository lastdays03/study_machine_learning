# Study Note: 앙상블 기법 심화 (Ensemble Mastery)

**Module**: Course 2 - Module 1 (Advanced ML)
**Topic**: Bagging vs Boosting
**Related Notebook**: [C2_M1_Exp_Ensemble.ipynb](../../notebooks/course_2/C2_M1_Exp_Ensemble.ipynb)

---

## 1. 🔍 Theory: 숲과 이어달리기

앙상블(Ensemble)은 여러 개의 모델을 조합하여 더 강력한 성능을 내는 기법입니다. 크게 **Bagging**과 **Boosting** 두 가지 방식으로 나뉩니다.

### 1) Bagging (Bootstrap Aggregating)
*   **비유**: "다수결의 원칙", "안정적인 숲(Forest)"
*   **대표 모델**: Random Forest
*   **원리**:
    *   데이터를 중복 허용하여 랜덤하게 샘플링(Bootstrap)합니다.
    *   여러 개의 Decision Tree를 **병렬(Parallel)**로 학습시킵니다.
    *   각 나무들의 예측 결과를 투표(Classification)하거나 평균(Regression)내어 결정합니다.
*   **장점**: **분산(Variance) 감소**. 개별 모델이 과적합되더라도, 합치면 일반화 성능이 좋아집니다.

### 2) Boosting
*   **비유**: "오답 노트", "이어달리기"
*   **대표 모델**: XGBoost, LightGBM, CatBoost
*   **원리**:
    *   모델을 **직렬(Sequential)**로 학습시킵니다.
    *   이전 모델이 틀린 문제(Residual, 오차)에 가중치를 주어 다음 모델이 집중적으로 학습합니다.
    *   점점 더 어려운 문제를 잘 풀게 됩니다.
*   **장점**: **편향(Bias) 감소**. 높은 정확도를 낼 수 있습니다.
*   **단점**: 이상치(Outlier)나 노이즈에 과적합(Overfitting)되기 쉽습니다.

---

## 2. 🧪 Experiment: Random Forest vs XGBoost

`C2_M1_Exp_Ensemble.ipynb`에서 수행한 과적합 실험 결과 요약입니다.

### 실험 설정
*   **Data**: `make_classification`으로 생성한 가상 데이터 (Features=20)
*   **Scenario**:
    *   **Break (XGBoost)**: `max_depth`를 15로 깊게 설정하고, `n_estimators`를 늘림. 학습 데이터에 과도하게 맞춰지는지 확인.
    *   **Fix (Random Forest)**: 동일한 깊이(15)에서 Random Forest는 어떤 양상을 보이는지 비교.

### 주요 발견 (Key Takeaways)
1.  **XGBoost의 과적합**: Boosting 계열은 깊은 트리와 높은 반복 횟수에서 Train Loss는 0에 수렴하지만, Valid Loss는 다시 증가하는(U-Shape) **Overfitting** 현상이 뚜렷하게 나타납니다. -> *Early Stopping이 필수적임.*
2.  **Random Forest의 안정성**: Bagging 방식은 개별 트리가 깊어도(Deep Tree), 서로 다른 데이터로 학습된 나무들을 평균내기 때문에 과적합에 훨씬 강한 모습을 보입니다. -> *하이퍼파라미터 튜닝이 상대적으로 덜 까다로움.*

---

## 3. 📝 Summary & Action Item
*   데이터가 노이즈가 많거나 안정성이 중요하다면 **Random Forest**를 베이스로 시작하세요.
*   최고의 성능(1%의 정확도라도 더)이 필요하다면 **XGBoost/LightGBM**을 쓰되, 반드시 과적합 방지 장치(`max_depth` 제한, `early_stopping`, `reg_alpha` 등)를 함께 사용해야 합니다.
