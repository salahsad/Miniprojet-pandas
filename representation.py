import geopandas
import matplotlib.pyplot as plt
import pandas as pd


def data_world():
    dataframe = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    pd.set_option("display.max_columns",50)
    pd.set_option("display.max_rows",300)
    pd.set_option("display.width",1000)
    dataframe = dataframe.set_index('name')
    return dataframe
