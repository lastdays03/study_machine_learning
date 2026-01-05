# Study Note: LLM Fine-Tuning

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M3_Plan_GenAI.md](../plans/C2_M3_Plan_GenAI.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 LLM 학습 3단계
1.  **Pre-training (사전 학습)**:
    *   인터넷의 방대한 텍스트로 "다음 단어 맞추기" 놀이를 하며 언어 모델링 능력 습득. (비용 막대함)
2.  **Fine-tuning (SFT)**:
    *   질문-답변 쌍(Instruction Dataset)을 주어, "사람의 지시를 따르는 법"을 가르침.
3.  **RLHF (인간 피드백 강화학습)**:
    *   윤리적이고 안전한 답변을 하도록 교정.

### 1.2 Efficient Fine-Tuning (PEFT)
*   거대 모델(7B, 70B)의 모든 파라미터를 업데이트하는 건 불가능(GPU 메모리 부족).
*   **LoRA (Low-Rank Adaptation)**:
    *   기존 가중치는 얼리고(Freeze), 옆에 아주 작은 랭크의 행렬 두 개만 붙여서 학습.
    *   적은 VRAM으로도 튜닝 가능하며 성능은 Full Fine-tuning에 준함.

## 2. 🧪 Experiment & Insight
*   **Experiment**: `C2_M3_Project_FineTuning.ipynb`
*   **Insight**: 
    *   데이터의 양보다 질(Quality)이 중요하다. 노이즈가 섞인 1만 개보다, 잘 정제된 100개의 데이터가 낫다.
    *   Catastrophic Forgetting: 튜닝하다가 원래 똑똑했던 지식을 까먹는 현상 주의.

## 3. 🔨 Break & Fix Log
*   **Break**: Learning Rate를 Pre-training 때처럼 높게 잡음.
*   **Result**: 모델의 언어 능력이 파괴되어 횡설수설함.
