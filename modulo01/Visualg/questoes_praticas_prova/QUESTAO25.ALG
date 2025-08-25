Algoritmo "QUESTAO25"

// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 25/08/2025
Var
// Seção de Declarações das variáveis 
senha1, senha2, confirmacao: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Informe a PRIMEIRA senha: ")
leia(senha1)
escreva("Informe a SEGUNDA senha: ")
leia(senha2)
confirmacao <- "1234"

se (senha1 = confirmacao) e (senha2 = confirmacao) entao
   escreva("Login efetuado")
senao
     escreva("Senha incorreta")
fimse

Fimalgoritmo
