import math
import tkinter

window = tkinter.Tk()
window.title("Multiplos")
window.geometry("300x300")

intro = tkinter.Label(text="Escribe dos numeros y calculara el M.C.D o M.C.M")
intro.pack()

numero1 = tkinter.Entry()
numero1.focus()
numero1.pack()

numero2 = tkinter.Entry()
numero2.pack()

def mcm():
    result['text'] = math.lcm(int(numero1.get()), int(numero2.get()))

def mcd():
    num1 = int(numero1.get())
    num2 = int(numero2.get())
    result['text'] = math.gcd(num1, num2)

mcm_button = tkinter.Button(window, text="M.C.M", command=mcm)
mcm_button.pack()

mcd_button = tkinter.Button(window, text="M.C.D", command=mcd)
mcd_button.pack()

result = tkinter.Label(window)
result["font"] = ("helvetica", 20)
result["fg"] = "orange"
result.pack()

window.mainloop()













