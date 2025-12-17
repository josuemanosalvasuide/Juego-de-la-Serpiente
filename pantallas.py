from motor import VENTANA_ANCHO, VENTANA_ALTO, escribir

def reglas(pantalla):
    escribir(pantalla, "REGLAS", VENTANA_ANCHO//2, 120, 36)
    escribir(pantalla, "1) No chocar con las paredes", VENTANA_ANCHO//2, 220, 24)
    escribir(pantalla, "2) Comer la comida para ganar puntos", VENTANA_ANCHO//2, 260, 24)
    escribir(pantalla, "3) No chocar contigo mismo", VENTANA_ANCHO//2, 300, 24)
    escribir(pantalla, "ESC para volver al menú", VENTANA_ANCHO//2, 500, 22)

def marcador(pantalla, score):
    escribir(pantalla, "MARCADOR", VENTANA_ANCHO//2, 140, 36)
    escribir(pantalla, f"Puntos: {score}", VENTANA_ANCHO//2, 260, 30)
    escribir(pantalla, "ESC para volver al menú", VENTANA_ANCHO//2, 500, 22)
