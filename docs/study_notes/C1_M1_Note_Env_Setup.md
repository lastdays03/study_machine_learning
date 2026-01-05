# 1주차 Session 2: 로컬 데이터 사이언스 환경 구축

> **목표**: M1 Max의 강력한 성능을 활용하기 위해 로컬 Python 가상환경을 구축하고, VSCode에서 Jupyter Notebook을 실행하는 환경을 만듭니다.

## 1. 가상환경(Virtual Environment) 구성

프로젝트마다 패키지 버전이 꼬이는 것을 방지하기 위해 **가상환경**을 필수적으로 사용합니다.

### 1) 터미널 열기
VSCode 하단 터미널(`Cmd + J`)을 열고 현재 프로젝트 루트(`study_machine_learning`)인지 확인합니다.

### 2) 가상환경 생성 및 활성화
```bash
# 가상환경(.venv 폴더) 생성
python3 -m venv .venv

# 가상환경 활성화 (Mac/Linux)
source .venv/bin/activate
```
*   터미널 프롬프트 앞에 `(.venv)`가 표시되면 성공입니다.

---

## 2. 필수 라이브러리 설치

데이터 분석과 머신러닝에 필요한 핵심 패키지들을 설치합니다.

```bash
# pip 업그레이드 (권장)
pip install --upgrade pip

# 필수 패키지 설치
pip install numpy pandas matplotlib seaborn scikit-learn ipykernel
```
*   `numpy`, `pandas`: 데이터 처리
*   `matplotlib`, `seaborn`: 데이터 시각화
*   `scikit-learn`: 머신러닝 알고리즘
*   `ipykernel`: Jupyter Notebook 커널

---

## 3. VSCode & Jupyter 연동

### 1) 확장 프로그램 설치
VSCode 좌측 Extension 탭에서 다음 항목들이 설치되어 있는지 확인합니다.
*   **Python** (Microsoft)
*   **Jupyter** (Microsoft)
*   *(Optional)* **Google Colab** (Google) - 원격 런타임 연결용

### 2) 첫 번째 노트북 만들기
1.  `notebooks` 폴더 안에 `01_env_test.ipynb` 파일을 생성합니다.
2.  파일을 열면 우측 상단에 **"Kernel"** 또는 **"Select Kernel"** 버튼이 보입니다.
3.  클릭 후 **'Python Environments'** -> **'.venv (Python 3.x.x)'**를 선택합니다.
    *   *Tip: 'Recommended' 태그가 붙은 것을 찾으세요.*

---

## 4. 실습: Hello World & GPU 확인

`01_env_test.ipynb`의 첫 셀에 아래 코드를 입력하고 실행(`Shift + Enter`) 해보세요.

```python
import sys
import platform
import torch  # 만약 torch를 설치하지 않았다면 import error가 날 수 있으니 건너뛰거나 pip install torch로 설치

print(f"Python Version: {sys.version}")
print(f"Platform: {platform.platform()}")
print("Hello, Machine Learning World!")

# M1 Mac GPU 가속(MPS) 확인 (PyTorch 설치 시)
# print(f"MPS Available: {torch.backends.mps.is_available()}")
```

## 5. (Option) Google Colab 연결하기
로컬 자원이 부족하거나 Colab 전용 기능을 써야 할 때 사용합니다.

1.  `.ipynb` 파일 우측 상단 커널 선택기 클릭.
2.  **'Google Colab'** 선택.
3.  Google 로그인 후 'Connect to runtime' -> 'T4 GPU' (또는 CPU) 선택.
4.  이제 코드가 내 컴퓨터가 아닌 Google 서버에서 실행됩니다.

---

## 📝 Practice Activity
위 과정을 따라 `notebooks/01_env_test.ipynb`를 완성하고, 해당 파일의 스크린샷이나 실행 결과를 확인하세요.
다음 단계로 넘어가기 전, **모든 셀이 에러 없이 실행**되어야 합니다.
