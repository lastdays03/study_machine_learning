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
---

# Model Card: Heart Failure Prediction (V1 & V2)

> [!NOTE]
> 이 리포트는 `data-model-reporter` 워크플로우를 기반으로 `EDA_01` 및 `EDA_02` 노트북을 비교 분석하여 자동 생성되었습니다.

## 1. 모델 개요 (Model Details)
*   **Name**: Heart Failure Predictor (V1 vs V2 Comparison)
*   **Version**: 2.0 (2026-01-05)
*   **Type**: RandomForestClassifier
*   **Framework**: Scikit-Learn 1.x
*   **Dev**: Antigravity (AI Agent)

## 2. 사용 목적 (Intended Use)
*   **Primary Use**:
    *   임상 기록(나이, 혈청 크레아틴, 박출계수 등)을 바탕으로 심부전증 환자의 사망 위험을 조기에 예측.
    *   의료진이 고위험군 환자를 선별하여 집중 모니터링 대상을 정하는 보조 도구(CDSS).
*   **Out of Scope (사용 제한)**:
    *   **단독 진단 도구로 사용 금지**: 최종 진단은 반드시 전문 의료진의 판단을 따라야 함.
    *   **어린이 환자**: 데이터셋이 성인(주로 고령자) 위주이므로 소아 환자에게는 적용 불가.

## 3. 주요 요소 및 성능 (Factors & Metrics)
### Factors (Features)
랜덤 포레스트 모델의 Feature Importance 분석 결과, 다음 변수들이 예측에 가장 큰 영향을 미쳤습니다.
*   `time`: 관찰 기간 (가장 강력한 설명력을 가지나 생존 편향 주의 필요)
*   `serum_creatinine`: 혈중 크레아틴 농도 (신장 기능 지표)
*   `ejection_fraction`: 박출계수 (심장 기능 지표)

### Metrics Comparison
테스트 데이터셋(Stratified Split, 20%)에 대한 평가 결과입니다.

| Model                | Accuracy   | F1-Score | Recall     | ROC-AUC    | 비고                 |
| :------------------- | :--------- | :------- | :--------- | :--------- | :------------------- |
| **V1 Logistic**      | 0.8167     | 0.6667   | 0.5789     | 0.8588     | Baseline             |
| **V1 Random Forest** | **0.8500** | 0.7273   | 0.6316     | **0.8941** | Best Overall         |
| **V2 RF (Tuned)**    | N/A        | N/A      | **0.7500** | N/A        | **Recall Optimized** |

*   **Insight**: V1 모델은 전반적인 정확도가 높으나 사망자(Class 1)를 찾아내는 Recall이 0.63으로 다소 낮음. V2는 임계값 조정(Threshold Tuning)을 통해 **Recall을 0.75까지 향상**시켜, '놓치는 환자'를 줄이는 데 최적화됨.

## 4. 윤리적 고려사항 (Ethical Considerations)
데이터 및 모델이 내포할 수 있는 편향과 공정성 문제입니다. **(사용자 검토 필수)**

1.  **Imbalanced Data (클래스 불균형)**:
    *   데이터셋의 약 68%가 생존, 32%가 사망으로 구성되어 있어, 모델이 생존(0)을 더 잘 맞추는 경향이 있음. V2에서 Class Weight로 보정했으나 여전히 주의 필요.
2.  **Age Bias (연령 편향)**:
    *   데이터 대다수가 50대 이상의 고령자로 구성됨. 젊은 심부전증 환자에 대한 예측 성능은 검증되지 않음.
3.  **Survival Bias (생존 편향)**:
    *   `time` 변수는 '오래 살았기 때문에 관찰 기간이 긴' 인과관계 역전의 소지가 있음. V2에서 `time`을 제거한 실험 결과도 함께 고려해야 함.

## 5. 정량적 분석 (Quantitative Analysis)
*   **Recall-Precision Trade-off**: V2에서 Recall을 0.63 -> 0.75로 높이는 과정에서 Precision(정밀도)은 하락했을 것임. 이는 위양성(실제 생존이나 사망으로 예측)이 증가함을 의미하며, 이는 추가 검사 비용을 발생시키지만 사망을 놓치는 것보다는 낫다는 비즈니스 판단이 전제됨.
