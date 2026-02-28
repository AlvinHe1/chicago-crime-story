import streamlit as st
import pandas as pd

@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv("chicago_crime_sample.csv")
    
    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    
    return df
    