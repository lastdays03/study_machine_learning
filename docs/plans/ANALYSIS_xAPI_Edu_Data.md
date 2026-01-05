# 분석 계획서 (Analysis Plan): xAPI Student Performance Analysis

**Date**: 2026-01-05
**Analyst**: Antigravity
**Status**: 🔄 In Progress

---

## 1. 목표 설정 (Goal Setting)

### 핵심 질문
- **Question**: 학생들의 학습 행동(`raisedhands`, `VisITedResources`)과 부모의 참여(`ParentAnsweringSurvey`)가 학업 성취도(`Class`)에 미치는 영향은 무엇인가?
- **Utility**:
  - 데이터 기반으로 학생의 성적 등급(L, M, H)을 조기에 예측하여 맞춤형 교육 개입(Intervention) 가능.
  - 학업 성취도에 긍정적인 영향을 주는 주요 행동 패턴 발굴.

### Success Metrics (KPI)
- [ ] **성능 지표**: Accuracy ≥ 0.75, F1-Macro ≥ 0.70 (클래스 불균형 고려)
- [ ] **해석 지표**: 성적 향상에 기여하는 Key Feature Top 3 식별.
- [ ] **완료 조건**: 탐색적 분석(EDA)부터 Logistic Regression/XGBoost 모델링 및 평가까지 파이프라인 완성.

---

## 2. 방법론 (Methodology)

- **Type**: Multiclass Classification (Target: L, M, H)
- **Tools**:
  - **Data**: Pandas, NumPy
  - **Viz**: Seaborn, Matplotlib
  - **Model**: Scikit-Learn (LogisticRegression), XGBoost
- **Methodology Screening**:
  - **Handling Ordinal**: `GradeID` (G-02, G-04...)는 순서가 중요하므로 Label/Ordinal Encoding 고려.
  - **Handling Cat**: `NationalITy`, `Topic` 등은 One-Hot Encoding.
  - **Linear vs Non-linear**: 해석력이 좋은 **Logistic Regression**과 성능이 뛰어난 **XGBoost** 비교.

---

## 3. 검증 가설 (Hypothesis to Validate)

### 도메인 가설
1. **H1 (참여도)**: 손을 든 횟수(`raisedhands`)와 리소스 방문(`VisITedResources`) 횟수가 많을수록 성적 등급(H)이 높을 것이다.
2. **H2 (부모 관여)**: 부모가 설문에 응답했거나(`ParentAnsweringSurvey`=Yes) 학교 만족도가 높을수록 자녀의 성취도가 높을 것이다.
3. **H3 (출석)**: 결석(`StudentAbsenceDays`)이 7일 이상(Above-7)인 학생은 낮은 등급(L)일 확률이 매우 높다.

### 데이터 품질 가설
- **H_Data**: 범주형 변수의 카테고리가 다양하여(`NationalITy` 등) 희소(Sparse)한 클래스가 존재할 수 있다.

---

## 4. 예상 산출물 (Expected Deliverables)

- [ ] **Notebook**: `docs/notebooks/EDA_01_xAPI_Edu_Data.ipynb`
  - Data Cleaning & EDA (Participation vs Class Visualization)
  - Feature Engineering (Encoding, Scaling)
  - Modeling (Logistic vs XGBoost)
  - Evaluation (Confusion Matrix, Classification Report)
- [ ] **Report**: 중요 변수 분석 결과 및 교육적 시사점 도출.

---

## 5. 데이터 개요
- **File**: `data/xAPI-Edu-Data.csv`
- **Features**:
  - **Numerical**: `raisedhands`, `VisITedResources`, `AnnouncementsView`, `Discussion`
  - **Categorical**: `gender`, `NationalITy`, `PlaceofBirth`, `StageID`, `GradeID`, `SectionID`, `Topic`, `Semester`, `Relation`, `ParentAnsweringSurvey`, `ParentschoolSatisfaction`, `StudentAbsenceDays`
  - **Target**: `Class` (L, M, H)

---

## 6. 분석 단계 (OSEMN Framework)

### Phase 1: Obtain & Scrub
- 데이터 로드 및 결측치 확인.
- `Class` 컬럼의 분포 확인 (Imbalance Check).

### Phase 2: Explore
- 수치형 변수(`raisedhands` 등)와 `Class` 간의 Boxplot 분석.
- 범주형 변수(`ParentAnsweringSurvey`)와 `Class` 간의 Countplot 비교.
- 통계적 유의성 검증 (ANOVA or Chi-square).

### Phase 3: Model
- **Preprocessing**: 
    - Ordinal Encoding: `Class` (L < M < H)
    - One-Hot Encoding: Other Categoricals
    - Scaling: StandardScaler (Logistic Regression용)
- **Train**:
    1. **Logistic Regression** (Multinomial)
    2. **XGBoost Classifier**
- **Validation**: Stratified K-Fold.

### Phase 4: Interpret
- **Confusion Matrix**: 어떤 등급끼리 혼동하는지(예: M을 H로 잘못 예측) 분석.
- **Feature Importance**: 성적 예측에 가장 큰 영향을 미치는 요인 도출.
