# Study Note: NLP & RNN Sequence Modeling

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M2_Plan_Deep_Learning.md](../plans/C2_M2_Plan_Deep_Learning.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 Sequence Modeling
*   **순서(Order)**가 중요한 데이터(텍스트, 주가, 음성)를 다루기 위한 모델링.
*   $t$ 시점의 출력은 $t$ 시점의 입력뿐만 아니라 $t-1$ 시점까지의 상태(Context)에 영향을 받는다.

### 1.2 RNN의 문제와 LSTM
*   **Vanishing Gradient (기울기 소실)**: RNN은 시간을 거슬러 올라가며 역전파할 때, 곱하기 연산이 반복되어 기울기가 0이 되어버리는 문제가 심각함. (옛날 기억을 못함)
*   **LSTM (Long Short-Term Memory)**:
    *   **Cell State ($C_t$)**: 정보가 흐르는 고속도로. 간섭 없이 오래 기억을 전달.
    *   **Gates**: 정보를 얼마나 열고 닫을지 조절하는 수도꼭지.
        *   **Forget Gate**: 불필요한 과거 기억 삭제.
        *   **Input Gate**: 새로운 중요 정보 저장.
        *   **Output Gate**: 현재 시점의 출력 결정.

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M2_Exp_RNN_Sentiment.ipynb`
*   **Insight**: 
    *   Bi-directional RNN: 문장을 앞에서만 읽는 게 아니라 뒤에서도 읽으면 문맥 파악이 더 정확해진다.
    *   Embedding: 단어를 의미 벡터로 바꾸는 것이 NLP의 시작과 끝이다.

## 3. 🔨 Break & Fix Log
*   **Break**: 시퀀스 길이를 1로 설정 (순서 정보 제거).
*   **Result**: 문맥 파악 불가능. 단순 키워드 매칭 수준으로 전락.
