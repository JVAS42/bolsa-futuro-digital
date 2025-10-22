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