import pandas as pd


def backendProcess(input_df: pd.DataFrame = None) -> pd.DataFrame:
    input_df["value"] = input_df["value"] * 3
    return input_df
