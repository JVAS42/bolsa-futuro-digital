# QUESTÃO 1 #
class Carro:
    def __init__(self, valor, estado):
        self.valor =  valor
        self.estado = estado

    
    def mostrar_estado(self):
        print(f'VALOR: {self.valor} e ESTADO: {self.estado}')


def teste1():
    fusca = Carro('Usado', 15_000)
    ferrari = Carro('Novo', 1_000_000)

    fusca.mostrar_estado()
    ferrari.mostrar_estado()


# QUESTÃO 2 #
class Motor:
    ligado = False

    def ligar(self):
        self.ligado = True


def teste2():
    motor = Motor()

    print(f'LIGADO: {motor.ligado}')
    motor.ligar()
    print(f'LIGADO: {motor.ligado}')


# QUESTÃO 3 #
class Banco:
    def __init__(self):
        self.clientes = []

    def add_cliente(self, nome):
        self.clientes.append(nome)


def teste3():
    santander = Banco()

    santander.add_cliente('Cliente1')
    print(f'CLIENTES {santander.clientes}')
    santander.add_cliente('Cliente2')
    santander.add_cliente('Cliente3')
    print(f'CLIENTES {santander.clientes}')


# QUESTÃO 4 #
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    
    def desconto(self):
        self.valor *= 0.9


def teste4():
    produto1 = Produto('Computador', 1000)
    print(f'O PRODUTO: {produto1.nome} CUSTA R${produto1.valor}')
    produto1.desconto()
    print(f'O PRODUTO: {produto1.nome} CUSTA R${produto1.valor}')


# QUESTÃO 5 #

# QUESTÃO 6 #
def soma(num1, num2):
    soma = num1 + num2
    return soma

def teste6():
    try:
        num1 = float(input('Informe primeiro número: '))
        num2 = float(input('Informe segundo número: '))

        print(f'{num1} + {num2} = {soma(num1, num2)}')

    except:
        print('ERRO')
        print('Informe apenas números!')

# QUESTÃO 7 #
def soma(num1, num2):
    soma = num1 + num2
    return soma


def teste7():
    try:
        num1 = float(input('Informe primeiro número: '))
        num2 = float(input('Informe segundo número: '))

        print(f'{num1} + {num2} = {soma(num1, num2)}')

    except:
        print('ERRO')
        print('Informe apenas números!')


# QUESTÃO 8 #
def soma_pares(list):
    soma_pares = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            soma_pares += list[i]
        else:
            continue
    return soma_pares


def teste8():
    nums = str(input())
    nums = list(map(int, nums.split()))

    print(soma_pares(nums))

def main():
    print('=== TESTE(S) ===')
    # teste1()
    # teste2()
    # teste3()
    # teste4()
    # teste6()
    # teste7()
    teste8()


if __name__ == "__main__":
    main()