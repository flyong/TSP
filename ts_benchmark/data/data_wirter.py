# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def write_data_rolling(data: any, file_path: str) -> None:
    """
    Write any prediction data to a file.
    data can be a pandas DataFrame, a numpy array, or a list of pandas DataFrame or numpy array.
    """
    # get the dimension of dataframes
    if isinstance(data, pd.DataFrame):
        data = [data]
    elif isinstance(data, np.ndarray):
        # get the dimension of the array
        if len(data.shape) == 1:
            data = [pd.DataFrame(data)]
        else:
            data = [pd.DataFrame(d) for d in data]
    elif isinstance(data, list):
        if isinstance(data[0], pd.DataFrame):
            pass
        elif isinstance(data[0], np.ndarray):
            data = [pd.DataFrame(d) for d in data]
        else:
            raise ValueError("Data type not supported")
    else:
        raise ValueError("Data type not supported")

    for i, df in enumerate(data):
        if i == 0:
            df.to_csv(file_path, index=False)
        else:
            # write a list [0,0,0] row to separate the data
            pd.DataFrame(np.zeros((1, len(df.columns)))).to_csv(
                file_path, mode="a", header=False, index=False
            )
            df.to_csv(file_path, mode="a", header=False, index=False)
    print(f"Predicted Data written to {file_path}")


def write_data_fixed(data: pd.DataFrame, file_path: str) -> None:
    """
    write data
    """
    data.to_csv(file_path, index=False)
    return None
