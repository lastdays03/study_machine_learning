import pandas as pd
import os

data_dir = '/Users/bagjongman/dev/workspace/study/python/study_machine_learning/data'
files = [
    '버스.csv',
    '병원.csv',
    '서울시 부동산 실거래가 정보 2025.csv',
    '지하철.csv',
    '학교.csv',
    '공원.csv'
]

for f in files:
    path = os.path.join(data_dir, f)
    print(f"Loading {f}...")
    try:
        # Try CP949 first (common for Korean CSVs from Windows)
        df = pd.read_csv(path, encoding='cp949')
        print(f"Success with CP949: {len(df)} rows")
        print("Columns:", df.columns.tolist())
        print(df.head(2))
    except Exception as e:
        print(f"Failed with CP949: {e}")
        try:
            df = pd.read_csv(path, encoding='euc-kr')
            print(f"Success with EUC-KR: {len(df)} rows")
            print("Columns:", df.columns.tolist())
        except Exception as e2:
            print(f"Failed with EUC-KR: {e2}")
    print("-" * 50)
