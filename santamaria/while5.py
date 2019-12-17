#Ingrese una edad de una persona
#Si tiene más de 18 años es mayor de edad
# Mostrar: Tiene DNI azul

#DECLARACION
apellidos,edad=" ",0

#INPUT
apellidos=" "
edad=5
edad_invalida=(edad<17)

while(edad_invalida):
    apellidos=input("Ingresar apellidos: ")
    edad=int(input("Ingrese edad: "))
    edad_invalida=(edad<17)

#fin_while
print(apellidos,"Tiene DNI azul")
