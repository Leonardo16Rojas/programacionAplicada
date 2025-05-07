class Calculator:#Python usa class Calcualtor: en lugar de public class Calculator { }

    def __init__(self):#Se usa def en lugar de especificar el tipo de retorno
        # Todos los métodos de instancia llevan self como primer parámetro
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
        except ZeroDivisionError: #Execpcion tipica de python
           return "No se puede dividir entre cero"
    # Si quisiera la division entera como en Java, deberias usar //  (return a // b)
       

    def modulo(self, a, b):  # Metodo para obtener el modulo
        try:
          return a % b
        except ZeroDivisionError:
          return "No se puede calcular el módulo por cero"

  #Python usa if __name__ == "__main__": para el punto de entrada
if __name__ == "__main__": # El equivalente al main de Java en Python es este bloque if,
    my_calculator = Calculator()  # Crear instancia de la calculadora
  
    # Llamar a los métodos y mostrar resultados
    print(my_calculator.add(5, 7)) #No se declara el tipo de variable
    print(my_calculator.substract(45, 11)) #No se usa new, solo se llama a la clase como si fuera una función
    print(my_calculator.multiply(3, 2))
    print(my_calculator.divide(12,0))
    print(my_calculator.divide(12,47))
