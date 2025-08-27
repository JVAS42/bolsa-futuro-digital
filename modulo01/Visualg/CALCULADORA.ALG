Algoritmo "CALCULADORA"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/8/2025
Var
// Seção de Declarações das variáveis 
x, y, final: real
op: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Valor1: ")
leia(x)
escreva("Operação: ")
leia(op)
escreva("Valor2: ")
leia(y)

se op = "+" entao
   final <- x + y
   escreva(final)
senao
     se op = "-" entao
        final <- x - y
        escreva(final)
     senao
          se op  = "*" entao
             final <- x * y
             escreva(final)
          senao
               se op = "/" entao
                  final <- x / y
                  escreva(final)
               senao
                    escreva("Operação informado está incorreto")
               fimse
          fimse
     fimse
fimse

Fimalgoritmo