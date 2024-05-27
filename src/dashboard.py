import pandas as pd
import plotly.express as px
from data_processing import load_data, clean_data
import os

def create_line_chart(data):
    """Create a line chart of temperature anomalies over time."""
    fig = px.line(data, x='Year', y='Anomaly', title='Global Temperature Anomalies Over Time')
    return fig

def create_histogram(data):
    """Create a histogram of temperature anomalies."""
    fig = px.histogram(data, x='Anomaly', nbins=30, title='Distribution of Temperature Anomalies')
    return fig

def create_heatmap(data):
    """Create a heatmap of temperature anomalies by month."""
    monthly_data = data.melt(id_vars=["Year"], value_vars=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                             var_name="Month", value_name="Monthly_Anomaly")
    fig = px.density_heatmap(monthly_data, x='Year', y='Month', z='Monthly_Anomaly', title='Heatmap of Monthly Temperature Anomalies')
    return fig

def create_dashboard(data):
    """Create and display the dashboard."""
    line_chart = create_line_chart(data)
    histogram = create_histogram(data)
    heatmap = create_heatmap(data)

    line_chart.show()
    histogram.show()
    heatmap.show()

if __name__ == "__main__":
    # Use the absolute path to ensure the file is found
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '../data/temperature.csv')
    
    data = load_data(data_path)
    clean_data = clean_data(data)
    create_dashboard(clean_data)
