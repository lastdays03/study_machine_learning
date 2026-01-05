# Study Note: RAG System & LangChain

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M3_Plan_GenAI.md](../plans/C2_M3_Plan_GenAI.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 RAG (Retrieval-Augmented Generation)
*   **필요성**:
    *   **Hallucination (환각)**: LLM의 거짓말.
    *   **Outdated Knowledge**: 학습 시점(Cut-off) 이후의 정보 모름.
    *   **Private Data**: 회사 내부 문서는 학습 안 되어 있음.
*   **프로세스**: 
    1.  **Indexing**: 문서를 쪼개서(Chunking) 벡터로 변환(Embedding)하여 DB에 저장.
    2.  **Retrieval**: 사용자의 질문과 가장 유사한 문서를 검색.
    3.  **Generation**: [질문 + 검색된 문서]를 프롬프트에 넣어 LLM에게 답변 요청.

### 1.2 Vector Search
*   **Cosine Similarity**: 두 벡터(문장) 사이의 각도를 이용한 유사도 측정. 방향이 비슷하면 의미가 비슷함.
*   **Embedding Model**: 텍스트를 고차원 공간의 좌표로 변환하는 번역기. (OpenAI Ada, HuggingFace BGE 등)

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M3_Project_RAG_Chatbot.ipynb`
*   **Insight**: 
    *   **Semantic Search**: 단순히 단어가 겹치는 게 아니라 '의미'가 같은 문서를 찾을 수 있다. (예: "배고파" <-> "식당 추천해줘")
    *   **Context Window**: LLM이 한 번에 읽을 수 있는 길이에 제한이 있으므로, 관련성 높은 청크만 잘 골라내는 게 핵심.

## 3. 🔨 Break & Fix Log
*   **Break**: Chunk Size를 너무 작게(10자) 설정.
*   **Result**: 문장의 문맥이 다 잘려나가서, 검색은 되지만 LLM이 내용을 이해 못함.
