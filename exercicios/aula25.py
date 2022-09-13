"""
For / Else em Python
"""
variavel = ['Jessica', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('p'):
        continue
    print(valor)