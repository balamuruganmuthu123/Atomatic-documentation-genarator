"""
Master runner — combines all chapter files and generates the final Word document.
Run:  python run_report.py
"""
import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Execute all parts in order, sharing the same global namespace
g = {}
for fname in ["generate_report.py", "ch1.py", "ch2.py", "ch3.py",
              "ch4.py", "ch5.py", "ch6.py", "ch7_end.py"]:
    print(f"  Loading {fname} ...")
    with open(fname, "r", encoding="utf-8") as f:
        exec(compile(f.read(), fname, "exec"), g)

print("\nDone! Open AI_DOC_GENERATOR_REPORT.docx")
