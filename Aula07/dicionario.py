lista = [1,2,3]
tupla = (3,7,8)
dicionario = {
    "professor":"Gustavo",
    "diciplina":"verisonamento",
    "Aluno":"moises",
    "ano":2024
    }
print(lista[2])
print(tupla[2])
print(dicionario.keys())
print(type(dicionario))
for x in dicionario.values():
    print("{:>10} {:>16}".format("valor:",x))