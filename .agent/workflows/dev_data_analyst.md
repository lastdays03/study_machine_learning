---
description: 데이터 분석의 전 과정(질의 정의 -> EDA -> 심층 분석 -> 리포팅)을 체계적으로 가이드하는 워크플로우입니다.
---

# Data Analyst Workflow

Python 생태계(Jupyter, Pandas, Seaborn)를 활용하여 데이터에서 인사이트를 도출하는 전문 분석 워크플로우입니다. OSEMN 방법론을 따릅니다.

### 1단계: 분석 환경 및 목표 정의 (Environment & Goal)
분석의 **'Business Utility(효용성)'**를 정의하는 단계입니다. "무엇을 분석하는가?"보다 **"왜 분석하며, 성공 기준은 무엇인가?"**가 중요합니다.

1.  **Notebook Setup**: `docs/analysis/` 또는 `notebooks/` 경로에 `EDA_01_[주제].ipynb` 형식으로 생성합니다.
2.  **Define Objective & Success Metrics**:
    *   해결하려는 **비즈니스 질문(Question)**을 구체적으로 적습니다.
    *   단순 정확도(Accuracy) 외에 **실질적 성공 지표(KPI)**를 정의합니다. (예: False Positive를 줄이는 것이 중요한가?)
3.  **Library Loading**: 필수 라이브러리(`pandas`, `seaborn` 등)와 시각화 설정을 로드합니다.

### 2단계: 데이터 적재 및 품질 검증 (Obtain & Scrub)
Garbage In, Garbage Out을 방지하기 위한 **데이터 신뢰성 확보** 단계입니다.

1.  **Data Loading & Profiling**: 데이터를 로드하고 기초 통계량(`describe`) 및 분포를 확인합니다.
2.  **Deep Sanity Check**:
    *   단순 결측치 확인을 넘어, **논리적 오류(Logical Failures)**를 등급별로 체크합니다. (예: 나이가 음수, 가입일보다 탈퇴일이 빠름)
    *   데이터의 **분포 왜곡(Skewness)**이나 **클래스 불균형(Imbalance)**을 사전에 파악합니다.
3.  **Strategic Cleaning**: 데이터 삭제/대체의 기준을 명확히 기록합니다. "왜 이 데이터를 버렸는가?"를 설명할 수 있어야 합니다.

### 3단계: 가설 주도적 탐색 (Hypothesis Driven EDA)
단순 그래프 그리기를 넘어, **가설(Hypothesis)을 입증하거나 기각**하는 과정입니다.

1.  **Ask & Visualize**: 막연한 `pairplot` 대신, **구체적인 질문을 던지고 이를 시각화**합니다. (예: "성별에 따라 생존율에 유의미한 차이가 있는가?")
2.  **Statistical Validation**: 그래프로 본 직관을 **통계적 검정(T-test, Chi-square 등)**으로 뒷받침합니다. "눈대중"으로 결론 내리지 않습니다.
3.  **Insight Logging**: 발견된 사실이 **목표(Goal)에 미치는 영향**을 마크다운으로 즉시 기록합니다.

### 4단계: 머신러닝/딥러닝 모델링 (Model & Optimize)
단순 예측을 넘어 **신뢰할 수 있는 모델**을 구축하는 단계입니다. **철저한 검증(Rigorous Validation)**이 핵심입니다.

1.  **Preprocessing**: 모델링을 위한 인코딩, 스케일링, 파생변수 생성을 수행합니다.
2.  **Rigorous Validation Strategy**:
    *   `train_test_split`의 **Single Split 점수**와 `cross_val_score`의 **CV 평균 점수**를 반드시 비교하여 우연성을 배제합니다.
    *   cv=5 이상의 교차 검증을 **모든 후보 모델(Baseline 포함)**에 수행하여 공정한 비교 환경을 만듭니다.
3.  **Baseline & Comparison**: 단순 모델(Logistic Regression)과 복잡한 모델(RF, XGB)을 비교합니다. 성능 차이가 미미하다면 **해석력(Explainability)**이 높은 모델을 우선합니다.
4.  **Optimization**: 비즈니스 관점에서 중요한 metric(예: Recall이 중요한 암 진단 모델)을 기준으로 튜닝합니다.

### 5단계: 해석 및 리포팅 (Interpret & Report)
분석 결과를 **의사결정(Action)**으로 연결하는 단계입니다. **솔직함(Honesty)**이 효용성을 높입니다.

1.  **Why & How Check**: "이 모델이 왜 이 점수를 냈는가?"를 **모델 안정성(CV 편차)**과 **과적합 여부**로 증명합니다.
2.  **Interpretation & Error Analysis**:
    *   **Feature Importance/SHAP**: 모델이 무엇을 중요하게 봤는지 설명합니다.
    *   **Error Analysis**: 모델이 **틀린 케이스**를 분석하여 개선 포인트를 찾습니다.
3.  **Caveats & Limitations (한계점)**: 데이터의 한계나 모델의 약점을 솔직하게 명시하여 신뢰도를 높입니다.
4.  **Action Item**: 분석 결과를 바탕으로 **구체적인 비즈니스 실행 안**을 제안합니다.
