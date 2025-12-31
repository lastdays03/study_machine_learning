# Study Machine Learning

> **Status**: Active
> **Type**: Study
> **Created**: 2025-12-30

## 📖 Overview
이 프로젝트는 "AI 리터러시와 기초 모델링"부터 "심화 알고리즘과 실전 품질관리"까지 머신러닝의 전 과정을 체계적으로 학습하기 위한 공간입니다. 입문자 과정과 중급자 과정을 포괄하며, 이론 학습과 실습(Colab/Jupyter)을 병행합니다.

## 📚 Curriculum

### [Course 1] 머신러닝 입문자 과정: "AI 리터러시와 기초 모델링"
인공지능의 기본 개념 이해 및 파이썬 도구를 활용한 데이터 전처리, 기초 예측 모델링 목표.

*   **1주차: 머신러닝 입문 및 환경 설정**
    *   머신러닝 정의, 용어(Feature, Label, Overfitting)
    *   Google Colab 환경 구축
    *   기초 통계 및 확률
*   **2주차: 데이터 핸들링 및 시각화**
    *   Python 라이브러리: Numpy, Pandas
    *   데이터 시각화: Matplotlib, Seaborn
*   **3주차: 지도 학습 기초 - 회귀(Regression)**
    *   선형 회귀(Linear Regression)
    *   최적화 원리: 경사하강법(Gradient Descent)
*   **4주차: 지도 학습 기초 - 분류(Classification)**
    *   알고리즘: 로지스틱 회귀, k-NN
    *   의사결정 트리(Decision Tree)
*   **5주차: 인공지능 윤리 및 입문 프로젝트**
    *   AI 윤리와 편향성
    *   미니 프로젝트: 붓꽃(Iris) 분류 또는 타이타닉 생존자 예측

### [Course 2] 머신러닝 중급자 과정: "심화 알고리즘과 실전 품질관리"
딥러닝, 비지도 학습, 모델 성능 최적화 기법을 다루는 심화 과정.

*   **1단계: 모델 최적화 및 평가 지표 심화**
    *   교차 검증(K-Fold), GridSearchCV
    *   정밀 평가: Precision, Recall, F1 Score, ROC-AUC
*   **2단계: 신경망과 딥러닝 기초**
    *   인공신경망(ANN), 역전파(Back Propagation)
    *   활성화 함수: ReLU, Softmax
*   **3단계: 컴퓨터 비전 및 자연어 처리(NLP)**
    *   이미지 인식: CNN(합성곱 신경망)
    *   텍스트 분석: 문자열 처리, 형태소 분석
*   **4단계: 비지도 학습 및 차원 축소**
    *   군집화: K-Means
    *   차원 축소: PCA(주성분 분석)
*   **5단계: 데이터 품질관리 및 실전 시스템**
    *   데이터 생애주기 품질 관리
    *   추천 시스템(협업 필터링), 강화 학습 기초

### [Course 3] 머신러닝 중급 및 실무 과정 통합 커리큘럼: "딥러닝 심화와 데이터 품질 관리"
기존 입문-중급 과정을 넘어, 딥러닝 심화, 비정형 데이터 처리, 그리고 실무급 데이터 품질 관리에 집중하는 통합 과정.

*   **1단계: 앙상블 학습과 고성능 모델링**
    *   트리 기반 앙상블: Random Forest, XGBoost, LightGBM 원리 및 튜닝
    *   심화 분류: SVM, MLP 구조 학습
    *   정밀 성능 분석: Confusion Matrix, AUROC, Precision-Recall Curve
*   **2단계: 인공신경망과 딥러닝 기초**
    *   신경망 구조: 뉴런, 레이어, 가중치, 역전파(Back Propagation)
    *   활성화/최적화: ReLU, Softmax, Advanced Optimization
    *   프레임워크: Tensorflow / PyTorch 실습
*   **3단계: 비정형 데이터 처리 (이미지 및 자연어)**
    *   컴퓨터 비전: CNN (Convolution, Pooling) 및 이미지 분류
    *   NLP: 토큰화, 임베딩, RNN/LSTM, Transformer 기초, LLM 개념
*   **4단계: 비지도 학습 및 특수 시스템**
    *   군집화/차원축소: K-Means, PCA
    *   추천 시스템: 협업 필터링 vs 콘텐츠 기반 필터링
    *   이상 탐지: Anomaly Detection (가우시안 분포 등)
*   **5단계: 인공지능 학습용 데이터 품질 관리 (실무 특화)**
    *   데이터 생애주기: 획득-정제-라벨링 및 공정별 품질 점검(NIA 가이드라인)
    *   적합성/유효성: 편향성 분석 및 참값(Ground Truth) 검증
*   **6단계: 생성형 AI 응용 및 배포**
    *   RAG & LangChain: 외부 지식 결합 및 챗봇 설계
    *   프롬프트 엔지니어링: 할루시네이션 제어
    *   웹 서비스 배포: Streamlit 활용


### [Course 4] 머신러닝 실무 심화 및 최신 트렌드: "MLOps와 LLM"
실험 관리부터 배포까지의 MLOps 전체 파이프라인과 최신 LLM 기술을 다루는 전문가 과정.

*   **1단계: MLOps와 실험 관리 (Engineering)**
    *   실험 추적: MLflow, Weights & Biases (W&B)
    *   데이터 버전 관리: DVC (Data Version Control)
*   **2단계: 딥러닝 실전과 전이 학습 (Transfer Learning)**
    *   Pre-trained Model 활용: HuggingFace Transformers 라이브러리
    *   Fine-tuning: BERT/ResNet 등 거대 모델을 내 데이터에 맞게 재학습
*   **3단계: 최신 LLM 생태계 (GenAI Advanced)**
    *   벡터 데이터베이스: RAG 핵심 저장소 (ChromaDB, Pinecone)
    *   Local LLM: Ollama, LM Studio 활용
    *   프롬프트 심화: Chain-of-Thought (CoT), Few-shot Engineering
*   **4단계: 실전 모델 배포 (Serving)**
    *   API 개발: FastAPI로 예측 서버 구축
    *   컨테이너화: Docker 기초 및 모델 패키징

## 🏗️ Structure
- `src/`: 소스 코드 및 모듈
- `docs/`: 학습 계획 및 이론 정리 문서
- `notebooks/`: Jupyter Notebook 실습 파일 (`.ipynb`)
- `data/`: 학습용 데이터셋 (Git Ignore 권장)
- `references/`: 참고 자료 (논문, PDF 등)
- `tests/`: 테스트 코드
- `scripts/`: 유틸리티 스크립트
