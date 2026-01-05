# 학습 계획서 (Study Plan): Course 2 Module 3 - Transformers & GenAI

**Status**: 📅 Planned
**Created**: 2026-01-05
**Goal**: 현대 자연어 처리의 핵심인 트랜스포머 구조를 이해하고, LLM을 활용한 응용 서비스(챗봇, RAG)를 구현한다.

---

## 🎯 핵심 목표 (Deep Objective)
**"Attention Is All You Need"**
- [ ] What: Self-Attention, BERT/GPT 파인튜닝, RAG(검색 증강 생성).
- [ ] Why: 단순 예측 모델을 넘어, 인간의 언어를 이해하고 생성하는 AI를 다루기 위해.
- [ ] How: [HuggingFace 강좌, LangChain 공식 문서]

---

## 📅 커리큘럼 (Curriculum)

### Session 1: 트랜스포머의 심장 (Transformer Architecture)
**Focus**: Attention Mechanism, Encoder-Decoder

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Self-Attention**: "문장 속 단어들이 서로 어떤 관계인지 주목한다"는 의미 설명.
    - [ ] **Multi-Head Attention**: 여러 개의 관점(Head)에서 문장을 분석하는 이유.
    - [ ] **Feynman Summary**: 트랜스포머를 "단어들의 회의 시간"으로 비유.
2.  **Practice (Break & Fix)**
    - [ ] **Break**: Attention Mask를 제거했을 때 Decoder가 미래 단어를 참조(Cheating)하는 현상 확인.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M3_Exp_Attention_Viz.ipynb` 생성 (Attention Score 시각화).

### Session 2: 거인들의 어깨 위에서 (Transfer Learning & LLM)
**Focus**: HuggingFace, Fine-tuning

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Pre-training vs Fine-tuning**: "일반 상식 공부(Pre-training)"와 "전공 심화 공부(Fine-tuning)" 비유.
    - [ ] **Tokenizer**: LLM이 텍스트를 숫자로 쪼개는 방식 (BPE, Subword).
2.  **Practice (Break & Fix)**
    - [ ] **Break**: Tokenizer 설정을 잘못 맞춰(최대 길이 제한 등) 모델 성능이 급락하는 상황 재현.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M3_Project_FineTuning.ipynb` 생성 (BERT로 뉴스 분류하기).

### Session 3: 지식의 확장 (RAG System)
**Focus**: Vector DB, LangChain

#### ✅ 심층 마스터 체크리스트
1.  **Theory (Feynman Test)**
    - [ ] **Embeddings**: 문장의 의미를 벡터 공간 좌표로 변환하는 원리.
    - [ ] **RAG Flow**: 질문 -> 검색(Retriever) -> 문맥 주입(Augment) -> 답변(Generation).
2.  **Practice (Break & Fix)**
    - [ ] **Break**: 엉뚱한 문서(Chunk)가 검색되었을 때 LLM이 환각(Hallucination)을 일으키는 현상 테스트.
3.  **Implementation (Output)**
    - [ ] `notebooks/course_2/C2_M3_Project_RAG_Chatbot.ipynb` 생성 (PDF 문서 기반 Q&A 봇).

---

## 📝 학습 로그 (Learning Log / Notes)

### Session 1 Notes (Transformer)
- 📄 **Detail Note**: [C2_M3_Note_Transformer.md](../study_notes/C2_M3_Note_Transformer.md)

### Session 2 Notes (LLM)
- 📄 **Detail Note**: [C2_M3_Note_LLM_FineTuning.md](../study_notes/C2_M3_Note_LLM_FineTuning.md)

### Session 3 Notes (RAG)
- 📄 **Detail Note**: [C2_M3_Note_RAG.md](../study_notes/C2_M3_Note_RAG.md)
