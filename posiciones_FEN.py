
#  https://ajedrez.pro/notacion-fen #
#  https://youtu.be/vBSiz2yDDdE?si=XCLKPv5kiwqAsgkh #
#  https://youtu.be/cd6cA3ekm_E?si=eQ-tZvDzT2E6-IVl #
#  https://youtu.be/CLfmsn5yqQ0?si=kR75B85mK7HkBg-I #
#  https://recursospython.com/guias-y-manuales/lista-listbox-en-tkinter/ #

import tkinter as tk
from tkinter import messagebox
import tablero
import configuracionTablero as confiT
import metePosicion
from functools import partial
import os

def borrar_metadatos():
    jugadores.set('')
    torneo.set('')
    parametros.set('')

def posicion_inicial():
    borrar_metadatos()
    posicion= 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    posicion= posicion.split('/')
    print(posicion)
    lb_fen.delete(0, tk.END) # para que quede bacio
    for index, fila in enumerate(posicion):
        lb_fen.insert(index, fila)

def tablero_inicial():
    borrar_metadatos()
    fen_posicion.set('N-N,_,rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR,_') # es una StringVar()
    tablero.introiduce_en_tablero(fen_posicion) # funcion del modulo tablero 

def borrar_tablero():
    fen_posicion.set('N-N,_,8/8/8/8/8/8/8/8,_') # es una StringVar()
    tablero.introiduce_en_tablero(fen_posicion)

##########################################################################################################
def borrar_posicion():
        lb_fen.delete(0,tk.END)
        jugadores.set('')
        torneo.set('')
        parametros.set('')
        for i in range(8):
            lb_fen.insert(i,'')
##########################################################################################################
def borrar_fila():
    index= lb_fen.curselection() # devuelbe el indice seleccionado
    if not index:
        return
    else:
        lb_fen.delete(index)
        lb_fen.insert(index, ' ')

##########################################################################################################
def sustituir_fila():
    
    index= lb_fen.curselection()
    if not index:
        return 
    else:
        lb_fen.delete(index)
        lb_fen.insert(index,fila.get())
        fila.set('')

##########################################################################################################
def anadir_FEN():
    FEN= list(lb_fen.get(0, tk.END))
    FEN= '/'.join(FEN)
     
    if jugadores.get() == '':
        jugadores.set('N-N')
    if torneo.get() == '':
        torneo.set('_')
    if parametros.get() == '':
        parametros.set('_')
     
    FEN= f'{jugadores.get()},{torneo.get()},{FEN},{parametros.get()}'
    lb_fichero.insert(tk.END,FEN)
     
    borrar_posicion()
        
def visualizar_FEN():
    index = lb_fichero.curselection()
    if not index:
         return 
    else:
        partida= str(lb_fichero.get(index))
        print(partida)
        nombre, torne, FEN, confi = partida.split(',')
        
        fen_posicion.set(partida) # Para pasarselo al tablero
        tablero.introiduce_en_tablero(fen_posicion) # funcion del modulo tablero
        
        jugadores.set(nombre)
        torneo.set(torne)
        parametros.set(confi)
        FEN= FEN.split('/')
        
        lb_fen.delete(0, tk.END)  # para que quede bacio
        for index, fila in enumerate(FEN):
            lb_fen.insert(index, fila)

def borrar_FEN():
    index= lb_fichero.curselection()  # devuelbe el indice seleccionado
    if not index:
        return
    else:
        lb_fichero.delete(index)
        
def guardar_FEN():
    if '.txt' in guardar.get(): 
        try :
            with open(guardar.get(), 'w') as fichero:
            
                partidas= lb_fichero.get(0,tk.END)
                for elemento in partidas:
                    fichero.writelines(elemento+'\n')
                lb_fichero.delete(0, tk.END)
    
            messagebox.showinfo('GUARDAR FEN', message='Las posiciones han sido guardadas')
        except:
            messagebox.showinfo(
                'GUARDAR FEN', message='Las posiciones no han sido guardadas')
    else:
        pass

def cargar_FEN():
    # carga lista de ficheros
    fichero_txt = [fichero for fichero in os.listdir() if 'txt' in fichero]
    for archivo in fichero_txt:
        lb_archivo.insert(tk.END,archivo)
    
    # selecciona el fichero
    lb_fichero.delete(0, tk.END)
    index = lb_archivo.curselection()
    if not index:
        return
    else:
        fichero = str(lb_archivo.get(index))
    lb_archivo.delete(0, tk.END)
    
    # abre fichero seleccionado
    with open(fichero, 'r') as fichero:

        partidas= fichero.read()
        lista_partidas= partidas.split('\n') # combierte a lista
        lista_partidas= lista_partidas[:-1]
        print(lista_partidas)
        for partida in lista_partidas:
            lb_fichero.insert(tk.END,partida)

def pasar_derecha():
    FEN= list(lb_fen.get(0, tk.END))
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
    ''' Pasa de posicion tablero a posicion FEN'''
    
    tabli= [] 
    for v in tablero.cuadro.values():
        contenido= v.cget('text'),v.cget('fg') # Es una tupla
    
        tabli.append(metePosicion.traduce_ing(
            # confiT apodo de configuracionTablero
            confiT.idioma, contenido))
      
    table= metePosicion.tablero_A_fen(tabli)       
    posicion = table
    posicion = posicion.split('/')
    print(posicion)
    lb_fen.delete(0, tk.END)  # para que quede bacio
    for index, fila in enumerate(posicion):
        lb_fen.insert(index, fila)

