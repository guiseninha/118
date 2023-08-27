import cv2


# Crie nosso classificador de corpos
body_clasifier = cv2.CascadeClasifier('haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
   #  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 #   body_classifier.detectMultiScale()

    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    
    # Passe o quadro para nosso classificador de corpos
bodies = body_clasifier.detectMultiScale(gray,1.2,)
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    

if cv2.waitKey(1) == 32: #32 é a barra de espaço
       

 cap.release()
cv2.destroyAllWindows()
