"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiro (int)
:f - Números de ponto flutuante (float)
:.número de casaf ex: :.2f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ⁾ (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(divisao)
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_2 = 3
print(f'{num_2:0>10}')
print(f'{num_2:0<10}')
print(f'{num_2:0^10}')
print(print(f'{num_2:0>10.2f}')) #float

nome = 'Jessica Ferreira'
print((50-len(nome)) / 2 )
print(f'{nome:#^50}')

print(nome.lower()) # Tudo minúsculo
print(nome.upper()) # Tudo maiscúlo
print(nome.title()) #Primeiras letras maiusculas