# QUESTÃO 1 #
class Pessoa:
    pass

p1 = Pessoa()
p1.nome = "Ana"

p2 = Pessoa()
p2.nome = "Beto"

print(p1.nome)
print(p2.nome)

# QUESTÃO 2 #
class Animal:
    pass

a1 = Animal()
a1.tipo = "cachorro"

a2 = Animal()
a2.tipo = "gato"

print(a1.tipo)
print(a2.tipo)

# QUESTÃO 3 #
class Carro:
    estado = 'novo'

fusca = Carro()
ferrari = Carro()

ferrari.estado = 'usado'

print(fusca.estado)
print(ferrari.estado)

# QUESTÃO 4 #
class Carro:
    estado = 'novo'

fusca = Carro()
fusca.cor = "azul"

ferrari = Carro()
ferrari.cor = "vermelho"
ferrari.estado = 'usado'

print(fusca.cor)
print(ferrari.cor)

# QUESTÃO 5 #
class Aluno:
    nome = ""
    nota = 0.0

aluno1 = Aluno()

aluno1.nome = input('Informe o nome: ')
aluno1.nota = float(input('Informe a nota: '))

print(f'Nome: {aluno1.nome} | Nota: {aluno1.nota}')

# QUESTÃO 6 #
class ContaBancaria:
    saldo = 0.0

c1 = ContaBancaria()
c1.saldo = 1500.50

c2 = ContaBancaria()
c2.saldo = 530.30

print(f'Conta 1 = R${c1.saldo}')
print(f'Conta 2 = R${c2.saldo}')

# QUESTÃO 7 #
class ContaBancaria:
    saldo = 0.0

    def mostrar_saldo(self):
        print(f'SALDO = R${self.saldo}')

c1 = ContaBancaria()
c1.saldo = 1500.50

c2 = ContaBancaria()
c2.saldo = 530.30

c1.mostrar_saldo()
c2.mostrar_saldo()

# QUESTÃO 8 #
class Produto:
    nome = ""
    preco = 0.0

p1 = Produto()
p1.nome = "Notebook"
p1.preco = 3500.00

p2 = Produto()
p2.nome = "Mouse"
p2.preco = 80.00

p3 = Produto()
p3.nome = "Teclado"
p3.preco = 150.00

print(f"Produto: {p1.nome}, Preço: R$ {p1.preco}")
print(f"Produto: {p2.nome}, Preço: R$ {p2.preco}")
print(f"Produto: {p3.nome}, Preço: R$ {p3.preco}")

# QUESTÃO 9 #
class Computador:
    ligado = False

    def ligar(self):
        self.ligado = True

pc = Computador()

print(pc.ligado)
pc.ligar()
print(pc.ligado)

# QUESTÃO 10 #
class Lampada:
    estado = 'apagado'

    def ligar(self):
        self.estado = 'acesa'

l1 = Lampada()
print(l1.estado)
l1.ligar()
print(l1.estado)

# QUESTÃO 11 #
class Funcionario:
    nome = ""
    salario = 0.0

f1 = Funcionario()
f2 = Funcionario()

f1.nome = "Carlos"
f2.nome = "Daniel"

f1.salario = 1300.50
f2.salario = 850.00

print(f'Funcionario: {f1.nome} Salario: R${f1.salario}')
print(f'Funcionario: {f2.nome} Salario: R${f2.salario}')

# QUESTÃO 12 #
class Cachorro:
    def latir(self):
        print('Au Au!')

dog = Cachorro()
dog.latir()

# QUESTÃO 13 #
class Celular:
    def __init__(self, bateria):
        self.bateria = bateria

    def carregar(self, valor_carga):
        self.bateria += valor_carga
        if self.bateria > 100:
            self.bateria = 100

celular = Celular(20)
print(celular.bateria)

celular.carregar(50)
celular.carregar(40)

print(celular.bateria)

# QUESTÃO 14 #
class Livro:
    titulo = ""
    autor = ""

l1 = Livro()
l1.titulo = "Dom Casmurro"
l1.autor = "Machado de Assis"

l2 = Livro()
l2.titulo = "O Senhor dos Anéis"
l2.autor = "J.R.R. Tolkien"

