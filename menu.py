from motor import VENTANA_ANCHO, dibujar_imagen, escribir, click_dentro

BOTONES = [
    ("Iniciar juego", 190, 190, 220, 60, "juego"),
    ("Marcador",      190, 270, 220, 60, "marcador"),
    ("Reglas",        190, 350, 220, 60, "reglas"),
    ("Salir",         190, 430, 220, 60, "salir"),
]

def dibujar(pantalla, boton_imagen):
    escribir(pantalla, "MENU PRINCIPAL", VENTANA_ANCHO // 2, 140, 38)

    for boton in BOTONES:
        texto = boton[0]
        x = boton[1]
        y = boton[2]
        w = boton[3]
        h = boton[4]

        dibujar_imagen(pantalla, boton_imagen, x, y)
        escribir(pantalla, texto, x + w // 2, y + h // 2, 24)

def detectar_click(mx, my):
    for boton in BOTONES:
        x = boton[1]
        y = boton[2]
        w = boton[3]
        h = boton[4]
        estado = boton[5]

        if click_dentro(mx, my, x, y, w, h):
            return estado

    return None
