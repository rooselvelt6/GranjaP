pollos = [

		   2.0,2.6,2.2,2.2,2.1,
		   1.8,2.4,2.2,2.3,2.5,
		   2.6,2.6,2.5,2.4,2.4,
		   2.4,2.4,2.3,2.3,2.3,
		   2.4,2.1,2.1,2.1,2.1,
		   2.1,2.5,2.3,2.6,2.1,
		   2.4,2.3,2.1,2.3,2.1,
		   2.2,2.2,2.3,2.3,2.3,
		   2.3,2.3,2.0,2.0,2.0, 
		   2.0,2.0,2.0,2.0,2.0,
		   2.0,2.0,2.0,2.0,2.0,
		   2.0,2.0,2.0,2.0,2.0,

]


lista_temporal = []

print("Cantidad de pollos criados:", len(pollos))
suma = 0
for x in pollos:
	suma += x
print("Cantidad de kilos de pollos obtenidos en la crianza:", suma, "Kg")
print("Retorno de inversiòn bruta:","Bolivares:", suma*15000, "==",suma * 15000 / 4440, "$")


pagos = [2.0, 2.3, 2.4,2.4,2.3,2.6,2.6,2.5,2.4,2.4,2.0,2.3,2.1,2.1,2.3,2.3,2.2,2.5,2.4,2.2]
pendientes = [1.8,2.1,2.3,2.1,2.1,2.4,2.3,2.3,2.0]

capital = pagos + pendientes
print("*******************************************************************************************")
print("Totalidad de pollos vendidos:", len(capital))
print("ROOSELVELT: CONSUMO PERSONAL PENDIENTE POR PAGAR:", len(pendientes),"pollos", sum(pendientes), "Kg", sum(pendientes)*15000/4400, "USD", sum(pendientes)*15000, "BS")
print("VENTAS EN CARIPE:", len(pagos), "pollos")
cancelados = 0
for x in pagos:
	cancelados += x
print("Total de kg cancelados:", cancelados, "Kg", cancelados*15000/4400, "USD")
print("*******************************************************************************************")
print("Quedan por vender:", len(pollos)-len(capital), "pollos")

