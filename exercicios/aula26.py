"""
Split, Join, Enumerate em Python
* Split - Dividir uma string, gerando uma lista dependendo do valor # str
* Join - Juntar elemento de uma lista baseado no caracter que passamos # str
* Enumerate - Enumerar elemento da lista  ela retorna tuplas # iteráveis
"""

# Exemplo1
string = 'O Brasil é o pais do futebol, o Brasil é o penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.' )
print()

# Exemplo 2
string = 'O Brasil é o o o pais do futebol, o Brasil é o penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
print()

# Exemplo 3
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)
print()

# Exemplo 4
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)
print()

# Exemplo 5
lista = [
    [0, 'Jessica'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, nome in lista:
    print(indice, nome)

