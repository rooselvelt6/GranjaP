import animal

print("*******************************")
print("(1) Animales                  *")
print("(2) Alimentos                 *")
print("(3) Corrales                  *")
print("(4) Herramientas              *")
print("(5) Reporte General           *")
print("(6) Inversión                 *")
print("*******************************")
opcion = int(input("Opción:"))
if(opcion == 1):
    # Lote == 0 mientras ventas.productos no este completada
    # vender productos cuando finalice las ventas aumenta el lote
    animal = animal.Animal("1","Carne","Primera", 70, 1)
    #animal.sacrificar()
    animal.obtenerInforme()

elif(opcion == 2):
    pass
else:
    print("Opciòn Invalida ")
