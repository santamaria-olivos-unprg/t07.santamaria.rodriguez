#Programa que muestre la resta de los números del 0 al 31 solo de los impares
resta=0
for i in range(32):
    if((i%2)!=0):
        resta=resta-i
  #fin_if
#fin_for
print("La resta es: ",resta)


