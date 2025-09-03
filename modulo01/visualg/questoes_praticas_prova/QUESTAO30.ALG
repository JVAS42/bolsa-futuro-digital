Algoritmo "QUESTAO30"

// Autor(a)    : João Victor de Araújo Silva
// Data atual  : 25/08/2025
Var
// Seção de Declarações das variáveis 
idade: inteiro
sexo: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Idade: ")
leia(idade)
escrevaL("Informe M -> Homem OU F -> Mulher")
escreva("Sexo [M/F]: ")
leia(sexo)

se (idade >= 18) entao
   se (sexo = "M") ou (sexo = "F") entao
      se (sexo = "M") entao
         escreva("Pode jogar no time masculino")
      senao
           escreva("Pode jogar no time femino")
      fimse
   senao
        escreva("Sexo informado incorreto")
   fimse
senao
     escreva("Não pode jogar")
fimse

Fimalgoritmo
