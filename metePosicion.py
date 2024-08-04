'''
https: // enriquelazcorreta.gitbooks.io/tkinter/content/creando-la-interfaz-grafica-de-usuario-gui/texto-index-tag-y-mark.html
'''
#from configuracion import *
import tkinter.ttk as ttk
from configuracionTablero import *



###################################################################
def posicion(fen_posicion):
    '''
    Realza la combersion de FEN a una matriz de 8 x 8
    '''
    #FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - 0 1'
    partida= fen_posicion.get() # es una StringVar
    
    
    print(partida)
    def devuelve_posicion(partida):
            nombre, torne, FEN, confi = partida.split(',')
            filas = FEN.split('/')
            return filas
        ############################
    fila = devuelve_posicion(partida)
        #####################################################################

    def devuelve_fila(fila):
        tabli = []
        for f in fila:
            fil = ' '*8
            fil = list(fil)
            con = -1
            for elemento in f:
                if elemento.isnumeric():
                     con += int(elemento)
                else:
                    con += 1
                    fil[con] = elemento
            tabli.append(fil)
        return tabli

    ##############################
    tabli = devuelve_fila(fila)
    ###########################################################################
    for fila in tabli:
        print(fila)
    return tabli

def tablero_A_fen():
     pass

def traduce(f):
    # '♟♜♞♝♛♚' #
    f = f.replace('R', '♜')
    f = f.replace('N', '♞')
    f = f.replace('B', '♝')
    f = f.replace('Q', '♛')
    f = f.replace('K', '♚')
    f = f.replace('P', '♟')

    f = f.replace('r', '♜')
    f = f.replace('n', '♞')
    f = f.replace('b', '♝')
    f = f.replace('q', '♛')
    f = f.replace('k', '♚')
    f = f.replace('p', '♟')
    return f


