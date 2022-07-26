"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo iso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
# Exemplos

#positivos [012345678] indice
texto = 'Python s2'
#negativos -[987654321]

print( len(texto)) # contagem de caracteres

print( texto[3])

# fatiamento
nova_string = texto[2:6] # indice positivo
print(nova_string)

nova_string = texto[:6]
print(nova_string)

nova_string = texto[0:6:2] # indice negativo / pula de 2 em 2
print(nova_string)

nova_string = texto[:-1]
print(nova_string)

url = 'www.google.com.br/'
print( url[:-1] )  # a barra foi excluida

url = 'www.google.com.br/'
print( url[3:]) # conseguimos controlar onde começa e onde acaba