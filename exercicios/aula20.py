"""
while em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""
# while True:
#    nome = input('Qual o seu nome? ')   # loop infinito
#    print(f'Olá {nome}!')

# Exemplo 1
x = 0
while x < 5:
    print(x)
    x = x + 1

print('Acabou!')
print()

# Exemplo 2
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break         # break, finaliza o loop
    print(x)
    x = x + 1

print('Acabou!')
print()

# Exemplo 3
x = 0 # coluna
while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1 # x = x + 1

print('Acabou')
print()

# Exemplo 4: Calculadora simpes
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]in ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():  # isnumeric, verifica se tem só numero
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')
