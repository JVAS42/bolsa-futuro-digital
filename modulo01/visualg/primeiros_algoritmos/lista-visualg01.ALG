Algoritmo "LISTA 1"
// Disciplina   : Curso Back-end - Python BFD
// Professor   : Glestiano
// Autor(a)    : Jo�o Victor de Ara�jo Silva
// Data atual  : 18/08/2025
Var
   valor1, valor2, soma: real
   nome: caracter
   idade: inteiro
   vi: logico
   
Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   escrevaL("--- Quest�o 1 - Soma ---")
   escreva("Informe o primeiro valor: ")
   leia(valor1)
   escreva("Informe o segundo valor: ")
   leia(valor2)
   soma <- valor1 + valor2
   escrevaL(valor1, " +", valor2, " =", soma)
   
   escrevaL("--- Quest�o 2 - Nome ---")
   escreva("Informe seu nome: ")
   leia(nome)
   escrevaL("Ol�, ", nome, ", seja bem-vindo.")
   
   escrevaL("--- Quest�o3 - Idade ---")
   escrevaL("FALSO -> MENOR DE IDADE")
   escrevaL("VERDADEIRO -> MAIOR DE IDADE")
   escreva("Informe a idade da pessoa: ")
   leia(idade)
   vi <- idade >= 18
   escrevaL("A pessoa � maior de idade:", vi)
   
Fimalgoritmo