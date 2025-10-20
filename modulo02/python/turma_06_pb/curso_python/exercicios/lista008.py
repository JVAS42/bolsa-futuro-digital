import random

# QUESTÃO 1 #
for i in range(1, 11):
    if i == 5:
        break
    else:
        print(i)

# QUESTÃO 2 #
for i in range(1, 11):
    if i%2 == 0:
        continue
    print(i)

# QUESTÃO 3 #
num = 0
while True:
    num += 1
    if num > 15:
        break
    print(num)

# QUESTÃO 4 #
nomes = ['Ana', 'Joao', 'Mariana', 'Lucas', 'Beatriz', 'Rafael', 'Camila', 'Pedro', 'Isabela', 'Gabriel']
for i in range(0, len(nomes)):
    if nomes[i][0] == 'A':
        continue
    print(nomes[i])

# QUESTÃO 5 #
for i in range(10, 0, -1):
    if i == 7:
        break
    print(i)

# QUESTÃO 6 #
num = 1
while num < 15:
    if num % 3 == 0:
        continue
    print(num)
    num += 1

# QUESTÃO 7 #
numeros = list()

for i in range(0, 50):
    n = random.randint(0, 9999)
    numeros.append(n)

for i in range(0, len(numeros)):
    if numeros[i] == 50:
        break

    print(i)

# QUESTÃO 8 #
for i in range(1, 21):
    if num%2 == 0:
        continue
    print(i)

# QUESTÃO 9 #
frutas = [
    "Maçã", "Banana", "Laranja", "Uva", "Morango", "Abacaxi", "Melancia", "Manga", "Kiwi", "Mamão",
    "Pera", "Limão", "Caju", "Goiaba", "Acerola", "Jabuticaba", "Pitaya", "Melão", "Coco", "Amora",
    "Framboesa", "Abacate", "Maracujá", "Tangerina", "Caqui", "Graviola", "Carambola", "Jaca", "Cupuaçu", "Pitanga",
    "Figo", "Romã", "Nectarina", "Cereja", "Pêssego", "Lichia", "Cambuci", "Açaí", "Tucumã", "Sapoti",
    "Guaraná", "Siriguela", "Tamarindo", "Buriti", "Jenipapo", "Pupunha", "Bacaba", "Pequi", "Murici", "Umbu"
]

for i in range(0, len(frutas)):
    if frutas[i].lower() == "banana":
        break
    print(frutas[i])

# QUESTÃO 10 #
while True:
    numero_user = float(input('Informe um número: '))
    if numero_user == 0:
        break

# QUESTÃO 11 #
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# QUESTÃO 12 #
for i in range(0, len(frutas)):
    if len(frutas[i]) >= 5:
        continue
    print(frutas[i])

# QUESTÃO 13 #
for i in range(1, 51):
    if i%7 == 0:
        break
    print(i)

# QUESTÃO 14 #
for i in range(1, 21):
    if i > 10:
        continue
    print(i)

# QUESTÃO 15 #
soma = 0
valor = 0
while valor <= 100:
    if soma > 50:
        break
    soma += valor
    valor += 1

# QUESTÃO 16 #
notas = [round(random.uniform(0, 10), 1) for _ in range(20)]
for i in range(0, len(notas)):
    if notas[i] < 5:
        continue
    print(notas[i])

# QUESTÃO 17 #
for i in range(0, 31):
    if i == 25:
        break
    print(i)

# QUESTÃO 18 #
palavra = 'PaRaLeLePíPeDo'
for i in range(0, len(palavra)):
    if palavra[i] == palavra[i].upper():
        continue
    print(palavra[i])

# QUESTÃO 19 #
while True:
    palavra_user = input('Digite uma palavra: ')
    if palavra_user.lower() == 'sair':
        break
    print(palavra_user)

# QUESTÃO 20 #
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# QUESTÃO 21 #
numeros = list()

for i in range(0, 50):
    n = random.randint(-9999, 9999)
    numeros.append(n)

for i in range(0, len(numeros)):
    if numeros[i] < 0:
        break
    print(i)

