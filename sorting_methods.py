import random
import time

# Datos de repuestos
def generar_repuestos(cantidad):
    repuestos = []
    for i in range(cantidad):
        repuestos.append({
            'id': i + 1,
            'nombre': f'Repuesto {i+1}',
            'precio': random.randint(50, 2000),
            'calificacion': round(random.uniform(1, 5), 1),
            'inventario': random.randint(0, 500)
        })
    return repuestos

# Algoritmos de ordenamiento
def bubble_sort(lista, clave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][clave] > lista[j+1][clave]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def insertion_sort(lista, clave):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i-1
        while j >=0 and actual[clave] < lista[j][clave]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual

def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)//2]
    menores = [x for x in lista if x[clave] < pivote[clave]]
    iguales = [x for x in lista if x[clave] == pivote[clave]]
    mayores = [x for x in lista if x[clave] > pivote[clave]]
    return quick_sort(menores, clave) + iguales + quick_sort(mayores, clave)

def merge_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista)//2
    izquierda = merge_sort(lista[:medio], clave)
    derecha = merge_sort(lista[medio:], clave)
    
    return mezclar(izquierda, derecha, clave)

def mezclar(izq, der, clave):
    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i][clave] <= der[j][clave]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Mostrar repuestos/cambiar el valor de limite=n cambia la cantidad de productos a generar
def mostrar_repuestos(repuestos, limite=8):
    print("\n--- Resultados ordenados ---")
    for i, repuesto in enumerate(repuestos[:limite]):
        print(f"{i+1}. {repuesto['nombre']}")
        print(f"   Precio: ${repuesto['precio']}")
        print(f"   Calificación: ⭐{repuesto['calificacion']}")
        print(f"   Inventario: {repuesto['inventario']} unidades\n")

def menu():
    datos = generar_repuestos(8)#El número de datos tiene que ser igual a la cantidad de repuestos a generar
    
    while True:
        print("\n=== Gestión Carfix ===")
        print("1. Ver repuestos sin ordenar")
        print("2. Ordenar por método específico")
        print("3. Comparar todos los métodos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_repuestos(datos)
        elif opcion == '2':
            print("\nMétodos de ordenamiento:")
            print("1. Burbuja")
            print("2. Inserción")
            print("3. Quick Sort")
            print("4. Merge Sort")
            metodo = input("Elija un método (1-4): ")
            
            print("\nAtributos para ordenar:")
            print("1. Precio")
            print("2. Calificación")
            print("3. Inventario")
            atributo = input("Elija un atributo (1-3): ")
            
            claves = ['precio', 'calificacion', 'inventario']
            clave = claves[int(atributo)-1]
            
            copia = datos.copy()
            inicio = time.time()
            
            if metodo == '1':
                bubble_sort(copia, clave)
                nombre = "Burbuja"
            elif metodo == '2':
                insertion_sort(copia, clave)
                nombre = "Inserción"
            elif metodo == '3':
                copia = quick_sort(copia, clave)
                nombre = "Quick Sort"
            elif metodo == '4':
                copia = merge_sort(copia, clave)
                nombre = "Merge Sort"
            else:
                print("Opción inválida")
                continue
            
            tiempo = time.time() - inicio
            mostrar_repuestos(copia)
            print(f"Tiempo de ejecución ({nombre}): {tiempo:.5f} segundos")
            
        elif opcion == '3':
            print("\nAtributos para comparar:")
            print("1. Precio")
            print("2. Calificación")
            print("3. Inventario")
            atributo = input("Elija un atributo (1-3): ")
            
            claves = ['precio', 'calificacion', 'inventario']
            clave = claves[int(atributo)-1]
            
            metodos = {
                'Burbuja': bubble_sort,
                'Inserción': insertion_sort,
                'Quick Sort': quick_sort,
                'Merge Sort': merge_sort
            }
            
            print("\nComparando métodos...")
            for nombre, funcion in metodos.items():
                copia = datos.copy()
                inicio = time.time()
                
                if nombre in ['Burbuja', 'Inserción']:
                    funcion(copia, clave)
                else:
                    copia = funcion(copia, clave)
                
                tiempo = time.time() - inicio
                print(f"{nombre}: {tiempo:.5f} segundos")
                
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
