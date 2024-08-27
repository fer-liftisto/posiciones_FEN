# http://www.unicode.org/charts/PDF/U2600.pd #
# https: // youtu.be/Fo-jkW8rPs8 #
# https: // docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/widget-frame-marco/
############################

from tkinter import   Frame, Button, BooleanVar, StringVar, IntVar
from functools import partial
from configuracionTablero import *
from metePosicion import *

##############



############################

def tablero(app):	
	##############
	
	table = Frame(app)
	table.place(x=455,y=5)
	table.config(width=LADO*9, height=LADO*10,bd=10,bg='goldenrod2')
	
	quita = BooleanVar(value=True)
	
	pieza = StringVar()
	color = StringVar()
	
	grande = IntVar()
	grande.set(LADO//2)
	
	
	seleccion = StringVar()
	color_seleccion =StringVar()

	poner_pieza=BooleanVar()
	poner_pieza.set(False)
	
	def pieza_introduce():
		pieza = ''  # Para poder concatenar <pieza += pi>
		color=[]
		for pie in 'RNBQKPrnbqkp ':
			if pie.islower():
				col = True
			else:
				col = False	
			color.append(col)
			
			pi = traduce(idioma, pie)
			pieza += pi
		print(pieza)
		return pieza,color

	def introduce(menu_posicion, pon):
		seleccion.set(menu_posicion[pon].cget('text'))
		color_seleccion.set(menu_posicion[pon].cget('fg'))
		print(menu_posicion[pon].cget('fg'))
		poner_pieza.set(True)

		
	def piezas_mete_posicion():
		''' Genera el menu para meter posiciones '''
		poner_pieza.set(True) #x#
		
		piezas, color = pieza_introduce()
		
		global menu_posicion 
		menu_posicion = dict()
		
		if poner_pieza.get():#x#
			
			b = -1 
			n = -1
		
			for indice, pon in enumerate(piezas):
				
				if color[indice]:	
					b += 1
					valor = pon + str(indice)
					# crea las piezas para introducir
					menu_posicion[valor] = Button(table,
                                 text=pon,
                                 font=(LETRA, grande.get()),
                                    fg='blue',
                                 command= partial(introduce,
                                      menu_posicion, valor))
					
					menu_posicion[valor].place(x= b*LADO,
                              y=LADO*8,
                              width=LADO,
                              height=LADO)
				
				else:	
					n += 1
					valor = pon + str(indice)
					menu_posicion[valor] = Button(table,
                                    text=pon,
                                    font=(LETRA, grande.get()),
                                    fg='black',
                                    command= partial(introduce,
                                            menu_posicion, valor))

					menu_posicion[valor].place(x= n*LADO,
                                    y=LADO*9,
                                    width=LADO,
                                    height=LADO)
				
		
		
	def pieza_quita_posicion():
			poner_pieza.set(False)
			piezas, _ = pieza_introduce()
			for indice, pon in enumerate(piezas):
				valor = pon+str(indice)
				menu_posicion[valor].place_forget()
			
				#menu_posicion[valor].place_forget()
				######xxxxxxxx		
	###################################################################################
	###################################################################################
	def pieza_corona():
		pieza='' # Para poder concatenar <pieza += pi>
		for pie in 'RNBQ':
			pi = traduce(idioma,pie)
			pieza += pi
		return pieza
	
	def pieza_corona_peon():
		return traduce(idioma,'P')
	
	def promueve(menu_coronar, corona):
		pieza.set(menu_coronar[corona].cget('text'))
		# Para borrar las pizas de coronacion
		piezas = pieza_corona()

		for borra in piezas:
			# Borra las piezas para coronar
			menu_coronar[borra].place_forget()  # Para borrar el menu de coronacion
			#
	#######################################################################

	def mueve(cuadro, casilla):
		if not poner_pieza.get():
			
			if quita.get():
				quita.set(False)
				pieza.set(cuadro[casilla].cget('text'))
				color.set(cuadro[casilla].cget('fg'))
				# Cuadro viene de configuracionTablero
				cuadro[casilla].configure(text=' ')

				
			else:
				quita.set(True)
				cuadro[casilla].configure(text=pieza.get(),
										font=(LETRA, grande.get()),
										fg=color.get())
						
		############################################################
		##corona########
				if (casilla[1] == '1' or casilla[1] == '8') and (pieza.get() == pieza_corona_peon()) :
					menu_coronar = dict()
						
					piezas = pieza_corona() 
					
					for indice, corona in enumerate(piezas):
						## crea las piezas para coronar
						menu_coronar[corona] = Button(table,
													text=corona,
													font=(LETRA, grande.get()),
													fg=color.get(),
													command=partial(promueve,
																	menu_coronar, corona))
		
		##
						menu_coronar[corona].place(x=indice*LADO,
													y=LADO*8,
													width=LADO,
													height=LADO)

						## Coloca la pieza coronada
						cuadro[casilla].configure(text=pieza.get(),
												font=(LETRA, grande.get()),
												fg=color.get())
			
		if poner_pieza.get():
			
			''' Mete posiciones '''
			cuadro[casilla].configure(text=seleccion.get(),
                             font=(LETRA, grande.get()),
                             fg=color_seleccion.get())
			seleccion.set(' ')
			#poner_pieza.set(False)



	# ############################################################
		
	################################################################################################
	''' Cuerpo de la funcion tablero '''
	##TABLERO###################
	for f, fila in enumerate(FILAS):
		for c, colum in enumerate(COLUMNAS):
			casilla = (colum+fila)
			# viene de configuracion
			escaque.append(casilla)
			
			if (c+f) % 2 == 0:
				# cuadro viene de configuracionTablero
				cuadro[escaque[-1]] = Button(table,
										text = ' ',
										bg = COLOR_BLANCO,
										command = partial(mueve, cuadro, casilla)) # llama a mueve(cuadro,casilla)

				cuadro[escaque[-1]].place(
									x=(c)*LADO,
									y=(f)*LADO,
									width=LADO,
									height=LADO)

			else:
				cuadro[escaque[-1]] = Button(table,
										text = ' ',
										bg = COLOR_NEGRO,
                                    # llama a mueve(cuadro,casilla)
                                    command=partial(mueve, cuadro, casilla))

				cuadro[escaque[-1]].place(
									x=(c)*LADO,
									y=(f)*LADO, 
									width=LADO, 
									height=LADO)
	''' Boton para meter posiciones '''
	
	indice1 = 7
	mete_posicion = Button(table,
                        text='Editar',
                        bg='goldenrod2',
                        fg='red',
                        command= piezas_mete_posicion)
	##
	mete_posicion.place(x=indice1*LADO,
                     y=LADO*8,
                     width=LADO,
                     height=2 * LADO)

	indice1 = 8
	quita_posicion = Button(table,
                        text='Editar',
                        bg='goldenrod2',
                        fg='blue',
                        command= pieza_quita_posicion)
	##
	quita_posicion.place(x=indice1*LADO,
                     y=LADO*8,
                     width=LADO,
                     # Para los botones de meter posiciones ##########xxxxxxxxx
                     height=2 * LADO)
	###############################################################################

''' Mismo nivel que funcion tablero'''
# Obtiene la posicion a introducir en el tablero |||| esta fuera de funcion tablero
def introiduce_en_tablero(fen_posicion):	
	grande = IntVar()
	grande.set(LADO//2)
	tabli = posicion(fen_posicion) # del modulo metePosicion.py se llama a la funcion, posicion(fen_posicion)
	###Coloca Posicion################
	for f, fi in enumerate(FILAS):
		for c, co in enumerate(COLUMNAS):
				casilla = co + fi
				if tabli[f][c].islower():
					tabli[f][c] = traduce(idioma,tabli[f][c]) # Pone idioma de piezas
					cuadro[casilla].configure(text=tabli[f][c],
											font=(LETRA, grande.get()),
											fg=COLOR_PIEZA_NEGRA)
				else:
					tabli[f][c] = traduce(idioma,tabli[f][c])
					cuadro[casilla].configure(text=tabli[f][c],
											font=(LETRA, grande.get()),
											fg=COLOR_PIEZA_BLANCA)


''' trabajando '''
# def menu_mete_posicion():
# 	print("funcion menu_mete_posicion")
	
# 	menu_coronar = dict()
	
# 	grande = IntVar()
# 	grande.set(LADO//2)
	
# 	piezas = 'RNBQRP'

# 	for indice, corona in enumerate(piezas):
# 		# crea las piezas para coronar
# 		menu_coronar[corona] = Button(tablero.table,
#                                text= corona,
#                                font= (LETRA, tablero.grande.get()),
#                                fg= tablero.color.get(),
#                                )
# 	##
# 		menu_coronar[corona].place(x=indice*LADO,
#                             y=LADO*8,
#                             width=LADO,
#                             height=LADO)





'''
app = Tk()
app.geometry('1200x900+10+10')
tablero(app)
app.mainloop()
'''
