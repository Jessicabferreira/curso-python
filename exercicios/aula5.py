"""
+, -, *, /, //, **, %, ()
"""
print('Multiplicação * ', 10 * 10)
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 5)
print('Divisão / ', 10 / 2)
print()
print()
#  Comportamentos diferentes
print('Multiplicação * ', 10 * '10')  # Colocar int com str da uma repetição e não soma
print('Multiplicação * ', 5 * 5)  # Colocando dois int temos a soma
print('Multiplicação * ', '5' + '5')  # Temos a concatenação = junta as duas str
# print('Multiplicação * ', 5 + '5') str com int da erro, ele não soma, precisa converter
print()
print()
print(10 / 3)  # Diferença de divisão normal / retorna o valor real com floo bem grande e  divisão inteira // vai
# arredondar o valor
print(2 ** 10)  # Potenciação 2 elevado a 10
print(10 % 3)  # Modulo resto da divisão
print(5+2*10)
print((5+2)*10)  # () Alterar a precedencia dos operadores
