Kg = [1,10,0.5,0.25,0.01]
g = [(x*1000) for x in Kg]
print("{:<4}{:<6}{:<8}".format("Nº","Kg","gramas"))
print("===+=====+========")
for x in range(1,len(Kg),1):
    print("{:<4}{:<6}{:<8}".format(x-1,Kg[x],g[x]))