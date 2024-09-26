from getTimeRange import read_excel_data,writeRangeToExcel
import pandas as pd
import os
from ts_benchmark.common.constant import ROOT_PATH

# data interpolation using ajacent value mean for missing data in some days
def interpolateData(grouped_data):
    interpolated_data = []
    for group in grouped_data:
        sensorID = group[0]
        data = group[1]
        data_for_interpolation = pd.DataFrame(data[['Date', 'value']], columns=['Date', 'value'])
        data_for_interpolation = data_for_interpolation.set_index('Date')
        data_for_interpolation = data_for_interpolation.resample('D').mean()
        data_for_interpolation = data_for_interpolation.interpolate(method='linear')
        data_for_interpolation = data_for_interpolation.reset_index()
        for index, row in data_for_interpolation.iterrows():
            interpolated_data.append([row['Date'],sensorID,row['value']])
    return interpolated_data


def runInterpolation():
    # get the root directory of the project
    file_path = os.path.join(ROOT_PATH, "dataset", "groundsettlement.xlsx")
    file_path_range = os.path.join(ROOT_PATH, "dataset", "range.xlsx")
    file_path_interpolated = os.path.join(ROOT_PATH, "dataset", "interpolated.xlsx")
    sensorDataSheets = ['GroundSettlement','B1SettleM', 'B2SettleM', 'A1SettleM', 'A2SettleM','A1ConverM']

    sensorDataSheet = sensorDataSheets[5]
    grouped_data = read_excel_data(file_path, sensorDataSheet)
    interpolated_data = interpolateData(grouped_data)
    interpolated_data =pd.DataFrame(interpolated_data, columns=['Date','sensorID','value'])
    writeRangeToExcel(interpolated_data, file_path_interpolated, sensorDataSheet)
    return True

runInterpolation()
