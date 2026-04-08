import pandas as pd
import sweetviz as sv
import streamlit as st
import analysis
import streamlit.components.v1 as components

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

    # Generate Sweetviz Report
    if st.button("Generate Sweetviz Report"):
        with st.spinner("Generating report..."):
            report_path = analysis.generate_sweetviz_report(df)

            # Display inside Streamlit
            with open(report_path, 'r', encoding='utf-8') as f:
                html_data = f.read()

            components.html(html_data, height=900, scrolling=True)

            # Download option
            with open(report_path, "rb") as f:
                st.download_button(
                    label="Download Report",
                    data=f,
                    file_name="sweetviz_report.html",
                    mime="text/html"
                )

else:
    st.info("Please upload a CSV file to begin.")
