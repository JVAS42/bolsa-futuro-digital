Algoritmo "questao10"
// Disciplina   : Curso Back-end Python BFD
// Professor   : Glestiano
// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 22/08/2025
Var
// Seção de Declarações das variáveis
nota1, nota2, nota3, media: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreva("Nota1: ")
leia(nota1)
escreva("Nota2: ")
leia(nota2)
escreva("Nota3: ")
leia(nota3)

media <- (nota1 + nota2 + nota3) / 3


se media >= 7 entao
    escreva("Aprovado")
senao
    escreva("Reprovado")
fimse

Fimalgoritmo