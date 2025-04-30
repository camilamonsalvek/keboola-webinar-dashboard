import streamlit as st
import pandas as pd
import os

# Define data paths
keboola_data_path = "/data/in/tables/webinar_registration.csv"
sample_data_path = "sample_data.csv"
data_loaded = False
df = None

st.set_page_config(layout="wide")

st.title("Webinar Registration Dashboard")

# Try loading data from Keboola input mapping
if os.path.exists(keboola_data_path):
    try:
        st.write(f"Loading data from {keboola_data_path}")
        df = pd.read_csv(keboola_data_path, compression='gzip')
        data_loaded = True
        st.success("Successfully loaded data from Keboola.")
    except Exception as e:
        st.error(f"Error loading data from Keboola: {e}")
        st.write("Attempting to load sample data...")

# Fallback to sample data if Keboola data fails or doesn't exist
if not data_loaded:
    if os.path.exists(sample_data_path):
        try:
            st.write(f"Loading sample data from {sample_data_path}")
            df = pd.read_csv(sample_data_path)
            data_loaded = True
            st.warning("Loaded sample data. Input data from Keboola not found or failed to load.")
        except Exception as e:
            st.error(f"Error loading sample data: {e}")
    else:
        st.error("Sample data file not found. Cannot display data.")

# Display the dataframe if data was loaded
if data_loaded and df is not None:
    st.header("Registration Data")
    st.dataframe(df)
else:
    st.warning("No data available to display.")

st.info("This is a basic dashboard structure. You can add more charts and analysis here.")