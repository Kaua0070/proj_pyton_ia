class Conversao:

    def velocidade():
        kmh = [75.4,30.6,120,32.8,20.8]
        mph = list(map(lambda x: round(x/1.61,2),kmh))
        return mph
    
    def temperatura():
          celsius = [45,30,12.5,32.6,50]
          fehrenheit = [round(x/1.61,2) for x in celsius]
          return fehrenheit
     
    def altura():
          metros = [10,100,500,250,1000] 
          pes = [round(x/0.3048,2) for x in metros]
          return pes
     
    def idade():
          anos = [12,29,45,2,5,10]
          meses = [x*12 for x in anos]
          x = 0
          while(x<=5):
               print(anos[x],"anos em meses são",meses[x])
               x += 1