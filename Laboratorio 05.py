# Ejercicio 01: Números Primos
def numeros_primos(conjunto_numeros):
    """
    Devuelve un conjunto con los números primos del conjunto dado.
    """
    primos = set()
    for num in conjunto_numeros:
        if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primos.add(num)
    return primos

# Ejercicio 02: Palabras que Comienzan con una Letra
def palabras_con_letra(conjunto_palabras, letra):
    """
    Devuelve un conjunto con las palabras que comienzan con la letra especificada.
    """
    # Inicializar un conjunto vacío para almacenar las palabras seleccionadas
    palabras_seleccionadas = set()

    # Iterar sobre cada palabra en el conjunto de palabras dado
    for palabra in conjunto_palabras:
        # Verificar si la palabra comienza con la letra especificada
        if palabra.startswith(letra):
            # Si es así, agregar la palabra al conjunto de palabras seleccionadas
            palabras_seleccionadas.add(palabra)

    # Devolver el conjunto de palabras seleccionadas
    return palabras_seleccionadas

# Ejercicio 03: Números Divisibles por un Número Determinado
def numeros_divisibles(conjunto_numeros, divisor):
    """
    Devuelve un conjunto con los números del conjunto dado que son divisibles por el divisor dado.
    """
    return {num for num in conjunto_numeros if num % divisor == 0}

# Ejercicio 04: Números en Ambos Conjuntos
def numeros_en_ambos_conjuntos(conjunto1, conjunto2):
    """
    Devuelve un conjunto con los números que están en ambos conjuntos.
    """
    return conjunto1.intersection(conjunto2)

# Ejercicio 05: Números en el Primer Conjunto pero no en el Segundo
def numeros_en_primer_no_segundo(conjunto1, conjunto2):
    """
    Devuelve un conjunto con los números que están en el primer conjunto pero no en el segundo.
    """
    return conjunto1.difference(conjunto2)

# Ejercicio 06: Números en el Segundo Conjunto pero no en el Primero
def numeros_en_segundo_no_primer(conjunto1, conjunto2):
    """
    Devuelve un conjunto con los números que están en el segundo conjunto pero no en el primero.
    """
    return conjunto2.difference(conjunto1)

# Ejercicio 07: Palabras Anagramas
def palabras_anagramas(conjunto_palabras):
    """
    Devuelve un conjunto con las palabras que son anagramas.
    """
    anagramas = set()
    sorted_words = [''.join(sorted(word)) for word in conjunto_palabras]
    for i, word in enumerate(conjunto_palabras):
        if sorted_words.count(sorted_words[i]) > 1:
            anagramas.add(word)
    return anagramas

# Ejercicio 08: Palabras Palíndromos
def palabras_palindromos(conjunto_palabras):
    """
    Devuelve un conjunto con las palabras que son palíndromos.
    """
    return {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}

# Ejercicio 09: Palabras con Longitud Determinada
def palabras_longitud(conjunto_palabras, longitud):
    """
    Devuelve un conjunto con las palabras que tienen una longitud determinada.
    """
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud}

# Ejercicio 10: Palabras que Contienen una Letra Determinada
def palabras_con_letra(conjunto_palabras, letra):
    """
    Devuelve un conjunto con las palabras que contienen la letra especificada.
    """
    return {palabra for palabra in conjunto_palabras if letra in palabra}

# Ejercicio 11: Números Ordenados de Menor a Mayor
def numeros_ordenados_menor_mayor(conjunto_numeros):
    """
    Devuelve una lista con los números ordenados de menor a mayor.
    """
    return sorted(conjunto_numeros)

# Ejercicio 12: Números Ordenados de Mayor a Menor
def numeros_ordenados_mayor_menor(conjunto_numeros):
    """
    Devuelve una lista con los números ordenados de mayor a menor.
    """
    return sorted(conjunto_numeros, reverse=True)

# Ejercicio 13: Números Duplicados
def numeros_duplicados(conjunto_numeros):
    """
    Devuelve un conjunto con los números que están duplicados.
    """
    duplicados = set()
    unicos = set()
    for num in conjunto_numeros:
        if num in unicos:
            duplicados.add(num)
        else:
            unicos.add(num)
    return duplicados

# Ejercicio 14: Números no Duplicados
def numeros_no_duplicados(conjunto_numeros):
    """
    Devuelve un conjunto con los números que no están duplicados.
    """
    unicos = set()
    for num in conjunto_numeros:
        unicos.add(num)
    return unicos

