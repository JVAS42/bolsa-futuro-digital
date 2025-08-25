Algoritmo "QUESTAO25"

// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 25/08/2025
Var
// Seção de Declarações das variáveis 
senha, confirmacao: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Informe sua senha: ")
leia(senha)
escreva("Confirme sua senha: ")
leia(confirmacao)

se (senha = confirmacao) entao
   escreva("Login efetuado")
senao
     escreva("Senha incorreta")
fimse

Fimalgoritmo