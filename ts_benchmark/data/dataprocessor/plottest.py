import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ts_benchmark.data.dataprocessor.getTimeRange import read_excel_data_byDate
import networkx as nx
import ts_benchmark.data.dataprocessor.extra as ex
from ts_benchmark.common.constant import ROOT_PATH
import os


def test():
    groundSensorID =["GS10-6","GS10-7","GS10-8","GS10-9","GS10-1","GS10-2","GS10-3","GS10-4","GS10-5","GS8-1","GS8-10","GS8-2","GS8-3","GS8-5","GS8-6","GS8-7","GS8-8","GS8-9","GS9-1","GS9-10","GS9-2","GS9-5","GS9-6","GS9-7","GS9-8","GS9-9"]

    tunnelSensorID = ['TSA1-01', 'TSA1-02', 'TSA1-03', 'TSA1-04', 'TSA1-05', 'TSA1-06', 'TSA1-07', 'TSA1-08', 'TSA1-09', 'TSA1-10', 'TSA1-11', 'TSA1-12', 'TSA1-13', 'TSA1-14', 'TSA1-15', 'TSA1-16', 'TSA1-17', 'TSA1-18', 'TSA1-19', 'TSA1-20', 'TSA1-21', 'TSA1-22', 'TSA1-23', 'TSA1-24', 'TSA1-25', 'TSA1-26', 'TSA1-27', 'TSA1-28', 'TSA1-29', 'TSA1-30', 'TSA1-31', 'TSA1-32', 'TSA1-33', 'TSA1-34', 'TSA1-35', 'TSA1-36', 'TSA1-37', 'TSA1-38', 'TSA1-39', 'TSA1-40', 'TSA1-41', 'TSA1-42', 'TSA1-43', 'TSA1-44', 'TSA1-45', 'TSA1-46', 'TSA1-47', 'TSA1-48', 'TSA1-49', 'TSA1-50', 'TSA1-51', 'TSA1-52', 'TSA1-53', 'TSA1-54', 'TSA1-55', 'TSA1-56', 'TSA1-57', 'TSA1-58', 'TSA1-59', 'TSA1-60', 'TSA1-61', 'TSA1-62', 'TSA1-63', 'TSA1-64', 'TSA1-65', 'TSA1-66', 'TSA1-67', 'TSA1-68', 'TSA1-69', 'TSA1-70', 'TSA1-70', 'TSA1-71', 'TSA1-72', 'TSA1-73', 'TSA1-74', 'TSA1-75']
    sheet_name = ['GroundSettlement', 'B1SettleM', 'B2SettleM', 'A1SettleM', 'A2SettleM']
    data_path, result_path, correlation_path, position_path, range_path = (
        ex.getFilePathList()
    )

    excel_file = pd.ExcelFile(position_path)
    excel_data = excel_file
    df_GSPosition = excel_data.parse('GS_XY')
    df_TSPosition = excel_data.parse('TS_A1_M_XY')

    GS_data=read_excel_data_byDate(data_path,sheet_name[0])
    TS_data=read_excel_data_byDate(data_path,sheet_name[3])

    DateList=['2021-04-01','2021-06-01','2021-08-01','2021-10-01','2021-12-01']
    GS4Plot=GS_data.get_group(DateList[0])
    TS4Plot=TS_data.get_group(DateList[0])

    x=[]
    y=[]
    z=[]
    label=[]

    for groundID in groundSensorID:
        x.append(df_GSPosition[df_GSPosition['sensorID']==groundID]['x_position'].values[0])
        y.append(df_GSPosition[df_GSPosition['sensorID']==groundID]['y_position'].values[0])
        z.append(GS4Plot[GS4Plot['sensorID']==groundID]['value'].values[0])
        label.append(groundID)

    for tunnelID in tunnelSensorID:
        x.append(df_TSPosition[df_TSPosition['sensorID']==tunnelID]['x_position'].values[0])
        y.append(df_TSPosition[df_TSPosition['sensorID']==tunnelID]['y_position'].values[0])
        z.append(TS4Plot[TS4Plot['sensorID']==tunnelID]['value'].values[0])
        label.append(tunnelID)

    # transform list to numpy array
    x=np.array(x)
    y=np.array(y)
    z=np.array(z)

def read_excel(file_path,sheet_name):
    # read the data from the excel file
    excel_file = pd.ExcelFile(file_path)
    excel_data = excel_file
    df = excel_data.parse(sheet_name)
    return df


