# 학습 계획서 (Study Plan): Course 2 Module 1 - Advanced ML & Data Quality (Deep Mastery)

**Status**: 🔄 In Progress
**Started**: 2026-01-05
**Goal**: 머신러닝의 고급 기법(앙상블, 비지도 학습, 추천 시스템)을 마스터하고, 현업 수준의 데이터 품질 관리 역량을 갖춘다.

---

## 🎯 핵심 목표 (Deep Objective)
**"Beyond Accuracy: Utility & Quality"**
- [ ] What: 앙상블(GBM 등), 비지도 학습(K-Means, PCA), 추천 시스템, 그리고 데이터 품질 관리.
- [ ] Why: 단순 예측을 넘어 '숨겨진 패턴'을 찾고, '신뢰할 수 있는 데이터'를 다루기 위함.
- [ ] How: [Scikit-learn 공식 문서, Kaggle Advanced Tutorials, NIA 데이터 품질 가이드라인]

---

## 📅 커리큘럼 (Curriculum)

### Session 1: 앙상블 기법 심화 (Ensemble Mastery)
**Focus**: Random Forest vs Boosting (XGBoost/LightGBM)

#### ✅ 심층 마스터 체크리스트 (Deep Mastery Checklist)
1.  **Theory (Feynman Test)**
    - [x] Bagging과 Boosting의 결정적 차이 이해 (Variance vs Bias 감소)
    - [x] **Feynman Summary**: "숲(Forest)과 릴레이 경주(Boosting)" 비유로 설명 작성.
2.  **Practice (Break & Fix)**
    - [x] XGBoost 하이퍼파라미터 과적합 실험 (learning_rate, max_depth 조절)
    - [x] **Log**: 파라미터 변화에 따른 Train/Test Loss 격차 기록.
3.  **Implementation (Output)**
    - [x] `notebooks/EXP_01_Ensemble_Comparison.ipynb` 생성 및 구현.

### Session 2: 비지도 학습과 이상 탐지 (Unsupervised & Anomaly)
**Focus**: K-Means, PCA, Isolation Forest

#### ✅ 심층 마스터 체크리스트 (Deep Mastery Checklist)
1.  **Theory (Feynman Test)**
    - [ ] 차원 축소의 필요성 (Curse of Dimensionality) 설명.
    - [ ] **Feynman Summary**: "사진 압축" 비유로 PCA 설명.
2.  **Practice (Break & Fix)**
    - [ ] K-Means의 K값 변경에 따른 실루엣 점수 변화 실험.
    - [ ] **Log**: 잘못된 K값이 군집 품질에 미치는 영향 기록.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M1_Exp_Unsupervised.ipynb` 생성 (고객 세그먼테이션 시나리오).

### Session 3: 추천 시스템 입문 (Recommender System Basic)
**Focus**: Collaborative Filtering (User-based vs Item-based)

#### ✅ 심층 마스터 체크리스트 (Deep Mastery Checklist)
1.  **Theory (Feynman Test)**
    - [ ] 협업 필터링의 희소성(Sparsity) 문제 이해.
    - [ ] **Feynman Summary**: "나와 비슷한 친구가 좋아하는 영화" 비유.
2.  **Practice (Break & Fix)**
    - [ ] Matrix Factorization 구현 및 Cold Start 문제 재현.
    - [ ] **Log**: 신규 유저에게 추천이 안 되는 현상 분석.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M1_Exp_Recommender.ipynb` 생성 (MovieLens 데이터셋 활용).

### Session 4: 데이터 품질 관리 (Data Quality Engineering)
**Focus**: NIA 가이드라인, 편향성 제거

#### ✅ 심층 마스터 체크리스트 (Deep Mastery Checklist)
1.  **Theory (Feynman Test)**
    - [ ] 데이터 품질의 6대 원칙(완전성, 유효성 등) 이해.
2.  **Practice (Break & Fix)**
    - [ ] 의도적인 노이즈/결측치 주입 후 모델 성능 하락 검증.
3.  **Implementation (Output)**
    - [ ] `docs/reports/Data_Quality_Checklist.md` 작성.

---

## 📝 학습 로그 (Learning Log / Notes)
*Feynman 요약과 아하 모먼트(Aha moment)를 기록하세요.*

### Session 1 Notes (Ensemble)
### Session 1 Notes (Ensemble)
- 📄 **Detail Note**: [C2_M1_Note_Ensemble.md](../study_notes/C2_M1_Note_Ensemble.md)
- **Feynman Summary**:
    - **Bagging (Random Forest)**: "다수결의 원칙". 여러 그루의 나무(Decision Tree)를 서로 다르게 키워서(Bootstrap), 투표를 통해 결론을 내린다. 개별 나무는 실수를 할 수 있지만, 숲 전체적으로는 안정적이다. (Variance 감소)
    - **Boosting (XGBoost/LightGBM)**: "오답 노트 이어달리기". 첫 번째 모델이 틀린 문제(Residual)를 두 번째 모델이 집중적으로 공부하고, 또 틀린건 세 번째가 공부한다. 뒤로 갈수록 어려운 문제에 강해진다. (Bias 감소)

### 🔨 트러블슈팅 로그 (Break Log)
...

### Session 2 Notes (Unsupervised)
- 📄 **Detail Note**: [C2_M1_Note_Unsupervised.md](../study_notes/C2_M1_Note_Unsupervised.md)

### Session 3 Notes (Recommender)
- 📄 **Detail Note**: [C2_M1_Note_Recommender.md](../study_notes/C2_M1_Note_Recommender.md)

### Session 4 Notes (Data Quality)
- 📄 **Detail Note**: [C2_M1_Note_Data_Quality.md](../study_notes/C2_M1_Note_Data_Quality.md)

---

## ✅ 회고 (Retrospective)
*모든 세션 완료 후 작성*
