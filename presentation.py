import numpy as np
import cv2
from matplotlib import pyplot as plt
#import os

class Pontos:
    def __init__(self, pts, desc):
        #print(self.__dict__)
        #print("............................")
        self.pts = np.float32(pts)
        self.descricao = desc
        print(self.descricao)
        print(self.pts)

        
    def getMatrizTransformacao(self, matDist):
        m = cv2.getPerspectiveTransform(self.pts,matDist.pts,cv2.DECOMP_LU)

        return m


def applyPerspectiva(ponto, matTransf): #Aplica a um ponto [x,y] a matriz de transformação
    pt =  np.array([[ponto]])
    mat = np.array(matTransf.pts, dtype='float32')
    persp = cv2.perspectiveTransform(pt, mat)

    print(" ")
    print(" - - - - - - - - - - - - - - - - - - - - ")
    print("RECEBEU O PONTO:")
    print(pt)
    print(" ")    
    print("RECEBEU A MATRIZ DE TRANSFORMAÇÃO:")
    print(mat)   
    print(" ") 
    

    print("RESULTADO EM:")
    print(persp) 
    print(" - - - - - - - - - - - - - - - - - - - - ")   
    print(" ")   
  

    return persp[0][0][0], persp[0][0][1]
    
    
def tamanhoCanvas(str): #Recebe um texto de canvas.figure e retorna hsize e vsize
    s =str.strip("Figure()")
    h, v = s.split("x")
    return float(h), float(v)
    
    
def mouseTxt(lista): #Recebe um lista de posição do mouse arredonda pra 1 decimal
    #print(lista.shape)
    #return np.round(lista[0],1), np.round(lista[1],1)
    arred =  str([np.round(x,1) for x in lista])
    return arred

    #COOOOOOOOOOOOOOOOOOONTINUAAAAAAAAAAAAAAAAR
    #https://stackoverflow.com/questions/31877353/overlay-an-image-segmentation-with-numpy-and-matplotlib
    
def onclick(event):
    if event.dblclick:
        print 
        click=0
        calc=1
        resultadoCoord = 0
        tamanho = str(event.canvas.figure)
        hsize, vsize = tamanhoCanvas(tamanho)  
        mousePos = np.array([event.xdata, event.ydata], dtype='float32')
        if float(event.x) > float(hsize/2):     #Click no mapa
            click=1
            calc=0
            conversao = applyPerspectiva(mousePos, matMapaFoto)
            resultadoCoord = applyPerspectiva(mousePos, matMapaCoord)
            #print(mousePos)
            #print(conversao)
        else:                                   #Click na foto
            click=0
            calc=1
            conversao = applyPerspectiva(mousePos, matFotoMapa)
            #print(conversao)
            resultadoCoord = applyPerspectiva(conversao, matMapaCoord)
        #resultado=applyPerspectiva(mapa, matMapaCoord)
        ax[0, click].set_title("Click: "+mouseTxt(mousePos))
        ax[0, calc].set_title("Resultado: "+mouseTxt(conversao))
        
        ax[0, click].text(mousePos[0],mousePos[1]," ",
        bbox={'facecolor': 'red', 'alpha': 0.6, 'pad': 0.05, 'boxstyle': 'circle'})
        ax[0, calc].text(conversao[0],conversao[1]," ", 
        bbox={'facecolor': 'green', 'alpha': 0.6, 'pad': 0.05,'boxstyle': 'circle'})
        plot1.suptitle("Coordenada: "+str(resultadoCoord), fontsize=16, ha='center' )
        plt.show() 
    if event.button == 3: 
        for t in ax[0,0].texts:
            t.set_visible(False)
        for t in ax[0,1].texts:
            t.set_visible(False)
        plt.show()

    #resultado = applyPerspectiva(mousePos, matFotoMapa)
    #print(str(mousePosTxt)+" -> "+str(resultado[0][0][0])+" , "+str(resultado[0][0][1]))
    #print(event)


    






#DADOS INFORMADOS NO PROBLEMA: PIXELS E COORDENADAS
foto = Pontos([[552,478],[220,148],[660,103],[412,118]], "Pixels ABCE na Foto") 
mapa = Pontos([[657,760],[418,496],[493,55],[368,241]], "Pixels ABCE no Mapa")   
coords = Pontos([[-43.974836,-19.885087],[-43.975112,-19.884362],[-43.978154,-19.880996],[-43.978796,-19.875391]], "Coordenadas geograficas dos pontos ABCE")
#CALC MATRIZES DE TRANSFORMAÇÃO
matFotoMapa = Pontos(foto.getMatrizTransformacao(mapa), "Matriz de Transformação FOTO -> MAPA")
matMapaFoto = Pontos(mapa.getMatrizTransformacao(foto), "Matriz de Transformação MAPA -> FOTO")
matMapaCoord = Pontos(mapa.getMatrizTransformacao(coords), "Matriz de Transformação MAPA -> Coordenada")
matFotoCoord = Pontos(foto.getMatrizTransformacao(coords), "Matriz de Transformação FOTO -> Coordenada")


#MATPLOTLIB: Plot Config
figFoto = cv2.cv2.imread('cameraview.png')
figMapa = cv2.cv2.imread('cmap.png')
plt.style.use('seaborn-white')
plot1, ax = plt.subplots(1,2, squeeze=False) #Squeeze=False força ax a receber um vetor de 2 dimensões para endereçar os eixos do plot
plot1.subplots_adjust(left=0.03, bottom=0.03, right=0.95, top=0.95, wspace=0.03, hspace=0.03)
ax[0, 0].imshow(figFoto[:,:,::-1]) #muda de RGB PRA BGR
ax[0, 0].set_title('FOTO')
ax[0, 1].imshow(figMapa[:,:,::-1])
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