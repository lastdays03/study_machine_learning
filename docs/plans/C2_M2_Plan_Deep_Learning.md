# 학습 계획서 (Study Plan): Course 2 Module 2 - Deep Learning Foundations

**Status**: 📅 Planned
**Created**: 2026-01-05
**Goal**: 딥러닝의 기초 원리(역전파)를 이해하고, 비정형 데이터(이미지, 텍스트) 처리를 위한 핵심 아키텍처(CNN, RNN)를 구현한다.

---

## 🎯 핵심 목표 (Deep Objective)
**"From Structured to Unstructured"**
- [ ] What: Neural Network, CNN(이미지), RNN(시계열/텍스트).
- [ ] Why: 정형 데이터(엑셀)를 넘어 이미지와 자연어를 이해하는 AI를 만들기 위해.
- [ ] How: [PyTorch/TensorFlow 기초, CS231n 강의 요약]

---

## 📅 커리큘럼 (Curriculum)

### Session 1: 신경망의 재발견 (Neural Networks)
**Focus**: Backpropagation & Optimization

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Backpropagation**: "미분의 연쇄 법칙(Chain Rule)"을 5단계로 쪼개서 설명하기.
    - [ ] **Activation Function**: ReLU가 Sigmoid보다 왜 학습이 잘 되는가? (Vanishing Gradient 문제).
    - [ ] **Feynman Summary**: 신경망 학습 과정을 "산에서 눈 가리고 내려오기(Gradient Descent)"로 비유.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: Learning Rate를 극단적으로 트윅(너무 크거나 작게)하여 Loss 발산/정체 현상 재현.
    - [ ] **Log**: Optimizer(SGD vs Adam) 변경에 따른 수렴 속도 차이 기록.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M2_Exp_NN_Basic.ipynb` 생성 (MNIST 손글씨 분류).

### Session 2: 컴퓨터 비전의 눈 (Computer Vision & CNN)
**Focus**: Convolution, Pooling, ResNet

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Convolution**: 필터(Filter)가 이미지를 훑으며 특징(Feature)을 뽑아내는 과정 설명.
    - [ ] **Pooling**: 정보 압축과 불변성(Invariance)의 의미.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: CNN 층을 너무 깊게 쌓거나 필터 수를 줄여서 정보 손실 유도.
    - [ ] **Log**: Overfitting 발생 시 Dropout 추가 전후 성능 비교.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M2_Project_CNN.ipynb` 생성 (CIFAR-10 이미지 분류).

### Session 3: 시퀀스 데이터와 기억 (NLP & RNN)
**Focus**: Word Embedding & RNN/LSTM

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Word Embedding**: 단어를 숫자로 바꿀 때 원-핫 인코딩의 문제점과 Word2Vec의 해결책.
    - [ ] **RNN vs LSTM**: "금붕어 기억력(RNN)"과 "장기 기억(LSTM cell state)"의 차이.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: 긴 문장에서 RNN의 기울기 소실(Vanishing Gradient) 현상 확인.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M2_Exp_RNN_Sentiment.ipynb` 생성 (영화 리뷰 감성 분석).

---

## 📝 학습 로그 (Learning Log / Notes)

### Session 1 Notes (NN)
- 📄 **Detail Note**: [C2_M2_Note_NN_Basic.md](../study_notes/C2_M2_Note_NN_Basic.md)

### Session 2 Notes (CNN)
- 📄 **Detail Note**: [C2_M2_Note_CNN.md](../study_notes/C2_M2_Note_CNN.md)

### Session 3 Notes (RNN)
- 📄 **Detail Note**: [C2_M2_Note_RNN.md](../study_notes/C2_M2_Note_RNN.md)
