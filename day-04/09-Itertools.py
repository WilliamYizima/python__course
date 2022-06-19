import itertools as it

# iteração infinita da interação------
# for item in it.cycle("ABCD"):
#     print(item)

# utilização interessante - para no index 10 
# for index, item in enumerate(it.cycle("ABCD")):
#     if index == 10:
#         break
#     print(item)

# iteração com o repeat------
# print(("will " *10).split(" "))
# com itertools
# print(list(it.repeat("will",10)))

# iteração com o accumulate------
# numeros = [1,2,3,4,5,6]
# # sum destrinchado
# print(list(it.accumulate(numeros)))

# iteração com o product------
produto = "abc"
#combinações
print(list(it.product("abc", repeat=2)))
print('\n')
print(list(it.product("abc", repeat=3)))
print('\n')
print(list(it.permutations("abc")))
print('\n')
print(list(it.combinations(['blue','green','red'],2)))
print('\n')
print('\n')
