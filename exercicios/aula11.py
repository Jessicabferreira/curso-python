"""
Operadores Relacionais
Essas expreção retorna um valor boleano = True ou False

== pergunta algo, se é igual
= afirma salgo
> maior que
>= maio que ou igual a
< menor que
<= menor que ou igual
!= diferente
"""
 # Exemplo 1

print(2 == 1)
print(2 == 2)
print()

 # Exemplo 2

num_1 = 3
num_2 = 2

expressao = (num_1 <= num_2)

print(expressao)
print()

 # Exemplo 3

var_1 = 'Jessica'
var_2 = 'Ferreira'

expressao = (num_1 != num_2)

print(expressao)
print()

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)
#Limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empreśtimo. ')
else:
    print(f'{nome} NÃO pode pegar o empréstimo. ')
