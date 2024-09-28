# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from ts_benchmark.common.constant import ROOT_PATH
import ts_benchmark.data.dataprocessor.extra as ex
from ts_benchmark.data.dataprocessor.correlateTimeSeries import (
    rolling_calculate_correlation,
)


def rolling_correlate(eveluation_config: dict) -> bool:
    """
    Correlate the time series by rolling window
    eveluation_config: dict
    """
    # default start_date and end_date
    start_date, end_date = ex.get_date_range()

    rolling_length = eveluation_config["strategy_args"]["num_rollings"]
    rolling_step = eveluation_config["strategy_args"]["stride"]

    # real_start_date = end_date minus rolling length by day
    real_start_date = pd.to_datetime(end_date) - pd.DateOffset(days=rolling_length)
    real_end_date = pd.to_datetime(end_date)

    # calculate the correlation matrix by rolling window, only write first/latest correlation matrix to csv
    write_flag = True
    while real_start_date >= pd.to_datetime(start_date):
        if write_flag:
            rolling_calculate_correlation(real_start_date, real_end_date, write_flag)
            write_flag = False
        else:
            rolling_calculate_correlation(real_start_date, real_end_date, write_flag)
        real_start_date = real_start_date - pd.DateOffset(days=rolling_step)
        real_end_date = real_end_date - pd.DateOffset(days=rolling_step)

    return True
