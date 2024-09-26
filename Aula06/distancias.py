def metros():
    metros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    polegadas = [round(m * 39.37, 2) for m in metros]
    pes = [round(m * 3.281, 2) for m in metros]
    jardas = [round(m * 1.094, 2) for m in metros]
    milhas_maritim = [round(m / 1852, 6) for m in metros]
    
    return list(zip(metros, polegadas, pes, jardas, milhas_maritim))

tabela = metros()
print("Linha | Metrs | Polegadas | Pés   | Jardas | Milhas Marítimas")
for i, (m, p, pe, j, mm) in enumerate(tabela, start=1):
    print(f"{i:<5} | {m:<6} | {p:<9} | {pe:<5} | {j:<6} | {mm:<18}")