# QUESTÕES 1 #

def sum(x, y):
    sum = x + y
    return sum

# QUESTÕES 2 #
def square(x):
    return x**2

# QUESTÕES 3 #
def bigger(x, y):
    if x > y:
        return x
    else:
        return y
    

# QUESTÕES 4 #
def pair(x):
    if x % 2 == 0:
        return True
    else:
        return False
    

# QUESTÕES 5 #
def avarege(a, b, c):
    avarege = (a+b+c)/3
    return avarege


# QUESTÕES 6 #
def area_rectangle(l, h):
    area = l * h
    return area


# QUESTÕES 7 #
def cumprimento(name):
    return f'Olá, {name}'


# QUESTÕES 8 #
def dobro(n):
    return n*2


# QUESTÕES 9 #
def resto_divisao(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        resto = a/b
        return resto
    

# QUESTÕES 10 #
def celsius_para_fahrenheit(c):
    fahrenheit = (c * (9/5)) + 32
    return fahrenheit


# QUESTÕES 11 #
import math

def hipotenusa(cat1, cat2):
    hipotenusa = math.sqrt(cat1**2 + cat2**2)


# QUESTÕES 12 #
def eh_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

# QUESTÕES 13 #
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

# QUESTÕES 14 #
def contador_vogais(texto):
    vogais = "aeiou"
    contador = sum(1 for letra in texto if letra in vogais)
    return contador

# QUESTÕES 15 #
def soma_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

# QUESTÕES 16 #
def menor_elemento(lista):
    menor = lista[i]
    for i in range(1, len(lista)):
        if menor > lista[i]:
            menor = lista[i]
    return menor

# QUESTÕES 17 #
def reverso(texto):
    reverso = texto[::-1]
    return reverso

# QUESTÕES 18 #
def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# QUESTÕES 19 #
def contar_palavras(frase):
    contar_palavras = frase.split()
    return len(contar_palavras)

# QUESTÕES 20 #
def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

# QUESTÕES 21 #
def maior_string(lista):
    maior_string = lista[0]
    for i in range(1, len(lista)):
        if len(maior_string) < len(lista[i]):
            maior_string = lista[i]
    return maior_string

# QUESTÕES 22 #
def soma_pares(lista):
    soma_pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma_pares += lista[i]
    return soma_pares

# QUESTÕES 23 #
def filtrar_pares(lista):
    lista_pares = list()
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pares.append(lista[i])
    return lista_pares

# QUESTÕES 24 #
def conversor_tempo(minutos):
    horas = minutos // 60
    minutos = minutos % 60

    return f"{horas}h: {minutos}mins"

# QUESTÕES 25 #
def calcular_desconto(valor, porcentagem):
    valor = valor - (valor*porcentagem)
    return valor

# QUESTÕES 26 #
def media_notas(notas):
    media = 0.0
    for i in range(len(notas)):
        media += notas[i]
    media = media / len(notas)
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
# QUESTÕES 27 #
def maior_diferenca(lista):
    menor = lista[0]
    maior = lista[0]

    for i in range(1, len(lista)):
        if menor > lista[i]:
            menor = lista[i]

        if maior < lista[i]:
            maior = lista[i]
    
    maior_diferenca = maior - menor
    return maior_diferenca

# QUESTÕES 28 #
def palindromo(texto):
    palindromo = texto[::-1]

    if texto == palindromo:
        return True
    else:
        return False
    
# QUESTÕES 29 #
def ocorrencias(texto, letra):
    contador = 0
    for caractere in texto:
        if caractere == letra:
            contador += 1
    return contador

# QUESTÕES 30 #
def gerar_email(nome, sobrenome):
    return f"{nome}.{sobrenome}@email.com"