while True:

    value = int(input("Ingrese un numero positivo: "))
    print("Numero: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        print(f'El factorial de {value} es: ', fact)
    else:
        print("Error, Ingrese un numero positivo por favor")