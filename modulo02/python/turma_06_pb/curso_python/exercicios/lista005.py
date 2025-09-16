NOME = 'Joao'

# QUESTÃO 1 #
print('QUESTÃO 1')
print(NOME[0])

# QUESTÃO 2 #
print('QUESTÃO 2')
print(NOME[-1])

# QUESTÃO 3 #
print('QUESTÃO 3')
print(NOME[2])

# QUESTÃO 4 #
print('QUESTÃO 4')
print(NOME[-2])

# QUESTÃO 5 #
print('QUESTÃO 5')
print(NOME[0])
print(NOME[1])
print(NOME[2])
print(NOME[3])

# QUESTÃO 6 #
print('QUESTÃO 6')
CONFERINDO = 'a' in NOME
print(CONFERINDO)

# QUESTÃO 7 #
print('QUESTÃO 7')
CONFERINDO = 'x' in NOME
print(CONFERINDO)

# QUESTÃO 8 #
print('QUESTÃO 8')
CONFERINDO = 'oao' in NOME
print(CONFERINDO)

# QUESTÃO 9 #
print('QUESTÃO 9')
CONFERINDO = 'tes' in NOME
print(CONFERINDO)

# QUESTÃO 10 #
print('QUESTÃO 10')
letra = input('LETRA: ')
CONFERINDO = letra in NOME
print(CONFERINDO)

# QUESTÃO 11 #
print('QUESTÃO 11')
CONFERINDO = 'z' in NOME
print(CONFERINDO)

# QUESTÃO 12 #
print('QUESTÃO 12')
CONFERINDO = 'J' in NOME
print(CONFERINDO)

# QUESTÃO 13 #
print('QUESTÃO 13')
CONFERINDO = 'ao' in NOME
print(CONFERINDO)

# QUESTÃO 14 #
print('QUESTÃO 14')
print('abc' not in 'Joao')

# QUESTÃO 15 #
print('QUESTÃO 15')
letra = input("Digite uma letra: ")
print(letra not in 'Joao')

# QUESTÃO 16 #
print('QUESTÃO 16')
print('Joao'[:4])

# QUESTÃO 17 #
print('QUESTÃO 17')
print('Joao'[-3:])

# QUESTÃO 18 #
print('QUESTÃO 18')
print('Joao'[2:7])

# QUESTÃO 19 #
print('QUESTÃO 19')
print('Joao'[::-1])

# QUESTÃO 20 #
print('QUESTÃO 20')
print('Joao'[::2])

# QUESTÃO 21 #
print('QUESTÃO 21')
print('Joao'.count('a'))

# QUESTÃO 22 #
print('QUESTÃO 22')
letra = input("Digite uma letra: ")
print('Joao'.find(letra))

# QUESTÃO 23 #
print('QUESTÃO 23')
print('Joao'.startswith('Gle'))

# QUESTÃO 24 #
print('QUESTÃO 24')
print('Joao'.endswith('ano'))

# QUESTÃO 25 #
print('QUESTÃO 25')
for i, c in enumerate('Joao'):
    print(i, c)

# QUESTÃO 26 #
print('QUESTÃO 26')
palavra = input("Digite uma palavra: ")
print(palavra in 'Joao')

# QUESTÃO 27 #
print('QUESTÃO 27')
for c in 'Joao':
    if c.lower() in 'aeiou':
        print(c)

# QUESTÃO 28 #
print('QUESTÃO 28')
for c in 'Joao':
    if c.lower() not in 'aeiou':
        print(c)

# QUESTÃO 29 #
print('QUESTÃO 29')
letra = input("Digite uma letra: ")
print('Joao'.count(letra) > 1)

# QUESTÃO 30 #
print('QUESTÃO 30')
print('Joao' == 'Joao'[::-1])
