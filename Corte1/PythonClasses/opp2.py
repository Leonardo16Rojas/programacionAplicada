import math
class calculatoravance:

    def __init__(self):
        pass  # No se necesita inicializar nada por ahora

    def raizcua(self, a):
        if a < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo"
        return math.sqrt(a)

    def potencia(self, base, exponent):
        return math.pow(base, exponent)

    def logarito(self, a, base=math.e):
        if a <= 0:
            return "El logaritmo solo está definido para números positivos"
        try:
            return math.log(a, base)
        except ValueError:
            return "Base inválida para logaritmo"