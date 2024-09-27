import pandas as pd

def clean_data(df):
    # Fill missing values or drop rows
    df = df.fillna(df.median())
    return df