# QUESTÃO 22 #
dias = ['Domingo', 'Segunda', 'Terça', 'Qurta', 'Quinta', 'Sexta', 'Sabado']
for i in range(0, len(dias)):
    if dias[i].lower() == 'domingo':
        continue
    print(dias[i])

# QUESTÃO 23 #
num = 0
while num <= 15:
    if num % 4 == 0:
        continue
    print(num)
    num += 1

# QUESTÃO 24 #
capitais = [
    "Cabul", "Pretória", "Tirana", "Berlim", "Andorra-a-Velha", "Luanda", "Riad", "Argel", "Buenos Aires", "Erevã",
    "Camberra", "Viena", "Bacu", "Nassau", "Daca", "Bridgetown", "Bruxelas", "Belmopan", "Porto Novo", "Minsk",
    "Sucre", "Sarajevo", "Gaborone", "Brasília", "Bandar Seri Begawan", "Sófia", "Uagadugu", "Gitega", "Thimphu", "Praia",
    "Yaoundé", "Ottawa", "Doha", "Santiago", "Pequim", "Nicósia", "Bogotá", "Moroni", "Brazzaville", "Pyongyang",
    "Seul", "Yamoussoukro", "San José", "Zagreb", "Havana", "Copenhague", "Cairo", "Abu Dhabi", "Quito", "Bratislava",
    "Liubliana", "Madri", "Washington, D.C.", "Tallinn", "Adis Abeba", "Manila", "Helsinque", "Paris", "Libreville", "Banjul",
    "Acra", "Tbilisi", "Atenas", "Cidade da Guatemala", "Georgetown", "Conacri", "Bissau", "Porto Príncipe", "Amsterdã", "Tegucigalpa",
    "Budapeste", "Sana", "Suva", "Reykjavík", "Nova Délhi", "Jacarta", "Teerã", "Bagdá", "Dublin", "Jerusalém",
    "Roma", "Kingston", "Tóquio", "Amã", "Pristina", "Cidade do Kuwait", "Vientiane", "Maseru", "Riga", "Beirute",
    "Monróvia", "Trípoli", "Vilnius", "Luxemburgo", "Antananarivo", "Kuala Lumpur", "Lilongwe", "Malé", "Bamaco", "Valeta",
    "Rabat", "Cidade do México", "Maputo", "Chisinau", "Mônaco", "Ulan Bator", "Podgorica", "Windhoek", "Catmandu", "Manágua",
    "Niamey", "Abuja", "Oslo", "Wellington", "Mascate", "Cidade do Panamá", "Islamabad", "Assunção", "Lima", "Varsóvia",
    "Lisboa", "Nairóbi", "Londres", "Bangui", "Santo Domingo", "Praga", "Bucareste", "Moscou", "San Marino", "Castries",
    "Dacar", "Belgrado", "Damasco", "Mogadíscio", "Sri Jayawardenepura Kotte", "Cartum", "Estocolmo", "Berna", "Bangcoc", "Dodoma",
    "Lomé", "Túnis", "Ancara", "Kiev", "Campala", "Montevidéu", "Cidade do Vaticano", "Caracas", "Hanói", "Lusaca", "Harare"
]

for i in range(0, len(capitais)):
    if capitais[i].lower() == 'paris':
        break
    print(capitais[i])

# QUESTÃO 25 #
for i in range(1, 21):
    if i == 15:
        continue
    print(i)

# QUESTÃO 26 #
num = 1
while num <= 10:
    if num == 8:
        break
    print(num)
    num += 1

# QUESTÃO 27 #
for i in range(0, len(frutas)):
    if 'a' in frutas[i].lower():
        continue
    print(frutas[i])

# QUESTÃO 28 #
for i in range(0, 31):
    if i % 13 == 0:
        break
    print(i)

# QUESTÃO 29 #
for i in range(0, len(capitais)):
    if len(capitais[i]) == 4:
        continue
    print(capitais[i])

# QUESTÃO 30 #
num = 1
while num <= 50:
    if num % 5 == 0:
        continue
    print(num)
    num += 1
