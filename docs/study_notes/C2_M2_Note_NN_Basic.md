# Study Note: Neural Networks & Backpropagation

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M2_Plan_Deep_Learning.md](../plans/C2_M2_Plan_Deep_Learning.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 Neural Network Architecture
*   **Perceptron**: 입력값에 가중치(Weight)를 곱하고 편향(Bias)을 더해, 활성화 함수를 통과시키는 가장 단순한 신경망 단위.
*   **MLP (Multi-Layer Perceptron)**: 퍼셉트론을 여러 층(Hidden Layers) 쌓아 비선형 문제를 해결할 수 있는 구조.
    *   **Universal Approximation Theorem**: 은닉층이 하나라도 있는 신경망은 세상의 어떤 함수라도 근사할 수 있다는 이론.

### 1.2 Backpropagation (역전파)
*   **목표**: Loss(오차)를 최소화하기 위해 각 파라미터($W$)를 얼마나 수정해야 하는지(Gradient)를 구하는 것.
*   **Chain Rule (연쇄 법칙)**:
    *   $rac{\partial Loss}{\partial x} = rac{\partial Loss}{\partial y} \cdot rac{\partial y}{\partial x}$
    *   출력층의 오차를 입력층 방향으로 미분값을 전달하며 기울기를 계산합니다.

### 1.3 Optimization
*   **GD (Gradient Descent)**: 산을 내려가는 가장 기본적인 방법. 전 데이터를 다 써서 느림.
*   **SGD (Stochastic GD)**: 랜덤하게 일부만 보고 내려감. 빠르지만 비틀거림.
*   **Adam**: 관성(Momentum)과 보폭 조절(Adaptive LR)을 합친, 가장 많이 쓰이는 최적화 알고리즘.

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M2_Exp_NN_Basic.ipynb`
*   **Insight**:
    *   **Loss Function**: 회귀는 MSE, 분류는 Cross-Entropy. 목적에 맞는 Loss 선택이 학습의 방향을 결정한다.
    *   초기화(Initialization)를 모두 0으로 하면 학습이 전혀 안 된다. (Symmetry Breaking 필요)

## 3. 🔨 Break & Fix Log
*   **Break**: Learning Rate를 10.0으로 설정.
*   **Result**: Loss가 줄어들지 않고 무한대로 발산(Exploding)하거나 진동함.
