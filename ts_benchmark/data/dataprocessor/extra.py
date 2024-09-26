# -*- coding: utf-8 -*-
from ts_benchmark.common.constant import ROOT_PATH
import os

def get_all_senorID():
    x = []
    for i in range(10):
        for j in range(10):
            x.append('DB'+str(i+1)+'-'+str(j+1))
    return x


# function to get the list of sensors
def getSensorList():
    groundSensorID = [
        "GS10-1",
        "GS10-2",
        "GS10-3",
        "GS10-4",
        "GS10-5",
        "GS10-6",
        "GS10-7",
        "GS10-8",
        "GS10-9",
        "GS8-1",
        "GS8-10",
        "GS8-2",
        "GS8-3",
        "GS8-5",
        "GS8-6",
        "GS8-7",
        "GS8-8",
        "GS8-9",
        "GS9-1",
        "GS9-10",
        "GS9-2",
        "GS9-5",
        "GS9-6",
        "GS9-7",
        "GS9-8",
        "GS9-9",
    ]

    tunnelSensorID = [
        "TSA1-01",
        "TSA1-02",
        "TSA1-03",
        "TSA1-04",
        "TSA1-05",
        "TSA1-06",
        "TSA1-07",
        "TSA1-08",
        "TSA1-09",
        "TSA1-10",
        "TSA1-11",
        "TSA1-12",
        "TSA1-13",
        "TSA1-14",
        "TSA1-15",
        "TSA1-16",
        "TSA1-17",
        "TSA1-18",
        "TSA1-19",
        "TSA1-20",
        "TSA1-21",
        "TSA1-22",
        "TSA1-23",
        "TSA1-24",
        "TSA1-25",
        "TSA1-26",
        "TSA1-27",
        "TSA1-28",
        "TSA1-29",
        "TSA1-30",
        "TSA1-31",
        "TSA1-32",
        "TSA1-33",
        "TSA1-34",
        "TSA1-35",
        "TSA1-36",
        "TSA1-37",
        "TSA1-38",
        "TSA1-39",
        "TSA1-40",
        "TSA1-41",
        "TSA1-42",
        "TSA1-43",
        "TSA1-44",
        "TSA1-45",
        "TSA1-46",
        "TSA1-47",
        "TSA1-48",
        "TSA1-49",
        "TSA1-50",
        "TSA1-51",
        "TSA1-52",
        "TSA1-53",
        "TSA1-54",
        "TSA1-55",
        "TSA1-56",
        "TSA1-57",
        "TSA1-58",
        "TSA1-59",
        "TSA1-60",
        "TSA1-61",
        "TSA1-62",
        "TSA1-63",
        "TSA1-64",
        "TSA1-65",
        "TSA1-66",
        "TSA1-67",
        "TSA1-68",
        "TSA1-69",
        "TSA1-70",
        "TSA1-71",
        "TSA1-72",
        "TSA1-73",
        "TSA1-74",
        "TSA1-75",
    ]  # Sensors in tunnelA1
    return groundSensorID, tunnelSensorID


# function to get path list of files
def getFilePathList():
    data_path = os.path.join(ROOT_PATH, "dataset", "interpolated.xlsx")
    result_path = os.path.join(ROOT_PATH, "dataset", "wtresult.xlsx")
    correlation_path = os.path.join(ROOT_PATH, "dataset", "correlation.xlsx")
    position_path = os.path.join(ROOT_PATH, "dataset", "position.xlsx")
    range_path = os.path.join(ROOT_PATH, "dataset", "range.xlsx")
    return data_path, result_path, correlation_path, position_path, range_path
