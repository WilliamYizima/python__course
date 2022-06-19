# a função any valida se pelo menos um valor é verdadeiro

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
e = ['']


print(any(a))
print(any(b))
print(any(c))
print(any(d))
print(any(e))