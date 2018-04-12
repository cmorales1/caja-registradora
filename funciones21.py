#!usr/bin/env python
#-*- coding: utf-8 -*- 

#conding-----------
import os
import time
#operative system
#cls windows
# linux, MacOS
productos = {}
codigoproductos = {}
def menu():	
	a=True
	while a==True:
		os.system("cls")
		print "---------Caja Registradora -----------"
		print "-----1. ingresa tus productos"
		print "-----2. comprar"

			 



	#si ingresa a la opcion invalida que regrese al menu y si esta bien que continue con el procedimiento

		Noopcion = raw_input("ingrese numero de opcion")
		if Noopcion == "1":
			os.system("cls")
			print "seleccionaste ingresa tus productos"
			a=False		
			productos1()
		elif Noopcion == "2":
			os.system("cls")
			print "seleccionaste comprar"
			a=False
			comprar()

		#elif Noopcion =="3":
		#	os.system("cls")
			#print "seleccionaste elige tus productos"
			#a=False
			#productos()
		
		else:
			print "opcion invalida"
			time.sleep(2)


			#------------------------------------Tarea----------------------------------
#refactorizar o reducir el codigo a que cuando meta 2 numeros automaticamente se operen  			

def productos1():
	validar1 = True
	while validar1 == True:
		opcion = raw_input("desea ingresar un producto SI/NO:")
		try:
			if opcion.isalpha()==True:
				if opcion.lower()=="si":
					nameProduct = raw_input("Ingrese nombre del producto: ")
					codigopro = raw_input("ingrese el codigo de su producto:")
					precioProducto = input("Precio:")
					productos[nameProduct]=precioProducto
					codigoproductos[codigopro,nameProduct]=precioProducto
			  	

				elif opcion.lower()=="no":
					validar1=False
					os.system('')

				else:
					print u"Lo sentimos, opciones válidas 'si/no'; intentelo nuevamente"
			else:
				print u"Lo sentimos, no acepta números"
		except:
			validar1=True
	for i in productos:
		print i,"Q",productos[i]
	for a in codigoproductos:
		print a,codigoproductos[a] 	
		
	time.sleep(2)		

	menu()	

def comprar():
	
	for x in codigoproductos:
		print x[0] 

	print "Agregue productos a su carrito:"
	os.system("cls")
	subtotal=0
	if len (codigoproductos)>0:
		validar2 = True
		while validar2 == True:
			for i in productos:
				print "productos disponibles", codigoproductos
			

				codigopro = raw_input("ingrese el codigo del producto")
				for elemento in codigoproductos:
					if elemento[0] == codigopro:
						
						cantidad = input ("cantidad unitaria a comprar:")
						sb=cantidad*codigoproductos[elemento]
						# ASIGNACION DE VARIABLES (CONTADOR MAS SB), VARIABLE GLOBAL
						subtotal = subtotal + sb
						print "*****%s Cant: %s Subtotal: Q.%s "%(elemento, cantidad,subtotal)
						print " "
						value3=True
						# ELECCION DE PRODUCTO NUEVAMENTE.................................
						while value3==True:
							seguir=raw_input("desea elegir otro articulo SI/NO: ")
							print " "
							if seguir.lower()=="si":
								os.system('cls')
								validar2=True
								value3=False
							elif seguir.lower()=="no":
								validar2 = False
								value3 = False
								os.system('cls')
							else:
								print "opcion invalida"
								value3=True
		else:
			factura(subtotal)
	else:
		print "¿¡Qué!, ya se va?, no ha comprado nada aún, talvés es porque el Gerente no ha comprado productos para la tienda. "



def factura(compragen):
	validar2=True
	cliente=raw_input("nombre del comprador: ")
	nit=raw_input("ingrese nit: ")
	print "posee alguna de las siguientes tarjetas: "
	print "---premia gold---"
	print "---premia silver---"
	print "preione cualquier tecla si no posee ninguna de las anteriores"
	while validar2==True:
		tarcliente=raw_input("Posee tarjeta de Miembro? ¿Cuál?: ")
		print " "
		# TARJETA GOLD Y PROCEDIMIENTO....................................................
		if tarcliente.lower()=="premia gold":
			print "El Sr.(a): " + cliente +" posee tarjeta tipo: "+ tarcliente+ " por lo cual obtiene el 5%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			descuento = (compragen*0.05)
			totalcompra = compragen + iva - descuento
			print " "
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			print "__________________________"
			print " "
			efectivo = input("Cantidad de Pago en Efectivo: ")
			os.system('clear')
			print " "
			cambio = efectivo - compragen
			print "__________________________"
			print "__________________________"
			print " "
			print "NOMBRE: %s"%(cliente)
			print "NIT: %s"%(nit)
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
		# TARJETA SILVER Y PROCEDIMIENTO..................................................
		elif tarcliente.lower()=="premia silver":
			print "El Sr.(a): " + cliente +" posee tarjeta tipo: "+ tarcliente+ " por lo cual obtiene el 2%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			descuento = (compragen*0.02)
			totalcompra = compragen + iva - descuento
			print " "
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			print "__________________________"
			print " "
			efectivo = input("Cantidad de Pago en Efectivo: ")
			os.system('clear')
			print " "
			cambio = efectivo - compragen
			print "__________________________"
			print "__________________________"
			print " "
			print "NOMBRE: %s"%(cliente)
			print "NIT: %s"%(nit)
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
		# NINGUNA TARJETA Y PROCEDIMIENTO
		else:
			print "El Sr.(a): " + cliente +" no posee tarjeta de ningún tipo por lo que no obtiene el 5%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			totalcompra = compragen + iva
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			efectivo = input("Efectivo: ")
			cambio = efectivo - compragen
			print cliente
			print nit
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
	print"Vuelva Pronto!"




	
		
	



	


	 	



		
# tarea ----------------ciclo while---------------------------	
	

#.lower para que todo se convierta a minuscula

#.upper se convierte todo a mayuscula




menu()
