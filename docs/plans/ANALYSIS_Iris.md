# Analysis Plan: Iris Species Classification (Deep Learning)

## 1. Context & Goal
- **Dataset**: `iris3.csv` (Multiclass Classification: Setosa, Versicolor, Virginica)
- **Goal**: Classify Iris species using Deep Learning.
- **Key Requirement**: Use **Deep Learning (MLP)**.

## 2. Methodology Screening (The Right Tool)

### 2.1 Metric Selection
- **Primary**: `Accuracy` (Classes are typically balanced in Iris).
- **Auxiliary**: `Confusion Matrix`.

### 2.2 Preprocessing Strategy
- **Target Encoding**: `LabelEncoder` or `to_categorical` (Species: String -> 0, 1, 2 -> One-hot).
- **Scaling**: `StandardScaler`.

### 2.3 Modeling Strategy
- **Key Model**: `Deep Learning (MLP)`
    - **Architecture**:
        - Input: 4 Features.
        - Hidden: Small network (e.g., 16 -> 8) is sufficient.
        - Output: 3 Units (`Softmax` activation).
    - **Loss**: `Sparse Categorical Crossentropy` (if integer labels) or `Categorical Crossentropy` (if one-hot).
    - **Optimizer**: `Adam`.

## 3. Deliverables
- `docs/notebooks/EDA_01_Iris.ipynb`
