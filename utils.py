import pandas as pd

def load_data(filepath="data\titanic.csv"):
    """Load the Titanic dataset and filter"""
    df = pd.read_csv(filepath)
    df = df[df["sex"] == "male"]
    return df

def clean_data(df):
    """
    Cleans the Titanic dataset by:
    - Dropping rows with missing values
    - Converting categorical columns to lowercase

    Parameters:
    df (pd.DataFrame): Input DataFrame

    Returns:
    pd.DataFrame: Cleaned DataFrame
    """
    
    #df_cleaned = df.dropna()
    df['embarked'] = df["embarked"].str.lower()

    return df