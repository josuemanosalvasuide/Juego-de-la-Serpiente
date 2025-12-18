from motor import iniciar_ventana, eventos, actualizar, tick, cerrar, cargar_imagen
from assets import cargar_assets
from game_over import dibujar_game_over, detectar_click_game_over
import menu
import pantallas
import snake_game

nivel = 1  # 1=facil, 2=medio, 3=dificil

def main():
    global nivel

    pantalla, reloj = iniciar_ventana("Snake - Menú")
    assets = cargar_assets()

    boton_imagen = cargar_imagen("boton.png", (220, 60))

    snake_sprites = {
        "cabeza"  : cargar_imagen("cabeza.png", (20, 20)),
        "cuerpo"  : cargar_imagen("cuerpo.png", (20, 20)),
        "curva_dr": cargar_imagen("curva_dl.png", (20, 20)),
        "curva_dl": cargar_imagen("curva_dr.png", (20, 20)),
        "curva_ur": cargar_imagen("curva_ul.png", (20, 20)),
        "curva_ul": cargar_imagen("curva_ur.png", (20, 20)),
        "cola"    : cargar_imagen("cola.png", (20, 20)),
        "manzana" : cargar_imagen("manzana.png", (20, 20)),
    }

    estado = "menu"
    score = 0
    score_final = 0
    corriendo = True

    while corriendo:
        for e in eventos():
            if e.type == 256:  # QUIT
                corriendo = False

            # CLICK en botones del menú
            if estado == "menu" and e.type == 1025:  # MOUSEBUTTONDOWN
                mx, my = e.pos
                nuevo = menu.detectar_click(mx, my)
                if nuevo == "salir":
                    corriendo = False
                elif nuevo is not None:
                    estado = nuevo   # puede ser "juego", "reglas", "marcador", "nivel"

            # CLICK en selección de NIVEL
            if estado == "nivel" and e.type == 1025:  # MOUSEBUTTONDOWN
                mx, my = e.pos
                n = menu.detectar_click_nivel(mx, my)
                if n is not None:
                    nivel = n
                    estado = "juego"

            # CLICK en botones del GAME OVER
            if estado == "game_over" and e.type == 1025:  # MOUSEBUTTONDOWN
                mx, my = e.pos
                opcion = detectar_click_game_over(mx, my)
                if opcion == "reiniciar":
                    estado = "nivel"   # ✅ eliges nivel otra vez
                elif opcion == "menu":
                    estado = "menu"

            # ESC para volver al menú desde cualquier pantalla (menos el juego)
            if estado not in ("menu", "juego") and e.type == 768:  # KEYDOWN
                if e.key == 27:  # ESC
                    estado = "menu"

        # DIBUJO
        pantalla.blit(assets["fondo"], (0, 0))

        if estado == "menu":
            menu.dibujar(pantalla, boton_imagen)

        elif estado == "nivel":
            menu.dibujar_nivel(pantalla, boton_imagen)

        elif estado == "reglas":
            pantallas.reglas(pantalla)

        elif estado == "marcador":
            pantallas.marcador(pantalla, score)

        elif estado == "game_over":
            dibujar_game_over(pantalla, boton_imagen, score_final)

        elif estado == "juego":
            score, accion = snake_game.jugar(pantalla, reloj, assets, snake_sprites, nivel)

            if accion == "salir":
                corriendo = False
            else:
                score_final = score
                estado = "game_over"

        actualizar()
        tick(reloj)

    cerrar()

if __name__ == "__main__":
    main()
