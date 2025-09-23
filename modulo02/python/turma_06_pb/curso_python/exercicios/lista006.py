# QUESTÃO 1 #
i1 = 1
while i1 <= 10:
    print(i1)
    i1 += 1

# QUESTÃO 2 #
i2 = 10
while i2 >= 1:
    print(i2)
    i2 -= 1

# QUESTÃO 3 #
i3 = 0
while i3 <= 20:
    print(i3)
    i3 += 2

# QUESTÃO 4 #
i4 = 1
while i4 < 20:
    print(i4)
    i4 += 2

# QUESTÃO 5 #
i5 = 1
contagem = int(input('Informe um número: '))
while i5 <= contagem:
    print(i5)
    i5 += 1

# QUESTÃO 6 #
palavra = str(input('Digite uma palavra: '))
i6 = 0
while i6 < 5:
    print(palavra)
    i6 += 1

# QUESTÃO 7 #
i7 = 1
numero = 2

while i7 <= 10:
    print(f'{numero} X {i7} = {i7*numero}')
    i7 += 1

# QUESTÃO 8 #
i8 = 1
num_user =  int(input('Informe um número: '))

while i8 <= 10:
    print(f'{num_user} X {i8} = {i8*num_user}')
    i8 += 1

# QUESTÃO 9 #
# lista_nomes = input().split()
lista_nomes = list()
i9 = 1
while i9 <= 5:
    nome = input(f'NOME {i9}: ')
    lista_nomes.append(nome)
    i9 += 1

i9 = 0
while i9 < 5:
    print(f'NOME {i9+1}: {lista_nomes[i9]}')
    i9 += 1

# QUESTÃO 10 #
soma = 0
i10 = 0
numeros = list()

while i10 < 5:
    numero_somar = int(input(f'Informe o {i10+1}º: '))
    numeros.append(numero_somar)
    soma += numero_somar
    i10 += 1

print(f'A SOMA DOS NÚMEROS {numeros} É {soma}')

# QUESTÃO 11 #
numero2 = 5

while numero2 <= 50:
    print(numero2)
    numero2 += 5

# QUESTÃO 12 #
num_user2 = int(input('Informe um número: '))
i12 = 0

while i12 <= num_user2:
    print(i12)
    i12 += 1

# QUESTÃO 13 #
condicao = True
while condicao:
    try:
        num_user3 = input('Informe um número: ')
        num_user3 = int(num_user3)

        if num_user3 == 0:
            print('Você digitou 0, fim do programa')
            condicao = False
    except:
        print('ERRO! Informe corretamente!')

# QUESTÃO 14 #
while True:
    try:
        senha = input('Informe a senha: ')
        senha = int(senha)

        if senha == 1234:
            print('Senha correta!')
            break
        
        print('Senha incorreta, tente novamente', end=' -> ')
    except:
        print('ERRO! Informe corretamente!')

# QUESTÃO 15 #
i15 = 1

while i15 <= 100:
    if i15 % 10 == 0:
        print(i15)
    i15 += 1