# Ejercicio 15: Números Primos Ordenados de Menor a Mayor
def primos_ordenados_menor_mayor(conjunto_numeros):
    """
    Devuelve una lista con los números primos ordenados de menor a mayor.
    """
    primos = numeros_primos(conjunto_numeros)
    return sorted(primos)

# Ejercicio 16: Palíndromos Ordenados de Menor a Mayor
def palindromos_ordenados_menor_mayor(conjunto_palabras):
    """
    Devuelve una lista con las palabras palíndromos ordenadas de menor a mayor.
    """
    palindromos = palabras_palindromos(conjunto_palabras)
    return sorted(palindromos)

# Ejercicio 17: Palabras con Longitud Determinada y Ordenadas de Menor a Mayor
def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    """
    Devuelve una lista con las palabras que tienen una longitud determinada, ordenadas de menor a mayor.
    """
    palabras_filtradas = palabras_longitud(conjunto_palabras, longitud)
    return sorted(palabras_filtradas)

# Ejercicio 18: Palabras con Letra Determinada y Ordenadas de Mayor a Menor
def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    """
    Devuelve una lista con las palabras que contienen la letra especificada, ordenadas de mayor a menor.
    """
    palabras_filtradas = palabras_con_letra(conjunto_palabras, letra)
    return sorted(palabras_filtradas, reverse=True)

# Ejercicio 19: Números Ordenados de Menor a Mayor y no Duplicados
def numeros_ordenados_no_duplicados(conjunto_numeros):
    """
    Devuelve una lista con los números ordenados de menor a mayor y que no están duplicados.
    """
    return sorted(set(conjunto_numeros))

# Ejercicio 20: Palíndromos, Longitud Determinada y Ordenados de Menor a Mayor
def palindromos_longitud_ordenados(conjunto_palabras, longitud):
    """
    Devuelve una lista con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.
    """
    palindromos = palabras_palindromos(conjunto_palabras)
    palindromos_longitud = palabras_longitud(palindromos, longitud)
    return sorted(palindromos_longitud)

#-------------------------------------------------------------------------------
#EJECUTANDO LOS PROGRAMAS
#-------------------------------------------------------------------------------

# Ejercicio 01: Números Primos
conjunto_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Ejercicio 01: Números Primos")
print("Números primos:", numeros_primos(conjunto_numeros))

# Ejercicio 02: Palabras que Comienzan con una Letra
conjunto_palabras = {"python", "programación", "ciencia", "datos", "inteligencia"}
letra = "p"
print("Ejercicio 02: Palabras que Comienzan con una Letra")
print("Palabras que comienzan con la letra 'p':", palabras_con_letra(conjunto_palabras, letra))

# Ejercicio 03: Números Divisibles por un Número Determinado
conjunto_numeros = {10, 15, 20, 25, 30}
divisor = 5
print("Ejercicio 03: Números Divisibles por un Número Determinado")
print("Números divisibles por 5:", numeros_divisibles(conjunto_numeros, divisor))

# Ejercicio 04: Números en Ambos Conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print("Ejercicio 04: Números en Ambos Conjuntos")
print("Números en ambos conjuntos:", numeros_en_ambos_conjuntos(conjunto1, conjunto2))

# Ejercicio 05: Números en el Primer Conjunto pero no en el Segundo
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print("Ejercicio 05: Números en el Primer Conjunto pero no en el Segundo")
print("Números en el primer conjunto pero no en el segundo:", numeros_en_primer_no_segundo(conjunto1, conjunto2))

# Ejercicio 06: Números en el Segundo Conjunto pero no en el Primero
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print("Ejercicio 06: Números en el Segundo Conjunto pero no en el Primero")
print("Números en el segundo conjunto pero no en el primero:", numeros_en_segundo_no_primer(conjunto1, conjunto2))

# Ejercicio 07: Palabras Anagramas
conjunto_palabras = {"tar", "rat", "casa", "saca", "arbol", "bolar"}
print("Ejercicio 07: Palabras Anagramas")
print("Palabras que son anagramas:", palabras_anagramas(conjunto_palabras))

# Ejercicio 08: Palabras Palíndromos
conjunto_palabras = {"reconocer", "oso", "casa", "radar", "solos"}
print("Ejercicio 08: Palabras Palíndromos")
print("Palabras que son palíndromos:", palabras_palindromos(conjunto_palabras))

