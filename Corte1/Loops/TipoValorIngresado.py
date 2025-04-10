a = input("Ingrese primer numero: ")
a = int(a)
b = input("Ingrese segundo numero: ")
b = float(b)
c = a + b

if a == b:
    print("Igual")
else:
    print("Diferente")

print("El primer valor es tipo: ", type(a))
print("El segundo valor es tipo: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("El primero y el segundo son del mismo tipo")
else:
    print("El primero y el segundo son de diferente tipo")