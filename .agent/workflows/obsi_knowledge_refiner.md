---
description: 기존 지식 노트의 품질을 "골드 스탠다드"로 끌어올리기 위해 구조화, 내용 심화, 연결, 시각화(멀티모달)를 수행하는 워크플로우입니다.
---

# Knowledge Refinement Workflow (Gardener)

이미 작성된 지식 노트(`20_Learning` 내의 파일)를 분석하고 다듬어, 단순한 메모를 **완전한 지식 자산**으로 탈바꿈시킵니다.

### 1단계: 진단 (Diagnosis)
1.  **Input**: 사용자가 지정한 파일 경로 (또는 폴더).
2.  **Analysis Checkpoints**:
    *   **Structure**: 필수 섹션(`Definition`, `Usage`, `Example`) 존재 여부.
    *   **Meta-data**: `Related Project` 링크, 태그 적절성.
    *   **Connectivity**: 연결되지 않은 고립(Orphan) 상태인지 확인.
    *   **Depth**: 내용이 너무 빈약한지 ("한 줄짜리 노트") 확인.

### 2단계: 처방 및 제안 (Prescription)
1.  **Reporting**: 분석 결과를 요약하여 사용자에게 제시합니다.
    *   "이 노트는 '예제'가 부족하고, 'REST API'라는 키워드가 링크되지 않았습니다."
2.  **Suggestion**: 개선할 작업의 범위를 제안합니다.
    *   (A) 포맷 표준화 (Standardization)
    *   (B) 내용 심화 (Elaboration)
    *   (C) 링크 연결 (Interconnection)
    *   (D) 멀티모달 확장 (Multimodal)

### 3단계: 실행 (Execution) - 대화형 진행

#### 모드 A: 표준화 (Standardization)
*   지식 베이스 표준 템플릿에 맞춰 헤더와 프론트매터를 재정렬합니다.
*   누락된 섹션(`## Example` 등)의 뼈대를 생성합니다.

#### 모드 B: 심화 (Elaboration)
*   **Definition**: 개념 정의가 모호하면 명확하게 다시 씁니다. (Explain Like I'm 5 옵션 가능)
*   **Example**: 코드 예제나 실제 사용 사례가 없다면 생성하여 추가합니다.
*   **Comparison**: 혼동하기 쉬운 개념과의 차이점을 설명합니다. (e.g., `Process vs Thread`)

#### 모드 C: 상호 연결 (Interconnection)
*   **Auto-Linking**: 본문 텍스트를 분석하여 `20_Learning` 내에 존재하는 다른 노트 제목과 일치하는 키워드를 찾아 `[[Wikilink]]`로 변환합니다.
*   **Backlinking**: 이 지식이 활용된 원본 프로젝트 파일에 역방향 링크를 추가할지 묻습니다.

#### 모드 D: 멀티모달 확장 (Multimodal Enhancement)
*   텍스트만으로는 부족한 부분을 시각적/구조적 요소로 보강합니다.
    *   **Mermaid Diagram**: 복잡한 프로세스나 계층 구조를 다이어그램 코드로 생성.
    *   **Tables**: 비교 분석표(예: 장단점 비교) 생성.
    *   **Callouts**: 중요 정보, 주의 사항을 Obsidian Callout 블록(`> [!NOTE]`)으로 강조.
    *   **LaTeX**: 수식이나 알고리즘 표기.
    *   **Image Generation**: (필요 시) 추상적 개념에 대한 일러스트 생성 요청.

### 4단계: 검증 (Verification)
1.  **Preview**: 변경된 내용을 사용자에게 보여줍니다 (Diff 또는 전체 뷰).
2.  **Render Check**: 생성된 Markdown(특히 Mermaid나 Callout)이 문법적으로 올바른지 확인합니다.
