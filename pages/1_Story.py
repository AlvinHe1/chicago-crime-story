import streamlit as st
from utils.io import load_data
from charts.charts import crime_time_series_chart

st.title("How Has Crime Changed Over Time?")

df = load_data()

st.write(
    """
    This visualization displays the total number of crimes recorded each month.
    By aggregating crime counts over time, we can observe overall trends and
    detect potential increases or decreases in crime activity.
    """
)

chart = crime_time_series_chart(df)

st.altair_chart(chart, use_container_width=True)

from charts.charts import crime_time_series_chart, crime_type_bar_chart
st.subheader("What Types of Crimes Are Most Common?")

st.write(
    """
    This chart shows the 10 most frequent crime categories.
    It highlights which types of crime dominate the dataset.
    """
)

bar_chart = crime_type_bar_chart(df)

st.altair_chart(bar_chart, use_container_width=True)
