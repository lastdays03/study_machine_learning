---
language: 
  - ko
  - en
tags:
  - tabular-classification
  - healthcare
datasets:
  - heart_failure_clinical_records_dataset
metrics:
  - accuracy
  - recall
  - f1
  - roc_auc
model-index:
  - name: RandomForest_V2_Tuned
    results:
      - task:
          type: tabular-classification
        metrics:
          - type: recall
            value: 0.75
          - type: accuracy
            value: 0.85
  - name: XGBoost_V3_Realistic
    results:
      - task:
          type: tabular-classification
        metrics:
          - type: recall
            value: 0.42
          - type: accuracy
            value: 0.74
---

# Model Card: Heart Failure Prediction (V1, V2, V3 Comparison)

> [!NOTE]
> 이 리포트는 `data-model-reporter` 워크플로우를 기반으로 `EDA_01`, `EDA_02`, `EDA_03`를 종합 분석한 결과입니다.

## 1. 모델 개요 (Model Details)
*   **Name**: Heart Failure Predictor (Realistic vs Optimistic)
*   **Version**: 3.0 (2026-01-06)
*   **Type**: XGBoost / RandomForest / KNN
*   **Framework**: Scikit-Learn 1.x, XGBoost
*   **Dev**: Antigravity (AI Agent)

## 2. 사용 목적 (Intended Use)
*   **Primary Use**: 초기 진단 시점의 환자 데이터를 기반으로 사망 위험 예측.
*   **Out of Scope**: 관찰 기간(`time`)이 포함된 데이터 사용 금지 (Data Leakage 주의).

## 3. 주요 요소 및 성능 (Factors & Metrics)

### 🚨 Critical Finding: The Impact of 'time' Variable
V1/V2와 V3의 성능 차이가 극명하게 발생했습니다.
- **V1/V2 (With `time`)**: `time` 변수가 사망 여부와 직접적인 인과(생존했으므로 관찰 기간이 김)를 가져 성능이 과대포장됨. (Recall 0.75)
- **V3 (Without `time`)**: 초기 진단 데이터만으로 예측 시, 실제 성능은 Recall 0.42 수준으로 하락함. 이는 **현실적인 예측 난이도**를 보여줌.

### Metrics Comparison (Test Set)

| Model                     | Recall (Target) | Accuracy | F1-Score | ROC-AUC  | 비고               |
| :------------------------ | :-------------- | :------- | :------- | :------- | :----------------- |
| **V1 Logistic** (w/ Time) | 0.58            | 0.82     | 0.67     | 0.86     | Baseline (Leaky)   |
| **V2 RF Tuned** (w/ Time) | **0.75**        | **0.85** | **0.73** | **0.89** | Optimized (Leaky)  |
| **V3 Logistic** (No Time) | 0.37            | N/A      | N/A      | 0.74     | Realistic Baseline |
| **V3 KNN** (No Time)      | 0.16            | N/A      | N/A      | N/A      | Poor Performance   |
| **V3 XGBoost** (No Time)  | **0.42**        | 0.74     | N/A      | **0.74** | **Realistic Best** |

*   **Insight**: `time` 변수 제거 시 모델들이 사망자(Class 1)를 찾아내는 데 큰 어려움을 겪음. XGBoost가 그나마 가장 높은 Recall(0.42)을 기록했으나, 임상적 활용을 위해서는 추가적인 Feature 발굴이 시급함.

## 4. 윤리적 고려사항 (Ethical Considerations)
1.  **Data Leakage Warning**: `time` 변수는 사후적으로 결정되는 값이므로, 사전 예측 모델에 포함되어서는 안 됨. V1/V2 결과는 '연구용'으로만 의미가 있음.
2.  **False Negative Risk**: V3(현실 모델)의 Recall이 0.42에 불과하여, 실제 고위험군 환자의 58%를 놓칠 수 있음. 단독 진단 도구 사용 절대 금지.

## 5. 정량적 분석 (Quantitative Analysis) 
*   **Top 10 Errors**: XGBoost가 틀린 케이스를 분석한 결과, `ejection_fraction`이 정상 범위임에도 사망한 케이스들을 주로 놓침. 이는 기존 임상 지표 외의 숨겨진 위험 요인(유전적 요인 등)이 존재함을 시사함.
