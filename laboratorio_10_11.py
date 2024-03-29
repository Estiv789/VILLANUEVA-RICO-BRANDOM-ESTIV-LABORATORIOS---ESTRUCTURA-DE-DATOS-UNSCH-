#EJERICIO 01
#DUPLICAR NODOS
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.previo = None
        self.siguiente = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        # Método para agregar un nuevo nodo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo será tanto la cabeza como la cola
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            # Si la lista ya tiene nodos, agregamos el nuevo nodo al final
            nuevo_nodo.previo = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def duplicar_nodos(self):
        # Método para duplicar los nodos de la lista
        actual = self.cabeza
        while actual:
            # Creamos un nuevo nodo con el mismo dato del nodo actual
            nuevo_nodo = Nodo(actual.dato)
            # Configuramos los punteros del nuevo nodo
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.previo = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.previo = actual
            # Avanzamos dos posiciones para duplicar el siguiente nodo
            actual = actual.siguiente.siguiente

    def imprimir_adelante(self):
        # Método para imprimir la lista desde la cabeza hacia adelante
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        # Método para imprimir la lista desde la cola hacia atrás
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.previo
        print()

# Crear la lista con al menos 4 nodos
lista_doble = ListaEnlazadaDoble()
lista_doble.agregar(1)
lista_doble.agregar(2)
lista_doble.agregar(3)
lista_doble.agregar(4)

print("Lista Original hacia adelante:")
lista_doble.imprimir_adelante()
print("Lista Original hacia atrás:")
lista_doble.imprimir_atras()

# Duplicar los nodos
lista_doble.duplicar_nodos()

print("Lista Duplicada hacia adelante:")
lista_doble.imprimir_adelante()
print("Lista Duplicada hacia atrás:")
lista_doble.imprimir_atras()

#EJERCICIO 02
#CONTAR NODOS PARES E IMPARES
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.previo = None
        self.siguiente = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        # Método para agregar un nuevo nodo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.previo = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def imprimir_adelante(self):
        # Método para imprimir la lista desde la cabeza hacia adelante
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        # Método para imprimir la lista desde la cola hacia atrás
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.previo
        print()

    def contar_pares_impares(self):
        # Método para contar nodos pares e impares en la lista
        actual = self.cabeza
        contar_pares = 0
        contar_impares = 0
        while actual:
            if actual.dato % 2 == 0:
                contar_pares += 1
            else:
                contar_impares += 1
            actual = actual.siguiente
        return contar_pares, contar_impares

# Crear la lista con al menos 9 nodos
lista_doble = ListaEnlazadaDoble()
for i in range(1, 10):
    lista_doble.agregar(i)

print("Lista hacia adelante:")
lista_doble.imprimir_adelante()
print("Lista hacia atrás:")
lista_doble.imprimir_atras()

# Contar nodos pares e impares
contar_pares, contar_impares = lista_doble.contar_pares_impares()
print(f"Nodos pares: {contar_pares}")
print(f"Nodos impares: {contar_impares}")

#EJERCICIO 03
# Insertar Nodo en Posición Específica:
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.previo = None
        self.siguiente = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        # Método para agregar un nuevo nodo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.previo = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def imprimir_adelante(self):
        # Método para imprimir la lista desde la cabeza hacia adelante
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        # Método para imprimir la lista desde la cola hacia atrás
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.previo
        print()

    def contar_pares_impares(self):
        # Método para contar nodos pares e impares en la lista
        actual = self.cabeza
        contar_pares = 0
        contar_impares = 0
        while actual:
            if actual.dato % 2 == 0:
                contar_pares += 1
            else:
                contar_impares += 1
            actual = actual.siguiente
        return contar_pares, contar_impares

    def insertar_en_posicion(self, dato, posicion):
        # Método para insertar un nodo con un dato dado en una posición específica
        if posicion < 1:
            print("Posición inválida")
            return
        nuevo_nodo = Nodo(dato)
        if posicion == 1:
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.previo = nuevo_nodo
            self.cabeza = nuevo_nodo
            if self.cola is None:
                self.cola = nuevo_nodo
            return
        actual = self.cabeza
        posicion_actual = 1
        while posicion_actual < posicion - 1 and actual.siguiente:
            actual = actual.siguiente
            posicion_actual += 1
        if actual is None:
            print("Posición inválida")
        else:
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.previo = actual
            if actual.siguiente:
                actual.siguiente.previo = nuevo_nodo
            actual.siguiente = nuevo_nodo
            if nuevo_nodo.siguiente is None:
                self.cola = nuevo_nodo

# Crear la lista con al menos 5 nodos
lista_doble = ListaEnlazadaDoble()
for i in range(1, 6):
    lista_doble.agregar(i)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

# Insertar nodo con el dato 15 en la posición 3
lista_doble.insertar_en_posicion(15, 3)