print(f"Livro 1: {l1.titulo}, por {l1.autor}")
print(f"Livro 2: {l2.titulo}, por {l2.autor}")

# QUESTÃO 15 #
class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
    
    def dados_alunos(self):
        print(f'ALUNO: {self.nome} do CURSO: {self.curso}')

a1 = Aluno("Carla", "Engenharia")
a2 = Aluno("Marcos", "Medicina")

a1.dados_alunos()
a2.dados_alunos()

# QUESTÃO 16 #
class Conta:
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")

minha_conta = Conta()
print(minha_conta.saldo)

minha_conta.depositar(100)
print(minha_conta.saldo)

# QUESTÃO 17 #
class Conta:
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        else:
            print(f"Saque de R$ {valor} falhou. Saldo insuficiente ou valor inválido.")

conta = Conta()
conta.depositar(200)

conta.sacar(50)
conta.sacar(300)

print(conta.saldo)

# QUESTÃO 18 #
class Pessoa:
    def falar(self):
        print("Olá, tudo bem?")

p = Pessoa()
p.falar()

# QUESTÃO 19 #
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

marca_user = input("Digite a marca: ")
modelo_user = input("Digite o modelo: ")
ano_user = int(input("Digite o ano: "))

meu_carro = Carro(marca_user, modelo_user, ano_user)

meu_carro.exibir_info()

# QUESTÃO 20 #
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

r1 = Retangulo(10, 5)
valor_area = r1.area()

print(f"A área do retângulo é: {valor_area}")

# QUESTÃO 21 #
class Aluno:
    pass

    def media(self, n1, n2):
        return (n1+n2)/2
    
a1 = Aluno()
print(f'MÉIDA = {a1.media(10, 9)}')

# QUESTÃO 22 #
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

# QUESTÃO 23 #
class Pessoa:
    def __init__(self, idade):
        self.idade = idade

    def maior_idade(self, idade):
        if self.idade < 18:
            return False
        else:
            return True
        
p1 = Pessoa(20)
p2 = Pessoa(15)


print(f'Pessoa 1 é maior de idade? {p1.maior_idade(p1.idade)}')
print(f'Pessoa 2 é maior de idade? {p2.maior_idade(p2.idade)}')

# QUESTÃO 24 #
class Banco:
    def __init__(self, clientes):
        self.clientes = clientes

    def adicionar(self, nome):
        self.clientes.append(nome)

bb = Banco([])
bb.adicionar('Joao')
print(bb.clientes)
bb.adicionar('Arthur')
bb.adicionar('Caio')
print(bb.clientes)

# QUESTÃO 25 #
class Motor:
    ligado = False

    def ligar_motor(self):
        self.ligado = True

motor = Motor()

print(motor.ligado)
motor.ligar_motor()
print(motor.ligado)

# QUESTÃO 26 #
class Casa:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

casinha = Casa("Verde", "Pequeno")
casa = Casa("Azul", "Médio")

print(f'CASINHA TEM COR: {casinha.cor} E TAMANHO: {casinha.tamanho}')
print(f'CASA TEM COR: {casinha.cor} E TAMANHO: {casinha.tamanho}')

# QUESTÃO 27 #
class Pessoa:
    def __init__(self):
        print('Pessoa Criada')

p1 = Pessoa()
p2 = Pessoa()

# QUESTÃO 28 #
class Carro:
    def __init__(self, estado):
        self.estado = estado
    
    def mostrar_estado(self):
        print(f'ESTADO DO CARRO: {self.estado}')

fusca = Carro("Usado")
ferrari = Carro("Novo")

fusca.mostrar_estado()
ferrari.mostrar_estado()

# QUESTÃO 29 #
class Computador:
    def __init__(self, ligado):
        self.ligado = ligado

    def ligar(self):
        self.ligado = True

    def info(self):
        if self.ligado == True:
            print('LIGADO')
        else:
            print('DEDLIGADO')

notebook = Computador(False)
notebook.info()
notebook.ligar()
notebook.info()

# QUESTÃO 30 #
class Aluno:
    def __init__(self):
        pass

    def situacao(self, nota):
        if nota >= 7:
            print('APROVADO')
        else:
            print('REPROVADO')

a1 = Aluno()
a2 = Aluno()

a1.situacao(9)
a2.situacao(5)