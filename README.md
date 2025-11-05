# ⚔️ Genshin Character Statistics Dashboard

An interactive data analysis project exploring **Genshin Impact character stats** — using real data from the Genshin API/Fandom Wiki.  
Built with **Python, pandas, and Streamlit**, this project visualizes and compares characters by their base stats and predicts potential damage output using a simple regression model.

---

## 📘 Overview
The goal of this project was to practice:
- Fetching and cleaning structured API data.
- Building visual dashboards with filters.
- Applying simple ML regression to game data.

Even though it was a short experiment, it helped me understand the pipeline from **data collection → preprocessing → visualization → modeling**.

---


---

## ⚙️ Features
- **Data Fetching:** Pulls stats (HP, ATK, DEF, Crit Rate, Element, Weapon, Rarity) from the Genshin API or Wiki.
- **Dashboard Filters:**  
  - Filter characters by element, weapon type, or rarity.  
  - Sort and compare base stats interactively.
- **Regression Model:**  
  - Predicts potential damage output using a simple linear regression.
- **Visualizations:**  
  - Plotly charts for stat comparisons and distributions.

---

## 🧠 Tools Used
| Purpose | Tools |
|----------|-------|
| Data Handling | pandas, numpy |
| Visualization | matplotlib, plotly |
| Web App | Streamlit |
| Machine Learning | scikit-learn |

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Bingeeverything/genshin-ai-lab.git
   cd genshin-ai-lab/tier1_data_dashboard
   
Install dependencies:
pip install -r requirements.txt

Run the dashboard:
streamlit run streamlit_app.py
