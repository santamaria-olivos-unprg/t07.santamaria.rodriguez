# Programa para calcular si el numero obtenido es multiple de 5
# Si el numeroro es multiplo de 5
# Mostrar, Si es multiple de 5

#DECLARACION
numero=0

#INPUT
numero=9
numero_invalido=(numero%5!= 0)

while(numero_invalido):
    numero=int(input("Ingrese el número: "))
    numero_invalido=(numero%5!= 0)
#fin_while
print("El número",numero,"es multiple de 5")

