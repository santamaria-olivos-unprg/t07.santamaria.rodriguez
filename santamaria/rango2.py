#Programa que muestre la suma de los números del 1 al 20 solo de los pares

suma=0

for i in range(21):
    if((i%2)==0):
        suma=suma+i
  #fin_if
#fin_for
print("La suma es: ",suma)

