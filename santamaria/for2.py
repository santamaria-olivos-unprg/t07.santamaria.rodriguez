#Programa que muestre la suma de los números del 1 al 20 solo de los pares
i=0
max=20
suma=0

while(i<=max):
    i=i+1
    if((i%2)==0):
        suma=suma+i
    #fin_if
#fin_while
print("La suma es:",suma)
