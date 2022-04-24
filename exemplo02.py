#!/usr/bin/env python3

"""Hello World Multi Language.

Dependendo da lingua configurada no ambiente(env) o programa exibe a mensagem
correspondente. 

Usage:

Tenha a variável LANG devidamente configurada, ex:

    export LANG=pt_BR

Exec:

    python3 hello.py
            ./hello.py
"""
__version__ = "0.0.1"
__author__ = "will y."
__license__ = "Unlicense"

import os
# use export LANG=pt_BR.utf8 para mudar para pt_br
# use export LANG=it_IT.utf8 para mudar para pt_br
# use export LANG=en_US.utf8 para mudar para pt_br

current_language = os.getenv("LANG","en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"


print(msg)

# forma que o python trata um bloco principal
# if __name__ == "__main__":
#    print("Hello world!")
