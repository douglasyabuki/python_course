import nbformat
import json

# Load your JSON file
with open('lesson195/jupyter_notebook_sample_2.json', 'r', encoding='utf-8') as file:
    notebook_data = json.load(file)

# Validate and convert the JSON data into notebook format
notebook = nbformat.from_dict(notebook_data)

# Save as .ipynb
with open('lesson195/jupyter_notebook_sample_2.ipynb', 'w', encoding='utf-8') as file:
    nbformat.write(notebook, file)

print('Notebook converted successfully!')
