# QUESTÃO 1
print('QUESTÃO 1')
nome = 'Joao'
print(f'Meu nome é {nome}')

# QUESTÃO 2
print('QUESTÃO 2')
nome = str(input('Nome: '))
idade = int(input('Idade: '))
print(f'Olá {nome}, você tem {idade} anos')

# QUESTÃO 3
print('QUESTÃO 3')
cidade = input('Cidade: ')
estado = input('Estado: ')
print(f'Moro em {cidade} - {estado}')

# QUESTÃO 4
print('QUESTÃO 4')
curso = input('Curso: ')
print(f'Você escolheu o curso de {curso}')

# QUESTÃO 5
print('QUESTÃO 5')
filme = input('Filme: ')
ano = input('Ano: ')
print(f'O filme {filme} foi lançado em {ano}')

# QUESTÃO 6
print('QUESTÃO 6')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
print(f'SOMA = {num1+num2}')

# QUESTÃO 7
print('QUESTÃO 7')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
print(f'SUBTRAÇÃO = {num1-num2}')

# QUESTÃO 8
print('QUESTÃO 8')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
print(f'MULTIPLICAÇÃO = {num1*num2}')

# QUESTÃO 9
print('QUESTÃO 9')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
print(f'DIVISÃO = {num1/num2}')

# QUESTÃO 10
print('QUESTÃO 10')
num = int(input('Número: '))
print(f'DOBRO = {num*2}')

# QUESTÃO 11
print('QUESTÃO 11')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
media = (nota1+nota2+nota3)/3

print(f'MÉDIA = {media}')

# QUESTAO 12
print('QUESTÃO 12')
ano_atual = int(input('Ano atual: '))
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'IDADE {idade}')

# QUESTAO 13
print('QUESTÃO 13')
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / altura ** 2
print(f'IMC = {imc:.2f}')

# QUESTOA 14
print('QUESTÃO 14')
dias = int(input('Informe os dias: '))
horas = dias*24
print(f'{dias} em horas é {horas}')

# QUESTAO 15
print('QUESTÃO 15')
valor = float(input('Valor: '))
print(f'Valor com desconto é R${valor*0.9:.2f}')

# QUESTAO 16
print('QUESTÃO 16')
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
print(f'Maior numero {max(num1, num2)}')

# QUESTAO 17
print('QUESTÃO 17')
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
print(f'Menor numero {min(num1, num2)}')

# QUESTAO 18
print('QUESTÃO 18')
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))
soma = num1 + num2 + num3
print(f'SOMA = {soma}')

# QUESTÃO 19
print('QUESTÃO 19')
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))
media = (num1 + num2 + num3)/3
print(f'MEDIA = {media}')

# QUESTAO 20
num = int(input('Informe um número: '))
print(f'{num} é ' + ('par' if num % 2 == 0 else 'impar')) # Operadores Ternários
verifica = num % 2 == 0
print(f'É par: {verifica}')

# QUESTAO 21
print('QUESTÃO 21')
time = input('Time: ')
jogador = input('Jogador: ')
print(f'{jogador} joga no time {time}')

# QUESTAO 22
print('QUESTÃO 22')
livro = input('Livro: ')
print(f'Estou lendo o livro {livro}')

# QUESTAO 23
print('QUESTÃO 23')
profissao = input('Profissão: ')
empresa = input('Empresa: ')
print(f'Trabalho como {profissao} na {empresa}')

# QUESTAO 24
print('QUESTÃO 24')
cor = input('Cor: ')
print(f'Minha cor favorita é {cor}')

# QUESTAO 25
print('QUESTÃO 25')
animal = input('Animal: ')
nome_animal = input('Nome: ')
print(f'Meu animal de estimação é {animal} e se chama {nome}.')

# QUESTAO 26
print('QUESTÃO 26')
nome = input('Nome usuário: ')
comida = input('Comida favorita: ')
print(f'{nome} gosta de comer {comida}')

# QUESTAO 27
print('QUESTÃO 27')
cantor = input('Nome cantor: ')
musica = input('Musica: ')
print(f'{cantor} canta a música {musica}')

# QUESTAO 28 
print('QUESTÃO 28')
nome = input('Nome: ')
ano = input('Ano: ')
print(f'Visitei {cidade} em {ano}')

# QUESTAO 29
print('QUESTÃO 29')
escola = input('Escola: ')
curso = input('Curso: ')
print(f'Visitei {curso} na escola {escola}')

# QUESTAO 30
print('QUESTÃO 30')
nome_amigo = input('Nome: ')
apelido = input('Apelido: ')
print(f'Meu amigo {nome_amigo} também é conhecido como {apelido}')