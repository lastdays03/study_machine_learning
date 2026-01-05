# Study Note: Model Serving (FastAPI)

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M4_Plan_MLOps.md](../plans/C2_M4_Plan_MLOps.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 Model Serving Patterns
*   **Batch Serving**: 밤마다 한 번씩 대량으로 예측해서 DB에 저장. (추천 시스템 등)
*   **Online Serving (API)**: 사용자가 요청할 때마다 실시간으로 예측. (챗봇, 이상 탐지 등)
    *   **Latency (지연 시간)**: 얼마나 빨리 응답하는가?
    *   **Throughput (처리량)**: 초당 몇 건을 처리하는가?

### 1.2 FastAPI & Async
*   **FastAPI**: Python 웹 프레임워크 중 가장 빠르고 현대적(Type Hint 기반).
*   **Uvicorn (ASGI)**: 비동기(Asynchronous) 서버 게이트웨이.
*   **Async/Await**: I/O 대기 시간(DB 조회, 외부 요청) 동안 멍하니 기다리지 않고 다른 요청을 처리하는 동시성 기술.

## 2. 🧪 Experiment & Insight
*   **Experiment**: `src/serving/app.py`
*   **Insight**: 
    *   **Pydantic**: 입출력 데이터의 스키마를 정의하면, validation 코드를 따로 짤 필요가 없다.
    *   무거운 모델은 서버 띄울 때 미리 GPU에 올려놔야 한다 (Warm-up).

## 3. 🔨 Break & Fix Log
*   **Break**: API 핸들러 안에서 `time.sleep()` 같은 동기 함수 사용.
*   **Result**: 전체 서버가 멈춰버림 (Blocking). 비동기 함수 `asyncio.sleep` 등을 써야 함.
