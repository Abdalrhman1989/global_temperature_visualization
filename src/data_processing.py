import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path, skiprows=1)
    return data

def clean_data(data):
    """Clean and preprocess the data."""
    # Renaming columns to match the structure expected by the dashboard script
    data = data.rename(columns={
        'Year': 'Year', 'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr',
        'May': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Aug', 'Sep': 'Sep',
        'Oct': 'Oct', 'Nov': 'Nov', 'Dec': 'Dec', 'J-D': 'Anomaly'
    })
    # Removing rows where 'Year' or 'Anomaly' are missing
    data = data.dropna(subset=['Year', 'Anomaly'])
    return data
