def pesos():
    quilos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    terra = quilos
    lua = [round(q * 0.165, 2) for q in quilos]
    marte = [round(q * 0.379, 2) for q in quilos]
    mercurio = [round(q * 0.377, 2) for q in quilos]
    
    return list(zip(quilos, terra, lua, marte, mercurio))

tabela = pesos()
print("Linha | Quilos | Terra | Lua  | Marte | Mercúrio")
for i, (q, t, l, m, mc) in enumerate(tabela, start=1):
    print(f"{i:<5} | {q:<6} | {t:<5} | {l:<5} | {m:<6} | {mc:<9}")