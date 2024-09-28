import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("DataInsight - Plug & Play Data Analysis")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    # Basic stats
    st.write("Summary Statistics:", df.describe())

    # Filter to numeric columns only
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Check if there are numeric columns for correlation
    if numeric_df.empty:
        st.write("No numeric columns to calculate correlation.")
    else:
        # Correlation heatmap
        st.write("Correlation Heatmap:")
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, ax=ax)
        st.pyplot(fig)
