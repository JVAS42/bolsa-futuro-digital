nome = str(input('Digite o nome do aluno: ')).capitalize()
nota = float(input('Digite a nota do aluno: '))

if nota >= 7:
    print(f'{nome} está APROVADO')
elif nota < 5:
    print(f'{nome} está REPROVADO')
else:
    print(f'{nome} está em REPOSIÇÃO')