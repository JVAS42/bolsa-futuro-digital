class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, preco):
        self.preco = self.preco * 0.9
    
p1 = Produto('Celular', 1000.00)

print(f'PRODUTO: {p1.nome} PREÇO: R${p1.preco}')
p1.desconto(p1.preco)
print(f'PRODUTO: {p1.nome} PREÇO c/ DESCONTO: R${p1.preco}')