import pandas as pd
df = pd.read_csv('Cities.csv')
print(df['City']) # Para mostrar una columna en especifico, no imprime el encabezado 
print(df[['City','Population']]) #Dos columnas, si imprime el cabezado,[[]]
