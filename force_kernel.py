
import json
import os
import glob

# Recursive search for all ipynb files
target_root = "notebooks"
files = [y for x in os.walk(target_root) for y in glob.glob(os.path.join(x[0], '*.ipynb'))]

new_kernelspec = {
    "display_name": "Python (Study ML)",
    "language": "python",
    "name": "study_ml_venv"
}

for nb_path in files:
    if ".ipynb_checkpoints" in nb_path:
        continue
    
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Update metadata
        # Ensure metadata exists
        if 'metadata' not in nb:
            nb['metadata'] = {}
        
        nb['metadata']['kernelspec'] = new_kernelspec
        
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=4, ensure_ascii=False)
        print(f"Updated kernel in {nb_path}")
        
    except Exception as e:
        print(f"Failed to update {nb_path}: {e}")
