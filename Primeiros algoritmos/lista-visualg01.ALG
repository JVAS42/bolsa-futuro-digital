Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/08/2025
Var
   valor1, valor2, soma: real
   nome: caracter
   idade: inteiro
   vi: logico
   
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escrevaL("--- Questão 1 - Soma ---")
   escreva("Informe o primeiro valor: ")
   leia(valor1)
   escreva("Informe o segundo valor: ")
   leia(valor2)
   soma <- valor1 + valor2
   escrevaL(valor1, " +", valor2, " =", soma)
   
   escrevaL("--- Questão 2 - Nome ---")
   escreva("Informe seu nome: ")
   leia(nome)
   escrevaL("Olá, ", nome, ", seja bem-vindo.")
   
   escrevaL("--- Questão3 - Idade ---")
   escrevaL("FALSO -> MENOR DE IDADE")
   escrevaL("VERDADEIRO -> MAIOR DE IDADE")
   escreva("Informe a idade da pessoa: ")
   leia(idade)
   vi <- idade >= 18
   escrevaL("A pessoa é maior de idade:", vi)
   
Fimalgoritmo