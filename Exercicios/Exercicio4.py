import random

lista = list(range(0, 100))
escolha = random.choice(lista)
print(escolha)
resposta = input("Acertei seu numero S/N: ")
while resposta == "n":
    aproximado = input("seu numero é: m pra maior ou me para menor: ")
    if aproximado == "m":
        escolha2 = random.choice(range(escolha, 100))
    else:
        escolha2 = random.choice(range(0,escolha))
    print(escolha2)
    resposta = input("Acertei seu numero S/N: ")
