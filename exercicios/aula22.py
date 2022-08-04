#       Índices
#       0123456789.......................33


#  Exemplo 1
frase = 'o rato roeu a roupa do rei de roma'  # Iteravel, valores com índices
tamanho_frase = len(frase)
contador = 0

# Iteração <- Iterar É o ato de percorrer cada um dos elementos da str
while contador < 10:
    print(contador)
    contador += 1
print()


#  Exemplo 2
s = 'Iterando String'
indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice+=1
print()

#  Exemplo 3
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''


while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1

print(nova_string)
print()

# Exemplo 4
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''


while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'  # mudou os r minusculos para o R maisculos na frase
    else:
        nova_string += letra
    contador += 1

print(nova_string)
