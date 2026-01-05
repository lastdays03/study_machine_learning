
import json
import glob

# Notebooks with "NoSuchKernel" error
targets = glob.glob("notebooks/extra_*.ipynb")

for nb_path in targets:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Fix kernelspec to default python3
    nb['metadata']['kernelspec'] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    }
    
    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=4, ensure_ascii=False)
    print(f"Fixed kernel in {nb_path}")