def plotNetwork(figureIndex, relation_sheet, result=None):
    """
    plot the network graph of the correlation matrix
    figureIndex: int, the index of the figure
    relation_sheet: str, the sheet name of the correlation matrix
    """
    testIter = 1
    dat_path_path, result_path, correlation_path, position_path, range_path = (
        ex.getFilePathList()
    )
    position_sheet_list = ["GS_XY", "TS_A1_M_XY"]

    # Read correlation matrix
    if result is not None:
        correlation_matrix = result
    else:
        correlation_matrix = read_excel(correlation_path, relation_sheet)
    groundPosition = read_excel(position_path, position_sheet_list[0])
    tunnelPosition = read_excel(position_path, position_sheet_list[1])

    groundSensorID =["GS10-1","GS10-2","GS10-3","GS10-4","GS10-5","GS10-6","GS10-7","GS10-8","GS10-9","GS8-1","GS8-10","GS8-2","GS8-3","GS8-5","GS8-6","GS8-7","GS8-8","GS8-9","GS9-1","GS9-10","GS9-2","GS9-5","GS9-6","GS9-7","GS9-8","GS9-9"]

    # tunnelSensorID = ['TSA1-01', 'TSA1-02', 'TSA1-03', 'TSA1-04', 'TSA1-05', 'TSA1-06', 'TSA1-07', 'TSA1-08', 'TSA1-09', 'TSA1-10', 'TSA1-11', 'TSA1-12', 'TSA1-13', 'TSA1-14', 'TSA1-15', 'TSA1-16', 'TSA1-17', 'TSA1-18', 'TSA1-19', 'TSA1-20', 'TSA1-21', 'TSA1-22', 'TSA1-23', 'TSA1-24', 'TSA1-25', 'TSA1-26', 'TSA1-27', 'TSA1-28', 'TSA1-29', 'TSA1-30', 'TSA1-31', 'TSA1-32', 'TSA1-33', 'TSA1-34', 'TSA1-35', 'TSA1-36', 'TSA1-37', 'TSA1-38', 'TSA1-39', 'TSA1-40', 'TSA1-41', 'TSA1-42', 'TSA1-43', 'TSA1-44', 'TSA1-45', 'TSA1-46', 'TSA1-47', 'TSA1-48', 'TSA1-49', 'TSA1-50', 'TSA1-51', 'TSA1-52', 'TSA1-53', 'TSA1-54', 'TSA1-55', 'TSA1-56', 'TSA1-57', 'TSA1-58', 'TSA1-59', 'TSA1-60', 'TSA1-61', 'TSA1-62', 'TSA1-63', 'TSA1-64', 'TSA1-65', 'TSA1-66', 'TSA1-67', 'TSA1-68', 'TSA1-69', 'TSA1-70', 'TSA1-71', 'TSA1-72', 'TSA1-73', 'TSA1-74', 'TSA1-75'] # Sensors in tunnelA1

    tunnelSensorID = ['TSA1-01', 'TSA1-02', 'TSA1-03', 'TSA1-04', 'TSA1-05', 'TSA1-06', 'TSA1-07', 'TSA1-08', 'TSA1-09', 'TSA1-10', 'TSA1-11', 'TSA1-12', 'TSA1-13', 'TSA1-14','TSA1-15', 'TSA1-16', 'TSA1-17', 'TSA1-18', 'TSA1-19', 'TSA1-20', 'TSA1-21', 'TSA1-22', 'TSA1-23', 'TSA1-24', 'TSA1-25', 'TSA1-26', 'TSA1-27', 'TSA1-28', 'TSA1-29', 'TSA1-30', 'TSA1-31', 'TSA1-32', 'TSA1-33', 'TSA1-34', 'TSA1-35', 'TSA1-36', 'TSA1-37', 'TSA1-38', 'TSA1-39', 'TSA1-40', 'TSA1-41', 'TSA1-42', 'TSA1-43', 'TSA1-44', 'TSA1-45', 'TSA1-46', 'TSA1-47', 'TSA1-48', 'TSA1-49', 'TSA1-50','TSA1-51', 'TSA1-52', 'TSA1-53', 'TSA1-54', 'TSA1-55', 'TSA1-56', 'TSA1-57', 'TSA1-58', 'TSA1-59', 'TSA1-60','TSA1-61', 'TSA1-62', 'TSA1-63', 'TSA1-64', 'TSA1-65', 'TSA1-66', 'TSA1-67', 'TSA1-68', 'TSA1-69', 'TSA1-70'] # Sensors in tunnelA1

    # Example sensor positions (replace with your data)
    nodePositions = []
    for sensorID in groundSensorID:
        x = groundPosition[groundPosition['sensorID']==sensorID]['x_position'].values[0]/100
        y = groundPosition[groundPosition['sensorID']==sensorID]['y_position'].values[0]/100
        nodePositions.append((x,y))
    for sensorID in tunnelSensorID:
        x = tunnelPosition[tunnelPosition['sensorID']==sensorID]['x_position'].values[0]/100
        y = tunnelPosition[tunnelPosition['sensorID']==sensorID]['y_position'].values[0]/100
        nodePositions.append((x,y))

    # reorganise the correlation matrix in case of disorder sensorID
    relationMatrix = np.zeros((len(tunnelSensorID), len(groundSensorID)))
    i=0
    if result is not None:
        for tunnelID in tunnelSensorID:
            j = 0
            for groundID in groundSensorID:
                relation = result.loc[
                    (result["tunnelID"] == tunnelID) & (result["groundID"] == groundID)
                ]["relation"].values[0]
                relationMatrix[i][j] = relation
                j += 1
            i += 1
    else:
        for tunnelID in tunnelSensorID:
            j = 0
            for groundID in groundSensorID:
                relationMatrix[i][j] = correlation_matrix.loc[
                    (correlation_matrix["tunnelID"] == tunnelID), groundID
                ].values[0]
                j += 1
            i += 1

    # Create a graph
    G = nx.Graph()

    plt.figure(figsize=(16, 8),dpi=300)

    # Add nodes with positions
    for index in range(len(nodePositions)):
        G.add_node(index, pos=nodePositions[index])

    # Add edges based on the correlation matrix
    for i in range(len(tunnelSensorID)):
        for j in range(len(groundSensorID)):
            if relationMatrix[i][j] == 1:
                G.add_edge(i+len(groundSensorID), j)

    # Get positions for drawing
    pos = nx.get_node_attributes(G, 'pos')

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='skyblue')

    # Draw the edges
    nx.draw_networkx_edges(G, pos,edge_color='gray')

    # Draw node labels (sensor IDs)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')

    # Remove axes for clarity
    plt.axis('off')  

    # Show the plot
    figname = os.path.join(ROOT_PATH, "result/image", str(figureIndex) + ".png")
    plt.savefig(figname)
    print("Plot saved as", figname)
