import random
import pygame
from motor import VENTANA_ANCHO, VENTANA_ALTO, eventos, actualizar, tick, escribir

SQUARE_SIZE = 20
BORDE = 50
BORDE_COLISION = 50

def iniciar_estado():
    serpiente = [(310, 310), (290, 310), (270, 310)]
    direccion = (1, 0)
    comida = generar_comida(serpiente)
    puntaje = 0
    return serpiente, direccion, comida, puntaje

def generar_comida(serpiente):
    while True:
        x = random.randrange(BORDE, BORDE + 400, SQUARE_SIZE)
        y = random.randrange(BORDE, BORDE + 400, SQUARE_SIZE)
        if (x, y) not in serpiente:
            return (x, y)

def cambiar_direccion(tecla, direccion_actual):
    dx, dy = direccion_actual

    if tecla == pygame.K_UP and (dx, dy) != (0, 1):
        return (0, -1)
    if tecla == pygame.K_DOWN and (dx, dy) != (0, -1):
        return (0, 1)
    if tecla == pygame.K_RIGHT and (dx, dy) != (-1, 0):
        return (1, 0)
    if tecla == pygame.K_LEFT and (dx, dy) != (1, 0):
        return (-1, 0)

    return direccion_actual


def sprite_cabeza(direccion, sprites):
    dx, dy = direccion
    cabeza = sprites["cabeza"]

    if (dx, dy) == (-1, 0):
        return cabeza
    if (dx, dy) == (1, 0):
        return pygame.transform.flip(cabeza, True, False)
    if (dx, dy) == (0, -1):
        return pygame.transform.rotate(cabeza, -90)
    if (dx, dy) == (0, 1):
        return pygame.transform.rotate(cabeza, 90)

    return cabeza

def direccion_entre(a, b):
    ax, ay = a
    bx, by = b

    if ax == bx:
        return "arriba" if ay > by else "abajo"
    if ay == by:
        return "izquierda" if ax > bx else "derecha"

def sprite_cuerpo(prev, actual, next_, sprites):
    if next_ is None:
        d = direccion_entre(actual, prev)
        base = sprites["cola"]

        if d == "derecha":
            return pygame.transform.flip(base, True, False)
        if d == "arriba":
            return pygame.transform.rotate(base, -90)
        if d == "abajo":
            return pygame.transform.rotate(base, 90)
        return base

    d1 = direccion_entre(actual, prev)
    d2 = direccion_entre(actual, next_)

    # curvas
    if ("abajo" in (d1, d2)) and ("derecha" in (d1, d2)):
        return sprites["curva_ul"]
    if ("abajo" in (d1, d2)) and ("izquierda" in (d1, d2)):
        return sprites["curva_ur"]
    if ("arriba" in (d1, d2)) and ("derecha" in (d1, d2)):
        return sprites["curva_dl"]
    if ("arriba" in (d1, d2)) and ("izquierda" in (d1, d2)):
        return sprites["curva_dr"]

    # recto vertical
    if ("arriba" in (d1, d2)) or ("abajo" in (d1, d2)):
        return pygame.transform.rotate(sprites["cuerpo"], 90)

    return sprites["cuerpo"]

def mover_serpiente(serpiente, direccion):
    dx, dy = direccion
    x, y = serpiente[0]
    nueva_cabeza = (x + dx * SQUARE_SIZE, y + dy * SQUARE_SIZE)
    serpiente.insert(0, nueva_cabeza)
    return nueva_cabeza

def colision_pared(pos):
    x, y = pos
    return (
        x < BORDE_COLISION or
        x >= VENTANA_ANCHO - BORDE_COLISION or
        y < BORDE_COLISION or
        y >= VENTANA_ALTO - BORDE_COLISION
    )

def colision_cuerpo(cabeza, serpiente):
    return cabeza in serpiente[1:]

def dibujar(pantalla, assets, sprites, serpiente, comida, puntaje, direccion, pausado=False):
    pantalla.blit(assets["fondo"], (0, 0))
    pantalla.blit(sprites["manzana"], comida)

    for i in range(len(serpiente)):
        x, y = serpiente[i]

        if i == 0:
            pantalla.blit(sprite_cabeza(direccion, sprites), (x, y))

        elif i == len(serpiente) - 1:
            prev = serpiente[i - 1]
            actual = serpiente[i]
            pieza = sprite_cuerpo(prev, actual, None, sprites)
            pantalla.blit(pieza, (x, y))

        else:
            prev = serpiente[i - 1]
            actual = serpiente[i]
            next_ = serpiente[i + 1]
            pieza = sprite_cuerpo(prev, actual, next_, sprites)
            pantalla.blit(pieza, (x, y))

    escribir(pantalla, f"Puntaje: {puntaje}", 80, 20, 20, (255, 255, 255))

    if pausado:
        escribir(pantalla, "PAUSA (P)", VENTANA_ANCHO // 2, 520, 22)

    actualizar()

def jugar(pantalla, reloj, assets, sprites, nivel=1):
    serpiente, direccion, comida, puntaje = iniciar_estado()
    pausado = False
    velocidad = 8

    while True:
        for e in eventos():
            if e.type == 256:
                return puntaje, "salir"

            if e.type == 768:
                if e.key == 27:
                    return puntaje, "menu"

                if e.key == pygame.K_p:
                    pausado = not pausado

                if not pausado:
                    direccion = cambiar_direccion(e.key, direccion)

        if pausado:
            dibujar(pantalla, assets, sprites, serpiente, comida, puntaje, direccion, pausado=True)
            reloj.tick(velocidad)  
            continue

        cabeza = mover_serpiente(serpiente, direccion)

        if colision_pared(cabeza) or colision_cuerpo(cabeza, serpiente):
            return puntaje, "menu"

        if cabeza == comida:
            puntaje += 1
            velocidad += nivel  

            if velocidad > 30:  
                velocidad = 30

            comida = generar_comida(serpiente)
        else:
            serpiente.pop()

        dibujar(pantalla, assets, sprites, serpiente, comida, puntaje, direccion, pausado=False)
        reloj.tick(velocidad)
