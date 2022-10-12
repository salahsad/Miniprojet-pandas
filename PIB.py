import pandas as pd
import matplotlib.pyplot as plt
from representation import *
from salaire import *

#chargement depuis le CSV file
data_of_pib = pd.read_csv('2.1 gdp_world_data.csv',index_col=0)
data_of_pib = data_of_pib.set_index("Country (or dependent territory)")

#ajout de nouvelles collones
data_of_pib["growth in the last 20 years"] = data_of_pib["2019"] - data_of_pib["2000"]
data_of_pib["pourcentage_growth"] = round(data_of_pib["growth in the last 20 years"] / data_of_pib["2000"] * 100)
data_of_pib = data_of_pib.loc[:,['2000','2019','growth in the last 20 years','pourcentage_growth']]
data_of_pib.columns = ["2000","2019","growth","%-growth"]

#supressions des collones avec NaN
data_of_pib = data_of_pib.dropna()

#jointures avec la carte mondiale
monde = data_world()
index_change = {'United States of America':'United States',
                'Central African Rep.':'Central African Republic',
                'Dem. Rep. Congo' : 'Democratic Republic of the Congo',
                'Dominican Rep.' : 'Dominican Republic',
                'Eq.Guinea': 'Equatorial Guinea',
                'Solomon Is.' :'Solomon Islands',
                 }
monde = monde.rename(index=index_change)
join_data = monde.join(data_of_pib,how="outer")
join_data["capita"] = join_data["growth"] / join_data["pop_est"]




#appel fonction et jointure
s_par_h = salaire_par_pays()
join_data_2 = join_data.join(s_par_h)
join_data_2['dollar/h'] = pd.to_numeric((join_data_2['dollar/h']),errors='coerce')
print(join_data_2)

#tester la corrélation
print(join_data_2.corr(numeric_only=True))


#visualsiation des données
'''join_data.plot('%-growth',legend=True,figsize=(12,4))
plt.show()'''

join_data.plot('capita',legend=True,figsize=(12,4))
plt.show()