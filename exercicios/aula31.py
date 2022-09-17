"""
 Expressão condicional com operador OR
"""

# Exemplo 1
nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada =( ')  # retorna falso para str vazias
print()

# Exemplo 2
nome = input('Qual o seu nome? ')
print(nome or 'Você não digitou nada!')  # se for verdadeiro retorna o primeiro, falso o segundo que esta depois do OR
print()

# Exemplo 3
a = 0
b = None
c = False
d = []
e = {}
f = 22          # vai chegar até chegar na varial verdadeira que tem um valor dentro
g = 'Jessica'

variavel = a or b or c or d or e or f or g

print(variavel)
