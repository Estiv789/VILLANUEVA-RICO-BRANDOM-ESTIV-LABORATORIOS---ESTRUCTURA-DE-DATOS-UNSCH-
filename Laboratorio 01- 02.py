# 1) Operaciones Básicas
def operaciones_basicas():
    # Solicitar al usuario dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Calcular las operaciones básicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    # Manejo de división por cero
    if num2 != 0:
        division = num1 / num2

        # Imprimir resultados
        print("--------------------------------------")
        print("SUMA:          ", num1, "+", num2, "=", suma)
        print("RESTA:         ", num1, "-", num2, "=", resta)
        print("MULTIPLICACIÓN:", num1, "x", num2, "=", multiplicacion)
        print("DIVISIÓN:      ", num1, "/", num2, "=", division)
    else:
        print("No se puede dividir por cero.")

# Llamar a la función para realizar operaciones básicas
operaciones_basicas()

# 2) Verificación de Número Par o Impar
def par_o_impar():
    # Solicitar al usuario un número
    numero = int(input("Ingrese un número: "))

    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

# Llamar a la función para verificar si un número es par o impar
par_o_impar()

# 3) Área de un Triángulo
def area_triangulo():
    # Solicitar al usuario la base y la altura del triángulo
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    # Calcular el área del triángulo
    area = (base * altura) / 2

    # Imprimir el área del triángulo
    print(f"El área del triángulo es: {area}")

# Llamar a la función para calcular el área del triángulo
area_triangulo()

# 4) Calculadora de Factorial
# Función para calcular el factorial de un número
def calcular_factorial(numero):
    factorial = 1

    # Verificar si el número es negativo
    if numero < 0:
        print("No se puede calcular el factorial de números negativos.")
    elif numero == 0:  # Si el número es 0, el factorial es 1
        return 1
    else:
        # Calcular el factorial del número dado
        for i in range(1, numero + 1):
            factorial *= i
    return factorial

#EJECUTAMOS EL PROGRAMA
num_factorial = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {num_factorial} es: {calcular_factorial(num_factorial)}")

# 5) Número Primo
# Solicitar al usuario un número para verificar si es primo
num_primo = int(input("Ingrese un número para verificar si es primo: "))

# Verificar si el número es primo
if num_primo < 2:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(num_primo ** 0.5) + 1):
        if num_primo % i == 0:
            es_primo = False
            break

# Imprimir el resultado
if es_primo:
    print(f"{num_primo} es un número primo.")
else:
    print(f"{num_primo} no es un número primo.")

# 6) Inversión de Cadena
# Solicitar al usuario una cadena de texto para invertir
cadena_original = input("Ingrese una cadena de texto para invertir: ")

# Inicializar una cadena vacía para almacenar la inversión
cadena_invertida = ""

# Iterar sobre la cadena original en orden inverso
for i in range(len(cadena_original) - 1, -1, -1):
    # Agregar cada carácter al principio de la cadena invertida
    cadena_invertida += cadena_original[i]

# Imprimir la inversión de la cadena original
print(f"Inversión de la cadena: {cadena_invertida}")

# 7) Suma de Números Pares
# Solicitar al usuario el inicio y el final del rango
rango_inicio = int(input("Ingrese el inicio del rango: "))
rango_fin = int(input("Ingrese el final del rango: "))

# Inicializar la suma de los números pares en el rango
suma = 0

# Iterar a través del rango dado
for num in range(rango_inicio, rango_fin + 1):
    # Verificar si el número es par
    if num % 2 == 0:
        # Si es par, agregarlo a la suma
        suma += num

# Imprimir la suma de los números pares en el rango
print(f"La suma de los números pares en el rango es: {suma}")

# 8) Lista de Cuadrados
# Inicializar una lista vacía para almacenar los cuadrados de los primeros 10 números naturales
cuadrados = []

# Calcular los cuadrados de los números del 1 al 10 e insertarlos en la lista
for i in range(1, 11):
    cuadrado = i ** 2
    cuadrados.append(cuadrado)

