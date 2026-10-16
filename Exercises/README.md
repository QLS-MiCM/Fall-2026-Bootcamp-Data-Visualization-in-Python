# Exercises

| Folder | Contents |
|---|---|
| `scripts/` | **Student notebook** `DataVisualizationInPython.ipynb` – explanations, demo code and ✏️ exercises with `___` blanks to fill in |
| `solutions/` | **Solutions notebook** `DataVisualizationInPython_solutions.ipynb` – same notebook, all exercises solved and executed |
| `data/` | Input data (GSE164073): metadata, raw counts, log2 CPM, differential expression results |
| `results/` | Example outputs exported by the solutions notebook: `Figure1_cornea_CoV2.{pdf,svg,png}`, `Exercise6.{pdf,svg,png}` (180 mm wide, 600 dpi PNG) |
| `data_scripts/` | `prepare_data.py` (data), `build_notebooks.py` (student + solutions notebooks from one source), `build_outline.py` (outline) |

**Order:** run the notebook top to bottom. Each module ends with an exercise. Later cells only depend on the *demo* cells (not on your exercise answers), so if you get stuck you can skip an exercise and continue – just make sure every non-exercise cell has been run. Cells marked *(optional)* can be skipped.

**Paths:** in Colab, data are read straight from GitHub. Locally, start Jupyter in `Exercises/scripts/` (data are read from `../data/`); exported figures go to `figures/` next to the notebook.

**Comment:** edit `data_scripts/build_notebooks.py`, not the `.ipynb` files, then run
`python Exercises/data_scripts/build_notebooks.py` and re-execute the solutions notebook
(`jupyter nbconvert --to notebook --execute --inplace Exercises/solutions/DataVisualizationInPython_solutions.ipynb`, run from inside `Exercises/solutions/`).
