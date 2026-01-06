import nbformat
import re
import os

notebooks = [
    "docs/notebooks/EDA_01_heart_failure_study.ipynb",
    "docs/notebooks/EDA_02_heart_failure_prediction.ipynb",
    "docs/notebooks/EDA_03_heart_failure_revisit.ipynb"
]

metrics_pattern = r"(Accuracy|F1|Recall|AUC|F1-Score|Precision):?\s*(\d+\.\d+)"
model_name_pattern = r"\[(.*?)\]"

results = {}

for nb_path in notebooks:
    if not os.path.exists(nb_path):
        print(f"Skipping {nb_path} (Not found)")
        continue
    
    print(f"\n{'='*20} Processing {nb_path} {'='*20}")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        
    nb_metrics = {}
    last_model_name = "Unknown"
    
    for cell in nb.cells:
        if cell.cell_type == 'code':
            if 'outputs' in cell:
                for output in cell['outputs']:
                    if 'text' in output:
                        text = output['text']
                        # Try to find model name lines like "[Random Forest]" or "--- Random Forest ---"
                        name_match = re.search(r"--- (.*?) ---|\[(.*?)\]", text)
                        if name_match:
                            last_model_name = name_match.group(1) or name_match.group(2)
                            if last_model_name not in nb_metrics:
                                nb_metrics[last_model_name] = {}
                        
                        # Find metrics
                        matches = re.findall(metrics_pattern, text)
                        for metric, value in matches:
                            if last_model_name:
                                if last_model_name not in nb_metrics:
                                    nb_metrics[last_model_name] = {}
                            nb_metrics[last_model_name][metric] = value
                            print(f"Found {metric}: {value} for {last_model_name}")
                    
                    # Also check for stream output which is common in print()
                    if output.get('name') == 'stdout':
                         text = output['text']
                         name_match = re.search(r"--- (.*?) ---|\[(.*?)\]", text)
                         if name_match:
                            last_model_name = name_match.group(1) or name_match.group(2)
                            if last_model_name not in nb_metrics:
                                nb_metrics[last_model_name] = {}
                         
                         matches = re.findall(metrics_pattern, text)
                         for metric, value in matches:
                            if last_model_name:
                                nb_metrics[last_model_name][metric] = value
                            print(f"Found {metric}: {value} for {last_model_name}")

    results[nb_path] = nb_metrics

print("\n\n=== Extraction Summary ===")
import json
print(json.dumps(results, indent=2))
