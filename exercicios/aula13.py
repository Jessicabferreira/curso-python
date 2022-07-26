"""
Len - Quantidade de caracteres // Não funciona com numeros // ela conta a quantidade de caracteres em uma str
"""
                             #Exemplo 1
usuario = input('Digite seu usúario: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')
    print()

                            #Exemplo2
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}') # forma mais usada
# outra forma de usar
# print(len(string2))
# print(string2.__len__())