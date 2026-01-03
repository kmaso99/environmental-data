# Analysis of Sea Ice Levels

A reproducible environmental time-series analysis exploring **sea ice variability and long-term change**, with an emphasis on **trend characterization** and **change-point detection** to identify potential regime shifts.

Notebook:
https://github.com/kmaso99/environmental-data/blob/main/Analysis%20of%20Sea%20Ice%20Levels.ipynb

---

## What this project does

This project analyzes sea ice time series to:
- visualize changes over time and summarize key patterns
- quantify shifts in behavior using **change-point detection**
- communicate results clearly with plots and interpretable outputs

The goal is to provide a clean, reviewable workflow that could slot into a broader “environmental intelligence” toolkit.

---

## Methods used

This notebook uses:
- exploratory time-series visualization and summary statistics
- change-point detection with `ruptures` (regime shift style analysis)
- standard Python data science tooling for reproducible plots and iteration

---

## Tech stack

Python: `pandas`, `numpy`
Visualization: `matplotlib`, `seaborn`
Time-series change detection: `ruptures`

---

## How to run locally

```bash
git clone https://github.com/kmaso99/environmental-data.git
cd environmental-data

python -m venv .venv
source .venv/bin/activate

pip install pandas numpy matplotlib seaborn ruptures jupyter
jupyter lab
