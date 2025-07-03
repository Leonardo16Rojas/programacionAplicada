import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo CSV
df = pd.read_csv('gps.csv')

# Extraer datos
speed = df['Speed_m_s']  # Radio (velocidad)
course = df['Course_deg']  # Ángulo (rumbo en grados)
timestamps = pd.to_datetime(df['Timestamp'])

# Convertir rumbo a radianes (Matplotlib usa radianes para diagramas polares)
# Rotar -90° para que 0° sea Norte
theta = np.radians(course - 90)

# Crear diagrama polar
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Graficar puntos (velocidad como radio, rumbo como ángulo)
scatter = ax.scatter(theta, speed, c='blue', s=100, label='Trayectoria GPS')

# Configurar el diagrama polar
ax.set_theta_zero_location('N')  # 0° en el Norte
ax.set_theta_direction(-1)  # Sentido horario (convención náutica)
ax.set_rlabel_position(90)  # Etiquetas radiales en el eje Este
ax.set_title('Diagrama Polar de GPS: Rumbo', pad=20)

# Añadir etiquetas con las marcas temporales
for i, (t, r, ts) in enumerate(zip(theta, speed, timestamps)):
    ax.annotate(f'{ts.strftime("%H:%M:%S")}',
                (t, r), textcoords="offset points", xytext=(5, 5), fontsize=8)

# Mostrar el gráfico
plt.legend()
plt.show()