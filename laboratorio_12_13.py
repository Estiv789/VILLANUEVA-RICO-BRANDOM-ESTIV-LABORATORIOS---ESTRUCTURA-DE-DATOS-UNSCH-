#EJERCICIO 01
# 01. Verificar si una palabra es palíndroma
'''1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para
comparar los caracteres de la palabra en orden original y reverso.
'''
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not bool(self.items)

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        return self.items.pop(0)

def es_palindromo(palabra):
    cola1 = Cola()
    cola2 = Cola()

    for caracter in palabra:
        cola1.encolar(caracter)
        cola2.encolar(caracter)

    while not cola1.esta_vacia():
        if cola1.desencolar() != cola2.items[-1]:
            return False
        cola2.items.pop()

    return True


#EJECUTANDO EL PROGRAMA
palabra = input("Ingrese una palabra para verificar si es palíndroma: ").lower()
if es_palindromo(palabra):
    print(f"{palabra} es palíndroma.")
else:
    print(f"{palabra} no es palíndroma.")

#Ejercicio 02
'''
Diseño de un sistema de gestión de pedidos
2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que
fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado
actual de la cola.
'''
class ColaPedidos:
    def __init__(self):
        # Inicializa la cola de pedidos como una lista vacía
        self.pedidos = []

    def agregar_pedido(self, pedido):
        # Agrega un pedido a la cola de pedidos
        self.pedidos.append(pedido)

    def procesar_pedido(self):
        # Procesa el pedido más antiguo de la cola de pedidos
        if self.pedidos:
            return self.pedidos.pop(0)
        else:
            return "No hay pedidos para procesar."

    def mostrar_pedidos(self):
        # Muestra los pedidos en espera en la cola
        if self.pedidos:
            print("Pedidos en espera:")
            for pedido in self.pedidos:
                print("-", pedido)
        else:
            print("No hay pedidos en espera.")

# Función principal
def main():
    # Crea una instancia de la cola de pedidos
    cola_pedidos = ColaPedidos()

    while True:
        print("\nSistema de Gestión de Pedidos")
        print("1. Agregar pedido")
        print("2. Procesar pedido")
        print("3. Mostrar pedidos en espera (mostrar el estado actual de la cola)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Agrega un nuevo pedido a la cola
            pedido = input("Ingrese el pedido: ")
            cola_pedidos.agregar_pedido(pedido)
            print("Pedido agregado exitosamente.")

        elif opcion == '2':
            # Procesa el pedido más antiguo de la cola
            pedido = cola_pedidos.procesar_pedido()
            print("Pedido procesado:", pedido)

        elif opcion == '3':
            # Muestra los pedidos en espera
            cola_pedidos.mostrar_pedidos()

        elif opcion == '4':
            # Sale del sistema
            print("Saliendo del sistema.")
            break

        else:
            # Opción no válida
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    # Ejecuta la función principal
    main()

# EJERCICIO 03: Búsqueda de rutas en un laberinto
#3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola
#para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

#El código proporcionado implementa un algoritmo de búsqueda en anchura (BFS) para encontrar el camino más corto desde el punto de inicio hasta el punto de destino en un laberinto representado por una matriz.
'''- La clase Cola implementa una cola básica utilizando una lista.
- La función bfs toma el laberinto, el punto de inicio y el punto de destino como entrada y devuelve el camino más corto desde el punto de inicio hasta el punto de destino.
- Dentro de la función bfs, se utiliza una cola para realizar la búsqueda en anchura. Comienza en el punto de inicio y explora todos los caminos posibles hasta llegar al punto de destino.
- Se utiliza un conjunto visitado para llevar un registro de los nodos visitados y evitar visitarlos más de una vez.
- La función devuelve el camino más corto encontrado como una lista de coordenadas.
- El laberinto se representa como una matriz donde 0 representa un camino válido y 1 representa una pared.

*El código proporcionado encuentra el camino más corto desde el punto de inicio hasta el punto de destino en el laberinto dado y lo imprime.'''
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not bool(self.items)

    def agregar(self, dato):
        self.items.append(dato)

    def sacar(self):
        return self.items.pop(0)

def bfs(maze, inicio, fin):
    cola = Cola()
    cola.agregar([inicio])
    visitado = set([inicio])

    while not cola.esta_vacia():
        camino = cola.sacar()
        actual = camino[-1]

        if actual == fin:
            return camino

        for direccion in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            fila, columna = actual[0] + direccion[0], actual[1] + direccion[1]
            if (fila in range(len(maze)) and
                columna in range(len(maze[0])) and
                maze[fila][columna] != 1 and
                (fila, columna) not in visitado):
                cola.agregar(camino + [(fila, columna)])
                visitado.add((fila, columna))

    return None

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0]
]
inicio = (0, 0)
fin = (4, 4)

print("El camino más corto encontrado como una lista de coordenadas es: ", bfs(laberinto, inicio, fin))

# EJERCICIO 04: Diseño de un sistema de gestión de tareas (Avanzado)
#4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como
#completadas y mostrar la próxima tarea pendiente.

class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_tarea_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
        else:
            print("Índice de tarea fuera de rango.")

    def mostrar_proxima_tarea_pendiente(self):
        for tarea in self.tareas:
            if not tarea.completada:
                print(f"Próxima tarea pendiente: {tarea.descripcion}")
                return
        print("No hay tareas pendientes.")

    def mostrar_todas_las_tareas(self):
        print("Lista de tareas:")
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i + 1}. {tarea.descripcion} - {estado}")

