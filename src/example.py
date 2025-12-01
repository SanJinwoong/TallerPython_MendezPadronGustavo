import pandas as pd
import numpy as np

df=pd.read_excel('datos.xlsx')
print(df.head())    

df['promedio']=df[['Parcial 1', 'Parcial 2', 'Parcial 3']].mean(axis=1)
df['estatus']=np.where(df['promedio']>=7.5,'Aprobado','Reprobado')

x=0