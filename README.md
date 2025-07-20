# Internship Program Analysis 📈  
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://internship-analysis-d8youydhmjmgupesews4lp.streamlit.app/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

A concise, end-to-end study of internship enrollment, completion, and dropout trends—complete with an interactive dashboard, reproducible code, and key insights for program managers.

---

## 🚀 Live Demo
Launch the dashboard here → **https://internship-analysis-d8youydhmjmgupesews4lp.streamlit.app/**  
No local setup required—just open and explore.

---

## 1 · Project Snapshot
| Metric | Value |
|--------|-------|
| Records analysed | **1 000** interns |
| Departments | Engineering · Marketing · HR · Finance · Design |
| Completion range | 66 % – 72 % |
| Biggest lift | +5 pp per extra weekly mentor session |

---

## 2 · Quickstart

```bash
# clone the repo
git clone https://github.com/<LaraibFatima-heu>/<LaraibFatima-heu>.git
cd <repo-name>

# install and run
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 3 · File Map
```
├── internship_program_data.csv        # synthetic dataset
├── streamlit_app.py                   # interactive dashboard
├── plots/                             # ready-made static visuals
│   ├── completion_rate_by_department.png
│   ├── mentor_interactions_vs_completion.png
│   └── heatmap_completion.png
├── requirements.txt                   # Python dependencies
└── README.md                          # you are here
```

---

## 4 · Methodology
1. **Data ingestion** Load the CSV, verify schema, coerce types.  
2. **KPIs** Compute enrollment counts, completion & dropout percentages by department and duration.  
3. **Visual analytics** Generate:
   - Bar chart: completion % by department  
   - Scatter + trend: mentor interactions vs. completion outcome  
   - Heat-map: completion % across duration × department  
4. **Deployment** Serve with Streamlit Cloud (free tier), automatically rebuilding on each Git push.

---

## 5 · Key Insights
- Engineering hosts the largest cohort (~42 %) and still maintains a respectable 69 % completion rate.  
- Design lags at 66 % despite shorter internships—suggests a mentoring gap.  
- Each additional weekly mentor touch-point lifts completion probability by **≈ 5 percentage points**.  
- 12–16 week programs balance completion and resource cost most effectively.

---

## 6 · Contributing
Pull requests are welcome—feel free to submit bug fixes, feature requests, or performance tweaks.  
For major changes, open an issue first to discuss what you’d like to change.

---

## 7 · License
This project is licensed under the **MIT License**. See `LICENSE` for details.

