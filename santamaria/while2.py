# Programa que dado el número de rifa
# Si el número es 348,152,258
# Mostrar, Te ganaste un TV LG!

#DECLARACION
nombre,num_rifa,= "  ",0

#INPUT
num_rifa=200
num_rifa_invalida=(num_rifa!=348 and num_rifa!=152 and num_rifa!=258 )



while(num_rifa_invalida):
    nombre=input("Ingres nombre: ")
    num_rifa=int(input("Ingrese número: "))
    num_rifa_invalida=(num_rifa!=348 and num_rifa!=152 and num_rifa!=258 )

#fin_while
print(nombre,"TE GANASTE UN TV LG!!!")
