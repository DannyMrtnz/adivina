numero = 26
usuario = 0
while usuario != numero:
	usuario = int(input("cual es el número?"))
	if usuario > numero:
		print("Digita un número menor")
	elif usuario < numero:
		print("Digita un número mayor")
	else:
		print("correto")