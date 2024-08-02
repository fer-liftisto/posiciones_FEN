
#  https://ajedrez.pro/notacion-fen #
#  https://youtu.be/vBSiz2yDDdE?si=XCLKPv5kiwqAsgkh #
#  https://youtu.be/cd6cA3ekm_E?si=eQ-tZvDzT2E6-IVl #
#  https://youtu.be/CLfmsn5yqQ0?si=kR75B85mK7HkBg-I #
#  https://recursospython.com/guias-y-manuales/lista-listbox-en-tkinter/ #

import tkinter as tk
from tkinter import messagebox
import tablero

def posicion_inicial():
    
    posicion= 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    posicion= posicion.split('/')
    
    lb.delete(0, tk.END) # para que quede bacio
    for index, fila in enumerate(posicion):
        lb.insert(index, fila)

def tablero_inicial():
    fen_posicion.set('N-N,_,rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR,_') # es una StringVar()
    tablero.introiduce_en_tablero(fen_posicion) # funcion del modulo tablero 

def borrar_tablero():
    fen_posicion.set('N-N,_,8/8/8/8/8/8/8/8,_') # es una StringVar()
    tablero.introiduce_en_tablero(fen_posicion)

##########################################################################################################
def borrar_posicion():
        lb.delete(0,tk.END)
        jugadores.set('')
        torneo.set('')
        parametros.set('')
        for i in range(8):
            lb.insert(i,'')
##########################################################################################################
def borrar_fila():
    index= lb.curselection() # devuelbe el indice seleccionado
    if not index:
        return
    else:
        lb.delete(index)
        lb.insert(index, ' ')

##########################################################################################################
def sustituir_fila():
    
    index= lb.curselection()
    if not index:
        return 
    else:
        lb.delete(index)
        lb.insert(index,fila.get())
        fila.set('')
##########################################################################################################
def anadir_FEN():
    FEN= list(lb.get(0, tk.END))
    FEN= '/'.join(FEN)
     
    if jugadores.get() == '':
        jugadores.set('N-N')
    if torneo.get() == '':
        torneo.set('_')
    if parametros.get() == '':
        parametros.set('_')
     
    FEN= f'{jugadores.get()},{torneo.get()},{FEN},{parametros.get()}'
    lb_fen.insert(tk.END,FEN)
     
    borrar_posicion()
     
     
    
def visualizar_FEN():
    index = lb_fen.curselection()
    if not index:
         return 
    else:
        partida= str(lb_fen.get(index))
        print(partida)
        nombre, torne, FEN, confi = partida.split(',')
        
        fen_posicion.set(partida) # Para pasarselo al tablero
        tablero.introiduce_en_tablero(fen_posicion) # funcion del modulo tablero
        
        jugadores.set(nombre)
        torneo.set(torne)
        parametros.set(confi)
        FEN= FEN.split('/')
        
        lb.delete(0, tk.END)  # para que quede bacio
        for index, fila in enumerate(FEN):
            lb.insert(index, fila)

def borrar_FEN():
    index= lb_fen.curselection()  # devuelbe el indice seleccionado
    if not index:
        return
    else:
        lb_fen.delete(index)
        
def guardar_FEN():
    with open('posiciones_FEN/posiciones_fen.txt', 'w') as fichero:
            
        partidas= lb_fen.get(0,tk.END)
        for elemento in partidas:
            fichero.writelines(elemento+'\n')
            print(elemento)
        lb_fen.delete(0, tk.END)
    
    messagebox.showinfo('GUARDAR FEN', message='Las posiciones han sido guardadas')

def cargar_FEN():
    with open('posiciones_FEN/posiciones_fen.txt', 'r') as fichero:

        partidas= fichero.read()
        partidas= partidas.split('\n')
        for partida in partidas:
            lb_fen.insert(tk.END,partida)

def pasar_derecha(): ########(pasarPosicion) ############
    FEN= list(lb.get(0, tk.END))
    posicion= '/'.join(FEN)
     
    if jugadores.get() == '':
        jugadores.set('N-N')
    if torneo.get() == '':
        torneo.set('_')
    if parametros.get() == '':
        parametros.set('_')
     
    FEN= f'{jugadores.get()},{torneo.get()},{posicion},{parametros.get()}'
    
    fen_posicion.set(FEN) # es una StringVar()
    tablero.introiduce_en_tablero(fen_posicion) # funcion del modulo tablero 

def pasar_izquierda():
    pass

def anadir_posicion():
    pass
###########################################################################################################
###  MAIN  ###
#######################################################################################################
v=tk.Tk()
v.geometry('1200x1000+15+15')
#img=tk.PhotoImage(file='CAMISETA.JPG')
v.title('VISOR FEN')
#v.iconbitmap('CAMISETA.ico')
v.config(bd= 10, bg= 'goldenrod3')
#########################################################################################################

jugadores= tk.StringVar()
torneo= tk.StringVar()
parametros= tk.StringVar()

