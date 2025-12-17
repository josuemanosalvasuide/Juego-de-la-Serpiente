from motor import iniciar_ventana, eventos, actualizar, tick, cerrar, cargar_imagen
from assets import cargar_assets
import menu
import pantallas
import snake_game

def main():
    pantalla, reloj = iniciar_ventana("Snake - Menú")
    assets = cargar_assets()

    boton_imagen = cargar_imagen("boton.png", (220, 60))

    estado = "menu"
    score = 0
    corriendo = True

    while corriendo:
        for e in eventos():
            if e.type == 256:  # QUIT
                corriendo = False

            # CLICK en botones solo en el menú
            if estado == "menu" and e.type == 1025:  # MOUSEBUTTONDOWN
                mx, my = e.pos
                nuevo = menu.detectar_click(mx, my)   # <- devuelve "juego", "marcador", "reglas", "salir"
                if nuevo == "salir":
                    corriendo = False
                elif nuevo is not None:
                    estado = nuevo

            # ESC para volver al menú desde cualquier pantalla
            if estado != "menu" and e.type == 768:  # KEYDOWN
                if e.key == 27:  # ESC
                    estado = "menu"

        # DIBUJO
        pantalla.blit(assets["fondo"], (0, 0))

        if estado == "menu":
            menu.dibujar(pantalla,boton_imagen)
        elif estado == "reglas":
            pantallas.reglas(pantalla)
        elif estado == "marcador":
            pantallas.marcador(pantalla, score)
        elif estado == "juego":
            snake_game.dibujar_juego(pantalla, score)

        actualizar()
        tick(reloj)

    cerrar()

if __name__ == "__main__":
    main()
