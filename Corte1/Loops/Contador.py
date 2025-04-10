times = input("Ingrese un numero: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("Error cero")
else:
    for i in range(1,times+1):
        print("i = ", i)