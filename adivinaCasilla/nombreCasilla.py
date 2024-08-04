
#Fer##
##########################
def tablero(table,LADO):
    # Costantes
    COLUMNAS='abcdefgh'
    FILAS = '87654321'
    COLOR_BLANCO='blue'
    COLOR_NEGRO='green'

    # Variables de intercambio
    acierto=IntVar(value=0)
    color=StringVar()
    ale=StringVar()
    pulsada=StringVar()

    # Tablero
    cuadro=dict()

    ##########################
    def aleatorio(table,LADO):
        # Genera casilla aleatoria
        c= choice('abcdefgh')
        f= choice('87654321')
        ale.set(c+f)

        # Muestra la casilla Aleatoria
        Label(table,text=ale.get(),font=('Helvetica',int(LADO*0.148148148)),borderwidth=6,relief='sunken').place(x= 6*LADO, y=1* LADO, width=LADO, height=LADO)
        #
        Label(table,text='Pulsa en =>',font=('Helvetica',int(LADO*0.148148148)),borderwidth=6,relief='sunken').place(x= 1*LADO, y=1* LADO, width=LADO*5, height=LADO)

    ##########################
    def seleccion(casilla):
        pulsada.set(casilla)

        if pulsada.get() == ale.get():

            # Llama a la función aleatorio
            aleatorio(table,LADO)
            # Incrementa la variable acierto
            acierto.set(acierto.get()+1)

            # Muestra: Número de aciertos'
            Label(table,text=acierto.get(),font=('Helvetica',int(LADO*0.148148148)),borderwidth=6,relief='sunken').place(x= 6*LADO, y= 10*LADO,width=LADO, height=LADO,)
            #
            Label(table,text='Aciertos =>',font=('Helvetica',int(LADO*0.148148148)),borderwidth=6,relief='sunken').place(x= 1*LADO, y= 10*LADO, width=5*LADO, height=LADO)

            # Muestra casilla acertada
            color.set('black')
            Label(table,text=pulsada.get(),font=('Helvetica',int(LADO*0.148148148)),fg=color.get(),borderwidth=6,relief='sunken').place(x= 6*LADO, y= 11*LADO, width=LADO, height=LADO)
            #
            Label(table,text='Pulsaste =>',font=('Helvetica',int(LADO*0.148148148)),fg=color.get(),borderwidth=6,relief='sunken').place(x= 1*LADO, y= 11*LADO, width=5*LADO, height=LADO)

        else:
            # Muestra casillas no acertadas
            color.set('red')
            Label(table,text=pulsada.get(),font=('Helvetica',int(LADO*0.148148148)),fg=color.get(),borderwidth=6,relief='sunken').place(x= 6*LADO, y= 11*LADO, width=LADO, height=LADO)
            #
            Label(table,text='Pulsaste =>',font=('Helvetica',int(LADO*0.148148148)),fg=color.get(),borderwidth=6,relief='sunken').place(x= 1*LADO, y= 11*LADO, width=5*LADO, height=LADO)

    ##Genera primera casilla aleatoria#
    aleatorio(table,LADO)

    ##TABLERO###############
    for c , colum in enumerate(COLUMNAS):
        for f , fila in enumerate(FILAS):
            # Genera el nombre de las
            # casillas
            casilla=(colum+fila)
            ##################
            if (c+f) % 2 == 0:
                # Genera los cuadros blancos
                cuadro[casilla]=Button(table,text=' ' , bg=COLOR_BLANCO,command=partial(seleccion,casilla) )
                #
                cuadro[casilla].place(x= c*LADO, y= (f+2)*LADO, width=LADO, height=LADO)
                ##################
            else:
                # Genera los cuadros negros
                cuadro[casilla]=Button(table, text=' ', bg=COLOR_NEGRO,command=partial(seleccion,casilla) )
                #
                cuadro[casilla].place(x= c*LADO, y=(f+2)*LADO, width=LADO,height=LADO)

    #########################

    #########################
# Para modularizar
if __name__ == '__main__':
    # Modulos
    from tkinter import *
    from functools import partial
    from random import choice
    
    # Objeto
    table = Tk()
    table.geometry('700x1000+15+15')
    #img=tk.PhotoImage(file='CAMISETA.JPG')
    table.title('ADIVINA CASILLA')
    #v.iconbitmap('CAMISETA.ico')
    table.config(bd= 10, bg= 'goldenrod3')
    ####################################
    
    # Dimensión del cuadro
    LADO=80
    # Función Tablero
    tablero(table,LADO)
    # bucle de la ventana   
    table.mainloop()
    ######################### 
