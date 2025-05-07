class Calculator:#Python usa class Calcualtor: en lugar de public class Calculator { }

    def __init__(self):#Se usa def en lugar de especificar el tipo de retorno
        # Todos los métodos de instancia llevan self como primer parámetro, p
        pass  # pass indica que no hace nada, como los {} vacíos en Java
    
    def add(self, a, b):   # Método para sumar dos números
        # self es equivalente a this en Java, pero en Python es explícito
        return a + b #No se declaran tipos de retorno
    
    def substract(self, a, b):# Método para restar dos números
        return a - b
    
    def multiply(self, a, b): # Método para multiplicar dos números
        return a * b
    
    def divide(self, a, b): # Metodo para dividir dos numeros
        try:
           return a / b # Nota: En Python la division de enteros con / devuelve float
        except ZeroDivisionError: #Execpcion de python
           return "No se puede dividir entre cero"
    # Si quisiera la division entera como en Java, deberias usar //  (return a // b)
       

    def modulo(self, a, b):  # Metodo para obtener el modulo
        try:
          return a % b
        except ZeroDivisionError:
          return "No se puede calcular el módulo por cero"

  
