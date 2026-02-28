import altair as alt
import pandas as pd

def crime_time_series_chart(df: pd.DataFrame):
    # Create month column
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
    
    monthly_counts = (
        df.groupby("Month")
        .size()
        .reset_index(name="Crime Count")
    )

    chart = (
        alt.Chart(monthly_counts)
        .mark_line()
        .encode(
            x="Month:T",
            y="Crime Count:Q"
        )
        .properties(
            title="Monthly Crime Counts in Chicago"
        )
    )

    return chart


def crime_type_bar_chart(df: pd.DataFrame):
    top_types = (
        df["Primary Type"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_types.columns = ["Primary Type", "Count"]

    chart = (
        alt.Chart(top_types)
        .mark_bar()
        .encode(
            x="Count:Q",
            y=alt.Y("Primary Type:N", sort="-x")
        )
        .properties(
            title="Top 10 Most Common Crime Types"
        )
    )

    return chart

def crime_type_time_series_interactive(df: pd.DataFrame, selected_type: str):
    filtered_df = df[df["Primary Type"] == selected_type]

    filtered_df["Month"] = (
        filtered_df["Date"]
        .dt.to_period("M")
        .dt.to_timestamp()
    )

    monthly_counts = (
        filtered_df
        .groupby("Month")
        .size()
        .reset_index(name="Crime Count")
    )

    chart = (
        alt.Chart(monthly_counts)
        .mark_line()
        .encode(
            x="Month:T",
            y="Crime Count:Q"
        )
        .properties(
            title=f"Monthly Trend for {selected_type}"
        )
    )

    return chart

import streamlit as st
import pandas as pd

def crime_map(df, selected_type):
    filtered_df = df[
        (df["Primary Type"] == selected_type)
        & df["Latitude"].notna()
        & df["Longitude"].notna()
    ]

    # Streamlit expects lat/lon column names exactly like this
    map_df = filtered_df.rename(
        columns={
            "Latitude": "lat",
            "Longitude": "lon"
        }
    )[["lat", "lon"]]

    st.subheader(f"Crime Locations for {selected_type}")
    st.map(map_df)
    

