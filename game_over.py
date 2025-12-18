from motor import VENTANA_ANCHO, dibujar_imagen, escribir, click_dentro

BOTONES_GAMEOVER = [
    ("Reiniciar", 190, 320, 220, 60, "reiniciar"),
    ("Menu",      190, 400, 220, 60, "menu"),
]

def dibujar_game_over(pantalla, boton_imagen, puntaje):
    escribir(pantalla, "GAME OVER", VENTANA_ANCHO // 2, 160, 42)
    escribir(pantalla, f"Puntaje: {puntaje}", VENTANA_ANCHO // 2, 230, 28)

    for boton in BOTONES_GAMEOVER:
        texto = boton[0]
        x = boton[1]
        y = boton[2]
        w = boton[3]
        h = boton[4]

        dibujar_imagen(pantalla, boton_imagen, x, y)
        escribir(pantalla, texto, x + w // 2, y + h // 2, 24)

def detectar_click_game_over(mx, my):
    for boton in BOTONES_GAMEOVER:
        x = boton[1]
        y = boton[2]
        w = boton[3]
        h = boton[4]
        estado = boton[5]

        if click_dentro(mx, my, x, y, w, h):
            return estado

    return None
