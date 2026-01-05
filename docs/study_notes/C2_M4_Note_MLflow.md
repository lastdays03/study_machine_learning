# Study Note: Experiment Tracking (MLflow)

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M4_Plan_MLOps.md](../plans/C2_M4_Plan_MLOps.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 MLOps Cycle
*   Dev(개발) -> Ops(운영)의 무한 루프.
*   **Tracking**: 실험 기록.
*   **Registry**: 모델 버전 관리.
*   **Serving**: 배포 및 모니터링.

### 1.2 Experiment Tracking Components
*   **Parameters**: 하이퍼파라미터 (LR, Batch Size, Depth 등).
*   **Metrics**: 성능 지표 (Accuracy, Loss, RMSE).
*   **Artifacts**: 결과물 파일 (Model.pkl, Plot.png, Data Sample).
*   **Source**: 어떤 코드(Git Commit)로 실행했는가?

### 1.3 Model Registry
*   실험 단계(Staging)에서 검증이 끝난 모델만 운영 단계(Production)로 승격(Promote)시키는 관리소.

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M4_Exp_MLflow.ipynb`
*   **Insight**: 
    *   Auto-logging: 프레임워크(Sklearn, TF, PyTorch)별 자동 로깅 기능을 쓰면 편리하다.
    *   비교 분석: MLflow UI에서 여러 실험을 선택해 병렬 좌표(Parallel Coordinates) 그래프를 그리면, 어떤 하이퍼파라미터가 중요한지 한눈에 보인다.

## 3. 🔨 Break & Fix Log
*   **Break**: 모델 저장 시 의존성 라이브러리 버전 기록 안 함.
*   **Result**: 나중에 로딩할 때 `ModuleNotFoundError` 또는 버전 불일치로 예측값 달라짐.
