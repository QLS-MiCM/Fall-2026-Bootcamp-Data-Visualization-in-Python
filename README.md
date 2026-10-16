# Data Visualization in Python

**Click one of these to start:**
[![Open student version in Colab](https://img.shields.io/badge/Open%20in%20Colab-Student%20version-blue?logo=googlecolab)](https://colab.research.google.com/github/QLS-MiCM/DataVisualizationInPython/blob/main/Exercises/scripts/DataVisualizationInPython.ipynb)
[![Open solutions version in Colab](https://img.shields.io/badge/Open%20in%20Colab-Solutions%20version-green?logo=googlecolab)](https://colab.research.google.com/github/QLS-MiCM/DataVisualizationInPython/blob/main/Exercises/solutions/DataVisualizationInPython_solutions.ipynb)

## Overview

This 2-hour, hands-on workshop explores the Python data visualization ecosystem, focusing on the relationship between
**Matplotlib** Figure/Axes objects and **Seaborn**'s high-level statistical plotting functions. Working with a real
bulk RNA-seq dataset, we build quality-control plots, distributions, volcano and MA plots, heatmaps and PCA/t-SNE/UMAP
embeddings, and then assemble them into a **multi-panel, publication-ready figure** exported at high resolution.

The figure you export today (PDF/SVG) is the starting point for **Day 4 – Building figures with Inkscape**, and the
same dataset is used on **Day 2 – Data visualization in R (ggplot2)**.

### Learning objectives

By the end of this workshop, you should be able to:

1. Explain the Matplotlib Figure/Axes model and use the object-oriented interface to build and customise plots.
2. Reshape data into tidy (long) format and choose between axes-level and figure-level Seaborn functions.
3. Create common biological visualizations: distributions, strip/box plots, volcano and MA plots, (clustered) heatmaps and PCA/t-SNE/UMAP embeddings.
4. Assemble a multi-panel figure at journal column width with consistent colours, fonts and panel labels.
5. Export figures as editable vector (PDF/SVG) and ≥300 dpi raster files ready for post-processing.

## Requirements

* **Basic Python**: variables, lists/dictionaries, loops, calling functions.
* **Basic pandas**: reading a CSV into a DataFrame, selecting rows and columns.
* To run the exercises, **either**:
  * **(Preferred)** a Google account to run the notebook in [Google Colab](https://colab.research.google.com/) – nothing to install; **or**
  * a local Python ≥ 3.10 installation with Jupyter (JupyterLab, VS Code or PyCharm).
* *(For the rest of the bootcamp: [Inkscape](https://inkscape.org/release/) installed and a free [Overleaf](https://www.overleaf.com/) account.)*

## Software

### Option A – Google Colab (recommended)

1. Click the **Student version** badge above (you may need to sign in to Google).
2. Run the first code cell. It detects Colab, installs the two packages Colab is missing (`umap-learn`, `adjustText`)
   and reads the data directly from this repository – no download needed.
3. Optional: *File → Save a copy in Drive* to keep your work.

### Option B – Local installation

```shell
git clone https://github.com/QLS-MiCM/DataVisualizationInPython.git
cd DataVisualizationInPython
python -m pip install -r requirements.txt      # or: conda install -c conda-forge --file requirements.txt
jupyter lab Exercises/scripts/DataVisualizationInPython.ipynb
```

Packages used: [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/) (≥ 3.8),
[Seaborn](https://seaborn.pydata.org/) (≥ 0.13), [SciPy](https://scipy.org/), [scikit-learn](https://scikit-learn.org/),
[umap-learn](https://umap-learn.readthedocs.io/) and [adjustText](https://adjusttext.readthedocs.io/).

> Run the notebook from inside `Exercises/scripts/` so that the relative data path `../data/` works.
> Exported figures are written to a `figures/` folder next to the notebook.

## Outline

| Module | Topic | Time | Exercise |
|---|---|---|---|
| 0 | Setup & the dataset | 10 min | – |
| 1 | Anatomy of a Matplotlib figure (Figure vs Axes, OO interface) | 15 min | Horizontal bar chart |
| 2 | Seaborn, tidy data & distributions | 20 min | Small multiples with `catplot` |
| 3 | Relationships: scatter, volcano & MA plots | 20 min | MA plot |
| 4 | Heatmaps & clustered heatmaps | 15 min | Heatmap of top DE genes |
| 5 | Dimensionality reduction: PCA, t-SNE, UMAP | 15 min | t-SNE perplexity |
| 6 | Multi-panel figures & high-resolution export | 20 min | Build & export your own figure |
| – | Wrap-up: publication-figure checklist & feedback | 5 min | – |

The full outline is in [`Outline/`](Outline/) and the slides in [`Slides/`](Slides/).

## Repository structure

```
├── README.md
├── requirements.txt
├── Exercises
│   ├── data                     # input data (see below)
│   ├── data_scripts             # scripts that generate the data, notebooks and outline
│   ├── scripts                  # STUDENT notebook (fill in the ___ blanks)
│   ├── solutions                # SOLUTIONS notebook (executed, with outputs)
│   └── results                  # example exported figures (PDF / SVG / PNG)
├── Slides
│   ├── QLS-MiCM_DataVisualizationInPython.pptx / .pdf
│   └── feedback-qr.png
└── Outline
    ├── MiCM - Data Visualization in Python Workshop Outline.docx / .pdf
    └── Outline.md
```

## Data

Bulk RNA-seq of post-mortem human **cornea, limbus and sclera** infected *ex vivo* with SARS-CoV-2 or mock
(3 tissues × 2 conditions × 3 donors = 18 samples; GEO [GSE164073](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164073)).
The count matrix is the one used in the QLS-MiCM [Differential Gene Expression Analysis](https://github.com/QLS-MiCM/Differential-Gene-Expression-Analysis) workshop.

| File | Description |
|---|---|
| `Exercises/data/sample_metadata.csv` | `sample`, `tissue`, `condition` for the 18 samples |
| `Exercises/data/GSE164073_Eye_count_matrix.tsv` | raw read counts (27,946 genes × 18 samples) |
| `Exercises/data/log2cpm_filtered.csv` | log2(CPM + 1) of 13,422 genes with ≥ 1 CPM in ≥ 3 samples |
| `Exercises/data/de_cornea_CoV2_vs_mock.csv` | differential expression in cornea, CoV2 vs mock ([PyDESeq2](https://pydeseq2.readthedocs.io/)) |

All derived files are regenerated with `python Exercises/data_scripts/prepare_data.py`.
The notebooks are generated from a single source with `python Exercises/data_scripts/build_notebooks.py`.

## References

* Eriksen AZ, *et al.* (2021). SARS-CoV-2 infects human adult donor eyes and hESC-derived ocular epithelium. *Cell Stem Cell*. [doi:10.1016/j.stem.2021.04.028](https://doi.org/10.1016/j.stem.2021.04.028)
* Muzellec B, *et al.* (2023). PyDESeq2: a python package for bulk RNA-seq differential expression analysis. *Bioinformatics*. [doi:10.1093/bioinformatics/btad547](https://doi.org/10.1093/bioinformatics/btad547)
* Rougier NP, Droettboom M, Bourne PE (2014). [Ten simple rules for better figures](https://doi.org/10.1371/journal.pcbi.1003833). *PLoS Comput Biol*.
* Crameri F, Shephard GE, Heron PJ (2020). [The misuse of colour in science communication](https://doi.org/10.1038/s41467-020-19160-7). *Nat Commun*.
* Weissgerber TL, *et al.* (2015). [Beyond bar and line graphs: time for a new data presentation paradigm](https://doi.org/10.1371/journal.pbio.1002128). *PLoS Biol*.
* [Matplotlib documentation & cheatsheets](https://matplotlib.org/cheatsheets/) · [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)

*This workshop builds on the QLS-MiCM [Data Processing in Python](https://github.com/QLS-MiCM/DataProcessingInPython),
[Advanced Data Visualization](https://github.com/QLS-MiCM/Advanced-Data-Visualization) and
[Differential Gene Expression Analysis](https://github.com/QLS-MiCM/Differential-Gene-Expression-Analysis) workshops.*

---

*Workshop created as part of the McGill Initiative in Computational Medicine (QLS-MiCM).*
For more information, visit <https://www.mcgill.ca/micm/>. Questions: workshop-micm@mcgill.ca
