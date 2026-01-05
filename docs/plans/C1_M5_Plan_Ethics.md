# 학습 계획서 (Study Plan): 5주차 - AI 윤리 및 입문 프로젝트 (Deep Mastery)

**Status**: 🔄 In Progress
**Started**: 2026-01-05
**Goal**: AI 윤리와 편향성 개념을 체득하고, 타이타닉/당뇨병 프로젝트를 통해 모델의 공정성을 검토하며 입문 과정을 최종 마무리한다.

---

## 🎯 핵심 목표 (Deep Objective)
**"Bias Awareness & Project Completion"**
- [ ] **What**: AI 윤리(Ethics), 편향성(Bias), 공정성(Fairness)의 개념과 실제 데이터 분석 프로젝트 마무리.
- [ ] **Why**: 성능만 좋은 모델이 아닌, '올바른' 모델을 만들기 위해. 데이터 수집부터 배포까지 윤리적 관점을 탑재하기 위해.
- [ ] **How**: Kaggle AI Ethics 과정, 타이타닉/당뇨병 노트북 심화 분석.

---

## 📅 커리큘럼 (Curriculum)

### Session 1: AI 윤리와 편향성 (AI Ethics & Bias)
**Focus**: Theory & Concept

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Bias 종류 학습**: Selection Bias, Automation Bias 등 5가지 주요 편향 정의.
    - [ ] **Fairness**: AI가 공정하다는 것은 무엇인가? (Group Fairness vs Individual Fairness)
    - [ ] **Feynman Summary**: "알고리즘이 차별을 한다고?"라는 주제로 비전공자에게 설명하는 글 작성.

2.  **Practice (Break & Fix)**
    - [x] **Break**: 타이타닉 데이터에서 특정 성별이나 클래스(Pclass)를 제거하거나 왜곡하여 편향된 모델 생성 (`notebooks/EXP_Week5_Bias_Experiment.ipynb`).
    - [x] **Fix**: 데이터 불균형을 해소하거나(SMOTE 등), Metric을 변경하여 공정성 확보 시도.
    - [x] **Log**: 편향이 모델 성능(Recall/Precision)에 미친 영향 기록.

### Session 2: 프로젝트 고도화 및 마무리 (Project Finalization)
**Focus**: Implementation (Titanic & Diabetes)

#### ✅ 심층 마스터 체크리스트
1.  **Review**:
    - [x] `EDA_01_Titanic_Analysis.ipynb`의 6단계(Macro-Analysis) 실행 결과 확인.
    - [x] `EDA_01_Diabetes_Analysis.ipynb` 생성 및 분석 수행.

2.  **Implementation (Output)**
    - [x] **Model Card 작성**: 내 모델의 한계점(Limitations)과 의도된 사용처(Intended Use)를 명시하는 미니 보고서 작성 (`docs/reports/Titanic_Model_Card.md`).
    - [x] **Code Refactoring**: `dev_data_analyst` 워크플로우를 완벽히 준수했는지 최종 점검.

---

## 📝 학습 로그 (Learning Log / Notes)

### Session 1 Notes
- 📄 **Detail Note**: [C1_M5_Note_Ethics_Project.md](../study_notes/C1_M5_Note_Ethics_Project.md)
- **Feynman Summary**:
    - **알고리즘의 편향(Bias)**: "데이터는 거울이다." 우리가 사는 세상의 불평등(성차별, 인종차별)이 데이터에 그대로 묻어 있으면, AI도 그대로 배운다.
        - **Selection Bias**: 여론조사를 하는데 '집전화' 있는 사람에게만 거는 것. 전체를 대표하지 못하는 샘플.
        - **Automation Bias**: "기계가 뱉은 결과니까 맞겠지"라고 무비판적으로 믿는 현상.
    - **공정성(Fairness)**:
        - 모델이 특정 그룹(성별, 인종)에게만 불리하게 동작하지 않도록 하는 것.
        - 타이타닉 예시: "여성은 무조건 생존, 남성은 무조건 사망"으로 예측하면 정확도는 높을지 몰라도, 모델이 '남성'이라는 이유만으로 생존 확률을 0으로 만드는 것은 공정한가?

### 🔨 트러블슈팅 로그 (Break Log)
- **Action**: 
- **Result**: 
- **Insight**: 

---

## ✅ 회고 (Retrospective)
- **Keep**: 
- **Problem**: 
- **Try**: 
