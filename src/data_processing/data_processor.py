import pandas as pd

class DataProcessor:
    def __init__(self):
        pass

    def load_data(self, file_path):
        return pd.read_csv(file_path)

    def clean_data(self, df):
        return df.dropna()

    def transform_data(self, df):
        return df * 2
