import random

maquina = random.randint(1, 20)
print(maquina)

for i in range(0, 5):
    palpite = int(input('Adivinhe o número (1 a 20): '))
    if palpite > maquina:
        print('Muito alto!')
    elif palpite < maquina:
        print('Muito baixo!')
    else:
        break

if palpite == maquina:
    print('Você acertou!')
else:
    print(f'Game over! O número era {maquina}')