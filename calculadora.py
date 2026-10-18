import tkinter as tk

#Janela
root = tk.Tk()
root.geometry("300x275")
root.title("Calculator")
root.resizable(False, False)

#Frame de cima e frame de baixo
frame_head = tk.Frame(root, bg="black", width=300, height=50)
frame_body = tk.Frame(root, bg="gray", width=300, height=250)
frame_head.pack()
frame_body.pack()

all_values = ""

#Funções
def calc(valor):
    global all_values

    all_values = all_values + str(valor)
    text_value.set(all_values)

def calculate():
    try:
        answer = eval(all_values)
        text_value.set(answer)
    except ZeroDivisionError:
        text_value.set("ZeroDivisionError")
    except SyntaxError:
        text_value.set("InvalidEquation")


def clean():
    global all_values
    all_values = ""
    text_value.set("")



#Entrada
text_value = tk.StringVar()
label = tk.Label(frame_head, textvariable=text_value, width=42,height=2, bg="black", fg="white",
                 anchor="e", font=("Arial", 20))
label.pack()


#Botões
button1 = tk.Button(frame_body,command=clean, text="C", width=17, height=2)
button1.place(x=1, y=1)

button2 = tk.Button(frame_body,command=lambda: calc("%"), text="%", width=15, height=2)
button2.place(x=125, y=1)

button3 = tk.Button(frame_body,command=lambda: calc("*"), text="*", width=8, height=2, bg="orange")
button3.place(x=240, y=1)

button4 = tk.Button(frame_body,command=lambda: calc("1"), text="1", width=10, height=2)
button4.place(x=1, y=41)

button5 = tk.Button(frame_body,command=lambda: calc("2"), text="2", width=10, height=2)
button5.place(x=81, y=41)

button6 = tk.Button(frame_body,command=lambda: calc("3"), text="3", width=10, height=2)
button6.place(x=161, y=41)

button7 = tk.Button(frame_body,command=lambda: calc("/"), text="/", width=8, height=2, bg="orange")
button7.place(x=241, y=41)

button8 = tk.Button(frame_body,command=lambda: calc("4"), text="4", width=10, height=2)
button8.place(x=1, y=82)

button9 = tk.Button(frame_body,command=lambda: calc("5"), text="5", width=10, height=2)
button9.place(x=81, y=82)

button10 = tk.Button(frame_body,command=lambda: calc("6"), text="6", width=10, height=2)
button10.place(x=161, y=82)

button11 = tk.Button(frame_body,command=lambda: calc("+"), text="+", width=8, height=2, bg="orange")
button11.place(x=241, y=82)

button12 = tk.Button(frame_body,command=lambda: calc("7"), text="7", width=10, height=2)
button12.place(x=1, y=123)

button13 = tk.Button(frame_body,command=lambda: calc("8"), text="8", width=10, height=2)
button13.place(x=81, y=123)

button14 = tk.Button(frame_body,command=lambda: calc("9"), text="9", width=10, height=2)
button14.place(x=161, y=123)

button15 = tk.Button(frame_body,command=lambda: calc("-"), text="-", width=8, height=2, bg="orange")
button15.place(x=241, y=123)

button16 = tk.Button(frame_body,command=calculate, text="=", width=8, height=2, bg="orange")
button16.place(x=241, y=164)

button17 = tk.Button(frame_body,command=lambda: calc("0"), text="0", width=22, height=2)
button17.place(x=1, y=164)

button18 = tk.Button(frame_body,command=lambda: calc("."), text=".", width=10, height=2)
button18.place(x=161, y=164)

root.mainloop()
