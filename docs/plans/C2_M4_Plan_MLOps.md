# 학습 계획서 (Study Plan): Course 2 Module 4 - MLOps & Engineering

**Status**: 📅 Planned
**Created**: 2026-01-05
**Goal**: 개발된 모델을 연구실(Notebook)에서 꺼내어, 실제 서비스 환경(Production)에 배포하고 운영하는 MLOps 파이프라인을 구축한다.

---

## 🎯 핵심 목표 (Deep Objective)
**"From Model to Product"**
- [ ] What: MLflow(실험 관리), FastAPI(서빙), Docker(컨테이너), GitHub Actions(CI/CD).
- [ ] Why: "내 컴퓨터에서는 잘 되는데요?"를 방지하고, 지속 가능한 머신러닝 시스템을 만들기 위해.
- [ ] How: [MLOps Zoomcamp, FastAPI 튜토리얼]

---

## 📅 커리큘럼 (Curriculum)

### Session 1: 실험의 기록 (Experiment Tracking)
**Focus**: MLflow / Weights & Biases

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Experiment Tracking**: 왜 실험 파라미터와 결과를 DB에 저장해야 하는가? (재현성 확보).
    - [ ] **Model Registry**: 모델 버전 관리(Staging vs Production)의 필요성.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: 시드를 고정하지 않고 실험하여 결과가 계속 바뀌는 '재현 불가능한' 상황 경험.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M4_Exp_MLflow.ipynb` 생성 (로컬 MLflow 서버 띄우고 실험 로깅).

### Session 2: 모델 서빙 (Model Serving)
**Focus**: REST API, FastAPI

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **API (Application Programming Interface)**: "식당의 점원" 비유로 클라이언트와 서버의 통신 설명.
    - [ ] **Serialization**: 모델 객체(Pickle)를 파일로 저장하고 API 서버에서 로딩하는 과정.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: 대용량 요청을보내서 API 서버가 멈추는(Latency) 현상 확인 및 배치 처리 필요성 체감.
3.  **Implementation (Output)**
    - [ ] `src/serving/app.py` 생성 (간단한 예측 API 구현 및 테스트).

### Session 3: 어디서든 실행되게 (Deployment)
**Focus**: Docker, Containerization

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Container**: "가상 환경을 통째로 얼려서 배송하는" 도시락통 비유. VM과의 차이점.
    - [ ] **Dockerfile**: 이미지를 굽기 위한 레시피 작성법.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: 호스트 OS 라이브러리 의존성 때문에 다른 컴퓨터에서 실행 실패하는 상황 재현 -> Docker로 해결.
3.  **Implementation (Output)**
    - [ ] `Dockerfile` 작성 및 로컬 컨테이너 배포 실습.

---

## 📝 학습 로그 (Learning Log / Notes)

### Session 1 Notes (MLflow)
- 📄 **Detail Note**: [C2_M4_Note_MLflow.md](../study_notes/C2_M4_Note_MLflow.md)

### Session 2 Notes (FastAPI)
- 📄 **Detail Note**: [C2_M4_Note_FastAPI.md](../study_notes/C2_M4_Note_FastAPI.md)

### Session 3 Notes (Docker)
- 📄 **Detail Note**: [C2_M4_Note_Docker.md](../study_notes/C2_M4_Note_Docker.md)
