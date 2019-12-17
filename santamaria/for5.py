#Programa que muestre la resta de los números del 10 al 31 solo de los impares
i=10
max=31
resta=0

while(i<=max):
    i=i+1
    if((i%2)!=0):
        resta=resta-i
    #fin_if
#fin_while
print("La resta es:",resta)
