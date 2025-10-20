'''

CLASSE -> OBJETO
    ATRIBUTOS -> CARACTERISTICAS
    METODOS -> FUNCOES DELE

'''

class Pessoa:
    # Método construtor para inicializar um novo objeto Pessoa
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # Um método para descrever a pessoa
    def descrever(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}m")

# Criando objetos (instâncias) da classe Pessoa
pessoa1 = Pessoa("Maria", 30, 1.65)
pessoa2 = Pessoa("João", 25, 1.80)

nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))
altura = float(input('Informe a altura: '))

pessoa3 = Pessoa(nome, idade, altura)

# Acessando os atributos e chamando os métodos dos objetos
pessoa1.descrever()
pessoa2.descrever()
pessoa3.descrever()
