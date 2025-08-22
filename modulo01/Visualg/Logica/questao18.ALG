Algoritmo "questao18"
// Disciplina   : Curso Back-end Python BFD
// Professor   : Glestiano
// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 22/08/2025
Var
// Seção de Declarações das variáveis
nota: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreva("Nota: ")
leia(nota)

se nota >= 9 entao
   escreva("A")
senao
     se nota >= 7 entao
        escreva("B")
     senao
          se nota >= 5 entao
             escreva("C")
          senao
               escreva("D")
          fimse
     fimse
fimse

Fimalgoritmo