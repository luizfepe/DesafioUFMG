import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

#import functools
mousePos = (1,2)
coords = (0,0)
resultado = np.float32([[1,1]])
clear = lambda: os.system('cls')


def transforma(pt, dst1, dst2): #aplica perspectiva e printa pontos
    a = np.array(pt, dtype='float32')
    h = np.array(dst1, dtype='float32')
    a = np.array([a])
    print(" - - -- - ------")
    print(a)
    print(type(a))
    print(" - - -- - ------")
    print(type(h))
    print(h)
    pointsOut = cv2.perspectiveTransform(a, h)

    a = pointsOut
    h = np.array(dst2, dtype='float32')
    #a = np.array([a])	
    coordsOut = cv2.perspectiveTransform(a, h)
    coords = coordsOut	
    plot1.suptitle(str(coords), fontsize=12, ha="left")
    '''
    clear()
    
    print(" ")
    print(" ")
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("CLICK nos pixels na imagem FOTO:")
    print(pt)	
    print(".")
    print("Pixel correspondente na imagem MAPA:")
    print(pointsOut)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    #print(a)
    print(" ")
    print("Coordenada correspondente ao pixel:")
    print(coordsOut)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print(" ")
    '''
	
def InitPerspectiva():
    ptsFoto = np.float32([[552,478],[220,148],[660,103],[412,118]])
    ptsMapa = np.float32([[657,760],[418,496],[493,55],[368,241]])
    return ptsFoto, ptsMapa

'''	
def InitHomografia():
    ptsFoto = np.float32([[552,478],[220,148],[660,103],[412,118]])
    ptsMapa = np.float32([[657,760],[418,496],[493,55],[368,241]])
    return ptsFoto, ptsMapa
'''
	
def coordConversao():
    pixMapa = np.float32([[657,760],[418,496],[493,55],[368,241]])
    #pixMapa = np.float32([[760,657],[496,418],[55,493],[241,368]])
    coords = np.float32([[-43.975112,-19.884362],[-43.978154,-19.880996],[-43.978796,-19.75391],[-43.978796,-19.877751]])
    #coords = np.float32([[-19.885087,-43.974836],[-19.884362,-43.975112],[-19.880996,-43.978154],[-19.875391,-43.978796]])	
    return pixMapa, coords

foto = cv2.cv2.imread('cameraview.png')
pts = cv2.cv2.imread('points.png')
mapa = cv2.cv2.imread('cmap.png')
#rows,cols,ch = mapa.shape




ptsFoto, ptsMapa = InitPerspectiva()
pixMapa, latLong = coordConversao()

matFotoMapa = cv2.getPerspectiveTransform(ptsFoto,ptsMapa,cv2.DECOMP_LU) #CALCULA MATRIZ DE TRANSFORM
matMapaFoto = cv2.getPerspectiveTransform(ptsMapa, ptsFoto,cv2.DECOMP_LU) #CALCULA MATRIZ DE TRANSFORM
matCoordenadas = cv2.getPerspectiveTransform(pixMapa,latLong,cv2.DECOMP_LU) #CALCULA MATRIZ DE TRANSFORM das coordenadas
#print("MAT TRANSFORM PERSPECTIVA. FORMADO NP.FLOAT32")
#print(matPerspectiva)


'''
#TESTE COM HOMOGRAFIA
#matHomografia = cv2.findHomography(ptsFoto,ptsMapa)
#print("MAT TRANSFORM HOMOGRAFIA. FORMATO ARRAY")
#print(matHomografia)
#dst = cv2.warpPerspective(pts,MatrizPerspectiva,(800,600)) #aplica perspectiva a uma imagem
'''
'''
TESTE DE PONTOS
transforma([[510,523]], matPerspectiva) #FUMAÇA
transforma([[546,117]], matPerspectiva)
transforma([[510,238]], matPerspectiva)
transforma([[412,118]], matPerspectiva)
plt.subplot(121),plt.imshow(foto[:,:,::-1]),plt.title('Foto')
plt.subplot(122),plt.imshow(mapa[:,:,::-1]),plt.title('Mapa')
plt.show()
'''

plt.style.use('seaborn-white')
plot1, ax = plt.subplots(1,2, squeeze=False) #Squeeze=False força ax a receber um vetor de 2 dimensões para endereçar os eixos do plot
#plot2, img2 = plt.subplots()


ax[0, 0].imshow(foto[:,:,::-1]) #muda de RGB PRA BGR
ax[0, 0].set_title('FOTO')
ax[0, 1].imshow(mapa[:,:,::-1])
ax[0, 1].set_title('MAPA') 


'''
plt.subplot(1,2,1)
plt.imshow(foto[:,:,::-1])
plt.title('FOTO')

plt.subplot(1,2,2)
plt.imshow(mapa[:,:,::-1])
plt.title('MAPA')
'''
def onclick(event):
    mousePos = event.xdata, event.ydata
    a = np.array(mousePos, dtype='float32')
    a = np.array([a])
    
    print(event.inaxes)
    print(event.canvas.figure)    
    o, p = mousePos
    mousePosTxt = [round(o,1), round(p,1)]
    ax[0, 0].set_title(mousePosTxt)
    transforma(a, matFotoMapa, matCoordenadas)
    print(type(a))
    plot1.suptitle(str(coords), fontsize=12)
    plt.show()

cid = plot1.canvas.mpl_connect('button_press_event', onclick)
#cid = plot2.canvas.mpl_connect('button_press_event', onclick)

plt.tight_layout()
plot1.tight_layout()
plt.show()
k = cv2.waitKey(0)
if k==27:    # Esc key to stop
    cv2.destroyAllWindows()



