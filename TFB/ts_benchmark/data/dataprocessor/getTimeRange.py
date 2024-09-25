import pandas as pd


# function to read excel data
def read_excel_data(file_path, sheet_name):
    excel_file = pd.ExcelFile(file_path)
    excel_data = excel_file
    df = excel_data.parse(sheet_name)
    # the data has columns 'Sensor Name', 'Date', and 'Value'
    df["Date"] = pd.to_datetime(
        df["Date"]
    )  # Ensure that 'Date' column is in datetime format
    # let the columns be 'date','value','sensorID'
    grouped = df.groupby("sensorID")
    return grouped


def read_excel_data_byDate(file_path, sheet_name):
    excel_file = pd.ExcelFile(file_path)
    excel_data = excel_file
    df = excel_data.parse(sheet_name)
    # the data has columns 'Sensor Name', 'Date', and 'Value'
    grouped = df.groupby("Date")
    return grouped


def read_position(file_path, sheet_name):
    # read the data from the excel file
    excel_file = pd.ExcelFile(file_path)
    excel_data = excel_file
    df = excel_data.parse(sheet_name)
    return df


# function to get the time range of the data
def getDataTimeRange(grouped):
    results = []
    for group in grouped:
        start_date = group[1]["Date"].min()
        end_date = group[1]["Date"].max()
        min_value = group[1]["value"].min()
        max_value = group[1]["value"].max()
        # get count of data points in each group
        count = group[1].shape[0]
        sensorID = group[0]
        results.append([sensorID, start_date, end_date, count, min_value, max_value])
        # transfer the list to a dataframe
        final_df = pd.DataFrame(
            results,
            columns=[
                "sensorID",
                "start_date",
                "end_date",
                "count",
                "min_value",
                "max_value",
            ],
        )
    return final_df


def writeRangeToExcel(final_df, file_path, sheetname):
    with pd.ExcelWriter(file_path, mode="a", engine="openpyxl") as writer:
        final_df.to_excel(writer, sheet_name=sheetname, index=False)
    print(f"Data has been successfully written to sheet in {file_path}")


# get maxium and minimum value of data
def run():
    file_path = r"/home/vsc/workspace/IDT3/Cor/dataprocess/data/groundsettlement.xlsx"
    file_path_range = r"/home/vsc/workspace/IDT3/Cor/dataprocess/data/range.xlsx"
    sensorDataSheets = [
        "GroundSettlement",
        "B1SettleM",
        "B2SettleM",
        "A1SettleM",
        "A2SettleM",
        "A1ConverM",
    ]
    sheet_name = sensorDataSheets[5]

    # for sheet in sensorDataSheets:
    #     grouped_data = read_excel_data(file_path, sheet)
    #     final_data = getDataTimeRange(grouped_data)
    #     writeRangeToExcel(final_data, file_path_range, sheet)

    path_interpolated = (
        r"/home/vsc/workspace/IDT3/Cor/dataprocess/data/interpolated.xlsx"
    )
    # get time range for ground settlement
    final_data = getDataTimeRange(read_excel_data(path_interpolated, sheet_name))
    writeRangeToExcel(final_data, file_path_range, sheet_name)


# run()
