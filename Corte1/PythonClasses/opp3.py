import math

class Trigonometria:

    def seno(self, angle_rad):
        return math.sin(angle_rad)

    def coseno(self, angle_rad):
        return math.cos(angle_rad)

    def tangente(self, angle_rad):
        try:
            return math.tan(angle_rad)
        except:
            return "No se puede calcular la tangente"

    # Opcional: convertir grados a radianes
    def gradosarad(self, degrees):
        return math.radians(degrees)
