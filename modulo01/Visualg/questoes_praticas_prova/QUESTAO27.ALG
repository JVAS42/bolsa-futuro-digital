Algoritmo "QUESTAO27"

// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 25/08/2025
Var
// Seção de Declarações das variáveis 
nota: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Nota: ")
leia(nota)

se (nota <= 6) entao
   se (nota < 4) entao
      escreva("Reprovado")
   senao
        escreva("Recuperação")
   fimse
senao
     escreva("Aprovado")
fimse


Fimalgoritmo
