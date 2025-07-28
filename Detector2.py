# ==============================================================================
#                 DETECTOR DE OBJETOS CON HSV FIJO Y CÁLCULO DE ÁREA
# ==============================================================================
#
# Descripción:
# ------------
# Este programa utiliza OpenCV en Python para detectar objetos en tiempo real
# a través de una cámara web, basándose en un rango de colores en el espacio HSV.
#
# A diferencia de la versión anterior con trackbars, este script utiliza valores
# fijos de umbralización HSV previamente calibrados. El sistema identifica los
# objetos que se encuentran dentro del rango definido y dibuja un rectángulo rojo
# alrededor del objeto detectado, además de mostrar su área en consola.
#
# También se descartan objetos con área muy pequeña para evitar ruido.
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
# 1.1
#
# Dependencias:
# -------------
# - Python 3.12
# - OpenCV-Python (`pip install opencv-python`)
# - NumPy (`pip install numpy`)
#
# Modo de uso:
# ------------
# 1. Ejecutar el script desde la terminal: `python deteccion_objeto_hsv.py`
# 2. Observar en la ventana "Frame Original" los objetos resaltados.
# 3. En la consola se imprimirá el área del objeto detectado.
# 4. Presionar la tecla 'Esc' para cerrar el programa.
#
# ==============================================================================

import cv2
import numpy as np

# --- Parámetros HSV obtenidos previamente ---
H_min, S_min, V_min = 0, 38, 100
H_max, S_max, V_max = 30, 220, 255

# Umbral de área mínima para ignorar objetos pequeños
area_minima = 500

# Inicia la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Conversión a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear máscara con los valores HSV definidos
    lower = np.array([H_min, S_min, V_min])
    upper = np.array([H_max, S_max, V_max])
    mask = cv2.inRange(hsv, lower, upper)

    # Filtrado y detección de contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > area_minima:
            #print(f"Área detectada: {area}")
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            coord_text = f"({x}, {y})"
            cv2.putText(frame, coord_text, (x - 25, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, "Objeto", (x - 25, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 155, 155), 2)

    # Mostrar resultados
    cv2.imshow("Detector HSV", frame)
    cv2.imshow("Mascara", mask)

    # Salida con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
