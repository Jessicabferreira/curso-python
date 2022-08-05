"""
For in em Python
Iterando strings com for
Função range
star=0, de qual numero vai iniciar
stop,
step=1, de quantas em quantas casas vai pular
"""
# Exemplo 1
texto = 'python'

for letra in texto:
    print(letra)
print()

# Exemplo 2
for numero in range(20, 9, -1):  # conta de forma decrescente
    print(numero)
print()

# Exemplo 3
for numero in range(0, 10, 3):  # pula de 3 em 3
    print(numero)
print()

# Exemplo 4
# enumerate enumera a cada volta do laço
texto = 'python'

for n, letra in enumerate(texto):
    print(n, letra)
print()

# Exemplo 5
for n in range(100):
    if n % 8 == 0:
        print(n)
print()