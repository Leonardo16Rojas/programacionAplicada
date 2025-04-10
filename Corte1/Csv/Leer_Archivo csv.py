import csv
import time

filename = 'numeros.csv'

try:
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for fila in reader:
            numero = float(fila[0])
            print(f'Número leído: {numero}')
            time.sleep(0.5)  
except FileNotFoundError:
    print(f"No se encontró el archivo '{filename}'.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
