# 분석 계획서: House Price Prediction (Deep Learning)

**작성자**: AI Assistant
**날짜**: 2026-01-09
**상태**: [x] 승인 완료

## 1. 분석 목표 (Goal Setting)
- **Problem**: 기존 Tree-based 모델(XGBoost/LGBM) 외에 **Deep Learning(딥러닝)**을 활용하여 주택 가격을 예측해봅니다.
- **Goal**: 딥러닝 모델(MLP)의 성능을 최적화하고, 기존 머신러닝 모델과 성과를 비교합니다.
- **KPIs**:
    - **RMSLE (Root Mean Squared Log Error)**: Target: < 0.15 (기존 모델 수준 도전).

## 2. 방법론 스크리닝 (Methodology Screening)
딥러닝에 적합한 전처리 및 모델링 기법을 선정했습니다.

### 2.1 데이터 전처리 (Preprocessing for DL)
| 항목               | 기법                              | 선정 이유                                                                                 |
| :----------------- | :-------------------------------- | :---------------------------------------------------------------------------------------- |
| **Scaling**        | **StandardScaler / MinMaxScaler** | 딥러닝은 Feature Scale에 민감하므로 모든 수치형 변수를 0~1 또는 표준정규분포로 변환 필수. |
| **Categorical**    | **One-Hot Encoding**              | 범주형 변수를 0과 1의 벡터로 변환하여 신경망 입력으로 사용.                               |
| **Target**         | **Log Transformation**            | `SalePrice`의 Skewness 완화를 위해 로그 변환 유지.                                        |
| **Missing Values** | **Zero/Mode Imputation**          | 이전 분석과 동일하게 Meaningful NA 처리 후 잔여 결측치 대치.                              |

### 2.2 모델링 (Deep Learning Architecture)
- **Framework**: TensorFlow / Keras (Sequential API).
- **Architecture (MLP)**:
    - **Input Layer**: 전처리된 모든 Feature (약 200~300개 예상).
    - **Hidden Layers**: 3~4개의 Dense Layer (Nodes: 256 -> 128 -> 64 -> 32).
    - **Activation**: `ReLU` (일반적인 은닉층 활성화 함수).
    - **Regularization**: `Dropout` (0.2~0.3) 및 `BatchNormalization`으로 과적합 방지.
    - **Output Layer**: 1 Node (Linear Activation for Regression).
- **Training**:
    - **Optimizer**: `Adam` (Learning Rate 조절).
    - **Loss Function**: `MSE` (Mean Squared Error).
    - **Callbacks**: `EarlyStopping` (Patience=20), `ModelCheckpoint` (Save Best Only).

## 3. 분석 가설 (Hypotheses)
1. **비선형성 학습**: 딥러닝은 변수 간의 복잡한 비선형 상호작용을 스스로 학습하여 Tree 모델과는 다른 패턴을 찾을 것이다.
2. **Scaling 효과**: 정규화(Scaling)를 통해 수렴 속도와 성능이 크게 향상될 것이다.

## 4. 예상 산출물 (Deliverables)
1. **Analysis Notebook**: `docs/notebooks/EDA_02_House_DL.ipynb`
2. **Analysis Report**: `walkthrough.md` 업데이트 (DL 모델 결과 추가)
3. **Optimized Model**: `model/best_house_dl_model.keras`

## 5. 리스크 및 대응 (Risks)
- **Overfitting**: 데이터 수(1460개) 대비 파라미터가 많아 과적합 위험 -> `Dropout`, `L2 Regularization` 적용.
- **Training Time**: 학습 시간이 길어질 수 있음 -> `EarlyStopping`으로 효율적 제어.
