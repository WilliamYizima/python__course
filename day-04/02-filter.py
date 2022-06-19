
"""Problema = fazer um filtro de digitos

solução com for:
"""
texto = "Will12345154534546"
result = ""

for letra in texto:
    if letra.isdigit():
        result += letra
print(result)


"""Problema = fazer um filtro de digitos

solução com filter:
"""

# paradigma funcional -> aplicando funções dentro de funções e sem variáveis de 'apoio'
print("".join(list(filter(str.isdigit, texto))))

name = 'WillL'

print(list(filter(str.isupper,name)))
# o primeiro parâmetro filtra com um bool 
# o segundo parâmetro é uma variável para aplicar o filtro