if __name__ == "__main__":
    sistema_tareas = SistemaGestionTareas()

    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar próxima tarea pendiente")
        print("4. Mostrar todas las tareas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            sistema_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            indice = int(input("Ingrese el índice de la tarea completada: ")) - 1
            sistema_tareas.marcar_tarea_completada(indice)
        elif opcion == "3":
            sistema_tareas.mostrar_proxima_tarea_pendiente()
        elif opcion == "4":
            sistema_tareas.mostrar_todas_las_tareas()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

"""# **EJERCICIO PARTES 02 - ÁRBOLES**"""

#-------------------------------------------------------------------------------
#Ejercicios parte 02 - Arboles:
#-------------------------------------------------------------------------------
'''Contar nodos:
5. Implementar una función que cuente la cantidad de nodos en el árbol.
6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).
7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).
'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def contar_nodos(arbol):
    if arbol is None:
        return 0
    else:
        contador = 1
        for hijo in arbol.hijos:
            contador += contar_nodos(hijo)
        return contador


def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    elif not arbol.hijos:
        return 1
    else:
        contador = 0
        for hijo in arbol.hijos:
            contador += contar_nodos_hoja(hijo)
        return contador


def contar_nodos_internos(arbol):
    if arbol is None or not arbol.hijos:
        return 0
    else:
        contador = 1
        for hijo in arbol.hijos:
            contador += contar_nodos_internos(hijo)
        return contador


# Ejemplo de uso:
if __name__ == "__main__":
    # Construcción del árbol
    a = Nodo(1)
    b = Nodo(2)
    c = Nodo(3)
    d = Nodo(4)
    e = Nodo(5)
    f = Nodo(6)

    a.agregar_hijo(b)
    a.agregar_hijo(c)
    b.agregar_hijo(d)
    b.agregar_hijo(e)
    c.agregar_hijo(f)

    # Contar nodos
    print("Cantidad de nodos:", contar_nodos(a))
    print("Cantidad de nodos hoja:", contar_nodos_hoja(a))
    print("Cantidad de nodos internos:", contar_nodos_internos(a))

'''Calcular altura y profundidad:
8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz
hasta una hoja).
9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz
hasta el nodo).'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def altura_arbol(arbol):
    if arbol is None:
        return 0
    elif not arbol.hijos:
        return 1
    else:
        alturas = [altura_arbol(hijo) for hijo in arbol.hijos]
        return 1 + max(alturas)


def profundidad_nodo(raiz, nodo):
    if raiz is None or raiz == nodo:
        return 0
    else:
        for hijo in raiz.hijos:
            profundidad = profundidad_nodo(hijo, nodo)
            if profundidad >= 0:
                return 1 + profundidad
        return -1  # Si no se encuentra el nodo


# Ejemplo de uso:
if __name__ == "__main__":
    # Construcción del árbol
    a = Nodo('A')
    b = Nodo('B')
    c = Nodo('C')
    d = Nodo('D')
    e = Nodo('E')
    f = Nodo('F')
    g = Nodo('G')
    h = Nodo('H')

    a.agregar_hijo(b)
    a.agregar_hijo(c)
    b.agregar_hijo(d)
    b.agregar_hijo(e)
    c.agregar_hijo(f)
    f.agregar_hijo(g)
    f.agregar_hijo(h)

    # Calcular altura del árbol
    print("Altura del árbol:", altura_arbol(a))

    # Calcular profundidad de un nodo
    nodo_objetivo = g
    print(f"Profundidad del nodo {nodo_objetivo.valor}:", profundidad_nodo(a, nodo_objetivo))

'''Buscar el mínimo y el máximo:
10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol.
11. Implementar una función que encuentre el nodo con el valor máximo en el árbol.'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def encontrar_minimo(raiz):
    if raiz is None:
        return None
    if not raiz.hijos:
        return raiz.valor
    minimo = raiz.valor
    for hijo in raiz.hijos:
        minimo_hijo = encontrar_minimo(hijo)
        if minimo_hijo is not None and minimo_hijo < minimo:
            minimo = minimo_hijo
    return minimo


def encontrar_maximo(raiz):
    if raiz is None:
        return None
    if not raiz.hijos:
        return raiz.valor
    maximo = raiz.valor
    for hijo in raiz.hijos:
        maximo_hijo = encontrar_maximo(hijo)
        if maximo_hijo is not None and maximo_hijo > maximo:
            maximo = maximo_hijo
    return maximo


# Ejemplo de uso:
if __name__ == "__main__":
    # Construcción del árbol
    a = Nodo(10)
    b = Nodo(5)
    c = Nodo(15)
    d = Nodo(1)
    e = Nodo(7)
    f = Nodo(23)
    g = Nodo(17)

    a.agregar_hijo(b)
    a.agregar_hijo(c)
    b.agregar_hijo(d)
    b.agregar_hijo(e)
    c.agregar_hijo(f)
    c.agregar_hijo(g)

    # Encontrar mínimo y máximo
    print("Valor mínimo en el árbol:", encontrar_minimo(a))
    print("Valor máximo en el árbol:", encontrar_maximo(a))
