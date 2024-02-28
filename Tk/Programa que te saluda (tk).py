import tkinter

window = tkinter.Tk()
window.geometry("300x300")

textBoxLabel = tkinter.Label(window)
textBoxLabel['text'] = '¡Escribe tu nombre!'
textBoxLabel.pack()

textBox = tkinter.Entry(window)
textBox.focus()
textBox.pack()

label = tkinter.Label(window)
label.pack()

def Textfromthebox():
    label["text"] = 'Hola ' + textBox.get()


Button1 = tkinter.Button(window, text="Click", command=Textfromthebox)
Button1.pack()

window.mainloop()










#label = tkinter.Label(window, text="hola josee", font=("Arial"), bg="green")
#label.pack()
#def saludos(nombre):
    #print("Holaaaaa " + nombre)
