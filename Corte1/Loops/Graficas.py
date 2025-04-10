import math
from matplotlib import pyplot as plt


numbers_a = [i * (2 * math.pi / 12) for i in range(12)]
numbers_b = [math.sin(x) for x in numbers_a]

plt.plot(numbers_a, numbers_b, marker='o')
plt.title("Señal Senoidal Discreta")
plt.xlabel("Ángulo (radianes)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()