fen_posicion= tk.StringVar()
#fen_posicion.set(f'{jugadores.get()},{torneo.get()},{FEN},{parametros.get()}')

fila= tk.StringVar()

##########################################################################################################
# para colocar el tablero
tablero.tablero(v)

##########################################################################################################
lba_partida=tk.Label(v, text= 'PARTIDA',bd=5, bg= 'goldenrod2')
lba_partida.place(x= 130,y= 30)

ent = tk.Entry(v, textvariable=jugadores, bd=5, bg='goldenrod2', width=26)
ent.place(x= 205, y= 30)

lba_torneo = tk.Label(v, text='TORNEO', bd=5, bg='goldenrod2')
lba_torneo.place(x=130, y=70)

ent_torneo = tk.Entry(v, textvariable=torneo, bd=5, bg='goldenrod2', width=26)
ent_torneo.place(x=205, y=70)
##########################################################################################################
lb = tk.Listbox(v, width= 15, height= 8, bd= 10, font= 'arial 20', bg= 'yellow')
lb.place(x= 130, y= 110)
##########################################################################################################
btn = tk.Button(v, text= ' >> ', bd= 5, bg= 'goldenrod2',width= 4, command= pasar_derecha)
btn.place(x= 395, y= 200)

btn = tk.Button(v, text= ' << ', bd= 5, bg= 'goldenrod2',width= 4, command= pasar_izquierda)
btn.place(x= 395, y= 300)
###########################################################################################################
lba_parametros = tk.Label(v, text= 'PARAMETROS', bd= 5, bg= 'goldenrod2', width= 11)
lba_parametros.place(x=130, y=410)

ent_parametros = tk.Entry(v, textvariable= parametros,bd= 5, bg='goldenrod2', width= 24)
ent_parametros.place(x= 225, y= 410)
##########################################################################################################
#########################################################################################################
btn = tk.Button(v, text= 'POSICION INICIAL', bd= 5, bg= 'goldenrod2',width= 15, command= posicion_inicial)
btn.place(x= 3, y= 110)

btn1 = tk.Button(v, text= 'BORRAR POSICION ', bd= 5, bg= 'goldenrod2',width= 15, command= borrar_posicion)
btn1.place(x= 3, y= 150)

btn2 = tk.Button(v, text='BORRAR FILA ', bd= 5, bg='goldenrod2',width= 15, command=borrar_fila)
btn2.place(x= 3, y= 235)
##########################################################################################################
ent=tk.Entry(v, textvariable= fila, bd= 5, bg= 'goldenrod2', width= 18)
ent.place(x= 3, y= 320)

btn3 = tk.Button(v, text= 'INSERTAR FILA ',bd=5, bg= 'goldenrod2',width=15, command= sustituir_fila)
btn3.place(x= 3, y= 360)
######################################################################################################
##########################################################################################################
btn_mostrar= tk.Button(v, text= 'Añadir FEN ',
                        bd=5, bg= 'goldenrod2',width= 15, command= anadir_FEN)
btn_mostrar.place(x= 130, y= 615)

btn_visualizar = tk.Button(v, text= 'Visualizar FEN ',
                           bd=5, bg= 'goldenrod2', width= 15, command= visualizar_FEN)
btn_visualizar.place(x= 260, y= 615)

btn_borrar = tk.Button(v, text= 'Borrar FEN ', bd= 5,
                       bg= 'goldenrod2', width= 15, command= borrar_FEN)
btn_borrar.place(x= 1000, y= 810)

btn_mostrar= tk.Button(v, text= 'Añadir Posicion ',
                        bd=5, bg= 'goldenrod2',width= 15, command= anadir_posicion)
btn_mostrar.place(x= 650, y= 615)

####################################################################################################
btn_guardar = tk.Button(v, text='Guardar FEN ', bd= 5,
                       bg= 'goldenrod2', width= 15, command= guardar_FEN)
btn_guardar.place(x= 130, y= 470)

btn_cargar = tk.Button(v, text= 'Cargar FEN ', bd= 5,
                        bg= 'goldenrod2', width= 15, command= cargar_FEN)
btn_cargar.place(x= 260, y= 470)
##################################################################################################
lb_fen = tk.Listbox(v, width= 85, height= 12, bd= 10,
                    font= 'arial 15', bg= 'yellow')
lb_fen.place(x= 30, y= 660)
##########################################################################################################
btn = tk.Button(v, text= 'TABLERO INICIAL ', bd= 5, bg= 'goldenrod2',width= 15, command= tablero_inicial)
btn.place(x= 1030, y= 110)

btn1 = tk.Button(v, text= 'BORRAR TABLERO', bd= 5, bg= 'goldenrod2',width= 15, command= borrar_tablero)
btn1.place(x= 1030, y= 150)
##############################################################################################################
v.mainloop()
# tablero inicial echo acer commit y merge con master