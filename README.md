# Environmental Data Analyses 🌿

This repo is a collection of **reproducible environmental and ecological analyses** spanning climate, habitat, biodiversity, and human–environment interactions. The emphasis is on **clean data workflows**, **geospatial reasoning**, and **decision-ready visuals** (maps, trend plots, compact writeups).

If you’re here from my profile: this repo is the “environmental counterpart” to my aerospace work — same focus on structure and reproducibility, applied to environmental intelligence and ecological datasets.

---

## What you’ll find here

This repo focuses on end-to-end analytical work: ingesting messy public datasets, building tidy analysis-ready tables, running models or statistical summaries, and producing clear outputs.

Typical workflows include geospatial joins, raster/vector preprocessing, timeseries aggregation, and uncertainty-aware evaluation (where labels exist).

---

## 🌟 Featured Projects (inside this repo)

<details>
<summary><strong>🐦 Wildlife Image Classification API</strong></summary>

**Goal:** Deploy a lightweight FastAPI service for individual bird identification.  

**Data:** Bird Individual ID dataset (Ferreira et al. 2020).  

**Methods:** Transfer learning (ResNet18), PyTorch dataloaders, FastAPI inference, CI/CD, model versioning. 

**Outputs:** Trained model (`.pt`), `classes.json`, API endpoints, benchmark scripts.

🔗 <a href="./wildlife-classification.api">View Project</a>

</details>

---

<details>
<summary><strong>🧊 Sea Ice Trend Analysis</strong></summary>

**Goal:** Quantify long‑term and seasonal changes in Arctic sea ice extent. 

**Data:** NSIDC Sea Ice Index (NOAA), Copernicus Arctic datasets.  

**Methods:** Raster time‑series analysis, anomaly detection, trend fitting, geospatial visualization. 

**Outputs:** Annotated plots, exploratory notebooks, exportable datasets.

🔗 <a href="./sea-ice-analysis">View Project</a>

</details>

---

## Repo structure

`data/` is intentionally not fully checked in if it’s large. This repo favors a structure that makes it easy to reproduce results without guessing.

- `notebooks/` exploratory and narrative analyses
- `src/` reusable functions (loading, cleaning, geospatial utilities)
- `reports/` exported figures and short writeups
- `data/` small samples or metadata (large raw data is pulled via scripts)
- `scripts/` one-shot CLIs to download/process data

---

## Reproducibility

The goal is that a reader can clone the repo and rerun the analysis with minimal friction.

- Environment: `environment.yml` or `pyproject.toml`
- Determinism: fixed random seeds where applicable
- Data provenance: dataset sources documented in each project folder
- Outputs: figures/maps exported to `reports/` (and kept lightweight)

Quickstart:

```bash
# create env (example)
conda env create -f environment.yml
conda activate envdata

# run notebooks (example)
jupyter lab
