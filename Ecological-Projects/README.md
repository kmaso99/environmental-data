# Analysis of Sea Ice Levels

## Question

How has sea‑ice extent changed over time, and do the Northern and Southern Hemispheres show different long‑term trends, seasonal structure, or evidence of regime shifts?

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

**Results:** Using NSIDC daily sea-ice extent records, I aggregated the data to monthly and annual means, then compared long‑term behavior between the Northern and Southern Hemispheres. The full time series shows a strong seasonal cycle plus a clear long‑term decline in overall extent. When split by hemisphere, the Arctic shows persistent losses over time, with the steepest declines concentrated in late summer/early autumn (around the annual minimum). The Antarctic signal is more variable: several decades show small gains, but the most recent period shows a sharp downturn. Decadal trend summaries highlight consistent negative trends in the north and a regime shift in the south late in the record. A change‑point analysis on annual mean extent identifies a structural break around 2002 in the Northern Hemisphere and around 2017 in the Southern Hemisphere, marking periods where the behavior of the series changes materially.

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
