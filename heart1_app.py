import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
@st.cache_data
def load_data():
    try:
        data = pd.read_csv("C:/Users/Admin/Downloads/archive (3)/heart.csv")
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

d = load_data()

if d is not None:
    # Title
    st.title("Heart Disease Prediction Dashboard")
    
    # Data Exploration
    st.header("Data Exploration")
    if st.checkbox("Show Raw Data"):
        st.dataframe(d.head())
    
    # Correlation Matrix
    if st.checkbox("Show Correlation Matrix"):
        st.subheader("Correlation Matrix")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(d.corr(), annot=True, cmap='coolwarm', ax=ax, fmt=".2f")
        st.pyplot(fig)
        plt.close()
    
    # Model Training
    st.header("Model Training")
    X = d.drop('target', axis=1)
    y = d['target']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Model Evaluation
    st.subheader("Model Evaluation")
    st.metric("Accuracy Score", f"{accuracy_score(y_test, y_pred):.2%}")
    
    st.write("Classification Report:")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.table(pd.DataFrame(report).transpose())
    
    # Feature Importance (Fixed)
    st.subheader("Feature Importance")
    importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x='Importance', 
        y='Feature', 
        data=importance, 
        hue='Feature',  # Added to fix warning
        palette='viridis', 
        legend=False,    # Added to fix warning
        ax=ax
    )
    plt.title('Feature Importance')
    st.pyplot(fig)
    plt.close()