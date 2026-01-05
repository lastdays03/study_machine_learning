# Study Machine Learning

> **Status**: Active
> **Type**: Study
> **Created**: 2025-12-30

## 📖 Overview
이 프로젝트는 "AI 리터러시와 기초 모델링"부터 "심화 알고리즘과 실전 품질관리"까지 머신러닝의 전 과정을 체계적으로 학습하기 위한 공간입니다. 입문자 과정과 중급자 과정을 포괄하며, 이론 학습과 실습(Colab/Jupyter)을 병행합니다.

## 📚 Curriculum

### [Course 1] 머신러닝 입문자 과정: "AI 리터러시와 기초 모델링"
인공지능의 기본 개념 이해 및 파이썬 도구를 활용한 데이터 전처리, 기초 예측 모델링 목표.

*   **Module 1: 머신러닝 입문 및 환경 설정**
    *   머신러닝 정의, 용어(Feature, Label, Overfitting)
    *   Google Colab 환경 구축
    *   기초 통계 및 확률
*   **Module 2: 데이터 핸들링 및 시각화**
    *   Python 라이브러리: Numpy, Pandas
    *   데이터 시각화: Matplotlib, Seaborn
*   **Module 3: 지도 학습 기초 - 회귀(Regression)**
    *   선형 회귀(Linear Regression)
    *   최적화 원리: 경사하강법(Gradient Descent)
*   **Module 4: 지도 학습 기초 - 분류(Classification)**
    *   알고리즘: 로지스틱 회귀, k-NN
    *   의사결정 트리(Decision Tree)
*   **Module 5: 인공지능 윤리 및 입문 프로젝트**
    *   AI 윤리와 편향성
    *   미니 프로젝트: 붓꽃(Iris) 분류 또는 타이타닉 생존자 예측

### [Course 2] 머신러닝 마스터 클래스: "딥러닝, LLM, 그리고 MLOps"
심화 알고리즘 활용부터 최신 생성형 AI 모델 구축, 그리고 서비스 배포(MLOps)까지 한 번에 마스터하는 전문가 과정.

*   **Module 1: 머신러닝 심화와 데이터 품질 (Advanced ML & Data Quality)**
    *   **앙상블 기법**: Random Forest, XGBoost, LightGBM 하이퍼파라미터 튜닝.
    *   **비지도 학습**: 군집화(K-Means), 차원 축소(PCA), 이상 탐지(Anomaly Detection).
    *   **추천 시스템**: 협업 필터링(Collaborative Filtering) 원리 및 구현.
    *   **평가 및 최적화**: Precision-Recall Curve, Threshold Moving.
    *   **데이터 품질 관리**: NIA 가이드라인 기반 데이터 검증 및 편향성 제거 실습.
*   **Module 2: 딥러닝과 비정형 데이터 (Deep Learning Foundations)**
    *   **Neural Networks**: 역전파(Backprop), 최적화(Adam, Dropout) 원리.
    *   **Computer Vision**: CNN 구조(ResNet 등) 이해 및 이미지 분류.
    *   **NLP 기초**: 임베딩(Word2Vec), RNN/LSTM, Attention 메커니즘.
*   **Module 3: 트랜스포머와 LLM (Transformers & GenAI)**
    *   **Transformer Architecture**: "Attention is All You Need" 논문 구현.
    *   **Transfer Learning**: HuggingFace를 활용한 BERT/GPT 파인튜닝.
    *   **RAG System**: Vector DB(Chroma)와 LangChain을 활용한 문서 기반 챗봇 구축.
*   **Module 4: MLOps와 엔지니어링 (Engineering & Serving)**
    *   **Experiment Tracking**: MLflow/W&B로 실험 이력 관리.
    *   **Model Serving**: FastAPI를 이용한 실시간 추론 API 개발.
    *   **Deployment**: Docker 컨테이너화 및 클라우드 배포 기초.

## 🏗️ Structure
- `src/`: 소스 코드 및 모듈
- `docs/`: 학습 계획 및 이론 정리 문서
- `notebooks/`: Jupyter Notebook 실습 파일 (`.ipynb`)
    - `course_1/`: 입문 과정 (C1_M#)
    - `course_2/`: 심화 과정 (C2_M#)
- `data/`: 학습용 데이터셋 (Git Ignore 권장)
- `references/`: 참고 자료 (논문, PDF 등)
- `tests/`: 테스트 코드
- `scripts/`: 유틸리티 스크립트
