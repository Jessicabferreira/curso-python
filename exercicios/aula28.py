"""
Desempacotamento de listas em Python
"""
# Exemplo 1
lista = ['Jessica', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista  # * resto do valor

print(n1, n2, outra_lista)
print(ultimo_da_lista)
print()

# Exemplo 2
lista = ['Jessica', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 100]

n1, n2, *_ = lista  # *_ indica que essa varial não sera usada no restante do código

print(n1, n2)



