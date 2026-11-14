import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Restaurant Menu Optimization", layout="wide")
st.title("Restaurant Menu Optimization Dashboard")

# Load data (Make sure 'restaurant_menu_optimization_data.csv' is uploaded in the same GitHub repo)
try:
    df = pd.read_csv("restaurant_menu_optimization_data.csv")
    st.success("Data loaded successfully!")

    # Display basic metrics
    st.subheader("Data Overview")
    st.dataframe(df.head())

    st.subheader("Dataset Summary")
    st.dataframe(df.describe())

    # Quick search / filter
    if not df.empty:
        st.subheader("Filter Menu Data")
        columns = df.columns.tolist()
        selected_col = st.selectbox("Filter by column:", columns)
        
        unique_vals = df[selected_col].dropna().unique()
        selected_val = st.selectbox("Select value:", unique_vals)
        
        filtered_df = df[df[selected_col] == selected_val]
        st.write(f"Filtered results ({len(filtered_df)} rows):")
        st.dataframe(filtered_df)

except FileNotFoundError:
    st.error("File 'restaurant_menu_optimization_data.csv' nahi mili! Please is CSV file ko apni GitHub repository mein upload karein.")
except Exception as e:
    st.error(f"Error: {e}")
