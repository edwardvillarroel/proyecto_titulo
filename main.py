import cv2 as cv
import numpy as np
import time

def iniciar_camara(index=0, width=640, height=480):
    cap=cv.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("No se pudo abrir la cámara. Verifica el índice o los permisos.")
    
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def mostrar_video(cap):

    while True:
        ret,frame=cap.read()

        if ret==False:
            time.sleep(0.1)
            continue

        cv.imshow("video frame", frame)

        key_pressed = cv.waitKey(1) & 0xFF

        if key_pressed == ord('q'):
            break
        elif key_pressed == ord('s'):
            timestamp = int(time.time())
            cv.imwrite(f"capture_{timestamp}.png", frame)

def liberar_camara(cap):    
    cap.release()
    cv.destroyAllWindows()

def main():
    cap=iniciar_camara()
    try:
        mostrar_video(cap)
    finally:
        liberar_camara(cap)

if __name__=="__main__":
    main()