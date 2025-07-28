# ==============================================================================
#                 DETECTOR DE OBJETOS CON UMBRALIZACIÓN HSV
# ==============================================================================
#
# Descripción:
# ------------
# Este programa utiliza OpenCV en Python para detectar objetos en tiempo real
# a través de una cámara web, basándose en un rango de colores en el espacio HSV.
#
# El script genera una ventana con barras de desplazamiento (trackbars) que
# permiten ajustar dinámicamente los valores de umbralización para Matiz (Hue),
# Saturación (Saturation) y Valor (Value).
#
# Una vez que un objeto es aislado por color, el programa calcula su contorno,
# dibuja un rectángulo rojo a su alrededor y marca su centroide con un círculo.
#
# Autor:
# ------
# Paty Constante
#
# Fecha de creación:
# ------------------
# 28 de julio de 2025
#
# Versión:
# --------
# 1.0
#
# Dependencias:
# -------------
# - Python 3.12
# - OpenCV-Python (`pip install opencv-python`)
# - NumPy (`pip install numpy`)
#
# Modo de uso:
# ------------
# 1. Ejecutar el script desde la terminal: `posicion.py`
# 2. Ajustar los valores en la ventana "Trackbars" hasta que el objeto de
#    interés aparezca en blanco sobre un fondo negro en la ventana "Mascara HSV".
# 3. Observar el resultado en la ventana "Frame Original".
# 4. Presionar la tecla 'Esc' para cerrar el programa.
#
# ==============================================================================
import cv2
import numpy as np

# Función de marcador de posición para los trackbars, no hace nada.
def nada(x):
    pass

# Inicializa la captura de video desde la cámara web (cámara integrada 0).
cap = cv2.VideoCapture(0)

# Crea una ventana para los trackbars.
cv2.namedWindow("Trackbars")

# Crea los trackbars para los valores HSV inferiores y superiores.
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nada)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nada)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nada)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nada)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nada)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nada)

while True:
    # Lee un fotograma de la cámara.
    ret, frame = cap.read()
    if not ret:
        break

    # Convierte el fotograma del espacio de color BGR a HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtiene los valores actuales de los trackbars.
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    # Define el rango inferior y superior de HSV para la umbralización.
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])

    # Crea una máscara aplicando el umbral al fotograma HSV.
    # Los píxeles dentro del rango se volverán blancos (255) y los demás negros (0).
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # Encuentra los contornos en la máscara.
    # cv2.RETR_EXTERNAL para los contornos exteriores.
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Procesa el contorno más grande.
    if contours:
        # Encuentra el contorno de mayor área.
        largest_contour = max(contours, key=cv2.contourArea)

        # Procesa solo si el área del contorno es suficientemente grande para evitar ruido.
        if cv2.contourArea(largest_contour) > 500:
            # Calcula el rectángulo delimitador para el contorno más grande.
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Dibuja un rectángulo rojo alrededor del objeto.
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Calcula los momentos del contorno para encontrar el centroide.
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                # Calcula las coordenadas X y Y del centroide.
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Dibuja un círculo para marcar el centroide.
                cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

                cv2.putText(frame, "Centroide", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                coord_text = f"({cX}, {cY})"
                cv2.putText(frame, coord_text, (cX - 25, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)



    # Muestra el fotograma original y la máscara.
    cv2.imshow("Frame Original", frame)
    cv2.imshow("Mascara HSV", mask)

    # Rompe el bucle si se presiona la tecla 'Esc'.
    key = cv2.waitKey(1)
    if key == 27:
        break

# Libera la captura de video y destruye todas las ventanas.
cap.release()
cv2.destroyAllWindows()