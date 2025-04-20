import pandas as pd
df = pd.read_csv('Cities.csv')
#print("Ciudades por la letra C")
#resultado = df[df['City'].str.startswith('C')] #buscar en especifico, en este caso por letra
#print(resultado)


opcion = int(input("Escoja: \n1 para buscar en city\n2 para buscar en country\n"))


if opcion == 1:
    letra = input("¿Por qué letra quieres buscar la ciudad? ").upper() # el .upper() se usa para que no importe si escribe minúscula
    resultado = df[df['City'].str.startswith(letra)] 
    print(resultado)

elif opcion == 2:
    letra = input("¿Por qué letra quieres buscar el pais? ").upper()
    resultado = df[df['Country'].str.startswith(letra)] 
    print(resultado)

else:
    print("Opción no válida. Solo se puede elegir 1 o 2.")

