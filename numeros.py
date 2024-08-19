import math

def calcular_factorial(numero):
    return math.factorial(numero)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def es_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

def convertir_a_binario(numero):
    return bin(numero)[2:]

# Solicitar el valor numérico
numero = int(input("Ingrese un número en base 10: "))

#Calcular y mostrar el factorial del valor ingresado
factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")

#Indicar si el número es primo
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

#Indicar si el número es perfecto
if es_perfecto(numero):
    print(f"El número {numero} es perfecto.")
else:
    print(f"El número {numero} no es perfecto.")

#Convertir el número a binario
binario = convertir_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")
