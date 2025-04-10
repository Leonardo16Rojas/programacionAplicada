import csv
import time
import keyboard  

filename = 'numeros.csv'
paso = 0.01
valor = paso

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Numero'])

try:
    while True:
        if keyboard.is_pressed('z'):
            print("\nProceso finalizado por el usuario con la tecla 'z'.")
            break
        if valor >= 1:
            valor = paso
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([round(valor, 5)])
        print(f"Guardado: {round(valor, 5)}")
        valor += paso
        time.sleep(0.5)
except Exception as e:
    print(f"\nError: {e}")
