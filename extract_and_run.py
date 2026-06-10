"""Extract code cells from the notebook and write a runnable script."""
import json
import os

notebook_path = os.path.join(os.path.dirname(__file__), 
                             "Customer Segmentation from Marketing Data.ipynb")

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

script_lines = []
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if source.strip():  # skip empty cells
            script_lines.append(source)
            script_lines.append("\n\n")

script = "\n".join(script_lines)

# Fix the hardcoded CSV path to use a relative path
script = script.replace(
    r'r"C:\\Users\\aansh\\OneDrive\\Desktop\\Customer-Segmentation-Analysis-main\\Mall_Customers.csv"',
    'os.path.join(os.path.dirname(__file__), "Mall_Customers.csv")'
)

# Add os import at the top and matplotlib backend for non-interactive
script = "import os\nimport matplotlib\nmatplotlib.use('Agg')  # non-interactive backend\n\n" + script

# Save all figures
script += """
# Save all open figures
import matplotlib.pyplot as plt
for i, fig_num in enumerate(plt.get_fignums()):
    fig = plt.figure(fig_num)
    output_path = os.path.join(os.path.dirname(__file__), f"output_figure_{i+1}.png")
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved figure {i+1} to {output_path}")
print("\\nAll figures saved. Script completed successfully!")
"""

output_path = os.path.join(os.path.dirname(__file__), "run_notebook.py")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(script)

print(f"Script written to: {output_path}")
