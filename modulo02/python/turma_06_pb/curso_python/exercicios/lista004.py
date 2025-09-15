# QUESTÕES 1 #
print('QUESTÃO 1')
nome = input('NOME: ')
print(f'Olá, {nome}! Bem-vindo ao Python.')

# QUESTÕES 2 #
print('QUESTÃO 2')
num1 = int(input('NUMERO 1: '))
num2 = int(input('NUMERO 2: '))
print(f'A soma de {num1} + {num2} = {num1 + num2}')

# QUESTÕES 3 #
print('QUESTÃO 3')
idade = int(input('IDADE: '))
print(f'Você tem anos {idade}')

# QUESTÕES 4 #
print('QUESTÃO 4')
produto = input('PRODUTO: ')
preco = float(input('PRECO: '))
print(f'O produto {produto} custa R${preco:.2f}')

# QUESTÕES 5 #
print('QUESTÃO 5')
altura = float(input('ALTURA: '))
print(f'{altura:.2f}')

# QUESTÕES 6 #
print('QUESTÃO 6')
NOME = 'Joao'
IDADE = 25

print('Meu nome é {} e tenho {} anos.'.format(NOME, IDADE))

# QUESTÕES 7 #
print('QUESTÃO 7')
num1 = int(input('NUM 1: '))
num2 = int(input('NUM 2: '))

print('O produto de {} e {} é {}'.format(num1, num2, num1*num2))

# QUESTÕES 8 #
print('QUESTÃO 8')
ALUNO = 'Joao V'
NOTA = 9.5
print('O aluno {} tirou nota {} na prova.'.format(ALUNO, NOTA))

# QUESTÕES 9 #
print('QUESTÃO 9')
pais = input()
capitao = input()
print('A capital de {} é {}.'.format(pais, capitao))

# QUESTÕES 10 #
print('QUESTÃO 10')
filme = input('FILME: ')
ano = input('ANO: ')

print('O filme {} foi lançado em {}.'.format(filme, ano))

# QUESTÕES 11 #
print('QUESTÃO 11')
pi = 3.14159
frase = "O valor de PI é aproximadamente %.2f" % pi
print(frase)

# QUESTÕES 12 #
print('QUESTÃO 12')
nome = input('NOME: ')
idade = int(input('IDADE: '))
frase = "Nome: %s | Idade: %d" % (nome, idade)
print(frase)

# QUESTÕES 13 #
print('QUESTÃO 13')
cidade = input()
estado = input()
frase = "Cidade: %s - Estado: %s" % (cidade, estado)
print(frase)

# QUESTÕES 14 #
print('QUESTÃO 14')
time = input('TIME: ')
titulos = int(input('TITULOS: '))
frase = "%s tem %d títulos" % (time, titulos)

# QUESTÕES 15 #
print('QUESTÃO 15')
temperatura = float(input('TEMPERATURA: '))
frase = "Temperatura atual: %.1f °C" % temperatura

# QUESTÕES 16 #
print('QUESTÃO 16')
nome = input('NOME: ')
idade = int(input('IDADE: '))
curso = input('CURSO: ')

print(f'O aluno {nome} tem {idade} anos e está matriculado em {curso}.')

# QUESTÕES 17 #
print('QUESTÃO 17')
num1 = float(input('NUMERO 1: '))
num2 = float(input('NUMERO 2: '))

print('{} / {} = {:.2f}'. format(num1, num2, num1/num2))

# QUESTÕES 18 #
print('QUESTÃO 18')
nota1 = float(input('NOTA 1: '))
nota2 = float(input('NOTA 2: '))
nota3 = float(input('NOTA 3: '))

frase = "NOTA 1 = %f, NOTA 2 = %f, NOTA 3 = %f, MEDIA = %1f" % (nota1, nota2, nota3, (nota1 + nota2 + nota3)/3)

# QUESTÕES 19 #
print('QUESTÃO 19')
print(f'{"PRODUTO":<15}{"PREÇO":>10}')
print('-'*25)


# QUESTÕES 20 #
print('QUESTÃO 20')
salario = float(input('SALARIO: '))
print('O funcionário recebe R${}'.format(salario))