import pandas as pd

def load_data(filepath="data\titanic.csv"):
    df = pd.read_csv(filepath)
    df = df[df["sex"] == "male"]
    return df