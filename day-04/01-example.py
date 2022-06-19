####### BUILT IN FUNCTIONS #######
"""
    BUILT IN  são escritos em C++ -> embutido no python

    stdlib(Standard Lib) -> bibliotecas que já vem na lib padrão, 
        porém é necessário importar(import os)
"""

# a função print é uma função built in (já vem no python)
print(type(print))

# também tem um id específico
print(id(print))

# .__code__ mostra onde está o código copilado
import os
print(os.getenv.__code__)
