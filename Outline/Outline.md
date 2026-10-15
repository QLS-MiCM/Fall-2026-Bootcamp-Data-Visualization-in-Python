# Data Visualization in Python

**Workshop Lead:** Zahra Tavakol Hamedani (Instructor) · Sameena Karsan (Facilitator)  
**Context:** Code to Manuscript Bootcamp – Day 1 · Monday, October 26, 2026, 2:30–4:30 pm · McIntyre Room 1027  
**Registration link:** NA  
**Approximate duration:** 2 hours

## Prerequisites

- Basic Python: variables, lists/dictionaries, loops and calling functions.
- Basic pandas: loading a CSV into a DataFrame and selecting rows/columns.
- A Google account to run the notebook in Google Colab (preferred), or a local Python 3 installation (≥ 3.10) with Jupyter, pandas, matplotlib, seaborn, scikit-learn, umap-learn and adjustText.

## Summary

This hands-on session explores the Python data visualization ecosystem, focusing on the relationship between Matplotlib Figure/Axes objects and Seaborn's high-level statistical plotting functions. Using a public bulk RNA-seq dataset (SARS-CoV-2-infected human ocular tissue, GEO GSE164073; the same dataset used on Day 2 in R), participants create quality-control plots, distributions, volcano/MA plots, heatmaps and PCA/t-SNE/UMAP embeddings. They then assemble a multi-panel figure at journal dimensions with a consistent, colour-blind-safe style and export it as vector (PDF/SVG) and high-resolution raster files for Inkscape (Day 4) and LaTeX (Day 5).

## Learning Objectives

1. Explain the Matplotlib Figure/Axes model and use the object-oriented interface to build and customise plots.
2. Reshape data into tidy (long) format and choose between axes-level and figure-level Seaborn functions.
3. Create common biological visualizations: distributions, strip/box plots, volcano and MA plots, (clustered) heatmaps, and PCA/t-SNE/UMAP embeddings.
4. Assemble a multi-panel figure at journal column width with consistent colours, fonts and panel labels.
5. Export figures as editable vector (PDF/SVG) and ≥300 dpi raster files ready for post-processing.

## Content

1. **Module 0 – Setup & the dataset (10 minutes)**
   1. Opening the notebook in Colab; installing umap-learn and adjustText
   1. The GSE164073 dataset: 3 tissues × 2 conditions × 3 donors
      1. Counts, normalised expression, DE results
   1. Defining a project-wide colour-blind-safe palette (Okabe–Ito)
2. **Module 1 – Anatomy of a Matplotlib figure (15 minutes)**
   1. Figure vs Axes; implicit (plt.) vs explicit (fig, ax) interfaces
   1. Bar chart of library sizes; labels, units, colours and custom legends
   1. **Exercise 1 – horizontal bar chart coloured by condition with a median line (5 min)**
3. **Module 2 – Seaborn, tidy data & distributions (20 minutes)**
   1. Wide vs long (tidy) data with melt/merge
   1. Axes-level vs figure-level functions
      1. Per-sample box plots (QC)
      1. Per-sample density curves faceted by tissue (optional)
   1. Showing individual points for small n: bar of means vs box + strip plot
   1. **Exercise 2 – small multiples of four inflammatory genes with catplot (5 min)**
4. **Module 3 – Relationships: scatter, MA & volcano plots (20 minutes)**
   1. Volcano plot: thresholds, colour by DE status, non-overlapping gene labels (adjustText)
   1. Rasterising dense point layers inside vector figures
   1. **Exercise 3 – MA plot (5 min)**
5. **Module 4 – Heatmaps & clustered heatmaps (15 minutes)**
   1. Choosing colour maps: sequential vs diverging; avoiding rainbow
   1. Sample–sample correlation heatmap (optional)
   1. Clustered heatmap of variable genes with z-scores and annotation colour bars
   1. Pitfall: heatmaps of DE-selected genes always separate the groups (circular analysis)
   1. **Exercise 4 – clustered heatmap of the top 30 DE genes in cornea (5 min)**
6. **Module 5 – Dimensionality reduction: PCA, t-SNE, UMAP (15 minutes)**
   1. Intuition only: what each method preserves and how to read the axes
   1. Side-by-side embeddings using hue (tissue) and style (condition)
   1. Within-tissue PCA: the input decides which effect a PCA can show
   1. **Exercise 5 (optional / live demo) – sensitivity of t-SNE to perplexity; what to report in Methods (3 min)**
7. **Module 6 – Multi-panel figures & high-resolution export (20 minutes)**
   1. Journal sizing in mm, paper-style rcParams, subplot_mosaic layouts and panel labels
   1. Combining a clustered heatmap inside a layout (SciPy ordering + sns.heatmap)
   1. Exporting PDF/SVG with editable text and a 600 dpi PNG; checking size and fonts
   1. Downloading figures from Colab for Day 4
   1. **Exercise 6 – build and export a 3-panel figure for Day 4 (8 min; can be finished after class)**
8. **Wrap-up – publication-figure checklist, next sessions & feedback (5 minutes)**
