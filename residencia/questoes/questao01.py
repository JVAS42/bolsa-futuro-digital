class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valor_total(self):
        return self.preco * self.quantidade
    
def main():
    produto1 = Produto('Teclado', 150, 3)
    produto2 = Produto('Mouse', 75, 5)
    produto3 = Produto('Fone', 40, 10)

    total_estoque = (
        produto1.valor_total() +
        produto2.valor_total() +
        produto3.valor_total()
    )

    print(f'VALOR TOTAL DO ESTOQUE: R${total_estoque}')

if __name__ == "__main__":
    main()
