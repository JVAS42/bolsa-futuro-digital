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

# QUESTÃO 16 #
i16 = 0

while i16 < 21:
    print(i16)
    i16 += 1

# QUESTÃO 17 #
palavra = input('Digite uma palavra: ')
i17 = 0

while i17 <= len(palavra):
    print(palavra[i17])

# QUESTÃO 18 #
num_user4 = int(input('Informe um numero: '))

soma = 0
i18 = 1

while i18 <= num_user4:
    soma += i18

print(f'SOMA = {soma}')

# QUESTÃO 19 #
while True:
    try:
        num_user5 = int(input('Digite um número: '))

        if num_user5 < 0:
            print('Fim do programa')
            break
    except:
        print('ERRO! Tente novamente', end=' ')

# QUESTÃO 20 #
palavra2 = input('Informe uma palavra: ')
i20 = 0

while i20 < len(palavra):
    i20 += 1

print(f'A PALAVRA {palavra} TEM {i20} LETRAS')

# QUESTÃO 21 #
i21 = 50

while i21 < 101:
    print(i21)
    i21 += 1

# QUESTÃO 22 #
i22 = 2

while i22 < 31:
    print(i22)
    i22 += 2

# QUESTÃO 23 #
i23 = 0

while i23 < 10:
    num_user6 = int(input('Digite um número: '))
    if num_user6 % 2 == 0:
        print(num_user6)

# QUESTÃO 24 #
i24 = 1
multiplo = 3

while i24 <= 15:
    print(multiplo)
    multiplo += 3
    i24 += 1

# QUESTÃO 25 #
cont = 0

while True:
    nota = float(input('Informe as notas [DIGITE -1 para encerrar]'))

    if nota == -1:
        break

    cont += 1

# QUESTÃO 26 #
num_user7 = int(input('Digite um número: '))

if num_user7 < 0:
    print('Fatorial não é definido para números negativos.')
else:
    fatorial = 1
    contador = num_user7

    while contador > 1:
        fatorial *= contador
        contador -= 1

    print(f'O fatorial de {num_user7} é {fatorial}.')

# QUESTÃO 27 #
frase = input("Digite uma frase: ")
i27 = 0
vogais = 0
while i27 < len(frase):
    if frase[i27].lower() in 'aeiou':
        vogais += 1
    i27 += 1
print("Total de vogais:", vogais)

# QUESTÃO 28 #
soma28 = 0
while soma28 <= 50:
    num = int(input("Digite um número: "))
    soma28 += num
print("Soma final:", soma28)

# QUESTÃO 29 #
i29 = 1
soma_idades = 0
while i29 <= 5:
    idade = int(input(f"Digite a idade {i29}: "))
    soma_idades += idade
    i29 += 1
media = soma_idades / 5
print("Média das idades:", media)

# QUESTÃO 30 #
numeros = list()
entrada = input("Digite um número ou 'fim' para encerrar: ")
while entrada.lower() != 'fim':
    numeros.append(int(entrada))
    entrada = input("Digite um número ou 'fim' para encerrar: ")
print("Números digitados:")
i30 = 0
while i30 < len(numeros):
    print(numeros[i30])
    i30 += 1
