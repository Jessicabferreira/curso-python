"""
Iniciar com letras, pode conter números, separar _, letras minúsculas
"""
nome = 'Jessica'  # Variavel é apelido para algum objeto
print(nome, type(nome))
print()
nome = "Jessica Ferreira"
idade = 26 # int
altura = 1.56 # float
e_maior = idade > 18 # bool, comparação
peso = 55
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
