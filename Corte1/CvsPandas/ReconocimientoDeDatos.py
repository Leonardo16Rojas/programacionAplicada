import pandas as pd

df = pd.read_csv("Cities.csv")
print("Primeras fias: \n")
print(df.head())
print("\n Informacion: \n")
print(df.info())
print("\n Estadisticas: \n")
print(df.describe())
