def ordenar_lista(numeros):
   #Guardamos la longitud de la lista
    n = len (numeros)

    #Hacemos un bucle externo que recorra la lista tantas veces como elementos haya

    for i in range(n):
        #Ahora hacemos un bucle interno para comparar pares adyacentes
        #Restamos i porqué despues de cada pasada los ultimos i elementos ya están ordenados
        for j in range (0,n-i-1):
            #Ahora si el numero actual es mayor que el siguiente, los intercambiamos
            if numeros[j] > numeros [j+i]:
                #Hago el intercambio usando una variable temporal
                temporal = numeros [j]
                numeros [j] = numeros [j+1]
                numeros [j+1] = temporal
    return numeros


class Ordenador:
    def __init__(self):
        pass
    def ordenar_lista(self,numeros):
        n = len(numeros)

        for i in range (n):  # n es la longitud de la lista

            for j in range(0,n - i - 1):
                if numeros [j] > numeros [j + 1]:
                    temp = numeros [j]
                    numeros [j] = numeros [j+1]
                    numeros [j + 1] = temp
        return numeros



Ordenador1 = Ordenador() #Creo a ordenador 1 que es un objeto de la clase ordenador
lista_numeros = [64,26,29,37,86,990]

print(Ordenador1.ordenar_lista(lista_numeros))