# Ejercicio 09: Palabras con Longitud Determinada
conjunto_palabras = {"python", "programación", "ciencia", "datos", "inteligencia"}
longitud = 7
print("Ejercicio 09: Palabras con Longitud Determinada")
print("Palabras con longitud 7:", palabras_longitud(conjunto_palabras, longitud))

# Ejercicio 10: Palabras que Contienen una Letra Determinada
conjunto_palabras = {"python", "programación", "ciencia", "datos", "inteligencia"}
letra = "i"
print("Ejercicio 10: Palabras que Contienen una Letra Determinada")
print("Palabras que contienen la letra 'i':", palabras_con_letra(conjunto_palabras, letra))

# Ejercicio 11: Números Ordenados de Menor a Mayor
conjunto_numeros = {5, 3, 8, 1, 7}
print("Ejercicio 11: Números Ordenados de Menor a Mayor")
print("Números ordenados de menor a mayor:", numeros_ordenados_menor_mayor(conjunto_numeros))

# Ejercicio 12: Números Ordenados de Mayor a Menor
conjunto_numeros = {5, 3, 8, 1, 7}
print("Ejercicio 12: Números Ordenados de Mayor a Menor")
print("Números ordenados de mayor a menor:", numeros_ordenados_mayor_menor(conjunto_numeros))

# Ejercicio 13: Números Duplicados
conjunto_numeros = {1, 2, 3, 4, 3, 5, 2, 6}
print("Ejercicio 13: Números Duplicados")
print("Números duplicados:", numeros_duplicados(conjunto_numeros))

# Ejercicio 14: Números no Duplicados
conjunto_numeros = {1, 2, 3, 4, 3, 5, 2, 6}
print("Ejercicio 14: Números no Duplicados")
print("Números no duplicados:", numeros_no_duplicados(conjunto_numeros))

# Ejercicio 15: Números Primos Ordenados de Menor a Mayor
conjunto_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Ejercicio 15: Números Primos Ordenados de Menor a Mayor")
print("Números primos ordenados de menor a mayor:", primos_ordenados_menor_mayor(conjunto_numeros))

# Ejercicio 16: Palíndromos Ordenados de Menor a Mayor
conjunto_palabras = {"reconocer", "oso", "casa", "radar", "solos"}
print("Ejercicio 16: Palíndromos Ordenados de Menor a Mayor")
print("Palíndromos ordenados de menor a mayor:", palindromos_ordenados_menor_mayor(conjunto_palabras))

# Ejercicio 17: Palabras con Longitud Determinada y Ordenadas de Menor a Mayor
conjunto_palabras = {"python", "programación", "ciencia", "datos", "inteligencia"}
longitud = 6
print("Ejercicio 17: Palabras con Longitud Determinada y Ordenadas de Menor a Mayor")
print("Palabras de longitud 6 ordenadas de menor a mayor:", palabras_longitud_ordenadas(conjunto_palabras, longitud))

# Ejercicio 18: Palabras con Letra Determinada y Ordenadas de Mayor a Menor
conjunto_palabras = {"python", "programación", "ciencia", "datos", "inteligencia"}
letra = "o"
print("Ejercicio 18: Palabras con Letra Determinada y Ordenadas de Mayor a Menor")
print("Palabras con letra 'o' ordenadas de mayor a menor:", palabras_con_letra_ordenadas(conjunto_palabras, letra))

# Ejercicio 19: Números Ordenados de Menor a Mayor y no Duplicados
conjunto_numeros = {5, 3, 8, 1, 7, 3, 2, 8}
print("Ejercicio 19: Números Ordenados de Menor a Mayor y no Duplicados")
print("Números ordenados de menor a mayor y no duplicados:", numeros_ordenados_no_duplicados(conjunto_numeros))

# Ejercicio 20: Palíndromos, Longitud Determinada y Ordenados de Menor a Mayor
conjunto_palabras = {"reconocer", "oso", "casa", "radar", "solos", "arriba"}
longitud = 5
print("Ejercicio 20: Palíndromos, Longitud Determinada y Ordenados de Menor a Mayor")
print("Palíndromos de longitud 5 ordenados de menor a mayor:", palindromos_longitud_ordenados(conjunto_palabras, longitud))

()
