import nbformat
import glob
import os

notebooks = [
    "docs/notebooks/EDA_01_heart_failure_prediction.ipynb",
    "docs/notebooks/EDA_01_heart_failure_study.ipynb",
    "docs/notebooks/EDA_02_heart_failure_prediction.ipynb"
]

for nb_path in notebooks:
    if not os.path.exists(nb_path):
        print(f"Skipping {nb_path} (Not found)")
        continue
        
    print(f"\n{'='*20} Comparing {nb_path} {'='*20}")
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        print(f"Total Cells: {len(nb.cells)}")
        
        # Print first 3 markdown cells to check language/style
        md_cells = [c for c in nb.cells if c.cell_type == 'markdown']
        print(f"Markdown Cells: {len(md_cells)}")
        for i, cell in enumerate(md_cells[:3]):
            print(f"--- MD Cell {i} ---")
            print(cell.source[:200] + "..." if len(cell.source) > 200 else cell.source)
            
        # Print imports from first code cell to check structure
        code_cells = [c for c in nb.cells if c.cell_type == 'code']
        if code_cells:
            print("\n--- First Code Cell (Imports?) ---")
            print(code_cells[0].source[:200])

    except Exception as e:
        print(f"Error reading {nb_path}: {e}")
