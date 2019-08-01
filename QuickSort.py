#Implementado en python 3
#Metodo para intercambiar dos elementos
def intercambiar(lista,elemento_uno,elemento_dos):
    lista[elemento_uno], lista[elemento_dos] = lista[elemento_dos], lista[elemento_uno]
#Partición del arreglo por medio de un pivote
def particion(lista, inicio, fin):
    pivote = lista[fin]
    ultimo = inicio - 1

    for i in range(inicio,fin):
    #Comparación de los elementos con el pivote
        if lista[i] < pivote:
            ultimo+= 1
    #Intercambio de elementos
            intercambiar(lista,ultimo,i)
    intercambiar(lista,ultimo+1,fin)
    return ultimo + 1

#Implementación recursiva de quick sort
def quick_sort(lista, inicio, fin):
    if(inicio < fin):
        #División del arreglo a partir de sus extremos
        q = particion(lista,inicio,fin)
        #Ordenación del sub-arreglo izquierdo
        quick_sort(lista,inicio,q-1)
        #Ordenación del sub-arreglo derecho
        quick_sort(lista,q+1,fin)

#Ingreso de datos
print("Tell me the numbers of the array")
str = input()

str = str.split()
lista = []

for i in str:
    lista.append(int(i))
#Llamada al metodo
quick_sort(lista,0,len(lista)-1)

#Impresión del resultado
for element in lista:
    print(element)
