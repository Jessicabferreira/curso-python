"""
 FUNÇÕES BUILT-IN
isnumeric, isdigt e isdecimal. Checa se a str pode ser convertida em numero int
"""
# EXEMPLO1 // Primeiro ex. não tem função para converter numeros,
# então aparecerá um erro, ele esta em int mas se converter os dois o usuario nao podera colocar letras que dara erro
num_1 = input('Digite um número: ')
num_2 = input('Digite outro numero: ')

#num_1 = int(num_1)
#num_2 = int(num_2)
#print(num_1 + num_2)
#print()
     #EXEMPLO2
if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
else:
     print('Não pude converter os números para realizar contas.')