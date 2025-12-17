import turtle
import time

ventana = turtle.Screen()
ventana.title("Juego de la Serpiente - Avance")
ventana.bgcolor("white")
ventana.setup(600, 600)

# -------- MENÚ EN CICLO --------
seguir_menu = True

while seguir_menu:

    print("===== MENU PRINCIPAL =====")
    print("1. Iniciar Juego")
    print("2. Marcador")
    print("3. Reglas")
    print("4. Reiniciar")
    print("5. Salir del juego")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        texto = turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(0, 200)
        texto.write("INICIO DEL JUEGO (AVANCE)")
        time.sleep(5)
        texto.clear()
        


    elif opcion == 2:
        print("Mostrando marcador...")
        texto = turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(0, 0)
        texto.write("MARCADOR (en construccion)")
        time.sleep(5)
        texto.clear()

    elif opcion == 3:
        print("Mostrando reglas...")
        texto = turtle.Turtle()
        texto.hideturtle()
        texto.penup()
        texto.goto(0, 50)
        texto.write("REGLAS DEL JUEGO")
        texto.goto(0, 10)
        texto.write("1. No chocar con las paredes")
        texto.goto(0, -20)
        texto.write("2. Comer la comida para ganar puntos")
        texto.goto(0, -50)
        texto.write("3. No chocar contigo mismo")
        time.sleep(5)
        texto.clear()

    elif opcion == 4:
        print("Reiniciando juego..")
        turtle.clearscreen()
        

    elif opcion == 5:
        print("Saliendo del juego...")
        seguir_menu = False
        ventana.bye() 

    else:
        print("Opcion incorrecta")

ventana.mainloop()


#### nuevo test ####