###########################################################################################################
###  MAIN  ###
#######################################################################################################
v= tk.Tk()
v.geometry('1200x1000+15+15')
#img=tk.PhotoImage(file='CAMISETA.JPG')
v.title('VISOR FEN')
#v.iconbitmap('CAMISETA.ico')
v.config(bd= 10, bg= 'goldenrod3')
#########################################################################################################

jugadores= tk.StringVar()
torneo= tk.StringVar()
parametros= tk.StringVar()
guardar= tk.StringVar()

fen_posicion= tk.StringVar()
#fen_posicion.set(f'{jugadores.get()},{torneo.get()},{FEN},{parametros.get()}')

fila= tk.StringVar()

pieza = tk.StringVar()

color = tk.StringVar()
color.set('#dfc07f')



##########################################################################################################
# para colocar el tablero
tablero.tablero(v)

##########################################################################################################
lbl_partida=tk.Label(v, text= 'PARTIDA',bd=5, bg= 'goldenrod2')
lbl_partida.place(x= 130,y= 30)

ent_partida = tk.Entry(v, textvariable=jugadores, bd=5, bg='goldenrod2', width=26)
ent_partida.place(x= 205, y= 30)

lbl_torneo = tk.Label(v, text='TORNEO', bd=5, bg='goldenrod2')
lbl_torneo.place(x=130, y=70)

ent_torneo = tk.Entry(v, textvariable=torneo, bd=5, bg='goldenrod2', width=26)
ent_torneo.place(x=205, y=70)
##########################################################################################################
lb_fen = tk.Listbox(v, width= 15, height= 8, bd= 10, font= 'arial 20', bg= 'yellow')
lb_fen.place(x= 130, y= 110)
##########################################################################################################
btn_pasar_a_tablero = tk.Button(v, text= ' >> ', bd= 5, bg= 'goldenrod2',width= 4, command= pasar_derecha)
btn_pasar_a_tablero.place(x= 395, y= 200) 

btn_pasar_a_fen = tk.Button(v, text= ' << ', bd= 5, bg= 'goldenrod2',width= 4, command= pasar_izquierda)
btn_pasar_a_fen.place(x= 395, y= 300) 
###########################################################################################################
lbl_parametros = tk.Label(v, text= 'PARAMETROS', bd= 5, bg= 'goldenrod2', width= 11)
lbl_parametros.place(x=130, y=410)

ent_parametros = tk.Entry(v, textvariable= parametros,bd= 5, bg='goldenrod2', width= 24)
ent_parametros.place(x= 225, y= 410)
##########################################################################################################
#########################################################################################################
btn_posicion_inicial = tk.Button(v, text= 'POSICION INICIAL', bd= 5, bg= 'goldenrod2',width= 15, command= posicion_inicial)
btn_posicion_inicial.place(x= 3, y= 110)

btn_borrar_posicion = tk.Button(v, text= 'BORRAR POSICION ', bd= 5, bg= 'goldenrod2',width= 15, command= borrar_posicion)
btn_borrar_posicion.place(x= 3, y= 150)

btn_borrar_fila = tk.Button(v, text='BORRAR FILA ', bd= 5, bg='goldenrod2',width= 15, command=borrar_fila)
btn_borrar_fila.place(x= 3, y= 235)
##########################################################################################################
ent_sustituir_fila=tk.Entry(v, textvariable= fila, bd= 5, bg= 'goldenrod2', width= 18)
ent_sustituir_fila.place(x= 3, y= 320)

btn_sustituir_fila = tk.Button(v, text= 'INSERTAR FILA ',bd=5, bg= 'goldenrod2',width=15, command= sustituir_fila)
btn_sustituir_fila.place(x= 3, y= 360)
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

####################################################################################################
############################# FICHEROS #############################################################
btn_guardar = tk.Button(v, text='Guardar FEN ', bd= 5,
                       bg= 'goldenrod2', width= 15, command= guardar_FEN)
btn_guardar.place(x= 3, y= 460)
#####
ent_guardar = tk.Entry(v, textvariable=guardar,
                        bd=5, bg='goldenrod2', width=24)
ent_guardar.place(x=130, y=460)
#############
btn_cargar = tk.Button(v, text= 'Cargar FEN ', bd= 5,
                        bg= 'goldenrod2', width= 15, command= cargar_FEN)
btn_cargar.place(x= 3, y= 510)
#####
lb_archivo = tk.Listbox(v, width=20, height=3, bd=10, # lista de archivos txt con posiciones fen
                        font='arial 15', bg='yellow')
lb_archivo.place(x=130, y=510)

##################################################################################################
lb_fichero = tk.Listbox(v, width= 85, height= 12, bd= 10,
                    font= 'arial 15', bg= 'yellow')
lb_fichero.place(x= 30, y= 660)
##########################################################################################################
btn_tablero_inicial = tk.Button(v, text= 'TABLERO INICIAL ', bd= 5, bg= 'goldenrod2',width= 15, command= tablero_inicial)
btn_tablero_inicial.place(x= 1030, y= 110)

btn_borrar_tablero = tk.Button(v, text= 'BORRAR TABLERO', bd= 5, bg= 'goldenrod2',width= 15, command= borrar_tablero)
btn_borrar_tablero.place(x= 1030, y= 150)
##############################################################################################################
v.mainloop()

