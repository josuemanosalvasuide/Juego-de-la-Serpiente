import pygame

VENTANA_ANCHO = 600
VENTANA_ALTO = 600
FPS = 60

def iniciar_ventana(titulo="Juego de la serpiente"):
    pygame.init()
    pantalla = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))
    pygame.display.set_caption(titulo)
    reloj = pygame.time.Clock()
    return pantalla, reloj

def eventos():
    return pygame.event.get()

def cargar_imagen(nombre, escala):
    imagen = pygame.image.load("assets/" + nombre).convert_alpha()
    return pygame.transform.scale(imagen, escala)

def texto_fuente(tam=24):
    return pygame.font.SysFont("assets/front/editundo.ttf", tam)

def escribir(pantalla, texto, x, y, tam=24, color=(0, 0, 0)):
    fuente = texto_fuente(tam)
    imagen = fuente.render(texto, True, color)
    rect = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rect)

def actualizar():
    pygame.display.flip()

def tick(reloj):
    reloj.tick(FPS)

def cerrar():
    pygame.quit()

def rectangulo(pantalla, x, y, w, h, color):
    pygame.draw.rect(pantalla, color, (x, y, w, h), border_radius=10)

def click_dentro(mx, my, x, y, w, h):
    return x <= mx <= x + w and y <= my <= y + h

def dibujar_imagen (pantalla, imagen, x, y):
    pantalla.blit(imagen, (x, y))


