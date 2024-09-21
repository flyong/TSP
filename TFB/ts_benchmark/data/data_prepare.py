# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def write_data(data: np.ndarray, file_path: str) -> None:
    """
    Write data to a file.
    """
    pd.DataFrame(data).to_csv(file_path, index=False)
    
