# Detector de Objetos con Umbralización HSV

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10-green?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

## Descripción

Este proyecto es un **detector de objetos en tiempo real** desarrollado en Python utilizando la biblioteca OpenCV. La detección se basa en la **umbralización de color en el espacio HSV (Matiz, Saturación, Valor)**. Es una herramienta interactiva que permite a los usuarios ajustar dinámicamente los rangos de color mediante barras deslizadoras (trackbars) para aislar objetos específicos en el *feed* de una cámara web.

Una vez que un objeto es segmentado por su color, el programa identifica su contorno, dibuja un **rectángulo delimitador** alrededor de él y marca su **centroide** con un círculo, ofreciendo una visualización clara de la posición del objeto.

## Características

* **Detección de objetos en tiempo real**: Utiliza la cámara web para procesar video en vivo.
* **Umbralización HSV interactiva**: Ajusta los valores de Matiz, Saturación y Valor en tiempo real usando trackbars para una segmentación de color precisa.
* **Visualización de máscara HSV**: Muestra la imagen binaria resultante de la umbralización (objeto en blanco, fondo en negro).
* **Contorno y centroide**: Calcula y dibuja el contorno del objeto detectado, un rectángulo delimitador y su centro.
* **Fácil de usar**: Interfaz intuitiva para configurar los parámetros de detección.

## Requisitos

Asegúrate de tener instalados los siguientes componentes:

* **Python 3.12** o superior
* **OpenCV-Python**: `pip install opencv-python`
* **NumPy**: `pip install numpy`

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/Patny1/hsv_object_detector
    cd hsv_object_detector

    ```

2.  **Instala las dependencias:**

    ```bash
    pip install opencv-python numpy
    ```

## Modo de Uso

1.  **Ejecuta el script:**

    ```bash
    python hsv_object_detector.py
    ```

2.  Se abrirán tres ventanas:
    * **`Frame Original`**: Muestra el *feed* de la cámara web con el objeto detectado, su contorno y centroide.
    * **`Mascara HSV`**: Muestra la imagen binaria (blanco y negro) resultante de la umbralización HSV. Aquí es donde verás si el objeto de interés está correctamente aislado.
    * **`Trackbars`**: Contiene las barras deslizadoras para ajustar los valores `Hue Min/Max`, `Sat Min/Max` y `Val Min/Max`.

3.  **Ajusta los valores en la ventana "Trackbars"**:
    * Mueve los deslizadores hasta que el objeto que deseas detectar aparezca en **blanco puro** sobre un fondo **negro** en la ventana **`Mascara HSV`**.
    * Observa cómo el rectángulo rojo y el círculo se ajustan al objeto en la ventana **`Frame Original`**.

4.  **Para salir**: Presiona la tecla `Esc` en cualquier momento.

## Autor

**Paty Constante**

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
