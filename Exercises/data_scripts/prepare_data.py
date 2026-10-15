"""Prepare the shared workshop dataset (GSE164073) used in the Python (Day 1) and R (Day 2) sessions.

Source: Eriksen et al. (2021) Cell Stem Cell, doi:10.1016/j.stem.2021.04.028 (GEO: GSE164073).
Human post-mortem ocular tissue (cornea, limbus, sclera) infected ex vivo with SARS-CoV-2 or mock.
The count matrix is the same one used in the QLS-MiCM "Differential Gene Expression Analysis" workshop.

Outputs (in Exercises/data/):
  sample_metadata.csv      - 18 samples x (sample, tissue, condition)
  log2cpm_filtered.csv     - log2(CPM + 1) for expressed genes (genes x samples)
  de_cornea_CoV2_vs_mock.csv - DESeq2-style results (PyDESeq2) for cornea, CoV2 vs mock

Run from the repo root:  python Exercises/data_scripts/prepare_data.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"

counts = pd.read_csv(DATA / "GSE164073_Eye_count_matrix.tsv", sep="\t", index_col=0)
counts.index.name = "gene"

# --- metadata ---------------------------------------------------------------
tissue = ["cornea"] * 6 + ["limbus"] * 6 + ["sclera"] * 6
condition = (["mock"] * 3 + ["CoV2"] * 3) * 3
meta = pd.DataFrame({"sample": counts.columns, "tissue": tissue, "condition": condition})
meta.to_csv(DATA / "sample_metadata.csv", index=False)

# --- normalised expression ---------------------------------------------------
cpm = counts / counts.sum(axis=0) * 1e6
keep = (cpm >= 1).sum(axis=1) >= 3          # expressed (>=1 CPM) in at least 3 samples
logcpm = np.log2(cpm.loc[keep] + 1).round(4)
logcpm.to_csv(DATA / "log2cpm_filtered.csv")
print(f"Kept {keep.sum()} / {len(keep)} genes")

# --- differential expression (cornea, CoV2 vs mock) -------------------------
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

m = meta.set_index("sample")
cornea = m.index[m.tissue == "cornea"]
c = counts.loc[keep, cornea].T
dds = DeseqDataSet(counts=c, metadata=m.loc[cornea], design="~condition", quiet=True)
dds.deseq2()
st = DeseqStats(dds, contrast=["condition", "CoV2", "mock"], quiet=True)
st.summary()
res = st.results_df[["baseMean", "log2FoldChange", "lfcSE", "pvalue", "padj"]]
res = res.dropna(subset=["pvalue"])
res[["baseMean", "log2FoldChange", "lfcSE"]] = res[["baseMean", "log2FoldChange", "lfcSE"]].round(4)
res.index.name = "gene"
res.to_csv(DATA / "de_cornea_CoV2_vs_mock.csv", float_format="%.6g")
print(res.sort_values("padj").head(15))
print("padj<0.05:", (res.padj < 0.05).sum())
