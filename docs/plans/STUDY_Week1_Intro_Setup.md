# STUDY: 1주차 - 머신러닝 입문 및 환경 설정

> **Topic**: 머신러닝 기초 개념 확립 및 실습 환경(Google Colab) 구축
> **Date**: 2025-12-30
> **Status**: Planning

## 🎯 Goal
1.  머신러닝의 핵심 용어(피처, 레이블, 과적합 등)를 명확히 이해하고 설명할 수 있다.
2.  Google Colab을 사용하여 별도의 설치 없이 Python 데이터 분석 환경을 구축할 수 있다.
3.  머신러닝 학습에 필수적인 기초 통계 및 확률 개념을 정리한다.

## 📚 Curriculum

### Session 1: 머신러닝 개요 및 용어 정복 (Theory)
*   **Key Concepts**:
    *   머신러닝 vs 전통적 프로그래밍
    *   지도 학습(Supervised) vs 비지도 학습(Unsupervised) vs 강화 학습(Reinforcement)
    *   **핵심 용어**: Feature(특성), Label(정답/Target), Training/Test Set, Overfitting(과적합)/Underfitting
*   **Activity**:
    *   용어 정의를 "나만의 언어"로 정리하기.

### Session 2: 로컬 데이터 사이언스 환경 구축 (Practice)
*   **Environment**: Device (M1 Max), Editor (VSCode), Python 3.x
*   **Actions**:
    *   **가상환경 구성**: `python -m venv .venv`로 프로젝트 격리 환경 생성.
    *   **패키지 설치**: `pip`를 사용해 필수 데이터 분석 라이브러리(`numpy`, `pandas`, `matplotlib`, `scikit-learn`, `ipykernel`) 설치.
    *   **VSCode 연동**: VSCode에서 Jupyter Notebook을 생성하고 `.venv` 커널을 연결하여 Hello World 실행.
    *   **Colab 연결 (Optional)**: VSCode Google Colab 확장을 통해 로컬 VSCode에서 원격 Colab 런타임을 사용하는 방법 실습.
    *   **Git 설정**: `.gitignore` 확인 및 환경 설정 파일 관리 방법 습득.

### Session 3: 기초 수학 리터러시 (Theory)
*   **Subjects**:
    *   기술 통계: 평균(Mean), 중앙값(Median), 표준편차(Std Dev).
    *   확률 기초: 확률 분포, 정규 분포의 의미.
*   **Activity**:
    *   간단한 수치 데이터를 보고 통계적 특성을 파악해보기.

## 🧪 Quiz / Challenge
1.  **Quiz**: "과적합(Overfitting)"을 학생에게 설명한다고 가정하고 3문장 이내로 서술하시오.
2.  **Challenge**: Google Colab에서 `numpy`를 사용하여 평균 0, 표준편차 1인 난수 1000개를 생성하고, 평균과 표준편차를 출력하여 검증하는 코드를 작성하시오.
