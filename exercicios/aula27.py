"""
* Enumerate - Enumerar elementos da lista # list
"""

# Exemplo 1
lista = [
    # 0         1         2     indices
    ['Jessica', 'João', 'Pedro'],  # 0
    ['Maria', 'Aline', 'Joana'],   # 1
    ['Helena', 'Luana', 'Ana'],    # 2
]

print(lista[1][2])
print()

# Exemplo 2
lista = [
    ['Jessica', 'João', 'Pedro'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Luana', 'Ana'],
]
enumerada = enumerate(lista)  # iterar sobre ele
print(list(enumerada))
print()
"""
[ <-- Enumerate
     0  1    indices
    (0, ['Jessica', 'João', 'Pedro']), 
          0         1         2         indices
    (1, ['Maria', 'Aline', 'Joana']),   # Tuplas ()
    (2, ['Helena', 'Luana', 'Ana'])
]
"""
# Exemplo 3
lista = [
    ['Jessica', 'João', 'Pedro'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Luana', 'Ana'],
]
for v1, v2, in enumerate(lista, 53):  # Enumerate manipulado, pegou elementos do for com indices e o enumerou iniciou com outro número
    print(v1, v2)
print()

# Exemplo 4
lista = [
    # 0         1         2     indices
    ['Jessica', 'João', 'Pedro'],  # 0
    ['Maria', 'Aline', 'Joana'],   # 1
    ['Helena', 'Luana', 'Ana'],    # 2
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)
