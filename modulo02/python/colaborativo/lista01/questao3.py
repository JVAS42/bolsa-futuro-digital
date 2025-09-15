notas = list()
media = 0
for i in range(0, 4):
    nota = float(input())
    notas.append(nota)
    media = media + nota

for i in range(0, len(notas)):
    print(f'Nota {i+1}: {notas[i]}')
print(f'Média = {media/len(notas)}')