print("Lista después de insertar el nodo hacia adelante:")
lista_doble.imprimir_adelante()
print("Lista después de insertar el nodo hacia atrás:")
lista_doble.imprimir_atras()

#EJERCICIO 04
#ELIMINAR NODOS DUPLICADOS
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.previo = None
        self.siguiente = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        # Método para agregar un nuevo nodo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.previo = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def imprimir_adelante(self):
        # Método para imprimir la lista desde la cabeza hacia adelante
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        # Método para imprimir la lista desde la cola hacia atrás
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.previo
        print()

    def eliminar_duplicados(self):
        # Método para eliminar nodos duplicados de la lista
        actual = self.cabeza
        vistos = set()  # Conjunto para almacenar los datos vistos
        while actual:
            if actual.dato not in vistos:
                vistos.add(actual.dato)  # Agrega el dato actual al conjunto
                actual = actual.siguiente
            else:
                nodo_siguiente = actual.siguiente
                self.eliminar_nodo(actual)  # Elimina el nodo actual
                actual = nodo_siguiente

    def eliminar_nodo(self, nodo):
        # Método para eliminar un nodo específico de la lista
        if nodo.previo:
            nodo.previo.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente
        if nodo.siguiente:
            nodo.siguiente.previo = nodo.previo
        else:
            self.cola = nodo.previo

# Crear la lista con nodos que contienen datos duplicados
lista_doble = ListaEnlazadaDoble()
lista_doble.agregar(1)
lista_doble.agregar(2)
lista_doble.agregar(3)
lista_doble.agregar(2)
lista_doble.agregar(4)
lista_doble.agregar(1)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

# Eliminar nodos duplicados
lista_doble.eliminar_duplicados()

print("Lista sin nodos duplicados hacia adelante:")
lista_doble.imprimir_adelante()
print("Lista sin nodos duplicados hacia atrás:")
lista_doble.imprimir_atras()

#EJERCICIO 05
#INVERTIR LA LISTA
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.previo = None
        self.siguiente = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        # Método para agregar un nuevo nodo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.previo = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def imprimir_adelante(self):
        # Método para imprimir la lista desde la cabeza hacia adelante
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        # Método para imprimir la lista desde la cola hacia atrás
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.previo
        print()

    def invertir_lista(self):
        actual = self.cabeza
        while actual is not None:
            temp = actual.previo
            actual.previo = actual.siguiente
            actual.siguiente = temp
            actual = actual.previo

        # Una vez invertida la lista, actualizamos la cabeza
        if temp is not None:
            self.cabeza = temp.previo

        # Ahora encontramos la nueva cola recorriendo hacia atrás desde la cabeza
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        self.cola = actual

# Crear la lista con al menos 6 nodos
lista_doble = ListaEnlazadaDoble()
for i in range(1, 7):
    lista_doble.agregar(i)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

# Invertir la lista
lista_doble.invertir_lista()

print("Lista invertida hacia adelante:")
lista_doble.imprimir_adelante()
print("Lista invertida hacia atrás:")
lista_doble.imprimir_atras()

"""### ***EJERCICIOS PARTE 02***"""

#EJERCICIO 06
#INVERTIR UNA CADENA USANDO PILAS
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def invertir_cadena(self, cadena):
        for caracter in cadena:
            self.apilar(caracter)
        cadena_invertida = ''
        while not self.esta_vacia():
            cadena_invertida += self.desapilar()
        return cadena_invertida

# Crear una instancia de la clase Pila
pila = Pila()

cadena_original = "Hola Mundo"
print("Cadena original:", cadena_original)
# Llamar al método invertir_cadena() a través de la instancia pila
print("Cadena invertida:", pila.invertir_cadena(cadena_original))

#EJERCICIO 07
#INVERTIR UNA CADENA USANDO PILAS
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def decimal_a_binario(numero):
    pila = Pila()
    while numero > 0:
        residuo = numero % 2
        pila.apilar(residuo)
        numero = numero // 2
    binario = ''
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    return binario

numero_decimal = 25
print("Número decimal:", numero_decimal)
print("Número binario:", decimal_a_binario(numero_decimal))

#EJERCICIO 08
#Evaluar la expresión posfija
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    for caracter in expresion.split():
        if caracter.isdigit():
            pila.apilar(int(caracter))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if caracter == '+':
                pila.apilar(operando1 + operando2)
            elif caracter == '-':
                pila.apilar(operando1 - operando2)
            elif caracter == '*':
                pila.apilar(operando1 * operando2)
            elif caracter == '/':
                pila.apilar(operando1 / operando2)
    return pila.ver_tope()

expresion_posfija = "3 2 *"
print("Resultado de la expresión posfija", expresion_posfija, "es:", evaluar_expresion_posfija(expresion_posfija))

