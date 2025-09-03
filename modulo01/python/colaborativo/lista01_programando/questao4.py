print("== Quiz de Conhecimentos Gerais ==")

pontos = 0

print("1) Capital do Brasil?")
print("1- São Paulo  2- Brasília  3- Rio de Janeiro")
resp = int(input("Sua resposta: "))
if resp == 2:
    pontos += 1

print("\n2) Planeta conhecido como planeta vermelho?")
print("1- Marte  2- Júpiter  3- Vênus")
resp = int(input("Sua resposta: "))
if resp == 1:
    pontos += 1

print("\n3) Quem escreveu Dom Quixote?")
print("1- Machado de Assis  2- Cervantes  3- Shakespeare")
resp = int(input("Sua resposta: "))
if resp == 2:
    pontos += 1

print("\n4) Qual o maior oceano?")
print("1- Atlântico  2- Pacífico  3- Índico")
resp = int(input("Sua resposta: "))
if resp == 2:
    pontos += 1

print("\n5) Qual a cor da clorofila?")
print("1- Verde  2- Azul  3- Amarela")
resp = int(input("Sua resposta: "))
if resp == 1:
    pontos += 1

print(f"\nPontuação final: {pontos}/5")
if pontos == 5:
    print("Gênio!")
elif pontos >= 3:
    print("Mandou bem!")
elif pontos >= 1:
    print("Precisa estudar mais")
else:
    print("Zerou o quiz")