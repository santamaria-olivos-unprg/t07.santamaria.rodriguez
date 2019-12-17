nota=-1
nota_invalida=(nota < 0 or nota > 100)

while(nota_invalida):
    nota=int(input("Ingrese nota (0-100):"))
    nota_invalida=(nota < 0 or nota >100)
#finwhile
print("nota valida:",nota)
