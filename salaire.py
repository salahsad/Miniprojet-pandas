import pandas as pd
def salaire_par_pays():
    #recuperer les données shouaité
    salaire= pd.read_csv("1.1 min_wages.csv",index_col=0)
    salaire= salaire.set_index('Country')
    salaire= salaire.loc[:,['Workweek (hours)[2]','Nominal hourly (US$)[6]']]
    salaire.columns = ['nbr_h/s','dollar/h']

    #affichage du dataframe
    pd.set_option("display.max_columns",50)
    pd.set_option("display.max_rows",300)
    pd.set_option("display.width",1000)

    return salaire