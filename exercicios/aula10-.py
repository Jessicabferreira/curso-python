"""
Condições IF, ELIF e ELSE, usado nessa ordem.
"""

if False: # IF = SE
    print('Verdadeiro.')  # espaço é identação, será lido o que esta identado.
    print('teste teste2')
elif False:                 # ELIF = ELSE IF OU 'SE'.
    print('Agora é verdadeiro.')
    nome = input('Qual o seu nome? ')

    print(f'Seu nome é {nome}.')
elif False:                # PODEMOS USAR MAIS DE UMA ELIF.
    print('Mais uma verdadeira.')
    print(22 + 22)
else:                     # ELSE = 'SE NÃO' essa função não pode ser usada sozinha.
    print('A minha expresão não é verdadeira.')
    print('Ela é falsa')