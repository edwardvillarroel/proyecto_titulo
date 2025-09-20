from camera import iniciar_camara, mostrar_video, liberar_camara


def main():
    cap=iniciar_camara()
    try:
        mostrar_video(cap)
    finally:
        liberar_camara(cap)

if __name__=="__main__":
    main()