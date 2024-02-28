import tkinter

window = tkinter.Tk()
window.geometry("300x600")
window.title("Prueba")

intro = tkinter.Label(window, text="¡Escribe x numeros y escoge una operación")
intro.pack()

Pantalla = tkinter.Label(window)
Pantalla.pack()


def button_click(number):
    Pantalla["text"] = Pantalla.cget("text") + str(number)


buttons = {}

for number in range(1, 10):
    buttons[number] = tkinter.Button(window, text=str(number), command=lambda n=number: button_click(n))
    buttons[number].pack()


def add():
    Pantalla["text"] = Pantalla.cget("text") + "+"


def subtract():
    Pantalla["text"] = Pantalla.cget("text") + "-"


def multiply():
    Pantalla["text"] = Pantalla.cget("text") + "*"


def divide():
    Pantalla["text"] = Pantalla.cget("text") + "/"


add_button = tkinter.Button(window, text="+", command=add, bg = "pink")
add_button.pack()

subtract_button = tkinter.Button(window, text="-", command=subtract, bg = "pink")
subtract_button.pack()

multiply_button = tkinter.Button(window, text="x", command=multiply, bg = "pink")
multiply_button.pack()

divide_button = tkinter.Button(window, text="/", command=divide, bg = "pink")
divide_button.pack()


def result():
    Pantalla["text"] = eval(Pantalla.cget("text"))


result_button = tkinter.Button(window, text="=", command=result, bg = "orange")
result_button.pack()

result_button = tkinter.Button(window, text="=", command=result, bg="orange")
result_button.grid(row=1, column=0)

window.mainloop()
