def quicksort(lista, start, end):
    if end - start > 1:
        p = partition(lista, start, end)
        quicksort(lista, start, p)
        quicksort(lista, p + 1, end)
 
 
def partition(lista, start, end):
    pivot = lista[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and lista[i] <= pivot):
            i = i + 1
        while (i <= j and lista[j] >= pivot):
            j = j - 1
 
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
        else:
            lista[start], lista[j] = lista[j], lista[start]
            return j
 
 
lista = input('Introduceti numerele: ').split()
lista = [int(x) for x in lista]
quicksort(lista, 0, len(lista))
print('Lista sortata: ', end='')
print(lista)
