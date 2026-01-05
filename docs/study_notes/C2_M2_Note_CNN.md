# Study Note: Computer Vision (CNN)

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M2_Plan_Deep_Learning.md](../plans/C2_M2_Plan_Deep_Learning.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 CNN (Convolutional Neural Network)
*   **Idea**: 이미지는 픽셀 하나하나가 독립적인 게 아니라, 주변 픽셀과의 관계(공간 정보)가 중요하다.
*   **Convolution Layer**:
    *   **Filter (Kernel)**: 특정 패턴(가로선, 세로선, 동그라미 등)을 탐지하는 작은 윈도우.
    *   **Feature Map**: 필터가 이미지를 훑으며 만들어낸 '특징 지도'.
*   **Pooling Layer**:
    *   **Max Pooling**: 해당 영역에서 가장 강한 특징값 하나만 남김. (노이즈 제거, 연산량 감소, 이동 불변성)

### 1.2 주요 개념
*   **Stride**: 필터가 이동하는 보폭. 클수록 출력 크기가 작아짐.
*   **Padding**: 가장자리의 정보를 보존하기 위해 테두리에 0을 채우는 기법.
*   **Receptive Field (수용 영역)**: 출력 레이어의 한 픽셀이 입력 이미지의 얼마만큼의 영역을 보고 있는가? 깊게 쌓을수록 넓어진다.

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M2_Project_CNN.ipynb`
*   **Insight**: 
    *   낮은 층(Low-level)은 선/점 같은 단순한 특징을, 높은 층(High-level)은 눈/코/입 같은 복합적인 특징을 배운다.
    *   전이 학습(Transfer Learning): 이미 ImageNet으로 학습된 모델(ResNet 등)을 가져와 내 데이터에 맞게 튜닝하는 것이 맨땅 학습보다 훨씬 강력하다.

## 3. 🔨 Break & Fix Log
*   **Break**: 채널(RGB) 순서를 섞어버림.
*   **Result**: 모델 성능 저하. 색상 정보도 중요한 특징 중 하나임.
