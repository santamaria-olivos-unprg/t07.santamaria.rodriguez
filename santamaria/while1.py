#Dado el promedio obtenido en 5to de secundaria
# Si su promedio es mayor o igual a 16
# Mostrar: SE GANO UNA BECA !!
#DECLARACION
alumno,promedio_final="",0

#INPUT
promedio_final=10
promedio_invalido=(promedio_final<16 or promedio_final>20)

while(promedio_invalido):
    alumno=input("Ingrese nombre del alumno: ")
    promedio_final=int(input("Ingrese promedio: "))
    promedio_invalido=(promedio_final<16 or promedio_final>20)

#fin_while
print("El alumno ",alumno,"obtuvo",promedio_final,"de promedio")
print("SE GANO UNA BECA!!!")
