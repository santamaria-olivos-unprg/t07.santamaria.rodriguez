# Si compra un celular Huawei en Ripley
# Si el celular es HUAWEI
# Si el celular es es LG
# Si el celular es SAMSUNG
# Mostras que tiene descuento
#DECLARACION
cliente,celular=" "," "

#INPUT
cliente=" "
celular=" "
celular_invalido=(celular!="HUAWEI" and celular!="SAMSUNG" and celular!="LG")

while(celular_invalido):
    cliente=input("Ingrese nombre de cliente: ")
    celular=input("Ingrese marca del celular: ")
    celular_invalido=(celular!="HUAWEI" and celular!="SAMSUNG" and celular!="LG")

#fin_while
print(cliente,"por tu compra tienes descuento")
