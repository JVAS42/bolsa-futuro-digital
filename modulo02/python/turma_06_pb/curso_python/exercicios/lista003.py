# QUESTÃO 1 #
print('QUESTÃO 1')
a = input('Informe um número: ')
a = int(a)

if a > 10:
    print(f'{a} é maior que 10')

# QUESTÃO 2 #
print('QUESTÃO 2')
b = input('Informe um número: ')
b = int(b)

if b >= 0:
    print(f'{b} é positivo!')
else:
    print(f'{b} é negativo!')

# QUESTÃO 3 #
print('QUESTÃO 3')
c = input('Informe um número: ')
c = int(c)
cond = c % 2 == 0

if cond:
    print(f'O número {c} é par')
else:
    print(f'O número {c} é negativo')

# QUESTÃO 4 #
print('QUESTÃO 4')
idade = input('Informe a idade: ')
idade = int(idade)

if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')

# QUESTÃO 5 #
print('QUESTÃO 5')
senha_sistema = '12345'
senha_usuario = input('Informe a senha: ')

print('Entrou, senha correta' if senha_usuario == senha_sistema else 'Senha incorreta')

# QUESTÃO 6 #
print('QUESTÃO 6')
d = input('Informe um número: ')
d = int(d)
e = input('Informe outro número: ')
e = int(e)

if d > e:
    print(f'{d} > {e}')
elif d < e:
    print(f'{d} < {e}')
else:
    print('São IGUAIS')

# QUESTÃO 7 #
print('QUESTÃO 7')
f = input('Informe o primeiro número: ')
f = int(f)
g = input('Informe o segundo número: ')
g = int(g)
h = input('Informe o terceiro número: ')
h = int(h)

if f > g and f > h:
    print(f'Primeiro número informardo é o maior: {f}')
elif g > f and g > h:
    print(f'Segundo número informado é o maior: {g}')
elif h > f and h > g:
    print(f'O terceiro número informado é o maior: {h}')
else:
    print('Nenhuma condição foi atendida')

# QUESTÃO 8 #
print('QUESTÃO 8')
nota = input('Informe a nota do aluno: ')
nota = int(nota)

print('Aluno foi aprovado' if nota >= 7 else 'Aluno reprovado')

# QUESTÃO 9 #
print('QUESTÃO 9')
idade = input('Informe a idade: ')
idade = int(idade)

if idade < 18:
    print('Criança')
elif idade >= 18 and idade < 70:
    print('Adulto')
else:
    print('Idoso')

# QUESTÃO 10 #
print('QUESTÃO 10')
temperatura = input('Informe a temperatura: ')
temperatura = float(temperatura)

print('Está frio' if temperatura < 25 else 'Está quente')

# QUESTÃO 11 #
print('QUESTÃO 11')
turno = input('Informe o turno: ')

if turno == 'matutino':
    print('Estuda de manhã')
elif turno == 'vespertino':
    print('Estuda de tarde')
elif turno == 'noturno':
    print('Estuda de noite')
elif turno == 'integral':
    print('Estuda o dia todo')
else:
    print('Não foi informado')

# QUESTÃO 12 #
print('QUESTÃO 12')
velocidade = input('Informe a velocidade: ')
velocidade = int(velocidade)

print(f'Está a acima de 50km/h, velocidade: {velocidade}' if velocidade > 50 else 'Está abaixo de 50hm/h')

# QUESTÃO 13 #
print('QUESTÃO 13')
numero = input('Informe um número: ')
numero = int(numero)

print(f'{numero} está entre 1 e 100' if numero > 0 and numero <= 100 else 'O número está foda do intervalor')

# QUESTÃO 14 #
print('QUESTÃO 14')
i = input('Informe o primeiro número: ')
i = int(i)
j = input('Informe o segundo número: ')
j = int(j)

print(f'{i} = {j}' if i == j else 'São diferentes')

# QUESTÃO 15 #
print('QUESTÃO 15')
letra = input('Informe uma letra: ').lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Vogais')
else:
    print('Consoante')

