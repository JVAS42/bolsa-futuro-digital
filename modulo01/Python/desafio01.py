preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))

troco = dinheiro - (preco * quantidade)
print(f'TRCO = {troco}')