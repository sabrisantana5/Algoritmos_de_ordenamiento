#Implementado en python 3
#Metodo complementario que ordena en funcion al número de apariciones de cada dígito
def countingSort(arrayToSort, decimal):

    length_arr = len(arrayToSort)
    #Arreglo que guardará el número de apariciones de cada dígito
    countingArray = []
    #Arreglo que al final estará ordenado
    sortedArray = []

    #Se insertan 10 0s en el arreglo contador
    for i in range(0, 10):
        countingArray.append(0)

    #Incrementa la posición del dígito en el arreglo contador depediendo del número de apariciones
    for i in range(0, length_arr):
        sortedArray.append(0)
        #Obtención del dígito a considerar
        index = (arrayToSort[i]/decimal)
        #Aquí incrementa
        countingArray[int(index % 10)] += 1

    for i in range(1, 10):
        countingArray[i] += countingArray[i-1]

    #Ordena el arreglo basandose en el dígito decimal en el que se encuentra
    for i in range(length_arr - 1, -1, -1 ):
        index = (arrayToSort[i]/decimal)
        sortedArray[countingArray[int(index % 10)]-1] = arrayToSort[i]
        countingArray[int(index % 10)] -= 1

    for i in range(0,length_arr):
        arrayToSort[i] = sortedArray[i]

#Implementación de radix sort
def radixSort(arrayToSort):
    #Encuentra el elemento más grande para sabes cuantas veces deberá repetir
    biggestNumber = max(arrayToSort)
    decimal = 1
    #Llamada a counting sort por cada posición decimal
    while biggestNumber / decimal > 0:
        countingSort(arrayToSort, decimal)
        #Cambio en la posición decimal
        decimal *= 10

#Ingreso de datos
print("Tell me the numbers of the array")
str = input()

str = str.split()
lista = []

for i in str:
    lista.append(int(i))
#Llamada al metodo
radixSort(lista)

#Impresión del resultado
for element in lista:
    print(element)
