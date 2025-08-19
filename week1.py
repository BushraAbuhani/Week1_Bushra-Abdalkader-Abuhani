import pandas as pd
import streamlit as st

# Load the dataset
url = "employees.csv"
df = pd.read_csv(url)

st.title("📊 Sales Data Visualization")

# Show available columns
st.write("Available columns:", list(df.columns))

# Let user choose the time column and value column
time_column = st.selectbox("Select the time column:", df.columns)
value_column = st.selectbox("Select the value column:", [c for c in df.columns if c != time_column])

# Chart type selection
chart_type = st.selectbox("Choose chart type:", ["Line Chart", "Bar Chart"])

if chart_type == "Line Chart":
    st.line_chart(df.set_index(time_column)[value_column])
else:
    st.bar_chart(df.set_index(time_column)[value_column])
