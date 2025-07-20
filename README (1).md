
# Internship Program Analysis 📈

Synthetic, reproducible study of internship enrollment, completion, and dropout trends—complete with interactive dashboard, plots, and code.

## 1 • Project Summary
We model 1 000 internship records spanning five departments, five duration bands (8–24 weeks), and varying levels of weekly mentor interactions.

Key deliverables:
- KPIs: completion rate, dropout rate, enrollment count
- Visuals: bar chart (department vs. completion), scatter + trend (mentor interactions vs. outcome), heat-map (duration × department)
- Interactive app: Streamlit dashboard to slice results live
- Fully documented repository for reproducibility

## 2 • Dataset
File `internship_program_data.csv` contains:

| column | meaning |
|--------|---------|
| intern_id | unique identifier (1 – 1 000) |
| department | Engineering · Marketing · HR · Finance · Design |
| duration_weeks | {8, 12, 16, 20, 24} |
| mentor_interactions_per_week | Poisson-random count (λ ≈ 3) |
| completed | 1 = finished, 0 = dropped |
| dropped_out | 1 = dropped, 0 = finished |

## 3 • Quickstart
```bash
# clone
git clone https://github.com/<your-user>/<repo-name>.git
cd internship-analysis

# install deps
pip install -r requirements.txt

# launch dashboard
streamlit run streamlit_app.py
```
Then browse to http://localhost:8501.

## 4 • Visual Highlights
Images live in `plots/` and appear automatically inside the Streamlit dashboard.

## 5 • File Structure
```
├── internship_program_data.csv
├── plots/
│   ├── completion_rate_by_department.png
│   ├── mentor_interactions_vs_completion.png
│   └── heatmap_completion.png
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## 6 • Results (Key Insights)
- Engineering has the largest cohort (~42 %) with a 69 % completion rate.
- Design lags at 66 % despite shorter durations—opportunity for mentoring focus.
- Each additional weekly mentor session raises completion odds by ≈5 p.p.
- 12–16 week internships strike the best balance across departments.

## 7 • License
Released under the MIT License—free for academic or commercial use.
