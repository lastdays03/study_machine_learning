import nbformat as nbf
import os

# Define the notebook structure
nb = nbf.v4.new_notebook()

# Title and Objective
text_intro = """# Seoul Real Estate & Infrastructure Analysis (2025)

## 1. Objective
Analyze the relationship between **2025 Seoul Real Estate Prices** and **Infrastructure Accessibility** (Bus, Subway, Hospital, School, Park).

## 2. Check Environment & Font
"""

code_font = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import os

# OS check and Font setting
system_name = platform.system()
if system_name == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
elif system_name == 'Windows': # Windows
    plt.rc('font', family='Malgun Gothic')
else: # Linux
    plt.rc('font', family='NanumGothic')

# Minus sign fix
plt.rcParams['axes.unicode_minus'] = False

print(f"OS: {system_name}")
"""

text_load = """## 3. Data Loading
Load the 6 datasets using `cp949` encoding.
"""

code_load = """# Paths
data_dir = '../../data'

files = {
    'bus': '버스.csv',
    'hospital': '병원.csv',
    'real_estate': '서울시 부동산 실거래가 정보 2025.csv',
    'subway': '지하철.csv',
    'school': '학교.csv',
    'park': '공원.csv'
}

dfs = {}

for key, filename in files.items():
    path = os.path.join(data_dir, filename)
    try:
        dfs[key] = pd.read_csv(path, encoding='cp949')
        print(f"Loaded {key}: {dfs[key].shape}")
    except Exception as e:
        print(f"Failed to load {key}: {e}")

# Quick Check
for key, df in dfs.items():
    print(f"\\n--- {key} ---")
    print(df.head(2))
"""

text_preprocess = """## 4. Preprocessing & Feature Engineering (Gu-level Aggregation)

### 4.1. Real Estate (Target)
- Filter valid transactions.
- Group by `자치구명` (District) and calculate **Average Transaction Price**.
"""

code_preprocess_real_estate = """df_re = dfs['real_estate']

# Check columns
print(df_re.columns)

# Filter for Seoul (Code 11...) if needed, but data seems to be Seoul only based on title
# Group by '자치구명'
# Ensure price column is numeric. '물건금액(만원)'
df_re_gu = df_re.groupby('자치구명')['물건금액(만원)'].mean().reset_index()
df_re_gu.rename(columns={'물건금액(만원)': 'Avg_Price'}, inplace=True)
print(df_re_gu.head())
"""

text_preprocess_infra = """### 4.2. Infrastructure Counts by Gu
- Parse addresses to extract `자치구명`.
- Count facilities per Gu.
"""

code_preprocess_infra = """# Function to extract Gu from address
def extract_gu(address):
    if pd.isna(address):
        return None
    # Address format usually "서울(특별시) XX구 ..."
    tokens = str(address).split()
    for token in tokens:
        if token.endswith('구'):
            return token
    return None

# 1. Hospital
df_hosp = dfs['hospital']
df_hosp['Gu'] = df_hosp['도로명주소'].apply(extract_gu)
hosp_counts = df_hosp.groupby('Gu').size().reset_index(name='Hospital_Count')

# 2. Subway
df_sub = dfs['subway']
# Use '도로명주소' or '지번주소'
df_sub['Gu'] = df_sub['도로명주소'].apply(extract_gu)
sub_counts = df_sub.groupby('Gu').size().reset_index(name='Subway_Count')

# 3. School
df_school = dfs['school']
df_school['Gu'] = df_school['소재지도로명주소'].apply(extract_gu)
school_counts = df_school.groupby('Gu').size().reset_index(name='School_Count')

# 4. Park
df_park = dfs['park']
# Park often has missing addresses, check '소재지도로명주소' or '소재지지번주소'
df_park['Gu'] = df_park['소재지도로명주소'].fillna(df_park['소재지지번주소']).apply(extract_gu)
park_counts = df_park.groupby('Gu').size().reset_index(name='Park_Count')

# 5. Bus
# Bus data (dfs['bus']) often lacks simple address. It has '정류장명', '위도', '경도'.
# Mapping lat/lon to Gu requires reverse geocoding or spatial join.
# For Phase 1, we might SKIP Bus count by Gu unless we have a mapping logic.
# Let's try to see if '도시명' or '관리도시명' helps, or simply omit for Gu-level summary if too complex without shapefiles.
print("Bus data columns:", dfs['bus'].columns)
# Use '도시명' to see if we can filter Seoul
print(dfs['bus']['도시명'].unique()[:10])
"""

text_merge = """## 5. Merging Data
Combine Real Estate Prices with Infrastructure Counts.
"""

code_merge = """# Base: Real Estate Gu
merged_df = df_re_gu.copy()

# Merge all counts
for df_count in [hosp_counts, sub_counts, school_counts, park_counts]:
    # Ensure Gu naming is consistent (e.g. '노원구')
    merged_df = pd.merge(merged_df, df_count, left_on='자치구명', right_on='Gu', how='left')
    # Drop the redundant 'Gu' column from the right immediately
    merged_df.drop(columns=['Gu', 'Gu_x', 'Gu_y'], inplace=True, errors='ignore')

# Fill NaN with 0 (no facility found)
merged_df.fillna(0, inplace=True)
print(merged_df.head())
"""

text_eda = """## 6. EDA & Correlation Analysis
"""

code_eda = """# Correlation Matrix
corr_matrix = merged_df.select_dtypes(include=[np.number]).corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation: Real Estate Price vs Infrastructure')
plt.show()

# Pairplot
sns.pairplot(merged_df)
plt.show()
"""

# cells
nb.cells = [
    nbf.v4.new_markdown_cell(text_intro),
    nbf.v4.new_code_cell(code_font),
    nbf.v4.new_markdown_cell(text_load),
    nbf.v4.new_code_cell(code_load),
    nbf.v4.new_markdown_cell(text_preprocess),
    nbf.v4.new_code_cell(code_preprocess_real_estate),
    nbf.v4.new_markdown_cell(text_preprocess_infra),
    nbf.v4.new_code_cell(code_preprocess_infra),
    nbf.v4.new_markdown_cell(text_merge),
    nbf.v4.new_code_cell(code_merge),
    nbf.v4.new_markdown_cell(text_eda),
    nbf.v4.new_code_cell(code_eda)
]

# Save
output_path = 'docs/notebooks/Seoul_Infrastructure_Analysis.ipynb'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Created notebook at {output_path}")
