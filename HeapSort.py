#Implementado en python 3
#Método para intercambiar dos elementos
def intercambiar(lista,elemento_uno,elemento_dos):
    lista[elemento_uno], lista[elemento_dos] = lista[elemento_dos], lista[elemento_uno]
#Método que intercambia los 'hijos' que son mayores a los 'padres'
def heapify(lista, longitud ,indice):
    mayor = indice
    izquierda = indice * 2 + 1
    derecha = indice * 2 + 2
    # Comparación con el fin de saber si hay un hijo mayor al padre
    if izquierda < longitud and lista[mayor] < lista[izquierda]:
        mayor = izquierda
    if derecha < longitud and lista[mayor] < lista[derecha]:
        mayor = derecha
    if mayor != indice:
        intercambiar(lista, indice, mayor)
        heapify(lista,longitud, mayor)
#Implementación de heapsort
def heapSort(lista):
    #Reordena por medio de 'heapify'
    for i in range(len(lista), -1, -1):
        heapify(lista,len(lista),i)

    for i in range(len(lista)-1, 0, -1):
        #Intercambio de el primer elemento con el último
        intercambiar(lista,0,i)
        #Reordena por medio de 'heapify'
        heapify(lista,i, 0)



#Ingreso de datos
print("Tell me the numbers of the array")
str = input()

str = str.split()
lista = []

for i in str:
    lista.append(int(i))
#Llamada al metodo
heapSort(lista)

#Impresión del resultado
for element in lista:
    print(element)
