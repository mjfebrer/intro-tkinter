# import tkinter
# window = tkinter.Tk()
# window.title("Que hay en el estuche")
# window.geometry("300x300")


estuche = ["goma", "lapiz", "sacapuntas", "rotulador", "boli", "tipex"]

acertados = []

intento = 0
numero_intentos = 15

while intento < numero_intentos:
    if estuche == acertados:
        print("Has adivinado todas los componentes de estuche:-)")
        exit()
    adivina = input("Que crees que hay en el stuche (tienes " + str(numero_intentos - intento) + " intentos) ")
    if adivina in estuche:
        if adivina in acertados:
            intento = intento + 1
            print("Este está repetido, tienes un intento menos ")
        else:
            print("Si, " + adivina + " esta en el estuche")
            acertados.append(adivina)
        print(acertados)
    else:
        print("No esta en el estuche")
        intento += 1

print("No te quedan intentos :-(")




