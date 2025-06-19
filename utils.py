import pandas as pd

def load_data(filepath="data\titanic.csv"):
    return pd.read_csv(filepath)