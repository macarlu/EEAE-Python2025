'''Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
Luego, intégrala como método en una clase Ordenador.'''

def ordena_lista(lista):
    n = len(lista) #Aquí se obtiene la longitud de la lista (el número total de elementos) y se almacena en la variable n. Esto es importante para saber cuántas veces necesitamos iterar.
    for i in range(n):#El primer bucle for controla el número de iteraciones completas necesarias. Se ejecutará n veces, porque en cada pasada colocamos un elemento más en su posición correcta al final de la lista.
        for j in range(0, n-i-1):#Este bucle interno compara cada par de elementos adyacentes en la lista, desde el principio hasta n-i-1, n-i-1 asegura que no volvamos a comparar los elementos ya ordenados (al final de la lista) en iteraciones anteriores.
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] #si el elemento actual es mayor que el siguiente intercambian sus posiciones
    return lista #devuelve la lista ordenada

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
ordena_lista(numeros)
print(numeros)  # [11, 12, 22, 25, 34, 64, 90]
