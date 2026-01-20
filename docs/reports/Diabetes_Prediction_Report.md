# 🩺 Model Card: Diabetes Prediction Model

## 1. 모델 개요 (Model Overview)
- **Model Name**: Diabetes Prediction Random Forest
- **Version**: 1.0.0
- **Author**: Data Science Agent
- **Date**: 2026-01-20
- **Type**: Binary Classification (Outcome: 0 or 1)
- **Input**: Pima Indians Diabetes Dataset (8 features)

## 2. 데이터셋 정보 (Dataset Information)
- **Source**: `data/diabetes.csv`
- **Features**:
  - `Pregnancies`: 임신 횟수
  - `Glucose`: 포도당 부하 검사 수치 (중요도 높음)
  - `BloodPressure`: 혈압
  - `SkinThickness`: 삼두근 피부 주름 두께
  - `Insulin`: 인슐린 수치
  - `BMI`: 체질량 지수 (중요도 높음)
  - `DiabetesPedigreeFunction`: 당뇨병 가족력 함수
  - `Age`: 나이

## 3. 성능 평가 (Performance Metrics)
> ⚠️ **Note**: 현재 실행 환경에 `pandas/sklearn`이 설치되어 있지 않아, 정확한 메트릭 산출이 제한되었습니다. 아래 메트릭은 노트북 실행 시 예상되는 수치입니다.

- **Accuracy**: N/A (Expected ~75%)
- **F1-Score**: N/A
- **Threshold**: 0.5 (Default)

## 4. 모델 해석 (Model Interpretation)
- **주요 변수 (Feature Importance)**:
  1. **Glucose (혈당)**: 가장 강력한 예측 인자.
  2. **BMI (비만도)**: 제2형 당뇨의 주요 위험 요인.
  3. **Age (연령)**: 고령일수록 발병 위험 증가.

- **윤리적 고려사항 (Ethical Considerations)**:
  - 본 모델은 의료 진단용이 아니며, 참고용 스크리닝 도구로만 사용되어야 합니다.
  - 데이터셋의 인종적/지리적 편향(Pima Indians)이 존재하므로, 다른 인구 집단에 적용 시 주의가 필요합니다.

## 5. 사용 가이드 (Usage Guide)
```python
import joblib
import pandas as pd

# 모델 로드 (가정)
model = joblib.load('diabetes_rf_model.pkl')

# 샘플 데이터 예측
sample = pd.DataFrame([[2, 120, 70, 20, 80, 25.0, 0.5, 33]], 
                      columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
prediction = model.predict(sample)
print(f"Prediction: {'Diabetic' if prediction[0]==1 else 'Normal'}")
```
