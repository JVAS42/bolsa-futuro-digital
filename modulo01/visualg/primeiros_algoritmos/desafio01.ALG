Algoritmo "DESAFIO 1"
// Disciplina   : Curso Back-end - Python BFD
// Professor   : Glestiano
// Autor(a)    : Jo�o Victor de Ara�jo Silva
// Data atual  : 19/08/2025
Var
// Se��o de Declara��es das vari�veis
   quantidade: inteiro
   preco, dinheiro, troco: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
   escreva("Pre�o unit�rio do produto: ")
   leia(preco)
   escreva("Quantidade comprada: ")
   leia(quantidade)
   escreva("Dinheiro recebido: ")
   leia(dinheiro)
   troco <- dinheiro - (preco*quantidade)
   escrevaL("Troco =", troco)

Fimalgoritmo