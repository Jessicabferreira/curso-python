"""
Entrada de dados
"""
                                  #EXEMPLO 1
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2022-int(idade)

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}.')
print()

                                    #EXEMPLO2
numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite outro número: ')
numero_2 = int(numero_2)  #Temos duas formas de inverter uma str para int.

print( numero_1 + numero_2 )