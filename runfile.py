import streamlit as st
import pandas as pd
import analysis
import os

st.set_page_config(page_title="Climate Data Explorer", layout="wide")

st.title("🌍 Climate Change Data Explorer")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = analysis.load_data(uploaded_file)

    # Preview
    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    # Info
    st.subheader("ℹ️ Dataset Info")
    info = analysis.basic_info(df)

    st.write(f"Shape: {info['shape']}")
    st.write("Columns:", info['columns'])

    st.subheader("❗ Missing Values")
    st.write(info['missing'])

    # Generate reports
    if st.button("Generate Profiling Report"):
        with st.spinner("Generating report..."):
            profile_path = analysis.generate_profile_report(df)
            with open(profile_path, "rb") as f:
                st.download_button("Download Profile Report", f, file_name="profile_report.html")

    if st.button("Generate Sweetviz Report"):
        with st.spinner("Generating report..."):
            sweetviz_path = analysis.generate_sweetviz_report(df)
            with open(sweetviz_path, "rb") as f:
                st.download_button("Download Sweetviz Report", f, file_name="sweetviz_report.html")

else:
    st.info("Please upload a CSV file to begin.")
