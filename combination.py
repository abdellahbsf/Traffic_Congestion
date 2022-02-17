from itertools import combinations
import pandas as pd
import sys

data=pd.read_csv('F:\Data\Casa\WazeRouteCalc\data_address\data_coord.csv')

data_n=data.drop(index=(105))
data_n=data_n.drop(index=(106))
data_n=data_n.drop(index=(107))
data_n=data_n.drop(index=(108))
data_n=data_n.drop(index=(109))



Mat= []
k = 0
for i in range(22):

    # Append an empty sublist inside the list
    Mat.append([])
    #
    coordinates = data_n['Lat_Long'][k:k+5]

    for coord in coordinates:
        Mat[i].append(coord)
    k = k + 5