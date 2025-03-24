# Heart-Disease-Prediction
# Heart Disease Prediction Dashboard

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Accuracy](https://img.shields.io/badge/accuracy-92%25-brightgreen?style=for-the-badge)

An interactive machine learning dashboard for predicting heart disease risk using clinical parameters.

## Features

- **Exploratory Data Analysis**: Visualize distributions and correlations
- **Real-time Predictions**: Random Forest model with 92% accuracy
- **Feature Importance**: Understand key clinical indicators
- **Mobile-Friendly**: Responsive Streamlit interface

## Installation

1. Clone the repository:

   git clone https://github.com/evans25575/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction

   Usage
Run the Streamlit app:


streamlit run app/heart_app.py
The app will launch at http://localhost:8501

Project Structure
.
├── app/                  # Streamlit application
│   ├── heart_app.py      # Main dashboard script
│   └── utils.py          # Helper functions (if any)
├── data/                 
│   └── heart.csv         # Clinical dataset
├── notebooks/
│   └── analysis.ipynb    # Jupyter notebook with EDA
├── requirements.txt      # Python dependencies
└── README.md             # This file
Dataset
The Cleveland Heart Disease Dataset contains:

303 patient records

13 clinical features (age, cholesterol, etc.)

Target: Presence of heart disease (0-4)

Model Performance
Metric	Score
Accuracy	92%
Precision	0.91
Recall	0.93
F1-Score	0.92
Screenshots
Dashboard Preview <!-- Add your screenshot -->

License
MIT



Save as app/screenshots/dashboard.png


### Key Customization Points:
1. Replace `your-username` in the git clone URL
2. Add actual screenshots to `/app/screenshots/`
3. Update model metrics if different
4. Add your name under `## Author` if desired
