import tkinter

window = tkinter.Tk()
window.geometry("300x300")

intro = tkinter.Label(window, text="¡Escribe dos números y escoge una operación")
intro.pack()

text_box_1 = tkinter.Entry(window)
text_box_1.focus()
text_box_1.pack()

text_box_2 = tkinter.Entry(window)
text_box_2.pack()


def add():
    result["text"] = int(text_box_1.get()) + int(text_box_2.get())


def subtract():
    result["text"] = int(text_box_1.get()) - int(text_box_2.get())


def multiply():
    result["text"] = int(text_box_1.get()) * int(text_box_2.get())


def divide():
    result["text"] = int(text_box_1.get()) / int(text_box_2.get())


add_button = tkinter.Button(window, text="+", command=add)
add_button.pack()

subtract_button = tkinter.Button(window, text="-", command=subtract)
subtract_button.pack()

multiply_button = tkinter.Button(window, text="x", command=multiply)
multiply_button.pack()

divide_button = tkinter.Button(window, text="/", command=divide)
divide_button.pack()

result = tkinter.Label(window)
result["font"] = ("helvetica", 20)
result["fg"] = "blue"
result.pack()

window.mainloop()
