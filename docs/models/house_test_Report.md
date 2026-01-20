# House Test 데이터 분석 리포트

> [!NOTE]
> 이 리포트는 `data-science-master` 워크플로우에 따라 `house_test_Analysis.ipynb`의 분석 결과를 요약한 문서입니다.

## 1. Model Details
- **데이터셋 명**: House Test Data (`house_test.csv`)
- **분석 유형**: 탐색적 데이터 분석 (EDA) 및 전처리 진단
- **작성 일자**: 2026-01-20
- **프레임워크**: Python (Pandas, Seaborn)

## 2. Intended Use
- **목적**: 주택 가격 예측 모델링을 위한 테스트 데이터셋의 특성을 파악하고, 학습 데이터(`train.csv`)와의 분포 차이 등을 비교하기 위함.
- **적용 범위**: 미국 아이오와주 에임스(Ames) 지역의 주거용 주택 특성 분석.
- **예상 사용자**: 데이터 사이언티스트, 부동산 시장 분석가.

## 3. Factors
- **주요 변수 (Features)**:
  - `OverallQual`: 전반적인 재료 및 마감 품질 (1~10)
  - `GrLivArea`: 지상 주거 면적 (sq ft)
  - `YearBuilt`: 건축 연도
  - `LotArea`: 부지 면적
  - `Neighborhood`: 물리적 위치 (동네)
- **환경 요인**: 주택 시장의 경기 변동 및 지역적 특성.

## 4. Metrics & Analysis
- **데이터 규모**: 1,459 행(Samples) x 80 열(Features)
- **결측치 현황**:
  - `PoolQC`, `MiscFeature`, `Alley` 등은 90% 이상의 높은 결측률을 보임. (해당 시설 부재 의미)
  - `LotFrontage`는 약 15~20% 결측.
- **분포 특성**:
  - `LotArea` 등 면적 관련 변수는 Right-skewed(오른쪽 꼬리가 긴) 형태를 띰. -> 로그 변환 필요성 시사.
  - `OverallQual`은 정규 분포와 유사하나 약간의 치우침 존재.

## 5. Caveats & Recommendations
- **결측치 처리 주의**: `NA`가 단순히 '데이터 없음'이 아니라 '해당 시설 없음'을 의미하는 경우가 많으므로(예: 차고 없음), 무조건적인 삭제보다는 **의미에 기반한 대체(Imputation)**가 필요함.
- **이상치(Outlier)**: `LotArea` 등에서 극단적인 값이 발견될 수 있으므로, 학습 시 Robust Scaler 사용이나 이상치 제거가 권장됨.
- **파생 변수**: 건축 연도(`YearBuilt`)와 리모델링 연도(`YearRemodAdd`)를 활용해 '건물 연식' 등의 파생 변수를 생성하면 예측력을 높일 수 있음.
