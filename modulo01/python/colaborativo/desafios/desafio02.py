nome = str(input('Nome: '))
valor = float(input('Valor por hora: '))
horas = int(input('Horas trabalhadas: '))

pagamento = valor * horas

print(f'O pagemento para {nome} deve ser R${pagamento:.2f}')