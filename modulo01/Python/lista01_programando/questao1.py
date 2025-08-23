win = 0
draw = 0
loser = 0

for i in range(0, 5):
    host = int(input(f'Gols da Seleção no jogo {i+1}: '))
    visitor = int(input(f'Gols do adversário no jogo {i+1}: '))

    if host > visitor:
        win += 1
    elif host < visitor:
        loser += 1
    else:
        draw += 1

print('=== Torneio de Futebol ===')
print(f'Vitórias: {win}')
print(f'Empates: {draw}')
print(f'Derrotas: {loser}')