# Imprimir la lista de cuadrados de los primeros 10 números naturales
print("Lista de cuadrados de los primeros 10 números naturales:", cuadrados)

# 9) Contador de Vocales
# Solicitar al usuario que ingrese una cadena de texto para contar las vocales
cadena_vocales = input("Ingrese una cadena de texto para contar vocales: ")

# Definir las vocales en mayúsculas y minúsculas
vocales = "aeiouAEIOU"

# Inicializar el contador de vocales
num_vocales = 0

# Iterar sobre cada carácter en la cadena de texto
for char in cadena_vocales:
    # Verificar si el carácter es una vocal
    if char in vocales:
        # Incrementar el contador de vocales si el carácter es una vocal
        num_vocales += 1

# Imprimir el número de vocales encontradas en la cadena
print(f"Número de vocales en la cadena: {num_vocales}")

# 10) Números de la Serie Fibonacci
def fibonacci(n):
    # Si se solicitan menos de 1 número en la serie Fibonacci, retornar una lista vacía
    if n <= 0:
        return []
    # Si se solicita exactamente 1 número en la serie Fibonacci, retornar [0]
    elif n == 1:
        return [0]
    # Si se solicitan exactamente 2 números en la serie Fibonacci, retornar [0, 1]
    elif n == 2:
        return [0, 1]
    else:
        # Inicializar la lista de Fibonacci con los dos primeros números
        fib = [0, 1]
        # Calcular los siguientes números en la serie Fibonacci
        for _ in range(2, n):
            # Agregar el siguiente número en la serie como la suma de los dos últimos números
            fib.append(fib[-1] + fib[-2])
        # Retornar la lista de Fibonacci completa
        return fib

# Imprimir los primeros 10 números de la serie Fibonacci
print("Primeros 10 números de la serie Fibonacci:", fibonacci(10))

# 11) Ordenamiento de Lista
def ordenar_lista(lista):
    # Obtener la longitud de la lista
    n = len(lista)

    # Iterar sobre la lista
    for i in range(n - 1):
        # Encontrar el índice del elemento más pequeño en el segmento no ordenado
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        # Intercambiar el elemento más pequeño con el primer elemento del segmento no ordenado
        lista[i], lista[min_index] = lista[min_index], lista[i]

    # Devolver la lista ordenada
    return lista

# Solicitar al usuario que ingrese números separados por espacio para ordenar
numeros = input("Ingrese números separados por espacio para ordenar: ").split()
lista_desordenada = [int(x) for x in numeros]

# Llamar a la función de ordenamiento y mostrar la lista ordenada
print("Lista ordenada:", ordenar_lista(lista_desordenada))

# 12) Palíndromo
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Convertir la palabra a minúsculas
palabra = palabra.lower()

es_palindromo = True
longitud = len(palabra)

# Verificar si la palabra es un palíndromo
for i in range(longitud // 2):
    if palabra[i] != palabra[longitud - i - 1]:
        es_palindromo = False
        break

if es_palindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

# 13) Generador de Tablas de Multiplicar
# Solicitar al usuario un número para generar su tabla de multiplicar
num_tabla_multiplicar = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Imprimir encabezado de la tabla
print(f"Tabla de multiplicar de {num_tabla_multiplicar}:")

# Generar y mostrar la tabla de multiplicar
for i in range(1, 13):
    resultado = num_tabla_multiplicar * i
    print(f"{num_tabla_multiplicar} x {i} = {resultado}")

# 14) Cálculo del Área de un Círculo
import math

def area_circulo(radio):
    return math.pi * radio**2
#EJECUTAMOS EL PROGRAMA
radio_circulo = float(input("Ingrese el radio de un círculo para calcular su área: "))
print(f"El área del círculo es: {area_circulo(radio_circulo)}")

# 15) Suma de Dígitos
def suma_digitos(numero):
    numero = abs(numero)
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

#EJECUTAMOS EL PROGRAMA
num_suma_digitos = int(input("Ingrese un número entero para calcular la suma de sus dígitos: "))
print(f"La suma de los dígitos es: {suma_digitos(num_suma_digitos)}")

