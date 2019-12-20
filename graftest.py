import numpy as np
import cv2
from matplotlib import pyplot as plt
#import os
    
def tamanhoCanvas(str): #Recebe um texto de canvas.figure e retorna hsize e vsize
    s =str.strip("Figure()")
    h, v = s.split("x")
    return float(h), float(v)

def onclick(event):
    if event.dblclick:
        click=0
        calc=1
        resultadoCoord = 0
        tamanho = str(event.canvas.figure)
        hsize, vsize = tamanhoCanvas(tamanho)  
        mousePos = np.array([event.xdata, event.ydata], dtype='float32')
        if float(event.x) > float(hsize/2):     #Click no mapa
            click=1
            calc=0
        else:                                   #Click na foto
            click=0
            calc=1

        #resultado=applyPerspectiva(mapa, matMapaCoord)
        ax[0, click].set_title("CLICOU NESSE")
        ax[0, calc].set_title("RESULTADO AQUI")
        plot1.suptitle(mousePos)
        plt.show()    
    #resultado = applyPerspectiva(mousePos, matFotoMapa)
    #print(str(mousePosTxt)+" -> "+str(resultado[0][0][0])+" , "+str(resultado[0][0][1]))
    #print(event.inaxes)
   






#MATPLOTLIB: Plot Config
figFoto = cv2.cv2.imread('cameraview.png')
figMapa = cv2.cv2.imread('cmap.png')
plt.style.use('seaborn-white')
plot1, ax = plt.subplots(1,2, squeeze=False) #Squeeze=False força ax a receber um vetor de 2 dimensões para endereçar os eixos do plot
plot1.subplots_adjust(left=0.03, bottom=0.03, right=0.95, top=0.95, wspace=0.03, hspace=0.03)
print(plot1.__dict__)
print(ax)
ax[0, 0].imshow(figFoto[:,:,::-1]) #muda de RGB PRA BGR
ax[0, 0].set_title('FOTO')
ax[0, 1].imshow(figMapa[:,:,::-1])
ax[0, 1].set_title('MAPA') 
cid = plot1.canvas.mpl_connect('button_press_event', onclick)

plt.show()
