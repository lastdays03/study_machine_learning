
import os
import subprocess
import glob

# Defines which folders to process order
target_folders = [
    "notebooks/course_2",
    "notebooks/course_1", 
    "notebooks"  # For extra_*.ipynb
]

def execute_notebook(filepath):
    print(f"▶️ Executing {filepath}...")
    try:
        # Run nbconvert
        # Timeout 60s per cell is usually enough for simple plots
        cmd = [
            "jupyter", "nbconvert", 
            "--to", "notebook", 
            "--execute", 
            "--inplace", 
            "--ExecutePreprocessor.timeout=60",
            filepath
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Success: {filepath}")
            return True, None
        else:
            print(f"❌ Failed: {filepath}")
            # print(result.stderr) # Optionally print error
            return False, result.stderr
            
    except Exception as e:
        print(f"❌ Error invoking command: {e}")
        return False, str(e)

# Main Loop
report = []
for folder in target_folders:
    # Get all .ipynb in this folder (non-recursive to avoid duplicates if nested)
    # Using glob
    files = glob.glob(os.path.join(folder, "*.ipynb"))
    
    for file in sorted(files):
        # Skip hidden
        if os.path.basename(file).startswith("."):
            continue
            
        success, err = execute_notebook(file)
        report.append((file, success, err))

# Final Report
print("\n" + "="*60)
print("FINAL EXECUTION REPORT")
print("="*60)
for file, success, err in report:
    status = "✅ OK" if success else "❌ FAIL"
    print(f"{status} | {file}")
    if not success and err:
        # Print last few lines of error
        lines = err.strip().split('\n')
        print(f"    Error: {lines[-1] if lines else 'Unknown'}") 
