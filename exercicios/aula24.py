"""
Listas em Python
fatiamento
append = FINAL, insert = COMEÇO, pop = REMOVER, del = DELETAR, clear = LIMPAR, extend = JUNTAR, +
min = MENOR, max = MAIOR,
rang = OBEJETO RANGE
"""

# Exemplo 1
#         0    1    2    3    4     indices
lista = ['A', 'B', 'C', 'D', 'E']  # valores
#   -     5    4    3    2    1
print(lista[0::2])  # fatiamento pulando de 2 em 2
print()

# Exemplo 2
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2  # junção

print(l1)
print(l2)
print(l3)
print()

# Exemplo 3
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
l2.append('b')  # insere valor no final da lista
l2.insert(0, 'legal')  # insere no começo
l1.pop()   # remove o ultimo elemento

print(l1)
print(l2)
print( l2[3] )
print(l1)
print()

# Exemplo 4
#     0  1  3  4  5  6  7  8  9
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
l2.insert(0, 'legal')
print(l2)
del(l2[0])   # deletar o legal
print(l2)
print()

# Exemplo 5
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print( max(l2) )   # maior valor da lista
print( min(l2) )   # menor valor
print()

# Exemplo 6
l2 = list(range(0, 100, 8))   # range objeto iteravel
print(l2)
print()

l2 = list(range(0, 100, 8))
for valor in l2:       # iterando sobre a lista
    print(valor)
print()

# Exemplo 6
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in l2:
    soma = soma + valor

print(soma)
print()

# Exemplo 7
l2 = ['string', True, 10, -20.5]

for elem in l2:
    print(f'O tipo do elem é {type(elem)} e seu valor é {elem}')