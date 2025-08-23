canditados = [[], [], []]
soma = 0

for i in range(0, 3):
    for j in range(0, 3):
        nota = int(input(f'Nota do avaliador {i+1} para o candidato {j+1}: '))
        canditados[j].append(nota)


canditado1 = sum(canditados[0])
canditado2 = sum(canditados[1])
canditado3 = sum(canditados[2])

print('Pontuação final:')
print(f'Candidato 1: {canditado1}')
print(f'Candidato 2: {canditado2}')
print(f'Candidato 3: {canditado3}')

if canditado1 > canditado2 and canditado1 > canditado3:
    print('Candidato 1 é o campeão!')
elif canditado2 > canditado1 and canditado2 > canditado3:
    print('Candidato 2 é o campeão!')
elif canditado3 > canditado1 and canditado3 > canditado2:
    print('Candidato 3 é o campeão!')
else:
    print('Empate! Disputa acirrada')