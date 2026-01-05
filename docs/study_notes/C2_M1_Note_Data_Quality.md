# Study Note: Data Quality Engineering

**Course**: Course 2 (Master Class)
**Related Plan**: [C2_M1_Plan_Advanced_ML.md](../plans/C2_M1_Plan_Advanced_ML.md)

---

## 1. 🔍 Theory (Textbook Deep Dive)
### 1.1 Data Quality Dimensions (데이터 품질 6대 원칙)
좋은 데이터란 무엇인가? NIA(한국지능정보사회진흥원) 가이드라인 기준:

1.  **완전성 (Completeness)**: 필수 항목에 누락(Null)이 없어야 함.
2.  **유일성 (Uniqueness)**: 데이터가 중복되지 않고 유일해야 함. (PK 제약조건)
3.  **유효성 (Validity)**: 정의된 형식(Format)과 도메인(범위)을 지켜야 함. (예: 날짜 형식 YYYY-MM-DD)
4.  **일관성 (Consistency)**: 데이터 간의 관계가 논리적으로 모순이 없어야 함. (예: 총계 = 부분의 합)
5.  **정확성 (Accuracy)**: 실세계의 사실 값과 일치해야 함.
6.  **무결성 (Integrity)**: 데이터 저장소 내에서 참조 관계가 깨지지 않아야 함.

### 1.2 Data Profiling
*   데이터를 본격적으로 분석하기 전에, 데이터의 통계적 분포, 결측률, 최빈값 등을 빠르게 훑어보는 과정.
*   도구: `pandas-profiling (ydata-profiling)`, `sweetviz` 등.

## 2. 🧪 Experiment & Insight
*   **Experiment**: 품질 검증 함수 `check_quality(df)` 구현.
*   **Insight**:
    *   품질 문제는 단순히 기술적 에러(Type Error)뿐만 아니라, 비즈니스 로직 에러(재고가 마이너스)도 포함된다.
    *   자동화된 품질 대시보드가 있으면 파이프라인 모니터링이 쉬워진다.

## 3. 🔨 Break & Fix Log
*   **Break**: 의도적으로 중복 데이터(Duplicate) 생성 후 학습.
*   **Result**: Train/Test 셋에 같은 데이터가 들어가면(Data Leakage), 테스트 점수가 비정상적으로 높게 나와 과적합을 인지하지 못하게 된다.
