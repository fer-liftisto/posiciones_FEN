'''
https: // enriquelazcorreta.gitbooks.io/tkinter/content/creando-la-interfaz-grafica-de-usuario-gui/texto-index-tag-y-mark.html
'''
#from configuracion import *
import tkinter.ttk as ttk
from configuracionTablero import *



###################################################################
def posicion(fen_posicion):
    '''
    Realiza la combersion de FEN a una matriz de 8 x 8
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
    # Es para visualizar tablero
    # for fila in tabli:
    #     print(fila)
    
    return tabli # es una lista de listas

def tablero_A_fen(contenido):
    def fen_fila(fila):
        fila= ''.join(fila) # covierte en string
        con= 0 # Contador de espacios
        fen= '' # posición FEN
        for i, v in enumerate(fila):
                if v == ' ':
                    con += 1
                    
                    try:
                        if fila[i+1] != ' ':
                            fen += str(con)
                    except:
                        fen += str(con)
                        
                elif v != ' ':
                    fen += v
                    con = 0

        return fen


    def tablero_fen(table):	
        inicio = 0 # indice del slice
        fin = 8
        fen = ''
        for i in range(0,64,8):
            ''' 
            Para coger filas de 8 elementos 
            '''
            inicio = i   # Para manejar el slice
            fin = i + 8  # Para manejar el slice
            aux = table[inicio:fin] # Toma 8 elementos

            fen += fen_fila(aux) + '/' # muestra la posicion fen
        return fen[:-1] # quita el ultimo /
    
    return tablero_fen(contenido)


def traduce_replace(f):
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

def traduce(idioma,pieza):
    
    if idioma == 'sn' : 
        a_sinbolo= {'R': '♜',
                    'N': '♞',
                    'B': '♝',
                    'Q': '♛',
                    'K': '♚',
                    'P': '♟',

                    'r': '♜',
                    'n': '♞',
                    'b': '♝',
                    'q': '♛',
                    'k': '♚',
                    'p': '♟',
                    ' ': ' '}
    
        return  a_sinbolo[pieza]
    
    elif idioma == 'sp' :
        
        a_sp=  {    'R': 'T',
                    'N': 'C',
                    'B': 'A',
                    'Q': 'D',
                    'K': 'R',
                    'P': 'P',

                    'r': 'T',
                    'n': 'C',
                    'b': 'A',
                    'q': 'D',
                    'k': 'R',
                    'p': 'P',
                    ' ': ' '    }
        
        return  a_sp[pieza]


def traduce_ing(idioma,pieza):

    if idioma == 'sn':
        if pieza[1] == COLOR_PIEZA_BLANCA:
            
            a_ing = {   '♜': 'R',
                        '♞': 'N',
                        '♝': 'B',
                        '♛': 'Q',
                        '♚': 'K',
                        '♟': 'P',
                        ' ': ' '    }
        if pieza[1] == COLOR_PIEZA_NEGRA:
                    
            a_ing = {   '♜': 'r',
                        '♞': 'n',
                        '♝': 'b',
                        '♛': 'q',
                        '♚': 'k',
                        '♟': 'p',
                        ' ': ' '    }

        return a_ing[pieza[0]]
     
