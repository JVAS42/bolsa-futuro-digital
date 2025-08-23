total = 0
quantidade = int(input('Quantas pessoas vão ao show? '))

for i in range (0, quantidade):
    idade = int(input(f'Idade da pessoa {i+1}: '))
    if idade <= 12:
        print('Entrada grátis ')
    elif idade >= 18:
        total = total + 20
        print('Ingresso inteiro (R$ 20)')
    else:
        total = total + 10
        print('Meia entrada (R$ 10)')

print(f'Total arrecadado: R$ {total}')