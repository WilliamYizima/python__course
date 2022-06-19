nomes = ["will","sono"]

result = []

for nome in nomes:
    result.append(nome.upper())

print(result)

# faz a mesma coisa com o map
print(list(map(str.upper, nomes)))

"""
em vez de utilizar for encadeados, seria interessante utilizar o map para a extração
"""

# um payload geral:

payload_api = {
    "result": [
        {"msg":"oi1"},
        {"msg":"oi2"},
        {"msg":"oi3"},
        ]
}

def get_msg(obj):
    return obj['msg']

print(list(map(get_msg, payload_api['result'])))