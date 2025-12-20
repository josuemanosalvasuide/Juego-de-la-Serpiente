from motor import cargar_imagen, VENTANA_ANCHO, VENTANA_ALTO

def cargar_assets():
    return {
        "fondo": cargar_imagen("fondo.png", (VENTANA_ANCHO, VENTANA_ALTO))
    }
