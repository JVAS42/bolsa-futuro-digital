Algoritmo "questao15"
// Disciplina   : Curso Back-end Python BFD
// Professor   : Glestiano
// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 22/08/2025
Var
// Seção de Declarações das variáveis
idade: inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreva("Idade: ")
leia(idade)

se idade < 18 entao
   se idade < 12 entao
      escreva("Criança")
   senao
        escreva("Adolescente")
   fimse
senao
    escreva("Adulto")
fimse

Fimalgoritmo