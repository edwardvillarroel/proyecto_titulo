import cv2 as cv
import numpy as np
import time
import sys

def iniciar_camara(index=0, width=640, height=480):
    cap = cv.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("No se pudo abrir la cámara. Verifica el índice o los permisos.")
        
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def mostrar_video(cap):
    window_name = 'video frame'
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    def salir(_):
        cap.release()
        cv.destroyAllWindows()
        sys.exit(0)
    
    def capturar(frame):
        timestamp = int(time.time())
        filename = f"capture_{timestamp}.png"
        cv.imwrite(filename, frame)
        print(f"Imagen guardada como: {filename}")
    actions={
        'q': salir,
        's': capturar
    }
    while True:
        ret, frame = cap.read()
        
        if not ret:
            time.sleep(0.1)
            continue
        
        # Verificar si la ventana fue cerrada con la X ANTES de mostrar el frame
        try:
            window_prop = cv.getWindowProperty(window_name, cv.WND_PROP_VISIBLE)
            if window_prop < 1:
                break
        except cv.error:
            break
            
        cv.imshow(window_name, frame)
        
        key_pressed = cv.waitKey(1) & 0xFF
        
        if key_pressed != 255:  # 255 significa "ninguna tecla"
            if key_pressed == 27:  # tecla ESC
                break

            key = chr(key_pressed).lower()

            if key in actions:
                actions[key](frame)   

def liberar_camara(cap):
    cap.release()
    cv.destroyAllWindows()

