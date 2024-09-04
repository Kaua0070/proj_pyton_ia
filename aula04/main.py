from Lambda import *

class Main:
    x=int(input("Escolha a sua operaçao:\n1 - adiçao\n2 - subtraçao\n3 - multiplicaçao\n4 - divisao"))
    if(x==1):
      a=int(input("Digite o n1: "))
      b=int(input("Digite o n2 "))
      print(Lambda.adi(a,b))
    if(x==2):
        a=int(input("Digite o n1: "))
        b=int(input("Digite o n2: "))
        print(Lambda.sub(a,b))
    if(x==3):
      a=int(input("Digite o n1: "))
      b=int(input("Digite o n2 "))
      print(Lambda.mul(a,b))
    if(x==4):
      a=int(input("Digite o n1: "))
      b=int(input("Digite o n2 "))
      print(Lambda.div(a,b))