# QUESTÃO 1 #
for i in range(1, 11):
    print(i)

# QUESTÃO 2 #
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# QUESTÃO 3 #
valor_tabuada = 5
for i in range(1, 11):
    print(f'{valor_tabuada} X {i} = {valor_tabuada*i}')

# QUESTÃO 4 #
valor_tabuada = int(input('Informe o valor da tabuada: '))
for i in range(1, 11):
    print(f'{valor_tabuada} X {i} = {valor_tabuada*i}')

# QUESTÃO 5 #
soma = 0
for i in range(1, 101):
    soma += i

print(soma)

# QUESTÃO 6 #
palavra = input('Informe uma palavra: ')
cont = 0
for i in range(0, len(palavra)):
    cont += 1
print(f'A palavra {palavra} tem {cont} caracteres')


# QUESTÃO 12 #
numeros = []
for i in range(0, 5):
    num = int(input(f'Informe o {i+1}º número: '))
    numeros.append(num)

print('Números na ordem inversa:')
for i in range(4, -1, -1):
    print(numeros[i])

# QUESTÃO 7 #
palavra = input('Informe um palavra: ')
for i in range(0, len(palavra)):
    print(palavra[i])

# QUESTÃO 8 #
palavra = input('Informe um palavra: ')
for i in range(0, len(palavra)):
    if palavra[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
        print(palavra[i])

# QUESTÃO 9 #
media = 0
for i in range(0, 10):
    num = float(input)
    soma += num

print(f'MEDIA = {soma/10}')

# QUESTÃO 10 #
fator = int(input('Informe um número: '))
fatorial = 1
for i in range(fator, 1, -1):
    fatorial *= i

print(fatorial)
    

# QUESTÃO 11 #
cont = 0
frase = input('Informe um a frase: ')
for i in range(0, len(frase)):
    if frase[i] == ' ':
        cont += 1
print(f'TEM {cont} ESPAÇOS NA FRASE {frase}')

# QUESTÃO 12 #


# QUESTÃO 13 #
lista_nome = list()
for i in range(0, 5):
    nome = input(f'Informe {i+1}º nome: ')
    lista_nome.append(nome)

print(lista_nome[::-1])

# QUESTÃO 14 #
maior = 0
menor = 0
for i in range(0, 5):
    valor = int(input(f'Informe o {i+1}º valor: '))
    if i == 0:
        maior = valor
        menor = valor
    else: 
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'MENOR VALOR = {menor} e MAIOR VALOR = {maior}')

# QUESTÃO 15 #
for i in range(0, 31):
    if i % 2 != 0:
        print(i)

# QUESTÃO 16 #
for i in range(1, 11):
    print(i ** 2)

# QUESTÃO 17 #
cont = 0
for i in range(0, 5):
    valor = int(input(f'Informe o {i+1}º: '))
    if valor >= 0:
        cont += 1

# QUESTÃO 18 #
palavra = input('Informe uma palavra: ')
invertida = ''
for i in range(len(palavra)-1, -1, -1):
    invertida += palavra[i]
print(f'A palavra invertida é {invertida}')


# QUESTÃO 19 #
numeros = []
for i in range(0, 10):
    num = int(input(f'Informe o {i+1}º número: '))
    numeros.append(num)

print('Números pares:')
for i in range(0, 10):
    if numeros[i] % 2 == 0:
        print(numeros[i])

# QUESTÃO 20 #
elementos = list()
for i in range(0, 10):
    valor = input(f'Adicione o {i+1}º elemento: ')
    elementos.append()

for j in range(0, 10):
    print(f'{i+1}º = {elementos[j]}')

# QUESTÃO 21 #
for i in range(10, 0, -1):
    print(i)

# QUESTÃO 22 #
nome_mais_letras = ''
for i in range(0, 5):
    nome = input(f'Informe o {i+1}º nome: ')
    if len(nome) > len(nome_mais_letras):
        nome_mais_letras = nome
print(f'O nome com mais letras é: {nome_mais_letras}')


# QUESTÃO 23 #
soma = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma += soma

print(f'A SOMA DOS PARES É {soma}')

# QUESTÃO 24 #
num = int(input('Informe um número: '))
print(f'Divisores de {num}:')
for i in range(1, num + 1):
    if num % i == 0:
        print(i)


# QUESTÃO 25 #
cont = 0
for i in range(0, 10):
    idade = int(input(f'Informe a {i+1}ª idade: '))
    if idade >= 18:
        cont += 1
print(f'TOTAL DE PESSOAS COM 18 ANOS OU MAIS: {cont}')


# QUESTÃO 26 #
cont = 0
frase = input('Informe uma frase: ')
for i in range(0, len(frase)):
    if frase[i].lower() == 'a':
        cont += 1

print(f'QUANTIDADE DE LETRAS [A] = {cont}')

# QUESTÃO 27 #
soma = 0
for i in range(1, 11):
    valor = int(input(f'Informe o {i}º valor: '))
    soma += valor
print(f'A soma dos 10 valores é {soma}')

# QUESTÃO 28 #
maior = 0
for i in range(0, 5):
    valor = int(input(f'Informe o {i+1}º valor: '))
    if valor > maior and valor % 2 != 0:
        maior = valor

print(f'MAIOR VALOR ÍMPAR {maior}')

# QUESTÃO 29 #
for i in range(100, 50, -1):
    print(i)

# QUESTÃO 30 #
cont = 0
for i in range(0, 10):
    valor = int(input(f'Informe o {i+1}º valor: '))
    if valor > 0:
        cont += 1

print(f'TOTAL DE NÚMEROS NEGATIVOS É {cont}')