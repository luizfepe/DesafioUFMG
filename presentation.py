import numpy as np
import cv2
from matplotlib import pyplot as plt
#import os

class Pontos:
    def __init__(self, pts, desc):
        self.pts = np.float32(pts)
        self.descricao = desc
        #print(self.__dict__)
        #print("............................")
    def getMatrizTransformacao(self, matDist):
        m = cv2.getPerspectiveTransform(self.pts,matDist.pts,cv2.DECOMP_LU)
        return m
        
def applyPerspectiva(ponto, matTransf):
    pt =  np.array([[ponto]])
    mat = np.array(matFotoMapa.pts, dtype='float32')
    persp = cv2.perspectiveTransform(pt, mat)
    return persp
    
def onclick(event):
    mousePos = np.array([event.xdata, event.ydata], dtype='float32')
    mousePosTxt = round(mousePos[0],1), round(mousePos[1],1)
    print(mousePosTxt)
    print("MATRIZ TRANSFORMADA:")
    print(applyPerspectiva(mousePos, matMapaFoto))
    
    
    pointsOut = 0

    ax[0, 0].set_title(mousePosTxt)
    ax[0, 1].set_title(mousePosTxt)
    #transforma(a, matFotoMapa, matCoordenadas)

    plot1.suptitle(str(coords), fontsize=12)
    plt.show()





#DADOS INFORMADOS NO PROBLEMA: PIXELS E COORDENADAS
foto = Pontos([[552,478],[220,148],[660,103],[412,118]], "Pixels ABCE na Foto") 
mapa = Pontos([[657,760],[418,496],[493,55],[368,241]], "Pixels ABCE no Mapa")   
coords = Pontos([[-19.885087,-43.974836],[-19.884362,-43.975112],[-19.880996,-43.978154],[-19.875391,-43.978796]], "Coordenadas geograficas dos pontos ABCE")
#MATRIZES DE TRANSFORMAÇÃO
matFotoMapa = Pontos(foto.getMatrizTransformacao(mapa), "Matriz de Transformação FOTO -> MAPA")
matMapaFoto = Pontos(mapa.getMatrizTransformacao(foto), "Matriz de Transformação MAPA -> FOTO")
matMapaCoord = Pontos(mapa.getMatrizTransformacao(coords), "MAtriz de Transformação MAPA -> Coordenada")



#MATPLOTLIB:
foto = cv2.cv2.imread('cameraview.png')
pts = cv2.cv2.imread('points.png')
mapa = cv2.cv2.imread('cmap.png')
plt.style.use('seaborn-white')
plot1, ax = plt.subplots(1,2, squeeze=False) #Squeeze=False força ax a receber um vetor de 2 dimensões para endereçar os eixos do plot
ax[0, 0].imshow(foto[:,:,::-1]) #muda de RGB PRA BGR
ax[0, 0].set_title('FOTO')
ax[0, 1].imshow(mapa[:,:,::-1])
ax[0, 1].set_title('MAPA') 
cid = plot1.canvas.mpl_connect('button_press_event', onclick)

plt.show()






'''
    def __init__(self, a, b, c, e, desc):
        self.a = np.float32(a)
        self.b = np.float32(b)
        self.c = np.float32(c)
        self.e = np.float32(e)
        self.pts = npfloat32(a,b,c,e)
        self.descricao = desc
        '''

'''
    a = np.array(mousePos, dtype='float32')
    print(" - - -- - ------")
    print(a)
    print(type(a))
    print(" - - -- - ------")
    a = np.array([a]) 
    a = np.array([a])
    print(a)    
    print(type(a))
    print(" - - -- - ------")
    print(type(matMapaCoord.pts))
    print(matMapaCoord.pts)
    print(applyPerspectiva(a, matMapaCoord)
    '''