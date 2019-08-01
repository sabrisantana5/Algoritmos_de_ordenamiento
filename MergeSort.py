#Implementación en python 3
#Método para unir sub-arreglos
def combinar(lista, inicio, medio, fin):
    auxiliar = []
    h = 0
    i = inicio
    j = medio + 1

    while i <= medio and j <= fin:
        #Comparación de elementos en sub-listas
        #Si es menor
        if lista[i] <= lista[j]:
            auxiliar.append(lista[i])
            i+= 1
        #Si es mayor
        else:
            auxiliar.append(lista[j])
            j+= 1
        h = h + 1

    #Si ya se recorrió el arreglo izquierdo
    if i > medio:
        while j <= fin:
            auxiliar.append(lista[j])
            j+= 1
            h+= 1
#Si ya se recorrió el arreglo derecho
    else:
        while i <= medio:
            auxiliar.append(lista[i])
            i+= 1
            h = h + 1
    #Lista auxiliar
    for x in range(len(auxiliar)):
        lista[inicio + x] = auxiliar[x]

#Implementación de merge sort
def merge_sort(lista, inicio, fin):
    #Comparación que indica si el arreglo ya terminó
    if(inicio < fin):
        #Definición de un elemento en medio del arreglo
        medio = int((inicio + fin)/2)
        #Llamadas recursivas del algoritmo para el sub-arreglo izquierdo y derecho
        merge_sort(lista, inicio, medio)
        merge_sort(lista, medio+1, fin)
        #Unión de sub-arreglos
        combinar(lista, inicio, medio, fin)


#Ingreso de datos
print("Tell me the numbers of the array")
str = input()

str = str.split()
lista = []

for i in str:
    lista.append(int(i))
#Llamada al metodo
merge_sort(lista,0,len(lista)-1)

#Impresión del resultado
for element in lista:
    print(element)
