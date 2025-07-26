# Heart-Disease-Prediction
# Heart Disease Prediction Dashboard

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Accuracy](https://img.shields.io/badge/accuracy-92%25-brightgreen?style=for-the-badge)


# ❤️ Heart Disease Prediction

An interactive machine learning dashboard built with Streamlit that predicts the likelihood of heart disease based on clinical parameters. The model is trained on the Cleveland Heart Disease dataset and achieves high accuracy using a Random Forest Classifier.

---

## 📌 Objectives

- Train and evaluate machine learning models to predict heart disease.
- Provide real-time predictions using a user-friendly Streamlit app.
- Visualize key features and model performance metrics.
- Deploy a responsive dashboard for users to interact with.

---

## 🧠 Key Features

- 📊 **Exploratory Data Analysis**: Correlation matrix, histograms, and outlier checks
- 🤖 **Model**: Random Forest (Accuracy: 92%)
- 🧮 **Feature Importance**: Visual ranking of predictors
- 📱 **Mobile-Friendly**: Built with responsive design in Streamlit
- 📥 **Fast Predictions**: Form-based input → result in real time

---

## 🛠 Tech Stack

- Python (Pandas, NumPy, Scikit-learn)
- Streamlit (Dashboard UI)
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 📂 Project Structure

```bash
.
├── app/
│   ├── heart_app.py       # Streamlit dashboard script
│   └── utils.py           # Helper functions (optional)
├── data/
│   └── heart.csv          # Dataset
├── notebooks/
│   └── analysis.ipynb     # EDA and model development
├── requirements.txt       # Dependencies
└── README.md              # Project documentation


📊 Dataset Summary

Dataset: Cleveland Heart Disease Dataset
Records: 303 patient samples
Target Variable: Heart disease presence (0 = no disease, 1–4 = disease)
Features:

Age, sex, chest pain type, cholesterol, resting BP, etc.



---

🚀 How to Run the App

1. Clone the repository

git clone https://github.com/evans25575.
cd Heart-Disease-Prediction

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit dashboard

streamlit run app/heart_app.py

Visit: http://localhost:8501


---

✅ Model Performance

Metric	Score

Accuracy	92%
Precision	0.91
Recall	0.93
F1-Score	0.92




👨‍💻 Author

Evans Kiplangat
🌐 https://github.com/evans25575
🐙 https://evans-kiplangat-portfolio27.netlify.app/



---

📜 License

MIT License
