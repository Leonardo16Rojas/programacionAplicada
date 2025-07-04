import csv
import matplotlib.pyplot as plt
import numpy as np

# Conversión aproximada de grados a metros
meters_per_deg_lat = 111320

# Leer datos
with open("Datosgps.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Tomar el primer punto como origen
lat0 = float(data[0]['latitude'])
lon0 = float(data[0]['longitude'])
meters_per_deg_lon = 111320 * np.cos(np.radians(lat0))

# listas para coordenadas polares
angles = []
radii = []

for row in data:
    lat = float(row['latitude'])
    lon = float(row['longitude'])
    
    delta_lat = lat - lat0
    delta_lon = lon - lon0
    
    dx = delta_lon * meters_per_deg_lon
    dy = delta_lat * meters_per_deg_lat
    
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    
    angles.append(theta)
    radii.append(r)

# Graficar
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
ax.scatter(angles, radii, c='blue', marker='o', s=50)

ax.set_title("Diagrama polar de coordenadas desde el primer punto")
ax.set_rmax(10)  # radio máximo 20 metros
ax.grid(True)

plt.show()