#EJERCICIO 09
#Validar operadores anidados
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def validar_operadores_anidados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter in "([{":
            pila.apilar(caracter)
        elif caracter in ")]}":
            if pila.esta_vacia():
                return False
            tope = pila.desapilar()
            if (caracter == ")" and tope != "(") or (caracter == "]" and tope != "[") or (caracter == "}" and tope != "{"):
                return False
    return pila.esta_vacia()


expresion = "{[())()]}"
print("¿Los operadores en la expresión", expresion, "están correctamente anidados?", validar_operadores_anidados(expresion))

#EJERCICIO 10
#ORDENAR UNA PILA
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def ordenar_pila(pila):
    pila_temporal = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        while not pila_temporal.esta_vacia() and pila_temporal.ver_tope() > elemento:
            pila.apilar(pila_temporal.desapilar())
        pila_temporal.apilar(elemento)
    return pila_temporal

pila_desordenada = Pila()
pila_desordenada.apilar(5)
pila_desordenada.apilar(2)
pila_desordenada.apilar(9)
pila_desordenada.apilar(1)
pila_desordenada.apilar(7)
print("Pila desordenada:", pila_desordenada)
print("Pila ordenada:", ordenar_pila(pila_desordenada))

#EJERCICIO 11
#ELIMINAR DUPLICADOS
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def eliminar_duplicados_pila(pila):
    conjunto = set()
    pila_temporal = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in conjunto:
            conjunto.add(elemento)
            pila_temporal.apilar(elemento)
    return pila_temporal

pila_con_duplicados = Pila()
pila_con_duplicados.apilar(1)
pila_con_duplicados.apilar(2)
pila_con_duplicados.apilar(3)
pila_con_duplicados.apilar(2)
pila_con_duplicados.apilar(4)
pila_con_duplicados.apilar(1)
print("Pila con duplicados:", pila_con_duplicados)
print("Pila sin duplicados:", eliminar_duplicados_pila(pila_con_duplicados))

#EJERCICIO 12
#IMPLEMENTAR UNA CALCULADORA SENCILLA
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        return self.items.pop()


def calcular_expresion(expresion):
    pila = Pila()
    operandos = expresion.split()
    for token in operandos:
        if token.isdigit():
            pila.push(int(token))
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()
            if token == '+':
                pila.push(operando1 + operando2)
            elif token == '-':
                pila.push(operando1 - operando2)
            elif token == '*':
                pila.push(operando1 * operando2)
            elif token == '/':
                pila.push(operando1 / operando2)
    return pila.pop()

# Solicitar la expresión al usuario
expresion_calculadora = input("Ingrese la expresión en notación polaca inversa (ejemplo: 5 3 + 8): ")

# Calcular y mostrar el resultado
resultado_calculadora = calcular_expresion(expresion_calculadora)
print("Resultado de la expresión:", expresion_calculadora, "=", resultado_calculadora)

#EJERCICIO 13
#Comprobar palíndromos
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        return self.items.pop()

def es_palindromo(cadena):
    cadena = cadena.lower().replace(' ', '')
    pila = Pila()
    for caracter in cadena:
        pila.push(caracter)
    cadena_invertida = ''
    while not pila.esta_vacia():
        cadena_invertida += pila.pop()
    return cadena == cadena_invertida
class SistemaDeshacer:
    def __init__(self):
        self.acciones = Pila()
        self.deshaceres = Pila()

    def hacer(self, accion):
        self.acciones.push(accion)

    def deshacer(self):
        if not self.acciones.esta_vacia():
            accion_deshacer = self.acciones.pop()
            self.deshaceres.push(accion_deshacer)

    def rehacer(self):
        if not self.deshaceres.esta_vacia():
            accion_rehacer = self.deshaceres.pop()
            self.acciones.push(accion_rehacer)

cadena_palindromo = "Anita lava la tina"
es_palindromo = es_palindromo(cadena_palindromo)
print("¿Es un palíndromo?", es_palindromo)

#EJERCICIO 14
#Sistema de deshacer
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        return self.items.pop()
class SistemaDeshacer:
    def __init__(self):
        self.acciones = Pila()
        self.deshaceres = Pila()

    def hacer(self, accion):
        self.acciones.push(accion)

    def deshacer(self):
        if not self.acciones.esta_vacia():
            accion_deshacer = self.acciones.pop()
            self.deshaceres.push(accion_deshacer)

    def rehacer(self):
        if not self.deshaceres.esta_vacia():
            accion_rehacer = self.deshaceres.pop()
            self.acciones.push(accion_rehacer)

sistema_deshacer = SistemaDeshacer()
sistema_deshacer.hacer("Escribir mensaje 1")
sistema_deshacer.hacer("Escribir mensaje 2")
print("Acciones realizadas:", sistema_deshacer.acciones.items)
sistema_deshacer.deshacer()
print("Después de deshacer:", sistema_deshacer.acciones.items)
sistema_deshacer.rehacer()
print("Después de rehacer:", sistema_deshacer.acciones.items)
