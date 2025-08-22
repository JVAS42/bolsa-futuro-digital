Algoritmo "questao12"
// Disciplina   : Curso Back-end Python BFD
// Professor   : Glestiano
// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 22/08/2025
Var
// Seção de Declarações das variáveis
quantidade: inteiro
total: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreva("Quantidade: ")
leia(quantidade)

se quantidade > 11 entao
   total <- quantidade * 0.4
   escreva("Total: R$", total)
senao
    total <- quantidade * 0.5
    escreva("Total: R$", total)
fimse

Fimalgoritmo