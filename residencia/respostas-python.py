#* QUESTOES PYTHON *#

# QUESTÃO 1 #
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total_estoque(self):
        return self.preco * self.quantidade

p1 = Produto("Arroz", 20.0, 10)
p2 = Produto("Feijão", 10.0, 5)
p3 = Produto("Macarrão", 5.0, 20)

print(f"{p1.nome}: {p1.valor_total_estoque()}")
print(f"{p2.nome}: {p2.valor_total_estoque()}")
print(f"{p3.nome}: {p3.valor_total_estoque()}")

# QUESTÃO 2 #
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def mostrarSaldo(self):
        print(f"Saldo: {self.saldo}")

conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.mostrarSaldo()

# QUESTÃO 3 #
class Funcionario:
    def __init__(self, salario_base):
        self.salario_base = salario_base
    
    def calcularSalario(self):
        return self.salario_base

class Gerente(Funcionario):
    def calcularSalario(self):
        return self.salario_base * 1.20

class Vendedor(Funcionario):
    def calcularSalario(self):
        return self.salario_base * 1.10

# QUESTÃO 4 #
class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        self.itens.remove(item)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

# QUESTÃO 5 #
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def buscar(self, nome):
        return [c for c in self.contatos if c.nome == nome]

    def listar_todos(self):
        for c in self.contatos: print(f"{c.nome}: {c.telefone}")

# QUESTÃO 6 #
class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.__senha = senha

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.__senha == senha

# QUESTÃO 7 #
class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.nota1 = n1
        self.nota2 = n2

    def calcularMedia(self):
        return (self.nota1 + self.nota2) / 2

alunos = [Aluno("A", 8, 9), Aluno("B", 7, 6), Aluno("C", 10, 9), Aluno("D", 5, 4), Aluno("E", 6, 8)]

# QUESTÃO 8 #
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar(self, livro):
        self.livros.append(livro)

    def listar_por_autor(self, autor):
        return [l.titulo for l in self.livros if l.autor == autor]

    def buscar_por_titulo(self, titulo):
        return [l for l in self.livros if l.titulo == titulo]

# QUESTÃO 9 #
class Produto:
    def __init__(self, preco):
        self.preco = preco

class ItemPedido:
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

class Pedido:
    def __init__(self):
        self.itens = []

    def calcular_total(self):
        return sum(i.produto.preco * i.qtd for i in self.itens)

# QUESTÃO 10 #
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, outro):
        outro.vida -= 10
        print(f"{self.nome} atacou {outro.nome}!")

p1 = Personagem("Guerreiro", 50)
p2 = Personagem("Mago", 40)
p1.atacar(p2)

# QUESTÃO 11 #
class Carro:
    def ligar(self): print("Ligado")
    def desligar(self): print("Desligado")
    def acelerar(self): print("Acelerando")
    def frear(self): print("Freando")

if __name__ == "__main__":
    c = Carro()
    c.ligar()
    c.acelerar()
    c.frear()
    c.desligar()

# QUESTÃO 12 #
class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

filmes = [Filme("Matrix", 1999, "Ficção"), Filme("Sexta-feira 13", 1980, "Terror")]
terror = [f.titulo for f in filmes if f.genero == "Terror"]

# QUESTÃO 13 #
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

# QUESTÃO 14 #
class Pagamento: # Interface (simulada em Python)
    def pagar(self): pass

class PagamentoPix(Pagamento):
    def pagar(self): print("Pago com Pix")

class PagamentoCartao(Pagamento):
    def pagar(self): print("Pago com Cartão")

# QUESTÃO 15 #
class Calculadora:
    # Python não suporta sobrecarga nativa como Java, usa-se argumentos padrão
    def somar(self, a, b, c=None):
        if c is None:
            return a + b
        return a + b + c

# QUESTÃO 16 #
class Veiculo:
    def mover(self): pass

class Carro(Veiculo):
    def mover(self): print("Carro rodando")

class Moto(Veiculo):
    def mover(self): print("Moto correndo")

# QUESTÃO 17 #
class Turma:
    def __init__(self, alunos):
        self.alunos = alunos

    def media_geral(self):
        return sum(a.calcularMedia() for a in self.alunos) / len(self.alunos)

# QUESTÃO 18 #
class Mensagem:
    def __init__(self, texto, remetente, destinatario):
        self.texto = texto
        self.remetente = remetente
        self.destinatario = destinatario

mensagens = []

# QUESTÃO 19 #
class BancoDados:
    def __init__(self): self.dados = []
    def inserir(self, item): self.dados.append(item)
    def atualizar(self, i, novo): self.dados[i] = novo
    def deletar(self, i): self.dados.pop(i)
    def listar(self): return self.dados

# QUESTÃO 20 #
class Empresa:
    def __init__(self):
        self.funcionarios = []

    def totalFolhaPagamento(self):
        return sum(f.calcularSalario() for f in self.funcionarios)
    