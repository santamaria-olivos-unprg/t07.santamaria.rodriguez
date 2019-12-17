edad=-1
edad_invalida=(edad < 0 or edad > 90)

while(edad_invalida):
    edad=int(input("Ingrese edad:"))
    edad_invalida=(edad < 0 or edad > 90)

#finwhile
print("edad:",edad)
