# 분석 계획서: House Price Prediction (Regression)

**작성자**: AI Assistant
**날짜**: 2026-01-09
**상태**: [x] 승인 완료

## 1. 분석 목표 (Goal Setting)
- **Problem**: 주택의 다양한 특성(80개 변수)을 기반으로 최종 가격(`SalePrice`)을 예측합니다.
- **Goal**: 정확도 높은 회귀 모델을 구축하고, 가격 결정에 영향을 미치는 주요 요인을 규명합니다.
- **KPIs**:
    - **RMSE (Root Mean Squared Error)**: 로그 변환된 예측값과 실제값의 차이 (Kaggle Standard: RMSLE).
    - **R-Squared ($R^2$)**: 모델의 설명력 (Target: > 0.85).

## 2. 방법론 스크리닝 (Methodology Screening)
`SKILL.md`에 기반하여 다음 기법을 선정했습니다.

### 2.1 데이터 전처리 (Preprocessing)
| 문제점               | 해결 방안                            | 선정 이유                                                          |
| :------------------- | :----------------------------------- | :----------------------------------------------------------------- |
| **Skewed Target**    | **Log Transformation**               | `SalePrice`는 우측으로 긴 꼬리를 가지므로 정규분포에 근사시킴      |
| **Missing Values**   | **Meaningful NA Handling**           | `PoolQC`, `Alley` 등의 NA는 '없음'을 의미하므로 별도 범주로 처리   |
| **High Cardinality** | **Target Encoding / Label Encoding** | `Neighborhood` 등 범주가 많은 변수에 적용                          |
| **Ordinal Features** | **Manual Mapping**                   | `ExterQual` (Ex, Gd, TA, Fa, Po) 등 순서가 있는 범주는 숫자로 매핑 |

### 2.2 모델링 (Modeling)
- **Baseline**: `Linear Regression (Lasso/Ridge)` - 규제를 통해 다중공선성 제어.
- **Advanced**: `XGBoost`, `LightGBM` - 결측치 처리 능력이 우수하고, 테이블 데이터에서 SOTA 성능.

## 3. 분석 가설 (Hypotheses)
1. **면적과 품질**: `GrLivArea`(지상 거주 면적)와 `OverallQual`(전반적 품질)은 가격과 가장 강한 양의 상관관계를 가질 것이다.
2. **건축 연도**: 최근에 지어진 집(`YearBuilt`)일수록 가격이 높을 것이나, 리모델링(`YearRemodAdd`) 여부가 변수가 될 것이다.
3. **지역성**: `Neighborhood`에 따라 가격대(Cluster)가 형성될 것이다.

## 4. 예상 산출물 (Deliverables)
1. **Analysis Notebook**: `docs/notebooks/EDA_01_House.ipynb` (데이터 전처리, EDA, 모델링 과정 포함)
2. **Analysis Report**: `walkthrough.md` (주요 발견 사항 및 모델 성능 요약)
3. **Model Weights**: `model/best_house_model.pkl` (최적 모델 저장)

## 5. 리스크 및 대응 (Risks)
- **Overfitting**: 훈련 데이터에 과적합될 위험 -> `K-Fold Cross Validation` 및 `Early Stopping` 적용.
- **Data Leakage**: 전처리(Target Encoding 등) 시 Train/Test 분리 엄격 준수.
