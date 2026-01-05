# Study Note: Deployment (Docker)

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M4_Plan_MLOps.md](../plans/C2_M4_Plan_MLOps.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 Containerization
*   **Virtual Machine (VM)**: 하드웨어부터 OS까지 통째로 가상화. 무겁다.
*   **Container (Docker)**: 호스트 OS의 커널을 공유하면서, 프로세스만 격리. 가볍고 빠르다.
*   **Image**: 변하지 않는(Immutable) 템플릿. 소스 코드 + 라이브러리 + 의존성.
*   **Container**: 이미지를 실행한 상태(Process).

### 1.2 MLOps with Docker
*   **Reproducibility (재현성)**: "내 로컬에선 되는데..." 문제의 완벽한 해결책.
*   **Scalability (확장성)**: 쿠버네티스(K8s) 같은 오케스트레이션 도구로 컨테이너를 수십 개로 늘렸다가 줄였다가 할 수 있음.

### 1.3 Dockerfile 핵심
*   `FROM`: 베이스 이미지 (python:3.9-slim 등)
*   `WORKDIR`: 작업 디렉토리
*   `COPY`: 파일 복사
*   `RUN`: 명령어 실행 (pip install 등)
*   `CMD`: 컨테이너 시작 시 실행할 명령

## 2. 🧪 Experiment & Insight
*   **Experiment**: `Dockerfile` build & run
*   **Insight**: 
    *   **Layer Caching**: Docker는 각 줄(Layer)을 캐싱한다. 자주 바뀌는 소스 코드 복사(`COPY . .`)를 `pip install` 뒤에 두어야 빌드 속도가 빠르다.
    *   **Multi-stage Build**: 빌드 도구는 빼고 실행 파일만 남겨서 이미지 크기를 줄일 수 있다.

## 3. 🔨 Break & Fix Log
*   **Break**: 호스트의 파일 경로(예: `C:/Users/...`)를 코드에 하드코딩.
*   **Result**: 컨테이너 안에는 그런 경로가 없어서 에러 발생. 상대 경로를 써야 함.
