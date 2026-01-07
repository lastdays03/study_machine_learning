# Analysis Plan: Pima Indians Diabetes (Deep Learning)

## 1. Context & Goal
- **Dataset**: `pima-indians-diabetes3.csv` (Medical diagnostic data)
- **Goal**: Predict diabetes onset based on diagnostic measures.
- **Key Requirement**: Use **Deep Learning (MLP)** for modeling.

## 2. Methodology Screening (The Right Tool)

### 2.1 Metric Selection
- **Primary**: `F1-Score` (Harmonic mean of Precision and Recall, suitable for medical diagnosis where False Negatives are costly but Precision matters too).
- **Auxiliary**: `ROC-AUC`, `Recall`.

### 2.2 Preprocessing Strategy
- **Sanity Check**:
    - `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI` cannot be 0.
    - **Action**: Replace `0` with `NaN` and impute (Median or KNN).
- **Scaling**:
    - **Method**: `StandardScaler` (Mandatory for Neural Networks to ensure convergence).
- **Feature Engineering**:
    - Logic: BMI categories (Obesity etc.) could be useful, but raw features + Non-linear MLP might capture it.

### 2.3 Modeling Strategy
- **Key Model**: `Deep Learning (MLP)`
    - **Architecture**:
        - Input Layer: 8 Features
        - Hidden Layers: 2~3 Layers (e.g., 32 -> 16 units) with `ReLU` activation.
        - Regularization: `Dropout(0.2)` to prevent overfitting on small data.
        - Output Layer: 1 Unit (`Sigmoid`).
    - **Optimizer**: `Adam`
    - **Loss**: `Binary Crossentropy`
- **Baseline Comparison**: `Logistic Regression` (to justify DL usage).

### 2.4 Validation Strategy
- **Split**: `Stratified K-Fold` (5 Splits) to ensure class distribution balance.
- **Early Stopping**: Monitor `val_loss` to stop training at optimal epoch.

## 3. Deliverables
- `docs/notebooks/EDA_01_PimaIndiansDiabetes.ipynb`: Complete analysis notebook.
- **Insights**: Key risk factors and model performance evaluation.
