# Study Note: Transformer Architecture

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M3_Plan_GenAI.md](../plans/C2_M3_Plan_GenAI.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 Transformer 혁명
*   **기존의 한계**: RNN은 순차적으로 처리해야 해서 느리고, 거리가 멀면 관계 파악이 힘듦.
*   **Attention Is All You Need**: 순환(Recurrence)을 완전히 버리고, **Attention**만으로 문맥을 파악.

### 1.2 Self-Attention Mechanism
*   **Query, Key, Value**:
    *   도서관 검색 시스템에 비유.
    *   **Query**: "내가 찾고 싶은 것" (예: '그것'이 가리키는 대상)
    *   **Key**: "책의 분류표" (각 단어의 특징)
    *   **Value**: "책의 내용" (단어의 실제 의미 정보)
*   **Scaled Dot-Product Attention**:
    *   Query와 Key의 유사도(Dot Product)를 구하고, 이를 가중치로 하여 Value를 섞는다(Weighted Sum).
*   **Positional Encoding**: 순서 정보가 없으므로, 단어 위치마다 고유한 사인/코사인 값을 더해준다.

### 1.3 Encoder & Decoder
*   **Encoder**: 입력을 이해하고 압축하는 역할 (BERT 계열).
*   **Decoder**: 이해한 것을 바탕으로 다음 단어를 생성하는 역할 (GPT 계열).

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M3_Exp_Attention_Viz.ipynb`
*   **Insight**: 
    *   Multi-Head Attention: 하나의 단어를 여러 관점(문법, 의미, 대명사 지칭 등)에서 동시에 바라보기 위해 헤드를 여러 개 둔다.

## 3. 🔨 Break & Fix Log
*   **Break**: Key와 Value를 랜덤하게 섞음.
*   **Result**: 문맥이 완전히 파괴되어 의미 없는 문장 생성.
