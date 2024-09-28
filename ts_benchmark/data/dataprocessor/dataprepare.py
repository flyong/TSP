# -*- coding: utf-8 -*-
import os
from typing import List
import pandas as pd
from ts_benchmark.common.constant import ROOT_PATH
from ts_benchmark.data.dataprocessor.correlateTimeSeries import get_date_range


def prepare_data() -> List[str]:
    """
    prepare data organised as time/number, value, and channel.
    return: a list of data set
    """
    # ROOT_PATH = r"/home/vsc/TSP"  # temporary path for testing

    data_path = os.path.join(ROOT_PATH, "dataset", "interpolated.xlsx")
    correlation_path = os.path.join(ROOT_PATH, "dataset", "correlation.xlsx")
    sheet_name_list = ["relationMatrix_rolling", "GroundSettlement", "A1SettleM"]

    ground_settlement_data = pd.read_excel(data_path, sheet_name=sheet_name_list[1])
    ground_settlement_data = ground_settlement_data.groupby("sensorID")
    tunnel_settlement_data = pd.read_excel(data_path, sheet_name=sheet_name_list[2])
    tunnel_settlement_data = tunnel_settlement_data.groupby("sensorID")

    # process raw correlation
    excel_data = pd.read_excel(correlation_path, sheet_name=sheet_name_list[0])

    excel_data = excel_data.groupby("tunnelID")

    # for each tunnelID, get the correlation
    # TODO: change the date according to the rolling window
    start_date, end_date = get_date_range()
    dataset_name_list = []
    for tunnelID, group in excel_data:
        # get the row for each tunnelID
        data = group.iloc[:, 1:]
        sum_data = data.sum(axis=1)
        channel_index = 1
        channel_name = []

        if sum_data.sum() >= 3:
            dataset_name = tunnelID + ".csv"
            dataset_name_list.append(dataset_name)
            # get the data from the tunnel settlement dataframe by tunnelID
            channel_1 = tunnel_settlement_data.get_group(tunnelID)
            channel_1 = channel_1[["Date", "value", "sensorID"]]
            channel_1 = channel_1[
                (channel_1["Date"] >= start_date) & (channel_1["Date"] <= end_date)
            ]
            channel_1["sensorID"] = "channel_" + str(channel_index)
            channel_name.append(["channel_" + str(channel_index), tunnelID])

            channel_index += 1
            # get the column name of excel data if the value is 1 (correlated data)
            columns = data.columns
            for index, row in data.iterrows():
                for i in range(len(row)):
                    if row[i] == 1:
                        channel_2 = ground_settlement_data.get_group(columns[i])
                        channel_2 = channel_2[["Date", "value", "sensorID"]]
                        channel_2 = channel_2[
                            (channel_2["Date"] >= start_date)
                            & (channel_2["Date"] <= end_date)
                        ]
                        channel_2["sensorID"] = "channel_" + str(channel_index)

                        # append channel_2 to channel_1
                        channel_1 = pd.concat([channel_1, channel_2], ignore_index=True)
                        channel_name.append(
                            ["channel_" + str(channel_index), columns[i]]
                        )

                        channel_index += 1
            channel_1.columns = ["date", "data", "cols"]
            write_data(channel_1, ROOT_PATH + "/dataset/forecasting/" + dataset_name)

            channel_name = pd.DataFrame(channel_name, columns=["channel", "sensorID"])
            write_data(
                channel_name,
                ROOT_PATH + "/dataset/channels/" + tunnelID + "_channel.csv",
            )

    return dataset_name_list


def write_data(data: pd.DataFrame, file_path: str) -> None:
    """
    write data
    """
    data.to_csv(file_path, index=False, if_exists="replace")
    return None


#  for testing
# prepare_data()
