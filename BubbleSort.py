
#Implementado en python 3
def bubble_sort(lista):
    #Recorre el arreglo desde el elemento en [0] hasta [n-1]
    for i in range(len(lista)-1):
        #Se itera los elementos con el fin de comparar e intercambiar
        for j in range(len(lista)-i-1):
            #Comparación para encontrar el mayor de la pareja
            if(lista[j]>lista[j+1]):
                #Intercambio de elementos en la pareja
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

#Ingreso de datos
print("Tell me the numbers of the array")
str = input()

str = str.split()
lista = []

for i in str:
    lista.append(int(i))
#Llamada al metodo
bubble_sort(lista)

#Impresión del resultado
for element in lista:
    print(element)
