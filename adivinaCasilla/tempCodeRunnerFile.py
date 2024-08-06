    def aleatorio(table,LADO):
        # Genera casilla aleatoria
        c=choice('abcdefgh')
        f=choice('87654321')
        ale.set(c+f)

        # Muestra la casilla Aleatoria
        Label(table,text=ale.get(),font=('Helvetica',int(LADO*0.148148148)),borderwidth=6,relief='sunken').place(x= 6*LADO, y=1* LADO, width=LADO, height=LADO)
        #
        Label(table,text='Pulsa en =>',font=('Helvetica',int(LADO*0.148148148)),borderwidth=6,relief='sunken').place(x= 1*LADO, y=1* LADO, width=LADO*5, height=LADO)

    ##########################
    def seleccion(casilla):
        pulsada.set(casilla)

        if pulsada.get()==ale.get():

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