class Calculadora: 

    def __init__(self, valor1, valor2): 

        self.valor1 = valor1 

        self.valor2 = valor2 

 

    def suma(self): 

        return self.valor1 + self.valor2 

 

    def resta(self): 

        return self.valor1 - self.valor2 

 

    def multiplicacion(self): 

        return self.valor1 * self.valor2 

 

    def division(self): 

        if self.valor2 != 0: 

            return self.valor1 / self.valor2 

        else: 

            return "No se puede dividir por cero." 

 

# Solicitar al usuario que ingrese dos valores enteros 

valor1 = int(input("Ingrese el primer valor entero: ")) 

valor2 = int(input("Ingrese el segundo valor entero: ")) 

 

# Crear una instancia de la clase Calculadora 

calculadora = Calculadora(valor1, valor2) 

 

# Realizar las operaciones e imprimir los resultados 

print("Suma:", calculadora.suma()) 

print("Resta:", calculadora.resta()) 

print("Multiplicación:", calculadora.multiplicacion()) 

print("División:", calculadora.division()) 
#samuelIbarra