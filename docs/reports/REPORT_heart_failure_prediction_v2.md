# 분석 결과 보고서 V2: Heart Failure Prediction (Advanced)

**Date**: 2026-01-05
**Analyst**: Antigravity
**Analysis File**: `docs/notebooks/EDA_02_heart_failure_prediction.ipynb`
**Goal**: 사망 위험 환자 식별 능력(Recall) 극대화 (Target: Recall > 0.75)

## 1. 운영 요약 (Executive Summary)
V2 분석에서는 **SMOTE(Data Augmentation)**와 **Threshold Tuning**을 통해 V1 대비 고위험군 식별 능력을 획기적으로 향상시켰습니다.
- **최종 성과**: Test Recall **0.84** 달성 (V1 0.63 대비 **33% 향상**)
- **Trade-off**: Recall 상승에 따라 Precision은 0.64로 다소 하락했으나, 놓치는 환자를 최소화한다는 의료적 목적 부합.
- **Key Strategy**: Random Forest (Balanced) + Threshold 조정 (0.5 → **0.31**)

## 2. 주요 개선 방법론 (Methodology)
1.  **SMOTE & Class Weight**:
    - 사망(Death Event=1) 데이터가 32%로 적은 불균형을 해소하기 위해 학습 시 합성 데이터 생성(SMOTE) 및 가중치 부여.
    - 결과: Cross Validation에서의 Recall 평균이 0.78수준으로 상승 (학습 안정성 확보).
2.  **Interaction Features**:
    - `age` * `serum_creatinine` 변수 추가로 고령자+신장기능저하 복합 위험 요소 반영.
3.  **Threshold Tuning (핵심 성공 요인)**:
    - 기본 임계값(0.5)에서는 Test Recall이 0.58~0.63에 머물렀으나, **0.31**로 낮춤으로써 잠재적 위험군까지 포착.

## 3. 모델 성능 비교 (V1 vs V2)

| Metric        | V1 (Best RF) | V2 (Default Threshold) | **V2 (Tuned Threshold 0.31)** | 비고                         |
| :------------ | :----------- | :--------------------- | :---------------------------- | :--------------------------- |
| **Recall**    | 0.63         | 0.58                   | **0.84**                      | **Target(0.75) 초과 달성**   |
| **Precision** | 0.79         | 0.69                   | 0.64                          | 다소 하락 (False Alarm 증가) |
| **F1 Score**  | 0.71         | 0.63                   | 0.73                          | 전반적 균형 유지             |

- **XGBoost/LightGBM**: 튜닝 없이도 0.63 수준의 Recall을 보였으나, Tuning된 RF의 0.84에는 미치지 못함.

## 4. 결론 및 제언 (Conclusion)
- **성공적인 Recall 개선**: 단순 모델 교체보다 **비즈니스 목적에 맞는 Threshold 설정**이 훨씬 강력함을 입증.
- **현장 적용 가이드**:
    - 예측 확률이 **31% 이상**인 환자는 모두 '집중 관리 대상'으로 분류.
    - 이 경우 실제 사망 위험 환자의 **84%**를 사전에 발견할 수 있음.
