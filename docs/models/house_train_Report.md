# House Train 데이터 분석 리포트

> [!NOTE]
> `data/house_train.csv` (학습 데이터)에 대한 분석 결과입니다. `house_train_Analysis.ipynb`의 내용을 요약합니다.

## 1. Model Details
- **데이터셋**: House Train Data (`house_train.csv`)
- **목적**: 주택 가격 예측 모델 학습을 위한 데이터 특성 파악
- **Target 변수**: `SalePrice` (주택 판매 가격)

## 2. Intended Use
- 이 분석 내용은 추후 회귀 모델(Regression Model) 구축 시 Feature Engineering 및 전처리 전략 수립에 활용됩니다.
- 학습 단계에서 `SalePrice`를 예측하는 것이 최종 목표입니다.

## 3. Factors (Target Analysis)
- **분포 특성**: `SalePrice`는 오른쪽 꼬리가 긴(Right-skewed) 분포를 보임.
- **정규성**: 원본 데이터는 정규성을 만족하지 않으나, **로그 변환(Log Transformation, `np.log1p`)** 적용 시 정규 분포에 근사함.
- **권장 사항**: 모델 학습 시 Target 변수에 반드시 로그 변환을 적용하고, 예측 후 지수 변환(`np.expm1`)으로 복원해야 함.

## 4. Metrics (Correlation)
`SalePrice`와 높은 양의 상관관계를 보이는 주요 변수(Top Features)는 다음과 같습니다:
1. **OverallQual (0.79)**: 전반적인 품질이 가격 결정의 가장 큰 요인.
2. **GrLivArea (0.71)**: 거주 면적이 클수록 가격 상승.
3. **GarageCars (0.64) / GarageArea (0.62)**: 차고의 크기 및 수용 능력이 중요함.
4. **TotalBsmtSF (0.61)**: 지하실 면적 또한 주요 영향 변수임.

## 5. Caveats & Recommendations
- **전처리 필수**: Target 변수의 로그 변환 누락 시 모델 성능 저하 우려.
- **다중공선성 주의**: `GarageCars`와 `GarageArea`는 상관관계가 높으므로(0.88), 모델링 시 변수 선택(Selection)이나 PCA 고려 필요.
- **이상치 처리**: `GrLivArea` 대비 가격이 지나치게 낮은 샘플(이상치)이 존재할 경우 삭제 필요.
