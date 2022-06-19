import functools as ft

# partial, eu posso inserir um arg em uma função(alterar a função parcialmente)
print('will', 'foi',sep="   \o/   ")

myprint = ft.partial(print, sep="----")
myprint('will','yziima')