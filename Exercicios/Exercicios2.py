lista = [2, 10, 93, 10, 7, 98]
val = input("Write A for ascending or write D for descending: ")
if val == "a":
    lista.sort()
    print(lista)
elif val == "d":
    lista.sort(reverse = True)
    print(lista)
else :
    print("Letra invalida")



