import random
import os

x=1
valor=[]

a=6
sort=[]

def digitar(dig):
    global val
    

    for i in range (a):
        val=int(input("digite um valor entre 0 a 60: "))

        while val in valor or val>60:
            val=int(input("digite um valor diferente"))






        valor.append(val) 

def sortear(sor):
    
    global y
    y=0
    

    for _ in range(6):
        sorteio= random.randint(1,10)

        while sorteio in sort:
            sorteio = random.randint(1,10)

        sort.append(sorteio)

    for val in valor:
        if val in sort:
         y+=1

       

def resultado (res):
    print("valores digitados: ",valor)
    print("numeros sorteados: ",sort)
    print("quantidade de numeros repetidos: ",y)

while x!=0:
    print("digite 1 para digitar")
    print("digite 2 para sortear")
    print("digite 3 para ver o resultado")
    print("digite 0 para sair")

    x=(int(input("digite o numero")))
    os.system('cls')

    if x==1:
        dig=0
        digitar(dig)

    if x==2:
        sor=0
        sortear(sor)

    if x==3:
        res=0
        resultado(res) 

    if x==0:
        tab=(int(input("para sair do programa")))

print("você saiu")                                           