vogais = ['a', 'e', 'i', 'o', 'u']

for i in vogais:
    print(i)

for indice, valor in enumerate(vogais):
    print(indice, valor)

for i in range(0, len(vogais), 1):
    print(vogais[i])

cont = 0
while cont < len(vogais):
    print(vogais[cont])
    cont += 1