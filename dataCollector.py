import cv2
import numpy as np
import math
import time

# captura da webcam
cap = cv2.VideoCapture(0)

# variável que comporta a informação de margem que a câmera capturará
offset = 20

# tamanho da imagem depois de redimensionada
imgSize = 300

# definição da pasta em que ficarão as imagens das mãos
folder = "Data/Obama"

# variável contadora para controle das fotos tiradas
counter = 0

# loop de repetição
while True and counter <= 15:

    # leitura do frame
    success, img = cap.read()

    # posicionamento do objeto mão nas mãos do usuário


    # exibição da imagem toda
    cv2.imshow("Image", img)

    # tecla apertada do teclado
    key = cv2.waitKey(1)

    # se a tecla apertada for s, ele salva a foto
    if key == ord("s"):

        # aumento do contador
        counter += 1

        # salvamento da imagem
        cv2.imwrite(f'{folder}/Image_{counter}.jpg', img)
        # cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', img)

        # impressão do contador
        print(counter)
    
    elif key == ord('q'):
        
        break