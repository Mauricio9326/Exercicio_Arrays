lista = ["Giovanni", "Nemo", "Jesper", "Maximilian", "Karina"]
filtro = input("qual letra deseja filtrar: ")

res = [k for k in lista if filtro in k]
print(res)