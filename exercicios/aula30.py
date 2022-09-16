"""
Operador ternário em python = avaliam algo com base em ser verdadeiro ou falso permitindo testar uma condição em uma
única linha, substituindo o if-else multilinha tornado o código compacto.
"""

# Exemplo 1
logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)
print()

# Exemplo 2
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)
print()

# Exemplo 3
idade = 18

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')
print()

# Exemplo 4
idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(msg)

