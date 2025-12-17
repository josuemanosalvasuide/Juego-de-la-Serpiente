from motor import VENTANA_ANCHO, escribir

def dibujar_juego(pantalla, score):
    escribir(pantalla, "INICIO DEL JUEGO (AVANCE)", VENTANA_ANCHO//2, 120, 32)
    escribir(pantalla, f"Score: {score}", VENTANA_ANCHO//2, 180, 28)
    escribir(pantalla, "Presiona ESC para volver", VENTANA_ANCHO//2, 450, 22)