# QUESTÃO 16 #
print('QUESTÃO 16')
l = input('Informe o primeiro número: ')
l = int(l)
m = input('Informe o segundo número: ')
m = int(m)

print(f'{l} é maior' if l > m else f'{m} é maior')

# QUESTÃO 17 #
print('QUESTÃO 17')
lado1 = input('LADO 1: ')
lado1 = int(lado1)
lado2 = input('LADO 2: ')
lado2 = int(lado2)
lado3 = input('LADO 3: ')
lado3 = int(lado3)

if lado1 == lado2 == lado3:
    print('Equílatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Isósceles')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Escaleno')
else:
    print('Não é um triangulo')

# QUESTÃO 18 #
print('QUESTÃO 18')
operacao = input('Informe a operação: ')
if operacao == '+':
    print('Soma')
elif operacao == '-':
    print('Subtração')
elif operacao == '*':
    print('Multiplicação')
else:
    print('Não foi informado operação')

# QUESTÃO 19 #
print('QUESTÃO 19')

dias = input('Informe a quantidade de dias: ')
dias = int(dias)

if dias == 365:
    print('Ano normal')
elif dias == 366:
    print('Ano bissexto')
else:
    print('Não é um ano')

# QUESTÃO 20 #
print('QUESTÃO 20')

multiplo = input('Informe um número: ')
multiplo = int(multiplo)

print('Múltiplo de 3 e 5' if multiplo % 3 == 0 and multiplo % 5 == 0 else 'Não é múltiplo')

# QUESTÃO 21 #
print('QUESTÃO 21')

preco = input('Informe o preço')
preco = float(preco)

print(f'TOTAL: R${preco*0.9}' if preco > 100 else f'TOTAL: R${preco}')

# QUESTÃO 22 #
print('QUESTÃO 22')
salario = input('Informe o salário: ')
salario = int(salario)

if salario <= 2000:
    print('Junior')
elif salario > 2000 and salario <= 4000:
    print('Pleno')
else: 
    print('Senior')

# QUESTÃO 23 #
print('QUESTÃO 23')

idade = input('Informe a idade: ')
idade = int(idade)

print('Pode dirigir' if idade >= 18 else f'Não pode dirigir')

# QUESTÃ0 24 #
print('QUESTÃO 24')

nota1 = input('Informe a primeira nota: ')
nota2 = input('Informe a segunda nota: ')

media = (nota1 + nota2)/2

if media >= 7:
    print('APROVADO')
elif media <= 7 and media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')

# QUESTÃO 25 #
print('QUESTÃO 25')

hora = input('Informe a hora: ')
hora = int(hora)

if hora <= 12:
    print('BOM DIA')
elif hora > 12 and hora <= 19:
    print('BOA TARDE')
elif hora > 19 and hora <= 24:
    print('BOA NOITE')
else:
    print('Fora do intervalo')

# QUESTÃO 26 #
print('QUESTÃO 26')

idade = input('Informe a idade: ')
idade = int(idade)

print('PODE VOTAR' if idade >= 16 else'NÃO PODE VOTAR')

# QUESTÃO 27 #
print('QUESTÃO 27')

multiplo = input('Informe um número: ')
multiplo = int(multiplo)

print('Múltiplo de 3 e 5' if multiplo % 2 == 0 and multiplo % 3 == 0 else 'Não é múltiplo')

# QUESTÃ0 28 #
print('QUESTÃO 28')

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"\nSeu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade grau I")
elif 35 <= imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III (mórbida)")

# QUESTÃO 29 #
print('QUESTÃO 29')
n = int(input("Digite um número: "))

if n%n == 0 and (n%2 == 0 or n%3 == 0):
    print('Não é primo')
else:
    print('É primo')

# QUESTÃO 30 #
print('QUESTÃO 30')

nome = input('NOME: ')
nota = input('NOTA: ')

print(f'{nome} APROVADO' if nota >= 7 else f'{nome} REPROVADO')