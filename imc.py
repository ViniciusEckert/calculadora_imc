from tkinter import *
from tkinter import ttk
from tkinter import messagebox

co1 = "#DCDCDC"
co2 = "#000000"
co3 = '#4F4F4F'

janela = Tk()
janela.title("IMC")
janela.geometry("450x430")
janela.configure(bg=co1)
janela.resizable(False, False)

frame_cima = Frame(janela, width=450, height=120, bg=co2, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela, width=450, height=430, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

l_nome = Label(frame_cima, text="IMC", height=5, anchor=NE, font=('Ivy 50 bold'), bg=co2, fg=co1)
l_nome.place(x=175, y=20)

l_peso = Label(frame_baixo, text="PESO:", height=5, anchor=NE, font=('Ivy 20'), bg=co1, fg=co2)
l_peso.place(x=20, y=30)
e_peso = Entry(frame_baixo, width=10, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_peso.place(x=120, y=35)

l_altura = Label(frame_baixo, text="ALTURA:", height=5, anchor=NE, font=('Ivy 20'), bg=co1, fg=co2)
l_altura.place(x=20, y=80)
e_altura = Entry(frame_baixo, width=10, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_altura.place(x=150, y=85)

def calc_imc():
    altura = float(e_altura.get())
    peso = float(e_peso.get())
    imc= peso/(altura*altura)

    if imc < 18.5:
        messagebox.showinfo('IMC',"Você está com abaixo do peso")
    elif imc < 24.9:
        messagebox.showinfo('IMC',"Você está com peso normal")
    elif imc < 29.9:
        messagebox.showinfo('IMC',"Você está com sobrepeso")
    elif imc < 34.9:
        messagebox.showinfo('IMC',"Você esta com obesidade grau 1")
    elif imc < 39.9:
        messagebox.showinfo('IMC',"Você está com obesidade grau 2")
    else:
        messagebox.showinfo('IMC',"Você está com obesidade grau 3")

botao_calcular = Button(frame_baixo, text="CALCULAR:", height=2, width=10, bg=co3, fg=co1, font=('Ivy 20'), relief="raised", command=calc_imc)
botao_calcular.place(x=150, y=200)


janela.mainloop()