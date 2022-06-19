# a função all valida se todos os valores são true

#exemplo:

a = [
    True, 
    True, 
    False
    ]

b = [
    True, 
    True, 
    True,
    ]
c = [
    'a', 
    True, 
    'afasf',
    ]
d = [
    '', 
    True, 
    'afasf',
    ]


print(all(a))
print(all(b))
print(all(c))
print(all(d))