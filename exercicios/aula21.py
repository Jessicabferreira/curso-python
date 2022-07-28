"""
While / Else
contadores
acumuladores
"""
contador = 1  # pode começar com qualquer número
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print()

# Exemplo 2

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')  # Ele vai ignorar o else
print('Isso será executado.')