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
	table.place(x=455,y=15)
	table.config(width=LADO*8, height=LADO*9,bd=10,bg='goldenrod2')
	
	
	quita = BooleanVar(value=True)
	
	pieza = StringVar()
	color = StringVar()
	
	grande = IntVar()
	grande.set(LADO//2)
	def promueve(menu_coronar, corona):
		pieza.set(menu_coronar[corona].cget('text'))
		# Para borrar las pizas de coronacion
		piezas = '♜♞♝♛'
		for corona in piezas:
			# Borra las piezas para coronar
			menu_coronar[corona].place_forget()
			#
	#######################################################################


	def mueve(cuadro, casilla):

		if quita.get():
			quita.set(False)
			pieza.set(cuadro[casilla].cget('text'))
			color.set(cuadro[casilla].cget('fg'))
			cuadro[casilla].configure(text=' ')

		else:
			quita.set(True)
			cuadro[casilla].configure(text=pieza.get(),
									font=(LETRA, grande.get()),
									fg=color.get())
	############################################################
	##corona########
			if (casilla[1] == '1' or casilla[1] == '8') and pieza.get() == PEON:
				menu_coronar = dict()
				piezas = '♜♞♝♛'
				for indice, corona in enumerate(piezas):
					##
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
			
	################################################################################################
	##TABLERO###################
	for f, fila in enumerate(FILAS):
		for c, colum in enumerate(COLUMNAS):
			casilla = (colum+fila)

			if (c+f) % 2 == 0:
				cuadro[casilla] = Button(table,
					text = ' ',
					bg = COLOR_BLANCO,
					command = partial(mueve, cuadro, casilla)) # mueve(cuadro,casilla)

				cuadro[casilla].place(
									x=(c)*LADO,
									y=(f)*LADO,
									width=LADO,
									height=LADO)

			else:
				cuadro[casilla] = Button(table,
										text = ' ',
										bg = COLOR_NEGRO,
										command = partial(mueve, cuadro, casilla))

				cuadro[casilla].place(
									x=(c)*LADO,
									y=(f)*LADO, 
									width=LADO, 
									height=LADO)

	###############################################################################
# Obtiene la posicion a introducir en el tablero
def introiduce_en_tablero(fen_posicion):	
	grande = IntVar()
	grande.set(LADO//2)
	tabli = posicion(fen_posicion) # del modulo metePosicion.py se llama a la funcion, posicion(fen_posicion)
	###Coloca Posicion################
	for f, fi in enumerate(FILAS):
		for c, co in enumerate(COLUMNAS):
				casilla = co + fi
				if tabli[f][c].islower():
					tabli[f][c] = traduce(tabli[f][c])
					cuadro[casilla].configure(text=tabli[f][c],
											font=(LETRA, grande.get()),
											fg=COLOR_PIEZA_NEGRA)
				else:
					tabli[f][c] = traduce(tabli[f][c])
					cuadro[casilla].configure(text=tabli[f][c],
											font=(LETRA, grande.get()),
											fg=COLOR_PIEZA_BLANCA)
'''
app = Tk()
app.geometry('1200x900+10+10')
tablero(app)
app.mainloop()
'''
