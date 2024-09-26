produto={
    "ID":2024001,
    "Produto":"Maça",
    "Preço":3.50,
    "Validade":"25/09/2024"
}
chave = [x for x in produto.keys()]
valor = [x for x in produto.values()]
x=0
while(x<len(chave)):
    print("{:<10}{:<10}".format(chave[x],valor[x]))
    x += 1