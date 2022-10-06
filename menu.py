import os
import actualizar
 
def menu():
	"""
	Limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # para windows clear por cls, Mac clear
	print ("Selecciona una opción")
	print ("\t1 - Actualizacion de datos")
	print ("\t2 - Visualizacion de datos")
	print ("\t3 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicitamos una opción al usuario
	opcionMenu = input("Ingresa un numero >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")