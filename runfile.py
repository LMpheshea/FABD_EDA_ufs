import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv
import os

def load_data(file):
    df = pd.read_csv(file)
    return df

def basic_info(df):
    info = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing": df.isnull().sum()
    }
    return info

def generate_profile_report(df, output_file="profile_report.html"):
    profile = ProfileReport(df, title="ONI Report", explorative=True)
    profile.to_file(output_file)
    return output_file

def generate_sweetviz_report(df, output_file="sweetviz_report.html"):
    report = sv.analyze(df)
    report.show_html(output_file)
    return output_file
