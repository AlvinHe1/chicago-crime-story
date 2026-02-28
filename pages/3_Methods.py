import streamlit as st
from utils.io import load_data

st.title("Methods")

df = load_data()

st.header("Dataset Description")

st.write(
    """
    This project uses the Chicago Crimes (2001–Present) dataset
    from the City of Chicago Open Data Portal.

    The dataset contains information about reported crimes including:
    - Date of occurrence
    - Primary crime type
    - Arrest indicator
    - Location description
    - Geographic coordinates
    """
)

st.header("Data Processing")

st.write(
    """
    Because the full dataset contains millions of rows,
    we randomly sampled 60,000 observations to ensure
    the application runs efficiently in Streamlit. The Date column was converted to datetime format,
    and additional time-based features (Year) were derived for visualization purposes.
    """
)

st.header("Data Preview")

st.dataframe(df.head())

st.header("Limitations")

st.write(
    """
    This analysis is based on a random sample of the full dataset.
    Results may differ slightly from the complete dataset. Additionally, crime reporting practices and policing
    strategies may vary over time, which can influence trends.
    """
)
