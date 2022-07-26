nome = "Jessica Ferreira"
idade = 26 # int
altura = 1.56 # float
e_maior = idade > 18 # bool, comparação
peso = 55
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # {imc:.2f} 2 casas decimais no imc "f str"
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))  # .format
print('{0} {0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc)) # caso queira repetir algum objeto
