import streamlit as st
from utils.io import load_data
from charts.charts import crime_type_time_series_interactive

st.title("Explore: Interactive Crime Trends")

df = load_data()

crime_types = sorted(df["Primary Type"].unique())

selected_type = st.selectbox(
    "Select a Crime Type:",
    crime_types
)

st.write(
    """
    Use the dropdown menu to explore how different crime categories
    have changed over time.
    """
)

chart = crime_type_time_series_interactive(df, selected_type)
st.altair_chart(chart, use_container_width=True)



from charts.charts import crime_map

# Year filter
min_year = df["Date"].dt.year.min()
max_year = df["Date"].dt.year.max()

selected_year = st.slider(
    "Select Year",
    min_value=int(min_year),
    max_value=int(max_year),
    value=int(max_year)
)

# Arrest filter
arrest_option = st.radio(
    "Arrest Made?",
    ["All", "Arrested", "Not Arrested"]
)

# Apply filtering
filtered_df = df[df["Date"].dt.year == selected_year]

if arrest_option == "Arrested":
    filtered_df = filtered_df[filtered_df["Arrest"] == True]
elif arrest_option == "Not Arrested":
    filtered_df = filtered_df[filtered_df["Arrest"] == False]

# Now call map ONLY ONCE
crime_map(filtered_df, selected_type)


