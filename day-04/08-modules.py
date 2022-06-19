# mostrando todos os modulos
# print(help('modules'))
"""RANDOM"""
import random

# numero randômico de 0.0 e 1.0
print(random.random())

# numero randômico entre o intervalo
print(random.randint(1,10))

# escolhe uma das opções da lista
colors = ["red", "green", "blue"]
print(random.choice(colors))

# escolhe uma amostra conforme definido
colors = ["red", "green", "blue"]
print(random.sample(colors,2))

print('\n')
numbers = [num for num in range(0,5)]
print(random.sample(numbers, len(numbers)))
