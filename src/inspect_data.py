import pandas as pd

def inspect_data(file_path):
    data = pd.read_csv(file_path, skiprows=1)
    print(data.head())
    print(data.columns)
    print(data.describe())

if __name__ == "__main__":
    file_path = '../data/temperature.csv'
    inspect_data(file_path)
