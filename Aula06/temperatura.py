def temperatura():
    kelvin = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475]
    celsius = [k - 273.15 for k in kelvin]
    fahrenheit = [round((k - 273.15) * 9/5 + 32, 2) for k in kelvin]
    return list(zip(kelvin, celsius, fahrenheit))

tabela = temperatura()
print("Linha | Kelvin | Celsius | Fahrenheit")
for i, (k, c, f) in enumerate(tabela, start=1):
    print(f"{i:<5} | {k:<6} | {c:<7} | {f:<10}")