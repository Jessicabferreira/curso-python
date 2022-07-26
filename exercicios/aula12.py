"""
Operadores Lógicos

and, as duas expressao precisa ser verdadeira
or,  qualquer uma expresao verdadeira retorna verdadeiro
not, inverte a expressao
in, esta/ se esta em executa esse bloco
not in, inverte a expressao
"""
# Verdadeiro E Verdadeiro = Verdadeiro
#comparacao1 and comparacao

# Verdadeiro OU Verdadeiro
#comp1 OR comp2

   #Exemplo 1
a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')
    print()

    #Exemplo 2
a = ''  # nenhuma das expressoes tem um valor
b = 0

if not b:
    print('Por favor preencha o valor de B.')
    print()

    #Exemplo 3
nome = 'Jessica.'

if 'Jessi' in nome:
    print('Existe a palavra jessi no seu nome')
else:
    print('Não existe essa palavra no seu nome')
    print()

    #Exemplo 4
nome = 'Jessica.'

if 'Jessi' not in nome:
    print('Existe a palavra jessi no seu nome')
else:
    print('Não existe essa palavra no seu nome')

    #Exemplo 5
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Jessica'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Vocẽ está logado no sistema')
else:
    print('Usuário ou senha inválido.')