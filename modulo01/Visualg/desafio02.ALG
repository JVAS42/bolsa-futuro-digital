Algoritmo "DESAFIO 2"
// Disciplina   : Curso Back-end - Python BFD
// Professor   : Glestiano
// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 19/08/2025
Var
// Seção de Declarações das variáveis
   nome: caractere
   valor, pagamento: real
   hora: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   escreva("Nome: ")
   leia(nome)
   escreva("Valor por hora: ")
   leia(valor)
   escreva("Horas trabalhadas: ")
   leia(hora)
   pagamento <- valor * hora
   escrevaL("O pagamento para", nome, "deve ser R$", pagamento)

Fimalgoritmo